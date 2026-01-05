<h1>Підсумок<a href="#summary" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Цикли надають механізм для виконання кодом повторюваних завдань; тобто ітерації.</p></li>
<li><p>Існує два види циклів: for-цикли та while-цикли.</p></li>
<li><p>Цикли важливі для побудови ітераційних рішень проблем.</p></li>
<li><p>Генератори надають ще один лаконічний спосіб ітерації послідовності.</p></li>
</ol>


<h1>Задачі<a href="#problems" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Яким буде значення y після виконання наступного коду?</p></li>
</ol>


<pre><span></span><span>y</span> <span>=</span> <span>0</span>
<span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>1000</span><span>):</span>
    <span>for</span> <span>j</span> <span>in</span> <span>range</span><span>(</span><span>1000</span><span>):</span>
        <span>if</span> <span>i</span> <span>==</span> <span>j</span><span>:</span>
            <span>y</span> <span>+=</span> <span>1</span>
</pre>



<ol>
<li><p>Напишіть функцію <em>my_max(x)</em>, яка повертає максимальне (найбільше) значення в <em>x</em>. Не використовуйте вбудовану функцію Python <em>max</em>.</p></li>
</ol>
<ol>
<li><p>Напишіть функцію <em>my_n_max(x, n)</em>, яка повертає список, що складається з n найбільших елементів <em>x</em>. Ви можете використовувати функцію Python <em>max</em>. Ви також можете припустити, що <em>x</em> є одновимірним списком без дублікатів, а <em>n</em> — це строго додатне ціле число, менше за довжину <em>x</em></p></li>
</ol>


<pre><span></span><span>x</span> <span>=</span> <span>[</span><span>7</span><span>,</span> <span>9</span><span>,</span> <span>10</span><span>,</span> <span>5</span><span>,</span> <span>8</span><span>,</span> <span>3</span><span>,</span> <span>4</span><span>,</span> <span>6</span><span>,</span> <span>2</span><span>,</span> <span>1</span><span>]</span>

<span>def</span> <span>my_n_max</span><span>(</span><span>x</span><span>,</span> <span>n</span><span>):</span>
    <span># напишіть тут код вашої функції</span>
    
    <span>return</span> <span>out</span>
</pre>





<pre><span></span><span># Вивід = [10, 9, 8]</span>
<span>out</span> <span>=</span> <span>my_n_max</span><span>(</span><span>x</span><span>,</span> <span>n</span><span>)</span>
<span>print</span><span>(</span><span>out</span><span>)</span>
</pre>



<ol>
<li><p>Нехай <em>m</em> — матриця додатних цілих чисел. Напишіть функцію <em>my_trig_odd_even(m)</em>, яка повертає масив <em>q</em>, де q[i, j] = sin (m[i, j]), якщо m[i, j] парне, і q[i, j] = cos (m[i, j]), якщо m[i, j] непарне.</p></li>
</ol>
<ol>
<li><p>Нехай <em>P</em> — це масив розміром <span>\(m \times p\)</span>, а <em>Q</em> — масив розміром <span>\(p \times n\)</span>. Як ви дізнаєтеся пізніше в цій книзі, <span>\(M = P \times Q\)</span> визначається як <span>\(M[i, j] = \sum_{k=1}^{p}P[i, k]\cdot Q[k, j]\)</span>. Напишіть функцію *my_mat_mult(P, Q)*, яка використовує for-цикли для обчислення <em>M</em>, добутку матриць <em>P</em> і <em>Q</em>. Підказка: Вам може знадобитися до трьох вкладених for-циклів. Не використовуйте функцію <em>np.dot</em>.</p></li>
</ol>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>

<span>def</span> <span>my_mat_mult</span><span>(</span><span>P</span><span>,</span> <span>Q</span><span>):</span>
    <span># напишіть тут код вашої функції</span>
    
    <span>return</span> <span>M</span>
</pre>





<pre><span></span><span># Вивід:</span>
<span>#  array([[3., 3., 3.],</span>
<span>#        [3., 3., 3.],</span>
<span>#        [3., 3., 3.]])</span>

<span>P</span> <span>=</span> <span>np</span><span>.</span><span>ones</span><span>((</span><span>3</span><span>,</span> <span>3</span><span>))</span>
<span>my_mat_mult</span><span>(</span><span>P</span><span>,</span> <span>P</span><span>)</span>
</pre>





<pre><span></span><span># Вивід:</span>
<span># array([[30, 30, 30],</span>
<span>#       [70, 70, 70]])</span>

