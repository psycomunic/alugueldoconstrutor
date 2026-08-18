# -*- coding: utf-8 -*-
"""Dados do negocio, icones e blocos comuns (head, header, footer, CTA).

Mudou telefone, endereco ou horario? Mude AQUI e rode `npm run build`.
A alteracao se propaga para todas as paginas, para os links wa.me,
para o rodape e para o JSON-LD de uma vez so.
"""
import os
from urllib.parse import quote

# ===========================================================================
# 1. NEGOCIO
# ===========================================================================
BRAND = "Aluguel do Construtor"
LEGAL = "LOJA DO CONSTRUTOR MATERIAIS E SERVIÇOS LTDA"
CNPJ = "42.626.394/0001-38"

WA = "5521972770014"                 # numero usado nos links wa.me
PHONE_DISPLAY = "(21) 97277-0014"
PHONE_TEL = "+5521972770014"
EMAIL = ""                           # pendente de confirmacao com o cliente

HOURS_SHORT = "Seg. a sex., 7h às 17h · Sáb., 7h às 12h"
HOURS_LONG = "Segunda a sexta, das 7h às 17h. Sábado, das 7h às 12h."

INSTAGRAM = "https://www.instagram.com/alugueldoconstrutoroficial/"
FACEBOOK = "https://www.facebook.com/p/Aluguel-do-construtor-61566654734638/"

CITY = "Rio de Janeiro"
STATE = "RJ"
STATE_FULL = "Rio de Janeiro"
COUNTRY = "BR"

# Bairros e regioes atendidas: alimenta o areaServed da Organization (lista
# inteira) e o de cada Service (so os 12 primeiros, ver schema.py).
# ORDEM IMPORTA: os bairros das unidades primeiro, depois por relevancia de
# busca, porque o corte em AREAS[:12] usa esta ordem.
# Sem duplicata. Uniao dos "atende" de cada unidade em content.py mais a
# cobertura adicional de Jacarepagua e Zona Norte.
AREAS = [
    # bairros onde ficam as cinco unidades
    "Recreio dos Bandeirantes", "Vargem Grande", "Pedra de Guaratiba", "Botafogo",
    # maior volume de busca no entorno
    "Barra da Tijuca", "Jacarepaguá", "Campo Grande", "Guaratiba",
    "Vargem Pequena", "Copacabana", "Ipanema", "Freguesia (Jacarepaguá)",
    # --- daqui para baixo nao entra no areaServed dos Service ---
    # Zona Sul
    "Leblon", "Flamengo", "Laranjeiras", "Humaitá", "Catete", "Urca", "Gávea",
    "Jardim Botânico", "São Conrado",
    # Barra, Recreio e vargens
    "Barra Olímpica", "Itanhangá", "Joá", "Grumari", "Camorim", "Curicica",
    # Jacarepaguá e entorno
    "Taquara", "Anil", "Gardênia Azul", "Pechincha", "Praça Seca", "Tanque",
    "Cidade de Deus",
    # Guaratiba e Zona Oeste
    "Barra de Guaratiba", "Santa Cruz", "Sepetiba", "Cosmos",
    "Senador Vasconcelos", "Santíssimo", "Bangu", "Realengo",
    # Zona Norte
    "Madureira", "Méier", "Irajá", "Penha",
]

# ===========================================================================
# 2. DOMINIO
# ===========================================================================
# og:image, og:url, canonical e o sitemap precisam de URL absoluta que exista
# de verdade. Resolve nesta ordem:
#   1. SITE_URL          (defina na mao quando quiser forcar)
#   2. VERCEL_PROJECT_PRODUCTION_URL (a Vercel injeta no build)
#   3. SITE_FINAL        (o dominio proprio)
SITE_FINAL = "https://alugueldoconstrutor.com"
_v = os.environ.get("VERCEL_PROJECT_PRODUCTION_URL", "").strip()
SITE = (os.environ.get("SITE_URL", "").strip()
        or (("https://" + _v) if _v else "")
        or SITE_FINAL).rstrip("/")


