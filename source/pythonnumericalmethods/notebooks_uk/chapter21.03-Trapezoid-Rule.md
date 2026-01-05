<h1>Правило трапецій<a href="#trapezoid-rule" title="Постійне посилання на цей заголовок"></a></h1>
<p><strong>Правило трапецій</strong> вписує трапецію в кожен підінтервал і підсумовує площі трапецій для наближення загального інтеграла. Це наближення інтеграла до довільної функції показано на наступному рисунку. Для кожного підінтервалу Правило трапецій обчислює площу трапеції з вершинами в <span>\((x_i, 0), (x_{i+1}, 0), (x_i, f(x_i))\)</span>, та <span>\((x_{i+1}, f(x_{i+1}))\)</span>, що становить <span>\(h\frac{f(x_i) + f(x_{i+1})}{2}\)</span>. Таким чином, Правило трапецій наближає інтеграли згідно з виразом</p>

\[\int_a^b f(x) dx \approx \sum_{i=0}^{n-1} h\frac{f(x_i) + f(x_{i+1})}{2}.\]

<p><strong>СПРОБУЙТЕ!</strong> Ви можете помітити, що Правило трапецій "подвійно враховує" більшість членів у ряді. Щоб проілюструвати цей факт, розгляньте розширення Правила трапецій:</p>

\[\begin{eqnarray*}\sum_{i=0}^{n-1} h\frac{f(x_i) + f(x_{i+1})}{2} &amp;=&amp; \frac{h}{2} \left[(f(x_0) + f(x_1)) + (f(x_1) + f(x_2)) + (f(x_2)\right. \\
&amp;&amp;\left. + f(x_3)) + \cdots + (f(x_{n-1}) + f(x_n))\right].\end{eqnarray*}\]
<p>З обчислювальної точки зору, це багато зайвих додавань та викликів <span>\(f(x)\)</span>, ніж насправді необхідно. Ми можемо бути більш обчислювально ефективними, використовуючи наступний вираз.</p>

\[\int_a^b f(x) dx \approx \frac{h}{2} \left(f(x_0) + 2 \left(\sum_{i=1}^{n-1} f(x_i)\right) + f(x_n)\right).\]
<p>Щоб визначити точність наближення Правила трапецій, ми спочатку розкладаємо <span>\(f(x)\)</span> в ряд Тейлора навколо <span>\(y_i = \frac{x_{i+1} + x_i}{2}\)</span>, що є середньою точкою між <span>\(x_i\)</span> та <span>\(x_{i+1}\)</span>. Це розкладання в ряд Тейлора має вигляд</p>

\[f(x) = f(y_i) + f^{\prime}(y_i)(x - y_i) + \frac{f''(y_i)(x - y_i)^2}{2!} + \cdots\]
<p>Обчислення ряду Тейлора в точках <span>\(x_i\)</span> та <span>\(x_{i+1}\)</span>, а також зауваження, що <span>\(x_i - y_i = -\frac{h}{2}\)</span> та <span>\(x_{i+1} - y_i = \frac{h}{2}\)</span>, дає наступні вирази:</p>

\[f(x_i) = f(y_i) - \frac{hf^{\prime}(y_i)}{2} + \frac{h^2f''(y_i)}{8} - \cdots\]
<p>та</p>

\[f(x_{i+1}) = f(y_i) + \frac{hf^{\prime}(y_i)}{2} + \frac{h^2f''(y_i)}{8} + \cdots.\]
<p>Взяття середнього значення цих двох виразів дає новий вираз,</p>

\[\frac{f(x_{i+1})+f(x_i)}{2} = f(y_i) + O(h^2).\]
<p>Розв'язання цього виразу відносно <span>\(f(y_i)\)</span> дає</p>

\[f(y_i) = \frac{f(x_{i+1})+f(x_i)}{2} + O(h^2).\]
<p>Тепер, повертаючись до розкладання <span>\(f(x)\)</span> в ряд Тейлора, інтеграл від <span>\(f(x)\)</span> по підінтервалу становить</p>

