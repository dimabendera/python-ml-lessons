<h1>Підсумок<a href="#summary" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Явне інтегрування функцій часто неможливе або незручне, тому замість нього необхідно використовувати чисельні підходи.</p></li>
<li><p>Інтеграл Рімана, Правило трапецій та Правило Сімпсона є поширеними методами наближення інтегралів.</p></li>
<li><p>Кожен метод має порядок точності, який залежить від наближення площі під функцією.</p></li>
</ol>


<h1>Задачі<a href="#problems" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Напишіть функцію <span>\(my\_int\_calc(f, f0, a, b, N, option)\)</span>, де <span>\(f\)</span> є об'єктом функції, <span>\(a\)</span> та <span>\(b\)</span> є скалярами такими, що a &lt; b, <span>\(N\)</span> є додатним цілим числом, а <span>\(option\)</span> є рядком ‘rect`, ‘trap` або ‘simp`. Нехай <span>\(x\)</span> буде масивом, що починається з <span>\(a\)</span>, закінчується на <span>\(b\)</span>, містить <span>\(N\)</span> рівномірно розташованих елементів. Вихідний аргумент, <span>\(I\)</span>, має бути наближенням інтеграла <span>\(f(x)\)</span>, з початковою умовою <span>\(f0\)</span>, обчисленим відповідно до вхідного аргументу, <span>\(option\)</span>.</p></li>
<li><p>Напишіть функцію <span>\(my\_poly\_int(x, y)\)</span>, де <span>\(x\)</span> та <span>\(y\)</span> є одновимірними масивами однакового розміру, а елементи <span>\(x\)</span> є унікальними та розташовані у порядку зростання. Функція <span>\(my\_poly\_int\)</span> має (1) обчислити поліном Лагранжа, що проходить через усі точки, визначені <span>\(x\)</span> та <span>\(y\)</span>, і (2) повернути наближення площі під кривою, визначеною <span>\(x\)</span> та <span>\(y\)</span>, <span>\(I\)</span>, визначене як аналітичний інтеграл інтерполяційного полінома Лагранжа.</p></li>
<li><p>Коли <span>\(my\_poly\_int\)</span> працюватиме <em>гірше</em>, ніж метод трапецій?</p></li>
<li><p>Напишіть функцію <span>\(my\_num\_calc(f, a, b, n, option)\)</span>, де вихідний аргумент <span>\(I\)</span> є чисельним інтегралом <span>\(f\)</span>, об'єкта функції, обчисленим на сітці з <span>\(n\)</span> рівномірно розташованих точок, що починаються з <span>\(a\)</span> і закінчуються на <span>\(b\)</span>. Метод інтегрування, що використовується, має бути одним з наступних рядків, визначених параметром option: ‘rect`, ‘trap`, ‘simp`. Для методу прямокутників значення функції слід брати з правої кінцевої точки інтервалу. Ви можете припустити, що <span>\(n\)</span> є непарним.</p></li>
</ol>
<p>Попередження: У читалці індекси <span>\(x\)</span> починаються з <span>\(x_0\)</span>, а не з <span>\(x_1\)</span>; зверніть на це увагу при програмуванні ваших циклів. Непарні-парні індекси будуть перевернуті. Також термін <span>\(n\)</span>, наведений у Правилі Сімпсона, позначає кількість підінтервалів, а не кількість точок, як зазначено у вхідному аргументі, <span>\(n\)</span>.</p>
<p>Тестові випадки:</p>
<pre><span></span><span>In</span><span>:</span> <span>f</span> <span>=</span> <span>lambda</span> <span>x</span><span>:</span> <span>x</span><span>**</span><span>2</span>
    <span>my_num_int</span><span>(</span><span>f</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>,</span> <span>3</span><span>,</span> <span>'rect'</span><span>)</span>
<span>Out</span><span>:</span> <span>0.625</span>
   
<span>In</span><span>:</span> <span>my_num_int</span><span>(</span><span>f</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>,</span> <span>3</span><span>,</span> <span>'trap'</span><span>)</span>
<span>Out</span><span>:</span> <span>0.375</span>
   
<span>In</span><span>:</span> <span>my_num_int</span><span>(</span><span>f</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>,</span> <span>3</span><span>,</span> <span>'simp'</span><span>)</span>
<span>Out</span><span>:</span> <span>0.3333333333333333</span>
   
