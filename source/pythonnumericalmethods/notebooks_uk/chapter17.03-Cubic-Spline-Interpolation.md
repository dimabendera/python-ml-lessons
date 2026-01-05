```html
<h1>Кубічна сплайн-інтерполяція<a href="#cubic-spline-interpolation" title="Permalink to this headline"></a></h1>
<p>В <strong>кубічній сплайн-інтерполяції</strong> (як показано на наступному малюнку), інтерполяційна функція є набором кусково-кубічних функцій. Зокрема, ми припускаємо, що точки <span>\((x_i, y_i)\)</span> та <span>\((x_{i+1}, y_{i+1})\)</span> з'єднані кубічним поліномом <span>\(S_i(x) = a_i x^3 + b_i x^2 + c_i x + d_i\)</span>, який є дійсним для <span>\(x_i \le x \le x_{i+1}\)</span> для <span>\(i = 1,\ldots, n-1\)</span>. Щоб знайти інтерполяційну функцію, ми повинні спочатку визначити коефіцієнти <span>\(a_i, b_i, c_i, d_i\)</span> для кожної з кубічних функцій. Для <span>\(n\)</span> точок, існує <span>\(n-1\)</span> кубічних функцій, які потрібно знайти, і кожна кубічна функція вимагає чотири коефіцієнти. Отже, ми маємо загалом <span>\(4(n-1)\)</span> невідомих, і тому нам потрібно <span>\(4(n-1)\)</span> незалежних рівнянь, щоб знайти всі коефіцієнти.</p>

<p>По-перше, ми знаємо, що кубічні функції повинні перетинати дані в точках зліва та справа:</p>

\[\begin{eqnarray*}
S_i(x_i) &amp;=&amp; y_i,\quad i = 1,\ldots,n-1,\\
S_i(x_{i+1}) &amp;=&amp; y_{i+1},\quad i = 1,\ldots,n-1,
\end{eqnarray*}\]
<p>що дає нам <span>\(2(n-1)\)</span> рівнянь. Далі, ми хочемо, щоб кожна кубічна функція з'єднувалася зі своїми сусідами якомога плавніше, тому ми накладаємо обмеження, щоб сплайни мали неперервні першу та другу похідні в точках даних <span>\(i = 2,\ldots,n-1\)</span>.</p>

\[\begin{eqnarray*}
S^{\prime}_i(x_{i+1}) &amp;=&amp; S^{\prime}_{i+1}(x_{i+1}),\quad i = 1,\ldots,n-2,\\
S''_i(x_{i+1}) &amp;=&amp; S''_{i+1}(x_{i+1}),\quad i = 1,\ldots,n-2,
\end{eqnarray*}\]
<p>що дає нам <span>\(2(n-2)\)</span> рівнянь.</p>
<p>Ще два рівняння потрібні для обчислення коефіцієнтів <span>\(S_i(x)\)</span>. Ці останні два обмеження є довільними, і їх можна вибрати відповідно до обставин виконуваної інтерполяції. Поширеним набором кінцевих обмежень є припущення, що другі похідні дорівнюють нулю в кінцевих точках. Це означає, що крива є "прямою лінією" в кінцевих точках. Явно,</p>

\[\begin{eqnarray*}
S''_1(x_1) &amp;=&amp; 0\\
S''_{n-1}(x_n) &amp;=&amp; 0.
\end{eqnarray*}\]
<p>У Python ми можемо використовувати функцію <em>CubicSpline</em> з бібліотеки <em>scipy</em> для виконання кубічної сплайн-інтерполяції. Зауважте, що наведені вище обмеження не є такими ж, як ті, що використовуються <em>CubicSpline</em> з <em>scipy</em> за замовчуванням для виконання кубічних сплайнів; існують різні способи додати останні два обмеження в scipy, встановивши аргумент <em>bc_type</em> (дивіться довідку для <em>CubicSpline</em>, щоб дізнатися більше про це).</p>
<p><strong>СПРОБУЙТЕ!</strong> Використовуйте <em>CubicSpline</em> для побудови графіка кубічної сплайн-інтерполяції для набору даних <em>x = [0, 1, 2]</em> та <em>y = [1, 3, 2]</em> для <span>\(0\le x\le2\)</span>.</p>


<pre><span></span><span>from</span> <span>scipy.interpolate</span> <span>import</span> <span>CubicSpline</span>
<span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
<span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>

<span>plt</span><span>.</span><span>style</span><span>.</span><span>use</span><span>(</span><span>'seaborn-poster'</span><span>)</span>
</pre>





<pre><span></span><span>x</span> <span>=</span> <span>[</span><span>0</span><span>,</span> <span>1</span><span>,</span> <span>2</span><span>]</span>
<span>y</span> <span>=</span> <span>[</span><span>1</span><span>,</span> <span>3</span><span>,</span> <span>2</span><span>]</span>

<span># використання bc_type = 'natural' додає обмеження, як ми описали вище</span>
<span>f</span> <span>=</span> <span>CubicSpline</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>bc_type</span><span>=</span><span>'natural'</span><span>)</span>
<span>x_new</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>2</span><span>,</span> <span>100</span><span>)</span>
<span>y_new</span> <span>=</span> <span>f</span><span>(</span><span>x_new</span><span>)</span>
</pre>





<pre><span></span><span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span><span>8</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x_new</span><span>,</span> <span>y_new</span><span>,</span> <span>'b'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>'ro'</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>'Кубічна сплайн-інтерполяція'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'x'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'y'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter17.03-Cubic-Spline-Interpolation_6_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter17.03-Cubic-Spline-Interpolation_6_0.png"/>


<p>Щоб визначити коефіцієнти кожної кубічної функції, ми явно записуємо обмеження у вигляді системи лінійних рівнянь з <span>\(4(n-1)\)</span> невідомими. Для <span>\(n\)</span> точок даних невідомими є коефіцієнти <span>\(a_i, b_i, c_i, d_i\)</span> кубічного сплайна, <span>\(S_i\)</span>, що з'єднує точки <span>\(x_i\)</span> та <span>\(x_{i+1}\)</span>.</p>
<p>Для обмежень <span>\(S_i(x_i) = y_i\)</span> ми маємо:
$<span>\(
\begin{array}{rrrrr}
a_1 x_1^3 + &amp; b_1 x_1^2 +  &amp; c_1 x_1 +  &amp; d_1 = &amp;y_1,\\ 
a_2 x_2^3 + &amp; b_2 x_2^2 +  &amp; c_2 x_2 +  &amp; d_2 = &amp;y_2,\\ 
\cdots\\ 
a_{n-1} x_{n-1}^3 + &amp;b_{n-1} x_{n-1}^2 + &amp;c_{n-1} x_{n-1} +&amp; d_{n-1} =&amp; y_{n-1}.
\end{array}
\)</span>$</p>
<p>Для обмежень <span>\(S_i(x_{i+1}) = y_{i+1}\)</span> ми маємо:
$<span>\(
\begin{array}{rrrrr}
a_1 x_2^3 +&amp;b_1 x_2^2 +&amp;c_1 x_2 +&amp;d_1 =&amp; y_2,\\ 
a_2 x_3^3 +&amp;b_2 x_3^2 +&amp;c_2 x_3 +&amp;d_2 =&amp; y_3,\\
&amp;&amp;\cdots\\
a_{n-1} x_{n}^3 +&amp;b_{n-1} x_{n}^2 +&amp;c_{n-1} x_{n} +&amp;d_{n-1} =&amp; y_{n}.
\end{array}
\)</span>$</p>
<p>Для обмежень <span>\(S^{\prime}_i(x_{i+1}) = S^{\prime}_{i+1}(x_{i+1})\)</span> ми маємо:
$<span>\(
\begin{array}{rrrrrr}
3a_1 x_2^2 +&amp;2b_1 x_2 +&amp;c_1 - &amp;3a_2 x_2^2 - &amp;2b_2 x_2 - &amp;c_2 =0,\\ 
3a_2 x_3^2 +&amp;2b_2 x_3 +&amp;c_2 -&amp; 3a_3 x_3^2 -&amp; 2b_3 x_3 -&amp; c_3 =0,\\ 
&amp;&amp;&amp;\cdots&amp;&amp;,\\
3a_{n-2} x_{n-1}^2 +&amp;2b_{n-2} x_{n-1} +&amp;c_{n-2} -&amp; 3a_{n-1} x_{n-1}^2 -&amp; 2b_{n-1} x_{n-1} -&amp; c_{n-1} =0.
\end{array}
\)</span>$</p>
<p>Для обмежень <span>\(S''_i(x_{i+1}) = S''_{i+1}(x_{i+1})\)</span> ми маємо:</p>

\[\begin{split}
\begin{array}{rrrrrr}
6a_1 x_2 +&amp; 2b_1 -&amp; 6a_2 x_2 -&amp; 2b_2 =&amp; 0,\\
6a_2 x_3 +&amp; 2b_2 -&amp; 6a_3 x_3 -&amp; 2b_3 =&amp; 0,\\
+&amp;&amp;\ldots -&amp; \\
6a_{n-2} x_{n-1} +&amp; 2b_{n-2} -&amp; 6a_{n-1} x_{n-1} -&amp; 2b_{n-1} =&amp; 0.
\end{array}
\end{split}\]
<p>Нарешті, для обмежень у кінцевих точках <span>\(S''_1(x_1) = 0\)</span> та <span>\(S''_{n-1}(x_n) = 0\)</span>, ми маємо:
$<span>\(
\begin{array}{rr}
6a_1 x_1 +&amp; 2b_1 = 0,\\
6a_{n-1} x_n +&amp;2b_{n-1} = 0.
\end{array}
\)</span>$</p>
<p>Ці рівняння є лінійними відносно невідомих коефіцієнтів <span>\(a_i, b_i, c_i\)</span>, та <span>\(d_i\)</span>. Ми можемо записати їх у матричній формі та розв'язати відносно коефіцієнтів кожного сплайна за допомогою лівого ділення. Пам'ятайте, що щоразу, коли ми розв'язуємо матричне рівняння <span>\(Ax = b\)</span> відносно <span>\(x\)</span>, ми повинні переконатися, що <span>\(A\)</span> є квадратною та невиродженою (оборотною). У випадку знаходження рівнянь кубічного сплайна, матриця <span>\(A\)</span> завжди є квадратною та невиродженою, доки значення <span>\(x_i\)</span> у наборі даних є унікальними.</p>
<p><strong>СПРОБУЙТЕ!</strong> Знайдіть значення кубічної сплайн-інтерполяції в точці <em>x = 1.5</em> на основі даних <em>x = [0, 1, 2]</em>, <em>y = [1, 3, 2]</em>.</p>
<p>Спочатку ми створюємо відповідну систему рівнянь і знаходимо коефіцієнти кубічних сплайнів, розв'язуючи систему в матричній формі.</p>
<p>Матрична форма системи рівнянь:</p>
$<span>\(
\left[\begin{array}{llllllll}
0 &amp; 0 &amp; 0 &amp; 1 &amp; 0 &amp; 0 &amp; 0 &amp; 0\\
0 &amp; 0 &amp; 0 &amp; 0 &amp; 1 &amp; 1 &amp; 1 &amp; 1\\
1 &amp; 1 &amp; 1 &amp; 1 &amp; 0 &amp; 0 &amp; 0 &amp; 0\\
0 &amp; 0 &amp; 0 &amp; 0 &amp; 8 &amp; 4 &amp; 2 &amp; 1\\
3 &amp; 2 &amp; 1 &amp; 0 &amp; -3 &amp; -2 &amp; -1 &amp; 0\\
6 &amp; 2 &amp; 0 &amp; 0 &amp; -6 &amp; -2 &amp; 0 &amp; 0\\
0 &amp; 2 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0\\
0 &amp; 0 &amp; 0 &amp; 0 &amp; 12 &amp; 2 &amp; 0 &amp; 0
\end{array}\right]
\left[\begin{array}{c}
a_1 \\
b_1 \\
c_1 \\
d_1 \\
a_2 \\
b_2 \\
c_2 \\
d_2
\end{array}\right] =
\left[\begin{array}{c}
1 \\
3 \\
3 \\
2 \\
0 \\
0 \\
0 \\
0 \end{array}\right]
\)</span>$</p>


<pre><span></span><span>b</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([</span><span>1</span><span>,</span> <span>3</span><span>,</span> <span>3</span><span>,</span> <span>2</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>])</span>
<span>b</span> <span>=</span> <span>b</span><span>[:,</span> <span>np</span><span>.</span><span>newaxis</span><span>]</span>
<span>A</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>],</span> <span>[</span><span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>,</span> <span>1</span><span>,</span> <span>1</span><span>,</span> <span>1</span><span>],</span> <span>[</span><span>1</span><span>,</span> <span>1</span><span>,</span> <span>1</span><span>,</span> <span>1</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>],</span> \
             <span>[</span><span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>8</span><span>,</span> <span>4</span><span>,</span> <span>2</span><span>,</span> <span>1</span><span>],</span> <span>[</span><span>3</span><span>,</span> <span>2</span><span>,</span> <span>1</span><span>,</span> <span>0</span><span>,</span> <span>-</span><span>3</span><span>,</span> <span>-</span><span>2</span><span>,</span> <span>-</span><span>1</span><span>,</span> <span>0</span><span>],</span> <span>[</span><span>6</span><span>,</span> <span>2</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>-</span><span>6</span><span>,</span> <span>-</span><span>2</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>],</span>\
             <span>[</span><span>0</span><span>,</span> <span>2</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>],</span> <span>[</span><span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>12</span><span>,</span> <span>2</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>]])</span>
</pre>





<pre><span></span><span>np</span><span>.</span><span>dot</span><span>(</span><span>np</span><span>.</span><span>linalg</span><span>.</span><span>inv</span><span>(</span><span>A</span><span>),</span> <span>b</span><span>)</span>
</pre>



<pre><span></span>array([[-0.75],
       [ 0.  ],
       [ 2.75],
       [ 1.  ],
       [ 0.75],
       [-4.5 ],
       [ 7.25],
       [-0.5 ]])
</pre>



<p>Отже, два кубічні поліноми є</p>

\[\begin{eqnarray*}
S_1(x) &amp;=&amp; -.75x^3 + 2.75x + 1, \quad  \text{для} \quad 0 \le x \le 1\ \text{та}\\
S_2(x) &amp;=&amp; .75x^3 - 4.5x^2 + 7.25x - .5, \quad  \text{для}  \quad 1 \le x \le 2
\end{eqnarray*}\]
<p>Тож для <span>\(x = 1.5\)</span> ми обчислюємо <span>\(S_2(1.5)\)</span> і отримуємо оціночне значення 2.7813.</p>
```