def url(path):
    """Caminho relativo -> URL absoluta e limpa (sem .html, sem index)."""
    p = (path or "").lstrip("/")
    if p in ("index.html", "index", ""):
        return SITE + "/"
    if p.endswith(".html"):
        p = p[:-5]
    return SITE + "/" + p


def wa_link(text=None, number=None):
    n = number or WA
    if not text:
        return "https://wa.me/" + n
    return "https://wa.me/%s?text=%s" % (n, quote(text))


WA_DEFAULT = wa_link("Olá! Vim pelo site e gostaria de um orçamento de locação de equipamentos.")


def maps_link(address):
    return "https://www.google.com/maps/search/?api=1&query=" + quote(address)


# ===========================================================================
# 3. ICONES (SVG inline: zero requisicao, herdam currentColor)
# ===========================================================================
_S = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" '
      'stroke="currentColor" stroke-width="1.9" stroke-linecap="round" '
      'stroke-linejoin="round" aria-hidden="true">%s</svg>')

ICONS = {
    "phone": _S % '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    "whatsapp": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.2-1.7-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.7 1-.9 1.2-.2.2-.3.2-.6.1-1.7-.9-2.9-1.6-4-3.6-.3-.5.3-.5.9-1.6.1-.2 0-.4 0-.5s-.7-1.6-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.3 5.2 4.6 2 .8 2.7.9 3.7.8.6-.1 1.7-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2m0 18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-3.1.8.8-3-.2-.3A8.2 8.2 0 1 1 12 20.2"/></svg>',
    "pin": _S % '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
    "clock": _S % '<circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 15.5 14"/>',
    "shield": _S % '<path d="M12 2.5 20 6v5.5c0 5-3.4 8.9-8 10.2-4.6-1.3-8-5.2-8-10.2V6z"/><polyline points="9 12 11.2 14.2 15.4 10"/>',
    "truck": _S % '<path d="M2 6.5h11v9H2z"/><path d="M13 9.5h4l3 3.2v2.8h-7z"/><circle cx="6.5" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
    "wrench": _S % '<path d="M14.6 6.6a4.5 4.5 0 0 0 5.9 5.9l-8 8a2.5 2.5 0 0 1-3.6-3.6z"/><path d="M14.6 6.6 17 4.2a4.5 4.5 0 0 1 3.5 7.7"/>',
    "star": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="m12 2.6 2.9 5.9 6.5.9-4.7 4.6 1.1 6.5-5.8-3-5.8 3 1.1-6.5L2.6 9.4l6.5-.9z"/></svg>',
    "check": _S % '<polyline points="20 6 9 17 4 12"/>',
    "arrow": _S % '<line x1="4" y1="12" x2="19" y2="12"/><polyline points="13 6 19 12 13 18"/>',
    "chevron": _S % '<polyline points="6 9 12 15 18 9"/>',
    "instagram": _S % '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="3.6"/><circle cx="17.4" cy="6.6" r="1" fill="currentColor" stroke="none"/>',
    "facebook": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M14 8.5V7c0-.8.2-1.2 1.3-1.2h1.6V3h-2.6C11.2 3 10.2 4.5 10.2 6.8v1.7H8.4V11h1.8v10h3.6V11h2.4l.4-2.5z"/></svg>',
    "card": _S % '<rect x="2.5" y="5" width="19" height="14" rx="2.5"/><line x1="2.5" y1="9.8" x2="21.5" y2="9.8"/>',
    "pix": _S % '<path d="m12 2.8 3.4 3.4a2.5 2.5 0 0 0 3.5 0"/><path d="M21.2 12 12 21.2 2.8 12 12 2.8z"/>',
    "bank": _S % '<path d="M3 9.5 12 4l9 5.5"/><line x1="4.5" y1="20" x2="19.5" y2="20"/><line x1="6.5" y1="10.5" x2="6.5" y2="17"/><line x1="12" y1="10.5" x2="12" y2="17"/><line x1="17.5" y1="10.5" x2="17.5" y2="17"/>',
    "doc": _S % '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><polyline points="14 3 14 8 19 8"/><line x1="8.5" y1="13" x2="15" y2="13"/><line x1="8.5" y1="16.5" x2="13" y2="16.5"/>',
    "chat": _S % '<path d="M21 11.5a8 8 0 0 1-11.6 7.2L3 21l2.3-6.4A8 8 0 1 1 21 11.5z"/>',
    "users": _S % '<path d="M16.5 20v-1.8a3.6 3.6 0 0 0-3.6-3.6H6.6A3.6 3.6 0 0 0 3 18.2V20"/><circle cx="9.8" cy="7.5" r="3.5"/><path d="M21 20v-1.8a3.6 3.6 0 0 0-2.7-3.5"/><path d="M15.4 4.2a3.6 3.6 0 0 1 0 6.6"/>',
    "money": _S % '<rect x="2.5" y="6" width="19" height="12" rx="2"/><circle cx="12" cy="12" r="2.6"/><line x1="6" y1="12" x2="6.01" y2="12"/><line x1="18" y1="12" x2="18.01" y2="12"/>',
    "gauge": _S % '<path d="M12 14.5 16 10"/><path d="M4 18a9 9 0 1 1 16 0"/>',
    "layers": _S % '<polygon points="12 2.8 21.5 8 12 13.2 2.5 8"/><polyline points="2.5 16 12 21.2 21.5 16"/><polyline points="2.5 12 12 17.2 21.5 12"/>',
    "target": _S % '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.4" fill="currentColor" stroke="none"/>',
    "eye": _S % '<path d="M1.8 12S5.5 5.5 12 5.5 22.2 12 22.2 12 18.5 18.5 12 18.5 1.8 12 1.8 12z"/><circle cx="12" cy="12" r="3"/>',
    "mail": _S % '<rect x="2.5" y="5" width="19" height="14" rx="2.5"/><polyline points="3 7 12 13.2 21 7"/>',
    "store": _S % '<path d="M3.5 9.5 5 4.5h14l1.5 5"/><path d="M4.5 9.5v10h15v-10"/><path d="M3.5 9.5a2.6 2.6 0 0 0 4.3 2 2.6 2.6 0 0 0 4.2 0 2.6 2.6 0 0 0 4.2 0 2.6 2.6 0 0 0 4.3-2"/>',
    "handshake": _S % '<path d="m11 17.5 2 2a1.7 1.7 0 0 0 2.4-2.4"/><path d="M13 15.5 15.4 18a1.7 1.7 0 0 0 2.4-2.4l-4.6-4.6"/><path d="M2.5 11 6 7.5h4l2.5 2.5-2 2a1.6 1.6 0 0 1-2.3 0L7 10.7"/><path d="M21.5 11 18 7.5h-3.5"/>',
    "spark": _S % '<path d="M13 2.5 4.5 13.5H11l-1 8 8.5-11H12z"/>',
    "ruler": _S % '<path d="m15.5 2.5 6 6-13 13-6-6z"/><line x1="11" y1="7" x2="13" y2="9"/><line x1="8" y1="10" x2="10" y2="12"/><line x1="5" y1="13" x2="7" y2="15"/>',
}


