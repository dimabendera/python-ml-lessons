<h1>Локальні та глобальні змінні<a href="#local-variables-and-global-variables" title="Постійне посилання на цей заголовок"></a></h1>
<p>У розділі 2 було представлено ідею пам'яті, пов'язаної з ноутбуком, де зберігаються змінні, створені в ньому. Функція також має власний блок пам'яті, зарезервований для змінних, створених у цій функції. Цей блок пам'яті не є спільним з усім блоком пам'яті ноутбука. Тому змінній з певним ім'ям можна присвоїти значення всередині функції, не змінюючи змінну з таким самим ім'ям поза функцією. Блок пам'яті, пов'язаний з функцією, відкривається щоразу, коли функція використовується.</p>
<p><strong>СПРОБУЙТЕ!</strong> Яким буде значення <em>out</em> після виконання наступних рядків коду? Зауважте, що це не 6, яке є значенням, присвоєним <em>out</em> всередині <em>my_adder</em>.</p>


<pre><span></span><span>def</span> <span>my_adder</span><span>(</span><span>a</span><span>,</span> <span>b</span><span>,</span> <span>c</span><span>):</span>
    <span>out</span> <span>=</span> <span>a</span> <span>+</span> <span>b</span> <span>+</span> <span>c</span>
    <span>print</span><span>(</span><span>f</span><span>'Значення out всередині функції: </span><span>{</span><span>out</span><span>}</span><span>'</span><span>)</span>
    <span>return</span> <span>out</span>

<span>out</span> <span>=</span> <span>1</span>
<span>d</span> <span>=</span> <span>my_adder</span><span>(</span><span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>)</span>
<span>print</span><span>(</span><span>f</span><span>'Значення out поза функцією: </span><span>{</span><span>out</span><span>}</span><span>'</span><span>)</span>
</pre>



<pre><span></span>Значення out всередині функції: 6
Значення out поза функцією: 1
</pre>



<p>У <em>my_adder</em> змінна <em>out</em> є <strong>локальною змінною</strong>. Тобто, вона визначена лише у функції <em>my_adder</em>. Тому вона не може впливати на змінні поза функцією, і дії, виконані в ноутбуці поза функцією, не можуть вплинути на неї, навіть якщо вони мають однакові імена. Отже, у попередньому прикладі є змінна <em>out</em>, визначена в комірці ноутбука. Коли <em>my_adder</em> викликається в наступному рядку, Python відкриває новий блок пам'яті для змінних цієї функції. Однією зі змінних, створених усередині функції, є інша змінна, <em>out</em>. Однак, оскільки вони знаходяться в різних блоках пам'яті, присвоєння значення <em>out</em> всередині <em>my_adder</em> не змінює значення, присвоєного <em>out</em> поза функцією.</p>
<p>Навіщо мати окремі блоки пам'яті для функцій, а не один спільний блок? Хоча може здатися, що розділення блоків пам'яті створює для Python багато клопоту, це дуже ефективно для великих проєктів, що складаються з багатьох функцій, які працюють разом. Якщо один програміст відповідає за створення однієї функції, а інший — за створення іншої, ми б не хотіли, щоб кожен програміст турбувався про те, які імена змінних використовує інший. Ми хочемо, щоб вони могли працювати незалежно і були впевнені, що їхня власна робота не заважає роботі іншого, і навпаки. Тому окремі блоки пам'яті захищають функцію від зовнішнього впливу. Єдине, що ззовні блоку пам'яті функції може вплинути на те, що відбувається всередині, — це вхідні аргументи, а єдине, що може вийти у зовнішній світ з блоку пам'яті функції після її завершення, — це вихідні аргументи.</p>
<p>Наступні приклади розроблені як вправи на концепцію локальних змінних. Вони навмисно дуже заплутані, але якщо ви зможете їх розплутати, то, ймовірно, ви розумієте концепцію локальної змінної всередині функції. Зосередьтеся на тому, що саме робить Python, і в якому порядку.</p>
<p><strong>ПРИКЛАД:</strong> Розглянемо наступну функцію:</p>


<pre><span></span><span>def</span> <span>my_test</span><span>(</span><span>a</span><span>,</span> <span>b</span><span>):</span>
    <span>x</span> <span>=</span> <span>a</span> <span>+</span> <span>b</span>
    <span>y</span> <span>=</span> <span>x</span> <span>*</span> <span>b</span>
    <span>z</span> <span>=</span> <span>a</span> <span>+</span> <span>b</span>
    
    <span>m</span> <span>=</span> <span>2</span>
    
    <span>print</span><span>(</span><span>f</span><span>'Всередині функції: x=</span><span>{</span><span>x</span><span>}</span><span>, y=</span><span>{</span><span>y</span><span>}</span><span>, z=</span><span>{</span><span>z</span><span>}</span><span>'</span><span>)</span>
    <span>return</span> <span>x</span><span>,</span> <span>y</span>
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Якими будуть значення a, b, x, y, та z після виконання наступного коду?</p>


<pre><span></span><span>a</span> <span>=</span> <span>2</span>
<span>b</span> <span>=</span> <span>3</span>
<span>z</span> <span>=</span> <span>1</span>
<span>y</span><span>,</span> <span>x</span> <span>=</span> <span>my_test</span><span>(</span><span>b</span><span>,</span> <span>a</span><span>)</span>

<span>print</span><span>(</span><span>f</span><span>'Поза функцією: x=</span><span>{</span><span>x</span><span>}</span><span>, y=</span><span>{</span><span>y</span><span>}</span><span>, z=</span><span>{</span><span>z</span><span>}</span><span>'</span><span>)</span>
</pre>



