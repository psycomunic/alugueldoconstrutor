# Aluguel do Construtor: contexto do projeto

> Arquivo de contexto para agentes de IA (Antigravity, Claude Code, Cursor, Copilot).
> Leia isto antes de qualquer alteração.

## O que é

Site do **Aluguel do Construtor**, locadora de equipamentos para construção civil no
**Rio de Janeiro**, com cinco unidades (Recreio dos Bandeirantes x2, Vargem Grande,
Pedra de Guaratiba e Botafogo). Substitui o site WordPress/Elementor antigo em
`alugueldoconstrutor.com`.

Razão social: LOJA DO CONSTRUTOR MATERIAIS E SERVIÇOS LTDA (CNPJ 42.626.394/0001-38).

**Objetivos de negócio, em ordem:**

1. **SEO** — ranquear para "aluguel de andaime rio de janeiro", "locação de betoneira RJ",
   "aluguel de martelete", e para a combinação equipamento + bairro
2. **Conversão** — orçamento pelo WhatsApp, que é o canal que o negócio já usa
3. **Autoridade** — conteúdo que ajuda a escolher o equipamento certo, não catálogo seco

## Stack

**HTML + CSS + JavaScript puro. Sem framework, sem bundler, sem dependência de runtime.**

Decisão deliberada, não limitação. Não introduza React, Tailwind, Vite ou Sass sem que
o usuário peça explicitamente.

- CSS: um arquivo, `assets/css/style.css`, com design tokens em `:root`
- JS: um arquivo, `assets/js/main.js`, vanilla, sem dependências, `defer`
- Fontes: Archivo + Inter **auto-hospedadas** em `assets/fonts/` (woff2 variável, subsets
  latin e latin-ext). `@font-face` no topo de `style.css`, `preload` dos dois subsets latin
  no `head` de `partials.py`. Nenhuma requisição sai para o Google
- Imagens: WebP com `width`/`height` declarados, `loading="lazy"` fora da dobra e
  `fetchpriority="high"` na imagem LCP

## ⚠️ As páginas são GERADAS. Não edite os `.html` às cegas

Os 28 arquivos `.html` são **saída** do gerador em `build/`.
Editar um `.html` direto funciona, mas a alteração é **perdida** na próxima vez que
alguém rodar `npm run build`.

| Tipo de alteração | Onde mexer |
|---|---|
| Telefone, endereço, horário, redes sociais, header, rodapé, CTA final, ícones | `build/partials.py` |
| Texto de equipamento, dados de unidade, depoimento, FAQ, diferenciais | `build/content.py` |
| Estrutura e seções de cada página | `build/build.py` |
| JSON-LD / structured data | `build/schema.py` |
| Cor, tipografia, espaçamento, componente, responsivo | `assets/css/style.css` |
| Comportamento (menu, acordeão, contador, formulário) | `assets/js/main.js` |

Depois de mexer em qualquer coisa dentro de `build/`, rode:

```bash
npm run build     # cd build && python3 build.py
npm run check     # valida antes de commitar
```

Se você **só** vai mexer em CSS/JS/imagens, não precisa rodar o build.

## Estrutura

```
.
├── index.html                     Home
├── equipamentos.html              Hub do catálogo + montador de orçamento
├── equipamentos/                  15 páginas, uma por categoria
│   ├── andaimes.html   betoneiras.html   marteletes.html
│   ├── compactadores.html   cortadores-de-piso.html   escoras.html
│   ├── escadas.html   furadeiras-e-parafusadeiras.html
│   ├── lixadeiras-e-esmerilhadeiras.html   serras-e-plainas.html
│   ├── lavadoras-de-alta-pressao.html   lavadoras-de-estofado.html
│   ├── motosserras-e-rocadeiras.html   sopradores-e-aspiradores.html
│   └── bombas-sapo.html
├── unidades.html                  Hub das unidades
├── unidades/                      5 páginas, uma por unidade (SEO local)
├── quem-somos.html
├── seja-parceiro.html             Página comercial: unidade na loja do parceiro
├── perguntas-frequentes.html
├── contato.html
├── 404.html
├── sitemap.xml  robots.txt  manifest.webmanifest  vercel.json
├── assets/
│   ├── css/style.css              Design system completo
│   ├── js/main.js                 Interações
│   ├── fonts/                     Archivo + Inter woff2 variável (latin, latin-ext)
│   └── img/                       Fotos, logos, og-cover, favicon
│       └── equipamentos/          Uma imagem 760px e uma 380px por categoria
├── build/
│   ├── partials.py                Dados do negócio, ícones SVG, head/header/footer/CTA
│   ├── content.py                 Equipamentos, unidades, depoimentos, FAQ
│   ├── schema.py                  JSON-LD
│   └── build.py                   Conteúdo das páginas + orquestração
└── tools/
    ├── serve.mjs                  Servidor local com URL limpa (só Node)
    ├── check.mjs                  Validador de SEO/HTML/links (só Node)
    └── images.py                  Pipeline que gerou as imagens a partir do site antigo
```

