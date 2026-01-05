```html
<h1>Метод Ньютона-Рафсона<a href="#newton-raphson-method" title="Постійне посилання на цей заголовок"></a></h1>
<p>Нехай <span>\(f(x)\)</span> — гладка і неперервна функція, а <span>\(x_r\)</span> — невідомий корінь <span>\(f(x)\)</span>. Тепер припустимо, що <span>\(x_0\)</span> є припущенням для <span>\(x_r\)</span>. Якщо <span>\(x_0\)</span> не є дуже вдалим припущенням, то <span>\(f(x_0)\)</span> не дорівнюватиме нулю. За такого сценарію ми хочемо знайти <span>\(x_1\)</span>, яке є покращенням для <span>\(x_0\)</span> (тобто, ближче до <span>\(x_r\)</span>, ніж <span>\(x_0\)</span>). Якщо ми припустимо, що <span>\(x_0\)</span> є "достатньо близьким" до <span>\(x_r\)</span>, то ми можемо покращити його, взявши лінійну апроксимацію <span>\(f(x)\)</span> в околі <span>\(x_0\)</span>, яка є прямою, і знайшовши перетин цієї прямої з віссю x. У розгорнутому вигляді лінійна апроксимація <span>\(f(x)\)</span> в околі <span>\(x_0\)</span> має вигляд <span>\(f(x) \approx f(x_0) + f^{\prime}(x_0)(x-x_0)\)</span>. Використовуючи цю апроксимацію, ми знаходимо <span>\(x_1\)</span> таке, що <span>\(f(x_1) = 0\)</span>. Підстановка цих значень у лінійну апроксимацію дає рівняння</p>

\[
0 = f(x_0) + f^{\prime}(x_0)(x_1-x_0),
\]
<p>яке, розв'язавши відносно <span>\(x_1\)</span>, отримуємо
$<span>\(
x_1 = x_0 - \frac{f(x_0)}{f^{\prime}(x_0)}.
\)</span>$</p>
<p>Ілюстрація того, як ця лінійна апроксимація покращує початкове припущення, показана на наступному малюнку.</p>

<p>У загальному вигляді, <strong>крок Ньютона</strong> обчислює покращене припущення, <span>\(x_i\)</span>, використовуючи попереднє припущення <span>\(x_{i-1}\)</span>, і задається рівнянням</p>

\[
x_i = x_{i-1} - \frac{g(x_{i-1})}{g^{\prime}(x_{i-1})}.
\]
<p><strong>Метод Ньютона-Рафсона</strong> для знаходження коренів ітеративно виконує кроки Ньютона, починаючи з <span>\(x_0\)</span>, доки похибка не стане меншою за задану точність.</p>
<p><strong>СПРОБУЙТЕ!</strong> Знову ж таки, <span>\(\sqrt{2}\)</span> є коренем функції <span>\(f(x) = x^2 - 2\)</span>. Використовуючи <span>\(x_0 = 1.4\)</span> як початкову точку, використайте попереднє рівняння для оцінки <span>\(\sqrt{2}\)</span>. Порівняйте цю апроксимацію зі значенням, обчисленим функцією `sqrt` у Python.</p>

\[
x = 1.4 - \frac{1.4^2 - 2}{2(1.4)} = 1.4142857142857144
\]


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>

<span>f</span> <span>=</span> <span>lambda</span> <span>x</span><span>:</span> <span>x</span><span>**</span><span>2</span> <span>-</span> <span>2</span>
<span>f_prime</span> <span>=</span> <span>lambda</span> <span>x</span><span>:</span> <span>2</span><span>*</span><span>x</span>
<span>newton_raphson</span> <span>=</span> <span>1.4</span> <span>-</span> <span>(</span><span>f</span><span>(</span><span>1.4</span><span>))</span><span>/</span><span>(</span><span>f_prime</span><span>(</span><span>1.4</span><span>))</span>

<span>print</span><span>(</span><span>"newton_raphson ="</span><span>,</span> <span>newton_raphson</span><span>)</span>
<span>print</span><span>(</span><span>"sqrt(2) ="</span><span>,</span> <span>np</span><span>.</span><span>sqrt</span><span>(</span><span>2</span><span>))</span>
</pre>



<pre><span></span>newton_raphson = 1.4142857142857144
sqrt(2) = 1.4142135623730951
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Напишіть функцію <span>\(my\_newton(f, df, x0, tol)\)</span>, де результатом є оцінка кореня <em>f</em>, <em>f</em> — це об'єкт-функція <span>\(f(x)\)</span>, <em>df</em> — це об'єкт-функція для <span>\(f^{\prime}(x)\)</span>, <em>x0</em> — початкове припущення, а <em>tol</em> — допустима похибка. Мірою похибки має бути <span>\(|f(x)|\)</span>.</p>


<pre><span></span><span>def</span> <span>my_newton</span><span>(</span><span>f</span><span>,</span> <span>df</span><span>,</span> <span>x0</span><span>,</span> <span>tol</span><span>):</span>
    <span># виводить оцінку кореня f</span>
    <span># використовуючи метод Ньютона-Рафсона</span>
    <span># рекурсивна реалізація</span>
    <span>if</span> <span>abs</span><span>(</span><span>f</span><span>(</span><span>x0</span><span>))</span> <span>&lt;</span> <span>tol</span><span>:</span>
        <span>return</span> <span>x0</span>
    <span>else</span><span>:</span>
        <span>return</span> <span>my_newton</span><span>(</span><span>f</span><span>,</span> <span>df</span><span>,</span> <span>x0</span> <span>-</span> <span>f</span><span>(</span><span>x0</span><span>)</span><span>/</span><span>df</span><span>(</span><span>x0</span><span>),</span> <span>tol</span><span>)</span>
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Використайте <em>my_newton</em>, щоб обчислити <span>\(\sqrt{2}\)</span> з точністю до 1e-6, починаючи з <em>x0 = 1.5</em>.</p>


<pre><span></span><span>estimate</span> <span>=</span> <span>my_newton</span><span>(</span><span>f</span><span>,</span> <span>f_prime</span><span>,</span> <span>1.5</span><span>,</span> <span>1e-6</span><span>)</span>
<span>print</span><span>(</span><span>"estimate ="</span><span>,</span> <span>estimate</span><span>)</span>
<span>print</span><span>(</span><span>"sqrt(2) ="</span><span>,</span> <span>np</span><span>.</span><span>sqrt</span><span>(</span><span>2</span><span>))</span>
</pre>



<pre><span></span>estimate = 1.4142135623746899
sqrt(2) = 1.4142135623730951
</pre>



<p>Якщо <span>\(x_0\)</span> близьке до <span>\(x_r\)</span>, то можна довести, що, в загальному, метод Ньютона-Рафсона збігається до <span>\(x_r\)</span> набагато швидше, ніж метод бісекції. Однак, оскільки <span>\(x_r\)</span> спочатку невідомий, немає способу дізнатися, чи є початкове припущення достатньо близьким до кореня для такої поведінки, якщо <em>апріорі</em> не відома якась спеціальна інформація про функцію (наприклад, що функція має корінь поблизу <span>\(x = 0\)</span>). Окрім цієї проблеми ініціалізації, метод Ньютона-Рафсона має й інші серйозні обмеження. Наприклад, якщо похідна в точці припущення близька до 0, то крок Ньютона буде дуже великим і, ймовірно, відведе далеко від кореня. Також, залежно від поведінки похідної функції між <span>\(x_0\)</span> та <span>\(x_r\)</span>, метод Ньютона-Рафсона може збігтися до іншого кореня, відмінного від <span>\(x_r\)</span>, який може бути некорисним для нашого інженерного застосування.</p>
<p><strong>СПРОБУЙТЕ!</strong> Обчисліть один крок Ньютона, щоб отримати покращену апроксимацію кореня функції <span>\(f(x) = x^3 + 3x^2 - 2x - 5\)</span> з початковим припущенням, <span>\(x_0 = 0.29\)</span>.</p>


<pre><span></span><span>x0</span> <span>=</span> <span>0.29</span>
<span>x1</span> <span>=</span> <span>x0</span><span>-</span><span>(</span><span>x0</span><span>**</span><span>3</span><span>+</span><span>3</span><span>*</span><span>x0</span><span>**</span><span>2</span><span>-</span><span>2</span><span>*</span><span>x0</span><span>-</span><span>5</span><span>)</span><span>/</span><span>(</span><span>3</span><span>*</span><span>x0</span><span>**</span><span>2</span><span>+</span><span>6</span><span>*</span><span>x0</span><span>-</span><span>2</span><span>)</span>
<span>print</span><span>(</span><span>"x1 ="</span><span>,</span> <span>x1</span><span>)</span>
</pre>



<pre><span></span>x1 = -688.4516883116648
</pre>



<p>Зауважте, що <span>\(f^{\prime}(x_0) = -0.0077\)</span> (близько до 0), а похибка в точці <span>\(x_1\)</span> становить приблизно 324880000 (дуже велика).</p>
<p><strong>СПРОБУЙТЕ!</strong> Розглянемо поліном <span>\(f(x) = x^3 - 100x^2 - x + 100\)</span>. Цей поліном має корені в точках <span>\(x = 1\)</span> та <span>\(x = 100\)</span>. Використайте метод Ньютона-Рафсона для знаходження кореня <span>\(f\)</span>, починаючи з <span>\(x_0 = 0\)</span>.</p>
<p>При <span>\(x_0 = 0, f(x_0) = 100\)</span>, а <span>\(f'(x) = -1\)</span>. Крок Ньютона дає <span>\(x_1 = 0 - \frac{100}{-1} = 100\)</span>, що є коренем <span>\(f\)</span>. Однак, зауважте, що цей корінь знаходиться набагато далі від початкового припущення, ніж інший корінь при <span>\(x = 1\)</span>, і це може бути не той корінь, який ви очікували отримати з початкового припущення 0.</p>
```
