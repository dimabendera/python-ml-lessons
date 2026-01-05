<h1>Обчислення інтегралів у Python<a href="#computing-integrals-in-python" title="Постійне посилання на цей заголовок"></a></h1>
<p>Підпакет <span>\(scipy.integrate\)</span> має кілька функцій для обчислення інтегралів. Функція <span>\(trapz\)</span> приймає як вхідні аргументи масив значень функції <span>\(f\)</span>, обчислених на числовій сітці <span>\(x\)</span>.</p>
<p><strong>СПРОБУЙТЕ!</strong> Використайте функцію <span>\(trapz\)</span> для апроксимації <span>\(\int_{0}^{\pi}\text{sin}(x)dx\)</span> для 11 рівновіддалених точок на всьому інтервалі. Порівняйте це значення з тим, що було обчислено в попередньому прикладі за допомогою правила трапецій.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
<span>from</span> <span>scipy.integrate</span> <span>import</span> <span>trapz</span>

<span>a</span> <span>=</span> <span>0</span>
<span>b</span> <span>=</span> <span>np</span><span>.</span><span>pi</span>
<span>n</span> <span>=</span> <span>11</span>
<span>h</span> <span>=</span> <span>(</span><span>b</span> <span>-</span> <span>a</span><span>)</span> <span>/</span> <span>(</span><span>n</span> <span>-</span> <span>1</span><span>)</span>
<span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>a</span><span>,</span> <span>b</span><span>,</span> <span>n</span><span>)</span>
<span>f</span> <span>=</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>x</span><span>)</span>

<span>I_trapz</span> <span>=</span> <span>trapz</span><span>(</span><span>f</span><span>,</span><span>x</span><span>)</span>
<span>I_trap</span> <span>=</span> <span>(</span><span>h</span><span>/</span><span>2</span><span>)</span><span>*</span><span>(</span><span>f</span><span>[</span><span>0</span><span>]</span> <span>+</span> <span>2</span> <span>*</span> <span>sum</span><span>(</span><span>f</span><span>[</span><span>1</span><span>:</span><span>n</span><span>-</span><span>1</span><span>])</span> <span>+</span> <span>f</span><span>[</span><span>n</span><span>-</span><span>1</span><span>])</span>

<span>print</span><span>(</span><span>I_trapz</span><span>)</span>
<span>print</span><span>(</span><span>I_trap</span><span>)</span>
</pre>



<pre><span></span>1.9835235375094542
1.9835235375094546
</pre>



<p>Іноді нам потрібно знати наближений кумулятивний (накопичувальний) інтеграл. Тобто, ми хочемо знайти <span>\(F(X) = \int_{x_0}^X f(x) dx\)</span>. Для цієї мети корисно використовувати функцію <span>\(cumtrapz\)</span>, яка приймає ті ж вхідні аргументи, що й <span>\(trapz\)</span>.</p>
<p><strong>СПРОБУЙТЕ!</strong> Використайте функцію <span>\(cumtrapz\)</span> для апроксимації кумулятивного інтеграла <span>\(f(x) = \text{sin}(x)\)</span> від <span>\(0\)</span> до <span>\(\pi\)</span> з кроком дискретизації 0.01. Точний розв'язок цього інтеграла — <span>\(F(x) = 1 - \text{cos}(x)\)</span>. Побудуйте графіки результатів.</p>


<pre><span></span><span>from</span> <span>scipy.integrate</span> <span>import</span> <span>cumtrapz</span>
<span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>

<span>%</span><span>matplotlib</span> inline
<span>plt</span><span>.</span><span>style</span><span>.</span><span>use</span><span>(</span><span>'seaborn-poster'</span><span>)</span>

<span>x</span> <span>=</span> <span>np</span><span>.</span><span>arange</span><span>(</span><span>0</span><span>,</span> <span>np</span><span>.</span><span>pi</span><span>,</span> <span>0.01</span><span>)</span>
<span>F_exact</span> <span>=</span> <span>-</span><span>np</span><span>.</span><span>cos</span><span>(</span><span>x</span><span>)</span>
<span>F_approx</span> <span>=</span> <span>cumtrapz</span><span>(</span><span>np</span><span>.</span><span>sin</span><span>(</span><span>x</span><span>),</span> <span>x</span><span>)</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span><span>6</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>F_exact</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>[</span><span>1</span><span>::],</span> <span>F_approx</span><span>)</span>
<span>plt</span><span>.</span><span>grid</span><span>()</span>
<span>plt</span><span>.</span><span>tight_layout</span><span>()</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>'$F(x) = \int_0^</span><span>{x}</span><span> sin(y) dy$'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'x'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'f(x)'</span><span>)</span>
<span>plt</span><span>.</span><span>legend</span><span>([</span><span>'Exact with Offset'</span><span>,</span> <span>'Approx'</span><span>])</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="../_images/chapter21.05-Computing-Integrals-in-Python_6_0.png" src="../_images/chapter21.05-Computing-Integrals-in-Python_6_0.png"/>


<p>Функція <span>\(quad(f,a,b)\)</span> використовує іншу схему чисельного інтегрування для апроксимації інтегралів. <span>\(quad\)</span> інтегрує функцію, визначену об'єктом-функцією <span>\(f\)</span>, від <span>\(a\)</span> до <span>\(b\)</span>.</p>
<p><strong>СПРОБУЙТЕ!</strong> Використайте функцію <span>\(integrate.quad\)</span> для обчислення <span>\(\int_{0}^{\pi} \text{sin}(x)dx\)</span>. Порівняйте вашу відповідь з правильною відповіддю 2.</p>


<pre><span></span><span>from</span> <span>scipy.integrate</span> <span>import</span> <span>quad</span>

<span>I_quad</span><span>,</span> <span>est_err_quad</span> <span>=</span> \
          <span>quad</span><span>(</span><span>np</span><span>.</span><span>sin</span><span>,</span> <span>0</span><span>,</span> <span>np</span><span>.</span><span>pi</span><span>)</span>
<span>print</span><span>(</span><span>I_quad</span><span>)</span>
<span>err_quad</span> <span>=</span> <span>2</span> <span>-</span> <span>I_quad</span>
<span>print</span><span>(</span><span>est_err_quad</span><span>,</span> <span>err_quad</span><span>)</span>
</pre>



<pre><span></span>2.0
2.220446049250313e-14 0.0
</pre>
