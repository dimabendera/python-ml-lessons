<h1>Регресія методом найменших квадратів у Python<a href="#least-squares-regression-in-python" title="Постійне посилання на цей заголовок"></a></h1>
<p>Нагадаємо, що якщо ми перерахуємо оцінку даних у кожній точці даних, <span>\(x_i\)</span>, це дає нам таку систему рівнянь:</p>

\[\begin{eqnarray*}
&amp;&amp;\hat{y}(x_1) = {\alpha}_1 f_1(x_1) + {\alpha}_2 f_2(x_1) + \cdots + {\alpha}_n f_n(x_1),\\
&amp;&amp;\hat{y}(x_2) = {\alpha}_1 f_1(x_2) + {\alpha}_2 f_2(x_2) + \cdots + {\alpha}_n f_n(x_2),\\
&amp;&amp;\qquad\qquad\qquad\qquad\qquad \cdots\\
&amp;&amp;\hat{y}(x_m) = {\alpha}_1 f_1(x_m) + {\alpha}_2 f_2(x_m) + \cdots + {\alpha}_n f_n(x_m).
\end{eqnarray*}\]
<p>Якби дані були абсолютно ідеальними (тобто без шуму), то функція оцінки проходила б через усі точки даних, що призвело б до такої системи рівнянь:</p>

