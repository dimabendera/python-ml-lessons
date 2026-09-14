/* Сторінка-зміст курсу з маніфесту.

   Розмітка, яку він розуміє:
     <b data-course-done></b>              — скільки тем готово (рахується, не пишеться руками)
     <b data-course-total></b>             — скільки тем усього
     <div data-course-blocks></div>        — блоки й теми: <section class="blk"> … <ul class="topics">

   Тема вважається готовою, якщо в маніфесті немає "soon": true. Готова — посилання
   (<li class="on">), не готова — сірий рядок (<li class="off">) з поміткою «скоро».

   ⚠️ Порядок і назви — лише з manifest.js. Руками список тем більше не пишеться:
   саме через ручний список індекс NLP пів курсу показував «30 готово», коли тем
   було вже 40.
*/
(function () {
  'use strict';
  var C = window.COURSE;
  if (!C) return;                       // без маніфесту лишається те, що у файлі

  function esc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;');
  }
  function qa(s) { return [].slice.call(document.querySelectorAll(s)); }

  var total = 0, done = 0;
  C.blocks.forEach(function (b) {
    b.topics.forEach(function (t) { total++; if (!t.soon) done++; });
  });

  qa('[data-course-total]').forEach(function (e) { e.textContent = total; });
  qa('[data-course-done]').forEach(function (e) { e.textContent = done; });

  var host = document.querySelector('[data-course-blocks]');
  if (!host) return;
  host.innerHTML = C.blocks.map(function (b) {
    var items = b.topics.map(function (t) {
      var num = '<span class="n">' + esc(t.num) + '</span>';
      return t.soon
        ? '<li class="off">' + num + esc(t.title) + '<span class="soon">скоро</span></li>'
        : '<li class="on"><a href="' + esc(t.slug) + '/lecture.html">' + num + esc(t.title) + '</a></li>';
    }).join('');
    return '<section class="blk"><h3><span class="bn">Блок ' + b.n + '</span>' +
           esc(b.title) + '</h3><ul class="topics">' + items + '</ul></section>';
  }).join('\n');
})();
