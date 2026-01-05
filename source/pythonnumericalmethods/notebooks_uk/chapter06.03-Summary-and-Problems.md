<h1>Підсумок<a href="#summary" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Рекурсивна функція — це функція, яка викликає сама себе.</p></li>
<li><p>Рекурсивні функції корисні, коли проблеми мають ієрархічну, а не ітеративну структуру.</p></li>
<li><p>Розділяй та володарюй — це потужна стратегія вирішення проблем, яку можна використовувати для розв'язання складних задач.</p></li>
</ol>


<h1>Задачі<a href="#problems" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Напишіть функцію <em>my_sum(lst)</em>, де <em>lst</em> — це список, а вихідні дані — сума всіх елементів <em>lst</em>. Ви можете використовувати рекурсію або ітерацію для вирішення проблеми, але не використовуйте функцію Python <em>sum</em>.</p></li>
</ol>


<pre><span></span><span>def</span> <span>my_sum</span><span>(</span><span>lst</span><span>):</span>
    <span># Write your function code here</span>
    
    <span>return</span> <span>out</span>
</pre>





<pre><span></span><span># Вивід: 6</span>
<span>my_sum</span><span>([</span><span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>])</span>
</pre>





<pre><span></span><span># Вивід: 5050</span>
<span>my_sum</span><span>(</span><span>range</span><span>(</span><span>1</span><span>,</span><span>101</span><span>))</span>
</pre>



<ol>
<li><p>Поліноми Чебишова визначаються рекурсивно. Поліноми Чебишова поділяються на два види: першого та другого. Поліноми Чебишова першого роду, <span>\(T_n(x)\)</span>, та другого роду, <span>\(U_n(x)\)</span>, визначаються наступними рекурентними співвідношеннями:</p></li>
</ol>

<span>(3)<a href="#equation-4367a07a-a740-4bd8-9022-7786a3913980" title="Постійне посилання на це рівняння"></a></span>\[\begin{equation}
T_n(x) = \begin{cases}
    1 &amp; \text{if $n=0$}\\
    x &amp; \text{if $n=1$}\\
    2xT_{n-1}(x)-T_{n-2}(x) &amp; \text{otherwise}\\
    \end{cases}
\end{equation}\]

<span>(4)<a href="#equation-322292df-12d6-4864-81c7-5f4a65c25f8f" title="Постійне посилання на це рівняння"></a></span>\[\begin{equation}
U_n(x) = \begin{cases}
    1 &amp; \text{if $n=0$}\\
    2x &amp; \text{if $n=1$}\\
    2xU_{n-1}(x)-U_{n-2}(x) &amp; \text{otherwise}\\
    \end{cases}
\end{equation}\]
<p>Напишіть функцію <em>my_chebyshev_poly1(n,x)</em>, де вихідні дані <em>y</em> — це n-й поліном Чебишова першого роду, обчислений у точці <em>x</em>. Переконайтеся, що ваша функція може приймати спискові вхідні дані для <em>x</em>. Ви можете припустити, що <em>x</em> є списком. Вихідна змінна <em>y</em> також повинна бути списком.</p>


<pre><span></span><span>def</span> <span>my_chebyshev_poly1</span><span>(</span><span>n</span><span>,</span><span>x</span><span>):</span>
    <span># Write your function code here</span>
    
    <span>return</span> <span>y</span>
</pre>





<pre><span></span><span>x</span> <span>=</span> <span>[</span><span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>,</span> <span>4</span><span>,</span> <span>5</span><span>]</span>
</pre>





<pre><span></span><span># Вивід: [1, 1, 1, 1, 1]</span>
<span>my_chebyshev_poly1</span><span>(</span><span>0</span><span>,</span><span>x</span><span>)</span>
</pre>





<pre><span></span><span># Вивід: [1, 2, 3, 4, 5]</span>
<span>my_chebyshev_poly1</span><span>(</span><span>1</span><span>,</span><span>x</span><span>)</span>
</pre>





<pre><span></span><span># Вивід: [1, 26, 99, 244, 485]</span>
<span>my_chebyshev_poly1</span><span>(</span><span>3</span><span>,</span><span>x</span><span>)</span>
</pre>