<span>P</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>,</span> <span>4</span><span>],</span> <span>[</span><span>5</span><span>,</span> <span>6</span><span>,</span> <span>7</span><span>,</span> <span>8</span><span>]])</span>
<span>Q</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>1</span><span>,</span> <span>1</span><span>,</span> <span>1</span><span>],</span> <span>[</span><span>2</span><span>,</span> <span>2</span><span>,</span> <span>2</span><span>],</span> <span>[</span><span>3</span><span>,</span> <span>3</span><span>,</span> <span>3</span><span>],</span> <span>[</span><span>4</span><span>,</span> <span>4</span><span>,</span> <span>4</span><span>]])</span>
<span>my_mat_mult</span><span>(</span><span>P</span><span>,</span> <span>Q</span><span>)</span>
</pre>



<ol>
<li><p>Відсотки, <span>\(i\)</span>, на основну суму, <span>\(P_0\)</span>, є платою за дозвіл банку використовувати ваші гроші. Складні відсотки накопичуються за формулою <span>\(P_n = (1 + i)P_{n-1}\)</span>, де n — період нарахування, зазвичай у місяцях або роках. Напишіть функцію <em>my_saving_plan(P0, i, goal)</em>, яка повертає кількість років, за які <span>\(P_0\)</span> досягне значення goal за <span>\(i\%\)</span> річних відсотків, що нараховуються щорічно.</p></li>
</ol>


<pre><span></span><span>def</span> <span>my_saving_plan</span><span>(</span><span>P0</span><span>,</span> <span>i</span><span>,</span> <span>goal</span><span>):</span>
    <span># напишіть тут код вашої функції</span>
    
    <span>return</span> <span>years</span>
</pre>





<pre><span></span><span># Вивід: 15</span>
<span>my_saving_plan</span><span>(</span><span>1000</span><span>,</span> <span>0.05</span><span>,</span> <span>2000</span><span>)</span>
</pre>





<pre><span></span><span># Вивід: 11</span>
<span>my_saving_plan</span><span>(</span><span>1000</span><span>,</span> <span>0.07</span><span>,</span> <span>2000</span><span>)</span>
</pre>





<pre><span></span><span># Вивід: 21</span>
<span>my_saving_plan</span><span>(</span><span>500</span><span>,</span> <span>0.07</span><span>,</span> <span>2000</span><span>)</span>
</pre>



<ol>
<li><p>Напишіть функцію <em>my_find(M)</em>, де вивід — це список індексів <em>i</em>, де M[i] дорівнює 1. Ви можете припустити, що <em>M</em> — це список, що складається лише з одиниць та нулів. Не використовуйте вбудовану функцію Python find.</p></li>
</ol>


<pre><span></span><span># Вивід: [0, 2, 3]</span>

<span>M</span> <span>=</span> <span>[</span><span>1</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>,</span> <span>1</span><span>,</span> <span>0</span><span>]</span>

<span>my_find</span><span>(</span><span>M</span><span>)</span>
</pre>



<ol>
<li><p>Припустімо, ви кидаєте два шестигранні кубики, кожна сторона яких має рівні шанси випасти. Напишіть функцію <em>my_monopoly_dice()</em>, де вивід — це сума значень двох кинутих кубиків, але з наступним додатковим правилом: якщо результати двох кидків кубиків однакові, то робиться ще один кидок, і нова сума додається до поточної суми. Наприклад, якщо на двох кубиках випало 3 і 4, то поточна сума має бути 7. Якщо на двох кубиках випало 1 і 1, то поточна сума має бути 2 плюс сума іншого кидка. Кидки припиняються, коли результати кубиків різні.</p></li>
</ol>
<ol>
<li><p>Число є простим, якщо воно ділиться без остачі лише на себе та на 1. Число 1 не є простим. Напишіть функцію <em>my_is_prime(n)</em>, де вивід дорівнює 1, якщо <em>n</em> є простим, і 0 в іншому випадку. Припустіть, що <em>n</em> — це строго додатне ціле число.</p></li>
</ol>
<ol>
<li><p>Напишіть функцію <em>my_n_primes(n)</em>, де primes — це список перших <em>n</em> простих чисел. Припустіть, що <em>n</em> — це строго додатне ціле число.</p></li>
</ol>
<ol>
<li><p>Напишіть функцію <em>my_n_fib_primes(n)</em>, де вивід <em>fib_primes</em> — це список перших <em>n</em> чисел, які є одночасно числами Фібоначчі та простими. Примітка: 1 не є простим числом. Підказка: Не використовуйте рекурсивну реалізацію чисел Фібоначчі. Функція для обчислення чисел Фібоначчі представлена в Розділі 6.1. Ви можете вільно використовувати цей код.</p></li>
</ol>


