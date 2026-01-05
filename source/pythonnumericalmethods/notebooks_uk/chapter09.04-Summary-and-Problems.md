<h1>Підсумок<a href="#summary" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Числа мають багато представлень, і кожне представлення має свої переваги та недоліки.</p></li>
<li><p>Комп'ютери повинні представляти числа, використовуючи скінченну кількість цифр (бітів).</p></li>
<li><p>Двійкове представлення та IEEE754 є скінченними представленнями чисел, що використовуються комп'ютерами.</p></li>
<li><p>Помилка округлення є важливою помилкою, пов'язаною з чисельними методами.</p></li>
</ol>


<h1>Задачі<a href="#problems" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Напишіть функцію <em>my_bin_2_dec(b)</em>, де <em>b</em> є двійковим числом, представленим списком одиниць та нулів. Останній елемент <em>b</em> представляє коефіцієнт <span>\(2^0\)</span>, передостанній елемент b представляє коефіцієнт <span>\(2^1\)</span>, і так далі. Вихідна змінна, <em>d</em>, має бути десятковим представленням b. Тестові випадки наведені нижче.</p></li>
</ol>


<pre><span></span><span>def</span> <span>my_bin_2_dec</span><span>(</span><span>b</span><span>):</span>
    <span># напишіть тут код вашої функції</span>
    <span>return</span> <span>d</span>
</pre>





<pre><span></span><span># Вивід: 7</span>
<span>my_bin_2_dec</span><span>([</span><span>1</span><span>,</span> <span>1</span><span>,</span> <span>1</span><span>])</span>
</pre>





<pre><span></span><span># Вивід: 85</span>
<span>my_bin_2_dec</span><span>([</span><span>1</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>])</span>
</pre>





<pre><span></span><span># Вивід: 33554431</span>
<span>my_bin_2_dec</span><span>([</span><span>1</span><span>]</span><span>*</span><span>25</span><span>)</span>
</pre>



<ol>
<li><p>Напишіть функцію <em>my_dec_2_bin(d)</em>, де <em>d</em> є додатним цілим числом у десятковій системі, а <em>b</em> є двійковим представленням <em>d</em>. Вивід <em>b</em> має бути списком одиниць та нулів, а провідний член має бути 1, якщо тільки десяткове вхідне значення не дорівнює 0. Тестові випадки наведені нижче.</p></li>
</ol>


<pre><span></span><span>def</span> <span>my_dec_2_bin</span><span>(</span><span>d</span><span>):</span>
    <span># напишіть тут код вашої функції</span>
    <span>return</span> <span>b</span>
</pre>





<pre><span></span><span># Вивід: [0]</span>
<span>my_dec_2_bin</span><span>(</span><span>0</span><span>)</span>
</pre>





<pre><span></span><span># Вивід: [1, 0, 1, 1, 1]</span>
<span>my_dec_2_bin</span><span>(</span><span>23</span><span>)</span>
</pre>





<pre><span></span><span># Вивід: [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1]</span>
<span>my_dec_2_bin</span><span>(</span><span>2097</span><span>)</span>
</pre>



<ol>
<li><p>Використайте дві функції, які ви написали в задачах 1 і 2, щоб обчислити <em>d = my_bin_2_dec(my_dec_2_bin(12654))</em>. Чи отримуєте ви те саме число?</p></li>
</ol>
<ol>
<li><p>Напишіть функцію <em>my_bin_adder(b1,b2)</em>, де <em>b1</em>, <em>b2</em> та вихідна змінна <em>b</em> є двійковими числами, представленими як у задачі 1. Вихідна змінна має бути обчислена як <em>b = b1 + b2</em>. Не використовуйте ваші функції з задач 1 і 2 для написання цієї функції (тобто, не перетворюйте <em>b1</em> та <em>b2</em> у десяткову систему; додайте їх, а потім перетворіть результат назад у двійкову). Ця функція повинна приймати вхідні дані <em>b1</em> та <em>b2</em> будь-якої довжини (тобто, дуже довгі двійкові числа), і <em>b1</em> та <em>b2</em> не обов'язково можуть бути однакової довжини.</p></li>
</ol>


<pre><span></span><span>def</span> <span>my_bin_adder</span><span>(</span><span>b1</span><span>,</span> <span>b2</span><span>):</span>
    <span># напишіть тут код вашої функції</span>
    <span>return</span> <span>b</span>
</pre>





<pre><span></span><span># Вивід: [1, 0, 0, 0, 0, 0]</span>
<span>my_bin_adder</span><span>([</span><span>1</span><span>,</span> <span>1</span><span>,</span> <span>1</span><span>,</span> <span>1</span><span>,</span> <span>1</span><span>],</span> <span>[</span><span>1</span><span>])</span>
</pre>





<pre><span></span><span># Вивід: [1, 1, 1, 0, 0, 1, 1]</span>
<span>my_bin_adder</span><span>([</span><span>1</span><span>,</span> <span>1</span><span>,</span> <span>1</span><span>,</span> <span>1</span><span>,</span> <span>1</span><span>],</span> <span>[</span><span>1</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>])</span>
</pre>





