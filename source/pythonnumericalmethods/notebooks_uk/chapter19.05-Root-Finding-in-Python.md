```html
<h1>Пошук коренів у Python<a href="#root-finding-in-python" title="Постійне посилання на цей заголовок"></a></h1>
<p>Як ви могли здогадатися, у Python є вбудовані функції для пошуку коренів, які спрощують нам життя. Функція, яку ми будемо використовувати для пошуку кореня, це <em>f_solve</em> з бібліотеки <em>scipy.optimize</em>.</p>
<p>Функція <em>f_solve</em> приймає багато аргументів, які ви можете знайти в <a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fsolve.html">документації</a>, але двома найважливішими є функція, корінь якої ви хочете знайти, та початкове наближення.</p>
<p><strong>СПРОБУЙТЕ!</strong> Обчисліть корінь функції <span>\(f(x) = x^3 - 100x^2 - x + 100\)</span> за допомогою <em>f_solve</em>.</p>


<pre><span></span><span>from</span> <span>scipy.optimize</span> <span>import</span> <span>fsolve</span>
</pre>





<pre><span></span><span>f</span> <span>=</span> <span>lambda</span> <span>x</span><span>:</span> <span>x</span><span>**</span><span>3</span><span>-</span><span>100</span><span>*</span><span>x</span><span>**</span><span>2</span><span>-</span><span>x</span><span>+</span><span>100</span>

<span>fsolve</span><span>(</span><span>f</span><span>,</span> <span>[</span><span>2</span><span>,</span> <span>80</span><span>])</span>
</pre>



<pre><span></span>array([  1., 100.])
</pre>



<p>Ми знаємо, що ця функція має два корені <span>\(x = 1\)</span> та <span>\(x = 100\)</span>, тому ми можемо досить просто отримати обидва корені за допомогою функції <em>f_solve</em>.</p>
```
