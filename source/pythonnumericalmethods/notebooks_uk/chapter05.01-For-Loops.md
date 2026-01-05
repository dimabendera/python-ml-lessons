<h1>Цикли For<a href="#for-loops" title="Постійне посилання на цей заголовок"></a></h1>
<p><strong>Цикл for</strong> — це набір інструкцій, який повторюється, або ітерується, для кожного значення в послідовності. Іноді цикли for називають <strong>визначеними циклами</strong>, оскільки вони мають попередньо визначені початок і кінець, обмежені послідовністю.</p>
<p>Загальний синтаксис блоку циклу for виглядає наступним чином.</p>
<p><strong>КОНСТРУКЦІЯ</strong>: Цикл For</p>
<pre><span></span><span>for</span> <span>змінна_циклу</span> <span>in</span> <span>послідовність</span><span>:</span>
    <span>блок_коду</span>
</pre>

<p>Цикл for присвоює <strong>змінній циклу</strong> перший елемент послідовності. Він виконує все, що знаходиться в блоці коду. Потім він присвоює змінній циклу наступний елемент послідовності і знову виконує блок коду. Це триває доти, доки в послідовності не залишиться елементів для присвоєння.</p>
<p><strong>СПРОБУЙТЕ!</strong> Яка сума всіх цілих чисел від 1 до 3?</p>


<pre><span></span><span>n</span> <span>=</span> <span>0</span>
<span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>1</span><span>,</span> <span>4</span><span>):</span>
    <span>n</span> <span>=</span> <span>n</span> <span>+</span> <span>i</span>
    
<span>print</span><span>(</span><span>n</span><span>)</span>
</pre>



<pre><span></span>6
</pre>



<p><strong>ЩО ВІДБУВАЄТЬСЯ?</strong></p>
<ol>
<li><p>Спочатку функція <em>range(1, 4)</em> генерує список чисел, що починається з 1 і закінчується 3. Перегляньте опис функції <em>range</em> та ознайомтеся з її використанням. У найпростішій формі це <em>range(start, stop, step)</em>, де <em>step</em> (крок) є необов'язковим і за замовчуванням дорівнює 1.</p></li>
<li><p>Змінній <em>n</em> присвоюється значення 0.</p></li>
<li><p>Змінній <em>i</em> присвоюється значення 1.</p></li>
<li><p>Змінній <em>n</em> присвоюється значення <em>n + i</em> (<span>\(0 + 1 = 1\)</span>).</p></li>
<li><p>Змінній <em>i</em> присвоюється значення 2.</p></li>
<li><p>Змінній <em>n</em> присвоюється значення <em>n + i</em> (<span>\(1 + 2 = 3\)</span>).</p></li>
<li><p>Змінній <em>i</em> присвоюється значення 3.</p></li>
<li><p>Змінній <em>n</em> присвоюється значення <em>n + i</em> (<span>\(3 + 3 = 6\)</span>).</p></li>
<li><p>Оскільки в списку більше немає значень для присвоєння, цикл for завершується зі значенням <em>n = 6</em>.</p></li>
</ol>
<p>Ми наведемо ще кілька прикладів, щоб дати вам уявлення про те, як працюють цикли for. Інші приклади послідовностей, які ми можемо ітерувати, включають елементи кортежу, символи в рядку та інші послідовні типи даних.</p>
<p><strong>ПРИКЛАД:</strong> Виведіть усі символи в рядку <code><span>"banana"</span></code>.</p>


<pre><span></span><span>for</span> <span>c</span> <span>in</span> <span>"banana"</span><span>:</span>
    <span>print</span><span>(</span><span>c</span><span>)</span>
</pre>



<pre><span></span>b
a
n
a
n
a
</pre>



<p>Як альтернативу, ви можете використовувати індекс для отримання кожного символу. Але це не так лаконічно, як у попередньому прикладі. Нагадаємо, що довжину рядка можна визначити за допомогою функції <em>len</em>. І ми можемо пропустити початкове значення, вказавши лише одне число як кінцеве.</p>


<pre><span></span><span>s</span> <span>=</span> <span>"banana"</span>
<span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>len</span><span>(</span><span>s</span><span>)):</span>
    <span>print</span><span>(</span><span>s</span><span>[</span><span>i</span><span>])</span>