<span>In</span><span>:</span> <span>f</span> <span>=</span> <span>lambda</span> <span>x</span><span>:</span> <span>np</span><span>.</span><span>exp</span><span>(</span><span>x</span><span>**</span><span>2</span><span>)</span>
    <span>my_num_int</span><span>(</span><span>f</span><span>,</span> <span>-</span><span>1</span><span>,</span> <span>1</span><span>,</span> <span>101</span><span>,</span> <span>'simp'</span><span>)</span>
<span>Out</span><span>:</span> <span>2.9253035883926493</span>
   
<span>In</span><span>:</span> <span>my_num_int</span><span>(</span><span>f</span><span>,</span> <span>-</span><span>1</span><span>,</span> <span>1</span><span>,</span> <span>10001</span><span>,</span> <span>'simp'</span><span>)</span>
<span>Out</span><span>:</span> <span>2.925303491814364</span>
   
<span>In</span><span>:</span> <span>my_num_int</span><span>(</span><span>f</span><span>,</span> <span>-</span><span>1</span><span>,</span> <span>1</span><span>,</span> <span>100001</span><span>,</span> <span>'simp'</span><span>)</span>
<span>Out</span><span>:</span> <span>2.9253034918143634</span>
</pre>

<ol>
<li><p>Попередній розділ продемонстрував, що деякі функції можуть бути виражені як нескінченна сума поліномів (тобто ряд Тейлора). Інші функції, зокрема періодичні, можуть бути записані як нескінченна сума синусоїдальних і косинусоїдальних хвиль. Для цих функцій,</p></li>
</ol>

\[f(x)= \frac{A_0}{2}+\sum_{n=1}^{\infty}A_n\ \cos{(nx)} + B_n\ \sin{(nx)}\]
<p>Можна показати, що значення <span>\(A_n\)</span> та <span>\(B_n\)</span> можна обчислити за допомогою наступних формул:</p>

\[A_n= \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos{(nx)}\ dx\]

\[B_n= \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin{(nx)}\ dx\]
<p>Так само, як і ряди Тейлора, функції можна наближати, обрізаючи ряд Фур'є на деякому <span>\(n = N\)</span>. Ряди Фур'є можуть бути використані для наближення деяких особливо складних функцій, таких як ступінчаста функція, і вони є основою багатьох інженерних застосувань, таких як обробка сигналів.</p>
<p>Напишіть функцію <span>\(my\_fourier\_coef(f, n)\)</span>, з виходом <span>\([A_n, B_n]\)</span>, де <span>\(f\)</span> є об'єктом функції, яка є <span>\(2\pi\)</span>-періодичною. Функція <span>\(my\_fourier\_coef\)</span> має обчислити <span>\(n\)</span>-ті коефіцієнти Фур'є, <span>\(A_n\)</span> та <span>\(B_n\)</span>, у ряді Фур'є для <span>\(f\)</span>, визначені двома формулами, наведеними раніше. Ви повинні використовувати функцію <span>\(quad\)</span> для виконання інтегрування.</p>
<p>Тестові випадки:</p>
<p>Використовуйте наступну функцію для побудови графіків аналітичних та наближених функцій за допомогою рядів Фур'є.</p>
<pre><span></span> <span>def</span> <span>plot_results</span><span>(</span><span>f</span><span>,</span> <span>N</span><span>):</span>
    <span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>-</span><span>np</span><span>.</span><span>pi</span><span>,</span> <span>np</span><span>.</span><span>pi</span><span>,</span> <span>10000</span><span>)</span>
    <span>[</span><span>A0</span><span>,</span> <span>B0</span><span>]</span> <span>=</span> <span>my_fourier_coef</span><span>(</span><span>f</span><span>,</span> <span>0</span><span>)</span>
    <span>y</span> <span>=</span> <span>A0</span><span>*</span><span>np</span><span>.</span><span>ones</span><span>(</span><span>len</span><span>(</span><span>x</span><span>))</span><span>/</span><span>2</span>
    <span>for</span> <span>n</span> <span>in</span> <span>range</span><span>(</span><span>1</span><span>,</span> <span>N</span><span>):</span>
        <span>[</span><span>An</span><span>,</span> <span>Bn</span><span>]</span> <span>=</span> <span>my_fourier_coef</span><span>(</span><span>f</span><span>,</span> <span>n</span><span>)</span>
        <span>y</span> <span>+=</span> <span>An</span><span>*</span><span>np</span><span>.</span><span>cos</span><span>(</span><span>n</span><span>*</span><span>x</span><span>)</span><span>+</span><span>Bn</span><span>*</span><span>np</span><span>.</span><span>sin</span><span>(</span><span>n</span><span>*</span><span>x</span><span>)</span>
    <span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span><span>6</span><span>))</span>
    <span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>f</span><span>(</span><span>x</span><span>),</span> <span>label</span> <span>=</span> <span>'analytic'</span><span>)</span>
    <span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>label</span> <span>=</span> <span>'approximate'</span><span>)</span>
    <span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'x'</span><span>)</span>
    <span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'y'</span><span>)</span>
    <span>plt</span><span>.</span><span>grid</span><span>()</span>
    <span>plt</span><span>.</span><span>legend</span><span>()</span>
    <span>plt</span><span>.</span><span>title</span><span>(</span><span>f</span><span>'</span><span>{</span><span>N</span><span>}</span><span>th Order Fourier Approximation'</span><span>)</span>
    <span>plt</span><span>.</span><span>show</span><span>()</span>
   
 <span>f</span> <span>=</span> <span>lambda</span> <span>x</span><span>:</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>np</span><span>.</span><span>exp</span><span>(</span><span>x</span><span>))</span>
 <span>N</span> <span>=</span> <span>2</span>
 <span>plot_results</span><span>(</span><span>f</span><span>,</span> <span>N</span><span>)</span>