def icon(name, cls=""):
    svg = ICONS.get(name, ICONS["check"])
    if cls:
        svg = svg.replace("<svg ", '<svg class="%s" ' % cls, 1)
    return svg


# ===========================================================================
# 4. NAVEGACAO
# ===========================================================================
NAV = [
    ("index.html", "Início"),
    ("equipamentos.html", "Equipamentos"),
    ("unidades.html", "Unidades"),
    ("quem-somos.html", "Quem somos"),
    ("seja-parceiro.html", "Seja parceiro"),
    ("perguntas-frequentes.html", "Dúvidas"),
    ("contato.html", "Contato"),
]


def rel(path, depth):
    """Caminho relativo a partir da profundidade da pagina atual."""
    return ("../" * depth) + path


# ---------------------------------------------------------------------------
# Cache: assinatura curta do conteudo de CSS e JS.
# Os dois tem nome fixo, e o navegador de quem ja visitou pode ficar com a
# versao antiga. Anexar ?v=<hash> muda a URL quando o conteudo muda, entao o
# navegador trata como recurso novo e baixa. Se o conteudo nao muda, a URL nao
# muda e o cache continua valendo.
_ASSINATURA = {}


def v(caminho):
    """<caminho>?v=abcdef12, a partir do hash do arquivo em disco."""
    if caminho not in _ASSINATURA:
        import hashlib
        raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        try:
            with open(os.path.join(raiz, caminho), "rb") as fp:
                _ASSINATURA[caminho] = hashlib.sha1(fp.read()).hexdigest()[:8]
        except OSError:
            _ASSINATURA[caminho] = "0"
    return "%s?v=%s" % (caminho, _ASSINATURA[caminho])


