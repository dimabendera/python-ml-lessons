<h1>Лінійна інтерполяція<a href="#linear-interpolation" title="Постійне посилання на цей заголовок"></a></h1>
<p>У **лінійній інтерполяції** передбачається, що оцінювана точка лежить на прямій, що з'єднує найближчі точки ліворуч і праворуч. Припустимо, без втрати загальності, що точки даних <span>\(x\)</span> розташовані у порядку зростання; тобто <span>\(x_i &lt; x_{i+1}\)</span>, і нехай <span>\(x\)</span> буде точкою такою, що <span>\(x_i &lt; x &lt; x_{i+1}\)</span>. Тоді лінійна інтерполяція в точці <span>\(x\)</span> дорівнює:
$<span>\(
\hat{y}(x) = y_i + \frac{(y_{i+1} - y_{i})(x - x_{i})}{(x_{i+1} - x_{i})}.\)</span>$</p>
<p>**СПРОБУЙТЕ!** Знайдіть лінійну інтерполяцію в точці <span>\(x=1.5\)</span> на основі даних x = [0, 1, 2], y = [1, 3, 2]. Перевірте результат за допомогою функції *interp1d* з бібліотеки scipy.</p>
<p>Оскільки <span>\(1 &lt; x &lt; 2\)</span>, ми використовуємо другу та третю точки даних для обчислення лінійної інтерполяції. Підставляючи відповідні значення, отримуємо
$<span>\(
\hat{y}(x) = y_i + \frac{(y_{i+1} - y_{i})(x - x_{i})}{(x_{i+1} - x_{i})} = 3 + \frac{(2 - 3)(1.5 - 1)}{(2 - 1)} = 2.5
\)</span>$</p>


<pre><span></span><span>from</span> <span>scipy.interpolate</span> <span>import</span> <span>interp1d</span>
<span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>

<span>plt</span><span>.</span><span>style</span><span>.</span><span>use</span><span>(</span><span>'seaborn-poster'</span><span>)</span>
</pre>





<pre><span></span><span>x</span> <span>=</span> <span>[</span><span>0</span><span>,</span> <span>1</span><span>,</span> <span>2</span><span>]</span>
<span>y</span> <span>=</span> <span>[</span><span>1</span><span>,</span> <span>3</span><span>,</span> <span>2</span><span>]</span>

<span>f</span> <span>=</span> <span>interp1d</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>)</span>
<span>y_hat</span> <span>=</span> <span>f</span><span>(</span><span>1.5</span><span>)</span>
<span>print</span><span>(</span><span>y_hat</span><span>)</span>
</pre>



<pre><span></span>2.5
</pre>





<pre><span></span><span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span><span>8</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>'-ob'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>1.5</span><span>,</span> <span>y_hat</span><span>,</span> <span>'ro'</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>'Лінійна інтерполяція в точці x = 1.5'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'x'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'y'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="../_images/chapter17.02-Linear-Interpolation_6_0.png" src="../_images/chapter17.02-Linear-Interpolation_6_0.png"/>
