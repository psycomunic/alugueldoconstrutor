# -*- coding: utf-8 -*-
"""Conteudo do site: equipamentos, unidades, depoimentos, FAQ.

Regra de ouro: nada aqui pode ser inventado.
Nao escreva preco, medida de estoque, quantidade de clientes ou prazo
que nao tenha sido confirmado pelo cliente. Quando a informacao depende
do estoque do dia, o texto manda a pessoa falar no WhatsApp.
"""

# ===========================================================================
# UNIDADES
# ===========================================================================
# Fonte: pagina /unidades/ do site atual. Confirmar CEP e coordenadas.
UNIDADES = [
    {
        "slug": "recreio-dos-bandeirantes",
        "seo_title": "Aluguel de Equipamentos no Recreio dos Bandeirantes",
        "seo_desc": "Locação de andaimes, betoneiras e marteletes no Recreio dos Bandeirantes, RJ. Entrega na obra e orçamento no WhatsApp (21) 99529-1741.",
        "nome": "Recreio dos Bandeirantes",
        "bairro": "Recreio dos Bandeirantes",
        "titulo_curto": "Recreio (Luiza Nogueira)",
        "rua": "Rua Professora Luiza Nogueira Gonçalves, 350",
        "wa": "5521995291741",
        "wa_display": "(21) 99529-1741",
        "matriz": True,
        "atende": ["Recreio dos Bandeirantes", "Barra da Tijuca", "Barra Olímpica",
                   "Vargem Pequena", "Itanhangá", "Joá", "Grumari", "São Conrado"],
        "sobre": ("É a unidade de referência da rede no Recreio dos Bandeirantes e a base "
                  "de boa parte das entregas na Barra da Tijuca. Fica em via de fácil acesso "
                  "para caminhão, o que encurta o tempo entre o pedido e a chegada do "
                  "equipamento na obra."),
    },
    {
        "slug": "recreio-leon-eliachar",
        "seo_title": "Aluguel de Equipamentos no Recreio | Léon Eliachar",
        "seo_desc": "Locação de equipamentos para obra na Rua Léon Eliachar, Recreio dos Bandeirantes, RJ. Entrega rápida e orçamento no WhatsApp (21) 97277-0014.",
        "nome": "Recreio dos Bandeirantes (Léon Eliachar)",
        "bairro": "Recreio (Léon Eliachar)",
        "titulo_curto": "Recreio (Léon Eliachar)",
        "rua": "Rua Léon Eliachar, 14",
        "wa": "5521972770014",
        "wa_display": "(21) 97277-0014",
        "matriz": False,
        "atende": ["Recreio dos Bandeirantes", "Barra da Tijuca", "Barra Olímpica",
                   "Vargem Pequena", "Itanhangá", "Joá", "Grumari", "São Conrado"],
        "sobre": ("Segunda unidade no Recreio, montada para dar vazão à demanda do bairro "
                  "sem fila de espera. Atende quem está tocando reforma de apartamento, "
                  "condomínio e obra de pequeno e médio porte na região."),
    },
    {
        "slug": "vargem-grande",
        "seo_title": "Aluguel de Equipamentos em Vargem Grande, Rio de Janeiro",
        "seo_desc": "Locação de andaimes, betoneiras e marteletes em Vargem Grande, RJ. Entrega na obra e orçamento no WhatsApp (21) 99696-0114.",
        "nome": "Vargem Grande",
        "bairro": "Vargem Grande",
        "titulo_curto": "Vargem Grande",
        "rua": "Estrada dos Bandeirantes, 23483, lojas A e B",
        "wa": "5521996960114",
        "wa_display": "(21) 99696-0114",
        "matriz": False,
        "atende": ["Vargem Grande", "Vargem Pequena", "Camorim", "Curicica",
                   "Jacarepaguá", "Taquara", "Anil", "Gardênia Azul",
                   "Recreio dos Bandeirantes"],
        "sobre": ("Fica na Estrada dos Bandeirantes, corredor que liga Vargem Grande a "
                  "Jacarepaguá e à Barra. É a unidade mais prática para obra em condomínio "
                  "e casa na região das vargens."),
    },
    {
        "slug": "pedra-de-guaratiba",
        "seo_title": "Aluguel de Equipamentos em Pedra de Guaratiba, RJ",
        "seo_desc": "Locação de equipamentos para construção em Pedra de Guaratiba e Zona Oeste, RJ. Entrega na obra e orçamento no WhatsApp (21) 99720-0114.",
        "nome": "Pedra de Guaratiba",
        "bairro": "Pedra de Guaratiba",
        "titulo_curto": "Pedra de Guaratiba",
        "rua": "Estrada da Matriz, 2801",
        "wa": "5521997200114",
        "wa_display": "(21) 99720-0114",
        "matriz": False,
        "atende": ["Pedra de Guaratiba", "Guaratiba", "Barra de Guaratiba",
                   "Campo Grande", "Santa Cruz", "Sepetiba", "Cosmos",
                   "Senador Vasconcelos", "Santíssimo"],
        "sobre": ("Atende toda a região de Guaratiba e a Zona Oeste mais distante, onde "
                  "encontrar locadora perto da obra costuma ser o maior problema. Trabalha "
                  "com o mesmo catálogo das demais unidades."),
    },
    {
        "slug": "botafogo",
        "seo_title": "Aluguel de Equipamentos em Botafogo, Zona Sul do Rio",
        "seo_desc": "Locação de andaimes, betoneiras e ferramentas em Botafogo e Zona Sul do Rio. Entrega na obra e orçamento no WhatsApp (21) 97156-9700.",
        "nome": "Botafogo",
        "bairro": "Botafogo",
        "titulo_curto": "Botafogo",
        "rua": "Rua Mena Barreto, 129",
        "wa": "5521971569700",
        "wa_display": "(21) 97156-9700",
        "matriz": False,
        "atende": ["Botafogo", "Humaitá", "Flamengo", "Laranjeiras", "Catete",
                   "Copacabana", "Urca", "Gávea", "Jardim Botânico", "Leblon",
                   "Ipanema", "São Conrado"],
        "sobre": ("Nossa unidade na Zona Sul. Atende reforma de apartamento, retrofit de "
                  "prédio antigo e obra comercial em Botafogo, Humaitá, Flamengo, "
                  "Laranjeiras e Copacabana, onde carga e descarga precisam de horário "
                  "combinado e equipamento que caiba no elevador."),
    },
]

for _u in UNIDADES:
    _u["endereco"] = "%s - %s, Rio de Janeiro - RJ" % (_u["rua"], _u["bairro"])

# ===========================================================================
# EQUIPAMENTOS
# ===========================================================================
# Campos:
#   slug, nome, singular, resumo (card), h1, title, desc (meta), destaque
#   intro   -> lista de paragrafos da abertura
#   usos    -> "onde se usa" (lista)
#   escolher-> "como escolher / o que perguntar" (lista de (titulo, texto))
#   inclui  -> o que acompanha / como funciona a locacao
#   norma   -> texto de seguranca (ou None)
#   faq     -> lista de (pergunta, resposta)
#   sinonimos -> termos que as pessoas usam para buscar (entram no texto e no schema)

