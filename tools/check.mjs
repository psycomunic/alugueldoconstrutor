/* Validador do site. `npm run check`
   Sem dependencia. Confere o que costuma quebrar em site estatico:
   title/description, H1 unico, alt de imagem, dimensao de imagem,
   JSON-LD valido, canonical, links internos e arquivos referenciados. */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
let errors = 0, warns = 0;
const err = (f, m) => { console.log(`  \x1b[31mERRO\x1b[0m  ${f}: ${m}`); errors++; };
const warn = (f, m) => { console.log(`  \x1b[33mAVISO\x1b[0m ${f}: ${m}`); warns++; };

function htmlFiles(dir = ROOT, out = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (['node_modules', '.git', 'build', 'tools', 'assets', '.vercel'].includes(e.name)) continue;
    const p = path.join(dir, e.name);
    if (e.isDirectory()) htmlFiles(p, out);
    else if (e.name.endsWith('.html')) out.push(p);
  }
  return out;
}

const files = htmlFiles();
console.log(`\nValidando ${files.length} paginas...\n`);

const titles = new Map(), descs = new Map(), canons = new Set();

for (const file of files) {
  const rel = path.relative(ROOT, file).replace(/\\/g, '/');
  const html = fs.readFileSync(file, 'utf8');
  const dir = path.dirname(file);

  // ---- lang
  if (!/<html lang="pt-BR">/.test(html)) err(rel, 'falta lang="pt-BR" no <html>');

  // ---- title
  const t = html.match(/<title>([^<]*)<\/title>/);
  if (!t || !t[1].trim()) err(rel, 'sem <title>');
  else {
    const v = t[1].trim();
    if (v.length > 65) warn(rel, `title com ${v.length} caracteres (ideal ate 60)`);
    if (titles.has(v)) err(rel, `title duplicado (igual a ${titles.get(v)})`);
    titles.set(v, rel);
  }

  // ---- description
  const d = html.match(/<meta name="description" content="([^"]*)"/);
  if (!d || !d[1].trim()) err(rel, 'sem meta description');
  else {
    const v = d[1].trim();
    if (v.length > 165) warn(rel, `description com ${v.length} caracteres (ideal ate 158)`);
    if (v.length < 70) warn(rel, `description com apenas ${v.length} caracteres`);
    if (descs.has(v)) err(rel, `description duplicada (igual a ${descs.get(v)})`);
    descs.set(v, rel);
  }

  // ---- canonical
  const c = html.match(/<link rel="canonical" href="([^"]*)"/);
  if (!c) err(rel, 'sem canonical');
  else {
    if (canons.has(c[1]) ) err(rel, `canonical duplicado: ${c[1]}`);
    canons.add(c[1]);
    if (!/^https:\/\//.test(c[1])) err(rel, 'canonical nao e URL absoluta');
  }

  // ---- H1
  const h1 = html.match(/<h1[^>]*>/g) || [];
  if (h1.length === 0) err(rel, 'sem <h1>');
  if (h1.length > 1) err(rel, `${h1.length} <h1> na mesma pagina`);

  // ---- OG
  for (const p of ['og:title', 'og:description', 'og:url', 'og:image']) {
    if (!html.includes(`property="${p}"`)) err(rel, `falta ${p}`);
  }

  // ---- imagens
  const imgs = html.match(/<img\b[^>]*>/g) || [];
  for (const tag of imgs) {
    if (!/\balt=/.test(tag)) err(rel, `img sem alt: ${tag.slice(0, 80)}`);
    if (!/\bwidth=/.test(tag) || !/\bheight=/.test(tag)) {
      warn(rel, `img sem width/height (risco de CLS): ${tag.slice(0, 80)}`);
    }
    const src = (tag.match(/\bsrc="([^"]+)"/) || [])[1];
    if (src && !/^https?:/.test(src)) {
      const target = path.resolve(dir, src);
      if (!fs.existsSync(target)) err(rel, `imagem inexistente: ${src}`);
    }
  }

  // ---- JSON-LD
  const lds = [...html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)];
  if (lds.length === 0) warn(rel, 'sem JSON-LD');
  for (const m of lds) {
    try {
      const o = JSON.parse(m[1]);
      if (!o['@context']) err(rel, 'JSON-LD sem @context');
    } catch (e) {
      err(rel, `JSON-LD invalido: ${e.message}`);
    }
  }

  // ---- links internos
  const hrefs = [...html.matchAll(/\bhref="([^"]+)"/g)].map((m) => m[1]);
  for (const h of hrefs) {
    if (/^(https?:|mailto:|tel:|#|data:)/.test(h)) continue;
    const [clean] = h.split('#');
    if (!clean) continue;
    const target = path.resolve(dir, clean);
    if (!fs.existsSync(target)) err(rel, `link quebrado: ${h}`);
  }

  // ---- externo sem rel
  for (const m of html.matchAll(/<a\b[^>]*target="_blank"[^>]*>/g)) {
    if (!/rel="[^"]*noopener/.test(m[0])) warn(rel, `target=_blank sem rel=noopener: ${m[0].slice(0, 70)}`);
  }

  // ---- travessao em texto visivel
  const visible = html.replace(/<script[\s\S]*?<\/script>/g, '').replace(/<[^>]+>/g, ' ');
  if (/—/.test(visible)) warn(rel, 'travessao (—) em texto visivel; a convencao do projeto evita');
}

// ---- sitemap
const sm = path.join(ROOT, 'sitemap.xml');
if (!fs.existsSync(sm)) err('sitemap.xml', 'nao existe');
else {
  const locs = [...fs.readFileSync(sm, 'utf8').matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]);
  console.log(`\n  sitemap.xml: ${locs.length} URLs`);
  const expected = files.filter((f) => !f.endsWith('404.html')).length;
  if (locs.length !== expected) warn('sitemap.xml', `${locs.length} URLs para ${expected} paginas indexaveis`);
}

// ---- robots
if (!fs.existsSync(path.join(ROOT, 'robots.txt'))) err('robots.txt', 'nao existe');

console.log(`\n${errors === 0 ? '\x1b[32mOK\x1b[0m' : '\x1b[31mFALHOU\x1b[0m'}  ${errors} erro(s), ${warns} aviso(s)\n`);
process.exit(errors ? 1 : 0);