</pre>

<p><img alt="" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/21.06.01-Solution_for_Question_4.jpg"/></p>
<pre><span></span> <span>N</span> <span>=</span> <span>2</span>
 <span>plot_results</span><span>(</span><span>f</span><span>,</span> <span>N</span><span>)</span>
</pre>

<p><img alt="" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/21.06.02-Solution_for_Question_4.jpg"/></p>
<pre><span></span> <span>f</span> <span>=</span> <span>lambda</span> <span>x</span><span>:</span> <span>np</span><span>.</span><span>mod</span><span>(</span><span>x</span><span>,</span> <span>np</span><span>.</span><span>pi</span><span>/</span><span>2</span><span>)</span>
 <span>N</span> <span>=</span> <span>5</span>
 <span>plot_results</span><span>(</span><span>f</span><span>,</span> <span>N</span><span>)</span>
</pre>

<p><img alt="" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/21.06.03-Solution_for_Question_4.jpg"/></p>
<pre><span></span> <span>N</span> <span>=</span> <span>20</span>
 <span>plot_results</span><span>(</span><span>f</span><span>,</span> <span>N</span><span>)</span>
</pre>

<p><img alt="" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/21.06.04-Solution_for_Question_4.jpg"/></p>
<pre><span></span> <span>f</span> <span>=</span> <span>lambda</span> <span>x</span><span>:</span> <span>(</span><span>x</span> <span>&gt;</span> <span>-</span><span>np</span><span>.</span><span>pi</span><span>/</span><span>2</span><span>)</span> <span>&amp;</span> <span>(</span><span>x</span> <span>&lt;</span> <span>np</span><span>.</span><span>pi</span><span>/</span><span>2</span><span>)</span>
 <span>N</span> <span>=</span> <span>2</span>
 <span>plot_results</span><span>(</span><span>f</span><span>,</span> <span>N</span><span>)</span>
</pre>

<p><img alt="" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/21.06.05-Solution_for_Question_4.jpg"/></p>
<pre><span></span> <span>N</span> <span>=</span> <span>20</span>
 <span>plot_results</span><span>(</span><span>f</span><span>,</span> <span>N</span><span>)</span>
</pre>

<p><img alt="" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/21.06.06-Solution_for_Question_4.jpg"/></p>
<ol>
<li><p>Для числової сітки з кроком <span>\(h\)</span>, Правило Буля для наближення інтегралів стверджує, що</p></li>
</ol>

\[\int_{x_i}^{x_{i+4}} f(x) dx \approx \frac{3h}{90} \left[7f(x_i)+32f(x_{i+1})+12f(x_{i+2})+32f(x_{i+3})+7f(x_{i+4})\right].\]
<p>Покажіть, що Правило Буля є <span>\(O(h^7)\)</span> на одному підінтервалі.</p>
