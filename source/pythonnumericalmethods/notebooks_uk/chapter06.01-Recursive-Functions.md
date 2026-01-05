```html
<h1>Рекурсивні функції<a href="#recursive-functions" title="Permalink to this headline"></a></h1>
<p><strong>Рекурсивна</strong> функція — це функція, яка викликає саму себе. Вона працює подібно до циклів, які ми описували раніше, але іноді ситуація краще підходить для використання рекурсії, ніж циклів.</p>
<p>Кожна рекурсивна функція має два компоненти: <strong>базовий випадок</strong> та <strong>рекурсивний крок</strong>. <strong>Базовий випадок</strong> — це зазвичай найменше вхідне значення, яке має рішення, що легко перевіряється. Це також механізм, який зупиняє функцію від нескінченного виклику самої себе. <strong>Рекурсивний крок</strong> — це набір усіх випадків, коли робиться <strong>рекурсивний виклик</strong>, тобто виклик функції самої себе.</p>
<p>Як приклад, покажемо, як рекурсію можна використовувати для визначення та обчислення факторіала цілого числа. Факторіал цілого числа <span>\(n\)</span> — це <span>\(1 \times 2 \times 3 \times ... \times (n - 1) \times n\)</span>. Рекурсивне визначення можна записати так:</p>

<span>(1)<a href="#equation-6bf6b8f2-82ca-4456-89cd-bcb1eed73ae3" title="Permalink to this equation"></a></span>\[\begin{equation}
f(n) = \begin{cases}
    1 &amp;\text{якщо $n=1$}\\
    n \times f(n-1) &amp; \text{в іншому випадку}\\
    \end{cases}
\end{equation}\]
<p>Базовий випадок — це <span>\(n = 1\)</span>, який обчислюється тривіально: <span>\(f(1) = 1\)</span>. На рекурсивному кроці <span>\(n\)</span> множиться на результат рекурсивного виклику факторіала від <span>\(n - 1\)</span>.</p>
<p><strong>СПРОБУЙТЕ!</strong> Напишіть функцію для обчислення факторіала за допомогою рекурсії. Використайте свою функцію для обчислення факторіала числа 3.</p>


<pre><span></span><span>def</span> <span>factorial</span><span>(</span><span>n</span><span>):</span>
    <span>"""Обчислює та повертає факторіал n, 
    додатного цілого числа.
    """</span>
    <span>if</span> <span>n</span> <span>==</span> <span>1</span><span>:</span> <span># Базовий випадок!</span>
        <span>return</span> <span>1</span>
    <span>else</span><span>:</span> <span># Рекурсивний крок</span>
        <span>return</span> <span>n</span> <span>*</span> <span>factorial</span><span>(</span><span>n</span> <span>-</span> <span>1</span><span>)</span> <span># Рекурсивний виклик     </span>
</pre>





<pre><span></span><span>factorial</span><span>(</span><span>3</span><span>)</span>
</pre>



<pre><span></span>6
</pre>



<p><strong>ЩО ВІДБУВАЄТЬСЯ?</strong> Спочатку згадаємо, що коли Python виконує функцію, він створює робочий простір для змінних, які створюються в цій функції, і щоразу, коли функція викликає іншу функцію, вона чекає, поки та функція поверне відповідь, перш ніж продовжити. У програмуванні цей робочий простір називається стеком. Подібно до стопки тарілок на нашій кухні, елементи в стеку додаються або видаляються з вершини стека, за принципом "останнім увійшов, першим вийшов" (LIFO). Наприклад, у виразі <code><span>np.sin(np.tan(x))</span></code>, функція <code><span>sin</span></code> повинна чекати, поки <code><span>tan</span></code> поверне результат, перш ніж вона зможе бути обчислена. Хоча рекурсивна функція викликає саму себе, застосовуються ті ж самі правила.</p>
<ol>
<li><p>Робиться виклик <code><span>factorial(3)</span></code>, відкривається новий робочий простір для обчислення <code><span>factorial(3)</span></code>.</p></li>
<li><p>Вхідний аргумент зі значенням 3 порівнюється з 1. Оскільки вони не рівні, виконується оператор else.</p></li>
<li><p>Необхідно обчислити <code><span>3*factorial(2)</span></code>. Відкривається новий робочий простір для обчислення <code><span>factorial(2)</span></code>.</p></li>
<li><p>Вхідний аргумент зі значенням 2 порівнюється з 1. Оскільки вони не рівні, виконується оператор else.</p></li>
<li><p>Необхідно обчислити <code><span>2*factorial(1)</span></code>. Відкривається новий робочий простір для обчислення <code><span>factorial(1)</span></code>.</p></li>
<li><p>Вхідний аргумент зі значенням 1 порівнюється з 1. Оскільки вони рівні, виконується оператор if.</p></li>
<li><p>Змінній, що повертається, присвоюється значення 1. <code><span>factorial(1)</span></code> завершується з результатом 1.</p></li>
<li><p><code><span>2*factorial(1)</span></code> можна обчислити як <span>\(2 \times 1 = 2\)</span>. Результату присвоюється значення 2. <code><span>factorial(2)</span></code> завершується з результатом 2.</p></li>
<li><p><code><span>3*factorial(2)</span></code> можна обчислити як <span>\(3 \times 2 = 6\)</span>. Результату присвоюється значення 6. <code><span>factorial(3)</span></code> завершується з результатом 6.</p></li>
</ol>
<p>Порядок рекурсивних викликів можна зобразити за допомогою дерева рекурсії, показаного на наступному малюнку для <code><span>factorial(3)</span></code>. Дерево рекурсії — це діаграма викликів функцій, з'єднаних пронумерованими стрілками, що показують порядок, у якому були зроблені виклики.</p>

<p>Числа Фібоначчі спочатку були розроблені для моделювання ідеалізованого зростання популяції кроликів. З того часу було виявлено, що вони мають значення в багатьох природних явищах. Числа Фібоначчі можна згенерувати за допомогою наступної рекурсивної формули. Зауважте, що рекурсивний крок містить два рекурсивні виклики, а також є два базові випадки (тобто два випадки, які змушують рекурсію зупинитися).</p>

<span>(2)<a href="#equation-8c06b779-e232-4cdc-bf9e-7e2ec502479c" title="Permalink to this equation"></a></span>\[\begin{equation}
F(n) = \begin{cases}
    1 &amp;\text{якщо $n=1$}\\
    1 &amp;\text{якщо $n=2$}\\
    F(n-1) + F(n-2) &amp; \text{в іншому випадку}\\
    \end{cases}
\end{equation}\]
<p><strong>СПРОБУЙТЕ!</strong> Напишіть рекурсивну функцію для обчислення <em>n-го</em> числа Фібоначчі. Використайте свою функцію для обчислення перших п'яти чисел Фібоначчі. Намалюйте відповідне дерево рекурсії.</p>


<pre><span></span><span>def</span> <span>fibonacci</span><span>(</span><span>n</span><span>):</span>
    <span>"""Обчислює та повертає n-те число Фібоначчі, 
    де n - додатне ціле число.
    """</span>
    <span>if</span> <span>n</span> <span>==</span> <span>1</span><span>:</span> <span># перший базовий випадок</span>
        <span>return</span> <span>1</span>
    <span>elif</span> <span>n</span> <span>==</span> <span>2</span><span>:</span> <span># другий базовий випадок</span>
        <span>return</span> <span>1</span>
    <span>else</span><span>:</span> <span># Рекурсивний крок</span>
        <span>return</span> <span>fibonacci</span><span>(</span><span>n</span><span>-</span><span>1</span><span>)</span> <span>+</span> <span>fibonacci</span><span>(</span><span>n</span><span>-</span><span>2</span><span>)</span> <span># Рекурсивний виклик </span>
</pre>





<pre><span></span><span>print</span><span>(</span><span>fibonacci</span><span>(</span><span>1</span><span>))</span>
<span>print</span><span>(</span><span>fibonacci</span><span>(</span><span>2</span><span>))</span>
<span>print</span><span>(</span><span>fibonacci</span><span>(</span><span>3</span><span>))</span>
<span>print</span><span>(</span><span>fibonacci</span><span>(</span><span>4</span><span>))</span>
<span>print</span><span>(</span><span>fibonacci</span><span>(</span><span>5</span><span>))</span>
</pre>



<pre><span></span>1
1
2
3
5
</pre>



<p><img alt="дерево рекурсії для fibonacci(5)" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/06.01.02-Recursion_tree_for_fibonacci.png"/></p>
<p>Як вправу, розгляньте наступну модифікацію функції <code><span>fibonacci</span></code>, де результати кожного рекурсивного виклику виводяться на екран.</p>
<p><strong>ПРИКЛАД:</strong> Напишіть функцію <code><span>fibonacci_display</span></code>, що базується на модифікації <code><span>fibonacci</span></code>. Чи можете ви визначити порядок, у якому числа Фібоначчі з'являться на екрані для fibonacci(5)?</p>


<pre><span></span><span>def</span> <span>fibonacci_display</span><span>(</span><span>n</span><span>):</span>
    <span>"""Обчислює та повертає n-те число Фібоначчі, 
    де n - додатне ціле число.
    """</span>
    <span>if</span> <span>n</span> <span>==</span> <span>1</span><span>:</span> <span># перший базовий випадок</span>
        <span>out</span> <span>=</span> <span>1</span>
        <span>print</span><span>(</span><span>out</span><span>)</span>
        <span>return</span> <span>out</span>
    <span>elif</span> <span>n</span> <span>==</span> <span>2</span><span>:</span> <span># другий базовий випадок</span>
        <span>out</span> <span>=</span> <span>1</span>
        <span>print</span><span>(</span><span>out</span><span>)</span>
        <span>return</span> <span>out</span>
    <span>else</span><span>:</span> <span># Рекурсивний крок</span>
        <span>out</span> <span>=</span> <span>fibonacci_display</span><span>(</span><span>n</span><span>-</span><span>1</span><span>)</span><span>+</span><span>fibonacci_display</span><span>(</span><span>n</span><span>-</span><span>2</span><span>)</span>
        <span>print</span><span>(</span><span>out</span><span>)</span>
        <span>return</span> <span>out</span> <span># Рекурсивний виклик </span>
</pre>





<pre><span></span><span>fibonacci_display</span><span>(</span><span>5</span><span>)</span>
</pre>



<pre><span></span>1
1
2
1
3
1
1
2
5
</pre>

<pre><span></span>5
</pre>



<p>Зверніть увагу, що кількість рекурсивних викликів стає дуже великою навіть для відносно малих вхідних значень <code><span>n</span></code>. Якщо ви не згодні, спробуйте намалювати дерево рекурсії для <code><span>fibonacci(10)</span></code>. Якщо ви спробуєте свою немодифіковану функцію для вхідних значень близько 35, ви помітите значний час обчислення.</p>


<pre><span></span><span>fibonacci</span><span>(</span><span>35</span><span>)</span>
</pre>



<pre><span></span>9227465
</pre>



<p>Існує ітеративний метод обчислення <em>n-го</em> числа Фібоначчі, який вимагає лише одного робочого простору.</p>
<p><strong>ПРИКЛАД:</strong> Ітеративна реалізація для обчислення чисел Фібоначчі.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>

<span>def</span> <span>iter_fib</span><span>(</span><span>n</span><span>):</span>
    <span>fib</span> <span>=</span> <span>np</span><span>.</span><span>ones</span><span>(</span><span>n</span><span>)</span>
    
    <span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>2</span><span>,</span> <span>n</span><span>):</span>
        <span>fib</span><span>[</span><span>i</span><span>]</span> <span>=</span> <span>fib</span><span>[</span><span>i</span> <span>-</span> <span>1</span><span>]</span> <span>+</span> <span>fib</span><span>[</span><span>i</span> <span>-</span> <span>2</span><span>]</span>
        
    <span>return</span> <span>fib</span>
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Обчисліть <em>25-те</em> число Фібоначчі за допомогою <code><span>iter_fib</span></code> та <code><span>fibonacci</span></code>. Використайте магічну команду <code><span>timeit</span></code>, щоб виміряти час виконання для кожної з них. Зверніть увагу на велику різницю в часі виконання.</p>


<pre><span></span><span>%</span><span>timeit</span> iter_fib(25)
</pre>



<pre><span></span>8.52 µs ± 141 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
</pre>





<pre><span></span><span>%</span><span>timeit</span> fibonacci(25)
</pre>



<pre><span></span>16.5 ms ± 260 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
</pre>



<p>У попередньому прикладі ви можете бачити, що ітеративна версія працює набагато швидше, ніж її рекурсивний аналог. Загалом, ітеративні функції швидші за рекурсивні, які виконують те саме завдання. Тож навіщо взагалі використовувати рекурсивні функції? Існують деякі методи розв'язання, які мають природно рекурсивну структуру. У цих випадках зазвичай дуже важко написати аналог з використанням циклів. Основна цінність написання рекурсивних функцій полягає в тому, що їх зазвичай можна написати набагато компактніше, ніж ітеративні функції. Ціною покращеної компактності є додатковий час виконання.</p>
<p>Зв'язок між вхідними аргументами та часом виконання детальніше розглядається пізніше в розділі про складність.</p>
<p><strong>ПОРАДА!</strong> Намагайтеся писати функції ітеративно, коли це зручно. Ваші функції працюватимуть швидше.</p>
<p><strong>ПРИМІТКА!</strong> Коли ми використовуємо рекурсивний виклик, як показано вище, нам потрібно переконатися, що він може досягти базового випадку, інакше це призведе до нескінченної рекурсії. У Python, коли ми виконуємо рекурсивну функцію для великого вхідного значення, яке не може досягти базового випадку, ми зіткнемося з помилкою "maximum recursion depth exceeded error" (перевищено максимальну глибину рекурсії). Спробуйте наступний приклад і подивіться, що ви отримаєте.</p>


<pre><span></span><span>factorial</span><span>(</span><span>5000</span><span>)</span>
</pre>



<pre><span></span><span>---------------------------------------------------------------------------</span>
<span>RecursionError</span><span>                            </span>Traceback (most recent call last)
<span>&lt;</span><span>ipython</span><span>-</span><span>input</span><span>-</span><span>11</span><span>-</span><span>4</span><span>d2572cc43ba</span><span>&gt;</span> <span>in</span> <span>&lt;</span><span>module</span><span>&gt;</span>
<span>----&gt; </span><span>1</span> <span>factorial</span><span>(</span><span>5000</span><span>)</span>

<span>&lt;ipython-input-1-d6624133408f&gt;</span> in <span>factorial</span><span>(n)</span>
<span>      </span><span>6</span>         <span>return</span> <span>1</span>
<span>      </span><span>7</span>     <span>else</span><span>:</span> <span># Рекурсивний крок</span>
<span>----&gt; </span><span>8</span>         <span>return</span> <span>n</span> <span>*</span> <span>factorial</span><span>(</span><span>n</span> <span>-</span> <span>1</span><span>)</span> <span># Рекурсивний виклик</span>

<span>...</span> <span>last</span> <span>1</span> <span>frames</span> <span>repeated</span><span>,</span> <span>from</span> <span>the</span> <span>frame</span> <span>below</span> <span>...</span>

<span>&lt;ipython-input-1-d6624133408f&gt;</span> in <span>factorial</span><span>(n)</span>
<span>      </span><span>6</span>         <span>return</span> <span>1</span>
<span>      </span><span>7</span>     <span>else</span><span>:</span> <span># Рекурсивний крок</span>
<span>----&gt; </span><span>8</span>         <span>return</span> <span>n</span> <span>*</span> <span>factorial</span><span>(</span><span>n</span> <span>-</span> <span>1</span><span>)</span> <span># Рекурсивний виклик</span>

<span>RecursionError</span>: maximum recursion depth exceeded in comparison
</pre>



<p>Ми можемо керувати лімітом рекурсії за допомогою модуля <code><span>sys</span></code> у Python і встановити вищий ліміт. Запустіть наступний код, і ви не побачите помилки.</p>


<pre><span></span><span>import</span> <span>sys</span>
<span>sys</span><span>.</span><span>setrecursionlimit</span><span>(</span><span>10</span><span>**</span><span>5</span><span>)</span>

<span>factorial</span><span>(</span><span>5000</span><span>)</span>
</pre>
```
