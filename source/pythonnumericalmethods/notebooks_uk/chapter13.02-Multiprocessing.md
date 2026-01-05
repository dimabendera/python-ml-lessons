<h1>Багатопроцесорність<a href="#multiprocessing" title="Permalink to this headline"></a></h1>
<p>Бібліотека multiprocessing є стандартною бібліотекою Python для підтримки паралельних обчислень за допомогою процесів. Вона має багато різних функцій, і якщо ви хочете дізнатися всі деталі, можете переглянути <a href="https://docs.python.org/3/library/multiprocessing.html">офіційну документацію</a>. Тут ми представимо основи, щоб ви могли розпочати роботу з паралельними обчисленнями. Почнімо з імпорту бібліотеки.</p>


<pre><span></span><span>import</span> <span>multiprocessing</span> <span>as</span> <span>mp</span>
</pre>



<p>Спершу виведемо загальну кількість процесорів на моїй машині, які можна використовувати для паралельних обчислень.</p>


<pre><span></span><span>print</span><span>(</span><span>f</span><span>"Number of cpu: </span><span>{</span><span>mp</span><span>.</span><span>cpu_count</span><span>()</span><span>}</span><span>"</span><span>)</span>
</pre>



<pre><span></span>Number of cpu: 12
</pre>



<p>Використаємо приклад, щоб показати, як використовувати кілька ядер на одній машині для скорочення часу виконання.</p>
<p><strong>ПРИКЛАД:</strong> Згенеруйте 10 000 000 випадкових чисел від 0 до 10 і піднесіть їх до квадрату. Збережіть результати у списку.</p>

<h2>Послідовна версія<a href="#serial-version" title="Permalink to this headline"></a></h2>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
<span>import</span> <span>time</span>

<span>def</span> <span>random_square</span><span>(</span><span>seed</span><span>):</span>
    <span>np</span><span>.</span><span>random</span><span>.</span><span>seed</span><span>(</span><span>seed</span><span>)</span>
    <span>random_num</span> <span>=</span> <span>np</span><span>.</span><span>random</span><span>.</span><span>randint</span><span>(</span><span>0</span><span>,</span> <span>10</span><span>)</span>
    <span>return</span> <span>random_num</span><span>**</span><span>2</span>
</pre>



<pre><span></span><span>t0</span> <span>=</span> <span>time</span><span>.</span><span>time</span><span>()</span>
<span>results</span> <span>=</span> <span>[]</span>
<span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>10000000</span><span>):</span> 
    <span>results</span><span>.</span><span>append</span><span>(</span><span>random_square</span><span>(</span><span>i</span><span>))</span>
<span>t1</span> <span>=</span> <span>time</span><span>.</span><span>time</span><span>()</span>
<span>print</span><span>(</span><span>f</span><span>'Execution time </span><span>{</span><span>t1</span> <span>-</span> <span>t0</span><span>}</span><span> s'</span><span>)</span>
</pre>



<pre><span></span>Execution time 32.9464430809021 s
</pre>



<h2>Паралельна версія<a href="#parallel-version" title="Permalink to this headline"></a></h2>
<p>Найпростіший спосіб виконати паралельні обчислення за допомогою multiprocessing — це використовувати клас <strong>Pool</strong>. У цьому класі є 4 поширені методи, які ми можемо часто використовувати: *apply*, *map*, *apply_async* та *map_async*. Перегляньте документацію, щоб дізнатися про відмінності, а ми нижче використаємо лише функцію *map* для паралелізації наведеного вище прикладу. Функція *map(func, iterable)* приймає два аргументи і застосовує функцію *func* до кожного елемента в *iterable*, а потім збирає результати.</p>


<pre><span></span><span>t0</span> <span>=</span> <span>time</span><span>.</span><span>time</span><span>()</span>
<span>n_cpu</span> <span>=</span> <span>mp</span><span>.</span><span>cpu_count</span><span>()</span>

<span>pool</span> <span>=</span> <span>mp</span><span>.</span><span>Pool</span><span>(</span><span>processes</span><span>=</span><span>n_cpu</span><span>)</span>
<span>results</span> <span>=</span> <span>[</span><span>pool</span><span>.</span><span>map</span><span>(</span><span>random_square</span><span>,</span> <span>range</span><span>(</span><span>10000000</span><span>))]</span>
<span>t1</span> <span>=</span> <span>time</span><span>.</span><span>time</span><span>()</span>
<span>print</span><span>(</span><span>f</span><span>'Execution time </span><span>{</span><span>t1</span> <span>-</span> <span>t0</span><span>}</span><span> s'</span><span>)</span>
</pre>



<pre><span></span>Execution time 6.066138744354248 s
</pre>



