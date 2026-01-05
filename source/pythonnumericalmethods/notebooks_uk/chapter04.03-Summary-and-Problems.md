<h1>Підсумок<a href="#summary" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Оператори розгалуження (if-else) дозволяють функціям виконувати різні дії за різних обставин.</p></li>
<li><p>Тернарні оператори дозволяють створювати однорядкові оператори розгалуження</p></li>
</ol>


<h1>Задачі<a href="#problems" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Напишіть функцію <code><span>my_tip_calc(bill,</span> <span>party)</span></code>, де <code><span>bill</span></code> — це загальна вартість страви, а <code><span>party</span></code> — кількість людей у групі. Чайові повинні розраховуватися як 15% для групи, що складається строго менше ніж з шести осіб, 18% для групи, що складається строго менше ніж з восьми, 20% для групи менше 11, і 25% для групи 11 або більше. Кілька тестових випадків наведено нижче.</p></li>
</ol>


<pre><span></span><span>def</span> <span>my_tip_calc</span><span>(</span><span>bill</span><span>,</span> <span>party</span><span>):</span>
    <span># write your function code here</span>
    
    <span>return</span> <span>tips</span>
</pre>





<pre><span></span><span># t = 16.3935</span>
<span>t</span> <span>=</span> <span>my_tip_calc</span><span>(</span><span>109.29</span><span>,</span><span>3</span><span>)</span> 
<span>print</span><span>(</span><span>t</span><span>)</span>
</pre>





<pre><span></span><span># t = 19.6722</span>
<span>t</span> <span>=</span> <span>my_tip_calc</span><span>(</span><span>109.29</span><span>,</span><span>7</span><span>)</span> 
<span>print</span><span>(</span><span>t</span><span>)</span>
</pre>





<pre><span></span><span># t = 21.8580</span>
<span>t</span> <span>=</span> <span>my_tip_calc</span><span>(</span><span>109.29</span><span>,</span><span>9</span><span>)</span>
<span>print</span><span>(</span><span>t</span><span>)</span>
</pre>





<pre><span></span><span># t = 27.3225</span>
<span>t</span> <span>=</span> <span>my_tip_calc</span><span>(</span><span>109.29</span><span>,</span><span>12</span><span>)</span>
<span>print</span><span>(</span><span>t</span><span>)</span>
</pre>



<ol>
<li><p>Напишіть функцію <code><span>my_mult_operation(a,b,operation)</span></code>. Вхідний аргумент <code><span>operation</span></code> — це рядок, який може бути <code><span>'plus'</span></code>, <code><span>'minus'</span></code>, <code><span>'mult'</span></code>, <code><span>'div'</span></code> або <code><span>'pow'</span></code>, і функція повинна обчислювати: <span>\(a+b\)</span>, <span>\(a-b\)</span>, <span>\(a∗b\)</span>, <span>\(a/b\)</span>, і <span>\(a^b\)</span> для відповідних значень <code><span>operation</span></code>. Кілька тестових випадків наведено нижче.</p></li>
</ol>


<pre><span></span><span>def</span> <span>my_mult_operation</span><span>(</span><span>a</span><span>,</span><span>b</span><span>,</span><span>operation</span><span>):</span>
    <span># write your function code here</span>
    
    <span>return</span> <span>out</span>
</pre>





<pre><span></span><span>x</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([</span><span>1</span><span>,</span><span>2</span><span>,</span><span>3</span><span>,</span><span>4</span><span>])</span>
<span>y</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([</span><span>2</span><span>,</span><span>3</span><span>,</span><span>4</span><span>,</span><span>5</span><span>])</span>
</pre>





<pre><span></span><span># Output: [3,5,7,9]</span>
<span>my_mult_operation</span><span>(</span><span>x</span><span>,</span><span>y</span><span>,</span><span>'plus'</span><span>)</span>
</pre>





<pre><span></span><span># Output: [-1,-1,-1,-1]</span>
<span>my_mult_operation</span><span>(</span><span>x</span><span>,</span><span>y</span><span>,</span><span>'minus'</span><span>)</span>
</pre>





