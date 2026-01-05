<h1>Підсумок<a href="#summary" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Паралельні обчислення можуть скоротити час виконання за рахунок використання кількох ядер у нашому комп'ютері.</p></li>
<li><p>Існує різниця між процесом і потоком, і в Python легше використовувати підхід на основі процесів для досягнення паралелізму.</p></li>
<li><p>Пакет Multiprocessing простий у використанні для вирішення ваших завдань на кількох ядрах.</p></li>
<li><p>Ми також можемо використовувати joblib для спрощення нашого коду паралельних обчислень для багатьох поширених завдань.</p></li>
</ol>


<h1>Завдання<a href="#problems" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Що таке паралельні обчислення?</p></li>
<li><p>Будь ласка, вкажіть різницю між процесом і потоком.</p></li>
<li><p>Знайдіть кількість процесорів на вашому комп'ютері за допомогою пакета multiprocessing.</p></li>
<li><p>Використайте пакет multiprocessing для паралелізації наступного коду та запишіть час виконання. Підказка: Можливо, вам знадобиться перевірити функцію <code><span>pool.apply</span></code>.</p></li>
</ol>
<pre><span></span><span>def</span> <span>plus_cube</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>):</span>
    <span>return</span> <span>(</span><span>x</span><span>+</span><span>y</span><span>)</span><span>**</span><span>3</span>

<span>for</span> <span>x</span><span>,</span> <span>y</span> <span>in</span> <span>zip</span><span>(</span><span>range</span><span>(</span><span>100</span><span>),</span> <span>range</span><span>(</span><span>100</span><span>)):</span>
    <span>results</span><span>.</span><span>append</span><span>(</span><span>plus_cube</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>))</span>
</pre>

<ol>
<li><p>Чи можете ви навести приклад, щоб проілюструвати різницю між <code><span>pool.map</span></code> та <code><span>pool.map_async</span></code>?</p></li>
<li><p>Що таке GIL у Python?</p></li>
<li><p>Використайте joblib для паралелізації наведеного вище прикладу та використовуйте multiprocessing як бекенд.</p></li>
</ol>