<ol>
<li><p>Функція Акермана, <em>A</em>, — це швидко зростаюча функція, яка визначається рекурсивним співвідношенням:</p></li>
</ol>

<span>(5)<a href="#equation-217e7fda-7a12-4a68-b900-49ab4af5ffc0" title="Постійне посилання на це рівняння"></a></span>\[\begin{equation}
A(m, n) = \begin{cases}
    n+1 &amp;\text{if $m=0$}\\
    A(m-1,1) &amp;\text{if  $m&gt;0$ and $n=1$}\\
    A(m-1,A(m,n-1)) &amp; \text{if  $m&gt;0$ and $n&gt;0$}\\
    \end{cases}
\end{equation}\]
<p>Напишіть функцію <em>my_ackermann(m,n)</em>, де вихідні дані — це функція Акермана, обчислена для <em>m</em> та <em>n</em>.</p>
<p><em>my_ackermann(4,4)</em> настільки велике, що його було б важко записати. Хоча функція Акермана не має багатьох практичних застосувань, обернена функція Акермана має кілька застосувань у плануванні руху роботів.</p>


<pre><span></span><span>def</span> <span>my_ackermann</span><span>(</span><span>m</span><span>,</span><span>n</span><span>):</span>
    <span># write your own function code here</span>
    <span>return</span> <span>out</span>
</pre>





<pre><span></span><span># Вивід: 3</span>
<span>my_ackermann</span><span>(</span><span>1</span><span>,</span><span>1</span><span>)</span>
</pre>





<pre><span></span><span># Вивід: 4</span>
<span>my_ackermann</span><span>(</span><span>1</span><span>,</span><span>2</span><span>)</span>
</pre>





<pre><span></span><span># Вивід: 9</span>
<span>my_ackermann</span><span>(</span><span>2</span><span>,</span><span>3</span><span>)</span>
</pre>





<pre><span></span><span># Вивід: 61</span>
<span>my_ackermann</span><span>(</span><span>3</span><span>,</span><span>3</span><span>)</span>
</pre>





<pre><span></span><span># Вивід: 125</span>
<span>my_ackermann</span><span>(</span><span>3</span><span>,</span><span>4</span><span>)</span>
</pre>



<ol>
<li><p>Функція <em>C(n,k)</em>, яка обчислює кількість різних способів унікального вибору <em>k</em> об'єктів з <em>n</em> без повторень, зазвичай використовується в багатьох статистичних застосуваннях. Наприклад, скільки існує морозива з трьома смаками, якщо є 10 смаків морозива? Щоб вирішити цю проблему, нам потрібно було б обчислити <em>C(10,3)</em>, кількість способів вибору трьох унікальних смаків морозива з 10. Функція <em>C</em> зазвичай називається "<em>n</em> по <em>k</em>". Ви можете припустити, що <em>n</em> та <em>k</em> є цілими числами.</p></li>
</ol>
<p>Якщо <em>n = k</em>, то очевидно, що <em>C(n,k) = 1</em>, оскільки існує лише один спосіб вибрати <em>n</em> об'єктів з <em>n</em> об'єктів.</p>
<p>Якщо <em>k = 1</em>, то <em>C(n,k) = n</em>, оскільки вибір кожного з <em>n</em> об'єктів є способом вибору одного об'єкта з <em>n</em>. Для всіх інших випадків <em>C(n,k) = C(n-1,k) + C(n-1,k-1)</em>. Чи можете ви зрозуміти, чому?</p>
<p>Напишіть функцію <em>my_n_choose_k(n,k)</em>, яка обчислює кількість способів унікального вибору <span>\(k\)</span> об'єктів з <span>\(n\)</span> об'єктів без повторень.</p>


<pre><span></span><span>def</span> <span>my_n_choose_k</span><span>(</span><span>n</span><span>,</span><span>k</span><span>):</span>
    <span># Write your own function code here</span>
    <span>return</span> <span>out</span>
</pre>





<pre><span></span><span># Вивід: 10</span>
<span>my_n_choose_k</span><span>(</span><span>10</span><span>,</span><span>1</span><span>)</span>
</pre>





