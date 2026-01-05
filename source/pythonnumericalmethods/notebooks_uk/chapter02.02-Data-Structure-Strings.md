<h1>Структура даних - Рядки<a href="#data-structure-strings" title="Постійне посилання на цей заголовок"></a></h1>
<p>Ми говорили про різні типи даних, такі як int, float та boolean, усі вони пов'язані з одним значенням. Решта цього розділу познайомить вас з іншими типами даних, щоб ми могли зберігати кілька значень. Структури даних, пов'язані з цими новими типами, це Рядки, Списки, Кортежі, Множини та Словники. Ми почнемо з рядків.</p>
<p>Рядок — це послідовність символів, наприклад "Hello World", який ми бачили в розділі 1. Рядки оточені одинарними або подвійними лапками. Ми можемо використовувати функцію <em>print</em> для виведення рядків на екран.</p>
<p><strong>СПРОБУЙТЕ!</strong> Виведіть "I love Python!" на екран.</p>


<pre><span></span><span>print</span><span>(</span><span>"I love Python!"</span><span>)</span>
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Присвойте символ "S" змінній з іменем s. Присвойте рядок "Hello World" змінній w. Перевірте, що s та w мають тип рядка, використовуючи функцію <em>type</em>.</p>


<pre><span></span><span>s</span> <span>=</span> <span>"S"</span>
<span>w</span> <span>=</span> <span>"Hello World"</span>
</pre>





<pre><span></span><span>type</span><span>(</span><span>s</span><span>)</span>
</pre>



<pre><span></span>str
</pre>





<pre><span></span><span>type</span><span>(</span><span>w</span><span>)</span>
</pre>



<pre><span></span>str
</pre>



<p>Зауважте, що пробіл, " ", між "Hello" та "World" також є типом <em>str</em>. Будь-який символ може бути символом, навіть ті, що зарезервовані для операторів. Зауважте, що як <em>str</em>, вони не виконують ту саму функцію. Хоча вони виглядають однаково, Python інтерпретує їх абсолютно по-різному.</p>
<p><strong>СПРОБУЙТЕ!</strong> Створіть порожній рядок. Перевірте, що порожній рядок є <em>str</em>.</p>


<pre><span></span><span>s</span> <span>=</span> <span>" "</span>
<span>type</span><span>(</span><span>s</span><span>)</span>
</pre>



<pre><span></span>str
</pre>



<p>Рядок — це масив символів, тому він має довжину, щоб вказувати розмір рядка. Наприклад, ми можемо перевірити розмір рядка за допомогою вбудованої функції <em>len</em>.</p>


<pre><span></span><span>len</span><span>(</span><span>w</span><span>)</span>
</pre>



<pre><span></span>11
</pre>



<p>Рядки також мають індекси, щоб вказувати розташування кожного символу, завдяки чому ми можемо легко знайти певний символ. Індекс позиції починається з 0, як показано на наступному зображенні.</p>
<p><img alt="Індекс_рядка" src="../_images/02.02.01-hello_world_index.png"/></p>
<p>Ми можемо отримати доступ до будь-якого символу, використовуючи квадратні дужки та індекс позиції. Наприклад, якщо ми хочемо отримати символ ‘W`, то нам потрібно зробити:</p>


<pre><span></span><span>w</span><span>[</span><span>6</span><span>]</span>
</pre>



<pre><span></span>'W'
</pre>



<p>Ми також можемо вибрати послідовність за допомогою зрізів рядків. Наприклад, якщо ми хочемо отримати "World", ми можемо виконати наступну команду.</p>


<pre><span></span><span>w</span><span>[</span><span>6</span><span>:</span><span>11</span><span>]</span>
</pre>



<pre><span></span>'World'
</pre>



<p>[6:11] означає, що початкова позиція — це індекс 6, а кінцева позиція — індекс 10. Для діапазону зрізів рядків Python верхня межа є виключною, що означає, що [6:11] фактично зрізає символи з 6 -> 10. Синтаксис для зрізів у Python: [start:end:step], третій елемент — step — є необов'язковим.</p>
<p>Ви можете ігнорувати кінцеву позицію, якщо хочете зробити зріз до кінця рядка. Наприклад, наступна команда ідентична попередній:</p>


<pre><span></span><span>w</span><span>[</span><span>6</span><span>:]</span>
</pre>



<pre><span></span>'World'
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Отримайте слово "Hello" з рядка <em>w</em>.</p>


<pre><span></span><span>w</span><span>[:</span><span>5</span><span>]</span>
</pre>



<pre><span></span>'Hello'
</pre>



<p>Ви також можете використовувати від'ємний індекс при зрізанні рядків, що означає відлік з кінця рядка. Наприклад, -1 означає останній символ, -2 — передостанній і так далі.</p>
<p><strong>СПРОБУЙТЕ!</strong> Зробіть зріз "Wor" зі слова "World".</p>


<pre><span></span><span>w</span><span>[</span><span>6</span><span>:</span><span>-</span><span>2</span><span>]</span>
</pre>



<pre><span></span>'Wor'
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Отримайте кожен другий символ у змінній <em>w</em></p>


<pre><span></span><span>w</span><span>[::</span><span>2</span><span>]</span>
</pre>



<pre><span></span>'HloWrd'
</pre>



<p>Рядки не можуть використовуватися в математичних операціях.</p>
<p><strong>СПРОБУЙТЕ!</strong> Використайте ‘+` для додавання двох чисел. Перевірте, що "+" не поводиться як оператор додавання, <code><span>+</span></code>.</p>


