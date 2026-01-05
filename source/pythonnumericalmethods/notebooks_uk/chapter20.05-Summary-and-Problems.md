<h1>Підсумок<a href="#summary" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Оскільки явне диференціювання функцій іноді є громіздким для інженерних застосувань, чисельні підходи можуть бути кращими.</p></li>
<li><p>Чисельне наближення похідних можна виконати за допомогою сітки, на якій похідна апроксимується скінченними різницями.</p></li>
<li><p>Скінченні різниці апроксимують похідну співвідношеннями різниць значень функції на малих інтервалах.</p></li>
<li><p>Схеми скінченних різниць мають різні порядки апроксимації залежно від використаного методу.</p></li>
<li><p>Існують проблеми зі скінченними різницями для апроксимації похідних, коли дані є зашумленими.</p></li>
</ol>


<h1>Задачі<a href="#problems" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Напишіть функцію <span>\(my\_der\_calc(f, a, b, N, option)\)</span>, з виходом у вигляді <span>\([df, X]\)</span>, де <span>\(f\)</span> є об'єктом функції, <span>\(a\)</span> та <span>\(b\)</span> є скалярами такими, що a &lt; b, <span>\(N\)</span> є цілим числом, більшим за 10, а <span>\(option)\)</span> є рядком <span>\(forward\)</span>, <span>\(backward\)</span>, або <span>\(central\)</span>. Нехай <span>\(x\)</span> буде масивом, що починається з <span>\(a\)</span>, закінчується на <span>\(b\)</span>, що містить <span>\(N\)</span> рівномірно розташованих елементів, і нехай <span>\(y\)</span> буде масивом <span>\(f(x)\)</span>. Вихідний аргумент, <span>\(df\)</span>, має бути чисельними похідними, обчисленими для <span>\(x\)</span> та <span>\(y\)</span> згідно з методом, визначеним вхідним аргументом, <span>\(option\)</span>. Вихідний аргумент <span>\(X\)</span> має бути масивом такого ж розміру, як <span>\(df\)</span>, що містить точки в <span>\(x\)</span>, для яких <span>\(df\)</span> є дійсним. Зокрема, метод прямої різниці "втрачає" останню точку, метод зворотної різниці втрачає першу точку, а метод центральної різниці втрачає першу та останню точки.</p></li>
<li><p>Напишіть функцію <span>\(my\_num\_diff(f, a, b, n, option)\)</span>, з виходом у вигляді <span>\([df, X]\)</span>, де <span>\(f\)</span> є об'єктом функції. Функція <span>\(my\_num\_diff\)</span> має обчислити похідну від <span>\(f\)</span> чисельно для <span>\(n\)</span> рівномірно розташованих точок, що починаються з <span>\(a\)</span> і закінчуються на <span>\(b\)</span> згідно з методом, визначеним <span>\(option\)</span>. Вхідний аргумент <span>\(option\)</span> є одним з наступних рядків: ‘forward`, ‘backward`, ‘central`. Зауважте, що для прямого та зворотного методів вихідний аргумент, <span>\(dy\)</span>, має бути <span>\((n-1)\)</span> 1D масивом, а для методу центральної різниці <span>\(dy\)</span> має бути <span>\((n-2)\)</span> 1D масивом. Функція також має виводити вектор <span>\(X\)</span> такого ж розміру, як <span>\(dy\)</span>, і позначати значення x, для яких <span>\(dy\)</span> є дійсним.</p></li>
</ol>
<p>Приклади використання:</p>
<pre><span></span><span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>2</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>,</span> <span>100</span><span>)</span>
<span>f</span> <span>=</span> <span>lambda</span> <span>x</span><span>:</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>x</span><span>)</span>
<span>[</span><span>dyf</span><span>,</span> <span>Xf</span><span>]</span> <span>=</span> <span>my_num_diff</span><span>(</span><span>f</span><span>,</span> <span>0</span><span>,</span> <span>2</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>,</span> <span>10</span><span>,</span> <span>'forward'</span><span>)</span>
<span>[</span><span>dyb</span><span>,</span> <span>Xb</span><span>]</span> <span>=</span> <span>my_num_diff</span><span>(</span><span>f</span><span>,</span> <span>0</span><span>,</span> <span>2</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>,</span> <span>10</span><span>,</span> <span>'backward'</span><span>)</span>
<span>[</span><span>dyc</span><span>,</span> <span>Xc</span><span>]</span> <span>=</span> <span>my_num_diff</span><span>(</span><span>f</span><span>,</span> <span>0</span><span>,</span> <span>2</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>,</span> <span>10</span><span>,</span> <span>'central'</span><span>)</span>
<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>12</span><span>,</span> <span>8</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>np</span><span>.</span><span>cos</span><span>(</span><span>x</span><span>),</span> <span>label</span> <span>=</span> <span>'аналітична'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>Xf</span><span>,</span> <span>dyf</span><span>,</span> <span>label</span> <span>=</span> <span>'пряма'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>Xb</span><span>,</span> <span>dyb</span><span>,</span> <span>label</span> <span>=</span> <span>'зворотна'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>Xc</span><span>,</span> <span>dyc</span><span>,</span> <span>label</span> <span>=</span> <span>'центральна'</span><span>)</span>
<span>plt</span><span>.</span><span>legend</span><span>()</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>'Аналітичні та чисельні похідні синуса'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'x'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'y'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>