# ===========================================================================
# 5. HEAD
# ===========================================================================
def head(title, description, path, depth=0, image="assets/img/og-cover.jpg",
         preload=None, robots=None, extra=""):
    r = lambda p: rel(p, depth)
    canonical = url(path)
    og_image = SITE + "/" + image.lstrip("/")
    pre = ""
    if preload:
        pre = ('\n  <link rel="preload" as="image" href="%s" fetchpriority="high">'
               % r(preload))
    return """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>%(title)s</title>
  <meta name="description" content="%(description)s">
  <link rel="canonical" href="%(canonical)s">
  <meta name="robots" content="%(robots)s">
  <meta name="author" content="%(brand)s">
  <meta name="theme-color" content="#17161A">
  <meta name="format-detection" content="telephone=no">

  <meta property="og:type" content="website">
  <meta property="og:site_name" content="%(brand)s">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:title" content="%(title)s">
  <meta property="og:description" content="%(description)s">
  <meta property="og:url" content="%(canonical)s">
  <meta property="og:image" content="%(og_image)s">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Caminhão do Aluguel do Construtor carregado com andaimes">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="%(title)s">
  <meta name="twitter:description" content="%(description)s">
  <meta name="twitter:image" content="%(og_image)s">

  <link rel="icon" href="%(favicon)s" type="image/svg+xml">
  <link rel="apple-touch-icon" href="%(apple)s">
  <link rel="manifest" href="%(manifest)s">

  <link rel="preload" href="%(font_body)s" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="%(font_display)s" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="%(css)s">%(pre)s
  <script>document.documentElement.className+=" js"</script>
%(extra)s</head>
<body>
<a class="skip-link" href="#conteudo">Ir para o conteúdo</a>
""" % {
        "title": title, "description": description, "canonical": canonical,
        "robots": robots or "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1",
        "brand": BRAND, "og_image": og_image,
        "favicon": r("assets/img/favicon.svg"),
        "apple": r("assets/img/apple-touch-icon.png"),
        "manifest": r("manifest.webmanifest"),
        "css": r(v("assets/css/style.css")),
        # Fontes auto-hospedadas: so o subset latin entra em preload, porque e o
        # que todo texto do site usa. O latin-ext fica declarado no CSS e so e
        # buscado se aparecer um glifo fora de U+0000-00FF.
        "font_body": r("assets/fonts/inter-latin.woff2"),
        "font_display": r("assets/fonts/archivo-latin.woff2"),
        "pre": pre, "extra": extra,
    }


# ===========================================================================
# 6. HEADER
# ===========================================================================
def _brand(depth, light=False):
    r = lambda p: rel(p, depth)
    _img = ('<img class="brand__mark%s" src="%s" width="40" height="40" '
            'alt="" loading="lazy" decoding="async">')
    if light:
        marks = _img % ("", r("assets/img/logo-mark-light.svg"))
    else:
        # Duas versoes da marca. O header fica transparente sobre o hero escuro
        # e ali o corpo escuro do logo (#201D1E) desaparece no fundo. O CSS
        # troca uma pela outra conforme o header esteja sobreposto ou solido.
        marks = ((_img % ("  brand__mark--dark", r("assets/img/logo-mark.svg")))
                 + (_img % (" brand__mark--light", r("assets/img/logo-mark-light.svg"))))
    return ('<a class="brand" href="%s" aria-label="%s, página inicial">%s'
            '<span class="brand__txt">Aluguel do<span>Construtor</span></span></a>'
            % (r("index.html"), BRAND, marks))