EQUIPAMENTOS = [
    {
        "slug": "andaimes",
        "nome": "Andaimes",
        "singular": "andaime",
        "destaque": 1,
        "resumo": "Fachadeiro e tubular para trabalho em altura, com montagem simples e pronta entrega.",
        "h1": "Aluguel de andaimes no Rio de Janeiro",
        "title": "Aluguel de Andaimes no Rio de Janeiro | Fachadeiro e Tubular",
        "desc": "Locação de andaimes fachadeiros e tubulares no Rio de Janeiro. Peças revisadas, entrega na obra e orçamento no WhatsApp em minutos. 5 unidades.",
        "sinonimos": ["andaime fachadeiro", "andaime tubular", "andaime suspenso",
                      "locação de andaime", "andaime metálico", "torre de andaime"],
        # Banner de largura inteira no hero, em vez da foto quadrada do produto.
        # Opcional: so os equipamentos que tiverem esta chave usam banner.
        # Espera dois arquivos em assets/img: <arquivo>.webp (1957px) e
        # <arquivo>-980.webp, que e a versao para tela estreita.
        # "espelhar" vira a foto na horizontal: nesta o sol fica na esquerda,
        # que e onde entra o texto, entao espelhada o brilho sobra para a
        # direita e o texto cai sobre a parte escura da estrutura.
        "banner": {
            "arquivo": "banner-andaimes-obra",
            "espelhar": True,
            "alt": ("Operário sobre plataforma de andaime tubular montado em obra, "
                    "ao fim da tarde"),
        },
        "intro": [
            "Andaime é o equipamento que decide se a obra vai render ou vai parar. "
            "Quando a estrutura chega completa, com sapata, travessa, diagonal e piso na "
            "quantidade certa, a equipe sobe no mesmo dia. Quando falta peça, todo mundo espera.",
            "Trabalhamos com andaime fachadeiro, para pintura, revestimento e reforma de "
            "fachada, e com andaime tubular, para serviço interno, forro, gesso e "
            "manutenção. Cada peça é conferida antes de sair: solda, encaixe, pino e "
            "estado do piso.",
        ],
        "usos": [
            "Pintura e impermeabilização de fachada",
            "Reboco, revestimento e assentamento de cerâmica em altura",
            "Instalação e manutenção de forro, gesso e elétrica",
            "Reforma de telhado, calha e platibanda",
            "Limpeza de vidro e manutenção predial",
            "Montagem de estrutura, cenografia e evento",
        ],
        "escolher": [
            ("Altura real do serviço",
             "Meça do piso de apoio até o ponto mais alto que a equipe precisa alcançar. "
             "É essa medida, e não a altura do prédio, que define quantos módulos você aluga."),
            ("Largura da frente de trabalho",
             "Fachada longa pede painéis em sequência. Serviço pontual costuma resolver "
             "com uma torre. Falar o comprimento aproximado acelera muito o orçamento."),
            ("Onde a base vai apoiar",
             "Piso irregular, terra batida ou calçada em desnível mudam a quantidade de "
             "sapatas e a necessidade de prancha de apoio."),
            ("Quem vai montar",
             "Montagem de andaime é serviço técnico. Se a sua equipe não tem prática, "
             "avise: orientamos a sequência correta de montagem e o que não pode ser feito."),
        ],
        "inclui": [
            "Peças conferidas uma a uma antes da saída",
            "Entrega e retirada com frota própria",
            "Orientação de montagem por telefone ou WhatsApp",
            "Reposição rápida em caso de peça danificada durante o uso",
        ],
        "norma": ("Trabalho em altura no Brasil segue a NR-18 e a NR-35. Andaime precisa de "
                  "base nivelada, travamento, guarda-corpo e rodapé, e a equipe precisa de "
                  "cinto e treinamento. Alugamos equipamento em condição de uso e orientamos "
                  "a montagem, mas a responsabilidade técnica pela obra e pela segurança da "
                  "equipe continua sendo do responsável pelo canteiro."),
        "faq": [
            ("Qual a diferença entre andaime fachadeiro e tubular?",
             "O fachadeiro é modular, monta em painéis e acompanha a fachada em altura e "
             "extensão, sendo o padrão para pintura e revestimento externo. O tubular monta "
             "com tubo e braçadeira, é mais flexível para espaços irregulares e resolve bem "
             "serviço interno, forro e manutenção pontual."),
            ("Vocês montam o andaime na obra?",
             "A locação é do equipamento. A montagem fica com a equipe da obra, e nós "
             "orientamos a sequência correta e os pontos de travamento. Se você precisa de "
             "montagem, fale com a gente pelo WhatsApp que indicamos o caminho."),
            ("Quanto tempo posso ficar com o andaime?",
             "O período é flexível: diária, semana, quinzena ou mês. Obra de fachada "
             "normalmente fecha por mês. Se a obra atrasar, é só avisar antes do fim do "
             "período para renovar."),
            ("Vocês entregam no Recreio, na Barra e na Zona Sul?",
             "Sim. Temos unidades no Recreio dos Bandeirantes, Vargem Grande, Pedra de "
             "Guaratiba e Botafogo, e entregamos com frota própria nas regiões atendidas "
             "por cada uma."),
        ],
    },
    {
        "slug": "betoneiras",
        "nome": "Betoneiras",
        "singular": "betoneira",
        "destaque": 2,
        "resumo": "Mistura homogênea de concreto e argamassa direto no canteiro, sem depender de usina.",
        "h1": "Aluguel de betoneiras no Rio de Janeiro",
        "title": "Aluguel de Betoneira no Rio de Janeiro | Locação por Dia ou Mês",
        "desc": "Locação de betoneiras para concreto e argamassa no Rio de Janeiro. Equipamento revisado, entrega na obra e orçamento rápido pelo WhatsApp.",
        "sinonimos": ["locação de betoneira", "betoneira elétrica", "betoneira de obra",
                      "misturador de concreto", "aluguel de betoneira para argamassa"],
        "intro": [
            "Betoneira resolve o que a mão não dá conta: mistura uniforme, na hora certa e "
            "no volume que a obra consome. Traço batido a pá varia de padeiro para padeiro. "
            "Na betoneira, a mistura sai igual do começo ao fim do dia.",
            "Para obra pequena e média, alugar sai muito mais barato que comprar concreto "
            "usinado, principalmente quando o consumo é fracionado ao longo da semana. "
            "Todas as nossas betoneiras passam por revisão de motor, correia, coroa e "
            "estrutura antes de sair.",
        ],
        "usos": [
            "Concreto para contrapiso, laje pequena, viga e baldrame",
            "Argamassa de assentamento e de revestimento",
            "Chapisco, emboço e reboco",
            "Massa para calçada, muro e piso externo",
            "Rejunte e grout em volume",
        ],
        "escolher": [
            ("Volume que a obra consome por vez",
             "Não é o volume total da obra, é quanto a equipe aplica antes da massa "
             "começar a puxar. Betoneira grande com equipe pequena vira desperdício."),
            ("Energia disponível no canteiro",
             "Confirme a tensão do ponto onde o equipamento vai ligar e se existe "
             "disjuntor dedicado. É o detalhe que mais causa dor de cabeça no primeiro dia."),
            ("Espaço e piso do canteiro",
             "A betoneira precisa de piso firme e nivelado, e de espaço livre em volta "
             "para carga e descarga com carrinho."),
            ("Quem vai operar",
             "Combine quem carrega, quem controla o traço e quem limpa. Betoneira lavada "
             "ao fim do dia dura mais e não devolve resíduo na próxima massa."),
        ],
        "inclui": [
            "Motor, correia e estrutura revisados",
            "Equipamento entregue limpo e pronto para ligar",
            "Entrega e retirada com frota própria",
            "Suporte por WhatsApp durante todo o período",
        ],
        "norma": ("Equipamento com parte móvel segue a NR-12. Mantenha as proteções no "
                  "lugar, não coloque a mão ou a ferramenta dentro do tambor em movimento e "
                  "desligue da tomada antes de qualquer limpeza."),
        "faq": [
            ("Betoneira elétrica ou a gasolina?",
             "Depende do canteiro. Onde existe energia estável, a elétrica é mais silenciosa, "
             "mais limpa e mais barata de operar. Em obra sem ligação definitiva, a opção a "
             "combustão resolve. Fale com a gente que indicamos pelo cenário da sua obra."),
            ("Preciso lavar a betoneira antes de devolver?",
             "Sim, e é do seu interesse. Concreto curado dentro do tambor é difícil de "
             "remover e pode gerar cobrança de limpeza. Lavar ao fim de cada dia de uso "
             "resolve em minutos."),
            ("Dá para alugar só por um dia?",
             "Dá. Trabalhamos com diária, semana, quinzena e mês. Para concretagem "
             "concentrada, a diária costuma ser o formato mais econômico."),
            ("Vocês entregam a betoneira na obra?",
             "Entregamos e retiramos com frota própria nas regiões atendidas pelas nossas "
             "unidades. É só informar o endereço da obra no orçamento."),
        ],
    },
    {
        "slug": "marteletes",
        "nome": "Marteletes",
        "singular": "martelete",
        "destaque": 3,
        "resumo": "Perfuração e demolição em concreto com potência de verdade e menos vibração na mão.",
        "h1": "Aluguel de marteletes e rompedores no Rio de Janeiro",
        "title": "Aluguel de Martelete no Rio de Janeiro | Perfuração e Demolição",
        "desc": "Locação de marteletes e rompedores para concreto no Rio de Janeiro. Equipamento revisado, brocas e ponteiros, entrega na obra. Orçamento no WhatsApp.",
        "sinonimos": ["locação de martelete", "martelete rompedor", "martelete perfurador",
                      "rompedor de concreto", "martelo demolidor", "furadeira de impacto pesada"],
        "intro": [
            "Furadeira comum não vence concreto estrutural. Martelete vence, porque o "
            "impacto vem de um mecanismo pneumático interno e não do esforço de quem "
            "segura. O serviço que levaria a tarde inteira sai em minutos, e a mão do "
            "profissional agradece.",
            "Temos martelete perfurador, para furo em concreto e alvenaria, e rompedor, "
            "para demolição e remoção de piso e revestimento. Cada equipamento sai com "
            "revisão de escova, mandril e sistema de impacto.",
        ],
        "usos": [
            "Furo para chumbador, barra roscada e fixação estrutural",
            "Passagem de tubulação hidráulica e eletroduto em laje e parede",
            "Remoção de piso, azulejo e contrapiso",
            "Demolição de alvenaria e trecho de parede",
            "Abertura de rasgo para instalação embutida",
            "Corte de concreto leve e regularização",
        ],
        "escolher": [
            ("O que você vai fazer: furar ou quebrar",
             "Furo pede perfurador com encaixe SDS. Demolição pede rompedor, mais pesado e "
             "com curso de impacto maior. Muita gente aluga o modelo errado e culpa o "
             "equipamento."),
            ("Diâmetro e profundidade do furo",
             "Furo de 8 mm para bucha e furo de 25 mm para chumbador não pedem a mesma "
             "máquina. Informe a medida e o material, que separamos a broca certa."),
            ("Material a ser rompido",
             "Concreto armado, alvenaria e cerâmica pedem ponteiros diferentes. Ponteiro "
             "errado desgasta rápido e rende pouco."),
            ("Tempo de uso contínuo",
             "Demolição de longa duração exige pausa para o equipamento e para o operador. "
             "Vale conversar sobre o ritmo previsto antes de fechar o período."),
        ],
        "inclui": [
            "Brocas e ponteiros conforme o serviço combinado",
            "Equipamento com revisão do sistema de impacto",
            "Maleta ou embalagem de transporte quando aplicável",
            "Suporte por WhatsApp para dúvida de uso",
        ],
        "norma": ("Ferramenta de impacto segue a NR-12 e exige EPI: óculos, protetor "
                  "auricular, luva antivibração e máscara contra poeira. Antes de furar "
                  "laje ou parede, confirme onde passam elétrica e hidráulica."),
        "faq": [
            ("Qual a diferença entre martelete e rompedor?",
             "O martelete perfurador gira e bate, e serve para abrir furo. O rompedor só "
             "bate, com energia de impacto maior, e serve para demolir e remover. Para furo "
             "de fixação, perfurador. Para tirar piso e derrubar parede, rompedor."),
            ("As brocas e os ponteiros vão junto?",
             "Vão, conforme o serviço combinado. Diga o que precisa furar ou romper e o "
             "diâmetro, que a gente separa junto com o equipamento."),
            ("Martelete fura qualquer parede?",
             "Fura concreto, bloco, tijolo e pedra. Para material cerâmico frágil e "
             "porcelanato o impacto pode trincar a peça, então nesses casos o indicado é "
             "furadeira com broca específica e sem percussão."),
            ("Posso alugar por um dia só?",
             "Pode. Diária, semana, quinzena ou mês. Para serviço pontual de fixação, a "
             "diária costuma resolver."),
        ],
    },
    {
        "slug": "compactadores",
        "nome": "Compactadores",
        "singular": "compactador",
        "resumo": "Sapo e placa vibratória para compactar solo, base e reaterro antes de concretar.",
        "h1": "Aluguel de compactadores de solo no Rio de Janeiro",
        "title": "Aluguel de Compactador de Solo no Rio de Janeiro | Sapo e Placa",
        "desc": "Locação de compactador tipo sapo e placa vibratória no Rio de Janeiro. Compactação de base, reaterro e calçada. Entrega na obra e orçamento no WhatsApp.",
        "sinonimos": ["compactador de solo", "sapo compactador", "placa vibratória",
                      "compactador de percussão", "locação de compactador"],
        "intro": [
            "Piso que trinca, calçada que afunda e contrapiso que descola quase sempre "
            "contam a mesma história: a base não foi compactada direito. Compactar é o "
            "passo mais barato da obra e o mais caro de refazer.",
            "Trabalhamos com compactador de percussão, o sapo, indicado para vala, "
            "reaterro e área estreita, e com placa vibratória, indicada para superfície "
            "aberta, base de piso e assentamento de bloco intertravado.",
        ],
        "usos": [
            "Reaterro de vala de tubulação e fundação",
            "Base de contrapiso, calçada e área externa",
            "Assentamento de bloco intertravado e paver",
            "Preparo de terreno para laje e piso industrial",
            "Compactação de aterro em pequena escala",
        ],
        "escolher": [
            ("Vala estreita ou área aberta",
             "Vala e canto pedem sapo, que concentra energia em uma área pequena. "
             "Superfície aberta rende muito mais com placa vibratória."),
            ("Tipo de solo",
             "Solo argiloso responde melhor à percussão. Areia e brita respondem melhor à "
             "vibração. Diga o material que a gente indica o equipamento."),
            ("Espessura de cada camada",
             "Compactar 40 cm de uma vez não funciona. Trabalhe em camadas e o resultado "
             "aparece no ensaio e no piso."),
            ("Acesso ao ponto de trabalho",
             "Equipamento de compactação é pesado. Vale confirmar se existe rampa, "
             "elevador de carga ou passagem livre até o local."),
        ],
        "inclui": [
            "Equipamento revisado e abastecido para o primeiro uso",
            "Orientação de operação e de camadas",
            "Entrega e retirada com frota própria",
        ],
        "norma": ("Compactador gera vibração e ruído altos. Use protetor auricular, "
                  "bota com biqueira e luva antivibração, e faça pausas regulares, "
                  "conforme a NR-12 e a NR-15."),
        "faq": [
            ("Sapo ou placa vibratória, qual eu preciso?",
             "Sapo para vala, canto e reaterro em faixa estreita. Placa vibratória para "
             "área aberta, base de piso e intertravado. Se a obra tem os dois cenários, "
             "muita gente aluga os dois pelo mesmo período."),
            ("O equipamento vem abastecido?",
             "Entregamos pronto para o primeiro uso e orientamos sobre combustível e óleo "
             "para o restante do período."),
            ("Dá para compactar terra molhada?",
             "Umidade demais atrapalha tanto quanto solo seco. O ideal é o solo na umidade "
             "próxima da ótima, quando ele fecha na mão sem escorrer água."),
        ],
    },
    {
        "slug": "cortadores-de-piso",
        "nome": "Cortadores de piso",
        "singular": "cortador de piso",
        "resumo": "Corte reto e limpo em cerâmica, porcelanato e concreto, sem quebrar a peça.",
        "h1": "Aluguel de cortadores de piso no Rio de Janeiro",
        "title": "Aluguel de Cortador de Piso no Rio de Janeiro | Locação",
        "desc": "Locação de cortador de piso e serra clipper no Rio de Janeiro. Corte de cerâmica, porcelanato e concreto. Entrega na obra e orçamento pelo WhatsApp.",
        "sinonimos": ["cortador de piso manual", "serra clipper", "cortador de cerâmica",
                      "máquina de cortar porcelanato", "serra de bancada para piso"],
        "intro": [
            "Porcelanato caro quebrando no corte é prejuízo silencioso. Cortador adequado "
            "faz o serviço com linha reta, sem lasca na borda e sem perder peça, o que na "
            "prática paga a locação já no primeiro dia.",
            "Temos cortador manual, para corte reto em cerâmica e porcelanato, e serra de "
            "bancada com disco diamantado e refrigeração a água, para corte molhado em "
            "peça grande, concreto e material mais duro.",
        ],
        "usos": [
            "Corte de piso e revestimento cerâmico",
            "Corte de porcelanato de formato grande",
            "Recorte para ralo, tomada e passagem de tubulação",
            "Corte de bloco, pastilha e pedra",
            "Ajuste de peça em rodapé e soleira",
        ],
        "escolher": [
            ("Tipo e dureza da peça",
             "Cerâmica comum aceita corte manual. Porcelanato técnico e pedra pedem disco "
             "diamantado e corte molhado."),
            ("Tamanho da peça",
             "Peça de formato grande exige mesa com curso compatível. Medir a maior peça "
             "do projeto evita surpresa no dia da instalação."),
            ("Tipo de corte",
             "Corte reto é uma coisa, recorte em L e furo para ralo é outra. Diga o que "
             "precisa fazer que indicamos a máquina certa."),
            ("Água disponível no local",
             "Serra de corte molhado precisa de ponto de água ou reservatório. É um detalhe "
             "que trava o serviço quando não foi previsto."),
        ],
        "inclui": [
            "Disco adequado ao material combinado",
            "Equipamento com bancada e guias revisados",
            "Entrega e retirada com frota própria",
        ],
        "norma": ("Use óculos de proteção, protetor auricular e máscara. Corte a seco em "
                  "material cerâmico gera poeira de sílica, que exige proteção respiratória "
                  "adequada. Sempre que possível, prefira corte molhado."),
        "faq": [
            ("Cortador manual serve para porcelanato?",
             "Serve para porcelanato esmaltado de espessura padrão e corte reto. "
             "Porcelanato técnico, peça muito espessa e recorte em L pedem serra com "
             "disco diamantado."),
            ("O disco vai junto?",
             "Vai, conforme o material que você informar no orçamento. Disco errado quebra "
             "peça e desgasta rápido, então vale detalhar o revestimento."),
            ("Preciso de energia trifásica?",
             "Os modelos de bancada que trabalhamos são monofásicos e ligam em tomada "
             "comum. Confirme a tensão do canteiro no momento do pedido."),
        ],
    },
    {
        "slug": "escoras",
        "nome": "Escoras",
        "singular": "escora",
        "resumo": "Escoramento metálico regulável para laje, viga e forma, com altura ajustável.",
        "h1": "Aluguel de escoras metálicas no Rio de Janeiro",
        "title": "Aluguel de Escora Metálica no Rio de Janeiro | Laje",
        "desc": "Locação de escoras metálicas reguláveis para laje e viga no Rio de Janeiro. Peças revisadas, entrega na obra e orçamento rápido pelo WhatsApp.",
        "sinonimos": ["escora metálica", "escoramento de laje", "escora regulável",
                      "pontalete metálico", "locação de escora"],
        "intro": [
            "Escora é o que segura a laje enquanto o concreto ganha resistência. "
            "Escoramento mal dimensionado é a causa clássica de flecha na laje, trinca no "
            "revestimento e, no pior cenário, de acidente grave.",
            "Trabalhamos com escora metálica regulável, que ajusta a altura no pino e "
            "substitui com folga o pontalete de madeira: não empena, não racha e mantém a "
            "capacidade de carga do primeiro ao último uso.",
        ],
        "usos": [
            "Escoramento de laje maciça, nervurada e pré-moldada",
            "Sustentação de forma de viga e de fundo de laje",
            "Reescoramento após a desforma",
            "Apoio temporário em reforma e recuperação estrutural",
            "Travamento de forma de pilar",
        ],
        "escolher": [
            ("Pé-direito da laje",
             "Cada faixa de escora tem altura mínima e máxima. Informe o pé-direito "
             "real, do contrapiso ao fundo da forma."),
            ("Quantidade e espaçamento",
             "O espaçamento vem do projeto estrutural, não do bom senso. Se você tem a "
             "planta, a conta da quantidade sai rápido."),
            ("Tipo de laje",
             "Laje pré-moldada, maciça e nervurada distribuem carga de formas diferentes "
             "e mudam o número de pontos de apoio."),
            ("Tempo até a desforma",
             "O período de locação precisa cobrir a cura e o reescoramento. Fechar curto "
             "demais sai mais caro no fim."),
        ],
        "inclui": [
            "Escoras conferidas quanto a rosca, pino e base",
            "Entrega e retirada com frota própria",
            "Reposição de peça danificada durante o uso",
        ],
        "norma": ("O escoramento deve seguir o projeto estrutural e a NR-18. A definição de "
                  "quantidade, espaçamento e prazo de desforma é do responsável técnico "
                  "pela obra. Nós fornecemos o equipamento em condição de uso."),
        "faq": [
            ("Quantas escoras eu preciso?",
             "Quem define é o projeto estrutural, a partir da carga e do vão da laje. "
             "Com a planta em mãos, conseguimos ajudar no cálculo da quantidade a alugar."),
            ("Escora metálica é melhor que pontalete de madeira?",
             "Para escoramento é sim, na maioria dos casos: a metálica regula a altura, "
             "mantém capacidade de carga constante e não empena com a umidade do concreto."),
            ("Vocês alugam junto com forma?",
             "Fale com a gente pelo WhatsApp que verificamos a disponibilidade do conjunto "
             "para a sua obra."),
        ],
    },
    {
        "slug": "furadeiras-e-parafusadeiras",
        "nome": "Furadeiras e parafusadeiras",
        "singular": "furadeira",
        "resumo": "Furadeira de impacto e parafusadeira a bateria para fixação, montagem e instalação.",
        "h1": "Aluguel de furadeiras e parafusadeiras no Rio de Janeiro",
        "title": "Aluguel de Furadeira e Parafusadeira no Rio de Janeiro | Locação",
        "desc": "Locação de furadeira de impacto e parafusadeira a bateria no Rio de Janeiro. Equipamento profissional revisado, entrega na obra e orçamento no WhatsApp.",
        "sinonimos": ["furadeira de impacto", "parafusadeira a bateria", "furadeira profissional",
                      "locação de furadeira", "aparafusadeira"],
        "intro": [
            "É a dupla que aparece em quase toda etapa da obra: furar para fixar e "
            "parafusar para montar. A diferença entre a ferramenta doméstica e a "
            "profissional aparece no terceiro dia de uso contínuo, quando uma esquenta e "
            "perde torque e a outra segue no mesmo ritmo.",
            "Alugamos furadeira de impacto, para furo em alvenaria e concreto leve, e "
            "parafusadeira a bateria, para montagem de drywall, forro, marcenaria e "
            "estrutura metálica leve.",
        ],
        "usos": [
            "Fixação de bucha, suporte e mão-francesa",
            "Montagem de drywall, forro e perfil metálico",
            "Instalação de móvel planejado e marcenaria",
            "Fixação de eletrocalha, eletroduto e quadro",
            "Montagem de estrutura leve e esquadria",
        ],
        "escolher": [
            ("Material a furar",
             "Alvenaria e concreto leve pedem impacto. Madeira, drywall e metal pedem furo "
             "sem percussão, com broca própria."),
            ("Com fio ou a bateria",
             "Com fio entrega torque constante e não para. A bateria ganha em mobilidade "
             "em obra sem energia ou em altura."),
            ("Volume de fixações",
             "Poucas fixações resolvem com uma ferramenta. Montagem de forro inteiro rende "
             "muito mais com duas parafusadeiras em paralelo."),
            ("Brocas e bits necessários",
             "Informe as bitolas que você vai usar para separarmos junto com a ferramenta."),
        ],
        "inclui": [
            "Brocas e bits conforme o serviço combinado",
            "Bateria e carregador nos modelos sem fio",
            "Maleta de transporte quando aplicável",
        ],
        "norma": None,
        "faq": [
            ("Furadeira de impacto substitui martelete?",
             "Para furo pequeno em alvenaria, sim. Para concreto estrutural e furo de "
             "diâmetro maior, não: o serviço rende pouco e desgasta a ferramenta. Nesse "
             "caso o indicado é martelete."),
            ("A bateria e o carregador vão junto?",
             "Vão. Os modelos sem fio saem com bateria e carregador."),
            ("Posso alugar mais de uma para a mesma obra?",
             "Pode, e para montagem de drywall e forro costuma compensar bastante. "
             "Consulte a disponibilidade pelo WhatsApp."),
        ],
    },
    {
        "slug": "lixadeiras-e-esmerilhadeiras",
        "nome": "Lixadeiras e esmerilhadeiras",
        "singular": "lixadeira",
        "resumo": "Acabamento em parede, corte em metal e desbaste de concreto com disco adequado.",
        "h1": "Aluguel de lixadeiras e esmerilhadeiras no Rio de Janeiro",
        "title": "Aluguel de Lixadeira e Esmerilhadeira no Rio de Janeiro | Locação",
        "desc": "Locação de lixadeira de parede e esmerilhadeira angular no Rio de Janeiro. Acabamento, corte e desbaste. Entrega na obra e orçamento pelo WhatsApp.",
        "sinonimos": ["lixadeira de parede", "esmerilhadeira angular", "lixadeira girafa",
                      "makita esmerilhadeira", "policorte", "locação de lixadeira"],
        "intro": [
            "O acabamento é o que o cliente enxerga. Lixar massa corrida na mão em uma "
            "sala inteira consome dias e devolve parede ondulada; com lixadeira própria, "
            "o mesmo serviço sai em horas e com superfície plana de verdade.",
            "A esmerilhadeira angular é a outra ponta: corta metal, desbasta concreto e "
            "remove rebarba, trocando só o disco. É provavelmente a ferramenta mais "
            "versátil do canteiro, e também a que mais exige atenção com segurança.",
        ],
        "usos": [
            "Lixamento de massa corrida, gesso e reboco",
            "Preparo de parede e teto antes da pintura",
            "Corte de ferro, vergalhão, perfil e cantoneira",
            "Desbaste de concreto e remoção de rebarba",
            "Corte de cerâmica e recorte pontual em piso",
            "Remoção de ferrugem e preparo de superfície metálica",
        ],
        "escolher": [
            ("Superfície ou metal",
             "Parede e teto pedem lixadeira de acabamento, de preferência com aspiração. "
             "Metal e concreto pedem esmerilhadeira com disco específico."),
            ("Pé-direito da área",
             "Teto alto e parede de escada rendem muito mais com lixadeira de haste, a "
             "chamada girafa, que dispensa andaime para o lixamento."),
            ("Controle de poeira",
             "Lixamento de massa gera poeira fina em volume alto. Se a área é habitada, "
             "vale combinar aspiração e isolamento antes de começar."),
            ("Disco e grão corretos",
             "Grão grosso desbasta e deixa marca, grão fino acaba e rende menos. Diga a "
             "etapa que a gente indica a sequência."),
        ],
        "inclui": [
            "Discos e lixas conforme o serviço combinado",
            "Equipamento com proteção e punho revisados",
            "Entrega e retirada com frota própria",
        ],
        "norma": ("Esmerilhadeira é a ferramenta que mais causa acidente de mão e olho em "
                  "obra. Nunca remova a proteção do disco, use óculos de segurança e "
                  "protetor facial, e confirme se o disco é compatível com a rotação da "
                  "máquina, conforme a NR-12."),
        "faq": [
            ("Dá para cortar cerâmica com esmerilhadeira?",
             "Dá, com disco diamantado próprio e muito cuidado com a poeira e com o "
             "acabamento da borda. Para volume alto de corte, o cortador de piso entrega "
             "resultado melhor e mais rápido."),
            ("A lixadeira de parede aspira o pó?",
             "Os modelos com aspiração reduzem bastante a poeira, mas não eliminam. "
             "Máscara e isolamento do ambiente continuam necessários."),
            ("Os discos estão incluídos?",
             "Incluímos os discos conforme o serviço que você descrever no orçamento."),
        ],
    },
    {
        "slug": "serras-e-plainas",
        "nome": "Serras e plainas",
        "singular": "serra",
        "resumo": "Serra circular, tico-tico e plaina para corte e acabamento em madeira e forma.",
        "h1": "Aluguel de serras e plainas no Rio de Janeiro",
        "title": "Aluguel de Serra Circular e Plaina no Rio de Janeiro | Locação",
        "desc": "Locação de serra circular, serra tico-tico e plaina elétrica no Rio de Janeiro. Corte e acabamento em madeira. Entrega na obra e orçamento no WhatsApp.",
        "sinonimos": ["serra circular", "serra tico-tico", "plaina elétrica",
                      "serra mármore", "locação de serra", "serra de bancada"],
        "intro": [
            "Corte de madeira em obra tem duas exigências: velocidade e esquadro. Serra "
            "circular resolve corte reto e repetido em compensado, tábua e sarrafo. "
            "Tico-tico resolve o recorte curvo e o acabamento onde a circular não entra.",
            "A plaina fecha o serviço: acerta espessura, tira empeno e deixa a peça pronta "
            "para receber acabamento. Para carpintaria de forma, é a diferença entre uma "
            "forma que fecha e uma que vaza nata.",
        ],
        "usos": [
            "Corte de compensado, chapa e sarrafo para forma",
            "Carpintaria de obra e montagem de gabarito",
            "Recorte curvo em bancada, tampo e painel",
            "Aplainamento e ajuste de espessura de peça",
            "Corte de porta, rodapé e batente",
            "Marcenaria de acabamento e montagem",
        ],
        "escolher": [
            ("Tipo de corte",
             "Reto e longo pede serra circular. Curvo e recorte pede tico-tico. "
             "Repetição em série rende muito mais com serra de bancada."),
            ("Espessura da peça",
             "Cada serra tem profundidade máxima de corte. Peça grossa demais para a "
             "máquina resulta em corte torto e disco forçado."),
            ("Tipo de madeira",
             "Madeira de lei, compensado plastificado e MDF pedem disco com dentes "
             "diferentes. Disco errado queima a borda."),
            ("Acabamento esperado",
             "Se a peça fica aparente, vale combinar disco de acabamento e plaina, não só "
             "o corte bruto."),
        ],
        "inclui": [
            "Discos e lâminas conforme o material combinado",
            "Guias e proteções revisadas",
            "Entrega e retirada com frota própria",
        ],
        "norma": ("Serra é ferramenta de corte contínuo e exige proteção do disco sempre "
                  "instalada, óculos, protetor auricular e atenção com o cabo. Nunca "
                  "trave o gatilho nem retire o protetor, conforme a NR-12."),
        "faq": [
            ("Qual serra usar para corte de porcelanato?",
             "Serra mármore com disco diamantado, e de preferência com refrigeração. "
             "Para volume alto, o cortador de piso de bancada rende mais."),
            ("A plaina serve para tirar tinta velha?",
             "Não é o indicado. Plaina remove material da madeira. Para remover tinta, "
             "lixadeira ou soprador térmico entregam resultado melhor."),
            ("Vocês fornecem os discos?",
             "Fornecemos conforme o material que você informar no pedido de orçamento."),
        ],
    },
    {
        "slug": "escadas",
        "nome": "Escadas",
        "singular": "escada",
        "resumo": "Escadas de alumínio e extensíveis para acesso seguro em manutenção e instalação.",
        "h1": "Aluguel de escadas de alumínio no Rio de Janeiro",
        "title": "Aluguel de Escada de Alumínio no Rio de Janeiro | Locação",
        "desc": "Locação de escadas de alumínio e extensíveis no Rio de Janeiro. Acesso seguro para manutenção, instalação e pintura. Entrega na obra e orçamento no WhatsApp.",
        "sinonimos": ["escada de alumínio", "escada extensível", "escada de abrir",
                      "escada de fibra", "locação de escada", "escada profissional"],
        "intro": [
            "Escada é o equipamento mais subestimado e um dos que mais causam queda em "
            "obra. Cadeira, caixote e escada de madeira velha continuam sendo o improviso "
            "mais caro do canteiro.",
            "Alugamos escada de alumínio em diferentes alturas, incluindo modelo "
            "extensível para alcance maior. Para serviço que passa de poucos minutos ou "
            "que exige as duas mãos livres, o correto é andaime, e a gente diz isso "
            "quando é o caso.",
        ],
        "usos": [
            "Manutenção elétrica e troca de luminária",
            "Instalação de ar-condicionado e antena",
            "Pintura de teto e parede alta",
            "Limpeza de calha e telhado",
            "Acesso a caixa d'água e casa de máquinas",
            "Instalação de cortina, persiana e suporte",
        ],
        "escolher": [
            ("Altura de alcance, não altura da escada",
             "A altura útil considera o degrau seguro mais alto, que não é o último. "
             "Meça o ponto de trabalho e some a folga."),
            ("Piso de apoio",
             "Piso liso e molhado exige sapata antiderrapante em boas condições. Terreno "
             "irregular exige nivelamento antes."),
            ("Serviço elétrico",
             "Trabalho perto de energia pede escada de fibra, que não conduz. Alumínio "
             "conduz e não deve ser usado nesse cenário."),
            ("Tempo em cima",
             "Serviço longo ou que exija as duas mãos livres não é serviço de escada. "
             "Nesse caso, andaime é mais seguro e mais produtivo."),
        ],
        "inclui": [
            "Escada com sapatas e travas conferidas",
            "Entrega e retirada com frota própria",
            "Orientação sobre o modelo adequado ao serviço",
        ],
        "norma": ("A NR-35 trata de trabalho em altura acima de 2 metros e exige análise de "
                  "risco, treinamento e proteção contra queda. Escada é meio de acesso, não "
                  "plataforma de trabalho prolongado."),
        "faq": [
            ("Escada ou andaime para pintar a fachada?",
             "Andaime, sem discussão. Escada serve para acesso e serviço rápido e pontual. "
             "Pintura de fachada exige plataforma estável, com guarda-corpo."),
            ("Vocês têm escada de fibra?",
             "Consulte a disponibilidade pelo WhatsApp informando a altura necessária e se "
             "o serviço é elétrico."),
            ("Qual altura eu preciso?",
             "Meça a altura do ponto de trabalho e conte que o degrau seguro mais alto fica "
             "abaixo do topo. Na dúvida, mande a medida que a gente indica."),
        ],
    },
    {
        "slug": "lavadoras-de-alta-pressao",
        "nome": "Lavadoras de alta pressão",
        "singular": "lavadora de alta pressão",
        "resumo": "Limpeza pesada de fachada, piso e calçada, com jato que tira o que a vassoura não tira.",
        "h1": "Aluguel de lavadoras de alta pressão no Rio de Janeiro",
        "title": "Aluguel de Lavadora de Alta Pressão no Rio de Janeiro | Locação",
        "desc": "Locação de lavadora de alta pressão no Rio de Janeiro. Limpeza de fachada, piso, calçada e pós-obra. Entrega e orçamento rápido pelo WhatsApp.",
        "sinonimos": ["lava jato profissional", "lavadora de alta pressão",
                      "máquina de lavar piso", "locação de lava jato", "hidrojato"],
        "intro": [
            "Limpeza de pós-obra e de fachada com balde e vassoura consome dias e não "
            "chega ao resultado. Alta pressão remove nata de cimento, limo, fuligem e "
            "tinta solta em uma passagem, e prepara a superfície para pintura ou "
            "impermeabilização.",
            "É também o equipamento que mais economiza mão de obra em condomínio: "
            "garagem, calçada, área de lazer e fachada saem em uma fração do tempo.",
        ],
        "usos": [
            "Limpeza de pós-obra em piso e calçada",
            "Remoção de limo, fuligem e mofo em fachada",
            "Preparo de superfície antes de pintar",
            "Lavagem de garagem, rampa e área comum",
            "Limpeza de telhado, muro e grade",
            "Lavagem de máquina e caçamba",
        ],
        "escolher": [
            ("Área e frequência",
             "Uso pontual e uso contínuo pedem máquinas diferentes. Lavagem de condomínio "
             "inteiro exige equipamento de trabalho contínuo."),
            ("Superfície a limpar",
             "Pressão alta demais marca madeira, pintura e revestimento delicado. Diga a "
             "superfície que a gente indica a regulagem e o bico."),
            ("Ponto de água e de energia",
             "A lavadora precisa de alimentação de água constante. Confirme se existe "
             "torneira próxima ou reservatório."),
            ("Acessórios necessários",
             "Bico turbo, extensão de mangueira e escova rotativa mudam bastante o "
             "rendimento em área grande."),
        ],
        "inclui": [
            "Mangueira, pistola e bicos conforme o serviço",
            "Equipamento testado antes da entrega",
            "Entrega e retirada com frota própria",
        ],
        "norma": ("Jato de alta pressão corta pele. Nunca aponte para pessoa ou animal, use "
                  "óculos e bota, e mantenha o equipamento longe de conexão elétrica "
                  "energizada."),
        "faq": [
            ("A lavadora vem com mangueira?",
             "Vem, junto com pistola e os bicos adequados ao serviço que você descrever."),
            ("Serve para limpar fachada pintada?",
             "Serve, com pressão controlada e bico de leque. Pressão alta demais remove a "
             "tinta, o que às vezes é exatamente o objetivo antes de repintar."),
            ("Preciso de ponto de água na obra?",
             "Sim, ou de um reservatório com volume suficiente. A máquina não pode operar "
             "sem alimentação contínua de água."),
        ],
    },
    {
        "slug": "lavadoras-de-estofado",
        "nome": "Lavadoras de estofado",
        "singular": "lavadora de estofado",
        "resumo": "Extratora para sofá, colchão, cadeira e carpete, com injeção e sucção.",
        "h1": "Aluguel de lavadoras de estofado no Rio de Janeiro",
        "title": "Aluguel de Extratora e Lavadora de Estofado no Rio de Janeiro",
        "desc": "Locação de lavadora extratora de estofado no Rio de Janeiro. Sofá, colchão, cadeira, carpete e interior de veículo. Entrega e orçamento no WhatsApp.",
        "sinonimos": ["extratora de estofado", "lavadora de sofá", "máquina de limpar carpete",
                      "extratora profissional", "locação de extratora"],
        "intro": [
            "Extratora injeta solução de limpeza no tecido e puxa de volta a sujeira "
            "dissolvida. É o que diferencia limpar de verdade de apenas passar pano: a "
            "sujeira sai da fibra em vez de descer para o enchimento.",
            "É o equipamento de quem trabalha com limpeza profissional, e também de quem "
            "quer recuperar sofá, colchão e carpete de casa sem contratar serviço.",
        ],
        "usos": [
            "Limpeza de sofá, poltrona e cadeira estofada",
            "Higienização de colchão e cabeceira",
            "Limpeza de carpete e tapete",
            "Higienização de interior de veículo",
            "Limpeza de cortina e persiana de tecido",
            "Pós-obra em ambiente com estofado e carpete",
        ],
        "escolher": [
            ("Volume de peças",
             "Uma peça pontual é um cenário. Limpeza de escritório inteiro é outro, e pede "
             "reservatório maior para não parar a cada dez minutos."),
            ("Tipo de tecido",
             "Tecido delicado, couro e camurça exigem produto e técnica específicos. "
             "Na dúvida, teste em área escondida antes."),
            ("Tempo de secagem",
             "Ambiente sem ventilação prolonga muito a secagem. Programe o serviço para "
             "um dia em que dê para abrir janela e ligar ventilador."),
            ("Produto adequado",
             "Use produto próprio para extratora. Detergente comum gera espuma que danifica "
             "o motor de sucção."),
        ],
        "inclui": [
            "Bico e mangueira de extração",
            "Equipamento higienizado antes da entrega",
            "Orientação de uso e de diluição",
        ],
        "norma": None,
        "faq": [
            ("O produto de limpeza está incluso?",
             "Consulte pelo WhatsApp. O produto correto muda conforme o tecido, e usar "
             "detergente comum danifica o equipamento."),
            ("Quanto tempo o estofado leva para secar?",
             "Depende do tecido, do enchimento e da ventilação do ambiente. Estofado denso "
             "em ambiente fechado pode levar bem mais de um dia."),
            ("Serve para limpar carro?",
             "Serve, e é um dos usos mais comuns: banco, forro, carpete e porta-malas."),
        ],
    },
    {
        "slug": "motosserras-e-rocadeiras",
        "nome": "Motosserras e roçadeiras",
        "singular": "motosserra",
        "resumo": "Poda, corte de árvore e limpeza de terreno com equipamento revisado e afiado.",
        "h1": "Aluguel de motosserras e roçadeiras no Rio de Janeiro",
        "title": "Aluguel de Motosserra e Roçadeira no Rio de Janeiro | Locação",
        "desc": "Locação de motosserra e roçadeira no Rio de Janeiro. Poda, corte de árvore e limpeza de terreno. Equipamento revisado e orçamento pelo WhatsApp.",
        "sinonimos": ["motosserra", "roçadeira", "aparador de grama profissional",
                      "locação de motosserra", "podador"],
        "intro": [
            "Terreno tomado por mato e árvore fora de controle travam o começo da obra e "
            "viram risco. Roçadeira limpa a área em horas e motosserra resolve poda e "
            "corte que machado não vence.",
            "Todo equipamento sai com corrente ou lâmina afiada e com revisão de motor. "
            "Corrente cega é a principal causa de acidente com motosserra, porque força o "
            "operador e provoca coice.",
        ],
        "usos": [
            "Limpeza de terreno antes do início da obra",
            "Poda de galho e manutenção de área verde",
            "Corte de árvore caída e remoção pós-temporal",
            "Roçada de gramado alto, talude e beira de muro",
            "Corte de madeira para escoramento e forma",
            "Manutenção de sítio, chácara e área de lazer",
        ],
        "escolher": [
            ("Diâmetro do que vai cortar",
             "Galho fino e tronco grosso pedem sabres de comprimento diferente. Informe o "
             "diâmetro aproximado."),
            ("Área e tipo de vegetação",
             "Grama alta, mato fibroso e capim duro pedem fio ou lâmina distintos na "
             "roçadeira."),
            ("Altura da poda",
             "Poda acima da cabeça é trabalho em altura e exige planejamento à parte, com "
             "acesso adequado e proteção contra queda."),
            ("Experiência do operador",
             "Motosserra não é ferramenta para quem nunca usou. Se não houver alguém "
             "treinado, o certo é contratar serviço."),
        ],
        "inclui": [
            "Corrente ou lâmina afiada",
            "Equipamento revisado e abastecido para o primeiro uso",
            "Entrega e retirada com frota própria",
        ],
        "norma": ("Motosserra exige EPI completo: calça anticorte, bota com biqueira, "
                  "protetor facial e auricular e luva. Corte de árvore em área urbana pode "
                  "exigir autorização do órgão ambiental municipal."),
        "faq": [
            ("Preciso de autorização para cortar árvore?",
             "Em área urbana no Rio de Janeiro, o corte e a poda pesada de árvore costumam "
             "exigir autorização do órgão ambiental municipal. Consulte a prefeitura antes."),
            ("O equipamento vem abastecido?",
             "Entregamos pronto para o primeiro uso e orientamos sobre a mistura de "
             "combustível correta para o restante do período."),
            ("Vocês fornecem EPI?",
             "Consulte a disponibilidade pelo WhatsApp. Motosserra sem EPI adequado não "
             "deve ser operada em hipótese nenhuma."),
        ],
    },
    {
        "slug": "sopradores-e-aspiradores",
        "nome": "Sopradores e aspiradores",
        "singular": "soprador",
        "resumo": "Limpeza de pós-obra, remoção de entulho fino e organização rápida do canteiro.",
        "h1": "Aluguel de sopradores e aspiradores no Rio de Janeiro",
        "title": "Aluguel de Soprador e Aspirador de Pó no Rio de Janeiro | Locação",
        "desc": "Locação de soprador e aspirador de pó e água no Rio de Janeiro. Limpeza de pós-obra e canteiro. Entrega na obra e orçamento rápido no WhatsApp.",
        "sinonimos": ["aspirador de pó e água", "soprador de folhas", "aspirador industrial",
                      "aspirador de obra", "locação de aspirador"],
        "intro": [
            "Limpeza de pós-obra é a etapa que o cliente final julga. Aspirador de pó e "
            "água engole entulho fino, resto de gesso, água de lavagem e poeira de "
            "lixamento, coisa que aspirador doméstico não aguenta.",
            "O soprador faz o trabalho grosso: junta folha, poeira e resíduo de área "
            "externa em minutos, e mantém o canteiro organizado durante a obra, o que "
            "reduz acidente e retrabalho.",
        ],
        "usos": [
            "Limpeza de pós-obra em apartamento, casa e loja",
            "Aspiração de resíduo de lixamento e corte",
            "Remoção de água acumulada após lavagem ou chuva",
            "Limpeza diária do canteiro",
            "Limpeza de área externa, garagem e calçada",
            "Manutenção de condomínio e área comum",
        ],
        "escolher": [
            ("Sólido, líquido ou os dois",
             "Aspirador de pó e água resolve os dois cenários. Modelo só de sólidos não "
             "pode aspirar líquido, sob risco de dano ao motor."),
            ("Volume do reservatório",
             "Obra grande com reservatório pequeno vira ida e volta para o descarte."),
            ("Tipo de resíduo",
             "Pó de gesso e de massa entope filtro comum rápido. Vale combinar filtro "
             "adequado e limpeza durante o uso."),
            ("Área interna ou externa",
             "Soprador resolve área externa. Em ambiente interno ele só espalha a poeira, "
             "e o certo é aspirar."),
        ],
        "inclui": [
            "Mangueira, bocais e filtro",
            "Equipamento higienizado antes da entrega",
            "Entrega e retirada com frota própria",
        ],
        "norma": None,
        "faq": [
            ("O aspirador pega água?",
             "Os modelos de pó e água pegam. Confirme no pedido, porque aspirar líquido "
             "com equipamento só de sólidos danifica o motor."),
            ("Serve para pó de gesso?",
             "Serve, com filtro adequado e limpeza do filtro durante o uso. Pó de gesso "
             "satura filtro comum rápido."),
            ("Soprador serve dentro de casa?",
             "Não é o indicado. Dentro de casa ele só levanta a poeira. O certo é aspirar."),
        ],
    },
    {
        "slug": "bombas-sapo",
        "nome": "Bombas sapo",
        "singular": "bomba sapo",
        "resumo": "Bomba submersível para esgotar vala, poço, fosso de elevador e alagamento.",
        "h1": "Aluguel de bombas sapo submersíveis no Rio de Janeiro",
        "title": "Aluguel de Bomba Sapo Submersível no Rio de Janeiro | Locação",
        "desc": "Locação de bomba sapo submersível no Rio de Janeiro. Esgotamento de vala, poço, fosso e alagamento. Entrega na obra e orçamento rápido no WhatsApp.",
        "sinonimos": ["bomba submersível", "bomba sapo", "bomba de esgotamento",
                      "bomba de porão", "locação de bomba d'água"],
        "intro": [
            "Vala alagada para a obra. Bomba sapo é o equipamento que devolve a frente de "
            "trabalho: joga na bomba, liga e a água sai. Em época de chuva no Rio, é um "
            "dos itens mais procurados da locação.",
            "Trabalhamos com bomba submersível para água limpa e para água com sólido em "
            "suspensão, que é o caso quase sempre em obra, onde a água vem misturada com "
            "barro e resto de material.",
        ],
        "usos": [
            "Esgotamento de vala de fundação e de tubulação",
            "Drenagem de poço, cisterna e reservatório",
            "Fosso de elevador e subsolo alagado",
            "Remoção de água de chuva acumulada",
            "Rebaixamento de lençol em escavação rasa",
            "Esvaziamento de piscina e caixa d'água",
        ],
        "escolher": [
            ("Água limpa ou com sólido",
             "Água de obra quase sempre tem barro e resíduo. Bomba de água limpa entope e "
             "queima nesse cenário."),
            ("Altura de recalque",
             "É a diferença de altura entre a bomba e o ponto de descarte. Quanto maior, "
             "menor a vazão real. Informe a altura no orçamento."),
            ("Vazão necessária",
             "Depende do volume e de quanto tempo você tem. Alagamento que precisa "
             "esvaziar rápido pede vazão maior ou mais de uma bomba."),
            ("Energia no ponto",
             "A bomba precisa de tomada com aterramento e disjuntor adequado, o que exige "
             "atenção redobrada em área alagada."),
        ],
        "inclui": [
            "Bomba testada antes da entrega",
            "Mangueira conforme o serviço combinado",
            "Entrega e retirada com frota própria",
        ],
        "norma": ("Equipamento elétrico em área alagada exige aterramento e disjuntor "
                  "diferencial. Nunca manuseie a bomba ligada nem entre na água com o "
                  "equipamento energizado."),
        "faq": [
            ("A bomba aguenta água com barro?",
             "Os modelos para água servida aguentam sólido em suspensão. Informe a "
             "condição da água no pedido, porque bomba de água limpa não serve para isso."),
            ("A mangueira vai junto?",
             "Vai, no comprimento combinado. Informe a distância até o ponto de descarte."),
            ("Quanto tempo a bomba pode ficar ligada?",
             "Os modelos submersíveis trabalham em regime contínuo desde que fiquem "
             "submersos. Bomba operando a seco queima."),
        ],
    },
]

