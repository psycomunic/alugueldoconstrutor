# -*- coding: utf-8 -*-
"""Gerador das paginas do site.

Rode com:  npm run build   (ou  python3 build/build.py  a partir da raiz)

O conteudo de cada pagina esta neste arquivo. Header, rodape e dados do
negocio estao em partials.py. Textos de equipamento e unidade estao em
content.py. JSON-LD esta em schema.py.
"""
import io
import os
import sys
import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import partials as P            # noqa: E402
import schema as S              # noqa: E402
from content import (           # noqa: E402
    EQUIPAMENTOS, DESTAQUES, UNIDADES, DEPOIMENTOS, PAGAMENTOS,
    FAQ_GERAL, DIFERENCIAIS, VIDEO_ANDAIME, relacionados,
)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICO = P.icon
PAGES = []                      # (path, prioridade, changefreq) para o sitemap


# ===========================================================================
# helpers
# ===========================================================================
def write(path, html, priority="0.7", changefreq="monthly", sitemap=True):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full) or ".", exist_ok=True)
    with io.open(full, "w", encoding="utf-8") as f:
        f.write(html)
    if sitemap:
        PAGES.append((path, priority, changefreq))
    print("  %-46s %6.1f KB" % (path, os.path.getsize(full) / 1024))


def r(path, depth):
    return P.rel(path, depth)


def faq_block(pares, title="Perguntas frequentes", lead=None, depth=0):
    items = "".join(
        '<details><summary>%s</summary><div class="faq__a"><p>%s</p></div></details>'
        % (q, a) for q, a in pares)
    head = ""
    if title:
        head = ('<div class="sec-head center"><p class="eyebrow">Tira-dúvidas</p>'
                '<h2>%s</h2>%s</div>'
                % (title, ('<p class="lead">%s</p>' % lead) if lead else ""))
    return """<section class="section section--paper">
  <div class="wrap">
    %s
    <div class="faq" data-faq>%s</div>
  </div>
</section>""" % (head, items)


def eq_cards(lista, depth):
    out = []
    for e in lista:
        out.append("""<a class="eq" href="%(href)s">
      <img class="eq__img" src="%(img)s" width="380" height="380" alt="%(alt)s" loading="lazy" decoding="async">
      <span class="eq__body">
        <span class="eq__t">%(nome)s</span>
        <span class="eq__d">%(res)s</span>
        <span class="eq__go">Ver e alugar %(arrow)s</span>
      </span>
    </a>""" % {
            "href": r("equipamentos/%s.html" % e["slug"], depth),
            "img": r("assets/img/banners/%s-card.webp" % e["slug"], depth),
            "alt": "Aluguel de %s no Rio de Janeiro" % e["nome"].lower(),
            "nome": e["nome"], "res": e["resumo"], "arrow": ICO("arrow"),
        })
    return '<div class="eqgrid">%s</div>' % "".join(out)


def unit_cards(depth, exclude=None):
    out = []
    for u in UNIDADES:
        if exclude and u["slug"] == exclude:
            continue
        out.append("""<article class="unit">
      <span class="unit__k">%(k)s</span>
      <h3>%(nome)s</h3>
      <div class="unit__meta">
        <div>%(ico_pin)s <span>%(rua)s<br>%(bairro)s, Rio de Janeiro &ndash; RJ</span></div>
        <div>%(ico_cl)s <span>%(hours)s</span></div>
        <div>%(ico_wa)s <a href="https://wa.me/%(wa)s" target="_blank" rel="noopener">%(wa_d)s</a></div>
      </div>
      <div class="unit__foot">
        <a class="link-arrow" href="%(href)s">Ver a unidade %(arrow)s</a>
      </div>
    </article>""" % {
            "k": "Matriz" if u.get("matriz") else "Unidade",
            "nome": u["nome"], "rua": u["rua"], "bairro": u["bairro"],
            "hours": P.HOURS_SHORT, "wa": u["wa"], "wa_d": u["wa_display"],
            "ico_pin": ICO("pin"), "ico_cl": ICO("clock"), "ico_wa": ICO("whatsapp"),
            "href": r("unidades/%s.html" % u["slug"], depth), "arrow": ICO("arrow"),
        })
    return '<div class="units">%s</div>' % "".join(out)


def quotes_block():
    out = []
    for d in DEPOIMENTOS:
        stars = "".join(ICO("star") for _ in range(d["nota"]))
        out.append("""<figure class="quote">
      <div class="stars" role="img" aria-label="%(n)d de 5 estrelas">%(stars)s</div>
      <blockquote><p>&ldquo;%(txt)s&rdquo;</p></blockquote>
      <figcaption class="quote__who">
        <span class="avatar" aria-hidden="true">%(ini)s</span>
        <span><b>%(nome)s</b><span>%(meta)s &middot; Google</span></span>
      </figcaption>
    </figure>""" % {
            "n": d["nota"], "stars": stars, "txt": d["texto"],
            "ini": d["nome"][0], "nome": d["nome"], "meta": d["meta"],
        })
    return '<div class="quotes">%s</div>' % "".join(out)


def pay_block():
    out = []
    for ico, nome, txt in PAGAMENTOS:
        out.append('<div class="pay">%s<span><b>%s</b><span>%s</span></span></div>'
                   % (ICO(ico), nome, txt))
    return '<div class="pays">%s</div>' % "".join(out)


def picker_block(depth):
    out = []
    for e in EQUIPAMENTOS:
        eid = "eq-" + e["slug"]
        out.append('<div class="pick"><input type="checkbox" id="%s" name="equipamento" value="%s">'
                   '<label for="%s">%s</label></div>' % (eid, e["nome"], eid, e["nome"]))
    return '<div class="picker" data-picker>%s</div>' % "".join(out)


