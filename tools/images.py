#!/usr/bin/env python3
"""Pipeline de imagens: recorta, redimensiona e converte para WebP otimizado.

Fonte: as pastas baixadas do site antigo (uma por pagina).
Saida: assets/img/ com nomes semanticos, bons para SEO.

Rode uma vez. Depois disso as imagens ficam versionadas no repositorio.
"""
import os
import sys
from PIL import Image

SRC = os.environ.get("ADC_SRC", "/mnt/user-data/uploads/ALUGUEL DO CONSTRUTOR")
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "img")

HOME = "Aluguel do Construtor – Tudo para sua obra_"
PROD = "Nossos Produtos – Aluguel do Construtor"
QUEM = "Quem Somos – Aluguel do Construtor"
UNID = "Unidades – Aluguel do Construtor"
CONT = "Contato – Aluguel do Construtor"


def op(path):
    return Image.open(os.path.join(SRC, path)).convert("RGBA")


def flatten(im, bg=(255, 255, 255)):
    base = Image.new("RGBA", im.size, bg + (255,))
    base.alpha_composite(im)
    return base.convert("RGB")


def save(im, name, quality=80, alpha=False, subdir=""):
    d = os.path.join(OUT, subdir)
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, name)
    if alpha:
        im.save(p, "WEBP", quality=quality, method=4)
    else:
        im.convert("RGB").save(p, "WEBP", quality=quality, method=4)
    kb = os.path.getsize(p) / 1024
    print("  %-46s %5dx%-5d %6.1f KB" % (os.path.join(subdir, name), im.size[0], im.size[1], kb))


def cover(im, w, h):
    """Redimensiona cobrindo a caixa e corta centralizado (levemente acima do centro)."""
    sw, sh = im.size
    scale = max(w / sw, h / sh)
    nw, nh = int(round(sw * scale)), int(round(sh * scale))
    im = im.resize((nw, nh), Image.LANCZOS)
    left = (nw - w) // 2
    top = int((nh - h) * 0.42)
    return im.crop((left, top, left + w, top + h))


def fit(im, w, h=None):
    h = h or w
    im = im.copy()
    im.thumbnail((w, h), Image.LANCZOS)
    return im


# ---------------------------------------------------------------- equipamentos
# (arquivo de origem, slug de saida)
EQUIP = [
    ("imgi_3_Andaimes.webp", "andaimes"),
    ("imgi_4_Betoneiras.webp", "betoneiras"),
    ("imgi_5_MARTELETE.webp", "marteletes"),
    ("imgi_6_Compactadores-1.webp", "compactadores"),
    ("imgi_7_Cortadores-de-Piso-1.webp", "cortadores-de-piso"),
    ("imgi_8_Escoras-1.webp", "escoras"),
    ("imgi_9_Furadeiras-e-Parafusadeiras-1-e1765218521101.webp", "furadeiras-e-parafusadeiras"),
    ("imgi_10_Lixadeiras-e-Esmerilhadeiras-1.webp", "lixadeiras-e-esmerilhadeiras"),
    ("imgi_11_Serras-e-Plainas-1.webp", "serras-e-plainas"),
    ("imgi_12_Escadas-1.webp", "escadas"),
    ("imgi_13_Lavadoras-de-Alta-Pressao-1.webp", "lavadoras-de-alta-pressao"),
    ("imgi_14_Lavadoras-de-Estofado-1.webp", "lavadoras-de-estofado"),
    ("imgi_15_Motosserras-e-Rocadeiras-1.webp", "motosserras-e-rocadeiras"),
    ("imgi_16_Sopradores_Aspiradores-1.webp", "sopradores-e-aspiradores"),
    ("imgi_17_Bombas-Sapo-1.webp", "bombas-sapo"),
]