\[\int_{x_i}^{x_{i+1}} f(x) dx = \int_{x_i}^{x_{i+1}} \left(f(y_i) + f^{\prime}(y_i)(x - y_i) + \frac{f''(y_i)(x - y_i)^2}{2!} + \cdots\right) dx.\]
<p>Розподіл інтеграла дає вираз</p>

\[\int_{x_i}^{x_{i+1}} f(x) dx = \int_{x_i}^{x_{i+1}} f(y_i) dx + \int_{x_i}^{x_{i+1}} f^{\prime}(y_i)(x - y_i)dx + \int_{x_i}^{x_{i+1}} \frac{f''(y_i)(x - y_i)^2}{2!} dx + \cdots\]
<p>Оскільки <span>\(x_i\)</span> та <span>\(x_{i+1}\)</span> симетричні відносно <span>\(y_i\)</span>, інтеграли непарних степенів <span>\((x - y_i)^p\)</span> зникають, а парні степені зводяться до множника <span>\(h^{p+1}\)</span>.</p>

\[\int_{x_i}^{x_{i+1}} f(x) dx = hf(y_i) + O(h^3).\]
<p>Тепер, якщо ми підставимо <span>\(f(y_i)\)</span> виразом, отриманим явно через <span>\(f(x_i)\)</span> та <span>\(f(x_{i+1})\)</span>, ми отримаємо</p>

\[\int_{x_i}^{x_{i+1}} f(x) dx = h \left(\frac{f(x_{i+1})+f(x_i)}{2} + O(h^2)\right) + O(h^3), \]
<p>що еквівалентно</p>

\[h \left(\frac{f(x_{i+1})+f(x_i)}{2}\right) + hO(h^2) + O(h^3)\]
<p>і, отже,</p>

\[\int_{x_i}^{x_{i+1}} f(x) dx = h \left(\frac{f(x_{i+1})+f(x_i)}{2}\right) + O(h^3).\]
<p>Оскільки <span>\(\frac{h}{2}(f(x_{i+1}) + f(x_i))\)</span> є наближенням інтеграла за Правилом трапецій для підінтервалу, воно є <span>\(O(h^3)\)</span> для одного підінтервалу та <span>\(O(h^2)\)</span> для всього інтервалу.</p>
<p><strong>СПРОБУЙТЕ!</strong> Використайте Правило трапецій для наближення <span>\(\int_0^{\pi} \sin(x) dx\)</span> з 11 рівномірно розташованими точками сітки по всьому інтервалу. Порівняйте це значення з точним значенням 2.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>

<span>a</span> <span>=</span> <span>0</span>
<span>b</span> <span>=</span> <span>np</span><span>.</span><span>pi</span>
<span>n</span> <span>=</span> <span>11</span>
<span>h</span> <span>=</span> <span>(</span><span>b</span> <span>-</span> <span>a</span><span>)</span> <span>/</span> <span>(</span><span>n</span> <span>-</span> <span>1</span><span>)</span>
<span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>a</span><span>,</span> <span>b</span><span>,</span> <span>n</span><span>)</span>
<span>f</span> <span>=</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>x</span><span>)</span>

<span>I_trap</span> <span>=</span> <span>(</span><span>h</span><span>/</span><span>2</span><span>)</span><span>*</span><span>(</span><span>f</span><span>[</span><span>0</span><span>]</span> <span>+</span> \
          <span>2</span> <span>*</span> <span>sum</span><span>(</span><span>f</span><span>[</span><span>1</span><span>:</span><span>n</span><span>-</span><span>1</span><span>])</span> <span>+</span> <span>f</span><span>[</span><span>n</span><span>-</span><span>1</span><span>])</span>
<span>err_trap</span> <span>=</span> <span>2</span> <span>-</span> <span>I_trap</span>

<span>print</span><span>(</span><span>I_trap</span><span>)</span>
<span>print</span><span>(</span><span>err_trap</span><span>)</span>
</pre>



<pre><span></span>1.9835235375094546
0.01647646249054535
</pre>
