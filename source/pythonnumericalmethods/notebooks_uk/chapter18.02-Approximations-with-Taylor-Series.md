<h1>Апроксимації за допомогою рядів Тейлора<a href="#approximations-with-taylor-series" title="Постійне посилання на цей заголовок"></a></h1>
<p>Очевидно, що виражати функції як нескінченні суми не є корисним, оскільки ми навіть не можемо обчислити їх таким чином. Однак часто корисно апроксимувати функції за допомогою <span>\(\textbf{\)</span>N-го<span>\( порядку наближення ряду Тейлора}\)</span> функції, що є усіченням її розкладу Тейлора при деякому <span>\(n = N\)</span>. Ця техніка особливо потужна, коли існує точка, навколо якої ми маємо знання про функцію для всіх її похідних. Наприклад, якщо ми візьмемо розклад Тейлора <span>\(e^x\)</span> навколо <span>\(a = 0\)</span>, тоді <span>\(f^{(n)}(a) = 1\)</span> для всіх <span>\(n\)</span>, нам навіть не потрібно обчислювати похідні в розкладі Тейлора, щоб апроксимувати <span>\(e^x\)</span>!</p>
<p><strong>СПРОБУЙТЕ!</strong> Використайте Python для побудови графіка функції синуса разом з апроксимаціями рядами Тейлора першого, третього, п'ятого та сьомого порядків. Зауважте, що це відповідає нульовому-третьому порядку у формулі, наведеній раніше.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
<span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>

<span>plt</span><span>.</span><span>style</span><span>.</span><span>use</span><span>(</span><span>'seaborn-poster'</span><span>)</span>
</pre>





<pre><span></span><span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>-</span><span>np</span><span>.</span><span>pi</span><span>,</span> <span>np</span><span>.</span><span>pi</span><span>,</span> <span>200</span><span>)</span>
<span>y</span> <span>=</span> <span>np</span><span>.</span><span>zeros</span><span>(</span><span>len</span><span>(</span><span>x</span><span>))</span>

<span>labels</span> <span>=</span> <span>[</span><span>'Перший порядок'</span><span>,</span> <span>'Третій порядок'</span><span>,</span> <span>'П'</span><span>ятий</span> <span>порядок</span><span>'</span><span>,</span> <span>'Сьомий порядок'</span><span>]</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span><span>8</span><span>))</span>
<span>for</span> <span>n</span><span>,</span> <span>label</span> <span>in</span> <span>zip</span><span>(</span><span>range</span><span>(</span><span>4</span><span>),</span> <span>labels</span><span>):</span>
    <span>y</span> <span>=</span> <span>y</span> <span>+</span> <span>((</span><span>-</span><span>1</span><span>)</span><span>**</span><span>n</span> <span>*</span> <span>(</span><span>x</span><span>)</span><span>**</span><span>(</span><span>2</span><span>*</span><span>n</span><span>+</span><span>1</span><span>))</span> <span>/</span> <span>np</span><span>.</span><span>math</span><span>.</span><span>factorial</span><span>(</span><span>2</span><span>*</span><span>n</span><span>+</span><span>1</span><span>)</span>
    <span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span><span>y</span><span>,</span> <span>label</span> <span>=</span> <span>label</span><span>)</span>

<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>x</span><span>),</span> <span>'k'</span><span>,</span> <span>label</span> <span>=</span> <span>'Аналітична'</span><span>)</span>
<span>plt</span><span>.</span><span>grid</span><span>()</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>'Апроксимації рядами Тейлора різних порядків'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'x'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'y'</span><span>)</span>
<span>plt</span><span>.</span><span>legend</span><span>()</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="../_images/chapter18.02-Approximations-with-Taylor-Series_6_0.png" src="../_images/chapter18.02-Approximations-with-Taylor-Series_6_0.png"/>


<p>Як бачите, апроксимація швидко наближається до аналітичної функції, навіть для <span>\(x\)</span>, що не знаходиться близько до <span>\(a=0\)</span>. Зауважте, що у наведеному вище коді ми також використали нову функцію - <em>zip</em>, яка дозволяє нам перебирати два параметри <em>range(4)</em> та <em>labels</em> і використовувати їх у нашому графіку.</p>
<p><strong>СПРОБУЙТЕ!</strong> Обчисліть апроксимацію ряду Тейлора сьомого порядку для <span>\(sin(x)\)</span> навколо <span>\(a=0\)</span> в точці <span>\(x=\pi/2\)</span>. Порівняйте отримане значення з правильним значенням, 1.</p>


<pre><span></span><span>x</span> <span>=</span> <span>np</span><span>.</span><span>pi</span><span>/</span><span>2</span>
<span>y</span> <span>=</span> <span>0</span>