# ===========================================================================
# HOME
# ===========================================================================
def page_index():
    path = "index.html"
    trail = [(None, "Início")]
    ld = S.dumps([
        S.organization(), S.website(),
        S.webpage(path, "Aluguel do Construtor - Locação de equipamentos no Rio de Janeiro",
                  "Locação de andaimes, betoneiras, marteletes e mais 12 categorias de "
                  "equipamentos para construção civil no Rio de Janeiro.",
                  primary_image="assets/img/hero-caminhao-andaimes.webp"),
        S.catalogo(path),
        S.lista_unidades(path),
        S.faqpage(path, FAQ_GERAL[:7]),
    ] + [S.unidade(u, full=False) for u in UNIDADES])

    feats = []
    for i, e in enumerate(DESTAQUES, start=1):
        tags = {
            "andaimes": ["Fachadeiro", "Tubular", "NR-18"],
            "betoneiras": ["Concreto", "Argamassa", "Revisada"],
            "marteletes": ["Perfurar", "Romper", "Brocas inclusas"],
        }.get(e["slug"], [])
        feats.append("""<a class="feat reveal" data-d="%(d)d" href="%(href)s">
      <div class="feat__media">
        <span class="feat__rank">Mais alugado</span>
        <img src="%(img)s" width="760" height="760" alt="%(alt)s" loading="lazy" decoding="async">
      </div>
      <div class="feat__body">
        <h3>%(nome)s</h3>
        <div class="feat__tags">%(tags)s</div>
        <p>%(res)s</p>
        <span class="link-arrow mt-4">Ver detalhes e alugar %(arrow)s</span>
      </div>
    </a>""" % {
            "d": i, "href": r("equipamentos/%s.html" % e["slug"], 0),
            "img": r("assets/img/banners/%s-card.webp" % e["slug"], 0),
            "alt": "Aluguel de %s no Rio de Janeiro" % e["nome"].lower(),
            "nome": e["nome"], "res": e["resumo"], "arrow": ICO("arrow"),
            "tags": "".join('<span class="tag">%s</span>' % t for t in tags),
        })

    difs = "".join("""<article class="card card--hover reveal" data-d="%d">
      <div class="icon-badge">%s</div>
      <h3>%s</h3><p>%s</p>
    </article>""" % (i % 4, ICO(ico), t, d)
        for i, (ico, t, d) in enumerate(DIFERENCIAIS))

    html = P.head(
        title="Aluguel do Construtor | Locação de Equipamentos no Rio de Janeiro",
        description=("Locação de andaimes, betoneiras, marteletes e mais 12 categorias para "
                     "obra no Rio de Janeiro. 5 unidades, entrega própria e orçamento no WhatsApp."),
        path=path, depth=0, preload="assets/img/hero-caminhao-andaimes.webp", extra=ld,
    )
    html += P.header(path, 0)

    html += """
<main id="conteudo">

<section class="hero hero--banner">
  <picture>
    <source media="(min-width: 900px)" srcset="assets/img/banners/hero-desktop.webp"
            width="1600" height="773">
    <img class="hero__bg" src="assets/img/banners/hero-mobile.webp" width="900" height="435"
         fetchpriority="high" decoding="async"
         alt="Caminhao do Aluguel do Construtor carregado no galpao, com estoque de equipamentos ao fundo">
  </picture>
  <div class="wrap hero__in">
    <div class="hero__copy">
      <div class="hero__badges">
        <span class="chip">%(ico_ck)s Equipamento revisado antes de sair</span>
        <span class="chip">%(ico_ck)s Entrega com frota própria</span>
      </div>
      <!-- H1 carrega os dois termos-alvo do AGENTS.md, "aluguel de
           equipamentos" e "Rio de Janeiro", que antes nao apareciam
           em lugar nenhum do H1. O gancho de marca fica no <em>. -->
      <h1>Aluguel de equipamentos para obra no Rio de Janeiro,
      <em>sem obra parada</em></h1>
      <p class="hero__lead">Andaimes, betoneiras, marteletes e mais 12 categorias, com peça
      conferida uma a uma, entrega no canteiro e orçamento respondido no WhatsApp. Cinco
      unidades no Rio de Janeiro, do Recreio a Botafogo.</p>
      <div class="btn-row mt-8">
        <a class="btn btn--wa btn--lg" href="%(wa)s" target="_blank" rel="noopener">%(ico_wa)s Pedir orçamento agora</a>
        <a class="btn btn--ghost btn--lg" href="%(eq)s">Ver os equipamentos</a>
      </div>
    </div>

    </div>
  </div>

  <div class="wrap">
    <div class="statbar">
      <div class="stat"><div class="stat__n"><span data-count="5">5</span></div><div class="stat__l">unidades no Rio de Janeiro</div></div>
      <div class="stat"><div class="stat__n"><span data-count="15">15</span></div><div class="stat__l">categorias de equipamento</div></div>
      <div class="stat"><div class="stat__n"><span data-count="40">40</span><small>+</small></div><div class="stat__l">bairros atendidos</div></div>
      <div class="stat"><div class="stat__n">100<small>%%</small></div><div class="stat__l">dos itens revisados antes de sair</div></div>
    </div>
  </div>
</section>

<div class="trustbar">
  <div class="wrap trustbar__in">
    <div class="trustbar__i">%(ico_shield)s <span><b>Inspeção antes de cada saída</b>Solda, encaixe, motor e piso conferidos</span></div>
    <div class="trustbar__i">%(ico_truck)s <span><b>Frota própria</b>Entrega e retirada sem depender de terceiro</span></div>
    <div class="trustbar__i">%(ico_clock)s <span><b>Diária, semana ou mês</b>Período que acompanha o ritmo da obra</span></div>
    <div class="trustbar__i">%(ico_pix)s <span><b>PIX, cartão e boleto</b>Inclusive faturamento para empresa</span></div>
  </div>
</div>

<section class="section section--paper">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Os mais alugados</p>
      <h2>Aluguel de andaimes, betoneiras e marteletes</h2>
      <p class="lead">Andaime, betoneira e martelete respondem por boa parte dos pedidos que
      chegam aqui. São também os itens em que a diferença entre equipamento bem cuidado e
      equipamento cansado aparece logo no primeiro dia.</p>
    </div>
    <div class="feat3">%(feats)s</div>
  </div>
</section>

<!-- Faixa de largura inteira: a arte e o fundo e o texto vem por cima, na
     metade escura da esquerda. Duas artes, enquadramentos diferentes por tela,
     por isso <picture> com media e nao srcset. -->
<section class="section section--dark section--art">
  <picture>
    <source media="(min-width: 900px)" srcset="assets/img/banners/linha-completa-desktop.webp"
            width="1600" height="650">
    <img class="section__art" src="assets/img/banners/linha-completa-mobile.webp"
         width="1200" height="1200" loading="lazy" decoding="async"
         alt="Compactador, lavadora de alta pressão, motosserra, serra circular e parafusadeira da linha alugada">
  </picture>
  <div class="wrap">
    <div class="section__copy">
      <p class="eyebrow">Linha completa</p>
      <h2>Do escoramento da laje à limpeza do pós-obra</h2>
      <p class="lead">São 15 categorias que cobrem a obra do começo ao fim. Você aluga tudo
      no mesmo lugar, com uma entrega só e um contato só, em vez de coordenar quatro
      fornecedores diferentes.</p>
      <ul class="checks mt-6">
        <li><strong>Estrutura e altura:</strong> andaimes, escoras e escadas</li>
        <li><strong>Concreto e demolição:</strong> betoneiras, marteletes e compactadores</li>
        <li><strong>Corte e acabamento:</strong> cortadores de piso, serras, plainas e lixadeiras</li>
        <li><strong>Limpeza e pós-obra:</strong> lavadoras, aspiradores, sopradores e bombas</li>
      </ul>
      <div class="btn-row mt-8">
        <a class="btn btn--primary" href="%(eq)s">Ver as 15 categorias</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--sand section--steps">
  <div class="wrap">
    <div class="sec-head center">
      <p class="eyebrow">Como funciona</p>
      <h2>Quatro passos entre o WhatsApp e o equipamento na obra</h2>
    </div>
    <div class="steps">
      <article class="step reveal"><h3>Manda a lista</h3><p>Diga o que precisa, o endereço da obra e por quanto tempo. Foto ou áudio serve.</p></article>
      <article class="step reveal" data-d="1"><h3>Recebe o orçamento</h3><p>Respondemos com disponibilidade, valor e prazo. Sem cadastro e sem formulário longo.</p></article>
      <article class="step reveal" data-d="2"><h3>Confirma e agenda</h3><p>Você escolhe a data e a janela de entrega que funcionam para o canteiro.</p></article>
      <article class="step reveal" data-d="3"><h3>Usa e devolve</h3><p>A gente entrega, acompanha durante o período e retira quando o serviço acabar.</p></article>
    </div>
  </div>
</section>
<section class="section section--dark section--video">
  <div class="wrap">
    <div class="split split--video">
      <div class="split--video__txt">
        <p class="eyebrow">Em vídeo</p>
        <h2>Andaime fachadeiro,<br>de perto</h2>
        <p class="lead">Antes de alugar, veja o equipamento. Painel, travessa, diagonal e
        piso montados, do jeito que chega no seu canteiro.</p>
        <div class="chips-col">
          <span class="chip">%(ico_ck)s Pintura de fachada</span>
          <span class="chip">%(ico_ck)s Revestimento em altura</span>
          <span class="chip">%(ico_ck)s Reforma e manutenção</span>
        </div>
        <div class="btn-row mt-8">
          <a class="btn btn--wa btn--lg" href="%(wa)s" target="_blank" rel="noopener">%(ico_wa)s Pedir orçamento</a>
          <a class="btn btn--ghost btn--lg" href="%(v_and)s">Ver andaimes</a>
        </div>
      </div>
      <div class="split--video__media">
        <span class="split--video__num" aria-hidden="true">01</span>
        %(video)s
      </div>
    </div>
  </div>
</section>


<section class="section section--paper">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Por que a gente</p>
      <h2>O que muda quando a locadora entende de obra</h2>
      <p class="lead">Locação de equipamento parece commodity até o dia em que chega peça
      faltando, motor cansado ou entrega no horário errado. A diferença está no operacional,
      não no catálogo.</p>
    </div>
    <div class="grid grid--3">%(difs)s</div>
  </div>
</section>

<section class="section section--white">
  <div class="wrap">
    <div class="split split--rev">
      <figure class="figure">
        <img src="assets/img/carregamento-equipamentos.webp" width="1200" height="800" loading="lazy" decoding="async"
             alt="Equipe do Aluguel do Construtor amarrando a carga de andaimes no caminhão antes da entrega">
      </figure>
      <div>
        <p class="eyebrow">Segurança</p>
        <h2>Equipamento certificado é o mínimo, não o diferencial</h2>
        <p>Cada item passa por inspeção, limpeza e manutenção preventiva antes de sair do
        galpão. Andaime tem solda, encaixe e piso conferidos. Betoneira tem motor, correia e
        coroa checados. Ferramenta elétrica tem cabo, escova e proteção testados.</p>
        <p>Trabalhamos dentro do que as normas de segurança exigem, entre elas a
        <strong>NR-12</strong>, de máquinas e equipamentos, e a <strong>NR-18</strong>, de
        condições no canteiro. A responsabilidade técnica pela montagem e pelo uso continua
        sendo do responsável pela obra, e a gente ajuda com orientação sempre que precisar.</p>
        <ul class="checks mt-6">
          <li>Inspeção item a item antes de cada saída</li>
          <li>Reposição rápida de peça danificada durante o uso</li>
          <li>Orientação de montagem e de operação por WhatsApp</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="wrap">
    <div class="sec-head center">
      <p class="eyebrow">Onde estamos</p>
      <h2>Cinco unidades, do Recreio a Botafogo</h2>
      <p class="lead">Cada unidade atende a sua região com o mesmo catálogo. Quanto mais perto
      a base, mais curto o prazo de entrega e mais fácil resolver imprevisto no meio da obra.</p>
    </div>
    %(units)s
    <div class="btn-row center mt-8"><a class="btn btn--dark" href="%(un)s">Ver todas as unidades e endereços</a></div>
  </div>
</section>

<section class="section section--white">
  <div class="wrap">
    <div class="sec-head center">
      <p class="eyebrow">Quem já alugou</p>
      <h2>Quem constrói com a gente recomenda</h2>
      <p class="lead">Avaliações públicas deixadas por clientes no Google.</p>
    </div>
    %(quotes)s
  </div>
</section>

<section class="section section--sand">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Pagamento</p>
      <h2>Facilidade para pagar, rapidez para construir</h2>
      <p class="lead">Escolha a forma que se encaixa na realidade da sua empresa ou do seu
      projeto. Para construtora e empreiteira, o boleto com prazo combinado é o formato mais usado.</p>
    </div>
    %(pays)s
  </div>
</section>

<section class="section section--white">
  <div class="wrap">
    <div class="split">
      <figure class="figure">
        <img src="assets/img/unidade-parceira-fachada.webp" width="1000" height="750" loading="lazy" decoding="async"
             alt="Fachada de loja parceira que opera uma unidade do Aluguel do Construtor">
      </figure>
      <div>
        <p class="eyebrow">Para lojistas</p>
        <h2>Tenha uma unidade do Aluguel do Construtor na sua loja</h2>
        <p class="lead">Se você já tem uma loja de material de construção, a locação de
        equipamentos é a receita que falta: usa o mesmo público, o mesmo espaço e traz o
        cliente de volta várias vezes por obra.</p>
        <div class="btn-row mt-6">
          <a class="btn btn--primary" href="%(parceiro)s">Como funciona a parceria</a>
        </div>
      </div>
    </div>
  </div>
</section>

%(faq)s

</main>
""" % {
        "ico_ck": ICO("check"), "ico_wa": ICO("whatsapp"), "ico_truck": ICO("truck"),
        "ico_shield": ICO("shield"), "ico_clock": ICO("clock"), "ico_pix": ICO("pix"),
        "wa": P.WA_DEFAULT, "eq": "equipamentos.html", "un": "unidades.html",
        "parceiro": "seja-parceiro.html",
        "feats": "".join(feats), "difs": difs,
        "v_and": "equipamentos/andaimes.html",
        "video": P.video(0, VIDEO_ANDAIME["id"], VIDEO_ANDAIME["titulo"],
                         VIDEO_ANDAIME["capa"], VIDEO_ANDAIME["alt"],
                         VIDEO_ANDAIME["legenda"]),
        "units": unit_cards(0), "quotes": quotes_block(), "pays": pay_block(),
        "faq": faq_block(FAQ_GERAL[:7],
                         "Dúvidas de quem vai alugar pela primeira vez",
                         'Não achou a sua? <a href="perguntas-frequentes.html">Veja a lista completa</a> ou pergunte no WhatsApp.'),
    }

    html += P.cta(0)
    html += P.footer(0)
    write(path, html, "1.0", "weekly")