<pre><span></span><span>1</span> <span>"+"</span> <span>2</span>
</pre>



<pre><span></span><span>  File</span><span> "&lt;ipython-input-13-46b54f731e00&gt;"</span><span>, line </span><span>1</span>
<span>    </span><span>1</span> <span>"+"</span> <span>2</span>
        <span>^</span>
<span>SyntaxError</span>: invalid syntax
</pre>



<p><strong>УВАГА!</strong> Числа також можуть бути виражені як <em>str</em>. Наприклад, <code><span>x</span> <span>=</span> <span>'123'</span></code> означає, що x — це рядок 123, а не число 123. Однак рядки представляють слова або текст, тому для них не повинно бути визначено додавання.</p>
<p><strong>ПОРАДА!</strong> Ви можете опинитися в ситуації, коли захочете використовувати апостроф як <em>str</em>. Це проблематично, оскільки апостроф використовується для позначення рядків. На щастя, апостроф можна використовувати в рядку наступним чином. Зворотний слеш (\) — це спосіб повідомити Python, що це частина рядка, а не позначення рядків. Символ зворотного слеша використовується для екранування символів, які інакше мають особливе значення, таких як новий рядок, сам зворотний слеш або символ лапок.</p>


<pre><span></span><span>'don</span><span>\'</span><span>t'</span>
</pre>



<pre><span></span>"don't"
</pre>



<p>Один рядок може бути об'єднаний з іншим рядком. Наприклад:</p>


<pre><span></span><span>str_a</span> <span>=</span> <span>"I love Python! "</span>
<span>str_b</span> <span>=</span> <span>"You too!"</span>

<span>print</span><span>(</span><span>str_a</span> <span>+</span> <span>str_b</span><span>)</span>
</pre>



<pre><span></span>I love Python! You too!
</pre>



<p>Ми також можемо перетворювати інші типи даних на рядки за допомогою вбудованої функції <em>str</em>. Це корисно, наприклад, якщо у нас є змінна x, яка зберігає 1 як ціле число, і ми хочемо вивести її безпосередньо з рядком, ми отримаємо помилку, що не можемо об'єднати рядок з цілим числом.</p>


<pre><span></span><span>x</span> <span>=</span> <span>1</span>
<span>print</span><span>(</span><span>"x = "</span> <span>+</span> <span>x</span><span>)</span>
</pre>



<pre><span></span><span>---------------------------------------------------------------------------</span>
<span>TypeError</span><span>                                 </span>Traceback (most recent call last)
<span>&lt;ipython-input-16-3e562ba0dd83&gt;</span> in <span>&lt;module&gt;</span><span>()</span>
<span>      </span><span>1</span> <span>x</span> <span>=</span> <span>1</span>
<span>----&gt; </span><span>2</span> <span>print</span><span>(</span><span>"x = "</span> <span>+</span> <span>x</span><span>)</span>