<pre><span></span>Всередині функції: x=5, y=10, z=5
Поза функцією: x=10, y=5, z=1
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Якими будуть значення a, b, x, y, та z після виконання наступного коду?</p>


<pre><span></span><span>x</span> <span>=</span> <span>5</span>
<span>y</span> <span>=</span> <span>3</span>
<span>b</span><span>,</span> <span>a</span> <span>=</span> <span>my_test</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>)</span>

<span>print</span><span>(</span><span>f</span><span>'Поза функцією: x=</span><span>{</span><span>x</span><span>}</span><span>, y=</span><span>{</span><span>y</span><span>}</span><span>, z=</span><span>{</span><span>z</span><span>}</span><span>'</span><span>)</span>
</pre>



<pre><span></span>Всередині функції: x=8, y=24, z=8
Поза функцією: x=5, y=3, z=1
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Яким буде значення m, якщо ви виведете <em>m</em> поза функцією?</p>


<pre><span></span><span>m</span>
</pre>



<pre><span></span><span>---------------------------------------------------------------------------</span>
<span>NameError</span><span>                                 </span>Traceback (most recent call last)
<span>&lt;</span><span>ipython</span><span>-</span><span>input</span><span>-</span><span>5</span><span>-</span><span>9</span><span>a40b379906c</span><span>&gt;</span> <span>in</span> <span>&lt;</span><span>module</span><span>&gt;</span>
<span>----&gt; </span><span>1</span> <span>m</span>

<span>NameError</span>: ім'я 'm' не визначено
</pre>



<p>Ми бачимо, що значення <em>m</em> не визначено поза функцією, оскільки воно визначено всередині неї. Зворотна ситуація схожа: наприклад, якщо ви визначите змінну поза функцією, але захочете використати її всередині функції та змінити її значення, ви отримаєте таку ж помилку.</p>
<p><strong>ПРИКЛАД:</strong> Спробуйте використати та змінити значення <em>n</em> всередині функції.</p>


<pre><span></span><span>n</span> <span>=</span> <span>42</span>

<span>def</span> <span>func</span><span>():</span>
    <span>print</span><span>(</span><span>f</span><span>'Всередині функції: n дорівнює </span><span>{</span><span>n</span><span>}</span><span>'</span><span>)</span>
    <span>n</span> <span>=</span> <span>3</span>
    <span>print</span><span>(</span><span>f</span><span>'Всередині функції: змінюємо n на </span><span>{</span><span>n</span><span>}</span><span>'</span><span>)</span>

<span>func</span><span>()</span>
<span>print</span><span>(</span><span>f</span><span>'Поза функцією: значення n дорівнює </span><span>{</span><span>n</span><span>}</span><span>'</span><span>)</span>
</pre>



<pre><span></span><span>---------------------------------------------------------------------------</span>
<span>UnboundLocalError</span><span>                         </span>Traceback (most recent call last)
<span>&lt;</span><span>ipython</span><span>-</span><span>input</span><span>-</span><span>6</span><span>-</span><span>85</span><span>f3215553ae</span><span>&gt;</span> <span>in</span> <span>&lt;</span><span>module</span><span>&gt;</span>
<span>      </span><span>6</span>     <span>print</span><span>(</span><span>f</span><span>'Всередині функції: змінюємо n на </span><span>{</span><span>n</span><span>}</span><span>'</span><span>)</span>
<span>      </span><span>7</span> 
<span>----&gt; </span><span>8</span> <span>func</span><span>()</span>
<span>      </span><span>9</span> <span>print</span><span>(</span><span>f</span><span>'Поза функцією: значення n дорівнює </span><span>{</span><span>n</span><span>}</span><span>'</span><span>)</span>

<span>&lt;ipython-input-6-85f3215553ae&gt;</span> in <span>func</span><span>()</span>
<span>      </span><span>2</span> 
<span>      </span><span>3</span> <span>def</span> <span>func</span><span>():</span>
<span>----&gt; </span><span>4</span>     <span>print</span><span>(</span><span>f</span><span>'Всередині функції: n дорівнює </span><span>{</span><span>n</span><span>}</span><span>'</span><span>)</span>
<span>      </span><span>5</span>     <span>n</span> <span>=</span> <span>3</span>
<span>      </span><span>6</span>     <span>print</span><span>(</span><span>f</span><span>'Всередині функції: змінюємо n на </span><span>{</span><span>n</span><span>}</span><span>'</span><span>)</span>

<span>UnboundLocalError</span>: локальна змінна 'n' згадується перед присвоєнням
</pre>



<p>Рішення полягає у використанні ключового слова <strong>global</strong>, щоб повідомити Python, що ця змінна є глобальною і її можна використовувати як поза функцією, так і всередині неї.</p>
<p><strong>ПРИКЛАД:</strong> Визначте n як глобальну змінну, а потім використайте та змініть її значення всередині функції.</p>


<pre><span></span><span>n</span> <span>=</span> <span>42</span>

<span>def</span> <span>func</span><span>():</span>
    <span>global</span> <span>n</span>
    <span>print</span><span>(</span><span>f</span><span>'Всередині функції: n дорівнює </span><span>{</span><span>n</span><span>}</span><span>'</span><span>)</span>
    <span>n</span> <span>=</span> <span>3</span>
    <span>print</span><span>(</span><span>f</span><span>'Всередині функції: змінюємо n на </span><span>{</span><span>n</span><span>}</span><span>'</span><span>)</span>

<span>func</span><span>()</span>
<span>print</span><span>(</span><span>f</span><span>'Поза функцією: значення n дорівнює </span><span>{</span><span>n</span><span>}</span><span>'</span><span>)</span>
</pre>



<pre><span></span>Всередині функції: n дорівнює 42
Всередині функції: змінюємо n на 3
Поза функцією: значення n дорівнює 3
</pre>