# ===========================================================================
# HUB DE EQUIPAMENTOS
# ===========================================================================
def page_equipamentos():
    path = "equipamentos.html"
    trail = [("index.html", "Início"), (None, "Equipamentos")]
    ld = S.dumps([
        S.organization(), S.website(),
        S.webpage(path, "Equipamentos para locação", "Catálogo completo de equipamentos "
                  "para construção civil disponíveis para locação no Rio de Janeiro.",
                  breadcrumb_id=P.url(path) + "#breadcrumb", page_type="CollectionPage"),
        S.breadcrumb(path, trail),
        S.catalogo(path),
    ] + [S.equipamento(e) for e in EQUIPAMENTOS])

    html = P.head(
        title="Equipamentos para Locação no Rio de Janeiro | Catálogo",
        description=("Andaimes, betoneiras, marteletes, compactadores, escoras, serras e "
                     "mais. Locação por dia, semana ou mês no Rio de Janeiro, com entrega."),
        path=path, depth=0, extra=ld)
    html += P.header(path, 0)

    html += """
<main id="conteudo">
<section class="pagehead">
  <div class="wrap pagehead__in">
    %(crumbs)s
    <h1>Equipamentos para locação no Rio de Janeiro</h1>
    <p class="lead">Quinze categorias que cobrem a obra do escoramento da laje à limpeza do
    pós-obra. Tudo revisado antes de sair, com entrega e retirada por frota própria.
    Monte a sua lista abaixo e receba o orçamento no WhatsApp.</p>
    <div class="btn-row mt-6">
      <a class="btn btn--wa" href="%(wa)s" target="_blank" rel="noopener">%(ico_wa)s Pedir orçamento</a>
      <a class="btn btn--ghost" href="#montar">Montar minha lista</a>
    </div>
  </div>
</section>
<div class="hazard" role="presentation"></div>

<section class="section section--paper">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Catálogo</p>
      <h2>Escolha a categoria e veja o que considerar antes de alugar</h2>
      <p class="lead">Cada página traz onde o equipamento se aplica, o que perguntar antes de
      fechar e as dúvidas mais comuns. É a informação que evita alugar o modelo errado.</p>
    </div>
    %(cards)s
  </div>
</section>

<section class="section section--white" id="montar">
  <div class="wrap wrap--narrow">
    <img src="assets/img/profissional-whatsapp.webp" width="720" height="720" loading="lazy" decoding="async"
         style="max-width:220px;margin:0 auto 8px"
         alt="Profissional de obra pedindo orçamento pelo WhatsApp">
    <div class="sec-head center">
      <p class="eyebrow">Orçamento em minutos</p>
      <h2>Monte a sua lista e receba o orçamento no WhatsApp</h2>
      <p class="lead">Marque os equipamentos, preencha o essencial e a gente monta a mensagem
      para você. Nenhum dado é armazenado: o formulário só abre a conversa já escrita.</p>
    </div>

    <form class="form" data-wa-form="%(wanum)s">
      %(picker)s
      <p class="form__note" data-picker-count>Nenhum item selecionado</p>

      <div class="form__row">
        <div class="field">
          <label for="f-nome">Seu nome <span class="req">*</span></label>
          <input id="f-nome" name="nome" type="text" required autocomplete="name">
        </div>
        <div class="field">
          <label for="f-tel">WhatsApp <span class="req">*</span></label>
          <input id="f-tel" name="telefone" type="tel" required autocomplete="tel" placeholder="(21) 90000-0000">
        </div>
      </div>

      <div class="form__row">
        <div class="field">
          <label for="f-bairro">Bairro da obra</label>
          <input id="f-bairro" name="bairro" type="text" placeholder="Recreio, Barra, Botafogo...">
        </div>
        <div class="field">
          <label for="f-periodo">Período de locação</label>
          <select id="f-periodo" name="periodo">
            <option value="">Selecione</option>
            <option>Diária</option>
            <option>Semanal</option>
            <option>Quinzenal</option>
            <option>Mensal</option>
            <option>Ainda não sei</option>
          </select>
        </div>
      </div>

      <div class="field">
        <label for="f-msg">Detalhes da obra</label>
        <textarea id="f-msg" name="mensagem" placeholder="Ex.: fachada de 3 pavimentos para pintar, preciso de andaime fachadeiro e escada."></textarea>
      </div>

      <button class="btn btn--wa btn--lg btn--block" type="submit">%(ico_wa)s Enviar pelo WhatsApp</button>
      <p class="form__note" data-form-ok hidden>Abrimos o WhatsApp com a sua mensagem pronta. Se não abriu, chame direto em %(phone)s.</p>
    </form>
  </div>
</section>

<section class="section section--sand">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Antes de fechar</p>
      <h2>Quatro perguntas que evitam alugar o equipamento errado</h2>
    </div>
    <div class="grid grid--4">
      <article class="card"><div class="icon-badge">%(ico_ruler)s</div><h3>Qual a medida real?</h3><p>Altura do serviço, pé-direito da laje, diâmetro do furo. Medida certa evita segunda viagem.</p></article>
      <article class="card"><div class="icon-badge">%(ico_layers)s</div><h3>Qual o material?</h3><p>Concreto armado, alvenaria e porcelanato pedem disco, broca e ponteiro diferentes.</p></article>
      <article class="card"><div class="icon-badge">%(ico_gauge)s</div><h3>Qual o volume de trabalho?</h3><p>Uso pontual e uso contínuo pedem máquinas de porte diferente e mudam o custo total.</p></article>
      <article class="card"><div class="icon-badge">%(ico_shield)s</div><h3>Como é o canteiro?</h3><p>Energia disponível, ponto de água, acesso para caminhão e piso de apoio mudam o que dá para usar.</p></article>
    </div>
  </div>
</section>

%(faq)s
</main>
""" % {
        "crumbs": P.crumbs(trail, 0), "wa": P.WA_DEFAULT, "wanum": P.WA,
        "ico_wa": ICO("whatsapp"), "ico_ruler": ICO("ruler"), "ico_layers": ICO("layers"),
        "ico_gauge": ICO("gauge"), "ico_shield": ICO("shield"),
        "cards": eq_cards(EQUIPAMENTOS, 0), "picker": picker_block(0),
        "phone": P.PHONE_DISPLAY,
        "faq": faq_block(FAQ_GERAL[1:5], "Como funciona a locação"),
    }

    html += P.cta(0)
    html += P.footer(0)
    write(path, html, "0.9", "weekly")


