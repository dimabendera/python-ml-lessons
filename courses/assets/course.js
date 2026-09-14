/* Обгортка сторінки теми.
   Дописує те, що раніше вшивалось у кожен файл: підпис над заголовком, зміст,
   номери розділів і фігур, числа в посиланнях «розділ N», смугу переходів,
   блок «Далі в темі», пейджер і підвал. Порядок тем і назви бере з маніфесту
   курсу (../manifest.js → window.COURSE) — це єдине джерело.

   ⚠️ Класичний скрипт: без fetch і без модулів. Сторінки мають відкриватися
   просто з диска (file://), де і те, і те заблоковано.
   ⚠️ Текст лекції лишається в HTML. Скрипт лише дописує обгортку й номери:
   якщо він не спрацює, лекцію все одно можна прочитати.

   Розмітка, яку він розуміє:
     <p class="eyebrow" data-auto></p>               — «Курс · Блок N · Тема N»
     <div class="toc" data-auto></div>               — зміст із заголовків h2[id]
     <nav class="topnav" data-auto></nav>            — ← попередня · Усі теми · наступна →
     <h2 id="s3" data-toc="коротше"><span class="num" data-n>Діагноз</span>…  — «03 / Діагноз»
       (data-no-toc — нумерується, але у зміст не йде)
       (слово «Розділ» дає «Розділ 3», з data-n="pad" — «Розділ 03»; data-toc — назва для змісту, якщо інша)
     <p class="fig-head" data-kind="Схема">…         — «Схема 4 · …»
     <main data-figs="kind">                         — фігури рахуються окремо за видами
     <span data-ref="s3">3</span>                    — число підставляється з цілі
     <div data-course-foot></div>                    — «Далі в темі», пейджер, підвал
*/
(function () {
  'use strict';
  var C = window.COURSE || null;
  var parts = location.pathname.split('/');
  var slug = decodeURIComponent(parts[parts.length - 2] || '');
  var flat = [], cur = -1;
  if (C) C.blocks.forEach(function (b) {
    b.topics.forEach(function (t) {
      flat.push({slug: t.slug, num: t.num, title: t.title, block: b});
      if (t.slug === slug) cur = flat.length - 1;
    });
  });
  var T = cur >= 0 ? flat[cur] : null;
  var prev = cur > 0 ? flat[cur - 1] : null;
  var next = cur >= 0 && cur + 1 < flat.length ? flat[cur + 1] : null;

  function q(s) { return document.querySelector(s); }
  function qa(s) { return [].slice.call(document.querySelectorAll(s)); }
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;'); }
  function href(t) { return '../' + t.slug + '/lecture.html'; }
  function titleHTML(h) {         // вміст заголовка без мітки номера — РАЗОМ із розміткою
    var c = h.cloneNode(true), n = c.querySelector('.num');   // (<code>, &nbsp; тощо)
    if (n) n.parentNode.removeChild(n);
    return c.innerHTML.trim();
  }
  function prepend(el, text) {     // ⚠️ у ТОЙ САМИЙ текстовий вузол: браузер формує
    var t = el.firstChild;          // гліфи по вузлах, і окремий вузол зсував кернінг
    if (t && t.nodeType === 3) t.data = text + t.data;
    else el.insertBefore(document.createTextNode(text), t);
  }

  // 1. підпис над заголовком
  var eb = q('header .eyebrow[data-auto]');
  if (eb && T) eb.textContent = C.title + ' · Блок ' + T.block.n + ' · Тема ' + T.num;

  // 2. зміст (до нумерації: йому потрібні лише назви)
  var heads = qa('main h2[id]');
  var toc = q('.toc[data-auto]');
  // data-no-toc — розділ нумерується, але у зміст не йде (підсумок наприкінці)
  if (toc) toc.innerHTML = '\n      <h4>Що всередині</h4>\n      <ol>\n' + heads.filter(function (h) {
    return !h.hasAttribute('data-no-toc');
  }).map(function (h) {
    // data-toc — коротша назва для змісту, якщо автор її дав (HTML)
    return '        <li><a href="#' + h.id + '">' + (h.getAttribute('data-toc') || titleHTML(h)) + '</a></li>';
  }).join('\n') + '\n      </ol>\n    ';

  // 3. номери розділів
  var secN = {};
  heads.forEach(function (h, i) {
    secN[h.id] = i + 1;
    var n = h.querySelector('.num[data-n]');
    if (!n) return;
    // мітка може містити розмітку (<span class="raw">γ</span>) — дописуємо номер, не чіпаючи її
    if (n.textContent.trim() === 'Розділ') n.textContent = 'Розділ ' + (n.getAttribute('data-n') === 'pad' ? pad(i + 1) : i + 1);
    else prepend(n, pad(i + 1) + ' / ');
  });

  // 4. номери фігур: наскрізно або окремо за видами (<main data-figs="kind">)
  var mainEl = q('main'), byKind = mainEl && mainEl.getAttribute('data-figs') === 'kind';
  var figN = {}, per = {};
  qa('main .fig-head[data-kind]').forEach(function (p, i) {
    var kind = p.getAttribute('data-kind');
    var num = byKind ? (per[kind] = (per[kind] || 0) + 1) : i + 1;
    prepend(p, kind + ' ' + num + ' · ');
    var f = p.closest('figure');
    if (f && f.id) figN[f.id] = num;
  });

  // 5. числа в посиланнях на розділи й фігури
  qa('[data-ref]').forEach(function (r) {
    var id = r.getAttribute('data-ref'), n = secN[id] || figN[id];
    // знак після числа лишається; «03» лишається «03» — автор пише так, як у мітці «03 / …»
    if (n) r.textContent = r.textContent.replace(/^\d+/, function (d) { return d.length > 1 && d[0] === '0' ? pad(n) : String(n); });
    else if (window.console) console.warn('course.js: посилання на відсутню ціль', id);
  });

  // 6. смуга переходів під шапкою
  var nav = q('nav.topnav[data-auto]');
  if (nav && T) {
    var h = '';
    if (prev) h += '<a href="' + href(prev) + '">← ' + prev.num + '. ' + esc(prev.title) + '</a>';
    h += '<a href="../index.html">Усі теми</a>';
    if (next) h += '<span class="spacer"></span><a href="' + href(next) + '">' + next.num + '. ' + esc(next.title) + ' →</a>';
    nav.innerHTML = h;
  }

  // 7. «Далі в темі», пейджер і підвал
  var foot = q('[data-course-foot]');
  if (foot) {
    var cards = [
      '<a class="step" href="practice.html"><span class="k">Практика</span><span class="d">Розібрати код разом із результатами просто в браузері.</span><span class="dl">переглянути →</span></a>',
      '<a class="step" href="practice.ipynb" download><span class="k">Зошит</span><span class="d">Завантажити .ipynb, щоб запускати й змінювати код у себе.</span><span class="dl">завантажити ↓</span></a>',
      '<a class="step" href="quiz.html"><span class="k">Тест</span><span class="d">Вісім питань із поясненням до кожної відповіді.</span><span class="dl">пройти →</span></a>',
      '<a class="step" href="homework.html"><span class="k">Домашнє завдання</span><span class="d">Три рівні: повторити, застосувати, зробити з нуля.</span><span class="dl">відкрити →</span></a>'];
    var pg = [];
    if (prev) pg.push('<a href="' + href(prev) + '"><span class="dir">попередня</span><span class="ttl">' + prev.num + '. ' + esc(prev.title) + '</span></a>');
    if (next) pg.push('<a class="next" href="' + href(next) + '"><span class="dir">наступна</span><span class="ttl">' + next.num + '. ' + esc(next.title) + '</span></a>');
    foot.outerHTML = '<div class="nextsteps">\n  <h3>Далі в темі</h3>\n  <p class="lead-sub">Теорію прочитано. Тепер закріпи її на практиці.</p>\n  <div class="steps">\n    ' +
      cards.join('\n    ') + '\n  </div>\n  <div class="pager">\n    ' + pg.join('\n    ') + '\n  </div>\n</div>\n\n<footer>\n  <p><a href="../index.html">Усі теми курсу</a> · <a href="../glossary.html">Глосарій</a> · <a href="../sources.html">Джерела</a></p>\n</footer>';
  }
})();