def video(depth, vid, titulo, capa, alt, legenda=None):
    """Capa clicavel que so carrega o player do YouTube depois do clique.

    Um <iframe> direto do YouTube custa centenas de KB e varias conexoes a
    terceiros em TODA visita, inclusive de quem nunca da play. Aqui a pagina
    carrega so a imagem de capa, que e auto-hospedada; o player entra no
    clique, via main.js, e no dominio youtube-nocookie.
    Sem JS o <noscript> leva para o video no YouTube.
    """
    r = lambda p: rel(p, depth)
    cap = ('<figcaption>%s</figcaption>' % legenda) if legenda else ''
    return """<figure class="ytlite" data-yt="%(vid)s">
  <div class="ytlite__quadro">
    <img class="ytlite__capa" src="%(capa)s" srcset="%(capa400)s 400w, %(capa)s 720w"
         sizes="(max-width: 700px) 86vw, 360px" width="720" height="1280"
         loading="lazy" decoding="async" alt="%(alt)s">
    <button class="ytlite__play" type="button" aria-label="Assistir ao vídeo: %(titulo)s">
      <span class="ytlite__tri" aria-hidden="true"></span>
    </button>
    <noscript><a class="ytlite__sem-js" href="https://www.youtube.com/watch?v=%(vid)s"
       target="_blank" rel="noopener">Assistir no YouTube</a></noscript>
  </div>
  %(cap)s
</figure>""" % {
        "vid": vid, "titulo": titulo, "alt": alt, "cap": cap,
        "capa": r("assets/img/%s.webp" % capa),
        "capa400": r("assets/img/%s-400.webp" % capa),
    }


def topbar(depth):
    r = lambda p: rel(p, depth)
    return """<div class="topbar">
  <div class="wrap topbar__in">
    <div class="topbar__list">
      <span class="topbar__item">%(pin)s <a href="%(unidades)s">5 unidades no Rio de Janeiro</a></span>
      <span class="topbar__item">%(clock)s %(hours)s</span>
    </div>
    <div class="topbar__list">
      <span class="topbar__item">%(phone)s <a href="tel:%(tel)s">%(phone_d)s</a></span>
      <span class="topbar__social">
        <a href="%(ig)s" target="_blank" rel="noopener" aria-label="Instagram do %(brand)s">%(ico_ig)s</a>
        <a href="%(fb)s" target="_blank" rel="noopener" aria-label="Facebook do %(brand)s">%(ico_fb)s</a>
      </span>
    </div>
  </div>
</div>""" % {
        "pin": icon("pin"), "clock": icon("clock"), "phone": icon("phone"),
        "unidades": r("unidades.html"), "hours": HOURS_SHORT,
        "tel": PHONE_TEL, "phone_d": PHONE_DISPLAY,
        "ig": INSTAGRAM, "fb": FACEBOOK, "brand": BRAND,
        "ico_ig": icon("instagram"), "ico_fb": icon("facebook"),
    }