# ===========================================================================
# PAGINA DE EQUIPAMENTO
# ===========================================================================
def page_equipamento(e):
    path = "equipamentos/%s.html" % e["slug"]
    depth = 1
    trail = [("index.html", "Início"), ("equipamentos.html", "Equipamentos"), (None, e["nome"])]

    ld = S.dumps([
        S.organization(), S.website(),
        S.webpage(path, e["h1"], e["desc"], breadcrumb_id=P.url(path) + "#breadcrumb",
                  primary_image="assets/img/equipamentos/%s.webp" % e["slug"],
                  page_type="ItemPage"),
        S.breadcrumb(path, trail),
        S.equipamento(e),
        S.faqpage(path, e["faq"]),
    ])

    usos = "".join("<li>%s</li>" % u for u in e["usos"])
    escolher = "".join(
        "<li><strong>%s</strong>%s</li>" % (t, d) for t, d in e["escolher"])
    inclui = "".join("<li>%s</li>" % i for i in e["inclui"])
    intro = "".join("<p>%s</p>" % p for p in e["intro"])
    norma = ""
    if e.get("norma"):
        norma = ('<div class="callout"><p><b>Segurança.</b> %s</p></div>' % e["norma"])

    sidelist = "".join(
        '<li><a href="%s"%s><img src="%s" width="28" height="28" alt="" loading="lazy" decoding="async">%s</a></li>'
        % (r("equipamentos/%s.html" % x["slug"], depth),
           ' aria-current="page"' if x["slug"] == e["slug"] else "",
           r("assets/img/equipamentos/%s-380.webp" % x["slug"], depth), x["nome"])
        for x in EQUIPAMENTOS)

    wa_txt = ("Olá! Quero um orçamento de locação de %s. A obra fica em: "
              % e["nome"].lower())
    wa = P.wa_link(wa_txt)

    sinon = e.get("sinonimos", [])
    sinon_txt = ""
    if sinon:
        sinon_txt = ('<p class="form__note mt-6">Também procurado como: %s.</p>'
                     % ", ".join(sinon))

    # Banner opcional no hero, por equipamento (chave "banner" em EQUIPAMENTOS).
    # Quem tem banner usa o hero de largura inteira com o texto por cima; quem
    # nao tem continua com a foto quadrada do produto ao lado do texto.
    banner = e.get("banner")
    if banner:
        # Par de artes por categoria em assets/img/banners/<slug>-desktop.webp
        # (1600x650) e <slug>-mobile.webp (1200x1200). Sao enquadramentos
        # diferentes, nao so tamanhos, entao <picture> com media e nao srcset.
        _desk = r("assets/img/banners/%s-desktop.webp" % e["slug"], depth)
        _mob = r("assets/img/banners/%s-mobile.webp" % e["slug"], depth)
        _alt = "%s para locação no Rio de Janeiro" % e["nome"]
        bg = ('\n  <picture>\n'
              '    <source media="(min-width: 900px)" srcset="%s" width="1600" height="650">\n'
              '    <img class="pagehead__bg" src="%s" width="1200" height="1200"\n'
              '         fetchpriority="high" decoding="async" alt="%s">\n'
              '  </picture>' % (_desk, _mob, _alt))
        head_cls = " pagehead--banner"
        abre = '<div class="pagehead__copy mt-6">'
        # Em tela pequena o banner fica atras E a foto do produto aparece
        # abaixo do texto, como nas outras paginas de equipamento: no celular
        # e ela que identifica o item. No desktop o banner ja faz esse papel,
        # entao o CSS esconde. Usa a variante de 380px porque so renderiza
        # em tela estreita, e lazy para nao competir com o banner no LCP.
        # srcset com as duas larguras: em aparelho de densidade 2x a foto ocupa
        # ~390 CSS px, ou seja 780 fisicos, e o arquivo de 380 sairia borrado.
        fecha = ('</div>\n      <img class="pagehead__img pagehead__img--mini" src="%s"\n'
                 '           srcset="%s 380w, %s 760w" sizes="(max-width: 939px) 92vw, 520px"\n'
                 '           width="380" height="380" loading="lazy" decoding="async" alt="%s">'
                 % (r("assets/img/equipamentos/%s-380.webp" % e["slug"], depth),
                    r("assets/img/equipamentos/%s-380.webp" % e["slug"], depth),
                    r("assets/img/equipamentos/%s.webp" % e["slug"], depth),
                    "%s disponíveis para locação no Rio de Janeiro" % e["nome"]))
        preload = "assets/img/banners/%s-mobile.webp" % e["slug"]
    else:
        bg = ""
        head_cls = ""
        abre = '<div class="pagehead--split mt-6">\n      <div>'
        fecha = ('</div>\n      <img class="pagehead__img" src="%s" width="760" height="760"\n'
                 '           fetchpriority="high" decoding="async" alt="%s">\n    </div>'
                 % (r("assets/img/equipamentos/%s.webp" % e["slug"], depth),
                    "%s disponíveis para locação no Rio de Janeiro" % e["nome"]))
        preload = "assets/img/equipamentos/%s.webp" % e["slug"]

    html = P.head(title=e["title"], description=e["desc"], path=path, depth=depth,
                  preload=preload, extra=ld)
    html += P.header("equipamentos.html", depth)

    html += """
<main id="conteudo">
<section class="pagehead%(head_cls)s">%(bg)s
  <div class="wrap pagehead__in">
    %(crumbs)s
    %(abre)s
        <p class="eyebrow">Locação de equipamentos</p>
        <h1>%(h1)s</h1>
        <p class="lead">%(resumo)s</p>
        <div class="hero__badges mt-6">
          <span class="chip">%(ico_ck)s Revisado antes de sair</span>
          <span class="chip">%(ico_ck)s Diária, semana ou mês</span>
          <span class="chip">%(ico_ck)s Entrega na obra</span>
        </div>
        <div class="btn-row mt-6">
          <a class="btn btn--wa btn--lg" href="%(wa)s" target="_blank" rel="noopener">%(ico_wa)s Pedir orçamento</a>
          <a class="btn btn--ghost btn--lg" href="%(eq)s">Ver todos os equipamentos</a>
        </div>
      %(fecha)s
  </div>
</section>
<div class="hazard" role="presentation"></div>

<section class="section section--paper">
  <div class="wrap eqlayout">
    <div class="prose">
      %(intro)s
      %(video)s

      <h2>Onde esse equipamento se aplica</h2>
      <ul>%(usos)s</ul>

      <h2>O que considerar antes de alugar</h2>
      <ul class="rulelist">%(escolher)s</ul>

      %(norma)s

      <h2>O que está incluído na locação</h2>
      <ul class="checks">%(inclui)s</ul>

      <h2>Períodos de locação</h2>
      <p>Você aluga pelo tempo que a obra precisa, sem pacote fechado que não faz sentido
      para o seu cronograma.</p>
      <table>
        <caption>Se a obra atrasar, avise antes do fim do período que renovamos sem interromper o serviço.</caption>
        <thead><tr><th>Período</th><th>Indicado para</th></tr></thead>
        <tbody>
          <tr><td>Diária</td><td>Serviço pontual, um dia de frente de trabalho</td></tr>
          <tr><td>Semanal</td><td>Etapa curta, reforma de ambiente</td></tr>
          <tr><td>Quinzenal</td><td>Reforma completa de apartamento ou casa</td></tr>
          <tr><td>Mensal</td><td>Obra de fachada, escoramento e canteiro em atividade</td></tr>
        </tbody>
      </table>

      <h2>Entrega no Rio de Janeiro</h2>
      <p>Entregamos e retiramos com frota própria a partir das nossas cinco unidades:
      duas no <a href="%(u1)s">Recreio dos Bandeirantes</a>, uma em
      <a href="%(u2)s">Vargem Grande</a>, uma em <a href="%(u3)s">Pedra de Guaratiba</a>
      e uma em <a href="%(u4)s">Botafogo</a>. Isso cobre a Barra da Tijuca e o Recreio,
      as vargens, Jacarepaguá e entorno, a região de Guaratiba, Campo Grande, a Zona Sul
      inteira e parte da Zona Norte.</p>
      %(sinon)s
    </div>

    <aside class="aside">
      <div class="aside__card aside__card--dark">
        <h3>Orçamento em minutos</h3>
        <p>Manda a lista, o endereço da obra e o período. A gente responde com
        disponibilidade e valor.</p>
        <a class="btn btn--wa btn--block mt-4" href="%(wa)s" target="_blank" rel="noopener">%(ico_wa)s Falar no WhatsApp</a>
        <a class="btn btn--ghost btn--block mt-2" href="%(tel)s">%(ico_ph)s %(phone)s</a>
      </div>
      <div class="aside__card">
        <h3>Todos os equipamentos</h3>
        <ul class="sidelist mt-4">%(sidelist)s</ul>
      </div>
    </aside>
  </div>
</section>

%(faq)s

<section class="section section--white">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Veja também</p>
      <h2>Equipamentos que costumam ir junto</h2>
    </div>
    %(rel)s
  </div>
</section>
</main>
""" % {
        "crumbs": P.crumbs(trail, depth), "h1": e["h1"], "resumo": e["resumo"],
        "ico_ck": ICO("check"), "ico_wa": ICO("whatsapp"), "ico_ph": ICO("phone"),
        "wa": wa, "eq": r("equipamentos.html", depth),
        "head_cls": head_cls, "bg": bg, "abre": abre, "fecha": fecha,
        # video so na pagina que tem "video" declarado em EQUIPAMENTOS
        "video": (P.video(depth, VIDEO_ANDAIME["id"], VIDEO_ANDAIME["titulo"],
                          VIDEO_ANDAIME["capa"], VIDEO_ANDAIME["alt"],
                          VIDEO_ANDAIME["legenda"])
                  if e.get("video") else ""),
        "intro": intro, "usos": usos, "escolher": escolher, "norma": norma, "inclui": inclui,
        "u1": r("unidades/recreio-dos-bandeirantes.html", depth),
        "u2": r("unidades/vargem-grande.html", depth),
        "u3": r("unidades/pedra-de-guaratiba.html", depth),
        "u4": r("unidades/botafogo.html", depth),
        "sinon": sinon_txt,
        "tel": "tel:" + P.PHONE_TEL, "phone": P.PHONE_DISPLAY,
        "sidelist": sidelist,
        "faq": faq_block(e["faq"], "Dúvidas sobre %s" % e["nome"].lower()),
        "rel": eq_cards(relacionados(e["slug"], 4), depth),
    }

    html += P.cta(depth, title="Precisa de %s para a sua obra?" % e["nome"].lower())
    html += P.footer(depth)
    write(path, html, "0.8", "monthly")


