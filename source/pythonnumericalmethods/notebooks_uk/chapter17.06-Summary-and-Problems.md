<h1>Підсумок<a href="#summary" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Маючи набір надійних точок даних, інтерполяція — це метод оцінки значень залежних змінних для значень незалежних змінних, яких немає в нашому наборі даних.</p></li>
<li><p>Лінійна, кубічна сплайнова, інтерполяція Лагранжа та поліноміальна інтерполяція Ньютона є поширеними методами інтерполяції.</p></li>
</ol>


<h1>Задачі<a href="#problems" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Напишіть функцію <em>my_lin_interp(x, y, X)</em>, де <em>x</em> та <em>y</em> — це масиви, що містять експериментальні точки даних, а <em>X</em> — це масив. Припустіть, що <em>x</em> та <em>X</em> розташовані у порядку зростання та мають унікальні елементи. Вихідний аргумент *Y* має бути масивом того ж розміру, що й *X*, де *Y[i]* є лінійною інтерполяцією *X[i]*. Ви не повинні використовувати *interp* з numpy або *interp1d* зі scipy.</p></li>
<li><p>Напишіть функцію <em>my_cubic_spline(x, y, X)</em>, де <em>x</em> та <em>y</em> — це масиви, що містять експериментальні точки даних, а *X* — це масив. Припустіть, що *x* та *X* розташовані у порядку зростання та мають унікальні елементи. Вихідний аргумент *Y* має бути масивом того ж розміру, що й *X*, де *Y[i]* є кубічною сплайновою інтерполяцією *X[i]*. Ви не можете використовувати *interp1d* або *CubicSpline*.</p></li>
<li><p>Напишіть функцію <em>my_nearest_neighbor(x, y, X)</em>, де <em>x</em> та <em>y</em> — це масиви, що містять експериментальні точки даних, а *X* — це масив. Припустіть, що *x* та *X* розташовані у порядку зростання та мають унікальні елементи. Вихідний аргумент *Y* має бути масивом того ж розміру, що й *X*, де *Y[i]* є інтерполяцією найближчого сусіда для *X[i]*. Тобто, *Y[i]* має бути *y[j]*, де *x[j]* є найближчою незалежною точкою даних до *X[i]*. Ви не можете використовувати *interp1d* зі scipy.</p></li>
<li><p>Подумайте про ситуацію, коли використання інтерполяції найближчого сусіда було б кращим, ніж кубічної сплайнової інтерполяції.</p></li>
<li><p>Напишіть функцію <em>my_cubic_spline_flat(x, y, X)</em>, де <em>x</em> та <em>y</em> — це масиви, що містять експериментальні точки даних, а *X* — це масив. Припустіть, що *x* та *X* розташовані у порядку зростання та мають унікальні елементи. Вихідний аргумент *Y* має бути масивом того ж розміру, що й *X*, де *Y[i]* є кубічною сплайновою інтерполяцією *X[i]*. Однак, замість обмежень, які ми ввели раніше, використовуйте <span>\(S'_1(x_1)=0\)</span> та <span>\(S'_{n-1}(x_n)=0\)</span>.</p></li>
<li><p>Напишіть функцію <em>my_quintic_spline(x, y, X)</em>, де <em>x</em> та <em>y</em> — це масиви, що містять експериментальні точки даних, а *X* — це масив. Припустіть, що *x* та *X* розташовані у порядку зростання та мають унікальні елементи. Вихідний аргумент *Y* має бути масивом того ж розміру, що й *X*, де *Y[i]* є квінтичною сплайновою інтерполяцією *X[i]*. Вам потрібно буде використати додаткові граничні умови для отримання достатньої кількості обмежень. Ви можете використовувати граничні умови на свій розсуд.</p></li>
<li><p>Напишіть функцію <em>my_interp_plotter(x, y, X, option)</em>, де <em>x</em> та <em>y</em> — це масиви, що містять експериментальні точки даних, а *X* — це масив, що містить координати, для яких бажана інтерполяція. Вхідний аргумент `option` має бути рядком: ‘linear`, ‘spline` або ‘nearest`. Ваша функція повинна створювати графік точок даних <span>\((x, y)\)</span>, позначених червоними колами, та точок <span>\((X, Y)\)</span>, де *X* — це вхідні дані, а *Y* — це інтерполяція в точках, що містяться в *X*, визначена вхідним аргументом `option`. Точки <span>\((X, Y)\)</span> мають бути з'єднані синьою лінією. Обов'язково включіть заголовок, підписи осей та легенду. Підказка: Ви повинні використовувати *interp1d* зі scipy та перевірити опцію *kind*.</p></li>
</ol>
<p>Тестові випадки:</p>
<pre><span></span><span>x</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([</span><span>0</span><span>,</span> <span>.</span><span>1</span><span>,</span> <span>.</span><span>15</span><span>,</span> <span>.</span><span>35</span><span>,</span> <span>.</span><span>6</span><span>,</span> <span>.</span><span>7</span><span>,</span> <span>.</span><span>95</span><span>,</span> <span>1</span><span>])</span>
<span>y</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([</span><span>1</span><span>,</span> <span>0.8187</span><span>,</span> <span>0.7408</span><span>,</span> <span>0.4966</span><span>,</span> <span>0.3012</span><span>,</span> <span>0.2466</span><span>,</span> <span>0.1496</span><span>,</span> <span>0.1353</span><span>])</span>

<span>my_interp_plotter</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>1</span><span>,</span> <span>101</span><span>),</span> <span>'nearest'</span><span>)</span>
</pre>


<pre><span></span><span>my_interp_plotter</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>1</span><span>,</span> <span>101</span><span>),</span> <span>'linear'</span><span>)</span>
</pre>


<pre><span></span><span>my_interp_plotter</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>1</span><span>,</span> <span>101</span><span>),</span> <span>'cubic'</span><span>)</span>
</pre>


<ol>
<li><p>Напишіть функцію <em>my_D_cubic_spline(x, y, X, D)</em>, де вихідний *Y* — це кубічна сплайнова інтерполяція в *X*, отримана з точок даних, що містяться в *x* та *y*. Однак, замість стандартних граничних умов (тобто <span>\(S''_1(x_1) = 0\)</span> та <span>\(S''_{n-1}(x_n) = 0\)</span>), ви повинні використовувати граничні умови <span>\(S^{\prime}_1(x_1) = D\)</span> та <span>\(S^{\prime}_{n-1}(x_n) = D\)</span> (тобто нахили інтерполяційних поліномів на кінцевих точках дорівнюють <span>\(D\)</span>).</p></li>
</ol>
<p>Тестові випадки:</p>
<pre><span></span><span>x</span> <span>=</span> <span>[</span><span>0</span><span>,</span> <span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>,</span> <span>4</span><span>]</span>
<span>y</span> <span>=</span> <span>[</span><span>0</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>]</span>
<span>X</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>4</span><span>,</span> <span>101</span><span>)</span>

<span># Solution: Y = 0.54017857</span>
<span>Y</span> <span>=</span> <span>my_D_cubic_spline</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>1.5</span><span>,</span> <span>1</span><span>)</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span> <span>8</span><span>))</span>
<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>221</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>'ro'</span><span>,</span> <span>X</span><span>,</span> <span>my_D_cubic_spline</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>X</span><span>,</span> <span>0</span><span>),</span> <span>'b'</span><span>)</span>
<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>222</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>'ro'</span><span>,</span> <span>X</span><span>,</span> <span>my_D_cubic_spline</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>X</span><span>,</span> <span>1</span><span>),</span> <span>'b'</span><span>)</span>
<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>223</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>'ro'</span><span>,</span> <span>X</span><span>,</span> <span>my_D_cubic_spline</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>X</span><span>,</span> <span>-</span><span>1</span><span>),</span> <span>'b'</span><span>)</span>
<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>224</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>'ro'</span><span>,</span> <span>X</span><span>,</span> <span>my_D_cubic_spline</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>X</span><span>,</span> <span>4</span><span>),</span> <span>'b'</span><span>)</span>
<span>plt</span><span>.</span><span>tight_layout</span><span>()</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>


<ol>
<li><p>Напишіть функцію <em>my_lagrange(x, y, X)</em>, де вихідний *Y* — це інтерполяція Лагранжа точок даних, що містяться в *x* та *y*, обчислена в *X*. Підказка: Використовуйте вкладений цикл `for`, де внутрішній цикл обчислює добуток для базисного полінома Лагранжа, а зовнішній цикл обчислює суму для полінома Лагранжа. Не використовуйте існуючу функцію *lagrange* зі scipy.</p></li>
</ol>
<p>Тестові випадки</p>
<pre><span></span><span>x</span> <span>=</span> <span>[</span><span>0</span><span>,</span> <span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>,</span> <span>4</span><span>]</span>
<span>y</span> <span>=</span> <span>[</span><span>2</span><span>,</span> <span>1</span><span>,</span> <span>3</span><span>,</span> <span>5</span><span>,</span> <span>1</span><span>]</span>

<span>X</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>4</span><span>,</span> <span>101</span><span>)</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span><span>8</span> <span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>X</span><span>,</span> <span>my_lagrange</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>X</span><span>),</span> <span>'b'</span><span>,</span> <span>label</span> <span>=</span> <span>'interpolation'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>'ro'</span><span>,</span> <span>label</span> <span>=</span> <span>'data points'</span><span>)</span>

<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'x'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'y'</span><span>)</span>

<span>plt</span><span>.</span><span>title</span><span>(</span><span>f</span><span>'Lagrange Interpolation of Data Points'</span><span>)</span>
<span>plt</span><span>.</span><span>legend</span><span>()</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>


<ol>
<li><p>Апроксимуйте дані x = [0, 1, 2, 3, 4], y = [2, 1, 3, 5, 1] за допомогою поліноміальної інтерполяції Ньютона.</p></li>
</ol>
<p>&lt; 17.5 Поліноміальна інтерполяція Ньютона | Зміст | РОЗДІЛ 18. Ряди &gt;</p>
