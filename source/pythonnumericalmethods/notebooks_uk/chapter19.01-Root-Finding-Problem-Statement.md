<h1>Постановка задачі пошуку коренів<a href="#root-finding-problem-statement" title="Постійне посилання на цей заголовок"></a></h1>
<p><strong>Корінь</strong> або **нуль** функції, <span>\(f(x)\)</span>, це <span>\(x_r\)</span> такий, що <span>\(f(x_r) = 0\)</span>. Для таких функцій, як <span>\(f(x) = x^2 - 9\)</span>, корені очевидно дорівнюють 3 та <span>\(-3\)</span>. Однак, для інших функцій, таких як <span>\(f(x) = {\rm cos}(x) - x\)</span>, визначення **аналітичного**, або точного, розв'язку для коренів функцій може бути складним. У цих випадках корисно генерувати числові наближення коренів <span>\(f\)</span> та розуміти обмеження, пов'язані з цим.</p>
<p><strong>СПРОБУЙТЕ!</strong> Використайте функцію <em>fsolve</em> з <em>scipy</em> для обчислення кореня <span>\(f(x) = {\rm cos}(x) - x\)</span> поблизу <span>\(-2\)</span>. Перевірте, що розв'язок є коренем (або достатньо близьким).</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
<span>from</span> <span>scipy</span> <span>import</span> <span>optimize</span>

<span>f</span> <span>=</span> <span>lambda</span> <span>x</span><span>:</span> <span>np</span><span>.</span><span>cos</span><span>(</span><span>x</span><span>)</span> <span>-</span> <span>x</span>
<span>r</span> <span>=</span> <span>optimize</span><span>.</span><span>fsolve</span><span>(</span><span>f</span><span>,</span> <span>-</span><span>2</span><span>)</span>
<span>print</span><span>(</span><span>"r ="</span><span>,</span> <span>r</span><span>)</span>

<span># Verify the solution is a root</span>
<span>result</span> <span>=</span> <span>f</span><span>(</span><span>r</span><span>)</span>
<span>print</span><span>(</span><span>"result="</span><span>,</span> <span>result</span><span>)</span>
</pre>



<pre><span></span>r = [0.73908513]
result= [0.]
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Функція <span>\(f(x) = \frac{1}{x}\)</span> не має коренів. Використайте функцію <em>fsolve</em>, щоб спробувати обчислити корінь <span>\(f(x) = \frac{1}{x}\)</span>. Увімкніть <em>full_output</em>, щоб побачити, що відбувається. Не забудьте перевірити документацію для отримання деталей.</p>


<pre><span></span><span>f</span> <span>=</span> <span>lambda</span> <span>x</span><span>:</span> <span>1</span><span>/</span><span>x</span>

<span>r</span><span>,</span> <span>infodict</span><span>,</span> <span>ier</span><span>,</span> <span>mesg</span> <span>=</span> <span>optimize</span><span>.</span><span>fsolve</span><span>(</span><span>f</span><span>,</span> <span>-</span><span>2</span><span>,</span> <span>full_output</span><span>=</span><span>True</span><span>)</span>
<span>print</span><span>(</span><span>"r ="</span><span>,</span> <span>r</span><span>)</span>

<span>result</span> <span>=</span> <span>f</span><span>(</span><span>r</span><span>)</span>
<span>print</span><span>(</span><span>"result="</span><span>,</span> <span>result</span><span>)</span>

<span>print</span><span>(</span><span>mesg</span><span>)</span>
</pre>



<pre><span></span>r = [-3.52047359e+83]
result= [-2.84052692e-84]
The number of calls to function has reached maxfev = 400.
</pre>



<p>Ми бачимо, що отримане значення <em>r</em> не є коренем, хоча <em>f(r)</em> є дуже малим числом. Оскільки ми увімкнули <em>full_output</em>, який містить більше інформації. Повідомлення буде повернуто, якщо рішення не знайдено, і ми можемо побачити деталі <em>mesg</em> щодо причини збою - "The number of calls to function has reached maxfev = 400."</p>