# ===========================================================================
# HUB DE UNIDADES
# ===========================================================================
def page_unidades():
    path = "unidades.html"
    trail = [("index.html", "Início"), (None, "Unidades")]
    ld = S.dumps([
        S.organization(), S.website(),
        S.webpage(path, "Unidades no Rio de Janeiro",
                  "Endereços, horários e WhatsApp das cinco unidades do Aluguel do Construtor.",
                  breadcrumb_id=P.url(path) + "#breadcrumb", page_type="CollectionPage"),
        S.breadcrumb(path, trail),
        S.lista_unidades(path),
    ] + [S.unidade(u) for u in UNIDADES])

    html = P.head(
        title="Unidades no Rio de Janeiro | Aluguel do Construtor",
        description=("Cinco unidades no Rio de Janeiro: Recreio dos Bandeirantes (2), "
                     "Vargem Grande, Pedra de Guaratiba e Botafogo. Endereço, horário e "
                     "WhatsApp de cada uma."),
        path=path, depth=0, extra=ld)
    html += P.header(path, 0)

    html += """
<main id="conteudo">
<section class="pagehead pagehead--banner">
  <img class="pagehead__bg" src="assets/img/banner-unidades-mapa.webp"
       srcset="assets/img/banner-unidades-mapa-980.webp 980w, assets/img/banner-unidades-mapa.webp 1957w"
       sizes="100vw" width="1957" height="775"
       fetchpriority="high" decoding="async" alt="">
  <div class="wrap pagehead__in">
    %(crumbs)s
    <div class="pagehead__copy mt-6">
      <p class="eyebrow">Cobertura no Rio</p>
      <h1>Nossas unidades no Rio de Janeiro</h1>
      <p class="lead">Cinco bases operando com o mesmo catálogo e o mesmo padrão de revisão.
      Fale com a unidade mais perto da sua obra: o prazo de entrega encurta e resolver
      imprevisto no meio do serviço fica muito mais simples.</p>
    </div>
  </div>
</section>
<div class="hazard" role="presentation"></div>

<section class="section section--paper">
  <div class="wrap">
    %(units)s
  </div>
</section>

<section class="section section--white">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="eyebrow">Cobertura</p>
        <h2>Onde entregamos</h2>
        <p class="lead">A entrega e a retirada são feitas com frota própria a partir da
        unidade mais próxima da obra. Estas são as regiões que atendemos com mais frequência:</p>
        <ul class="checks mt-6">
          <li><strong>Barra, Recreio e vargens:</strong> Recreio dos Bandeirantes, Barra da Tijuca, Barra Olímpica, São Conrado, Joá, Itanhangá, Grumari, Vargem Grande, Vargem Pequena, Camorim</li>
          <li><strong>Jacarepaguá e entorno:</strong> Jacarepaguá, Freguesia (Jacarepaguá), Pechincha, Taquara, Tanque, Praça Seca, Anil, Gardênia Azul, Curicica, Cidade de Deus</li>
          <li><strong>Guaratiba, Campo Grande e Zona Oeste:</strong> Pedra de Guaratiba, Guaratiba, Barra de Guaratiba, Campo Grande, Santa Cruz, Sepetiba, Cosmos, Senador Vasconcelos, Santíssimo, Bangu, Realengo</li>
          <li><strong>Zona Sul:</strong> Botafogo, Humaitá, Flamengo, Laranjeiras, Catete, Copacabana, Ipanema, Leblon, Urca, Gávea, Jardim Botânico</li>
          <li><strong>Zona Norte:</strong> Madureira, Méier, Irajá, Penha</li>
        </ul>
        <p class="mt-6">A obra fica fora dessas regiões? Chame no WhatsApp mesmo assim.
        Dependendo do equipamento e do período, conseguimos atender.</p>
      </div>
      <figure class="figure">
        <img src="assets/img/estoque-andaimes-galpao.webp" width="900" height="1120" loading="lazy" decoding="async"
             alt="Andaimes empilhados e prontos para carga no galpão do Aluguel do Construtor">
      </figure>
    </div>
  </div>
</section>

%(faq)s
</main>
""" % {
        "crumbs": P.crumbs(trail, 0), "units": unit_cards(0),
        "faq": faq_block([FAQ_GERAL[3], FAQ_GERAL[7], FAQ_GERAL[5]], "Dúvidas sobre atendimento e entrega"),
    }

    html += P.cta(0)
    html += P.footer(0)
    write(path, html, "0.9", "monthly")


# ===========================================================================
# PAGINA DE UNIDADE
# ===========================================================================
def page_unidade(u):
    path = "unidades/%s.html" % u["slug"]
    depth = 1
    trail = [("index.html", "Início"), ("unidades.html", "Unidades"), (None, u["bairro"])]
    title = u["seo_title"]
    desc = u["seo_desc"]

    ld = S.dumps([
        S.organization(), S.website(),
        S.webpage(path, title, desc, breadcrumb_id=P.url(path) + "#breadcrumb"),
        S.breadcrumb(path, trail),
        S.unidade(u),
    ])

    atende = "".join("<li>%s</li>" % a for a in u["atende"])
    wa = P.wa_link("Olá! Quero um orçamento na unidade %s." % u["nome"], number=u["wa"])

    html = P.head(title=title, description=desc, path=path, depth=depth, extra=ld)
    html += P.header("unidades.html", depth)

    html += """
<main id="conteudo">
<section class="pagehead">
  <div class="wrap pagehead__in">
    %(crumbs)s
    <p class="eyebrow mt-6">%(kind)s</p>
    <h1>Aluguel de equipamentos em %(bairro)s</h1>
    <p class="lead">%(sobre)s</p>
    <div class="btn-row mt-6">
      <a class="btn btn--wa btn--lg" href="%(wa)s" target="_blank" rel="noopener">%(ico_wa)s WhatsApp %(wa_d)s</a>
      <a class="btn btn--ghost btn--lg" href="%(maps)s" target="_blank" rel="noopener">%(ico_pin)s Ver no mapa</a>
    </div>
  </div>
</section>
<div class="hazard" role="presentation"></div>

<section class="section section--paper">
  <div class="wrap eqlayout">
    <div class="prose">
      <h2>Endereço e horário</h2>
      <p><strong>%(rua)s</strong><br>%(bairro)s, Rio de Janeiro &ndash; RJ</p>
      <p>%(hours_long)s</p>
      <p>WhatsApp da unidade: <a href="%(wa)s" target="_blank" rel="noopener">%(wa_d)s</a></p>

      <h2>Bairros atendidos por esta unidade</h2>
      <ul>%(atende)s</ul>
      <p>A entrega e a retirada saem daqui com frota própria. Se a sua obra fica em um bairro
      vizinho que não está na lista, chame no WhatsApp: na maior parte dos casos conseguimos
      atender do mesmo jeito.</p>

      <h2>O que você aluga nesta unidade</h2>
      <p>O catálogo é o mesmo em todas as unidades: 15 categorias de equipamento, do
      escoramento de laje à limpeza de pós-obra. Os mais procurados são
      <a href="%(e1)s">andaimes</a>, <a href="%(e2)s">betoneiras</a> e
      <a href="%(e3)s">marteletes</a>.</p>

      <h2>Como pedir um orçamento</h2>
      <p>Chame no WhatsApp desta unidade com três informações: o que você precisa, o
      endereço da obra e por quanto tempo. A gente responde com disponibilidade, valor e
      prazo de entrega. Não tem cadastro obrigatório nem formulário longo.</p>
    </div>

    <aside class="aside">
      <div class="aside__card aside__card--dark">
        <h3>Falar com %(curta)s</h3>
        <p>%(hours_long)s</p>
        <a class="btn btn--wa btn--block mt-4" href="%(wa)s" target="_blank" rel="noopener">%(ico_wa)s %(wa_d)s</a>
        <a class="btn btn--ghost btn--block mt-2" href="%(maps)s" target="_blank" rel="noopener">Como chegar</a>
      </div>
      <div class="aside__card">
        <h3>Outras unidades</h3>
        <ul class="sidelist mt-4">%(outras)s</ul>
      </div>
    </aside>
  </div>
</section>

<section class="section section--white">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Catálogo</p>
      <h2>Equipamentos disponíveis em %(bairro)s</h2>
    </div>
    %(cards)s
    <div class="btn-row center mt-8"><a class="btn btn--dark" href="%(eq)s">Ver o catálogo completo</a></div>
  </div>
</section>
</main>
""" % {
        "crumbs": P.crumbs(trail, depth),
        "kind": "Matriz" if u.get("matriz") else "Unidade",
        "bairro": u["bairro"], "sobre": u["sobre"], "rua": u["rua"],
        "hours_long": P.HOURS_LONG, "wa": wa, "wa_d": u["wa_display"],
        "maps": P.maps_link(u["endereco"]),
        "ico_wa": ICO("whatsapp"), "ico_pin": ICO("pin"),
        "atende": atende, "curta": u["titulo_curto"],
        "e1": r("equipamentos/andaimes.html", depth),
        "e2": r("equipamentos/betoneiras.html", depth),
        "e3": r("equipamentos/marteletes.html", depth),
        "outras": "".join(
            '<li><a href="%s">%s</a></li>' % (r("unidades/%s.html" % o["slug"], depth), o["bairro"])
            for o in UNIDADES if o["slug"] != u["slug"]),
        "cards": eq_cards(EQUIPAMENTOS[:8], depth),
        "eq": r("equipamentos.html", depth),
    }

    html += P.cta(depth, title="Sua obra em %s não pode parar." % u["bairro"],
                  primary=wa)
    html += P.footer(depth)
    write(path, html, "0.8", "monthly")


