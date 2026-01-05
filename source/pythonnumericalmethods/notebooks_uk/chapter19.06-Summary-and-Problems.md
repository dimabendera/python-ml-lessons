<h1>Підсумок<a href="#summary" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Корені є важливою властивістю функцій.</p></li>
<li><p>Метод бісекції — це спосіб знаходження коренів, заснований на принципі "розділяй і володарюй". Хоча він стабільний, його збіжність може бути повільною порівняно з методом Ньютона-Рафсона.</p></li>
<li><p>Метод Ньютона-Рафсона — це інший спосіб знаходження коренів, заснований на апроксимації функції. Метод Ньютона-Рафсона швидко збігається поблизу дійсного кореня, але може мати нестабільну поведінку.</p></li>
</ol>


<h1>Задачі<a href="#problems" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Напишіть функцію <span>\(my\_nth\_root(x, n, tol)\)</span>, де <span>\(x\)</span> та <span>\(tol\)</span> є строго додатними скалярами, а <span>\(n\)</span> є цілим числом, строго більшим за 1. Вихідний аргумент, <span>\(r\)</span>, має бути апроксимацією <span>\(r = \sqrt[N]{x}\)</span>, N-го кореня з <span>\(x\)</span>. Ця апроксимація повинна бути обчислена за допомогою методу Ньютона-Рафсона для знаходження кореня функції <span>\(f(y) = y^N - x\)</span>. Метрика похибки повинна бути <span>\(|f(y)|\)</span>.</p></li>
<li><p>Напишіть функцію <span>\(my\_fixed\_point(f, g, tol, max_iter)\)</span>, де <span>\(f\)</span> та <span>\(g\)</span> є об'єктами-функціями, а <span>\(tol\)</span> та <span>\(max\_iter\)</span> є строго додатними скалярами. Вхідний аргумент, <span>\(max\_iter\)</span>, також є цілим числом. Вихідний аргумент, <span>\(X\)</span>, має бути скаляром, що задовольняє <span>\(|f(X) - g(X)| &lt; tol\)</span>; тобто, <span>\(X\)</span> є точкою, яка (майже) задовольняє <span>\(f(X) = g(X)\)</span>. Щоб знайти <span>\(X\)</span>, ви повинні використовувати метод бісекції з метрикою похибки, <span>\(|F(m)| &lt; tol\)</span>. Функція <span>\(my\_fixed\_point\)</span> повинна "здатися" після <span>\(max\_iter\)</span> кількості ітерацій і повернути <span>\(X = []\)</span>, якщо це станеться.</p></li>
<li><p>Чому метод бісекції не працює для <span>\(f(x) = 1/x\)</span> з похибкою, заданою як <span>\(|b-a|\)</span>? Підказка: Як <span>\(f(x)\)</span> порушує теорему про проміжне значення?</p></li>
<li><p>Напишіть функцію <span>\(my\_bisection(f, a, b, tol)\)</span>, яка повертає <span>\([R, E]\)</span>, де <span>\(f\)</span> є об'єктом-функцією, <span>\(a\)</span> та <span>\(b\)</span> є скалярами такими, що <span>\(a &lt; b\)</span>, а <span>\(tol\)</span> є строго додатним скалярним значенням. Функція повинна повернути масив, <span>\(R\)</span>, де <span>\(R[i]\)</span> є оцінкою кореня <span>\(f\)</span>, визначеною як <span>\((a + b)/2\)</span> для <span>\(i\)</span>-ї ітерації методу бісекції. Не забудьте включити початкову оцінку. Функція також повинна повернути масив, <span>\(E\)</span>, де <span>\(E[i]\)</span> є значенням <span>\(| f(R[i]) |\)</span> для <span>\(i\)</span>-ї ітерації методу бісекції. Функція повинна завершитися, коли <span>\(E(i) &lt; tol\)</span>. Ви можете припустити, що <span>\({\text{sign}}(f(a)) \neq {\text{sign}}(f(b))\)</span>.</p></li>
</ol>
<p>Уточнення: Вхідні значення <span>\(a\)</span> та <span>\(b\)</span> становлять першу ітерацію бісекції, і тому <span>\(R\)</span> та <span>\(E\)</span> ніколи не повинні бути порожніми.</p>
<p>Тестові випадки:</p>
<pre><span></span><span>In</span><span>:</span> <span>f</span> <span>=</span> <span>lambda</span> <span>x</span><span>:</span> <span>x</span><span>**</span><span>2</span> <span>-</span> <span>2</span>
    <span>[</span><span>R</span><span>,</span> <span>E</span><span>]</span> <span>=</span> <span>my_bisection</span><span>(</span><span>f</span><span>,</span> <span>0</span><span>,</span> <span>2</span><span>,</span> <span>1e-1</span><span>)</span>