<span>TypeError</span>: can only concatenate str (not "int") to str
</pre>



<p>Правильний спосіб зробити це — спочатку перетворити ціле число на рядок, а потім вивести його.</p>
<p><strong>СПРОБУЙТЕ!</strong> Виведіть <em>x = 1</em> на екран.</p>


<pre><span></span><span>print</span><span>(</span><span>"x = "</span> <span>+</span> <span>str</span><span>(</span><span>x</span><span>))</span>
</pre>



<pre><span></span>x = 1
</pre>





<pre><span></span><span>type</span><span>(</span><span>str</span><span>(</span><span>x</span><span>))</span>
</pre>



<pre><span></span>str
</pre>



<p>У Python рядок є об'єктом, який має різні методи, що можуть бути використані для маніпулювання ним (ми поговоримо про об'єктно-орієнтоване програмування пізніше). Спосіб отримати доступ до різних методів — це використовувати шаблон "string.method_name".</p>
<p><strong>СПРОБУЙТЕ!</strong> Перетворіть змінну w на верхній регістр.</p>


<pre><span></span><span>w</span><span>.</span><span>upper</span><span>()</span>
</pre>



<pre><span></span>'HELLO WORLD'
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Підрахуйте кількість входжень літери "l" у w.</p>


<pre><span></span><span>w</span><span>.</span><span>count</span><span>(</span><span>"l"</span><span>)</span>
</pre>



<pre><span></span>3
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Замініть "World" у змінній w на "Berkeley".</p>


<pre><span></span><span>w</span><span>.</span><span>replace</span><span>(</span><span>"World"</span><span>,</span> <span>"Berkeley"</span><span>)</span>
</pre>



<pre><span></span>'Hello Berkeley'
</pre>



<p>Існують різні способи попереднього форматування рядка. Тут ми представимо два способи зробити це. Наприклад, якщо у нас є дві змінні <em>name</em> та <em>country</em>, і ми хочемо вивести їх у реченні, але не хочемо використовувати конкатенацію рядків, яку ми використовували раніше, оскільки це призведе до багатьох знаків ‘+` у рядку. Замість цього ми можемо зробити наступне:</p>


<pre><span></span><span>name</span> <span>=</span> <span>"UC Berkeley"</span>
<span>country</span> <span>=</span> <span>'USA'</span>

<span>print</span><span>(</span><span>"</span><span>%s</span><span> is a great school in </span><span>%s</span><span>!"</span><span>%</span><span>(</span><span>name</span><span>,</span> <span>country</span><span>))</span>
</pre>



<pre><span></span>UC Berkeley is a great school in USA!
</pre>



<p><strong>ЩО ВІДБУВАЄТЬСЯ?</strong> У попередньому прикладі %s у подвійних лапках повідомляє Python, що ми хочемо вставити деякі рядки в це місце (s у цьому випадку означає string — рядок). <em>%(name, country)</em> — це місце, куди ми хочемо вставити два рядки.</p>
<p><strong>НОВИНКА!</strong> Існує інший спосіб, представлений лише в Python 3.6 і вище, він називається f-рядок (f-String), що означає форматований рядок (formated-String). Ви можете легко форматувати рядок за допомогою наступного рядка:</p>


<pre><span></span><span>print</span><span>(</span><span>f</span><span>"</span><span>{</span><span>name</span><span>}</span><span> is a great school in </span><span>{</span><span>country</span><span>}</span><span>."</span><span>)</span>
</pre>



<pre><span></span>UC Berkeley is a great school in USA.
</pre>



<p>Ви навіть можете вивести числовий вираз без перетворення типу даних, як ми робили раніше.</p>
<p><strong>СПРОБУЙТЕ!</strong> Виведіть результат <em>3*4</em> безпосередньо за допомогою f-рядка.</p>


<pre><span></span><span>print</span><span>(</span><span>f</span><span>"</span><span>{</span><span>3</span><span>*</span><span>4</span><span>}</span><span>"</span><span>)</span>
</pre>



<pre><span></span>12
</pre>



<p>Гаразд, ми багато чого дізналися про структуру даних — рядок, це наша перша послідовна структура даних. Давайте дізнаємося більше зараз.</p>