def build_equip():
    print("equipamentos (quadradas, fundo transparente):")
    for src, slug in EQUIP:
        im = op(os.path.join(PROD, src))
        # normaliza para quadrado com margem, mantendo a proporcao original
        side = max(im.size)
        canvas = Image.new("RGBA", (side, side), (0, 0, 0, 0))
        canvas.alpha_composite(im, ((side - im.size[0]) // 2, (side - im.size[1]) // 2))
        save(canvas.resize((760, 760), Image.LANCZOS), slug + ".webp", 78, alpha=True, subdir="equipamentos")
        save(canvas.resize((380, 380), Image.LANCZOS), slug + "-380.webp", 76, alpha=True, subdir="equipamentos")


# ---------------------------------------------------------------------- fotos
def build_fotos():
    print("fotos reais:")
    # hero: caminhao carregado com andaimes, com a marca visivel
    hero = op(os.path.join(HOME, "imgi_4_Estoque-01-scaled.webp"))
    save(cover(flatten(hero), 1120, 1400), "hero-caminhao-andaimes.webp", 76)
    save(cover(flatten(hero), 560, 700), "hero-caminhao-andaimes-560.webp", 74)

    save(cover(flatten(op(os.path.join(HOME, "imgi_3_Estoque-03-scaled.webp"))), 900, 1120),
         "estoque-andaimes-galpao.webp", 76)
    save(cover(flatten(op(os.path.join(HOME, "imgi_5_Estoque-02-scaled.webp"))), 1200, 800),
         "carregamento-equipamentos.webp", 78)
    save(cover(flatten(op(os.path.join(HOME, "imgi_12_IMG-01-1.webp"))), 1200, 800),
         "loja-do-construtor-fachada.webp", 80)
    save(cover(flatten(op(os.path.join(UNID, "imgi_3_Rectangle-161124752.webp"))), 1000, 750),
         "unidade-parceira-fachada.webp", 80)
    save(cover(flatten(op(os.path.join(QUEM, "imgi_4_Confianca-que-se-constroi-com-atitude-nao-com-palavras.webp"))),
               1100, 820), "andaime-fachadeiro-obra.webp", 78)
    save(cover(flatten(op(os.path.join(QUEM, "imgi_2_Quem-Somos-e1765291999769.webp"))), 900, 900),
         "andaime-tubular-montado.webp", 78)
    save(cover(flatten(op(os.path.join(QUEM, "imgi_9_A-confianca-e-o-nosso-maior-contrato-scaled-e1765217573563.webp"))),
               800, 1000), "andaime-torre.webp", 78)
    save(cover(flatten(op(os.path.join(QUEM, "imgi_8_Por-que-somos-diferentes-scaled.webp"))), 1000, 900),
         "andaime-estrutura.webp", 78)

    print("recortes com transparencia:")
    for src, name, w in [
        (os.path.join(HOME, "imgi_41_Tenha-uma-unidade-do-Aluguel-do-Construtor-na-sua-loja.webp"),
         "profissional-uniforme.webp", 760),
        (os.path.join(PROD, "imgi_29_Monte-seu-pedido-e-receba-o-orcamento-em-minutos.webp"),
         "profissional-whatsapp.webp", 720),
        (os.path.join(PROD, "imgi_2_Nossos-Produtos-e1765292706210.webp"), "kit-ferramentas.webp", 860),
        (os.path.join(CONT, "imgi_2_Contato-e1765293148487.webp"), "whatsapp-celular.webp", 640),
        (os.path.join(UNID, "imgi_2_Unidades.webp"), "mapa-unidades.webp", 640),
    ]:
        save(fit(op(src), w), name, 78, alpha=True)


# ---------------------------------------------------------------------- social
def build_social():
    """og-cover 1200x630 montado a partir da foto do caminhao + faixa da marca."""
    from PIL import ImageDraw, ImageFont
    print("social:")
    base = cover(flatten(op(os.path.join(HOME, "imgi_4_Estoque-01-scaled.webp"))), 1200, 630)
    ov = Image.new("RGBA", (1200, 630), (0, 0, 0, 0))
    px = ov.load()
    for x in range(1200):
        t = min(1.0, max(0.0, (x - 120) / 820.0))
        a = int(238 - 168 * t)          # scrim da esquerda para a direita
        for y in range(630):
            px[x, y] = (23, 22, 26, a)
    d = ImageDraw.Draw(ov)
    d.rectangle([0, 606, 1200, 630], fill=(250, 126, 2, 255))
    out = Image.alpha_composite(base.convert("RGBA"), ov)

    def font(sz, bold=True):
        for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
                  "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
            if os.path.exists(p):
                return ImageFont.truetype(p, sz)
        return ImageFont.load_default()

    d = ImageDraw.Draw(out)
    logo = Image.open("/tmp/logo-mark-light.png").convert("RGBA") if os.path.exists(
        "/tmp/logo-mark-light.png") else None
    x = 76
    if logo:
        logo = fit(logo, 132, 132)
        out.alpha_composite(logo, (x, 150))
    d.text((x, 320), "ALUGUEL DO", font=font(78), fill=(255, 255, 255))
    d.text((x, 404), "CONSTRUTOR", font=font(78), fill=(6, 190, 37))
    d.text((x, 512), "Locação de equipamentos para construção civil  ·  Rio de Janeiro",
           font=font(26), fill=(232, 230, 228))
    out.convert("RGB").save(os.path.join(OUT, "og-cover.jpg"), "JPEG", quality=86, optimize=True)
    print("  og-cover.jpg %.1f KB" % (os.path.getsize(os.path.join(OUT, "og-cover.jpg")) / 1024))


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("all", "equip"):
        build_equip()
    if which in ("all", "fotos"):
        build_fotos()
    if which in ("all", "social"):
        build_social()