EQ_BY_SLUG = {e["slug"]: e for e in EQUIPAMENTOS}
DESTAQUES = sorted([e for e in EQUIPAMENTOS if e.get("destaque")], key=lambda e: e["destaque"])


def relacionados(slug, n=4):
    """Equipamentos relacionados: os vizinhos na lista, em ciclo."""
    idx = [e["slug"] for e in EQUIPAMENTOS].index(slug)
    out = []
    i = 1
    while len(out) < n:
        out.append(EQUIPAMENTOS[(idx + i) % len(EQUIPAMENTOS)])
        i += 1
    return out


# ===========================================================================
# DEPOIMENTOS
# ===========================================================================
# Transcritos das avaliacoes publicas do Google exibidas no site atual.
# NAO invente depoimento. Para trocar, use avaliacao real e mantenha o nome.
DEPOIMENTOS = [
    {"nome": "Fernando Golinelli", "meta": "Local Guide · 477 avaliações", "nota": 5,
     "texto": "A loja sempre tem tudo que preciso e conta com ótimo atendimento."},
    {"nome": "Victor Matos", "meta": "Local Guide · 12 avaliações", "nota": 5,
     "texto": "Atendimento ótimo, preços muito bons. Possuem estacionamento."},
    {"nome": "Fernando Zordan", "meta": "Local Guide · 139 avaliações", "nota": 5,
     "texto": "Grande variedade, bom preço, recomendo."},
    {"nome": "Edson Sá", "meta": "10 avaliações", "nota": 5,
     "texto": "Muito bom no preço, na qualidade e no atendimento dedicado e carinhoso "
              "pelos funcionários, parabéns! Compro sempre lá e indico."},
    {"nome": "Júlia Rocha", "meta": "8 avaliações", "nota": 5,
     "texto": "Excelente loja e atendimento! Precisava de uma lista de materiais e, leiga "
              "que sou, confesso que fiquei um pouco intimidada. No entanto, recebi um "
              "tratamento super paciente e cuidadoso."},
]

