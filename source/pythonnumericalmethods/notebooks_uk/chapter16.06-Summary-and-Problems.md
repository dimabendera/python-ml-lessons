<h1>Підсумок<a href="#summary" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Математичні моделі використовуються для розуміння, прогнозування та керування інженерними системами. Ці моделі складаються з параметрів, які визначають поведінку моделі.</p></li>
<li><p>За наявності набору експериментальних даних, регресія методом найменших квадратів є методом знаходження набору параметрів моделі, який добре відповідає даним. Тобто, вона мінімізує квадратичну похибку між моделлю, або функцією оцінки, та точками даних.</p></li>
<li><p>У лінійній регресії методом найменших квадратів функція оцінки повинна бути лінійною комбінацією лінійно незалежних базисних функцій.</p></li>
<li><p>Набір параметрів <span>\({\beta}\)</span> може бути визначений за рівнянням найменших квадратів <span>\({\beta} = (A^T A)^{-1} A^T Y\)</span>, де <span>\(j\)</span>-й стовпець <span>\(A\)</span> — це <span>\(j\)</span>-та базисна функція, обчислена для кожної точки даних <span>\(X\)</span>.</p></li>
<li><p>Щоб оцінити нелінійну функцію, ми можемо перетворити її на лінійну функцію оцінки або безпосередньо використовувати регресію методом найменших квадратів для розв'язання нелінійної функції за допомогою <em>curve_fit</em> з scipy.</p></li>
</ol>


<h1>Задачі<a href="#problems" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Повторіть виведення формули регресії методом найменших квадратів за допомогою багатовимірного числення для функції оцінки <span>\(\hat{y}(x) = ax^2 + bx + c\)</span>, де <span>\(a, b\)</span> та <span>\(c\)</span> є параметрами.</p></li>
<li><p>Напишіть функцію <em>my_ls_params(f, x, y)</em>, де <em>x</em> та <em>y</em> — масиви однакового розміру, що містять експериментальні дані, а <em>f</em> — список, кожен елемент якого є об'єктом функції для базисного вектора функції оцінки. Вихідний аргумент, <em>beta</em>, повинен бути масивом параметрів регресії методом найменших квадратів для <em>x</em>, <em>y</em> та <em>f</em>.</p></li>
<li><p>Напишіть функцію <em>my_func_fit (x,y)</em>, де <em>x</em> та <em>y</em> — вектор-стовпці однакового розміру, що містять експериментальні дані, а функція повертає <em>alpha</em> та <em>beta</em> — параметри функції оцінки <span>\(\hat{y}(x) = {\alpha} x^{{\beta}}\)</span>.</p></li>
<li><p>Задано чотири точки даних <span>\((x_i, y_i)\)</span> та параметри для кубічного полінома <span>\(\hat{y}(x) = ax^3 + bx^2 + cx + d\)</span>, якою буде загальна похибка, пов'язана з функцією оцінки <span>\(\hat{y}(x)\)</span>? Куди ми можемо помістити ще одну точку даних <em>(x,y)</em> так, щоб не виникло додаткової похибки для функції оцінки?</p></li>
<li><p>Напишіть функцію <em>my_lin_regression(f, x, y)</em>, де <em>f</em> — список, що містить об'єкти функцій для базисних функцій, а <em>x</em> та <em>y</em> — масиви, що містять зашумлені дані. Припустіть, що <em>x</em> та <em>y</em> мають однаковий розмір.</p></li>
</ol>
<p>Нехай функція оцінки для даних, що містяться в <em>x</em> та <em>y</em>, визначається як <span>\(\hat{y}(x) = {\beta}(1) \cdot f_{1}(x) + {\beta}(2) \cdot f_{2}(x) + \cdots + {\beta}(n) \cdot f_{n}(x)\)</span>, де <em>n</em> — довжина <em>f</em>. Ваша функція повинна обчислювати <em>beta</em> відповідно до формули регресії методом найменших квадратів.</p>
<p>Тестовий приклад: Зауважте, що ваше рішення може дещо відрізнятися залежно від згенерованих випадкових чисел.</p>
<pre><span></span><span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>2</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>,</span> <span>1000</span><span>)</span>
<span>y</span> <span>=</span> <span>3</span><span>*</span><span>np</span><span>.</span><span>sin</span><span>(</span><span>x</span><span>)</span> <span>-</span> <span>2</span><span>*</span><span>np</span><span>.</span><span>cos</span><span>(</span><span>x</span><span>)</span> <span>+</span> <span>np</span><span>.</span><span>random</span><span>.</span><span>random</span><span>(</span><span>len</span><span>(</span><span>x</span><span>))</span>
<span>f</span> <span>=</span> <span>[</span><span>np</span><span>.</span><span>sin</span><span>,</span> <span>np</span><span>.</span><span>cos</span><span>]</span>
<span>beta</span> <span>=</span> <span>my_lin_regression</span><span>(</span><span>f</span><span>,</span> <span>x</span><span>,</span> <span>y</span><span>)</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span><span>8</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span><span>y</span><span>,</span><span>'b.'</span><span>,</span> <span>label</span> <span>=</span> <span>'data'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>beta</span><span>[</span><span>0</span><span>]</span><span>*</span><span>f</span><span>[</span><span>0</span><span>](</span><span>x</span><span>)</span><span>+</span><span>beta</span><span>[</span><span>1</span><span>]</span><span>*</span><span>f</span><span>[</span><span>1</span><span>](</span><span>x</span><span>)</span><span>+</span><span>beta</span><span>[</span><span>2</span><span>],</span> <span>'r'</span><span>,</span> <span>label</span><span>=</span><span>'regression'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'x'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'y'</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>'Least Square Regression Example'</span><span>)</span>
<span>plt</span><span>.</span><span>legend</span><span>()</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>


<ol>
<li><p>Напишіть функцію <em>my_exp_regression (x,y)</em>, де <em>x</em> та <em>y</em> — масиви однакового розміру.</p></li>
</ol>
<p>Нехай функція оцінки для даних, що містяться в <em>x</em> та <em>y</em>, визначається як <span>\(\hat{y}(x) = {\alpha} e^{{\beta} x}\)</span>. Ваша функція повинна обчислювати <span>\({\alpha}\)</span> та <span>\({\beta}\)</span> як рішення формули регресії методом найменших квадратів.</p>
<p>Тестові приклади: Зауважте, що ваше рішення може дещо відрізнятися від тестового прикладу залежно від згенерованих випадкових чисел.</p>
<pre><span></span><span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>1</span><span>,</span> <span>1000</span><span>)</span>
<span>y</span> <span>=</span> <span>2</span><span>*</span><span>np</span><span>.</span><span>exp</span><span>(</span><span>-</span><span>0.5</span><span>*</span><span>x</span><span>)</span> <span>+</span> <span>0.25</span><span>*</span><span>np</span><span>.</span><span>random</span><span>.</span><span>random</span><span>(</span><span>len</span><span>(</span><span>x</span><span>))</span>

<span>alpha</span><span>,</span> <span>beta</span> <span>=</span> <span>my_exp_regression</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>)</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span><span>8</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span><span>y</span><span>,</span><span>'b.'</span><span>,</span> <span>label</span> <span>=</span> <span>'data'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>alpha</span><span>*</span><span>np</span><span>.</span><span>exp</span><span>(</span><span>beta</span><span>*</span><span>x</span><span>),</span> <span>'r'</span><span>,</span> <span>label</span><span>=</span><span>'regression'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'x'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'y'</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>'Least Square Regression on Exponential Model'</span><span>)</span>
<span>plt</span><span>.</span><span>legend</span><span>()</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>
