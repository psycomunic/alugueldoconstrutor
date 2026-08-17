# Aluguel do Construtor: novo site

Versão nova do `alugueldoconstrutor.com`, feita para converter mais e ranquear melhor.
Este arquivo é para você, Angelo. O `AGENTS.md` ao lado é o que o Antigravity vai ler.

---

## Como abrir

**Só olhar o site:** abra a pasta e dê dois cliques em `index.html`. Funciona, mas os
links "limpos" (sem `.html`) só se comportam como em produção pelo servidor local.

**Do jeito certo, com servidor local:**

```bash
npm run dev
```

Abre em `http://localhost:8080`. Precisa só do Node instalado, não tem `npm install`.

**No Antigravity:** abra a pasta inteira. Ele lê o `AGENTS.md` sozinho e já entende que as
páginas são geradas por um script Python, então não vai editar HTML no lugar errado.

---

## O que mudou em relação ao site antigo

| | Antes | Agora |
|---|---|---|
| Páginas | 5 | 28 |
| Páginas por equipamento | nenhuma | 15 |
| Páginas por unidade | nenhuma | 5 |
| Texto indexável | pouco (muito título virou imagem) | ~15 mil palavras |
| Structured data | nenhum | Organization, 5 LocalBusiness, 15 Service, FAQ, Breadcrumb |
| Peso da home | WordPress + Elementor | 366 KB com tudo carregado |
| Formulário | envia e some | monta a mensagem e abre o WhatsApp |
| Tecnologia | WordPress + Elementor | HTML/CSS/JS, sem plugin e sem banco |

O ganho grande de SEO está nas 20 páginas novas. Hoje o site antigo tem uma página só
falando de todos os equipamentos, o que faz ele competir mal para "aluguel de andaime no
Recreio". Agora existe uma página dedicada por equipamento e uma por bairro, cada uma com
título, texto e schema próprios.

---

## Publicar na Vercel

1. Suba a pasta para um repositório no GitHub
2. Na Vercel: **Add New → Project → Import** o repositório
3. Framework Preset: **Other**. Não precisa configurar mais nada, o `vercel.json` já traz
   o build, os redirects 301 das URLs antigas e os cabeçalhos de segurança
4. Deploy
5. Depois, em **Settings → Domains**, adicione `alugueldoconstrutor.com`

O build roda `python3 build/build.py` e regenera as páginas com o domínio de produção
correto nas tags `canonical` e `og:image`.

> Se preferir não usar build na Vercel, dá para desligar: as páginas já estão prontas na
> pasta. Basta remover a linha `buildCommand` do `vercel.json`. O risco é o `canonical`
> ficar apontando para `alugueldoconstrutor.com` enquanto o domínio ainda serve o site velho.

---

## Depois de publicar: a parte que não é código

Estas quatro coisas valem mais para o ranqueamento do que qualquer ajuste no site.

1. **Google Search Console.** Adicione a propriedade e envie
   `https://alugueldoconstrutor.com/sitemap.xml`.
2. **Perfil da Empresa no Google, um por unidade.** São cinco endereços. Cada perfil deve
   apontar para a página da unidade correspondente (`/unidades/botafogo`, e assim por
   diante), com o mesmo nome, o mesmo endereço e o mesmo telefone que estão no site.
   Consistência de nome, endereço e telefone é o que o Google usa para confiar no negócio.
3. **Peça avaliação.** Os cinco depoimentos do site são reais e vieram do Google, mas dois
   são antigos. Avaliação nova e frequente move o mapa local.
4. **Redirects.** Já estão no `vercel.json`, mas confira depois de publicar se
   `alugueldoconstrutor.com/nossos-produtos` cai em `/equipamentos`.

---

## Mudar alguma coisa

**Telefone, horário, endereço, redes sociais:** `build/partials.py`, no topo do arquivo.

**Texto de um equipamento, dados de uma unidade, FAQ, depoimento:** `build/content.py`.

**Cor, fonte, espaçamento:** `assets/css/style.css`, bloco `:root` no começo.

Depois de mexer em qualquer arquivo dentro de `build/`:

```bash
npm run build     # regenera as 28 páginas
npm run check     # confere se não quebrou nada
```

O `npm run check` valida título, description, canonical, H1 único, `alt` de imagem,
links internos quebrados e JSON-LD. Ele tem que terminar com **0 erros**.

---

## O que ficou pendente

Nada disso trava a publicação, mas vale resolver:

- **CEP e coordenadas de cada unidade.** O schema tem rua, bairro e cidade, mas não CEP
  nem latitude/longitude. Preferi deixar em branco a inventar.
- **E-mail de contato.** O site antigo não mostrava nenhum, então o site novo só usa
  WhatsApp e telefone.
- **Fotos.** Só existiam cinco fotos reais no material baixado, e elas se repetem entre as
  páginas. Foto de cada unidade, da equipe e de obra em andamento melhoraria bastante,
  inclusive para o Perfil da Empresa no Google.
- **Facebook.** Usei o link que estava no site antigo; vale confirmar se é o perfil ativo.

A lista completa, com o motivo de cada uma, está no fim do `AGENTS.md`.

---

## Uma decisão que pode parecer erro e não é

O botão laranja usa **texto escuro**, não branco. Branco sobre laranja `#FA7E02` dá 2.6:1
de contraste e reprova em acessibilidade (o mínimo é 4.5:1). O texto escuro dá 6.7:1.
Se alguém "consertar" isso trocando para branco, o site volta a reprovar.

Pelo mesmo motivo o laranja dos textos e links (`--orange-700`) é mais escuro que o laranja
dos fundos e ícones (`--orange`). São dois tokens de propósito.