<span>Out</span><span>:</span> <span>R</span> <span>=</span> <span>[</span><span>1</span><span>,</span> <span>1.5</span><span>,</span> <span>1.25</span><span>,</span> <span>1.375</span><span>,</span> <span>1.4375</span><span>]</span>
     <span>E</span> <span>=</span> <span>[</span><span>1</span><span>,</span> <span>0.25</span><span>,</span> <span>0.4375</span><span>,</span> <span>0.109375</span><span>,</span> <span>0.06640625</span><span>]</span>
       
<span>In</span><span>:</span> <span>f</span> <span>=</span> <span>lambda</span> <span>x</span><span>:</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>x</span><span>)</span> <span>-</span> <span>np</span><span>.</span><span>cos</span><span>(</span><span>x</span><span>)</span>
    <span>[</span><span>R</span><span>,</span> <span>E</span><span>]</span> <span>=</span> <span>my_bisection</span><span>(</span><span>f</span><span>,</span> <span>0</span><span>,</span> <span>2</span><span>,</span> <span>1e-2</span><span>)</span>
<span>Out</span><span>:</span> <span>R</span> <span>=</span> <span>[</span><span>1</span><span>,</span> <span>0.5</span><span>,</span> <span>0.75</span><span>,</span> <span>0.875</span><span>,</span> <span>0.8125</span><span>,</span> <span>0.78125</span><span>]</span>
     <span>E</span> <span>=</span> <span>[</span><span>0.30116867893975674</span><span>,</span> <span>0.39815702328616975</span><span>,</span> <span>0.05005010885048666</span><span>,</span> <span>0.12654664407270177</span><span>,</span> <span>0.038323093040207645</span><span>,</span> <span>0.005866372111545948</span><span>]</span>
</pre>

<ol>
<li><p>Напишіть функцію <span>\(my\_newton(f, df, x0, tol)\)</span>, яка повертає <span>\([R, E]\)</span>, де <span>\(f\)</span> є об'єктом-функцією, <span>\(df\)</span> є об'єктом-функцією для похідної від <span>\(f\)</span>, <span>\(x0\)</span> є початковою оцінкою кореня, а <span>\(tol\)</span> є строго додатним скаляром. Функція повинна повернути масив, <span>\(R\)</span>, де <span>\(R[i)]\)</span> є оцінкою кореня <span>\(f\)</span> за методом Ньютона-Рафсона для <span>\(i\)</span>-ї ітерації. Не забудьте включити початкову оцінку. Функція також повинна повернути масив, <span>\(E\)</span>, де <span>\(E[i]\)</span> є значенням <span>\(| f(R[i]) |\)</span> для <span>\(i\)</span>-ї ітерації методу Ньютона-Рафсона. Функція повинна завершитися, коли <span>\(E(i) &lt; tol\)</span>. Ви можете припустити, що похідна від <span>\(f\)</span> не дорівнюватиме 0 під час жодної ітерації для будь-якого з наведених тестових випадків.</p></li>
</ol>
<p>Тестові випадки:</p>
<pre><span></span><span>In</span><span>:</span> <span>f</span> <span>=</span> <span>lambda</span> <span>x</span><span>:</span> <span>x</span><span>**</span><span>2</span> <span>-</span> <span>2</span>
   <span>df</span> <span>=</span> <span>lambda</span> <span>x</span><span>:</span> <span>2</span><span>*</span><span>x</span>
    <span>[</span><span>R</span><span>,</span> <span>E</span><span>]</span> <span>=</span> <span>my_newton</span><span>(</span><span>f</span><span>,</span> <span>df</span><span>,</span> <span>1</span><span>,</span> <span>1e-5</span><span>)</span>