\[\begin{eqnarray*}
&amp;&amp;y_1 = {\alpha}_1 f_1(x_1) + {\alpha}_2 f_2(x_1) + \cdots + {\alpha}_n
f_n(x_1),\\
&amp;&amp;y_2 = {\alpha}_1 f_1(x_2) + {\alpha}_2 f_2(x_2) + \cdots + {\alpha}_n
f_n(x_2),\\
&amp;&amp;\qquad\qquad\qquad\qquad\cdots\\
&amp;&amp;y_m = {\alpha}_1 f_1(x_m) + {\alpha}_2 f_2(x_m) + \cdots + {\alpha}_n f_n(x_m).
\end{eqnarray*}\]
<p>Якщо ми візьмемо <span>\(A\)</span> як визначено раніше, це призведе до матричного рівняння
$<span>\(
Y = A{\beta}.
\)</span>$</p>
<p>Однак, оскільки дані не є ідеальними, не існуватиме функції оцінки, яка б проходила через усі точки даних, і ця система матиме <span>\(\textit{без розв'язку}\)</span>. Тому нам потрібно використати регресію методом найменших квадратів, яку ми вивели в попередніх двох розділах, щоб отримати розв'язок.</p>

\[{\beta} = (A^T A)^{-1} A^T Y\]
<p><strong>СПРОБУЙТЕ!</strong> Розгляньте штучні дані, створені за допомогою <span>\(\textit{x = np.linspace(0, 1, 101)}\)</span> та <span>\(\textit{y = 1 + x + x * np.random.random(len(x))}\)</span>. Виконайте регресію методом найменших квадратів з функцією оцінки, визначеною як <span>\(\hat{y}=\alpha_1x+\alpha_2\)</span>. Побудуйте точки даних разом з регресією методом найменших квадратів. Зауважте, що ми очікуємо <span>\(\alpha_1=1.5\)</span> та <span>\(\alpha_2=1.0\)</span> на основі цих даних. Через випадковий шум, який ми додали до даних, ваші результати можуть дещо відрізнятися.</p>

<h2>Використання методу прямої інверсії<a href="#use-direct-inverse-method" title="Постійне посилання на цей заголовок"></a></h2>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
<span>from</span> <span>scipy</span> <span>import</span> <span>optimize</span>
<span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>

<span>plt</span><span>.</span><span>style</span><span>.</span><span>use</span><span>(</span><span>'seaborn-poster'</span><span>)</span>
</pre>





<pre><span></span><span># generate x and y</span>
<span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>1</span><span>,</span> <span>101</span><span>)</span>
<span>y</span> <span>=</span> <span>1</span> <span>+</span> <span>x</span> <span>+</span> <span>x</span> <span>*</span> <span>np</span><span>.</span><span>random</span><span>.</span><span>random</span><span>(</span><span>len</span><span>(</span><span>x</span><span>))</span>
</pre>





<pre><span></span><span># assemble matrix A</span>
<span>A</span> <span>=</span> <span>np</span><span>.</span><span>vstack</span><span>([</span><span>x</span><span>,</span> <span>np</span><span>.</span><span>ones</span><span>(</span><span>len</span><span>(</span><span>x</span><span>))])</span><span>.</span><span>T</span>

<span># turn y into a column vector</span>
<span>y</span> <span>=</span> <span>y</span><span>[:,</span> <span>np</span><span>.</span><span>newaxis</span><span>]</span>
</pre>





<pre><span></span><span># Direct least square regression</span>
<span>alpha</span> <span>=</span> <span>np</span><span>.</span><span>dot</span><span>((</span><span>np</span><span>.</span><span>dot</span><span>(</span><span>np</span><span>.</span><span>linalg</span><span>.</span><span>inv</span><span>(</span><span>np</span><span>.</span><span>dot</span><span>(</span><span>A</span><span>.</span><span>T</span><span>,</span><span>A</span><span>)),</span><span>A</span><span>.</span><span>T</span><span>)),</span><span>y</span><span>)</span>
<span>print</span><span>(</span><span>alpha</span><span>)</span>
</pre>



<pre><span></span>[[1.459573  ]
 [1.02952189]]
</pre>





<pre><span></span><span># plot the results</span>
<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span><span>8</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>'b.'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>alpha</span><span>[</span><span>0</span><span>]</span><span>*</span><span>x</span> <span>+</span> <span>alpha</span><span>[</span><span>1</span><span>],</span> <span>'r'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'x'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'y'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="Графік регресії методом найменших квадратів" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter16.04-Least-Squares-Regression-in-Python_8_0.png"/>


<p>У Python існує багато різних способів виконання регресії методом найменших квадратів. Наприклад, ми можемо використовувати такі пакети, як *numpy*, *scipy*, *statsmodels*, *sklearn* тощо, щоб отримати розв'язок методом найменших квадратів. Тут ми використаємо наведений вище приклад і покажемо вам більше способів це зробити. Обирайте той, який вам подобається.</p>


<h2>Використання псевдооберненої матриці<a href="#use-the-pseudoinverse" title="Постійне посилання на цей заголовок"></a></h2>
<p>Раніше ми говорили, що <span>\((A^T A)^{-1} A^T\)</span> називається псевдооберненою матрицею, тому ми можемо використовувати функцію *pinv* у *numpy* для її безпосереднього обчислення.</p>


<pre><span></span><span>pinv</span> <span>=</span> <span>np</span><span>.</span><span>linalg</span><span>.</span><span>pinv</span><span>(</span><span>A</span><span>)</span>
<span>alpha</span> <span>=</span> <span>pinv</span><span>.</span><span>dot</span><span>(</span><span>y</span><span>)</span>
<span>print</span><span>(</span><span>alpha</span><span>)</span>
</pre>



<pre><span></span>[[1.459573  ]
 [1.02952189]]
</pre>





<h2>Використання numpy.linalg.lstsq<a href="#use-numpy-linalg-lstsq" title="Постійне посилання на цей заголовок"></a></h2>
<p>Насправді, *numpy* вже реалізував методи найменших квадратів, тому ми можемо просто викликати функцію, щоб отримати розв'язок. Функція поверне більше, ніж сам розв'язок, будь ласка, перегляньте документацію для отримання детальної інформації.</p>


<pre><span></span><span>alpha</span> <span>=</span> <span>np</span><span>.</span><span>linalg</span><span>.</span><span>lstsq</span><span>(</span><span>A</span><span>,</span> <span>y</span><span>,</span> <span>rcond</span><span>=</span><span>None</span><span>)[</span><span>0</span><span>]</span>
<span>print</span><span>(</span><span>alpha</span><span>)</span>
</pre>



<pre><span></span>[[1.459573  ]
 [1.02952189]]
</pre>





<h2>Використання optimize.curve_fit з scipy<a href="#use-optimize-curve-fit-from-scipy" title="Постійне посилання на цей заголовок"></a></h2>
<p>Ця функція scipy насправді дуже потужна, оскільки вона може апроксимувати не тільки лінійні функції, але й багато різних форм функцій, таких як нелінійні функції. Тут ми покажемо лінійний приклад, наведений вище. Зауважте, що, використовуючи цю функцію, нам не потрібно перетворювати y на вектор-стовпець.</p>


<pre><span></span><span># generate x and y</span>
<span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>1</span><span>,</span> <span>101</span><span>)</span>
<span>y</span> <span>=</span> <span>1</span> <span>+</span> <span>x</span> <span>+</span> <span>x</span> <span>*</span> <span>np</span><span>.</span><span>random</span><span>.</span><span>random</span><span>(</span><span>len</span><span>(</span><span>x</span><span>))</span>
</pre>





<pre><span></span><span>def</span> <span>func</span><span>(</span><span>x</span><span>,</span> <span>a</span><span>,</span> <span>b</span><span>):</span>
    <span>y</span> <span>=</span> <span>a</span><span>*</span><span>x</span> <span>+</span> <span>b</span>
    <span>return</span> <span>y</span>

<span>alpha</span> <span>=</span> <span>optimize</span><span>.</span><span>curve_fit</span><span>(</span><span>func</span><span>,</span> <span>xdata</span> <span>=</span> <span>x</span><span>,</span> <span>ydata</span> <span>=</span> <span>y</span><span>)[</span><span>0</span><span>]</span>
<span>print</span><span>(</span><span>alpha</span><span>)</span>
</pre>



<pre><span></span>[1.44331612 1.0396133 ]
</pre>