<pre><span></span><span>def</span> <span>my_n_fib_primes</span><span>(</span><span>n</span><span>):</span>
    <span># напишіть тут код вашої функції</span>
    
    <span>return</span> <span>fib_primes</span>
</pre>





<pre><span></span><span># Вивід: [3, 5, 13, 89, 233, 1597, 28657, 514229]</span>

<span>my_n_fib_primes</span><span>(</span><span>3</span><span>)</span>
</pre>





<pre><span></span><span># Вивід: [3, 5, 13]</span>

<span>my_n_fib_primes</span><span>(</span><span>8</span><span>)</span>
</pre>



<ol>
<li><p>Напишіть функцію <em>my_trig_odd_even(M)</em>, де вивід <span>\(Q[i, j] = sin (\pi/M[i, j])\)</span>, якщо <span>\(M[i,j]\)</span> непарне, і <span>\(Q[i, j] = cos (\pi/M[i, j])\)</span>, якщо <span>\(M[i, j]\)</span> парне. Припустіть, що M — це двовимірний масив строго додатних цілих чисел.</p></li>
</ol>


<pre><span></span><span>def</span> <span>my_trig_odd_even</span><span>(</span><span>M</span><span>):</span>
    <span># напишіть тут код вашої функції</span>
    
    <span>return</span> <span>Q</span>
</pre>





<pre><span></span><span># Вивід: [[0.8660, 0.7071], [0.8660, 0.4339]]</span>
<span>M</span> <span>=</span> <span>[[</span><span>3</span><span>,</span> <span>4</span><span>],</span> <span>[</span><span>6</span><span>,</span> <span>7</span><span>]]</span>
<span>my_trig_odd_even</span><span>(</span><span>M</span><span>)</span>
</pre>



<ol>
<li><p>Нехай <span>\(C\)</span> — це квадратний масив зв'язності, що містить нулі та одиниці. Ми говоримо, що точка <span>\(i\)</span> має зв'язок з точкою <span>\(j\)</span>, або <span>\(i\)</span> з'єднана з <span>\(j\)</span>, якщо <span>\(C [i , j ] = 1\)</span>. Зауважте, що зв'язки в цьому контексті є односпрямованими, тобто <span>\(C [i , j]\)</span> не обов'язково дорівнює <span>\(C [ j , i ]\)</span>. Наприклад, уявіть вулицю з одностороннім рухом від точки А до точки В. Якщо А з'єднана з В, то В не обов'язково з'єднана з А.</p></li>
</ol>
<p>Напишіть функцію <em>my_connectivity_mat_2_dict(C, names)</em>, де <em>C</em> — це масив зв'язності, а <em>names</em> — список рядків, що позначають назву точки. Тобто, <em>names[i]</em> — це назва <em>i-тої</em> точки.</p>
<p>Вихідна змінна <em>node</em> має бути словником, де ключ — це рядок з <em>names</em>, а значення — вектор, що містить індекси <em>j</em>, такі що <span>\(C[i,j] = 1\)</span>. Іншими словами, це список точок, до яких з'єднана точка <em>i</em>.</p>


<pre><span></span><span>def</span> <span>my_connectivity_mat_2_dict</span><span>(</span><span>C</span><span>,</span> <span>names</span><span>):</span>
    <span># напишіть тут код вашої функції</span>
    <span>return</span> <span>node</span>
</pre>





<pre><span></span><span>C</span> <span>=</span> <span>[[</span><span>0</span><span>,</span> <span>1</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>],</span> <span>[</span><span>1</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>],</span> <span>[</span><span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>],</span> <span>[</span><span>1</span><span>,</span> <span>1</span><span>,</span> <span>1</span><span>,</span> <span>0</span><span>]]</span>
<span>names</span> <span>=</span> <span>[</span><span>'Los Angeles'</span><span>,</span> <span>'New York'</span><span>,</span> <span>'Miami'</span><span>,</span> <span>'Dallas'</span><span>]</span>
</pre>





<pre><span></span><span># Вивід: node['Los Angeles'] = [2, 4]</span>
<span>#         node['New York'] = [1, 4]</span>
<span>#         node['Miami'] = [4]</span>
<span>#         node['Dallas'] = [1, 2, 3]</span>

<span>node</span> <span>=</span> <span>my_connectivity_mat_2_dict</span><span>(</span><span>C</span><span>,</span> <span>names</span><span>)</span>
</pre>



<ol>
<li><p>Перетворіть список <em>words</em> з символів нижнього регістру на символи верхнього регістру за допомогою генератора списків.</p></li>
</ol>


<pre><span></span><span>words</span> <span>=</span> <span>[</span><span>'test'</span><span>,</span> <span>'data'</span><span>,</span> <span>'analyze'</span><span>]</span>
</pre>