# ===========================================================================
# QUEM SOMOS
# ===========================================================================
def page_quem_somos():
    path = "quem-somos.html"
    trail = [("index.html", "Início"), (None, "Quem somos")]
    ld = S.dumps([
        S.organization(), S.website(),
        S.webpage(path, "Quem somos", "A história, a missão e os valores do Aluguel do Construtor.",
                  breadcrumb_id=P.url(path) + "#breadcrumb", page_type="AboutPage"),
        S.breadcrumb(path, trail),
    ])

    html = P.head(
        title="Quem Somos | Aluguel do Construtor - Locação no Rio de Janeiro",
        description=("Locadora de equipamentos para construção civil no Rio de Janeiro, com "
                     "cinco unidades, frota própria e atendimento de quem entende de obra."),
        path=path, depth=0, extra=ld)
    html += P.header(path, 0)

    html += """
<main id="conteudo">
<section class="pagehead">
  <div class="wrap pagehead__in">
    %(crumbs)s
    <h1>Mais do que equipamento. A gente constrói confiança.</h1>
    <p class="lead">Somos uma locadora de equipamentos para construção civil no Rio de
    Janeiro, feita por gente que conhece o dia a dia do canteiro. Atendemos construtoras,
    empreiteiros, pedreiros, pintores e quem está tocando a própria reforma.</p>
  </div>
</section>
<div class="hazard" role="presentation"></div>

<section class="section section--paper">
  <div class="wrap">
    <div class="split">
      <div class="prose">
        <p class="eyebrow">Nossa história</p>
        <h2>De um sonho pequeno a uma marca de referência</h2>
        <p>O Aluguel do Construtor nasceu de uma constatação simples: quem constrói perde
        tempo demais atrás de equipamento. A obra para porque faltou peça de andaime, porque
        a betoneira chegou sem correia, porque a entrega ficou para amanhã.</p>
        <p>A gente decidiu resolver essa parte. Estrutura enxuta, processo direto e um
        compromisso que não muda: o equipamento sai revisado e chega no prazo combinado.
        Construir é mais do que levantar parede, é erguer sonho com segurança, e cada item
        que entregamos passa por inspeção antes de subir no caminhão.</p>
        <p>Hoje somos cinco unidades no Rio de Janeiro, com frota própria, catálogo de 15
        categorias e atendimento que fala a língua da obra. Somos o braço de locação da
        <strong>%(legal_short)s</strong>.</p>
      </div>
      <figure class="figure">
        <img src="assets/img/loja-do-construtor-fachada.webp" width="1200" height="800" loading="lazy" decoding="async"
             alt="Fachada da Loja do Construtor, empresa por trás do Aluguel do Construtor">
      </figure>
    </div>
  </div>
</section>

<section class="section section--white">
  <div class="wrap">
    <div class="sec-head center">
      <p class="eyebrow">O que nos guia</p>
      <h2>Missão, visão e valores</h2>
    </div>
    <div class="grid grid--3">
      <article class="card"><div class="icon-badge">%(ico_target)s</div><h3>Missão</h3><p>Oferecer equipamento de qualidade e solução prática para a obra, garantindo segurança e produtividade, com atendimento transparente e humano.</p></article>
      <article class="card"><div class="icon-badge icon-badge--green">%(ico_eye)s</div><h3>Visão</h3><p>Ser reconhecida como referência em locação de equipamentos para construção no Rio de Janeiro, crescendo sem abrir mão do padrão de atendimento.</p></article>
      <article class="card"><div class="icon-badge icon-badge--dark">%(ico_shield)s</div><h3>Valores</h3><p>Cumprir o que foi combinado. Ser transparente no preço e no prazo. Ter agilidade sem abrir mão da qualidade. Respeitar o investimento e o tempo de quem contrata.</p></article>
    </div>
  </div>
</section>

<section class="section section--sand">
  <div class="wrap">
    <div class="split split--rev">
      <figure class="figure">
        <img src="assets/img/equipe-carregando.webp" width="900" height="1120" loading="lazy" decoding="async"
             alt="Profissional do Aluguel do Construtor preparando a carga de andaimes para entrega na obra">
      </figure>
      <div class="prose">
        <p class="eyebrow">Por que somos diferentes</p>
        <h2>Confiança se constrói com atitude, não com palavra</h2>
        <p>Não dá para prometer agilidade e depois deixar o cliente esperando resposta por
        dois dias. Não dá para falar em segurança e mandar peça com solda aberta. O que
        sustenta uma locadora é o operacional, e é nele que a gente investe.</p>
        <ul class="rulelist">
          <li><strong>Equipamento testado e mantido</strong>Inspeção, limpeza e manutenção preventiva antes de cada saída</li>
          <li><strong>Catálogo amplo em um fornecedor só</strong>Andaime, betoneira, martelete, compactador e mais 11 categorias</li>
          <li><strong>Processo sem burocracia</strong>Orçamento pelo WhatsApp, sem cadastro obrigatório para começar</li>
          <li><strong>Atendimento com vivência de canteiro</strong>Quem responde entende o que você está descrevendo</li>
          <li><strong>Logística própria</strong>Entrega e retirada com equipe nossa, sem depender de terceiro</li>
          <li><strong>Suporte durante todo o período</strong>Do orçamento à devolução, com o mesmo canal aberto</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section section--white">
  <div class="wrap">
    <div class="sec-head center">
      <p class="eyebrow">Quem alugou</p>
      <h2>O que dizem sobre a gente</h2>
      <p class="lead">Avaliações públicas deixadas por clientes no Google.</p>
    </div>
    %(quotes)s
  </div>
</section>

<section class="section section--paper">
  <div class="wrap">
    <div class="sec-head center">
      <p class="eyebrow">Onde estamos</p>
      <h2>Cinco unidades no Rio de Janeiro</h2>
    </div>
    %(units)s
  </div>
</section>
</main>
""" % {
        "crumbs": P.crumbs(trail, 0), "legal_short": P.LEGAL.title(),
        "ico_target": ICO("target"), "ico_eye": ICO("eye"), "ico_shield": ICO("shield"),
        "quotes": quotes_block(), "units": unit_cards(0),
    }

    html += P.cta(0)
    html += P.footer(0)
    write(path, html, "0.7", "monthly")


