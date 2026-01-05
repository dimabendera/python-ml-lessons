<h1>Інтеграл Рімана<a href="#riemanns-integral" title="Постійне посилання на цей заголовок"></a></h1>
<p>Найпростіший метод апроксимації інтегралів полягає в сумуванні площ прямокутників, визначених для кожного підінтервалу. Ширина прямокутника дорівнює <span>\(x_{i+1} - x_i = h\)</span>, а висота визначається значенням функції <span>\(f(x)\)</span> для деякого <span>\(x\)</span> у підінтервалі. Очевидним вибором для висоти є значення функції в лівій кінцевій точці, <span>\(x_i\)</span>, або в правій кінцевій точці, <span>\(x_{i+1}\)</span>, оскільки ці значення можна використовувати, навіть якщо сама функція невідома. Цей метод дає апроксимацію <strong>інтеграла Рімана</strong>, яка має вигляд</p>

\[\int_a^b f(x) dx \approx \sum_{i = 0}^{n-1} hf(x_i),\]
<p>або</p>

\[\int_a^b f(x) dx \approx \sum_{i = 1}^{n} hf(x_i),\]
<p>залежно від того, чи обрана ліва, чи права кінцева точка.</p>
<p>Як і у випадку з чисельним диференціюванням, ми хочемо охарактеризувати, як покращується точність зі зменшенням <span>\(h\)</span>. Щоб визначити цю характеристику, ми спочатку перепишемо інтеграл <span>\(f(x)\)</span> над довільним підінтервалом у термінах ряду Тейлора. Ряд Тейлора для <span>\(f(x)\)</span> навколо <span>\(a = x_i\)</span> має вигляд</p>

\[f(x) = f(x_i) + f^{\prime}(x_i)(x-x_i) + \cdots\]
<p>Отже,</p>

\[\int_{x_i}^{x_{i+1}} f(x) dx = \int_{x_i}^{x_{i+1}} (f(x_i) + f^{\prime}(x_i)(x-x_i) + \cdots)\ dx\]
<p>шляхом підстановки ряду Тейлора для функції. Оскільки інтеграл є дистрибутивним, ми можемо перегрупувати праву частину в таку форму:</p>

\[\int_{x_i}^{x_{i+1}} f(x_i) dx + \int_{x_i}^{x_{i+1}} f^{\prime}(x_i)(x-x_i)dx + \cdots.\\]
<p>Розв'язання кожного інтеграла окремо дає апроксимацію</p>

\[\int_{x_i}^{x_{i+1}} f(x) dx = hf(x_i) + \frac{h^2}{2}f^{\prime}(x_i) + O(h^3),\]
<p>що є просто</p>

\[\int_{x_i}^{x_{i+1}} f(x) dx = hf(x_i) + O(h^2).\]
<p>Оскільки член <span>\(hf(x_i)\)</span> є нашою апроксимацією інтеграла Рімана для одного підінтервалу, апроксимація інтеграла Рімана над одним інтервалом є <span>\(O(h^2)\)</span>.</p>
<p>Якщо ми підсумуємо похибку <span>\(O(h^2)\)</span> по всій сумі Рімана, ми отримаємо <span>\(nO(h^2)\)</span>. Зв'язок між <span>\(n\)</span> і <span>\(h\)</span> такий:</p>

\[h = \frac{b - a}{n},\]
<p>і тому наша загальна похибка стає <span>\(\frac{b - a}{h}O(h^2) = O(h)\)</span> на всьому інтервалі. Таким чином, загальна точність становить <span>\(O(h)\)</span>.</p>
<p><strong>Правило середньої точки</strong> (або правило прямокутників за середніми точками) приймає висоту прямокутника на кожному підінтервалі як значення функції в середній точці між <span>\(x_i\)</span> та <span>\(x_{i+1}\)</span>, яку для компактності ми позначаємо як <span>\(y_i = \frac{x_{i+1} + x_i}{2}\)</span>. Правило середньої точки стверджує:</p>

\[\int_a^b f(x)dx \approx \sum_{i = 0}^{n-1} hf(y_i).\]
<p>Аналогічно до інтеграла Рімана, ми беремо ряд Тейлора для <span>\(f(x)\)</span> навколо <span>\(y_i\)</span>, який має вигляд</p>

\[f(x) = f(y_i) + f^{\prime}(y_i)(x - y_i) + \frac{f''(y_i)(x - y_i)^2}{2!} + \cdots\]
<p>Тоді інтеграл над підінтервалом дорівнює</p>

\[\int_{x_i}^{x_{i+1}} f(x) dx= \int_{x_i}^{x_{i+1}} \left(f(y_i) + f^{\prime}(y_i)(x - y_i) + \frac{f''(y_i)(x - y_i)^2}{2!} + \cdots\right) dx,\]
<p>що розподіляється на</p>

