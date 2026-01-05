<h1>Поліноміальна інтерполяція Ньютона<a href="#newton-s-polynomial-interpolation" title="Постійне посилання на цей заголовок"></a></h1>
<p>Поліноміальна інтерполяція Ньютона — це ще один популярний спосіб точного апроксимування набору точок даних. Загальний вигляд полінома Ньютона <span>\(n-1\)</span>-го порядку, що проходить через <span>\(n\)</span> точок, такий:</p>

\[ f(x) = a_0 + a_1(x-x_0) + a_2(x-x_0)(x-x_1) + \dots + a_n(x-x_0)(x-x_1)\dots(x-x_n)\]
<p>який можна переписати як:</p>

\[ f(x) = \sum_{i=0}^{n}{a_in_i(x)}\]
<p>де $<span>\( n_i(x) = \prod_{j=0}^{i-1}(x-x_j)\)</span>$</p>
<p>Особливістю полінома Ньютона є те, що коефіцієнти <span>\(a_i\)</span> можна визначити за допомогою дуже простої математичної процедури. Наприклад, оскільки поліном проходить через кожну точку даних, то для точки даних <span>\((x_i, y_i)\)</span> ми матимемо <span>\(f(x_i) = y_i\)</span>, отже, ми маємо</p>

\[f(x_0) = a_0 = y_0\]
<p>І <span>\(f(x_1) = a_0 + a_1(x_1-x_0) = y_1\)</span>, перегрупувавши його, щоб отримати <span>\(a_1\)</span>, ми матимемо:</p>

\[a_1 = \frac{y_1 - y_0}{x_1 - x_0}\]
<p>Тепер, вставивши точки даних <span>\((x_2, y_2)\)</span>, ми можемо обчислити <span>\(a_2\)</span>, і він має вигляд:</p>

\[a_2 = \frac{\frac{y_2 - y_1}{x_2 - x_1} - \frac{y_1 - y_0}{x_1 - x_0}}{x_2 - x_0}\]
<p>Давайте візьмемо ще одну точку даних <span>\((x_3, y_3)\)</span>, щоб обчислити <span>\(a_3\)</span>, після вставки точки даних у рівняння, ми отримаємо:</p>

\[a_3 = \frac{\frac{\frac{y_3-y_2}{x_3-x_2} - \frac{y_2 - y_1}{x_2-x_1}}{x_3 - x_1} - \frac{\frac{y_2-y_1}{x_2-x_1}-\frac{y_1 - y_0}{x_1 - x_0}}{x_2-x_0}}{x_3 - x_0}\]
<p>Тепер бачите закономірності? Це називається <strong>розділеними різницями</strong>, якщо ми визначимо:</p>

\[ f[x_1, x_0] = \frac{y_1 - y_0}{x_1 - x_0}\]

\[ f[x_2, x_1, x_0] = \frac{\frac{y_2 - y_1}{x_2 - x_1} - \frac{y_1 - y_0}{x_1 - x_0}}{x_2 - x_0} = \frac{f[x_2,x_1] - f[x_1,x_0]}{x_2-x_1}\]
<p>Продовжуючи записувати це, ми отримаємо наступне ітераційне рівняння:</p>

\[ f[x_k, x_{k-1}, \dots, x_{1}, x_0] = \frac{f[x_k, x_{k-1}, \dots, x_{2}, x_2] - f[x_{k-1}, x_{k-2}, \dots, x_{1}, x_0]}{x_k-x_0}\]
<p>Ми бачимо одну перевагу методу: як тільки коефіцієнти визначені, додавання нових точок даних не змінить вже обчислених, нам потрібно лише продовжувати обчислювати вищі різниці таким же чином. Всю процедуру знаходження цих коефіцієнтів можна узагальнити в таблиці розділених різниць. Розглянемо приклад з використанням 5 точок даних:</p>

\[\begin{split}
\begin{array}{cccccc}
x_0 &amp; y_0 \\
    &amp;     &amp; f[x_1,x_0] \\
x_1 &amp; y_1 &amp;             &amp; f[x_2, x_1,x_0]\\
    &amp;     &amp; f[x_2,x_1]  &amp;              &amp; f[x_3, x_2, x_1,x_0]\\
x_2 &amp; y_2 &amp;             &amp; f[x_3, x_2,x_1] &amp;             &amp; f[x_4, x_3, x_2, x_1,x_0]\\
    &amp;     &amp; f[x_3,x_2]  &amp;              &amp; f[x_4, x_3, x_2, x_1]\\
x_3 &amp; y_3 &amp;             &amp; f[x_4, x_3,x_2]\\
    &amp;     &amp; f[x_4,x_3] \\
x_4 &amp; y_4
\end{array}
\end{split}\]
<p>Кожен елемент у таблиці можна обчислити, використовуючи два попередні елементи (ліворуч). Насправді, ми можемо обчислити кожен елемент і зберегти їх у діагональній матриці, тобто матрицю коефіцієнтів можна записати як:</p>