# ===========================================================================
# SEJA PARCEIRO
# ===========================================================================
def page_parceiro():
    path = "seja-parceiro.html"
    trail = [("index.html", "Início"), (None, "Seja parceiro")]
    ld = S.dumps([
        S.organization(), S.website(),
        S.webpage(path, "Seja parceiro", "Tenha uma unidade do Aluguel do Construtor na sua loja.",
                  breadcrumb_id=P.url(path) + "#breadcrumb"),
        S.breadcrumb(path, trail),
    ])
    wa = P.wa_link("Olá! Tenho uma loja e quero saber como ter uma unidade do Aluguel do Construtor.")

    html = P.head(
        title="Seja Parceiro | Tenha uma Unidade do Aluguel do Construtor",
        description=("Tem loja de material de construção? Agregue locação de equipamentos ao "
                     "seu mix com o Aluguel do Construtor e crie uma nova fonte de receita "
                     "no Rio de Janeiro."),
        path=path, depth=0, extra=ld)
    html += P.header(path, 0)

    html += """
<main id="conteudo">
<section class="pagehead">
  <div class="wrap pagehead__in">
    %(crumbs)s
    <h1>Tenha uma unidade do Aluguel do Construtor na sua loja</h1>
    <p class="lead">Se você já vende material de construção, o seu cliente já está com a obra
    na mão. A locação de equipamentos usa o mesmo público, o mesmo espaço e traz essa pessoa
    de volta várias vezes durante a mesma obra.</p>
    <div class="btn-row mt-6">
      <a class="btn btn--wa btn--lg" href="%(wa)s" target="_blank" rel="noopener">%(ico_wa)s Quero saber como funciona</a>
    </div>
  </div>
</section>
<div class="hazard" role="presentation"></div>

<section class="section section--paper">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Por que agregar locação</p>
      <h2>A receita que já está passando pela sua porta</h2>
      <p class="lead">Quem compra cimento vai precisar de betoneira. Quem compra tinta vai
      precisar de andaime. Hoje esse cliente sai da sua loja e resolve isso em outro lugar.</p>
    </div>
    <div class="grid grid--3">
      <article class="card"><div class="icon-badge">%(ico_money)s</div><h3>Receita recorrente</h3><p>Locação gera faturamento repetido dentro da mesma obra, e não uma venda única.</p></article>
      <article class="card"><div class="icon-badge">%(ico_users)s</div><h3>Mais visitas à loja</h3><p>Retirada e devolução trazem o cliente ao balcão de novo, o que abre nova oportunidade de venda.</p></article>
      <article class="card"><div class="icon-badge">%(ico_layers)s</div><h3>Mix mais completo</h3><p>Material e equipamento no mesmo lugar é conveniência real, e conveniência fideliza.</p></article>
      <article class="card"><div class="icon-badge">%(ico_handshake)s</div><h3>Marca já conhecida</h3><p>Você entra com uma operação estruturada, e não começando do zero.</p></article>
      <article class="card"><div class="icon-badge">%(ico_wrench)s</div><h3>Operação apoiada</h3><p>Você não fica sozinho na parte técnica nem na manutenção do equipamento.</p></article>
      <article class="card"><div class="icon-badge">%(ico_store)s</div><h3>Aproveita o seu espaço</h3><p>A operação se adapta ao espaço disponível na sua loja ou no seu depósito.</p></article>
    </div>
  </div>
</section>

<section class="section section--white">
  <div class="wrap">
    <div class="split split--rev">
      <figure class="figure">
        <img src="assets/img/profissional-uniforme.webp" width="748" height="760" loading="lazy" decoding="async"
             alt="Profissional uniformizado do Aluguel do Construtor">
      </figure>
      <div>
        <p class="eyebrow">Para quem é</p>
        <h2>Quem costuma se dar bem nessa parceria</h2>
        <ul class="checks mt-6">
          <li>Loja de material de construção com fluxo de obra na região</li>
          <li>Depósito com espaço para guarda e movimentação de equipamento</li>
          <li>Empresa que já atende construtora e empreiteira e quer ampliar o ticket</li>
          <li>Empreendedor que quer entrar no setor com marca e processo prontos</li>
        </ul>
        <p class="mt-6">A conversa começa simples: você conta como é a sua operação hoje e a
        gente explica o modelo, o que é necessário e o que fica sob nossa responsabilidade.
        Sem compromisso na primeira conversa.</p>
        <div class="btn-row mt-6">
          <a class="btn btn--primary btn--lg" href="%(wa)s" target="_blank" rel="noopener">%(ico_wa)s Conversar sobre a parceria</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--sand">
  <div class="wrap">
    <div class="sec-head center">
      <p class="eyebrow">Primeiros passos</p>
      <h2>Como começa</h2>
    </div>
    <div class="steps">
      <article class="step"><h3>Conversa inicial</h3><p>Você chama no WhatsApp e conta onde fica a loja e como é a sua operação hoje.</p></article>
      <article class="step"><h3>Análise da região</h3><p>A gente avalia a demanda da área e o encaixe com as unidades que já existem.</p></article>
      <article class="step"><h3>Modelo e condições</h3><p>Apresentamos o formato da parceria, o que cada lado assume e o investimento envolvido.</p></article>
      <article class="step"><h3>Montagem da unidade</h3><p>Definido o modelo, estruturamos a operação e a sua loja começa a alugar.</p></article>
    </div>
  </div>
</section>
</main>
""" % {
        "crumbs": P.crumbs(trail, 0), "wa": wa, "ico_wa": ICO("whatsapp"),
        "ico_money": ICO("money"), "ico_users": ICO("users"), "ico_layers": ICO("layers"),
        "ico_handshake": ICO("handshake"), "ico_wrench": ICO("wrench"), "ico_store": ICO("store"),
    }

    html += P.cta(0, title="Chegou a hora de crescer com a locação.",
                  text="Conte um pouco sobre a sua loja e a gente explica o modelo de parceria, "
                       "o que é necessário e o que fica sob nossa responsabilidade.",
                  primary=wa)
    html += P.footer(0)
    write(path, html, "0.6", "monthly")


# ===========================================================================
# FAQ
# ===========================================================================
def page_faq():
    path = "perguntas-frequentes.html"
    trail = [("index.html", "Início"), (None, "Dúvidas frequentes")]
    todas = FAQ_GERAL + [(q, a) for e in EQUIPAMENTOS for q, a in e["faq"][:1]]
    ld = S.dumps([
        S.organization(), S.website(),
        S.webpage(path, "Perguntas frequentes", "Dúvidas sobre locação de equipamentos para obra.",
                  breadcrumb_id=P.url(path) + "#breadcrumb", page_type="FAQPage"),
        S.breadcrumb(path, trail),
        S.faqpage(path, todas),
    ])

    html = P.head(
        title="Perguntas Frequentes | Locação de Equipamentos no Rio",
        description=("Prazo, entrega, formas de pagamento, revisão dos equipamentos e "
                     "bairros atendidos. As dúvidas mais comuns de quem aluga equipamento "
                     "para obra no Rio de Janeiro."),
        path=path, depth=0, extra=ld)
    html += P.header(path, 0)

    por_eq = "".join(
        '<details><summary>%s</summary><div class="faq__a"><p>%s</p>'
        '<p><a class="link-arrow" href="%s">Ver a página de %s %s</a></p></div></details>'
        % (e["faq"][0][0], e["faq"][0][1], "equipamentos/%s.html" % e["slug"],
           e["nome"].lower(), ICO("arrow"))
        for e in EQUIPAMENTOS)

    html += """
<main id="conteudo">
<section class="pagehead">
  <div class="wrap pagehead__in">
    %(crumbs)s
    <h1>Perguntas frequentes</h1>
    <p class="lead">Prazo, entrega, pagamento, revisão dos equipamentos e cobertura de
    atendimento. Se a sua dúvida não estiver aqui, chame no WhatsApp que a gente responde.</p>
  </div>
</section>
<div class="hazard" role="presentation"></div>

<section class="section section--paper">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Geral</p><h2>Sobre a locação</h2></div>
    <div class="faq" data-faq>%(geral)s</div>
  </div>
</section>

<section class="section section--white">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Por equipamento</p><h2>Dúvidas específicas de cada categoria</h2></div>
    <div class="faq" data-faq>%(por_eq)s</div>
  </div>
</section>
</main>
""" % {
        "crumbs": P.crumbs(trail, 0),
        "geral": "".join('<details><summary>%s</summary><div class="faq__a"><p>%s</p></div></details>'
                         % (q, a) for q, a in FAQ_GERAL),
        "por_eq": por_eq,
    }

    html += P.cta(0)
    html += P.footer(0)
    write(path, html, "0.6", "monthly")


