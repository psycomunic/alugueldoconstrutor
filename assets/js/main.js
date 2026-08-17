/* =========================================================================
   Aluguel do Construtor - interacoes
   Vanilla, sem dependencias. Tudo degrada bem sem JS.
   ========================================================================= */
(function () {
  'use strict';

  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  var calmo = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var temIO = 'IntersectionObserver' in window;

  /* rAF com throttle: usado pelo progresso e pelo parallax do hero */
  var noFrame = function (fn) {
    var pedido = false;
    return function () {
      if (pedido) return;
      pedido = true;
      requestAnimationFrame(function () { pedido = false; fn(); });
    };
  };

  /* ------------------------------------------------------------ header */
  var header = $('[data-header]');
  if (header) {
    /* barra de progresso da leitura, dentro do proprio header */
    var barra = document.createElement('div');
    barra.className = 'progress';
    barra.setAttribute('aria-hidden', 'true');
    header.appendChild(barra);

    /* Bloco escuro no topo da pagina. So existe se for o primeiro filho de
       main: na 404 o primeiro bloco e claro, entao nao ha sobreposicao e o
       header fica solido do inicio. */
    var capa = document.querySelector('main > .hero:first-child, main > .pagehead:first-child');

    var onScroll = noFrame(function () {
      var y = window.scrollY || 0;
      header.classList.toggle('is-stuck', y > 8);
      /* transparente enquanto o bloco escuro ainda cobre a altura do header */
      if (capa) {
        header.classList.toggle('is-over', capa.getBoundingClientRect().bottom > header.offsetHeight + 6);
      }
      var alcance = (document.documentElement.scrollHeight - window.innerHeight);
      barra.style.setProperty('--p', alcance > 0 ? Math.min(1, y / alcance).toFixed(4) : 0);
    });
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll, { passive: true });
  }

  /* ------------------------------------------------------------ drawer */
  var drawer = $('[data-drawer]');
  var burger = $('[data-burger]');
  if (drawer && burger) {
    var open = function (v) {
      drawer.classList.toggle('is-open', v);
      burger.setAttribute('aria-expanded', v ? 'true' : 'false');
      document.documentElement.style.overflow = v ? 'hidden' : '';
      if (v) { var f = drawer.querySelector('a, button'); if (f) f.focus(); }
    };
    burger.addEventListener('click', function () {
      open(burger.getAttribute('aria-expanded') !== 'true');
    });
    drawer.addEventListener('click', function (e) {
      if (e.target === drawer || e.target.closest('[data-drawer-close]') || e.target.tagName === 'A') open(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && drawer.classList.contains('is-open')) { open(false); burger.focus(); }
    });
  }

  /* ------------------------------------------------------------ reveal
     O build so marca .reveal na home. Para as outras 27 paginas nao ficarem
     estaticas, aqui a gente marca sozinho:
       - cabecalho de secao e figura entram com fade
       - grade de cards entra em cascata (data-stagger + --i por filho)
     Nada disso e marcado acima da primeira dobra, para nao piscar no load.
     ------------------------------------------------------------ */
  var abaixoDaDobra = function (el) {
    return el.getBoundingClientRect().top > window.innerHeight * 0.9;
  };

  if (!calmo) {
    /* cascata nas grades que ainda nao tem reveal proprio */
    $$('.eqgrid, .feat3, .units, .quotes, .pays, .steps, .grid, .checks').forEach(function (g) {
      if (g.querySelector('.reveal') || g.hasAttribute('data-stagger')) return;
      var filhos = $$(':scope > *', g);
      if (filhos.length < 2 || !abaixoDaDobra(g)) return;
      g.setAttribute('data-stagger', '');
      filhos.forEach(function (f, i) { f.style.setProperty('--i', Math.min(i, 9)); });
    });

    /* fade nos blocos de texto e imagem das paginas internas */
    $$('.sec-head, .figure, .prose > h2, .callout, .aside__card').forEach(function (el) {
      if (el.classList.contains('reveal') || el.closest('[data-stagger]')) return;
      if (!abaixoDaDobra(el)) return;
      el.classList.add('reveal');
      if (el.classList.contains('figure')) el.setAttribute('data-r', 'wipe');
    });
  }

  var alvos = $$('.reveal, [data-stagger]');
  if (alvos.length) {
    if (!temIO) {
      alvos.forEach(function (el) { el.classList.add('is-in'); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
      alvos.forEach(function (el) { io.observe(el); });
    }
  }

  /* ------------------------------------------------------------ parallax do hero
     Deslocamento pequeno na imagem enquanto rola. Da profundidade sem
     transformar a home em carrossel. */
  /* No .hero__img, nao no .hero__media: o media tem a animacao de entrada com
     fill both, e animacao vence estilo inline no cascade. O transform inline
     aqui seria ignorado. */
  var heroImg = $('.hero__img');
  if (heroImg && !calmo && window.innerWidth > 900) {
    var parallax = noFrame(function () {
      var y = window.scrollY || 0;
      if (y > window.innerHeight * 1.2) return;
      heroImg.style.transform = 'translate3d(0,' + (y * -0.045).toFixed(2) + 'px,0)';
    });
    parallax();
    window.addEventListener('scroll', parallax, { passive: true });
  }

  /* ------------------------------------------------------------ FAB do WhatsApp
     Esconde quando a faixa de CTA ou o rodape aparecem: ali ele e redundante
     e estava cobrindo o canto inferior direito do conteudo. */
  var fab = $('.wafab');
  if (fab && temIO) {
    var zonas = $$('.cta, .footer');
    if (zonas.length) {
      /* conjunto em vez de contador: nao acumula erro se o observer disparar
         fora de ordem ou repetido para o mesmo alvo */
      var naTela = [];
      var iof = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          var i = naTela.indexOf(en.target);
          if (en.isIntersecting && i === -1) naTela.push(en.target);
          if (!en.isIntersecting && i !== -1) naTela.splice(i, 1);
        });
        fab.classList.toggle('is-away', naTela.length > 0);
      }, { threshold: 0.06 });
      zonas.forEach(function (z) { iof.observe(z); });
    }
  }

  /* ------------------------------------------------------------ contador */
  var counters = $$('[data-count]');
  if (counters.length && 'IntersectionObserver' in window) {
    var ioc = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        ioc.unobserve(el);
        var target = parseFloat(el.getAttribute('data-count')) || 0;
        var dur = 1100, t0 = null;
        var tick = function (ts) {
          if (!t0) t0 = ts;
          var p = Math.min(1, (ts - t0) / dur);
          var e = 1 - Math.pow(1 - p, 3);
          el.textContent = Math.round(target * e).toString();
          if (p < 1) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
      });
    }, { threshold: 0.4 });
    counters.forEach(function (el) { ioc.observe(el); });
  } else {
    counters.forEach(function (el) { el.textContent = el.getAttribute('data-count'); });
  }

  /* ------------------------------------------------------------ FAQ: um aberto por vez */
  $$('[data-faq]').forEach(function (group) {
    var items = $$('details', group);
    items.forEach(function (d) {
      d.addEventListener('toggle', function () {
        if (!d.open) return;
        items.forEach(function (o) { if (o !== d) o.open = false; });
      });
    });
  });

  /* ------------------------------------------------------------ formulario -> WhatsApp
     Nao existe backend. O formulario monta a mensagem e abre a conversa.
     ------------------------------------------------------------ */
  $$('[data-wa-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var wa = form.getAttribute('data-wa-form');
      var d = new FormData(form);
      var picked = d.getAll('equipamento');
      var lines = ['Ol\u00e1! Vim pelo site do Aluguel do Construtor.', ''];

      var push = function (label, key) {
        var v = (d.get(key) || '').toString().trim();
        if (v) lines.push(label + ': ' + v);
      };
      push('Nome', 'nome');
      push('Telefone', 'telefone');
      push('E-mail', 'email');
      push('Unidade mais pr\u00f3xima', 'unidade');
      push('Bairro da obra', 'bairro');
      push('Per\u00edodo de loca\u00e7\u00e3o', 'periodo');
      if (picked.length) lines.push('Equipamentos: ' + picked.join(', '));
      push('Assunto', 'assunto');

      var msg = (d.get('mensagem') || '').toString().trim();
      if (msg) { lines.push(''); lines.push(msg); }

      var url = 'https://wa.me/' + wa + '?text=' + encodeURIComponent(lines.join('\n'));
      window.open(url, '_blank', 'noopener');

      var ok = form.querySelector('[data-form-ok]');
      if (ok) { ok.hidden = false; }
    });
  });

  /* ------------------------------------------------------------ contador do seletor */
  $$('[data-picker]').forEach(function (picker) {
    var out = $('[data-picker-count]', picker.closest('form') || document);
    var upd = function () {
      var n = $$('input:checked', picker).length;
      if (out) {
        out.textContent = n === 0 ? 'Nenhum item selecionado'
          : n === 1 ? '1 item selecionado' : n + ' itens selecionados';
      }
    };
    picker.addEventListener('change', upd);
    upd();
  });

  /* ------------------------------------------------------------ ano no rodape */
  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
