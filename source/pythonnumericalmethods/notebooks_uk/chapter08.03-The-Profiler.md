```html
<h1>Профайлер<a href="#the-profiler" title="Permalink to this headline"></a></h1>

<h2>Використання магічної команди<a href="#using-the-magic-command" title="Permalink to this headline"></a></h2>
<p>Навіть якщо це не змінює складність програми за нотацією Big-O, багато програмістів витрачають довгі години, щоб змусити свій код працювати вдвічі швидше або досягти навіть менших покращень.</p>
<p>Існують способи перевірити час виконання коду в Jupyter notebook, тут ми представимо магічні команди для цього:</p>
<ul>
<li></li>
<li></li>
<li></li>
<li></li>
</ul>
<p>Зверніть увагу, що магічна команда з подвійним відсотком вимірює час виконання всього коду в комірці, тоді як команда з одним відсотком працює лише для одного виразу.</p>


<pre><span></span><span>%</span><span>time</span> sum(range(200))
</pre>



<pre><span></span>CPU times: user 6 µs, sys: 1 µs, total: 7 µs
Wall time: 9.06 µs
</pre>

<pre><span></span>19900
</pre>





<pre><span></span><span>%</span><span>timeit</span> sum(range(200))
</pre>



<pre><span></span>1.24 µs ± 70.6 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
</pre>





<pre><span></span><span>%%time</span>
<span>s</span> <span>=</span> <span>0</span>
<span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>200</span><span>):</span>
    <span>s</span> <span>+=</span> <span>i</span>
</pre>



<pre><span></span>CPU times: user 15 µs, sys: 0 ns, total: 15 µs
Wall time: 17.9 µs
</pre>





<pre><span></span><span>%%time</span>it
<span>s</span> <span>=</span> <span>0</span>
<span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>200</span><span>):</span>
    <span>s</span> <span>+=</span> <span>i</span>
</pre>



<pre><span></span>7.06 µs ± 414 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
</pre>



<p><strong>УВАГА!</strong> Іноді може бути недоцільно використовувати <em>timeit</em>, оскільки він виконує код у багатьох циклах. Якщо у вас є код, який виконується довго, вимірювання його часу з багатьма циклами займе дуже багато часу.</p>


<h2>Використання профайлера Python<a href="#use-python-profiler" title="Permalink to this headline"></a></h2>
<p>Ви також можете використовувати профайлер Python (детальніше можна прочитати в документації Python) для профілювання написаного вами коду. У Jupyter notebook для цього є такі магічні команди:</p>
<ul>
<li></li>
<li></li>
</ul>
<p>Розглянемо наступний приклад, який знову і знову підсумовує випадкові числа.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
</pre>





<pre><span></span><span>def</span> <span>slow_sum</span><span>(</span><span>n</span><span>,</span> <span>m</span><span>):</span>

    <span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>n</span><span>):</span>
        <span># ми створюємо масив випадкових чисел розміром m</span>
        <span>a</span> <span>=</span> <span>np</span><span>.</span><span>random</span><span>.</span><span>rand</span><span>(</span><span>m</span><span>)</span>

        <span>s</span> <span>=</span> <span>0</span>
        <span># у цьому циклі ми проходимо по масиву</span>
        <span># і додаємо елементи до суми один за одним</span>
        <span>for</span> <span>j</span> <span>in</span> <span>range</span><span>(</span><span>m</span><span>):</span>
            <span>s</span> <span>+=</span> <span>a</span><span>[</span><span>j</span><span>]</span>   
</pre>





<pre><span></span><span>%</span><span>prun</span> slow_sum(1000, 10000)
</pre>



<pre><span></span>
</pre>



<p>Ви повинні побачити щось на зразок наступної таблиці:</p>
<pre><span></span>         <span>1004</span> <span>function</span> <span>calls</span> <span>in</span> <span>1.413</span> <span>seconds</span>

   <span>Ordered</span> <span>by</span><span>:</span> <span>internal</span> <span>time</span>

   <span>ncalls</span>  <span>tottime</span>  <span>percall</span>  <span>cumtime</span>  <span>percall</span> <span>filename</span><span>:</span><span>lineno</span><span>(</span><span>function</span><span>)</span>
        <span>1</span>    <span>1.320</span>    <span>1.320</span>    <span>1.413</span>    <span>1.413</span> <span>&lt;</span><span>ipython</span><span>-</span><span>input</span><span>-</span><span>20</span><span>-</span><span>cc5de53096ac</span><span>&gt;</span><span>:</span><span>1</span><span>(</span><span>slow_sum</span><span>)</span>
     <span>1000</span>    <span>0.093</span>    <span>0.000</span>    <span>0.093</span>    <span>0.000</span> <span>{</span><span>method</span> <span>'rand'</span> <span>of</span> <span>'mtrand.RandomState'</span> <span>objects</span><span>}</span>
        <span>1</span>    <span>0.000</span>    <span>0.000</span>    <span>1.413</span>    <span>1.413</span> <span>{</span><span>built</span><span>-</span><span>in</span> <span>method</span> <span>builtins</span><span>.</span><span>exec</span><span>}</span>
        <span>1</span>    <span>0.000</span>    <span>0.000</span>    <span>1.413</span>    <span>1.413</span> <span>&lt;</span><span>string</span><span>&gt;</span><span>:</span><span>1</span><span>(</span><span>&lt;</span><span>module</span><span>&gt;</span><span>)</span>
        <span>1</span>    <span>0.000</span>    <span>0.000</span>    <span>0.000</span>    <span>0.000</span> <span>{</span><span>method</span> <span>'disable'</span> <span>of</span> <span>'_lsprof.Profiler'</span> <span>objects</span><span>}</span>
</pre>

<p>Таблиця показує наступні стовпці (з профайлера Python)</p>
<blockquote>
<p><strong>ncalls</strong>: кількість викликів,<br/>
<strong>tottime</strong>: загальний час, витрачений у даній функції (за винятком часу, витраченого на виклики підфункцій),<br/>
<strong>percall</strong>: частка від ділення tottime на ncalls<br/>
<strong>cumtime</strong>: загальний час, витрачений у цій та всіх підфункціях (від виклику до виходу). Цей показник є точним навіть для рекурсивних функцій.<br/>
<strong>percall</strong>: частка від ділення cumtime на кількість примітивних викликів</p>
</blockquote>


<h2>Використання Line Profiler<a href="#use-line-profiler" title="Permalink to this headline"></a></h2>
<p>Часто ми хочемо зрозуміти, який рядок у нашому коді займає багато часу, щоб ми могли переписати його для підвищення ефективності. Це можна зробити за допомогою <em>line_profiler</em>, який може профілювати код рядок за рядком. Але він не постачається разом з Python, тому спочатку його потрібно встановити. Потім ми можемо використовувати магічну команду:</p>
<ul>
<li></li>
</ul>


<pre><span></span><span># Примітка, це потрібно запустити лише один раз.</span>
<span>!</span>conda install line_profiler
</pre>



<pre><span></span>Solving environment: done

# Усі запитані пакети вже встановлено.
</pre>



<p>Після встановлення цього пакету ми можемо завантажити розширення <em>line_profiler</em>:</p>


<pre><span></span><span>%</span><span>load_ext</span> line_profiler
</pre>



<p>Спосіб використання line_profiler для профілювання коду показаний нижче:</p>


<pre><span></span><span>%</span><span>lprun</span> -f slow_sum slow_sum(1000, 10000)
</pre>



<p>Після виконання наведеної вище команди ми отримаємо результати профілювання по рядках:</p>
<pre><span></span><span>Timer</span> <span>unit</span><span>:</span> <span>1e-06</span> <span>s</span>

<span>Total</span> <span>time</span><span>:</span> <span>6.1411</span> <span>s</span>
<span>File</span><span>:</span> <span>&lt;</span><span>ipython</span><span>-</span><span>input</span><span>-</span><span>20</span><span>-</span><span>cc5de53096ac</span><span>&gt;</span>
<span>Function</span><span>:</span> <span>slow_sum</span> <span>at</span> <span>line</span> <span>1</span>

<span>Line</span> <span>#      Hits         Time  Per Hit   % Time  Line Contents</span>
<span>==============================================================</span>
     <span>1</span>                                           <span>def</span> <span>slow_sum</span><span>(</span><span>n</span><span>,</span> <span>m</span><span>):</span>
     <span>2</span>                                           
     <span>3</span>      <span>1001</span>        <span>301.0</span>      <span>0.3</span>      <span>0.0</span>      <span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>n</span><span>):</span>
     <span>4</span>                                                   <span># ми створюємо масив випадкових чисел розміром m</span>
     <span>5</span>      <span>1000</span>      <span>87876.0</span>     <span>87.9</span>      <span>1.4</span>          <span>a</span> <span>=</span> <span>np</span><span>.</span><span>random</span><span>.</span><span>rand</span><span>(</span><span>m</span><span>)</span>
     <span>6</span>                                           
     <span>7</span>      <span>1000</span>        <span>439.0</span>      <span>0.4</span>      <span>0.0</span>          <span>s</span> <span>=</span> <span>0</span>
     <span>8</span>                                                   <span># у цьому циклі ми проходимо по масиву</span>
     <span>9</span>                                                   <span># і додаємо елементи до суми один за одним</span>
    <span>10</span>  <span>10001000</span>    <span>2463579.0</span>      <span>0.2</span>     <span>40.1</span>          <span>for</span> <span>j</span> <span>in</span> <span>range</span><span>(</span><span>m</span><span>):</span>
    <span>11</span>  <span>10000000</span>    <span>3588901.0</span>      <span>0.4</span>     <span>58.4</span>              <span>s</span> <span>+=</span> <span>a</span><span>[</span><span>j</span><span>]</span>
</pre>

<p>Ми бачимо, що результати містять зведення для кожного рядка функції; чітко видно, що рядки 10 та 11 займають більшу частину загального часу виконання.</p>
<p>Зазвичай, коли код виконується довше, ніж хотілося б, існує <strong>"вузьке місце"</strong>, де витрачається значна частина часу. Тобто, є рядок коду, який виконується набагато довше, ніж інші рядки в програмі. Усунення "вузького місця" в програмі зазвичай призводить до найбільшого покращення продуктивності, навіть якщо є інші частини вашого коду, які легше вдосконалити.</p>
<p><strong>ПОРАДА!</strong> Починайте покращувати продуктивність коду з "вузького місця".</p>
```