</pre>



<pre><span></span>b
a
n
a
n
a
</pre>



<p><strong>ПРИКЛАД</strong>: Дано список цілих чисел <em>a</em>, додайте всі елементи <em>a</em>.</p>


<pre><span></span><span>s</span> <span>=</span> <span>0</span>
<span>a</span> <span>=</span> <span>[</span><span>2</span><span>,</span> <span>3</span><span>,</span> <span>1</span><span>,</span> <span>3</span><span>,</span> <span>3</span><span>]</span>
<span>for</span> <span>i</span> <span>in</span> <span>a</span><span>:</span>
    <span>s</span> <span>+=</span> <span>i</span> <span># зауважте, це еквівалентно s = s + i</span>
    
<span>print</span><span>(</span><span>s</span><span>)</span>
</pre>



<pre><span></span>12
</pre>



<p>Функція Python <em>sum</em> вже написана для обробки попереднього прикладу. Однак, припустимо, ви хочете додати лише парні числа. Що б ви змінили в попередньому блоці циклу for, щоб врахувати це обмеження?</p>


<pre><span></span><span>s</span> <span>=</span> <span>0</span>
<span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>0</span><span>,</span> <span>len</span><span>(</span><span>a</span><span>),</span> <span>2</span><span>):</span>
    <span>s</span> <span>+=</span> <span>a</span><span>[</span><span>i</span><span>]</span>
    
<span>print</span><span>(</span><span>s</span><span>)</span>
</pre>



<pre><span></span>6
</pre>



<p><strong>ПРИМІТКА!</strong> Ми використовуємо <em>step</em> (крок) зі значенням 2 у функції <em>range</em>, щоб отримати парні індекси для списку <em>a</em>. Також, у Python часто використовується скорочення — оператор <em>+=</em>. У Python та багатьох інших мовах програмування вираз на кшталт <em>i += 1</em> еквівалентний <em>i = i + 1</em>, і те ж саме стосується інших операторів, таких як <em>-=</em>, <em>*=</em>, <em>/=</em>.</p>
<p><strong>Приклад</strong>: Визначте словник і пройдіться циклом по всіх його ключах та значеннях.</p>


<pre><span></span><span>dict_a</span> <span>=</span> <span>{</span><span>"One"</span><span>:</span><span>1</span><span>,</span> <span>"Two"</span><span>:</span><span>2</span><span>,</span> <span>"Three"</span><span>:</span><span>3</span><span>}</span>

<span>for</span> <span>key</span> <span>in</span> <span>dict_a</span><span>.</span><span>keys</span><span>():</span>
    <span>print</span><span>(</span><span>key</span><span>,</span> <span>dict_a</span><span>[</span><span>key</span><span>])</span>
</pre>



<pre><span></span>One 1
Two 2
Three 3
</pre>



<p>У наведеному вище прикладі ми спочатку отримуємо всі ключі за допомогою методу <em>keys</em>, а потім використовуємо ключ для доступу до значення. Як альтернативу, ми можемо використати метод <em>items</em> у словнику і отримати ключ та значення одночасно, як показано в наступному прикладі.</p>


<pre><span></span><span>for</span> <span>key</span><span>,</span> <span>value</span> <span>in</span> <span>dict_a</span><span>.</span><span>items</span><span>():</span>
    <span>print</span><span>(</span><span>key</span><span>,</span> <span>value</span><span>)</span>
</pre>



<pre><span></span>One 1
Two 2
Three 3
</pre>



<p>Зауважте, що ми можемо присвоювати значення двом різним змінним циклу одночасно. Існують й інші випадки, коли ми можемо робити щось подібне. Наприклад, якщо у нас є два списки однакової довжини, і ми хочемо пройтися по них циклом, ми можемо зробити це, як у наступному прикладі, використовуючи функцію <em>zip</em>:</p>


<pre><span></span><span>a</span> <span>=</span> <span>[</span><span>"One"</span><span>,</span> <span>"Two"</span><span>,</span> <span>"Three"</span><span>]</span>
<span>b</span> <span>=</span> <span>[</span><span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>]</span>

<span>for</span> <span>i</span><span>,</span> <span>j</span> <span>in</span> <span>zip</span><span>(</span><span>a</span><span>,</span> <span>b</span><span>):</span>
    <span>print</span><span>(</span><span>i</span><span>,</span> <span>j</span><span>)</span>