def header(active, depth=0, equipamentos=None):
    from content import EQUIPAMENTOS
    equipamentos = equipamentos or EQUIPAMENTOS
    r = lambda p: rel(p, depth)

    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ""
        if href == "equipamentos.html":
            panel = []
            for e in equipamentos[:10]:
                panel.append(
                    '<a href="%s"><img src="%s" width="30" height="30" alt="" loading="lazy" decoding="async">%s</a>'
                    % (r("equipamentos/%s.html" % e["slug"]),
                       r("assets/img/equipamentos/%s-380.webp" % e["slug"]), e["nome"]))
            panel.append('<a class="nav__all" href="%s">Ver todos os %d equipamentos %s</a>'
                         % (r("equipamentos.html"), len(equipamentos), icon("arrow")))
            items.append(
                '<li class="nav__item"><a class="nav__link" href="%s"%s>%s %s</a>'
                '<div class="nav__panel">%s</div></li>'
                % (r(href), cur, label, icon("chevron"), "".join(panel)))
        else:
            items.append('<li class="nav__item"><a class="nav__link" href="%s"%s>%s</a></li>'
                         % (r(href), cur, label))

    drawer_eq = "".join(
        '<a href="%s">%s</a>' % (r("equipamentos/%s.html" % e["slug"]), e["nome"])
        for e in equipamentos)
    # Fora "equipamentos.html", que virou o <details> com as 15 categorias, e
    # fora "index.html", que ja e escrito na mao logo antes do <details>. Sem
    # esta segunda exclusao o "Inicio" aparecia duas vezes no menu mobile.
    drawer_nav = "".join(
        '<a href="%s"%s>%s</a>' % (r(h), ' aria-current="page"' if h == active else "", l)
        for h, l in NAV if h not in ("equipamentos.html", "index.html"))

    return """%(topbar)s
<header class="header" data-header>
  <div class="wrap header__in">
    %(brand)s
    <nav class="nav" aria-label="Principal">
      <ul class="nav__list">%(items)s</ul>
    </nav>
    <a class="btn btn--primary btn--sm nav__cta" href="%(wa)s" target="_blank" rel="noopener">%(ico_wa)s Pedir orçamento</a>
    <button class="burger" data-burger type="button" aria-expanded="false" aria-controls="menu-mobile" aria-label="Abrir menu">
      <span></span>
    </button>
  </div>
</header>

<div class="drawer" data-drawer id="menu-mobile">
  <div class="drawer__panel">
    <div class="drawer__head">
      %(brand2)s
      <button class="drawer__close" data-drawer-close type="button" aria-label="Fechar menu">&times;</button>
    </div>
    <a href="%(home)s"%(home_cur)s>Início</a>
    <details>
      <summary>Equipamentos</summary>
      <a href="%(eq)s"><strong>Ver todos</strong></a>
      %(drawer_eq)s
    </details>
    %(drawer_nav)s
    <a class="btn btn--primary btn--block" href="%(wa)s" target="_blank" rel="noopener">%(ico_wa)s Pedir orçamento</a>
    <a class="btn btn--ghost btn--block" href="tel:%(tel)s">%(ico_ph)s %(phone_d)s</a>
  </div>
</div>
""" % {
        "topbar": topbar(depth), "brand": _brand(depth), "brand2": _brand(depth),
        "items": "".join(items), "wa": WA_DEFAULT, "ico_wa": icon("whatsapp"),
        "home": r("index.html"), "home_cur": ' aria-current="page"' if active == "index.html" else "",
        "eq": r("equipamentos.html"), "drawer_eq": drawer_eq, "drawer_nav": drawer_nav,
        "tel": PHONE_TEL, "phone_d": PHONE_DISPLAY, "ico_ph": icon("phone"),
    }


# ===========================================================================
# 7. MIGALHAS
# ===========================================================================
def crumbs(trail, depth=0, dark=False):
    """trail: lista de (href|None, label). O ultimo item e a pagina atual."""
    r = lambda p: rel(p, depth)
    lis = []
    for href, label in trail:
        if href:
            lis.append('<li><a href="%s">%s</a></li>' % (r(href), label))
        else:
            lis.append('<li><span aria-current="page">%s</span></li>' % label)
    return ('<nav class="crumbs" aria-label="Você está aqui"><ol>%s</ol></nav>'
            % "".join(lis))


# ===========================================================================
# 8. CTA FINAL + RODAPE
# ===========================================================================
def cta(depth=0, title=None, text=None, primary=None):
    r = lambda p: rel(p, depth)
    title = title or "Sua obra não pode parar. A gente também não."
    text = text or ("Mande a lista do que você precisa pelo WhatsApp. "
                    "Respondemos com disponibilidade, prazo e valor, sem burocracia e sem cadastro.")
    primary = primary or WA_DEFAULT
    return """<section class="cta">
  <div class="wrap cta__in">
    <div>
      <p class="eyebrow">Orçamento em minutos</p>
      <h2>%(title)s</h2>
      <p>%(text)s</p>
    </div>
    <div class="cta__side">
      <a class="btn btn--wa btn--lg" href="%(primary)s" target="_blank" rel="noopener">%(ico_wa)s Falar no WhatsApp</a>
      <a class="btn btn--ghost" href="%(contato)s">Preencher formulário</a>
      <a class="btn btn--ghost" href="tel:%(tel)s">%(ico_ph)s %(phone_d)s</a>
    </div>
  </div>
</section>
<div class="hazard" role="presentation"></div>""" % {
        "title": title, "text": text, "primary": primary,
        "ico_wa": icon("whatsapp"), "ico_ph": icon("phone"),
        "contato": r("contato.html"), "tel": PHONE_TEL, "phone_d": PHONE_DISPLAY,
    }