## Onde ficam os dados do negócio

Tudo no topo de `build/partials.py`:

```python
WA            = "5521972770014"          # número dos links wa.me
PHONE_DISPLAY = "(21) 97277-0014"
HOURS_SHORT   = "Seg. a sex., 7h às 17h · Sáb., 7h às 12h"
INSTAGRAM / FACEBOOK
AREAS         = [...]                    # bairros: alimenta o texto e o areaServed
```

Unidades (endereço, WhatsApp próprio, bairros atendidos, título e description de SEO):
`build/content.py` → lista `UNIDADES`.

Equipamentos (texto, aplicações, o que considerar, FAQ, sinônimos de busca):
`build/content.py` → lista `EQUIPAMENTOS`.

Mudou o telefone? Muda em `partials.py` e roda `npm run build`. Atualiza nas 28 páginas
de uma vez, incluindo os links `wa.me`, o schema e o rodapé.

### O domínio das URLs absolutas

`og:image`, `og:url`, `canonical` e o `sitemap.xml` precisam de URL absoluta que exista
de verdade. `SITE` resolve nesta ordem:

1. variável de ambiente `SITE_URL`, se definida
2. `VERCEL_PROJECT_PRODUCTION_URL`, que a Vercel injeta no build
3. `SITE_FINAL`, o `alugueldoconstrutor.com`

Enquanto o domínio ainda servir o site antigo, o passo 2 mantém o preview correto.

## Design tokens

Em `assets/css/style.css`, bloco `:root`. Paleta tirada do próprio logo:

- `--green: #06BE25` é o verde da marca. Uso restrito: logo, WhatsApp, checks de confirmação
- `--orange: #FA7E02` é a **cor de ação**: CTA, eyebrows, ícones de destaque
- `--orange-700: #A35200` é a versão de **texto** do laranja (a clara não passa em
  contraste AA sobre fundo claro; não troque de volta)
- `--ink-900: #17161A` para hero, faixas escuras e rodapé; `--ink-950` para o rodapé
- `--paper: #F6F5F3` é o fundo padrão; `--white` e `--sand: #FBF7F1` alternam entre seções
  (`.section--white`, `.section--sand`, `.section--paper`)
- Display: `Archivo` (700/800) · Corpo/UI: `Inter`

Não invente cores novas fora dos tokens. Se precisar de um tom novo, adicione ao `:root`.

### Formas

A linguagem visual vem do telhado do logo:

- `--notch` é o canto chanfrado no topo direito de `.hero__img` e `.figure img`
- `.hazard` é a faixa listrada laranja/preta usada como divisor entre seções escuras e claras
- Botões são retangulares com raio médio (`--r`), não pílula: leitura mais industrial
- `.eq` é o card de equipamento, `.unit` o card de unidade, `.step` o card numerado

### Contraste

O botão laranja usa **texto escuro** (`#2B1400`), não branco. Branco sobre `#FA7E02` dá
2.6:1 e reprova em WCAG AA. Não "conserte" isso trocando para branco.

### Copy

**Não use travessão (—) em texto visível.** Prefira vírgula, dois-pontos ou frase nova.
O `npm run check` avisa quando aparece um.

## Convenções

- Idioma: **português do Brasil**
- Copy: direta, sem jargão de marketing, sem superlativo vazio
- Classes CSS: BEM frouxo (`.card`, `.card__img`, `.card--dark`), utilitários curtos (`.mt-6`)
- Animação de entrada: `class="reveal"` e opcionalmente `data-d="1..4"` para delay.
  O CSS só esconde quando existe JS (`.js .reveal`), então sem JS nada some
- Contador animado: `<span data-count="15">15</span>` (o texto já vem preenchido)
- Todo link externo: `target="_blank" rel="noopener"`
- Um `<h1>` por página. Sempre `alt` em imagem. Sempre `width`/`height`

## SEO: o que já está implementado

Não remova nada disto sem entender o efeito.