</pre>



<pre><span></span>One 1
Two 2
Three 3
</pre>



<p><strong>ПРИКЛАД:</strong> Нехай функція <em>have_digits</em> приймає на вхід рядок. Вихідне значення <em>out</em> повинно дорівнювати 1, якщо рядок містить цифри, і 0 в іншому випадку. Ви можете використовувати метод рядка <em>isdigit</em>, щоб перевірити, чи є символ цифрою.</p>


<pre><span></span><span>def</span> <span>have_digits</span><span>(</span><span>s</span><span>):</span>
    
    <span>out</span> <span>=</span> <span>0</span>
    
    <span># проходимо циклом по рядку</span>
    <span>for</span> <span>c</span> <span>in</span> <span>s</span><span>:</span>
        <span># перевіряємо, чи є символ цифрою</span>
        <span>if</span> <span>c</span><span>.</span><span>isdigit</span><span>():</span>
            <span>out</span> <span>=</span> <span>1</span>
            <span>break</span>
            
    <span>return</span> <span>out</span>
</pre>





<pre><span></span><span>out</span> <span>=</span> <span>have_digits</span><span>(</span><span>'only4you'</span><span>)</span>
<span>print</span><span>(</span><span>out</span><span>)</span>
</pre>



<pre><span></span>1
</pre>





<pre><span></span><span>out</span> <span>=</span> <span>have_digits</span><span>(</span><span>'only for you'</span><span>)</span>
<span>print</span><span>(</span><span>out</span><span>)</span>
</pre>



<pre><span></span>0
</pre>



<p>Перший крок у функції <em>have_digits</em> припускає, що в рядку <em>s</em> немає цифр (тобто вихідне значення дорівнює 0 або False).</p>
<p>Зверніть увагу на нове ключове слово <em>break</em>. При виконанні ключове слово <em>break</em> негайно зупиняє найближчий цикл for, в якому воно міститься; тобто, якщо воно знаходиться у вкладеному циклі for, то воно зупинить лише найвнутрішніший цикл. У цьому конкретному випадку команда break виконується, якщо ми знаходимо цифру в рядку. Код буде працювати правильно і без цього оператора, але оскільки завдання полягає в тому, щоб з'ясувати, чи є в <em>s</em> хоча б одна цифра, нам не потрібно продовжувати пошук, якщо ми її вже знайшли. Аналогічно, якби людина отримала таке ж завдання для довгого рядка символів, вона б не продовжувала шукати цифри, якби вже знайшла одну. Оператори break використовуються, коли в циклі for відбувається щось, що змушує вас зупинити його достроково. Менш нав'язливою командою є ключове слово <em>continue</em>, яке пропускає решту коду в поточній ітерації циклу for і переходить до наступного елемента ітерованої послідовності. Розгляньте наступний приклад, де ми використовуємо ключове слово <em>continue</em>, щоб пропустити виконання функції <em>print</em> для виведення числа 2:</p>


<pre><span></span><span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>5</span><span>):</span>
    
    <span>if</span> <span>i</span> <span>==</span> <span>2</span><span>:</span>
        <span>continue</span>
        
    <span>print</span><span>(</span><span>i</span><span>)</span>
</pre>



<pre><span></span>0
1
3
4
</pre>



<p><strong>ПРИКЛАД:</strong> Нехай функція <em>my_dist_2_points(xy_points, xy)</em>, де вхідний аргумент <em>xy_points</em> — це список x-y координат точок в евклідовому просторі, <em>xy</em> — це список, що містить x-y координати однієї точки, а вихідне значення <em>d</em> — це список, що містить відстані від <em>xy</em> до точок, що містяться в кожному рядку <em>xy_points</em>.</p>


<pre><span></span><span>import</span> <span>math</span>