<p><img alt="" src="../_images/20.05.01-Q2-1.png"/></p>
<pre><span></span><span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>np</span><span>.</span><span>pi</span><span>,</span> <span>1000</span><span>)</span>
<span>f</span> <span>=</span> <span>lambda</span> <span>x</span><span>:</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>np</span><span>.</span><span>exp</span><span>(</span><span>x</span><span>))</span>
<span>[</span><span>dy10</span><span>,</span> <span>X10</span><span>]</span> <span>=</span> <span>my_num_diff</span><span>(</span><span>f</span><span>,</span> <span>0</span><span>,</span> <span>np</span><span>.</span><span>pi</span><span>,</span> <span>10</span><span>,</span> <span>'central'</span><span>)</span>
<span>[</span><span>dy20</span><span>,</span> <span>X20</span><span>]</span> <span>=</span> <span>my_num_diff</span><span>(</span><span>f</span><span>,</span> <span>0</span><span>,</span> <span>np</span><span>.</span><span>pi</span><span>,</span> <span>20</span><span>,</span> <span>'central'</span><span>)</span>
<span>[</span><span>dy100</span><span>,</span> <span>X100</span><span>]</span> <span>=</span> <span>my_num_diff</span><span>(</span><span>f</span><span>,</span> <span>0</span><span>,</span> <span>np</span><span>.</span><span>pi</span><span>,</span> <span>100</span><span>,</span> <span>'central'</span><span>)</span>
<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>12</span><span>,</span> <span>8</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>np</span><span>.</span><span>cos</span><span>(</span><span>np</span><span>.</span><span>exp</span><span>(</span><span>x</span><span>)),</span> <span>label</span> <span>=</span> <span>'аналітична'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>X10</span><span>,</span> <span>dy10</span><span>,</span> <span>label</span> <span>=</span> <span>'10 точок'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>X20</span><span>,</span> <span>dy20</span><span>,</span> <span>label</span> <span>=</span> <span>'20 точок'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>X100</span><span>,</span> <span>dy100</span><span>,</span> <span>label</span> <span>=</span> <span>'100 точок'</span><span>)</span>
<span>plt</span><span>.</span><span>legend</span><span>()</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>'Аналітичні та чисельні похідні синуса'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'x'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'y'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>