# ===========================================================================
# CONTATO
# ===========================================================================
def page_contato():
    path = "contato.html"
    trail = [("index.html", "Início"), (None, "Contato")]
    ld = S.dumps([
        S.organization(), S.website(),
        S.webpage(path, "Contato", "Fale com o Aluguel do Construtor pelo WhatsApp ou pelo formulário.",
                  breadcrumb_id=P.url(path) + "#breadcrumb", page_type="ContactPage"),
        S.breadcrumb(path, trail),
    ] + [S.unidade(u, full=False) for u in UNIDADES])

    unidade_opts = "".join('<option value="%s">%s</option>' % (u["nome"], u["nome"]) for u in UNIDADES)

    html = P.head(
        title="Contato | Aluguel do Construtor - Rio de Janeiro",
        description=("Fale com o Aluguel do Construtor: WhatsApp %s, cinco unidades no Rio de "
                     "Janeiro e formulário que monta a mensagem para você." % P.PHONE_DISPLAY),
        path=path, depth=0, extra=ld)
    html += P.header(path, 0)

    html += """
<main id="conteudo">
<section class="pagehead">
  <div class="wrap pagehead__in">
    %(crumbs)s
    <div class="pagehead--split mt-6">
      <div>
        <p class="eyebrow">Fale com a gente</p>
        <h1>Pronto para falar com a gente?</h1>
        <p class="lead">Conte o que a sua obra precisa. Em poucos minutos retornamos com uma
        resposta clara: o que temos disponível, por quanto tempo e quando conseguimos entregar.</p>
        <div class="btn-row mt-6">
          <a class="btn btn--wa btn--lg" href="%(wa)s" target="_blank" rel="noopener">%(ico_wa)s WhatsApp %(phone)s</a>
          <a class="btn btn--ghost btn--lg" href="tel:%(tel)s">%(ico_ph)s Ligar agora</a>
        </div>
      </div>
      <img class="pagehead__img" src="assets/img/whatsapp-celular.webp" width="640" height="600"
           fetchpriority="high" decoding="async"
           alt="Celular com o ícone do WhatsApp, canal de atendimento do Aluguel do Construtor">
    </div>
  </div>
</section>
<div class="hazard" role="presentation"></div>

<section class="section section--paper">
  <div class="wrap eqlayout">
    <div>
      <div class="sec-head">
        <p class="eyebrow">Formulário</p>
        <h2>Monte o seu pedido</h2>
        <p class="lead">Preencha o essencial e a gente escreve a mensagem para você. Nada é
        armazenado: ao enviar, abrimos o WhatsApp com o texto pronto.</p>
      </div>

      <form class="form" data-wa-form="%(wanum)s">
        <div class="form__row">
          <div class="field">
            <label for="c-nome">Nome <span class="req">*</span></label>
            <input id="c-nome" name="nome" type="text" required autocomplete="name">
          </div>
          <div class="field">
            <label for="c-tel">Telefone / WhatsApp <span class="req">*</span></label>
            <input id="c-tel" name="telefone" type="tel" required autocomplete="tel" placeholder="(21) 90000-0000">
          </div>
        </div>

        <div class="form__row">
          <div class="field">
            <label for="c-email">E-mail</label>
            <input id="c-email" name="email" type="email" autocomplete="email">
          </div>
          <div class="field">
            <label for="c-unidade">Unidade mais próxima</label>
            <select id="c-unidade" name="unidade">
              <option value="">Não sei / a mais próxima da obra</option>
              %(unidade_opts)s
            </select>
          </div>
        </div>

        <div class="field">
          <label for="c-assunto">Assunto</label>
          <select id="c-assunto" name="assunto">
            <option>Orçamento de locação</option>
            <option>Dúvida sobre equipamento</option>
            <option>Prazo e entrega</option>
            <option>Parceria / unidade na minha loja</option>
            <option>Outro assunto</option>
          </select>
        </div>

        <div class="field">
          <label for="c-msg">Sua mensagem <span class="req">*</span></label>
          <textarea id="c-msg" name="mensagem" required placeholder="Ex.: preciso de andaime fachadeiro para uma fachada de 3 pavimentos no Recreio, por 30 dias."></textarea>
        </div>

        <button class="btn btn--wa btn--lg btn--block" type="submit">%(ico_wa)s Enviar pelo WhatsApp</button>
        <p class="form__note">Ao enviar, abrimos o WhatsApp com a mensagem pronta. Nenhum dado é armazenado neste site.</p>
        <p class="form__note" data-form-ok hidden>Pronto! Se o WhatsApp não abriu, chame direto em %(phone)s.</p>
      </form>
    </div>

    <aside class="aside">
      <div class="aside__card aside__card--dark">
        <h3>Prefere falar direto?</h3>
        <p>%(hours_long)s</p>
        <a class="btn btn--wa btn--block mt-4" href="%(wa)s" target="_blank" rel="noopener">%(ico_wa)s %(phone)s</a>
      </div>
      <div class="aside__card">
        <h3>WhatsApp de cada unidade</h3>
        <ul class="sidelist mt-4">%(unidades_links)s</ul>
      </div>
      <div class="aside__card">
        <h3>Redes sociais</h3>
        <ul class="sidelist mt-4">
          <li><a href="%(ig)s" target="_blank" rel="noopener">%(ico_ig)s Instagram</a></li>
          <li><a href="%(fb)s" target="_blank" rel="noopener">%(ico_fb)s Facebook</a></li>
        </ul>
      </div>
    </aside>
  </div>
</section>

<section class="section section--white">
  <div class="wrap">
    <div class="sec-head center">
      <p class="eyebrow">Endereços</p>
      <h2>Onde nos encontrar</h2>
      <p class="lead">%(hours_long)s</p>
    </div>
    %(units)s
  </div>
</section>
</main>
""" % {
        "crumbs": P.crumbs(trail, 0), "wa": P.WA_DEFAULT, "wanum": P.WA,
        "ico_wa": ICO("whatsapp"), "ico_ph": ICO("phone"),
        "ico_ig": ICO("instagram"), "ico_fb": ICO("facebook"),
        "phone": P.PHONE_DISPLAY, "tel": P.PHONE_TEL, "hours_long": P.HOURS_LONG,
        "unidade_opts": unidade_opts,
        "unidades_links": "".join(
            '<li><a href="https://wa.me/%s" target="_blank" rel="noopener">%s &middot; %s</a></li>'
            % (u["wa"], u["bairro"], u["wa_display"]) for u in UNIDADES),
        "units": unit_cards(0), "ig": P.INSTAGRAM, "fb": P.FACEBOOK,
    }

    html += P.cta(0)
    html += P.footer(0)
    write(path, html, "0.7", "monthly")


# ===========================================================================
# 404
# ===========================================================================
def page_404():
    path = "404.html"
    ld = S.dumps([S.organization(), S.website()])
    html = P.head(title="Página não encontrada | Aluguel do Construtor",
                  description=("A página que você procurou não existe ou mudou de endereço. "
                               "Veja os equipamentos disponíveis para locação no Rio de Janeiro."),
                  path=path, depth=0, robots="noindex, follow", extra=ld)
    html += P.header("", 0)
    html += """
<main id="conteudo">
  <section class="notfound">
    <div class="wrap wrap--narrow">
      <div class="notfound__code">404</div>
      <h1>Essa página saiu para entrega</h1>
      <p class="lead center">O endereço que você abriu não existe ou mudou. Mas o que você
      procura provavelmente está a um clique daqui.</p>
      <div class="btn-row center mt-8">
        <a class="btn btn--primary" href="equipamentos.html">Ver os equipamentos</a>
        <a class="btn btn--ghost" href="index.html">Ir para a página inicial</a>
        <a class="btn btn--ghost" href="unidades.html">Ver as unidades</a>
      </div>
    </div>
  </section>
</main>
"""
    html += P.footer(0)
    write(path, html, sitemap=False)


# ===========================================================================
# SITEMAP / ROBOTS / MANIFEST
# ===========================================================================
def write_sitemap():
    today = datetime.date.today().isoformat()
    rows = []
    for path, prio, freq in PAGES:
        rows.append("  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n"
                    "    <changefreq>%s</changefreq>\n    <priority>%s</priority>\n  </url>"
                    % (P.url(path), today, freq, prio))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n'
           % "\n".join(rows))
    write("sitemap.xml", xml, sitemap=False)


def write_robots():
    txt = """User-agent: *
Allow: /

# Sem area restrita: tudo pode ser indexado.
Disallow: /404.html

Sitemap: %s/sitemap.xml
""" % P.SITE
    write("robots.txt", txt, sitemap=False)


def write_manifest():
    import json
    m = {
        "name": P.BRAND,
        "short_name": "Aluguel Construtor",
        "description": "Locação de equipamentos para construção civil no Rio de Janeiro.",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#F6F5F3",
        "theme_color": "#17161A",
        "lang": "pt-BR",
        "icons": [
            {"src": "/assets/img/logo-mark.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
            {"src": "/assets/img/apple-touch-icon.png", "sizes": "180x180", "type": "image/png"},
            {"src": "/assets/img/favicon.svg", "sizes": "any", "type": "image/svg+xml"},
        ],
    }
    write("manifest.webmanifest", json.dumps(m, ensure_ascii=False, indent=2), sitemap=False)


# ===========================================================================
# main
# ===========================================================================
def main():
    print("Gerando o site a partir de %s\n" % P.SITE)
    page_index()
    page_equipamentos()
    for e in EQUIPAMENTOS:
        page_equipamento(e)
    page_unidades()
    for u in UNIDADES:
        page_unidade(u)
    page_quem_somos()
    page_parceiro()
    page_faq()
    page_contato()
    page_404()
    write_sitemap()
    write_robots()
    write_manifest()
    print("\n%d paginas no sitemap." % len(PAGES))


if __name__ == "__main__":
    main()