# ===========================================================================
# PAGAMENTO
# ===========================================================================
PAGAMENTOS = [
    ("pix", "PIX", "Confirmação na hora, sem taxa adicional."),
    ("card", "Cartão de crédito", "Parcelamento flexível conforme o valor."),
    ("card", "Cartão de débito", "Rapidez e segurança no ato."),
    ("doc", "Boleto bancário", "Para empresa e construtora, com prazo combinado."),
    ("bank", "Transferência", "Direto da conta, sem burocracia."),
]

# ===========================================================================
# FAQ GERAL
# ===========================================================================
FAQ_GERAL = [
    ("Quais equipamentos vocês alugam?",
     "Trabalhamos com 15 categorias: andaimes, betoneiras, marteletes, compactadores, "
     "cortadores de piso, escoras, escadas, furadeiras e parafusadeiras, lixadeiras e "
     "esmerilhadeiras, serras e plainas, lavadoras de alta pressão, lavadoras de estofado, "
     "motosserras e roçadeiras, sopradores e aspiradores e bombas sapo. Os mais procurados "
     "são andaime, betoneira e martelete."),
    ("Por quanto tempo posso alugar?",
     "O período é flexível: diária, semanal, quinzenal ou mensal. Obra de fachada e "
     "escoramento costumam fechar por mês; serviço pontual de furo ou corte resolve na "
     "diária. Se a obra atrasar, avise antes do fim do período que renovamos."),
    ("Os equipamentos são revisados?",
     "Sim. Cada item passa por inspeção, limpeza e manutenção preventiva antes de sair "
     "para a obra, seguindo as normas de segurança aplicáveis, entre elas a NR-12, "
     "para máquinas e equipamentos, e a NR-18, para o canteiro."),
    ("Vocês entregam na obra?",
     "Entregamos e retiramos com frota própria nas regiões atendidas por cada unidade. "
     "Informe o endereço da obra no orçamento que confirmamos prazo e condição de entrega."),
    ("Quais são as formas de pagamento?",
     "PIX, cartão de crédito, cartão de débito, boleto bancário e transferência. "
     "Para construtora e empresa, o boleto com prazo combinado costuma ser o formato "
     "mais prático."),
    ("Como peço um orçamento?",
     "Pelo WhatsApp, que é o caminho mais rápido: mande a lista do que precisa, o endereço "
     "da obra e o período. Também dá para usar o formulário do site, que monta a mensagem "
     "para você."),
    ("Preciso de cadastro ou contrato para alugar?",
     "Para começar o orçamento, não. Basta chamar no WhatsApp. A documentação necessária "
     "para a locação é combinada no momento do fechamento e varia conforme o equipamento "
     "e o período."),
    ("Quais bairros vocês atendem no Rio de Janeiro?",
     "Temos unidades no Recreio dos Bandeirantes (duas), em Vargem Grande, em Pedra de "
     "Guaratiba e em Botafogo, e a entrega sai da que estiver mais perto da obra. "
     "Na Barra e no Recreio, atendemos também Barra Olímpica, São Conrado, Itanhangá, "
     "Joá e Grumari. Nas vargens e em Jacarepaguá, vamos de Vargem Grande e Vargem "
     "Pequena a Camorim, Curicica, Freguesia, Taquara, Anil e Praça Seca. Na região de "
     "Guaratiba, cobrimos Barra de Guaratiba, Campo Grande, Santa Cruz, Sepetiba, "
     "Cosmos e Santíssimo. Na Zona Sul, de Botafogo e Humaitá a Copacabana, Ipanema e "
     "Leblon. Também entregamos em Bangu, Realengo e em parte da Zona Norte, como "
     "Madureira, Méier e Irajá. Não achou o seu bairro? Chame no WhatsApp: na maior "
     "parte dos casos conseguimos atender."),
    ("O que acontece se o equipamento apresentar defeito na obra?",
     "Avise pelo WhatsApp da unidade. Defeito que não venha de mau uso é resolvido com "
     "troca ou reparo, para que a obra não fique parada."),
    ("Vocês montam o andaime ou o escoramento?",
     "A locação é do equipamento. A montagem fica com a equipe da obra, sob "
     "responsabilidade do responsável técnico, e nós orientamos a sequência correta. "
     "Se você precisa de montagem, fale com a gente que indicamos o caminho."),
]