<pre><span></span><span># Вивід: 1</span>
<span>my_n_choose_k</span><span>(</span><span>10</span><span>,</span><span>10</span><span>)</span>
</pre>





<pre><span></span><span># Вивід: 120</span>
<span>my_n_choose_k</span><span>(</span><span>10</span><span>,</span><span>3</span><span>)</span>
</pre>



<ol>
<li><p>При покупках, оплачених готівкою, продавець повинен повернути надмірно сплачені гроші. Це зазвичай називається "видачею решти". Купюри та монети, необхідні для правильної видачі решти, можуть бути визначені рекурсивним співвідношенням. Якщо сплачена сума перевищує вартість на \<span>\(100, то поверніть стодоларову купюру разом з результатом рекурсивного виклику функції видачі решти, віднявши \\\)</span>100 від сплаченої суми. Якщо сплачена сума перевищує вартість товару на \<span>\(50, то поверніть п'ятдесятидоларову купюру разом з результатом рекурсивного виклику функції видачі решти, віднявши \\\)</span>50. Подібні умови можуть бути надані для кожного номіналу валюти США. Номінали валюти США, у доларах, становлять 100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05 та 0.01. Для цієї задачі ми ігноруватимемо дводоларову купюру, яка не перебуває в широкому обігу. Ви можете припустити, що <em>cost</em> та
<em>paid</em> є скалярами, і що <em>paid &gt;= cost</em>. Вихідна
змінна <em>change</em> повинна бути списком, як показано в
тестовому прикладі.</p></li>
</ol>
<p>Використовуйте рекурсію для програмування функції <em>my_change(cost, paid)</em>, де <em>cost</em> — це вартість товару, <em>paid</em> — сплачена сума, а вихідні дані <em>change</em> — це список купюр та монет, які слід повернути продавцю. Примітка: Зверніть увагу на базовий випадок!</p>


<pre><span></span><span>def</span> <span>my_change</span><span>(</span><span>cost</span><span>,</span> <span>paid</span><span>):</span>
    <span># Write your own function code here</span>
    <span>return</span> <span>change</span>
</pre>





<pre><span></span><span># Вивід: [50.0, 20.0, 1.0, 1.0, 0.25, 0.10, 0.05, 0.01, 0.01, 0.01]</span>
<span>my_change</span><span>(</span><span>27.57</span><span>,</span> <span>100</span><span>)</span>
</pre>



<ol>
<li><p>Золотий перетин, <span>\(\phi\)</span>, — це границя <span>\(\frac{F(n+1)}{F(n)}\)</span> при <em>n</em>, що прямує до нескінченності, де <em>F(n)</em> — це <em>n</em>-те число Фібоначчі, яке, як можна показати, дорівнює точно <span>\(\frac{1 + \sqrt{5}}{2}\)</span> і приблизно 1.62. Ми говоримо, що <span>\(G(n) = \frac{F(n+1)}{F(n)}\)</span> є <em>n</em>-м наближенням золотого перетину, і <span>\(G(1) = 1\)</span>.</p></li>
</ol>
<p>Можна показати, що <span>\(\phi\)</span> також є границею неперервного дробу:</p>

\[\varphi = 1 + \dfrac{1}{1 + \dfrac{1}{1 + \dfrac{1}{1 + \ddots}}}.\]
<p>Напишіть рекурсивну функцію із заголовком <em>my_golden_ratio(n)</em>, де вихідні дані — це <em>n</em>-те наближення золотого перетину відповідно до рекурсивного співвідношення неперервного дробу. Ви повинні використовувати наближення золотого перетину за допомогою неперервного дробу, а не визначення <span>\(G(n) = F(n+1)/F(n)\)</span>. Однак для обох визначень <span>\(G(1) = 1\)</span>.</p>
<p>Дослідження показали, що прямокутники зі співвідношенням сторін (тобто довжина, поділена на ширину), близьким до золотого перетину, є більш приємними, ніж прямокутники, які не відповідають цьому. Яке співвідношення сторін у багатьох широкоекранних телевізорів та кіноекранів?</p>


<pre><span></span><span>def</span> <span>my_golden_ratio</span><span>(</span><span>n</span><span>):</span>
    <span># Write your own function code here</span>
    <span>return</span> <span>out</span>
</pre>





<pre><span></span><span># Вивід: 1.618181818181818</span>
<span>my_golden_ratio</span><span>(</span><span>10</span><span>)</span>
</pre>





<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
<span>(</span><span>1</span> <span>+</span> <span>np</span><span>.</span><span>sqrt</span><span>(</span><span>5</span><span>))</span><span>/</span><span>2</span>
</pre>



<ol>
<li><p>Найбільший спільний дільник двох цілих чисел <em>a</em> та <em>b</em> — це найбільше ціле число, яке ділить обидва числа без остачі, і функція для його обчислення позначається як <em>gcd(a,b)</em>. Функцію <em>gcd</em> можна записати рекурсивно. Якщо <em>b</em> дорівнює 0, то <em>a</em> є найбільшим спільним дільником. В іншому випадку, <em>gcd(a,b) = gcd(b,a%b)</em>, де <em>a%b</em> — це остача від ділення <em>a</em> на <em>b</em>. Припустіть, що <em>a</em> та <em>b</em> є цілими числами.</p></li>
</ol>
<p>Напишіть рекурсивну функцію <em>my_gcd(a,b)</em>, яка обчислює найбільший спільний дільник <em>a</em> та <em>b</em>. Припустіть, що <em>a</em> та <em>b</em> є цілими числами.</p>


<pre><span></span><span>def</span> <span>my_gcd</span><span>(</span><span>a</span><span>,</span> <span>b</span><span>):</span>
    <span># Write your own function code here</span>
    <span>return</span> <span>gcd</span>
</pre>





<pre><span></span><span># Вивід: 2</span>
<span>my_gcd</span><span>(</span><span>10</span><span>,</span> <span>4</span><span>)</span>
</pre>





<pre><span></span><span># Вивід: 11</span>
<span>my_gcd</span><span>(</span><span>33</span><span>,</span> <span>121</span><span>)</span>
</pre>





<pre><span></span><span># Вивід: 1</span>
<span>my_gcd</span><span>(</span><span>18</span><span>,</span> <span>1</span><span>)</span>
</pre>



<ol>
<li><p>Трикутник Паскаля — це розташування чисел, де кожен рядок еквівалентний коефіцієнтам біноміального розкладу <span>\((x + y)^{(p-1)}\)</span>, де <em>p</em> — деяке додатне ціле число, більше або рівне 1. Наприклад, <span>\((x+y)^2 = 1 x^2 + 2 xy + 1 y^2\)</span>, тому третій рядок трикутника Паскаля — це 1 2 1.</p></li>
</ol>
<p>Нехай <span>\(R_{m}\)</span> представляє <em>m</em>-й рядок трикутника Паскаля, а <span>\(R_m(n)\)</span> — <span>\(n\)</span>-й елемент цього рядка. За визначенням, <span>\(R_m\)</span> має <em>m</em> елементів, і <span>\(R_m(1) = R_m(n) = 1\)</span>. Решта елементів обчислюються за наступним рекурсивним співвідношенням: <span>\(R_m(i) = R_{m-1}(i-1) + R_{m-1}(i)\)</span> для <span>\(i = 2,\ldots,m-1\)</span>. Перші кілька рядків трикутника Паскаля зображені на наступному малюнку. Ви можете припустити, що <em>m</em> є строго додатним цілим числом. Вихідна змінна <em>row</em> повинна бути списком.</p>

<p>Напишіть функцію <em>my_pascal_row(m)</em>, де вихідна змінна <em>row</em> — це <em>m</em>-й рядок трикутника Паскаля. Ви можете припустити, що <em>m</em> є строго додатним цілим числом.</p>


<pre><span></span><span>def</span> <span>my_pascal_row</span><span>(</span><span>m</span><span>):</span>
    <span># Write your own function code here</span>
    <span>return</span> <span>row</span>
</pre>





<pre><span></span><span># Вивід: [1]</span>
<span>my_pascal_row</span><span>(</span><span>1</span><span>)</span>
</pre>





<pre><span></span><span># Вивід: [1, 1]</span>
<span>my_pascal_row</span><span>(</span><span>2</span><span>)</span>
</pre>





<pre><span></span><span># Вивід: [1, 2, 1]</span>
<span>my_pascal_row</span><span>(</span><span>3</span><span>)</span>
</pre>





<pre><span></span><span># Вивід: [1, 3, 3, 1]</span>
<span>my_pascal_row</span><span>(</span><span>4</span><span>)</span>
</pre>





<pre><span></span><span># Вивід: [1, 4, 6, 4, 1]</span>
<span>my_pascal_row</span><span>(</span><span>5</span><span>)</span>
</pre>



<ol>
<li><p>Розглянемо матрицю розміром <span>\(n\times{n}\)</span> наступного вигляду:</p></li>
</ol>

\[\begin{split}A =
\left[{\begin{array}{l@{\quad}l@{\quad}l@{\quad}l@{\quad}l}
1 &amp; 1 &amp; 1 &amp; 1 &amp; 1\\ 
1 &amp; 0 &amp; 0 &amp; 0 &amp; 0\\ 
1 &amp; 0 &amp; 1 &amp; 1 &amp; 0\\
1 &amp; 0 &amp; 0 &amp; 1 &amp; 0\\
1 &amp; 1 &amp; 1 &amp; 1 &amp; 0
\end{array}}\right]
\end{split}\]
<p>де одиниці утворюють праву спіраль. Напишіть функцію <em>my_spiral_ones(n)</em>, яка створює матрицю розміром <span>\(n\times{n}\)</span> заданого вигляду. Зверніть увагу, що рекурсивні кроки повинні бути в правильному порядку (тобто одиниці йдуть вправо, потім вниз, потім вліво, потім вгору, потім вправо тощо).</p>


<pre><span></span><span>def</span> <span>my_spiral_ones</span><span>(</span><span>n</span><span>):</span>
    <span># Write your own function code here</span>
    <span>return</span> <span>A</span>
</pre>





<pre><span></span><span># Вивід: 1</span>
<span>my_spiral_ones</span><span>(</span><span>1</span><span>)</span>
</pre>





<pre><span></span><span># Вивід: </span>
<span># масив([[1, 1],</span>
<span>#       [0, 1]])</span>
<span>my_spiral_ones</span><span>(</span><span>2</span><span>)</span>
</pre>





<pre><span></span><span># Вивід:</span>
<span>#масив([[0, 1, 1],</span>
<span>#       [0, 0, 1],</span>
<span>#       [1, 1, 1]])</span>
<span>my_spiral_ones</span><span>(</span><span>3</span><span>)</span>
</pre>





<pre><span></span><span># Вивід:</span>
<span>#масив([[1, 0, 0, 0],</span>
<span>#       [1, 0, 1, 1],</span>
<span>#       [1, 0, 0, 1],</span>
<span>#       [1, 1, 1, 1]])</span>
<span>my_spiral_ones</span><span>(</span><span>4</span><span>)</span>
</pre>





<pre><span></span><span># Вивід:</span>
<span>#масив([[1, 1, 1, 1, 1],</span>
<span>#       [1, 0, 0, 0, 0],</span>
<span>#       [1, 0, 1, 1, 0],</span>
<span>#       [1, 0, 0, 1, 0],</span>
<span>#       [1, 1, 1, 1, 0]])</span>
<span>my_spiral_ones</span><span>(</span><span>5</span><span>)</span>
</pre>



<ol>
<li><p>Перепишіть функцію <em>my_spiral_ones</em> без використання рекурсії.</p></li>
<li><p>Намалюйте дерево рекурсії для <em>my_towers(4)</em>.</p></li>
<li><p>Перепишіть функцію "Ханойські вежі" з цього розділу без використання рекурсії.</p></li>
<li><p>Намалюйте дерево рекурсії для <em>my_quicksort([5 4 6 2 9 1 7 3])</em>.</p></li>
<li><p>Перепишіть функцію <em>quicksort</em> з цього розділу без використання рекурсії.</p></li>
</ol>