\[\begin{split}
\begin{array}{cccccc}
y_0 &amp; f[x_1,x_0] &amp; f[x_2, x_1,x_0] &amp; f[x_3, x_2, x_1,x_0] &amp; f[x_4, x_3, x_2, x_1,x_0]\\
y_1 &amp; f[x_2,x_1] &amp; f[x_3, x_2,x_1] &amp; f[x_4, x_3, x_2, x_1] &amp; 0\\
y_2 &amp; f[x_3,x_2] &amp; f[x_4, x_3,x_2] &amp; 0          &amp; 0 \\
y_3 &amp; f[x_4,x_3] &amp; 0 &amp; 0 &amp; 0            \\
y_4 &amp; 0 &amp; 0 &amp; 0  &amp; 0  
\end{array}
\end{split}\]
<p>Зауважте, що перший рядок у матриці — це насправді всі коефіцієнти, які нам потрібні, тобто <span>\(a_0, a_1, a_2, a_3, a_4\)</span>. Давайте розглянемо приклад, як це можна зробити.</p>
<p><strong>СПРОБУЙТЕ!</strong> Обчисліть таблицю розділених різниць для x = [-5, -1, 0, 2], y = [-2, 6, 1, 3].</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
<span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>

<span>plt</span><span>.</span><span>style</span><span>.</span><span>use</span><span>(</span><span>'seaborn-poster'</span><span>)</span>

<span>%</span><span>matplotlib</span> inline
</pre>





<pre><span></span><span>def</span> <span>divided_diff</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>):</span>
    <span>'''</span>
<span>    функція для обчислення таблиці</span>
<span>    розділених різниць</span>
<span>    '''</span>
    <span>n</span> <span>=</span> <span>len</span><span>(</span><span>y</span><span>)</span>
    <span>coef</span> <span>=</span> <span>np</span><span>.</span><span>zeros</span><span>([</span><span>n</span><span>,</span> <span>n</span><span>])</span>
    <span># перший стовпець - це y</span>
    <span>coef</span><span>[:,</span><span>0</span><span>]</span> <span>=</span> <span>y</span>
    
    <span>for</span> <span>j</span> <span>in</span> <span>range</span><span>(</span><span>1</span><span>,</span><span>n</span><span>):</span>
        <span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>n</span><span>-</span><span>j</span><span>):</span>
            <span>coef</span><span>[</span><span>i</span><span>][</span><span>j</span><span>]</span> <span>=</span> \
           <span>(</span><span>coef</span><span>[</span><span>i</span><span>+</span><span>1</span><span>][</span><span>j</span><span>-</span><span>1</span><span>]</span> <span>-</span> <span>coef</span><span>[</span><span>i</span><span>][</span><span>j</span><span>-</span><span>1</span><span>])</span> <span>/</span> <span>(</span><span>x</span><span>[</span><span>i</span><span>+</span><span>j</span><span>]</span><span>-</span><span>x</span><span>[</span><span>i</span><span>])</span>
            
    <span>return</span> <span>coef</span>

<span>def</span> <span>newton_poly</span><span>(</span><span>coef</span><span>,</span> <span>x_data</span><span>,</span> <span>x</span><span>):</span>
    <span>'''</span>
<span>    обчислити поліном Ньютона </span>
<span>    в точці x</span>
<span>    '''</span>
    <span>n</span> <span>=</span> <span>len</span><span>(</span><span>x_data</span><span>)</span> <span>-</span> <span>1</span> 
    <span>p</span> <span>=</span> <span>coef</span><span>[</span><span>n</span><span>]</span>
    <span>for</span> <span>k</span> <span>in</span> <span>range</span><span>(</span><span>1</span><span>,</span><span>n</span><span>+</span><span>1</span><span>):</span>
        <span>p</span> <span>=</span> <span>coef</span><span>[</span><span>n</span><span>-</span><span>k</span><span>]</span> <span>+</span> <span>(</span><span>x</span> <span>-</span><span>x_data</span><span>[</span><span>n</span><span>-</span><span>k</span><span>])</span><span>*</span><span>p</span>
    <span>return</span> <span>p</span>
</pre>





<pre><span></span><span>x</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([</span><span>-</span><span>5</span><span>,</span> <span>-</span><span>1</span><span>,</span> <span>0</span><span>,</span> <span>2</span><span>])</span>
<span>y</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([</span><span>-</span><span>2</span><span>,</span> <span>6</span><span>,</span> <span>1</span><span>,</span> <span>3</span><span>])</span>
<span># get the divided difference coef</span>
<span>a_s</span> <span>=</span> <span>divided_diff</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>)[</span><span>0</span><span>,</span> <span>:]</span>

<span># evaluate on new data points</span>
<span>x_new</span> <span>=</span> <span>np</span><span>.</span><span>arange</span><span>(</span><span>-</span><span>5</span><span>,</span> <span>2.1</span><span>,</span> <span>.</span><span>1</span><span>)</span>
<span>y_new</span> <span>=</span> <span>newton_poly</span><span>(</span><span>a_s</span><span>,</span> <span>x</span><span>,</span> <span>x_new</span><span>)</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>12</span><span>,</span> <span>8</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>'bo'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x_new</span><span>,</span> <span>y_new</span><span>)</span>
</pre>



<pre><span></span>[&lt;matplotlib.lines.Line2D at 0x11bd4e630&gt;]
</pre>

<img alt="../_images/chapter17.05-Newtons-Polynomial-Interpolation_6_1.png" src="../_images/chapter17.05-Newtons-Polynomial-Interpolation_6_1.png"/>


<p>Ми бачимо, що поліном Ньютона проходить через усі точки даних і апроксимує їх.</p>
