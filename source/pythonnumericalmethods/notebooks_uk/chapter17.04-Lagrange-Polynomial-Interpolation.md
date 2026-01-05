<h1>Інтерполяція поліномом Лагранжа<a href="#lagrange-polynomial-interpolation" title="Постійне посилання на цей заголовок"></a></h1>
<p>Замість того, щоб знаходити кубічні поліноми між послідовними парами точок даних, <strong>інтерполяція поліномом Лагранжа</strong> знаходить єдиний поліном, який проходить через усі точки даних. Цей поліном називається **поліномом Лагранжа**, <span>\(L(x)\)</span>, і як інтерполяційна функція, він повинен мати властивість <span>\(L(x_i) = y_i\)</span> для кожної точки в наборі даних. Для обчислення поліномів Лагранжа корисно записати їх як лінійну комбінацію **базисних поліномів Лагранжа**, <span>\(P_i(x)\)</span>, де
$<span>\(
P_i(x) = \prod_{j = 1, j\ne i}^n\frac{x - x_j}{x_i - x_j},
\)</span>$</p>
<p>і
$<span>\(
L(x) = \sum_{i = 1}^n y_i P_i(x).
\)</span>$</p>
<p>Тут <span>\(\prod\)</span> означає "добуток" або "перемножити".</p>
<p>Ви помітите, що за побудовою, <span>\(P_i(x)\)</span> має властивість, що <span>\(P_i(x_j) = 1\)</span> коли <span>\(i = j\)</span> і <span>\(P_i(x_j) = 0\)</span> коли <span>\(i \ne j\)</span>. Оскільки <span>\(L(x)\)</span> є сумою цих поліномів, ви можете спостерігати, що <span>\(L(x_i) = y_i\)</span> для кожної точки, саме так, як бажано.</p>
<p><strong>СПРОБУЙТЕ!</strong> Знайдіть базисні поліноми Лагранжа для набору даних <em>x = [0, 1, 2]</em> та <em>y = [1, 3, 2]</em>. Побудуйте графік кожного полінома та перевірте властивість, що <span>\(P_i(x_j) = 1\)</span> коли <span>\(i = j\)</span> і <span>\(P_i(x_j) = 0\)</span> коли <span>\(i \ne j\)</span>.</p>

\[\begin{eqnarray*}
P_1(x) &amp;=&amp; \frac{(x - x_2)(x - x_3)}{(x_1-x_2)(x_1-x_3)} = \frac{(x - 1)(x - 2)}{(0-1)(0-2)} = \frac{1}{2}(x^2 - 3x + 2),\\
P_2(x) &amp;=&amp; \frac{(x - x_1)(x - x_3)}{(x_2-x_1)(x_2-x_3)} = \frac{(x - 0)(x - 2)}{(1-0)(1-2)} = -x^2 + 2x,\\
P_3(x) &amp;=&amp; \frac{(x - x_1)(x - x_2)}{(x_3-x_1)(x_3-x_2)} = \frac{(x - 0)(x - 1)}{(2-0)(2-1)} = \frac{1}{2}(x^2 - x).
\end{eqnarray*}\]


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
<span>import</span> <span>numpy.polynomial.polynomial</span> <span>as</span> <span>poly</span>
<span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>

<span>plt</span><span>.</span><span>style</span><span>.</span><span>use</span><span>(</span><span>'seaborn-poster'</span><span>)</span>
</pre>





<pre><span></span><span>x</span> <span>=</span> <span>[</span><span>0</span><span>,</span> <span>1</span><span>,</span> <span>2</span><span>]</span>
<span>y</span> <span>=</span> <span>[</span><span>1</span><span>,</span> <span>3</span><span>,</span> <span>2</span><span>]</span>
<span>P1_coeff</span> <span>=</span> <span>[</span><span>1</span><span>,</span><span>-</span><span>1.5</span><span>,</span><span>.</span><span>5</span><span>]</span>
<span>P2_coeff</span> <span>=</span> <span>[</span><span>0</span><span>,</span> <span>2</span><span>,</span><span>-</span><span>1</span><span>]</span>
<span>P3_coeff</span> <span>=</span> <span>[</span><span>0</span><span>,</span><span>-.</span><span>5</span><span>,</span><span>.</span><span>5</span><span>]</span>

<span># get the polynomial function</span>
<span>P1</span> <span>=</span> <span>poly</span><span>.</span><span>Polynomial</span><span>(</span><span>P1_coeff</span><span>)</span>
<span>P2</span> <span>=</span> <span>poly</span><span>.</span><span>Polynomial</span><span>(</span><span>P2_coeff</span><span>)</span>
<span>P3</span> <span>=</span> <span>poly</span><span>.</span><span>Polynomial</span><span>(</span><span>P3_coeff</span><span>)</span>