\[\int_{x_i}^{x_{i+1}} f(x) dx= \int_{x_i}^{x_{i+1}} f(y_i)dx + \int_{x_i}^{x_{i+1}} f^{\prime}(y_i)(x - y_i)dx + \int_{x_i}^{x_{i+1}} \frac{f''(y_i)(x - y_i)^2}{2!}dx + \cdots.\]
<p>Враховуючи, що <span>\(x_i\)</span> та <span>\(x_{i+1}\)</span> симетричні відносно <span>\(y_i\)</span>, тоді <span>\(\int_{x_i}^{x_{i+1}} f^{\prime}(y_i)(x - y_i)dx = 0\)</span>. Це справедливо для інтеграла <span>\((x - y_i)^p\)</span> для будь-якого непарного <span>\(p\)</span>. Для інтеграла <span>\((x - y_i)^p\)</span> з парним <span>\(p\)</span> достатньо сказати, що <span>\(\int_{x_i}^{x_{i+1}} (x - y_i)^p dx = \int_{-\frac{h}{2}}^{\frac{h}{2}} x^p dx\)</span>, що дасть деяке кратне <span>\(h^{p+1}\)</span> без членів нижчого порядку <span>\(h\)</span>.</p>
<p>Використання цих фактів зводить вираз для інтеграла <span>\(f(x)\)</span> до</p>

\[\int_{x_i}^{x_{i+1}} f(x) dx= hf(y_i) + O(h^3).\]
<p>Оскільки <span>\(hf(y_i)\)</span> є апроксимацією інтеграла над підінтервалом, правило середньої точки є <span>\(O(h^3)\)</span> для одного підінтервалу, і, використовуючи аналогічні аргументи, як для інтеграла Рімана, є <span>\(O(h^2)\)</span> на всьому інтервалі. Оскільки правило середньої точки вимагає такої ж кількості обчислень, як і інтеграл Рімана, ми по суті отримуємо додатковий порядок точності безкоштовно! Однак, якщо <span>\(f(x_i)\)</span> задано у вигляді точок даних, то ми не зможемо обчислити <span>\(f(y_i)\)</span> для цієї схеми інтегрування.</p>
<p><strong>СПРОБУЙТЕ!</strong> Використайте лівий інтеграл Рімана, правий інтеграл Рімана та правило середньої точки для апроксимації <span>\(\int_{0}^{\pi} \text{sin}(x) dx\)</span> з 11 рівномірно розташованими точками сітки на всьому інтервалі. Порівняйте це значення з точним значенням 2.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>

<span>a</span> <span>=</span> <span>0</span>
<span>b</span> <span>=</span> <span>np</span><span>.</span><span>pi</span>
<span>n</span> <span>=</span> <span>11</span>
<span>h</span> <span>=</span> <span>(</span><span>b</span> <span>-</span> <span>a</span><span>)</span> <span>/</span> <span>(</span><span>n</span> <span>-</span> <span>1</span><span>)</span>
<span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>a</span><span>,</span> <span>b</span><span>,</span> <span>n</span><span>)</span>
<span>f</span> <span>=</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>x</span><span>)</span>

<span>I_riemannL</span> <span>=</span> <span>h</span> <span>*</span> <span>sum</span><span>(</span><span>f</span><span>[:</span><span>n</span><span>-</span><span>1</span><span>])</span>
<span>err_riemannL</span> <span>=</span> <span>2</span> <span>-</span> <span>I_riemannL</span>

<span>I_riemannR</span> <span>=</span> <span>h</span> <span>*</span> <span>sum</span><span>(</span><span>f</span><span>[</span><span>1</span><span>::])</span>
<span>err_riemannR</span> <span>=</span> <span>2</span> <span>-</span> <span>I_riemannR</span>

<span>I_mid</span> <span>=</span> <span>h</span> <span>*</span> <span>sum</span><span>(</span><span>np</span><span>.</span><span>sin</span><span>((</span><span>x</span><span>[:</span><span>n</span><span>-</span><span>1</span><span>]</span> \
        <span>+</span> <span>x</span><span>[</span><span>1</span><span>:])</span><span>/</span><span>2</span><span>))</span>
<span>err_mid</span> <span>=</span> <span>2</span> <span>-</span> <span>I_mid</span>

<span>print</span><span>(</span><span>I_riemannL</span><span>)</span>
<span>print</span><span>(</span><span>err_riemannL</span><span>)</span>

<span>print</span><span>(</span><span>I_riemannR</span><span>)</span>
<span>print</span><span>(</span><span>err_riemannR</span><span>)</span>

<span>print</span><span>(</span><span>I_mid</span><span>)</span>
<span>print</span><span>(</span><span>err_mid</span><span>)</span>
</pre>



<pre><span></span>1.9835235375094546
0.01647646249054535
1.9835235375094546
0.01647646249054535
2.0082484079079745
-0.008248407907974542
</pre>