def footer(depth=0):
    from content import EQUIPAMENTOS, UNIDADES
    r = lambda p: rel(p, depth)

    eq_links = "".join(
        '<li><a href="%s">Aluguel de %s</a></li>' % (r("equipamentos/%s.html" % e["slug"]), e["nome"].lower())
        for e in EQUIPAMENTOS[:8])
    un_links = "".join(
        '<li><a href="%s">%s</a></li>' % (r("unidades/%s.html" % u["slug"]), u["bairro"])
        for u in UNIDADES)
    inst_links = "".join(
        '<li><a href="%s">%s</a></li>' % (r(h), l) for h, l in NAV if h != "index.html")

    return """<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div class="footer__brand">
        %(brand)s
        <p>Locação de andaimes, betoneiras, marteletes e mais 12 categorias de equipamentos para construção civil no Rio de Janeiro. Entrega e retirada com frota própria.</p>
        <div class="footer__soc">
          <a href="%(ig)s" target="_blank" rel="noopener" aria-label="Instagram">%(ico_ig)s</a>
          <a href="%(fb)s" target="_blank" rel="noopener" aria-label="Facebook">%(ico_fb)s</a>
          <a href="%(wa)s" target="_blank" rel="noopener" aria-label="WhatsApp">%(ico_wa)s</a>
        </div>
      </div>

      <div>
        <h4>Equipamentos</h4>
        <ul>%(eq)s<li><a href="%(eq_all)s"><strong>Ver todos</strong></a></li></ul>
      </div>

      <div>
        <h4>Unidades</h4>
        <ul>%(un)s</ul>
        <h4 style="margin-top:26px">Institucional</h4>
        <ul>%(inst)s</ul>
      </div>

      <div>
        <h4>Fale com a gente</h4>
        <address class="footer__nap">
          <div>%(ico_pin)s <span>Rua Professora Luiza Nogueira Gonçalves, 350<br>Recreio dos Bandeirantes, Rio de Janeiro &ndash; RJ</span></div>
          <div>%(ico_ph)s <a href="tel:%(tel)s">%(phone_d)s</a></div>
          <div>%(ico_cl)s <span>%(hours)s</span></div>
        </address>
        <a class="btn btn--wa btn--sm" style="margin-top:18px" href="%(wa)s" target="_blank" rel="noopener">%(ico_wa)s Pedir orçamento</a>
      </div>
    </div>

    <div class="footer__bar">
      <span>&copy; <span data-year>%(year)s</span> %(legal)s &mdash; CNPJ %(cnpj)s. Todos os direitos reservados.</span>
      <span>Locação de equipamentos para construção civil no Rio de Janeiro.</span>
    </div>
  </div>
</footer>

<a class="wafab" href="%(wa)s" target="_blank" rel="noopener" aria-label="Falar no WhatsApp">%(ico_wa)s <span>Orçamento no WhatsApp</span></a>

<script src="%(js)s" defer></script>
</body>
</html>
""" % {
        "brand": _brand(depth, light=True),
        "ig": INSTAGRAM, "fb": FACEBOOK, "wa": WA_DEFAULT,
        "ico_ig": icon("instagram"), "ico_fb": icon("facebook"), "ico_wa": icon("whatsapp"),
        "eq": eq_links, "eq_all": r("equipamentos.html"), "un": un_links, "inst": inst_links,
        "ico_pin": icon("pin"), "ico_ph": icon("phone"), "ico_cl": icon("clock"),
        "tel": PHONE_TEL, "phone_d": PHONE_DISPLAY, "hours": HOURS_SHORT,
        "year": 2026, "legal": LEGAL, "cnpj": CNPJ,
        "js": r(v("assets/js/main.js")),
    }
