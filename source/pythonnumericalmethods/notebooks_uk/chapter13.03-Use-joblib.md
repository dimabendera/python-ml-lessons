<h1>Використання joblib<a href="#use-joblib" title="Постійне посилання на цей заголовок"></a></h1>
<p>У Python існують також інші сторонні пакети, які можуть полегшити паралельні обчислення, особливо для деяких повсякденних завдань. <a href="https://joblib.readthedocs.io/en/latest/index.html">joblib</a> є одним з них, він надає простий спосіб для виконання паралельних обчислень (він також має багато інших застосувань).</p>
<p>Спочатку вам потрібно встановити його, виконавши команду</p>
<pre><span></span><span>pip</span> <span>install</span> <span>joblib</span>
</pre>

<p>Давайте подивимося, як ми можемо запустити попередній приклад, використовуючи цей новий пакет.</p>


<pre><span></span><span>from</span> <span>joblib</span> <span>import</span> <span>Parallel</span><span>,</span> <span>delayed</span>
<span>import</span> <span>numpy</span> <span>as</span> <span>np</span>

<span>def</span> <span>random_square</span><span>(</span><span>seed</span><span>):</span>
    <span>np</span><span>.</span><span>random</span><span>.</span><span>seed</span><span>(</span><span>seed</span><span>)</span>
    <span>random_num</span> <span>=</span> <span>np</span><span>.</span><span>random</span><span>.</span><span>randint</span><span>(</span><span>0</span><span>,</span> <span>10</span><span>)</span>
    <span>return</span> <span>random_num</span><span>**</span><span>2</span>
</pre>





<pre><span></span><span>results</span> <span>=</span> <span>Parallel</span><span>(</span><span>n_jobs</span><span>=</span><span>8</span><span>)</span>\
    <span>(</span><span>delayed</span><span>(</span><span>random_square</span><span>)(</span><span>i</span><span>)</span> <span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>1000000</span><span>))</span>
</pre>



<p>Ми бачимо, що паралельна частина коду стає одним рядком завдяки використанню бібліотеки joblib, що дуже зручно. <em>Parallel</em> — це допоміжний клас, який по суті надає зручний інтерфейс для модуля <em>multiprocessing</em>, який ми розглядали раніше. <em>delayed</em> використовується для захоплення аргументів цільової функції, в даному випадку <em>random_square</em>. Ми запускаємо наведений вище код з 8 процесорами. Якщо ви хочете використати всю обчислювальну потужність вашої машини, ви можете використати всі процесори, встановивши <em>n_jobs=-1</em>. Якщо встановити значення -2, будуть використані всі процесори, крім одного.</p>
<p>Крім того, ви можете увімкнути аргумент <em>verbose</em> для виведення повідомлень про стан.</p>


<pre><span></span><span>results</span> <span>=</span> <span>Parallel</span><span>(</span><span>n_jobs</span><span>=-</span><span>1</span><span>,</span> <span>verbose</span><span>=</span><span>1</span><span>)</span>\
    <span>(</span><span>delayed</span><span>(</span><span>random_square</span><span>)(</span><span>i</span><span>)</span> <span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>1000000</span><span>))</span>
</pre>



<pre><span></span>[Parallel(n_jobs=-1)]: Using backend LokyBackend with 12 concurrent workers.
[Parallel(n_jobs=-1)]: Done  60 tasks      | elapsed:    0.1s
[Parallel(n_jobs=-1)]: Done 176056 tasks      | elapsed:    3.0s
[Parallel(n_jobs=-1)]: Done 787056 tasks      | elapsed:   12.4s
[Parallel(n_jobs=-1)]: Done 1000000 out of 1000000 | elapsed:   15.5s finished
</pre>



<p>У joblib є кілька бекендів, що означає використання різних способів для виконання паралельних обчислень. Якщо ви встановите бекенд як <em>multiprocessing</em>, то під капотом фактично створюється пул багатопроцесорності, який використовує окремі робочі процеси Python для одночасного виконання завдань на окремих процесорах.</p>


<pre><span></span><span>results</span> <span>=</span> \
    <span>Parallel</span><span>(</span><span>n_jobs</span><span>=-</span><span>1</span><span>,</span> <span>backend</span><span>=</span><span>'multiprocessing'</span><span>,</span> <span>verbose</span><span>=</span><span>1</span><span>)</span>\
    <span>(</span><span>delayed</span><span>(</span><span>random_square</span><span>)(</span><span>i</span><span>)</span> <span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>1000000</span><span>))</span>
</pre>



<pre><span></span>[Parallel(n_jobs=-1)]: Using backend MultiprocessingBackend with 12 concurrent workers.
[Parallel(n_jobs=-1)]: Done 220 tasks      | elapsed:    0.0s
[Parallel(n_jobs=-1)]: Done 457032 tasks      | elapsed:    1.9s
[Parallel(n_jobs=-1)]: Done 1000000 out of 1000000 | elapsed:    3.8s finished
</pre>