<pre><span></span><span># Вивід: [1, 0, 1, 1]</span>
<span>my_bin_adder</span><span>([</span><span>1</span><span>,</span> <span>1</span><span>,</span> <span>0</span><span>],</span> <span>[</span><span>1</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>])</span>
</pre>



<ol>
<li><p>Який ефект має виділення більшої кількості бітів для дробової частини порівняно з характеристикою і навпаки? Який ефект має виділення більшої кількості бітів для знака?</p></li>
</ol>
<ol>
<li><p>Напишіть функцію <em>my_ieee_2_dec(ieee)</em>, де <em>ieee</em> є рядком, що містить 64 символи одиниць та нулів, які представляють 64-бітне число IEEE754. Вивід має бути <em>d</em>, еквівалентним десятковим представленням <em>ieee</em>. Вхідна змінна <em>ieee</em> завжди буде 64-елементним рядком одиниць та нулів, що визначає 64-бітне число з плаваючою комою.</p></li>
</ol>


<pre><span></span><span>def</span> <span>my_ieee_2_dec</span><span>(</span><span>ieee</span><span>):</span>
    <span># Напишіть вашу функцію тут</span>
    <span>return</span> <span>d</span>
</pre>





<pre><span></span><span># Вивід: -48</span>
<span>ieee</span> <span>=</span> <span>'1100000001001000000000000000000000000000000000000000000000000000'</span>
<span>my_ieee_2_dec</span><span>(</span><span>ieee</span><span>)</span>
</pre>





<pre><span></span><span># Вивід: 3.39999999999999991118215802999</span>
<span>ieee</span> <span>=</span> <span>'0100000000001011001100110011001100110011001100110011001100110011'</span>
<span>my_ieee_2_dec</span><span>(</span><span>ieee</span><span>)</span>
</pre>



<ol>
<li><p>Напишіть функцію <em>my_dec_2_ieee(d)</em>, де <em>d</em> є числом у десятковій системі, а вихідна змінна <em>ieee</em> є рядком з 64 символів одиниць та нулів, що представляє 64-бітне число IEEE754, найближче до <em>d</em>. Ви можете припустити, що <em>d</em> не спричинить переповнення для 64-бітних <em>ieee</em> чисел.</p></li>
</ol>


<pre><span></span><span>def</span> <span>my_dec_2_ieee</span><span>(</span><span>d</span><span>):</span>
    <span># напишіть тут код вашої функції</span>
    <span>return</span> <span>ieee</span>
</pre>





<pre><span></span><span># Вивід: '0100000000101110010111101010001110011100001100011010010001101000'</span>

<span>d</span> <span>=</span> <span>1.518484199625</span>
<span>my_dec_2_ieee</span><span>(</span><span>d</span><span>)</span>
</pre>





<pre><span></span><span># Вивід: '1100000001110011010100100100010010010001001010011000100010010000'</span>

<span>d</span> <span>=</span> <span>-</span><span>309.141740</span>
<span>my_dec_2_ieee</span><span>(</span><span>d</span><span>)</span>
</pre>





<pre><span></span><span># Вивід: '1100000011011000101010010000000000000000000000000000000000000000'</span>

<span>d</span> <span>=</span> <span>-</span><span>25252</span>
<span>my_dec_2_ieee</span><span>(</span><span>d</span><span>)</span>
</pre>



<ol>
<li><p>Визначте <em>ieee_baby</em> як представлення чисел за допомогою 6 бітів, де перший біт є бітом знака, другий і третій біти виділені для характеристики, а четвертий, п'ятий і шостий біти виділені для дробової частини. Нормалізація для характеристики дорівнює 1.</p></li>
</ol>
<p>Запишіть усі десяткові числа, які можуть бути представлені за допомогою <em>ieee_baby</em>.
Який найбільший/найменший проміжок у <em>ieee_baby</em>?</p>
<ol>
<li><p>Використайте функцію <em>np.spacing</em>, щоб визначити найменше число, для якого проміжок дорівнює 1.</p></li>
</ol>
<ol>
<li><p>Які переваги та недоліки використання двійкової системи порівняно з десятковою?</p></li>
</ol>
<ol>
<li><p>Запишіть число 13 (основа 10) в основі 1. Як би ви виконували додавання та множення в основі 1?</p></li>
</ol>
<ol>
<li><p>Як високо ви можете рахувати на пальцях, якщо рахуєте в двійковій системі?</p></li>
</ol>
<ol>
<li><p>Нехай <em>b</em> буде двійковим числом, що має <em>n</em> цифр. Чи можете ви придумати способи множення та ділення <em>b</em> на 2, які не передбачають жодних арифметичних операцій? Підказка: Подумайте, як ви множите та ділите десяткове число на 10.</p></li>
</ol>