<pre><span></span><span># Output: [2,6,12,20]</span>
<span>my_mult_operation</span><span>(</span><span>x</span><span>,</span><span>y</span><span>,</span><span>'mult'</span><span>)</span>
</pre>





<pre><span></span><span># Output: [0.5,0.66666667,0.75,0.8]</span>
<span>my_mult_operation</span><span>(</span><span>x</span><span>,</span><span>y</span><span>,</span><span>'div'</span><span>)</span>
</pre>





<pre><span></span><span># Output: [1,8,81,1024]</span>
<span>my_mult_operation</span><span>(</span><span>x</span><span>,</span><span>y</span><span>,</span><span>'pow'</span><span>)</span>
</pre>



<ol>
<li><p>Розгляньте трикутник з вершинами в точках <span>\((0,0)\)</span>, <span>\((1,0)\)</span> та <span>\((0,1)\)</span>. Напишіть функцію <em>my_inside_triangle(x,y)</em>, де вихідним значенням є рядок ‘outside` (зовні), якщо точка <span>\((x,y)\)</span> знаходиться за межами трикутника, ‘border` (межа), якщо точка знаходиться точно на межі трикутника, і ‘inside` (всередині), якщо точка знаходиться всередині трикутника.</p></li>
</ol>


<pre><span></span><span>def</span> <span>my_inside_triangle</span><span>(</span><span>x</span><span>,</span><span>y</span><span>):</span>
    <span># write your function code here</span>
    
    <span>return</span> <span>position</span>
</pre>





<pre><span></span><span># Output: 'border'</span>
<span>my_inside_triangle</span><span>(</span><span>.</span><span>5</span><span>,</span><span>.</span><span>5</span><span>)</span>
</pre>





<pre><span></span><span># Output: 'inside'</span>
<span>my_inside_triangle</span><span>(</span><span>.</span><span>25</span><span>,</span><span>.</span><span>25</span><span>)</span>
</pre>





<pre><span></span><span># Output: 'outside'</span>
<span>my_inside_triangle</span><span>(</span><span>5</span><span>,</span><span>5</span><span>)</span>
</pre>



<ol>
<li><p>Напишіть функцію <em>my_make_size10(x)</em>, де <em>x</em> — це масив, а вихідним значенням є перші 10 елементів <em>x</em>, якщо <em>x</em> має більше 10 елементів, і вихідним значенням є масив <em>x</em>, доповнений достатньою кількістю нулів, щоб зробити його довжиною 10, якщо <em>x</em> має менше 10 елементів.</p></li>
</ol>


<pre><span></span><span>def</span> <span>my_make_size10</span><span>(</span><span>x</span><span>):</span>
    <span># write your function code here</span>
    
    <span>return</span> <span>size10</span>
</pre>





<pre><span></span><span># Output: [1,2,0,0,0,0,0,0,0,0]</span>
<span>my_make_size10</span><span>(</span><span>range</span><span>(</span><span>1</span><span>,</span><span>2</span><span>))</span>
</pre>





<pre><span></span><span># Output: [1,2,3,4,5,6,7,8,9,10]</span>
<span>my_make_size10</span><span>(</span><span>range</span><span>(</span><span>1</span><span>,</span><span>15</span><span>))</span>
</pre>





<pre><span></span><span># Output: [3,6,13,4,0,0,0,0,0,0]</span>
<span>my_make_size10</span><span>(</span><span>5</span><span>,</span><span>5</span><span>)</span>
</pre>



<ol>
<li><p>Чи можете ви написати my_make_size10 без використання операторів if (тобто, використовуючи лише логічні та масивові операції)?</p></li>
</ol>
<ol>
<li><p>Напишіть функцію <em>my_letter_grader(percent)</em>, де оцінка є рядком ‘A+` (відмінно), якщо <em>percent</em> більше 97, ‘A` якщо <em>percent</em> більше 93, ‘A-‘ якщо <em>percent</em> більше 90, ‘B+` якщо <em>percent</em> більше 87, ‘B` якщо <em>percent</em> більше 83, ‘B-‘ якщо <em>percent</em> більше 80, ‘C+` якщо <em>percent</em> більше 77, ‘C` якщо <em>percent</em> більше 73, ‘C-‘ якщо <em>percent</em> більше 70, ‘D+` якщо <em>percent</em> більше 67, ‘D` якщо <em>percent</em> більше 63, ‘D-‘ якщо <em>percent</em> більше 60, і ‘F` (незадовільно) для будь-якого <em>percent</em> менше 60. Оцінки, що точно відповідають межі, повинні бути включені до вищої категорії оцінок.</p></li>
</ol>