<span>x_new</span> <span>=</span> <span>np</span><span>.</span><span>arange</span><span>(</span><span>-</span><span>1.0</span><span>,</span> <span>3.1</span><span>,</span> <span>0.1</span><span>)</span>

<span>fig</span> <span>=</span> <span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span><span>8</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x_new</span><span>,</span> <span>P1</span><span>(</span><span>x_new</span><span>),</span> <span>'b'</span><span>,</span> <span>label</span> <span>=</span> <span>'P1'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x_new</span><span>,</span> <span>P2</span><span>(</span><span>x_new</span><span>),</span> <span>'r'</span><span>,</span> <span>label</span> <span>=</span> <span>'P2'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x_new</span><span>,</span> <span>P3</span><span>(</span><span>x_new</span><span>),</span> <span>'g'</span><span>,</span> <span>label</span> <span>=</span> <span>'P3'</span><span>)</span>

<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>np</span><span>.</span><span>ones</span><span>(</span><span>len</span><span>(</span><span>x</span><span>)),</span> <span>'ko'</span><span>,</span> <span>x</span><span>,</span> <span>np</span><span>.</span><span>zeros</span><span>(</span><span>len</span><span>(</span><span>x</span><span>)),</span> <span>'ko'</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>'Lagrange Basis Polynomials'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'x'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'y'</span><span>)</span>
<span>plt</span><span>.</span><span>grid</span><span>()</span>
<span>plt</span><span>.</span><span>legend</span><span>()</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="../_images/chapter17.04-Lagrange-Polynomial-Interpolation_5_0.png" src="../_images/chapter17.04-Lagrange-Polynomial-Interpolation_5_0.png"/>


<p><strong>СПРОБУЙТЕ!</strong> Для попереднього прикладу обчисліть та побудуйте графік полінома Лагранжа і перевірте, що він проходить через кожну з точок даних.</p>


<pre><span></span><span>L</span> <span>=</span> <span>P1</span> <span>+</span> <span>3</span><span>*</span><span>P2</span> <span>+</span> <span>2</span><span>*</span><span>P3</span>

<span>fig</span> <span>=</span> <span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span><span>8</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x_new</span><span>,</span> <span>L</span><span>(</span><span>x_new</span><span>),</span> <span>'b'</span><span>,</span> <span>x</span><span>,</span> <span>y</span><span>,</span> <span>'ro'</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>'Lagrange Polynomial'</span><span>)</span>
<span>plt</span><span>.</span><span>grid</span><span>()</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'x'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'y'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="../_images/chapter17.04-Lagrange-Polynomial-Interpolation_7_0.png" src="../_images/chapter17.04-Lagrange-Polynomial-Interpolation_7_0.png"/>


<p><strong>УВАГА!</strong> Інтерполяційні поліноми Лагранжа, визначені за межами області інтерполяції, тобто за межами інтервалу <span>\([x_1,x_n]\)</span>, будуть дуже швидко і необмежено зростати за межами цієї області. Це не є бажаною властивістю, оскільки загалом це не відповідає поведінці вихідних даних. Таким чином, інтерполяцію Лагранжа ніколи не слід використовувати для інтерполяції за межами цієї області.</p>

<h2>Використання функції lagrange зі scipy<a href="#using-lagrange-from-scipy" title="Постійне посилання на цей заголовок"></a></h2>
<p>Замість того, щоб обчислювати все з нуля, у scipy ми можемо використовувати функцію <em>lagrange</em> безпосередньо для інтерполяції даних. Розглянемо наведений вище приклад.</p>


<pre><span></span><span>from</span> <span>scipy.interpolate</span> <span>import</span> <span>lagrange</span>
</pre>





<pre><span></span><span>f</span> <span>=</span> <span>lagrange</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>)</span>
</pre>





<pre><span></span><span>fig</span> <span>=</span> <span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span><span>8</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x_new</span><span>,</span> <span>f</span><span>(</span><span>x_new</span><span>),</span> <span>'b'</span><span>,</span> <span>x</span><span>,</span> <span>y</span><span>,</span> <span>'ro'</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>'Lagrange Polynomial'</span><span>)</span>
<span>plt</span><span>.</span><span>grid</span><span>()</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'x'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'y'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="../_images/chapter17.04-Lagrange-Polynomial-Interpolation_12_0.png" src="../_images/chapter17.04-Lagrange-Polynomial-Interpolation_12_0.png"/>