<span>Out</span><span>:</span> <span>R</span> <span>=</span> <span>[</span><span>1</span><span>,</span> <span>1.5</span><span>,</span> <span>1.4166666666666667</span><span>,</span> <span>1.4142156862745099</span><span>]</span>
     <span>E</span> <span>=</span> <span>[</span><span>1</span><span>,</span> <span>0.25</span><span>,</span> <span>0.006944444444444642</span><span>,</span> <span>6.007304882871267e-06</span><span>]</span>
       
<span>In</span><span>:</span> <span>f</span> <span>=</span> <span>lambda</span> <span>x</span><span>:</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>x</span><span>)</span> <span>-</span> <span>np</span><span>.</span><span>cos</span><span>(</span><span>x</span><span>)</span>
   <span>df</span> <span>=</span> <span>lambda</span> <span>x</span><span>:</span> <span>np</span><span>.</span><span>cos</span><span>(</span><span>x</span><span>)</span> <span>+</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>x</span><span>)</span>
    <span>[</span><span>R</span><span>,</span> <span>E</span><span>]</span> <span>=</span> <span>my_newton</span><span>(</span><span>f</span><span>,</span> <span>df</span><span>,</span> <span>1</span><span>,</span> <span>1e-5</span><span>)</span>
<span>Out</span><span>:</span> <span>R</span> <span>=</span> <span>[</span><span>1</span><span>,</span> <span>0.782041901539138</span><span>,</span> <span>0.7853981759997019</span><span>]</span>
     <span>E</span> <span>=</span> <span>[</span><span>0.30116867893975674</span><span>,</span> <span>0.004746462127804163</span><span>,</span> <span>1.7822277875723103e-08</span><span>]</span>
</pre>

<ol>
<li><p>Розглянемо задачу будівництва трубопроводу від офшорної нафтової платформи, на відстані <span>\(H\)</span> миль від берегової лінії, до нафтопереробної станції на суші, на відстані <span>\(L\)</span> миль уздовж берега. Вартість будівництва труби становить <span>\(C_{\text{ocean}/\text{mile}}\)</span>, поки труба знаходиться під океаном, і <span>\(C_{\text{land}/\text{mile}}\)</span>, поки труба знаходиться на суші. Труба буде прокладена по прямій лінії до берега, де вона з'єднається в деякій точці, <span>\(x\)</span>, між 0 та <span>\(L\)</span>. Вона продовжиться вздовж берега по суші, доки не досягне нафтопереробного заводу. Дивіться рисунок для уточнення.</p></li>
</ol>

<p>Напишіть функцію <span>\(my\_pipe\_builder(C\_ocean, C\_land, L, H)\)</span>, де вхідні аргументи описані раніше, а <span>\(x\)</span> є значенням x, яке мінімізує загальну вартість трубопроводу. Ви повинні використовувати метод бісекції для визначення цього значення з точністю до <span>\(1\times10^{-6}\)</span>, починаючи з початкових меж <span>\(a=0\)</span> та <span>\(b=L\)</span>.</p>
<p>Тестові випадки:</p>
<pre><span></span><span>In</span><span>:</span> <span>my_pipe_builder</span><span>(</span><span>20</span><span>,</span> <span>10</span><span>,</span> <span>100</span><span>,</span> <span>50</span><span>)</span>
<span>Out</span><span>:</span> <span>28.867512941360474</span>
  
<span>In</span><span>:</span> <span>my_pipe_builder</span><span>(</span><span>30</span><span>,</span> <span>10</span><span>,</span> <span>100</span><span>,</span> <span>50</span><span>)</span>
<span>Out</span><span>:</span> <span>17.677670717239380</span>
  
<span>In</span><span>:</span> <span>my_pipe_builder</span><span>(</span><span>30</span><span>,</span> <span>10</span><span>,</span> <span>100</span><span>,</span> <span>20</span><span>)</span>
<span>Out</span><span>:</span> <span>7.071067392826080</span>
</pre>

<ol>
<li><p>Знайдіть функцію <span>\(f(x)\)</span> та припущення для кореня <span>\(f, x_0\)</span>, такі, щоб метод Ньютона-Рафсона коливався між <span>\(x_0\)</span> та <span>\(-x_0\)</span> нескінченно.</p></li>
</ol>
