<h1>Підсумок<a href="#summary" title="Permalink to this headline"></a></h1>
<ol>
<li><p>Функція — це самодостатній набір інструкцій, призначений для виконання певного завдання.</p></li>
<li><p>Функція має власний блок пам'яті для своїх змінних. Інформація може бути додана до блоку пам'яті функції лише через її вхідні змінні. Інформація може покинути блок пам'яті функції лише через її вихідні змінні.</p></li>
<li><p>Функцію можна визначити всередині іншої функції, що називається вкладеною функцією. Доступ до цієї вкладеної функції може мати лише батьківська функція.</p></li>
<li><p>Ви можете визначити анонімну функцію за допомогою ключового слова lambda, так звану лямбда-функцію.</p></li>
<li><p>Ви можете присвоювати функції змінним за допомогою дескрипторів функцій.</p></li>
</ol>


<h1>Задачі<a href="#problems" title="Permalink to this headline"></a></h1>
<ol>
<li><p>Нагадаємо, що гіперболічний синус, що позначається як <span>\(\sinh\)</span>, дорівнює <span>\(\frac{\exp{(x)} - \exp{(-x)}}{2}\)</span>. Напишіть функцію <span>\(my\_sinh(x)\)</span>, де вихідне значення <span>\(y\)</span> є гіперболічним синусом, обчисленим для <span>\(x\)</span>. Припустімо, що <em>x</em> є числом з плаваючою комою розміром 1 на 1.</p></li>
</ol>
<p>Тестові випадки:</p>
<pre><span></span><span>Вхід</span><span>:</span> <span>my_sinh</span><span>(</span><span>0</span><span>)</span>
<span>Вихід</span><span>:</span> <span>0</span>
   
<span>Вхід</span><span>:</span> <span>my_sinh</span><span>(</span><span>1</span><span>)</span>
<span>Вихід</span><span>:</span> <span>1.1752</span>
   
<span>Вхід</span><span>:</span> <span>my_sinh</span><span>(</span><span>2</span><span>)</span>
<span>Вихід</span><span>:</span> <span>3.6269</span>
</pre>

<ol>
<li><p>Напишіть функцію <span>\(my\_checker\_board(n)\)</span>, де вихідне значення <span>\(m\)</span> є масивом розміром <span>\(n\times n\)</span> наступного вигляду:</p>

\[\begin{split}
    m =\begin{array}{ccccc}
    1 &amp; 0 &amp; 1 &amp; 0 &amp; 1\\
    0 &amp; 1 &amp; 0 &amp; 1 &amp; 0\\
    1 &amp; 0 &amp; 1 &amp; 0 &amp; 1\\
    0 &amp; 1 &amp; 0 &amp; 1 &amp; 0\\
    1 &amp; 0 &amp; 1 &amp; 0 &amp; 1
    \end{array}
    \end{split}\]
</li>
</ol>
<p>Зауважте, що верхній лівий елемент завжди повинен бути 1. Припустімо, що <em>n</em> є строго додатним цілим числом.</p>
<p>Тестові випадки:</p>
<pre><span></span><span>Вхід</span><span>:</span> <span>my_checker_board</span><span>(</span><span>1</span><span>)</span>
<span>Вихід</span><span>:</span> <span>1</span>
   
<span>Вхід</span><span>:</span> <span>my_checker_board</span><span>(</span><span>2</span><span>)</span>
<span>Вихід</span><span>:</span> <span>array</span><span>([[</span><span>1</span><span>,</span> <span>0</span><span>],</span>
            <span>[</span><span>0</span><span>,</span> <span>1</span><span>]])</span>
   
<span>Вхід</span><span>:</span> <span>y</span> <span>=</span> <span>my_sinh</span><span>(</span><span>3</span><span>)</span>
<span>Вихід</span><span>:</span> <span>array</span><span>([[</span><span>1</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>],</span>
            <span>[</span><span>0</span><span>,</span> <span>1</span><span>,</span> <span>0</span><span>],</span> 
            <span>[</span><span>1</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>]])</span>
   
<span>Вхід</span><span>:</span> <span>y</span> <span>=</span> <span>my_sinh</span><span>(</span><span>5</span><span>)</span>
<span>Вихід</span><span>:</span> <span>array</span><span>([[</span><span>1</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>],</span>
            <span>[</span><span>0</span><span>,</span> <span>1</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>,</span> <span>0</span><span>],</span> 
            <span>[</span><span>1</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>],</span> 
            <span>[</span><span>0</span><span>,</span> <span>1</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>,</span> <span>0</span><span>],</span> 
            <span>[</span><span>1</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>]])</span>
</pre>