<span>def</span> <span>my_dist_2_points</span><span>(</span><span>xy_points</span><span>,</span> <span>xy</span><span>):</span>
    <span>"""</span>
<span>    Повертає масив відстаней між xy та точками,</span>
<span>    що містяться в рядках xy_points</span>
<span>    </span>
<span>    автор</span>
<span>    дата</span>
<span>    """</span>
    <span>d</span> <span>=</span> <span>[]</span>
    <span>for</span> <span>xy_point</span> <span>in</span> <span>xy_points</span><span>:</span>
        <span>dist</span> <span>=</span> <span>math</span><span>.</span><span>sqrt</span><span>(</span>\
            <span>(</span><span>xy_point</span><span>[</span><span>0</span><span>]</span> <span>-</span> <span>xy</span><span>[</span><span>0</span><span>])</span><span>**</span><span>2</span> <span>+</span> <span>(</span><span>xy_point</span><span>[</span><span>1</span><span>]</span> <span>-</span> <span>xy</span><span>[</span><span>1</span><span>])</span><span>**</span><span>2</span><span>)</span>
        
        <span>d</span><span>.</span><span>append</span><span>(</span><span>dist</span><span>)</span>
        
    <span>return</span> <span>d</span>
</pre>





<pre><span></span><span>xy_points</span> <span>=</span> <span>[[</span><span>3</span><span>,</span><span>2</span><span>],</span> <span>[</span><span>2</span><span>,</span> <span>3</span><span>],</span> <span>[</span><span>2</span><span>,</span> <span>2</span><span>]]</span>
<span>xy</span> <span>=</span> <span>[</span><span>1</span><span>,</span> <span>2</span><span>]</span>
<span>my_dist_2_points</span><span>(</span><span>xy_points</span><span>,</span> <span>xy</span><span>)</span>
</pre>



<pre><span></span>[2.0, 1.4142135623730951, 1.0]
</pre>



<p>Так само, як і оператори if, цикли for можуть бути вкладеними.</p>
<p><strong>ПРИКЛАД:</strong> Нехай <em>x</em> — це двовимірний масив, [5 6; 7 8]. Використайте вкладений цикл for, щоб підсумувати всі елементи в <em>x</em>.</p>


<pre><span></span><span>x</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>5</span><span>,</span> <span>6</span><span>],</span> <span>[</span><span>7</span><span>,</span> <span>8</span><span>]])</span>
<span>n</span><span>,</span> <span>m</span> <span>=</span> <span>x</span><span>.</span><span>shape</span>
<span>s</span> <span>=</span> <span>0</span>
<span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>n</span><span>):</span>
    <span>for</span> <span>j</span> <span>in</span> <span>range</span><span>(</span><span>m</span><span>):</span>
        <span>s</span> <span>+=</span> <span>x</span><span>[</span><span>i</span><span>,</span> <span>j</span><span>]</span>
        
<span>print</span><span>(</span><span>s</span><span>)</span>
</pre>



<pre><span></span>26
</pre>



<p><strong>ЩО ВІДБУВАЄТЬСЯ?</strong></p>
<ol>
<li><p><em>s</em>, що представляє поточну суму, встановлюється в 0.</p></li>
<li><p>Зовнішній цикл for починається зі змінною циклу i, встановленою в 0.</p></li>
<li><p>Внутрішній цикл for починається зі змінною циклу j, встановленою в 0.</p></li>
<li><p><em>s</em> збільшується на x[i,j] = x[0,0] = 5. Отже, s = 5.</p></li>
<li><p>Внутрішній цикл встановлює j = 1.</p></li>
<li><p><em>s</em> збільшується на x[i,j] = x[0,1] = 6. Отже, s = 11.</p></li>
<li><p>Внутрішній цикл завершується.</p></li>
<li><p>Зовнішній цикл встановлює i = 1.</p></li>
<li><p>Внутрішній цикл for починається зі змінною циклу j, встановленою в 0.</p></li>
<li><p><em>s</em> збільшується на x[i,j] = x[1,0] = 7. Отже, s = 18.</p></li>
<li><p>Внутрішній цикл встановлює j = 1.</p></li>
<li><p><em>s</em> збільшується на x[i,j] = x[1,1] = 8. Отже, s = 26.</p></li>
<li><p>Внутрішній цикл завершується.</p></li>
<li><p>Зовнішній цикл завершується зі значенням s = 26.</p></li>
</ol>
<p><strong>ПОПЕРЕДЖЕННЯ!</strong> Хоча це можливо, не намагайтеся змінювати змінну циклу всередині циклу for. Це зробить ваш код дуже складним і, ймовірно, призведе до помилок.</p>
