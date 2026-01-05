```html
<h1>Чисельне диференціювання з шумом<a href="#numerical-differentiation-with-noise" title="Постійне посилання на цей заголовок"></a></h1>
<p>Як зазначалося раніше, іноді <span>\(f\)</span> задається як вектор, де <span>\(f\)</span> є відповідним значенням функції для незалежних значень даних в іншому векторі <span>\(x\)</span>, який є сітковим. Іноді дані можуть бути забруднені <strong>шумом</strong>, що означає, що їхнє значення відрізняється на невелику величину від того, яким воно було б, якби було обчислено з чистої математичної функції. Це часто може відбуватися в інженерії через неточності у вимірювальних пристроях або самі дані можуть бути дещо змінені збуреннями поза системою інтересу. Наприклад, ви можете намагатися слухати, як ваш друг розмовляє в переповненій кімнаті. Сигнал <span>\(f\)</span> може бути інтенсивністю та тональними значеннями в мовленні вашого друга. Однак, оскільки кімната переповнена, шум від інших розмов чути разом з мовленням вашого друга, і його стає важко зрозуміти.</p>
<p>Щоб проілюструвати це, ми чисельно обчислюємо похідну простої косинусної хвилі, спотвореної невеликою синусною хвилею. Розглянемо наступні дві функції:</p>

\[f(x) = \cos(x)\]
<p>та</p>

\[f_{\epsilon,\omega}(x) = \cos(x)+\epsilon \sin(\omega x)\]
<p>де <span>\(0 &lt; \epsilon\ll1\)</span> — дуже мале число, а <span>\(\omega\)</span> — велике число. Коли <span>\(\epsilon\)</span> мале, очевидно, що <span>\(f\simeq f_{\epsilon,\omega}\)</span>. Щоб проілюструвати це, ми будуємо графік <span>\(f_{\epsilon,\omega}(x)\)</span> для <span>\(\epsilon = 0.01\)</span> та <span>\(\omega = 100\)</span>, і бачимо, що він дуже близький до <span>\(f(x)\)</span>, як показано на наступному рисунку.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
<span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>
<span>plt</span><span>.</span><span>style</span><span>.</span><span>use</span><span>(</span><span>'seaborn-poster'</span><span>)</span>
<span>%</span><span>matplotlib</span> inline
</pre>





<pre><span></span><span>x</span> <span>=</span> <span>np</span><span>.</span><span>arange</span><span>(</span><span>0</span><span>,</span> <span>2</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>,</span> <span>0.01</span><span>)</span>
<span># compute function</span>
<span>omega</span> <span>=</span> <span>100</span>
<span>epsilon</span> <span>=</span> <span>0.01</span>

<span>y</span> <span>=</span> <span>np</span><span>.</span><span>cos</span><span>(</span><span>x</span><span>)</span> 
<span>y_noise</span> <span>=</span> <span>y</span> <span>+</span> <span>epsilon</span><span>*</span><span>np</span><span>.</span><span>sin</span><span>(</span><span>omega</span><span>*</span><span>x</span><span>)</span>

<span># Plot solution</span>
<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>12</span><span>,</span> <span>8</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y_noise</span><span>,</span> <span>'r-'</span><span>,</span> \
         <span>label</span> <span>=</span> <span>'cos(x) + шум'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>'b-'</span><span>,</span> \
         <span>label</span> <span>=</span> <span>'cos(x)'</span><span>)</span>

<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'x'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'y'</span><span>)</span>

<span>plt</span><span>.</span><span>legend</span><span>()</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter20.04-Numerical-Differentiation-with-Noise_5_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter20.04-Numerical-Differentiation-with-Noise_5_0.png"/>


<p>Похідні наших двох тестових функцій:</p>

\[f^{\prime}(x) = -\sin(x)\]
<p>та</p>

\[f_{\epsilon,\omega}^{\prime}(x) = -\sin(x)+\epsilon\omega \cos(\omega x).\]
<p>Оскільки <span>\(\epsilon\omega\)</span> може бути не малим, коли <span>\(\omega\)</span> велике, внесок шуму в похідну може бути не малим. В результаті, похідна (аналітична та чисельна) може бути непридатною для використання. Наприклад, наступний рисунок показує <span>\(f^{\prime}(x)\)</span> та <span>\(f^{\prime}_{\epsilon,\omega}(x)\)</span> для <span>\(\epsilon = 0.01\)</span> та <span>\(\omega = 100\)</span>.</p>


<pre><span></span><span>x</span> <span>=</span> <span>np</span><span>.</span><span>arange</span><span>(</span><span>0</span><span>,</span> <span>2</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>,</span> <span>0.01</span><span>)</span>
<span># compute function</span>
<span>y</span> <span>=</span> <span>-</span><span>np</span><span>.</span><span>sin</span><span>(</span><span>x</span><span>)</span> 
<span>y_noise</span> <span>=</span> <span>y</span> <span>+</span> <span>epsilon</span><span>*</span><span>omega</span><span>*</span><span>np</span><span>.</span><span>cos</span><span>(</span><span>omega</span><span>*</span><span>x</span><span>)</span>

<span># Plot solution</span>
<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>12</span><span>,</span> <span>8</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y_noise</span><span>,</span> <span>'r-'</span><span>,</span> \
         <span>label</span> <span>=</span> <span>'Похідна cos(x) + шум'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>'b-'</span><span>,</span> \
         <span>label</span> <span>=</span> <span>'Похідна cos(x)'</span><span>)</span>

<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'x'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'y'</span><span>)</span>

<span>plt</span><span>.</span><span>legend</span><span>()</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter20.04-Numerical-Differentiation-with-Noise_7_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter20.04-Numerical-Differentiation-with-Noise_7_0.png"/>
```