<ol>
<li><p>Напишіть функцію <span>\(my\_triangle(b,h)\)</span>, де вихідним значенням є площа трикутника з основою, <em>b</em>, та висотою, <em>h</em>. Нагадаємо, що площа трикутника дорівнює половині добутку основи на висоту. Припустімо, що <em>b</em> та <em>h</em> є числами з плаваючою комою розміром 1 на 1.</p></li>
</ol>
<p>Тестові випадки:</p>
<pre><span></span><span>Вхід</span><span>:</span> <span>my_triangle</span><span>(</span><span>1</span><span>,</span> <span>1</span><span>)</span>
<span>Вихід</span><span>:</span> <span>0.5</span>

<span>Вхід</span><span>:</span> <span>my_triangle</span><span>(</span><span>2</span><span>,</span> <span>1</span><span>)</span>
<span>Вихід</span><span>:</span> <span>1</span>
   
<span>Вхід</span><span>:</span> <span>my_triangle</span><span>(</span><span>12</span><span>,</span> <span>5</span><span>)</span>
<span>Вихід</span><span>:</span> <span>30</span>
</pre>

<ol>
<li><p>Напишіть функцію <span>\(my\_split\_matrix(m)\)</span>, де <span>\(m\)</span> — це масив, а вихідним значенням є список <em>[m1, m2]</em>, де <em>m1</em> — ліва половина <em>m</em>, а <em>m2</em> — права половина <em>m</em>. У випадку, коли кількість стовпців непарна, середній стовпець повинен належати <em>m1</em>. Припустімо, що <em>m</em> має щонайменше два стовпці.</p></li>
</ol>
<p>Тестові випадки:</p>
<pre><span></span> <span>Вхід</span><span>:</span> <span>m</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>],</span> <span>[</span><span>4</span><span>,</span> <span>5</span><span>,</span> <span>6</span><span>],</span> <span>[</span><span>7</span><span>,</span> <span>8</span><span>,</span> <span>9</span><span>]])</span>
 <span>Вхід</span><span>:</span> <span>m1</span><span>,</span> <span>m2</span> <span>=</span> <span>my_split_matrix</span><span>(</span><span>m</span><span>)</span>  
 <span>Вихід</span><span>:</span> <span>m1</span> <span>=</span> <span>array</span><span>([[</span><span>1</span><span>,</span> <span>2</span><span>],</span>
                   <span>[</span><span>4</span><span>,</span> <span>5</span><span>],</span>
                   <span>[</span><span>7</span><span>,</span> <span>8</span><span>]])</span>  
 <span>Вихід</span><span>:</span> <span>m2</span> <span>=</span> <span>array</span><span>([</span><span>3</span><span>,</span> <span>6</span><span>,</span> <span>9</span><span>])</span>
   
  
 <span>Вхід</span><span>:</span> <span>m</span> <span>=</span> <span>np</span><span>.</span><span>ones</span><span>((</span><span>5</span><span>,</span> <span>5</span><span>))</span>
 <span>Вхід</span><span>:</span> <span>m1</span><span>,</span> <span>m2</span> <span>=</span> <span>my_split_matrix</span><span>(</span><span>m</span><span>)</span> 
 <span>Вихід</span><span>:</span> <span>m1</span> <span>=</span> <span>array</span><span>([[</span><span>1.</span><span>,</span> <span>1.</span><span>,</span> <span>1.</span><span>],</span>
       <span>[</span><span>1.</span><span>,</span> <span>1.</span><span>,</span> <span>1.</span><span>],</span>
       <span>[</span><span>1.</span><span>,</span> <span>1.</span><span>,</span> <span>1.</span><span>],</span>
       <span>[</span><span>1.</span><span>,</span> <span>1.</span><span>,</span> <span>1.</span><span>],</span>
       <span>[</span><span>1.</span><span>,</span> <span>1.</span><span>,</span> <span>1.</span><span>]])</span>
 <span>Вихід</span><span>:</span> <span>m2</span> <span>=</span>  <span>array</span><span>([[</span><span>1.</span><span>,</span> <span>1.</span><span>],</span>
       <span>[</span><span>1.</span><span>,</span> <span>1.</span><span>],</span>
       <span>[</span><span>1.</span><span>,</span> <span>1.</span><span>],</span>
       <span>[</span><span>1.</span><span>,</span> <span>1.</span><span>],</span>
       <span>[</span><span>1.</span><span>,</span> <span>1.</span><span>]])</span>
   
</pre>