# ===========================================================================
# DIFERENCIAIS
# ===========================================================================
DIFERENCIAIS = [
    ("shield", "Equipamento revisado, não improvisado",
     "Cada item passa por inspeção, limpeza e manutenção antes de sair. "
     "Peça com folga, solda aberta ou motor cansado não vai para a obra."),
    ("truck", "Frota própria para entregar e retirar",
     "Não dependemos de transportadora. A entrega e a retirada são nossas, o que encurta "
     "prazo e evita o equipamento parado esperando carona."),
    ("chat", "Atendimento de quem já pisou em canteiro",
     "Você fala com gente que entende o que é uma laje escorada e o que é uma fachada "
     "para pintar. Isso muda a qualidade da recomendação."),
    ("store", "Cinco unidades no Rio de Janeiro",
     "Duas no Recreio dos Bandeirantes, uma em Vargem Grande, uma em Pedra de "
     "Guaratiba e uma em Botafogo. Sempre tem uma base perto da sua obra."),
    ("money", "Preço claro, sem letra miúda",
     "Você recebe o valor, o período e as condições no orçamento. Sem taxa que aparece "
     "só na devolução."),
    ("gauge", "Resposta rápida no WhatsApp",
     "Mandou a lista, a gente responde com disponibilidade e valor. Sem formulário longo, "
     "sem cadastro obrigatório e sem espera de dias."),
]