<p>Ми бачимо, що, використовуючи наведену вище паралельну версію коду, ми скоротили час виконання з ~38 с до ~7 с. Це значний приріст швидкості, особливо якщо ми маємо складні обчислення, паралельні обчислення значно скоротять час.</p>
<p>Функція <code><span>pool.apply</span></code> схожа, за винятком того, що вона може приймати більше аргументів. <code><span>pool.map</span></code> та <code><span>pool.apply</span></code> блокуватимуть основну програму, доки всі процеси не завершаться, що досить корисно, якщо ми хочемо отримати результати в певному порядку для деяких застосунків. Навпаки, якщо нам не потрібні результати в певному порядку, ми також можемо використовувати <code><span>pool.apply_async</span></code> або <code><span>pool.map_async</span></code>, які надсилатимуть усі процеси одночасно та отримуватимуть результати, щойно вони будуть завершені. Перегляньте онлайн, щоб дізнатися більше.</p>


<h2>Візуалізація часу виконання<a href="#visualize-the-execution-time" title="Permalink to this headline"></a></h2>
<p>Давайте візуалізуємо зміни часу виконання залежно від кількості точок даних, використовуючи як послідовну, так і паралельну версії. І ви побачите, що до певного моменту краще використовувати послідовну версію.</p>


<pre><span></span><span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>
<span>plt</span><span>.</span><span>style</span><span>.</span><span>use</span><span>(</span><span>'seaborn-poster'</span><span>)</span>
<span>%</span><span>matplotlib</span> inline

<span>def</span> <span>serial</span><span>(</span><span>n</span><span>):</span>
    <span>t0</span> <span>=</span> <span>time</span><span>.</span><span>time</span><span>()</span>
    <span>results</span> <span>=</span> <span>[]</span>
    <span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>n</span><span>):</span> 
        <span>results</span><span>.</span><span>append</span><span>(</span><span>random_square</span><span>(</span><span>i</span><span>))</span>
    <span>t1</span> <span>=</span> <span>time</span><span>.</span><span>time</span><span>()</span>
    <span>exec_time</span> <span>=</span> <span>t1</span> <span>-</span> <span>t0</span>
    <span>return</span> <span>exec_time</span>

<span>def</span> <span>parallel</span><span>(</span><span>n</span><span>):</span>
    <span>t0</span> <span>=</span> <span>time</span><span>.</span><span>time</span><span>()</span>
    <span>n_cpu</span> <span>=</span> <span>mp</span><span>.</span><span>cpu_count</span><span>()</span>

    <span>pool</span> <span>=</span> <span>mp</span><span>.</span><span>Pool</span><span>(</span><span>processes</span><span>=</span><span>n_cpu</span><span>)</span>
    <span>results</span> <span>=</span> <span>[</span><span>pool</span><span>.</span><span>map</span><span>(</span><span>random_square</span><span>,</span> <span>range</span><span>(</span><span>n</span><span>))]</span>
    <span>t1</span> <span>=</span> <span>time</span><span>.</span><span>time</span><span>()</span>
    <span>exec_time</span> <span>=</span> <span>t1</span> <span>-</span> <span>t0</span>
    <span>return</span> <span>exec_time</span>
</pre>



<pre><span></span><span>n_run</span> <span>=</span> <span>np</span><span>.</span><span>logspace</span><span>(</span><span>1</span><span>,</span> <span>7</span><span>,</span> <span>num</span> <span>=</span> <span>7</span><span>)</span>

<span>t_serial</span> <span>=</span> <span>[</span><span>serial</span><span>(</span><span>int</span><span>(</span><span>n</span><span>))</span> <span>for</span> <span>n</span> <span>in</span> <span>n_run</span><span>]</span>
<span>t_parallel</span> <span>=</span> <span>[</span><span>parallel</span><span>(</span><span>int</span><span>(</span><span>n</span><span>))</span> <span>for</span> <span>n</span> <span>in</span> <span>n_run</span><span>]</span>
</pre>



<pre><span></span><span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span> <span>6</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>n_run</span><span>,</span> <span>t_serial</span><span>,</span> <span>'-o'</span><span>,</span> <span>label</span> <span>=</span> <span>'serial'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>n_run</span><span>,</span> <span>t_parallel</span><span>,</span> <span>'-o'</span><span>,</span> <span>label</span> <span>=</span> <span>'parallel'</span><span>)</span>
<span>plt</span><span>.</span><span>loglog</span><span>()</span>
<span>plt</span><span>.</span><span>legend</span><span>()</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Execution time (s)'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'Number of random points'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="../_images/chapter13.02-Multiprocessing_16_0.png" src="../_images/chapter13.02-Multiprocessing_16_0.png"/>


<p>З малюнка видно, що коли кількість точок даних невелика (менше 10000), час виконання для послідовної версії швидший через накладні витрати паралельної версії на запуск та підтримку нових процесів. Але після цього ми чітко бачимо, що переможцем є паралельна версія.</p>