<pre><span></span><span>def</span> <span>my_letter_grader</span><span>(</span><span>percent</span><span>):</span>
    <span># write your function code here</span>
    
    <span>return</span> <span>grade</span>
</pre>





<pre><span></span><span># Output: 'A+'</span>
<span>my_letter_grader</span><span>(</span><span>97</span><span>)</span>
</pre>





<pre><span></span><span># Output: 'B'</span>
<span>my_letter_grader</span><span>(</span><span>84</span><span>)</span>
</pre>



<ol>
<li><p>Більшість інженерних систем мають надмірність. Тобто, інженерна система має більше, ніж потрібно для досягнення своєї мети. Розгляньте ядерний реактор, температура якого контролюється трьома датчиками. Сигналізація повинна спрацювати, якщо показання будь-яких двох датчиків відрізняються. Напишіть функцію <em>my_nuke_alarm(s1,s2,s3)</em>, де <em>s1</em>, <em>s2</em> і <em>s3</em> — це показання температури для датчика 1, датчика 2 і датчика 3 відповідно. Вихідним значенням повинен бути рядок ‘alarm!` (тривога!), якщо показання будь-яких двох температур відрізняються строго більше ніж на 10 градусів, і ‘normal` (нормально) в іншому випадку.</p></li>
</ol>


<pre><span></span><span>def</span> <span>my_nuke_alarm</span><span>(</span><span>s1</span><span>,</span><span>s2</span><span>,</span><span>s3</span><span>):</span>
    <span># write your function code here</span>
    
    <span>return</span> <span>response</span>
</pre>





<pre><span></span><span>#Output: 'normal'</span>
<span>my_nuke_alarm</span><span>(</span><span>94</span><span>,</span><span>96</span><span>,</span><span>90</span><span>)</span>
</pre>





<pre><span></span><span>#Output: 'alarm!'</span>
<span>my_nuke_alarm</span><span>(</span><span>94</span><span>,</span><span>96</span><span>,</span><span>80</span><span>)</span>
</pre>





<pre><span></span><span>#Output: 'normal'</span>
<span>my_nuke_alarm</span><span>(</span><span>100</span><span>,</span><span>96</span><span>,</span><span>90</span><span>)</span>
</pre>



<ol>
<li><p>Нехай Q(x) — квадратне рівняння <span>\(Q(x) = ax^2 + bx + c\)</span> для деяких скалярних значень <em>a</em>, <em>b</em> і <em>c</em>. Корінь <span>\(Q(x)\)</span> — це <em>r</em> таке, що <span>\(Q(r) = 0\)</span>. Два корені квадратного рівняння можна описати за допомогою квадратичної формули, яка є</p></li>
</ol>

\[r = \frac{-b\pm\sqrt{b^2-4ac}}{2a}\]
<p>Квадратне рівняння має або два дійсні корені (тобто <span>\(b^2 &gt; 4ac\)</span>), два уявні корені (тобто <span>\(b^2 &lt; 4ac\)</span>), або один корінь, <span>\(r = − \frac{b}{2a}\)</span>.</p>
<p>Напишіть функцію <em>my_n_roots(a,b,c)</em>, де <em>a</em>, <em>b</em> і <em>c</em> — коефіцієнти квадратного рівняння <span>\(Q(x)\)</span>, функція повинна повертати два значення: <em>n_roots</em> і <em>r</em>. <em>n_roots</em> дорівнює 2, якщо <em>Q</em> має два дійсні корені, 1, якщо <em>Q</em> має один корінь, −2, якщо <em>Q</em> має два уявні корені, а <em>r</em> — це масив, що містить корені <em>Q</em>.</p>


