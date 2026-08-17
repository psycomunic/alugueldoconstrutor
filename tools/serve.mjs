/* Servidor local, sem dependencia. `npm run dev` -> http://localhost:8080
   Resolve URL limpa (/equipamentos -> equipamentos.html) igual a Vercel. */
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const PORT = Number(process.env.PORT || 8080);

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.webmanifest': 'application/manifest+json; charset=utf-8',
  '.xml': 'application/xml; charset=utf-8',
  '.txt': 'text/plain; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.woff2': 'font/woff2',
  '.webp': 'image/webp',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.ico': 'image/x-icon',
};

const send = (res, code, body, type) => {
  res.writeHead(code, { 'Content-Type': type || 'text/plain; charset=utf-8' });
  res.end(body);
};

http.createServer((req, res) => {
  let p = decodeURIComponent(new URL(req.url, 'http://x').pathname);
  if (p.endsWith('/')) p += 'index.html';

  const candidates = [p, p + '.html', path.posix.join(p, 'index.html')];
  for (const c of candidates) {
    const file = path.join(ROOT, c);
    if (!file.startsWith(ROOT)) break;
    if (fs.existsSync(file) && fs.statSync(file).isFile()) {
      return send(res, 200, fs.readFileSync(file), MIME[path.extname(file)] || 'application/octet-stream');
    }
  }

  const nf = path.join(ROOT, '404.html');
  if (fs.existsSync(nf)) return send(res, 404, fs.readFileSync(nf), MIME['.html']);
  send(res, 404, 'Not found');
}).listen(PORT, () => {
  console.log(`\n  Aluguel do Construtor\n  http://localhost:${PORT}\n`);
});