<ol>
<li><p>Напишіть функцію <span>\(my\_cylinder(r,h)\)</span>, де <em>r</em> та <em>h</em> — це радіус та висота циліндра відповідно, а вихідним значенням є список <em>[s, v]</em>, де <em>s</em> та <em>v</em> — це площа поверхні та об'єм того ж циліндра відповідно. Нагадаємо, що площа поверхні циліндра дорівнює <span>\(2\pi r^2 + 2\pi rh\)</span>, а об'єм — <span>\(\pi r^2h\)</span>. Припустімо, що <em>r</em> та <em>h</em> є числами з плаваючою комою розміром 1 на 1.</p></li>
</ol>
<p>Тестові випадки:</p>
<pre><span></span><span>Вхід</span><span>:</span> <span>my_cylinder</span><span>(</span><span>1</span><span>,</span><span>5</span><span>)</span>
<span>Вихід</span><span>:</span> <span>[</span><span>37.6991</span><span>,</span> <span>15.7080</span><span>]</span>

<span>Вхід</span><span>:</span> <span>my_cylinder</span><span>(</span><span>2</span><span>,</span><span>4</span><span>)</span>
<span>Вихід</span><span>:</span> <span>[</span><span>62.8319</span><span>,</span> <span>37.6991</span><span>]</span>
</pre>

<ol>
<li><p>Напишіть функцію <span>\(my\_n\_odds(a)\)</span>, де <em>a</em> — це одновимірний масив чисел з плаваючою комою, а вихідним значенням є кількість непарних чисел у <em>a</em>.</p></li>
</ol>
<p>Тестові випадки:</p>
<pre><span></span><span>Вхід</span><span>:</span> <span>my_n_odds</span><span>(</span><span>np</span><span>.</span><span>arange</span><span>(</span><span>100</span><span>))</span>
<span>Вихід</span><span>:</span> <span>50</span>

<span>Вхід</span><span>:</span> <span>my_n_odds</span><span>(</span><span>np</span><span>.</span><span>arange</span><span>(</span><span>2</span><span>,</span> <span>100</span><span>,</span> <span>2</span><span>))</span>
<span>Вихід</span><span>:</span> <span>0</span>
</pre>

<ol>
<li><p>Напишіть функцію <span>\(my\_twos(m,n)\)</span>, де вихідним значенням є масив двійок розміром <span>\(m\times n\)</span>. Припустімо, що <em>m</em> та <em>n</em> є строго додатними цілими числами.</p></li>
</ol>
<p>Тестові випадки:</p>
<pre><span></span><span>Вхід</span><span>:</span> <span>my_twos</span><span>(</span><span>3</span><span>,</span> <span>2</span><span>)</span>
<span>Вихід</span><span>:</span> <span>array</span><span>([[</span><span>2</span><span>,</span> <span>2</span><span>],</span>
      <span>[</span><span>2</span><span>,</span> <span>2</span><span>],</span>
      <span>[</span><span>2</span><span>,</span> <span>2</span><span>]])</span>

<span>Вхід</span><span>:</span> <span>my_twos</span><span>(</span><span>1</span><span>,</span> <span>4</span><span>)</span>
<span>Вихід</span><span>:</span> <span>array</span><span>([</span><span>2</span><span>,</span> <span>2</span><span>,</span> <span>2</span><span>,</span> <span>2</span><span>])</span>
</pre>