<pre><span></span><span>def</span> <span>my_n_roots</span><span>(</span><span>a</span><span>,</span><span>b</span><span>,</span><span>c</span><span>):</span>
    <span># write your function code here</span>
    
    <span>return</span> <span>n_roots</span><span>,</span> <span>r</span>
</pre>





<pre><span></span><span># Output: n_roots = 2, r = [3, -3]</span>
<span>n_roots</span><span>,</span> <span>r</span> <span>=</span> <span>my_n_roots</span><span>(</span><span>1</span><span>,</span><span>0</span><span>,</span><span>-</span><span>9</span><span>)</span>
<span>print</span><span>(</span><span>n_roots</span><span>,</span> <span>r</span><span>)</span>
</pre>





<pre><span></span><span># Output: n_roots = -2, r = [-0.6667 + 1.1055i, -0.6667 - 1.1055i]</span>
<span>my_n_roots</span><span>(</span><span>3</span><span>,</span><span>4</span><span>,</span><span>5</span><span>)</span>
</pre>





<pre><span></span><span># Output: n_roots = 1, r = [1]</span>
<span>my_n_roots</span><span>(</span><span>2</span><span>,</span><span>4</span><span>,</span><span>2</span><span>)</span>
</pre>



<ol>
<li><p>Напишіть функцію <em>my_split_function(f,g,a,b,x)</em>, де <em>f</em> і <em>g</em> — це посилання на функції <span>\(f(x)\)</span> і <span>\(g(x)\)</span> відповідно. Вихідним значенням повинно бути <span>\(f(x)\)</span>, якщо <span>\(x≤a\)</span>, <span>\(g(x)\)</span>, якщо <span>\(x≥b\)</span>, і <span>\(0\)</span> в іншому випадку. Можна припустити, що <span>\(b&gt;a\)</span>.</p></li>
</ol>


<pre><span></span><span>def</span> <span>my_split_function</span><span>(</span><span>f</span><span>,</span><span>g</span><span>,</span><span>a</span><span>,</span><span>b</span><span>,</span><span>x</span><span>):</span>
    
    <span>if</span> <span>x</span><span>&lt;=</span><span>a</span><span>:</span>
        <span>return</span> <span>f</span><span>(</span><span>x</span><span>)</span>
    <span>elif</span> <span>x</span><span>&gt;=</span><span>b</span><span>:</span>
        <span>return</span> <span>g</span><span>(</span><span>x</span><span>)</span>
    <span>else</span><span>:</span>
        <span>return</span> <span>0</span>
</pre>





<pre><span></span><span># Output: 2.713</span>
<span>my_split_function</span><span>(</span><span>np</span><span>.</span><span>exp</span><span>,</span><span>np</span><span>.</span><span>sin</span><span>,</span><span>2</span><span>,</span><span>4</span><span>,</span><span>1</span><span>)</span>
</pre>





<pre><span></span><span># Output: 0</span>
<span>my_split_function</span><span>(</span><span>np</span><span>.</span><span>exp</span><span>,</span><span>np</span><span>.</span><span>sin</span><span>,</span><span>2</span><span>,</span><span>4</span><span>,</span><span>3</span><span>)</span>
</pre>





<pre><span></span><span># Output: -0.9589</span>
<span>my_split_function</span><span>(</span><span>np</span><span>.</span><span>exp</span><span>,</span><span>np</span><span>.</span><span>sin</span><span>,</span><span>2</span><span>,</span><span>4</span><span>,</span><span>5</span><span>)</span>
</pre>