<span>for</span> <span>n</span> <span>in</span> <span>range</span><span>(</span><span>4</span><span>):</span>
    <span>y</span> <span>=</span> <span>y</span> <span>+</span> <span>((</span><span>-</span><span>1</span><span>)</span><span>**</span><span>n</span> <span>*</span> <span>(</span><span>x</span><span>)</span><span>**</span><span>(</span><span>2</span><span>*</span><span>n</span><span>+</span><span>1</span><span>))</span> <span>/</span> <span>np</span><span>.</span><span>math</span><span>.</span><span>factorial</span><span>(</span><span>2</span><span>*</span><span>n</span><span>+</span><span>1</span><span>)</span>
    
<span>print</span><span>(</span><span>y</span><span>)</span>
</pre>



<pre><span></span>0.9998431013994987
</pre>



<p>Апроксимація ряду Тейлора сьомого порядку дуже близька до теоретичного значення функції, навіть якщо вона обчислюється далеко від точки, навколо якої був обчислений ряд Тейлора (тобто <span>\(x = \pi/2\)</span> та <span>\(a = 0\)</span>).</p>
<p>Найпоширенішою апроксимацією ряду Тейлора є апроксимація першого порядку, або <strong>лінійна апроксимація</strong>. Інтуїтивно, для "гладких" функцій лінійна апроксимація функції навколо точки <span>\(a\)</span> може бути зроблена настільки точною, наскільки ви бажаєте, за умови, що ви залишаєтеся достатньо близько до <span>\(a\)</span>. Іншими словами, "гладкі" функції все більше і більше схожі на пряму, чим більше ви наближаєтеся до будь-якої точки. Цей факт зображено на наступному малюнку, де ми будуємо послідовні рівні масштабування гладкої функції, щоб проілюструвати лінійну природу функцій локально. Лінійні апроксимації є корисними інструментами при аналізі складних функцій локально.</p>


<pre><span></span><span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>3</span><span>,</span> <span>30</span><span>)</span>
<span>y</span> <span>=</span> <span>np</span><span>.</span><span>exp</span><span>(</span><span>x</span><span>)</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>14</span><span>,</span> <span>4.5</span><span>))</span>
<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>1</span><span>,</span> <span>3</span><span>,</span> <span>1</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>)</span>
<span>plt</span><span>.</span><span>grid</span><span>()</span>
<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>1</span><span>,</span> <span>3</span><span>,</span> <span>2</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>)</span>
<span>plt</span><span>.</span><span>grid</span><span>()</span>
<span>plt</span><span>.</span><span>xlim</span><span>(</span><span>1.7</span><span>,</span> <span>2.3</span><span>)</span>
<span>plt</span><span>.</span><span>ylim</span><span>(</span><span>5</span><span>,</span> <span>10</span><span>)</span>
<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>1</span><span>,</span> <span>3</span><span>,</span> <span>3</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>)</span>
<span>plt</span><span>.</span><span>grid</span><span>()</span>
<span>plt</span><span>.</span><span>xlim</span><span>(</span><span>1.92</span><span>,</span> <span>2.08</span><span>)</span>
<span>plt</span><span>.</span><span>ylim</span><span>(</span><span>6.6</span><span>,</span> <span>8.2</span><span>)</span>
<span>plt</span><span>.</span><span>tight_layout</span><span>()</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="../_images/chapter18.02-Approximations-with-Taylor-Series_10_0.png" src="../_images/chapter18.02-Approximations-with-Taylor-Series_10_0.png"/>


<p><strong>СПРОБУЙТЕ!</strong> Візьміть лінійну апроксимацію для <span>\(e^x\)</span> навколо точки <span>\(a = 0\)</span>. Використайте лінійну апроксимацію для <span>\(e^x\)</span>, щоб апроксимувати значення <span>\(e^1\)</span> та <span>\(e^{0.01}\)</span>. Використайте функцію Numpy <em>exp</em> для обчислення <em>exp(1)</em> та <em>exp(0.01)</em> для порівняння.</p>
<p>Лінійна апроксимація <span>\(e^x\)</span> навколо <span>\(a = 0\)</span> дорівнює <span>\(1 + x\)</span>.</p>
<p>Функція Numpy <em>exp</em> дає наступне:</p>


<pre><span></span><span>np</span><span>.</span><span>exp</span><span>(</span><span>1</span><span>)</span>
</pre>



<pre><span></span>2.718281828459045
</pre>





<pre><span></span><span>np</span><span>.</span><span>exp</span><span>(</span><span>0.01</span><span>)</span>
</pre>



<pre><span></span>1.010050167084168
</pre>



<p>Лінійна апроксимація <span>\(e^1\)</span> дорівнює 2, що є неточним, а лінійна апроксимація <span>\(e^{0.01}\)</span> дорівнює 1.01, що є дуже хорошим результатом. Цей приклад ілюструє, як лінійна апроксимація наближається до функцій поблизу точки, навколо якої береться апроксимація.</p>