<ol>
<li><p>Напишіть лямбда-функцію, яка приймає <em>x</em> та <em>y</em> і повертає значення <em>x - y</em>.</p></li>
<li><p>Напишіть функцію <span>\(add\_string(s1, s2)\)</span>, де вихідним значенням є конкатенація (об'єднання) рядків <em>s1</em> та <em>s2</em>.</p></li>
</ol>
<p>Тестові випадки:</p>
<pre><span></span><span>Вхід</span><span>:</span> <span>s1</span> <span>=</span> <span>add_string</span><span>(</span><span>'Programming'</span><span>,</span> <span>' '</span><span>)</span>
<span>Вхід</span><span>:</span> <span>s2</span> <span>=</span> <span>add_string</span><span>(</span><span>'is'</span><span>,</span> <span>'fun!'</span><span>)</span>
<span>Вхід</span><span>:</span> <span>add_string</span><span>(</span><span>s1</span><span>,</span> <span>s2</span><span>)</span>
<span>Вихід</span><span>:</span> <span>'Programming is fun!'</span>
</pre>

<ol>
<li><p>Згенеруйте наступні помилки:</p>
<ul>
<li><p>TypeError: fun() відсутній 1 обов'язковий позиційний аргумент: ‘a`</p></li>
<li><p>IndentationError: очікувався блок з відступом</p></li>
</ul>
</li>
<li><p>Напишіть функцію <span>\(greeting(name, age)\)</span>, де <em>name</em> — це рядок, <em>age</em> — число з плаваючою комою, а вихідним значенням є рядок ‘Привіт, мене звати XXX і мені XXX років.`, де XXX — це вхідні ім'я та вік відповідно.</p></li>
</ol>
<p>Тестові випадки:</p>
<pre><span></span><span>Вхід</span><span>:</span> <span>greeting</span><span>(</span><span>'John'</span><span>,</span> <span>26</span><span>)</span>
<span>Вихід</span><span>:</span> <span>'Привіт, мене звати John і мені 26 років.'</span>

<span>Вхід</span><span>:</span> <span>greeting</span><span>(</span><span>'Kate'</span><span>,</span> <span>19</span><span>)</span>
<span>Вихід</span><span>:</span> <span>'Привіт, мене звати Kate і мені 19 років.'</span>
</pre>

<ol>
<li><p>Нехай <em>r1</em> та <em>r2</em> — це радіуси кіл з однаковим центром, і нехай <em>r2&gt;r1</em>. Напишіть функцію <em>my_donut_area(r1, r2)</em>, де вихідним значенням є площа поза колом з радіусом <em>r1</em> та всередині кола з радіусом <em>r2</em>. Переконайтеся, що функція є векторизованою. Припустімо, що <em>r1</em> та <em>r2</em> є одновимірними масивами однакового розміру.</p></li>
</ol>
<p>Тестові випадки:</p>
<pre><span></span><span>Вхід</span><span>:</span> <span>my_donut_area</span><span>(</span><span>np</span><span>.</span><span>arange</span><span>(</span><span>1</span><span>,</span> <span>4</span><span>),</span> <span>np</span><span>.</span><span>arange</span><span>(</span><span>2</span><span>,</span> <span>7</span><span>,</span> <span>2</span><span>))</span>
<span>Вихід</span><span>:</span> <span>array</span><span>([</span><span>9.4248</span><span>,</span> <span>37.6991</span><span>,</span> <span>84.8230</span><span>])</span>
</pre>

<ol>
<li><p>Напишіть функцію <span>\(my\_within\_tolerance(A, a, tol)\)</span>, де вихідним значенням є масив або список індексів у <em>A</em> таких, що <span>\(|A-a| &lt; \text{tol}\)</span>. Припустімо, що <em>A</em> — це одновимірний список або масив чисел з плаваючою комою, а <em>a</em> та <em>tol</em> — числа з плаваючою комою розміром 1 на 1.</p></li>
</ol>
<p>Тестові випадки:</p>
<pre><span></span><span>Вхід</span><span>:</span> <span>my_within_tolerance</span><span>([</span><span>0</span><span>,</span> <span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>],</span> <span>1.5</span><span>,</span> <span>0.75</span><span>)</span>
<span>Вихід</span><span>:</span> <span>[</span><span>1</span><span>,</span> <span>2</span><span>]</span>
   
<span>Вхід</span><span>:</span> <span>my_within_tolerance</span><span>(</span><span>np</span><span>.</span><span>arange</span><span>(</span><span>0</span><span>,</span> <span>1.01</span><span>,</span> <span>0.01</span><span>),</span> <span>0.5</span><span>,</span> <span>0.03</span><span>)</span>
<span>Вихід</span><span>:</span> <span>[</span><span>47</span><span>,</span> <span>48</span><span>,</span> <span>49</span><span>,</span> <span>50</span><span>,</span> <span>51</span><span>,</span> <span>52</span><span>]</span>
</pre>

<ol>
<li><p>Напишіть функцію <span>\(bounding\_array(A, top, bottom)\)</span>, де вихідне значення дорівнює масиву <em>A</em> там, де <em>bottom &lt; A &lt; top</em>, дорівнює <em>bottom</em> там, де <em>A &lt;= bottom</em>, і дорівнює <em>top</em> там, де <em>A &gt;= top</em>. Припустімо, що <em>A</em> — це одновимірний масив чисел з плаваючою комою, а <em>top</em> та <em>bottom</em> — числа з плаваючою комою розміром 1 на 1.</p></li>
</ol>
<p>Тестові випадки:</p>
<pre><span></span><span>Вхід</span><span>:</span> <span>bounding_array</span><span>(</span><span>np</span><span>.</span><span>arange</span><span>(</span><span>-</span><span>5</span><span>,</span> <span>6</span><span>,</span> <span>1</span><span>),</span> <span>3</span><span>,</span> <span>-</span><span>3</span><span>)</span>
<span>Вихід</span><span>:</span> <span>[</span><span>-</span><span>3</span><span>,</span> <span>-</span><span>3</span><span>,</span> <span>-</span><span>3</span><span>,</span> <span>-</span><span>2</span><span>,</span> <span>-</span><span>1</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>,</span> <span>3</span><span>,</span> <span>3</span><span>]</span>
</pre>