<p><img alt="" src="../_images/20.05.01-Q2-2.png"/></p>
<ol>
<li><p>Напишіть функцію <span>\(my\_num\_diff\_w\_smoothing(x, y, n)\)</span>, з виходом <span>\([dy, X], \)</span>де <span>\(x\)</span> та <span>\(y\)</span> є 1D масивами numpy однакової довжини, а <span>\(n\)</span> є строго позитивним скаляром. Функція спочатку має створити вектор "згладжених" точок даних <span>\(y\)</span>, де <span>\(y\_smooth[i] = np.mean(y[i-n:i+n])\)</span>. Потім функція має обчислити <span>\(dy\)</span>, похідну згладженого <span>\(y\)</span>-вектора, використовуючи метод центральної різниці. Функція також має виводити 1D масив <span>\(X\)</span> такого ж розміру, як <span>\(dy\)</span>, і позначати значення x, для яких <span>\(dy\)</span> є дійсним.</p></li>
</ol>
<p>Припустімо, що дані, що містяться в <span>\(x\)</span>, розташовані у зростаючому порядку без дублікатів. Однак можливо, що елементи <span>\(x\)</span> не будуть рівномірно розташовані. Зауважте, що вихідний <span>\(dy\)</span> матиме на <span>\(2n + 2\)</span> точок менше, ніж <span>\(y\)</span>. Припустімо, що довжина <span>\(y\)</span> значно більша за <span>\(2n + 2\)</span>.</p>
<p>Приклади використання:</p>
<pre><span></span><span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>2</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>,</span> <span>100</span><span>)</span>
<span>y</span> <span>=</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>x</span><span>)</span> <span>+</span> <span>np</span><span>.</span><span>random</span><span>.</span><span>randn</span><span>(</span><span>len</span><span>(</span><span>x</span><span>))</span><span>/</span><span>100</span>
<span>[</span><span>dy</span><span>,</span> <span>X</span><span>]</span> <span>=</span> <span>my_num_diff_w_smoothing</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>4</span><span>)</span>
<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>12</span><span>,</span> <span>12</span><span>))</span>
<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>211</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>'Зашумлена функція синуса'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'x'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'y'</span><span>)</span>
<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>212</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>np</span><span>.</span><span>cos</span><span>(</span><span>x</span><span>),</span> <span>'b'</span><span>,</span> <span>label</span> <span>=</span> <span>'косинус'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>[:</span><span>-</span><span>1</span><span>],</span> <span>(</span><span>y</span><span>[</span><span>1</span><span>:]</span> <span>-</span> <span>y</span><span>[:</span><span>-</span><span>1</span><span>])</span><span>/</span><span>(</span><span>x</span><span>[</span><span>1</span><span>]</span><span>-</span><span>x</span><span>[</span><span>0</span><span>]),</span> <span>'g'</span><span>,</span> \
    <span>label</span> <span>=</span> <span>'незгладжена пряма різниця'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>X</span><span>,</span> <span>dy</span><span>,</span> <span>'r'</span><span>,</span> <span>label</span> <span>=</span> <span>'згладжена'</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>'Аналітична та згладжена похідна'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'x'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'y'</span><span>)</span>
<span>plt</span><span>.</span><span>legend</span><span>()</span>
<span>plt</span><span>.</span><span>tight_layout</span><span>()</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>

<p><img alt="" src="../_images/20.05.01-Q3.png"/></p>
<ol>
<li><p>Використайте ряд Тейлора, щоб показати наступні апроксимації та їх точність.
$$</p></li>
</ol>

\[\begin{eqnarray*}
f''(x_j) &amp;=&amp; \frac{-f(x_{j+3})+4f(x_{j+2}) - 5f(x_{j+1}) + 2f(x_j)}{h^2} + O(h^2),\\
f'''(x_j) &amp;=&amp; \frac{f(x_{j+3})-3f(x_{j+2}) +3f(x_{j+1}) - f(x_j)}{h^3} + O(h).
\end{eqnarray*}\]
<p>$$</p>