- `title` único e ≤ 65 caracteres por página; `meta description` única e ≤ 165
- `canonical` absoluto em todas as páginas; `lang="pt-BR"`
- Open Graph + Twitter Card completos, com `og-cover.jpg` 1200x630
- Hierarquia semântica: um `h1`, `h2`/`h3` em ordem, `<main>`, `<nav>`, `<article>`, `<aside>`
- Migalhas visíveis + `BreadcrumbList` em JSON-LD
- JSON-LD em `@graph` com `@id` estáveis:
  `Organization` + `LocalBusiness` (matriz), um `LocalBusiness` por unidade com
  `openingHoursSpecification`, `areaServed` e `hasMap`, um `Service` + `Offer` por
  equipamento, `ItemList` nos hubs, `FAQPage` onde há FAQ, `WebSite`, `WebPage`
- **Sem `Review`/`AggregateRating` da própria empresa.** O Google trata isso como
  self-serving review e pode aplicar penalidade manual. Os depoimentos são texto normal
- `sitemap.xml` gerado com `lastmod`, `changefreq` e `priority`; `robots.txt` aponta para ele
- Interlinking: hub ↔ categoria, categoria ↔ unidade, categoria ↔ categoria relacionada
- Imagens com nome de arquivo descritivo, `alt` que descreve a cena, dimensões declaradas
- `vercel.json` com `cleanUrls`, cabeçalhos de segurança, cache imutável em `/assets`
  e **redirects 301 das URLs antigas do WordPress** (`/nossos-produtos`, `/produtos`, etc.)
- Conteúdo com profundidade: cada página de equipamento tem 800+ palavras úteis

## Regras que não podem quebrar

1. **Não fabricar informação.** Nada de preço, medida de estoque, número de clientes,
   ano de fundação ou prazo que o cliente não confirmou. Quando depende do estoque do dia,
   o texto manda falar no WhatsApp. Isso vale especialmente para `build/content.py`.
2. **Não inventar depoimento.** Os cinco em `DEPOIMENTOS` são transcrições de avaliações
   públicas do Google que já apareciam no site antigo. Só troque por avaliação real.
3. **Manter os CTAs de WhatsApp** em toda página: é o objetivo primário do site.
4. **Manter o JSON-LD válido.** Depois de mudança estrutural, valide em
   https://validator.schema.org/ e no Rich Results Test.
5. **Não adicionar backend.** O formulário monta a mensagem e abre o WhatsApp
   (`data-wa-form` em `main.js`). Não há servidor e nenhum dado é armazenado.
6. **Rodar `npm run check` antes de commitar.** Ele precisa terminar com 0 erros.

## Pendências conhecidas

- [ ] Confirmar CEP de cada unidade e adicionar ao `PostalAddress` no `schema.py`
- [ ] Adicionar `geo` (latitude/longitude) por unidade em `schema.py`. Hoje só existe
      `hasMap`, porque coordenada inventada é pior que coordenada ausente
- [ ] Confirmar e-mail de contato (`EMAIL` em `partials.py` está vazio de propósito)
- [ ] Verificar se o Facebook oficial é mesmo `/p/Aluguel-do-construtor-61566654734638/`
- [ ] Criar/reivindicar o **Perfil da Empresa no Google** de cada uma das cinco unidades e
      apontar o site para a página da unidade correspondente. Para SEO local isso pesa mais
      que qualquer coisa no código
- [ ] Fotos próprias de cada unidade (hoje só existem 5 fotos reais, reaproveitadas)
- [ ] Enviar o `sitemap.xml` no Google Search Console depois de publicar
- [x] ~~Auto-hospedar as fontes em `assets/fonts/`~~. Feito: woff2 variável, `@font-face`
      com `font-display: swap` em `style.css`, `preload` no `head`. Zero conexão a
      `fonts.gstatic.com`

## Comandos

```bash
npm run dev      # servidor local em http://localhost:8080 (só Node)
npm run build    # regenera as 28 páginas a partir de build/ (precisa de Python 3)
npm run check    # valida SEO, HTML, links e imagens (só Node)
npm run images   # regera assets/img a partir das pastas baixadas (só se precisar)
```

Não há `npm install`: nenhum comando tem dependência externa.
Só `npm run build` e `npm run images` precisam de Python 3 no PATH.

**No Windows, `python` e `python3` costumam cair no stub da Microsoft Store**, que não
executa nada: imprime "Python não foi encontrado" e sai com **exit 49**. Por isso os dois
scripts tentam `python3`, depois `python`, depois `py -3`: na Vercel (Linux) o primeiro
resolve, e no Windows o `py -3` alcança a instalação real. Se o `py` também não estiver no
PATH, adicione a pasta do launcher (`%LOCALAPPDATA%\Programs\Python\Launcher`) ou a da
instalação (`%LOCALAPPDATA%\Programs\Python\Python3xx`) ao PATH do usuário.
`npm run images` ainda precisa das pastas originais baixadas do site antigo e da Pillow
(`pip install pillow`); as imagens já geradas estão versionadas, então normalmente não é
necessário.
