<h1>Основи функцій<a href="#function-basics" title="Permalink to this headline"></a></h1>
<p>У програмуванні <strong>функція</strong> — це послідовність інструкцій, яка виконує певне завдання. Функція — це блок коду, який може виконуватися, коли його викликають. Функція може мати <strong>вхідні аргументи</strong>, які надаються їй користувачем або сутністю, що викликає функцію. Функції також мають <strong>вихідні параметри</strong>, які є результатами роботи функції, що користувач очікує отримати після завершення її завдання. Наприклад, функція <em>math.sin</em> має один вхідний аргумент, кут у радіанах, і один вихідний параметр, наближене значення функції синуса, обчислене для вхідного кута (округлене до 16 знаків). Послідовність інструкцій для обчислення цього наближення становить <strong>тіло функції</strong>, яке до цього моменту не було показано.</p>
<p>Ми вже бачили багато вбудованих функцій Python, таких як <em>type</em>, <em>len</em> тощо. Також ми бачили функції з деяких пакетів, наприклад, <em>math.sin</em>, <em>np.array</em> тощо. Чи ви ще пам'ятаєте, як ми могли викликати та використовувати ці функції?</p>
<p><strong>СПРОБУЙТЕ!</strong> Перевірте, що <em>len</em> є вбудованою функцією, використовуючи функцію <em>type</em>.</p>


<pre><span></span><span>type</span><span>(</span><span>len</span><span>)</span>
</pre>



<pre><span></span>builtin_function_or_method
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Перевірте, що <em>np.linspace</em> є функцією, використовуючи функцію <em>type</em>. І дізнайтеся, як використовувати цю функцію за допомогою знака питання.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>

<span>type</span><span>(</span><span>np</span><span>.</span><span>linspace</span><span>)</span>
</pre>



<pre><span></span>function
</pre>





<pre><span></span>np.linspace<span>?</span>
</pre>




<h2>Визначення власної функції<a href="#define-your-own-function" title="Permalink to this headline"></a></h2>
<p>Ми можемо визначати власні функції. Функцію можна визначити кількома способами. Тут ми представимо найпоширеніший спосіб визначення функції, який використовує ключове слово <em>def</em>, як показано нижче:</p>
<pre><span></span><span>def</span> <span>function_name</span><span>(</span><span>argument_1</span><span>,</span> <span>argument_2</span><span>,</span> <span>...</span><span>):</span>
    <span>'''</span>
<span>    Описовий рядок</span>
<span>    '''</span>
    <span># коментарі до інструкцій</span>
    <span>function_statements</span> 
    
    <span>return</span> <span>output_parameters</span> <span>(</span><span>необов'язково</span><span>)</span>

</pre>

<p>Ми бачимо, що для визначення функції в Python потрібні наступні два компоненти:</p>
<ol>
<li><p><strong>Заголовок функції:</strong> Заголовок функції починається з ключового слова <em>def</em>, за яким іде пара дужок із вхідними аргументами всередині, і закінчується двокрапкою (:)</p></li>
<li><p><strong>Тіло функції:</strong> Блок з відступом (зазвичай чотири пробіли), що позначає основне тіло функції. Він складається з 3 частин:</p>
<ul>
<li><p><em>Описовий рядок:</em> Рядок, що описує функцію, до якого можна отримати доступ за допомогою функції <em>help()</em> або знака питання. Ви можете писати будь-які рядки всередині, вони можуть бути багаторядковими.</p></li>
<li><p><em>Інструкції функції:</em> Це покрокові інструкції, які функція виконуватиме, коли ми її викликаємо. Ви також можете помітити, що є рядок, який починається з '#', це рядок коментаря, що означає, що функція його не виконуватиме.</p></li>
<li><p><em>Інструкції повернення:</em> Функція може повертати деякі параметри після її виклику, але це необов'язково, ми можемо це пропустити. Можна повернути будь-який тип даних, навіть функцію, про це ми розповімо пізніше.</p></li>
</ul>
</li>
</ol>
<p><strong>ПОРАДА!</strong> Коли ваш код стає довшим і складнішим, коментарі допомагають вам та іншим, хто читає ваш код, орієнтуватися в ньому та розуміти, що ви намагаєтеся зробити. Звичка часто коментувати допоможе вам уникнути помилок у кодуванні, розуміти напрямок розвитку коду під час його написання та знаходити помилки, коли ви їх робите. Також прийнято розміщувати опис функції, автора та дату створення в описовому рядку під заголовком функції, хоча це і необов'язково (ви можете пропустити описовий рядок). Ми наполегливо рекомендуємо вам активно коментувати власний код.</p>
<p><strong>СПРОБУЙТЕ!</strong> Визначте функцію з назвою <em>my_adder</em>, яка приймає 3 числа та обчислює їх суму.</p>


<pre><span></span><span>def</span> <span>my_adder</span><span>(</span><span>a</span><span>,</span> <span>b</span><span>,</span> <span>c</span><span>):</span>
    <span>"""</span>
<span>    функція для сумування 3 чисел</span>
<span>    Вхід: 3 числа a, b, c</span>
<span>    Вихід: сума a, b, та c</span>
<span>    автор:</span>
<span>    дата:</span>
<span>    """</span>
    
    <span># це підсумовування</span>
    <span>out</span> <span>=</span> <span>a</span> <span>+</span> <span>b</span> <span>+</span> <span>c</span>
    
    <span>return</span> <span>out</span>
</pre>



<p><strong>УВАГА!</strong> Якщо ви не зробите відступ у коді при визначенні функції, ви отримаєте <strong>IndentationError</strong>.</p>


<pre><span></span><span>def</span> <span>my_adder</span><span>(</span><span>a</span><span>,</span> <span>b</span><span>,</span> <span>c</span><span>):</span>
<span>"""</span>
<span>функція для сумування 3 чисел</span>
<span>Вхід: 3 числа a, b, c</span>
<span>Вихід: сума a, b, та c</span>
<span>автор:</span>
<span>дата:</span>
<span>"""</span>

<span># це підсумовування</span>
<span>out</span> <span>=</span> <span>a</span> <span>+</span> <span>b</span> <span>+</span> <span>c</span>

<span>return</span> <span>out</span>
</pre>



<pre><span></span><span>  File</span><span> "&lt;ipython-input-5-e6a61721f00e&gt;"</span><span>, line </span><span>8</span>
    <span>"""</span>
<span>       </span>
<span>^</span>
<span>IndentationError</span>: expected an indented block
</pre>



<p><strong>ПОРАДА!</strong> 4 пробіли — це один рівень відступу, ви можете мати глибші рівні відступів, коли у вас є вкладені функції або інструкції if (ви побачите це в наступному розділі). Також, іноді вам потрібно додати або прибрати відступ для цілого блоку коду. Ви можете зробити це, спочатку виділивши всі рядки в блоці коду, а потім натиснувши <em>Tab</em> та <em>Shift+Tab</em>, щоб збільшити або зменшити рівень відступу.</p>
<p><strong>ПОРАДА!</strong> Формуйте хороші практики кодування, даючи змінним та функціям описові імена, часто коментуючи та уникаючи зайвих рядків коду.</p>
<p>Для порівняння, розгляньте наступну функцію, яка виконує те ж завдання, що й my_adder, але написана погано. Як ви можете бачити, надзвичайно важко зрозуміти, що відбувається і який був намір автора.</p>
<p><strong>ПРИКЛАД</strong>: Поганий приклад реалізації my_adder.</p>


<pre><span></span><span>def</span> <span>abc</span><span>(</span><span>a</span><span>,</span> <span>s2</span><span>,</span> <span>d</span><span>):</span>
    <span>z</span> <span>=</span> <span>a</span> <span>+</span> <span>s2</span>
    <span>z</span> <span>=</span> <span>z</span> <span>+</span> <span>d</span>
    <span>x</span> <span>=</span> <span>z</span>
    <span>return</span> <span>x</span>
</pre>



<p>Функції повинні відповідати схемі іменування, подібній до змінних. Вони можуть містити лише літерно-цифрові символи та підкреслення, а перший символ має бути літерою.</p>
<p><strong>ПОРАДА!</strong> За домовленістю, як і імена змінних, імена функцій повинні бути в нижньому регістрі, зі словами, розділеними підкресленнями за потреби для покращення читабельності.</p>
<p><strong>ПОРАДА!</strong> Хорошою практикою програмування є часте збереження під час написання функції. Насправді, багато програмістів повідомляють, що зберігають файл за допомогою комбінації клавіш ctrl+s (PC) або cmd+s (Mac) щоразу, коли припиняють друкувати!</p>
<p><strong>СПРОБУЙТЕ!</strong> Використайте вашу функцію my_adder для обчислення суми кількох чисел. Перевірте, чи правильний результат. Спробуйте викликати функцію help для my_adder.</p>


<pre><span></span><span>d</span> <span>=</span> <span>my_adder</span><span>(</span><span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>)</span>
<span>d</span>
</pre>



<pre><span></span>6
</pre>





<pre><span></span><span>d</span> <span>=</span> <span>my_adder</span><span>(</span><span>4</span><span>,</span> <span>5</span><span>,</span> <span>6</span><span>)</span>
<span>d</span>
</pre>



<pre><span></span>15
</pre>





<pre><span></span><span>help</span><span>(</span><span>my_adder</span><span>)</span>
</pre>



<pre><span></span>Довідка по функції my_adder в модулі __main__:

my_adder(a, b, c)
    функція для сумування 3 чисел
    Вхід: 3 числа a, b, c
    Вихід: сума a, b, та c
    автор:
    дата:
</pre>



<p><strong>ЩО ВІДБУВАЄТЬСЯ?</strong> Спочатку згадайте, що оператор присвоєння працює справа наліво. Це означає, що <em>my_adder(1,2,3)</em> обчислюється перед присвоєнням значення змінній <em>d</em>.</p>
<ol>
<li><p>Python знаходить функцію <em>my_adder</em>.</p></li>
<li><p><em>my_adder</em> приймає перше значення вхідного аргументу 1 і присвоює його змінній з іменем <em>a</em> (перше ім'я змінної у списку вхідних аргументів).</p></li>
<li><p><em>my_adder</em> приймає друге значення вхідного аргументу 2 і присвоює його змінній з іменем <em>b</em> (друге ім'я змінної у списку вхідних аргументів).</p></li>
<li><p><em>my_adder</em> приймає третє значення вхідного аргументу 3 і присвоює його змінній з іменем <em>c</em> (третє ім'я змінної у списку вхідних аргументів).</p></li>
<li><p><em>my_adder</em> обчислює суму <em>a</em>, <em>b</em>, та <em>c</em>, що дорівнює 1 + 2 + 3 = 6.</p></li>
<li><p><em>my_adder</em> присвоює значення 6 змінній <em>out</em>.</p></li>
<li><p><em>my_adder</em> повертає значення, що міститься у вихідній змінній <em>out</em>, тобто 6.</p></li>
<li><p><em>my_adder(1,2,3)</em> еквівалентно значенню 6, і це значення присвоюється змінній з іменем <em>d</em>.</p></li>
</ol>
<p>Python надає користувачеві величезну свободу присвоювати змінним різні типи даних. Наприклад, можна присвоїти змінній x значення словника або дійсного числа. В інших мовах програмування це не завжди так, ви повинні оголосити на початку сесії, чи буде x словником або дійсним числом, і потім ви з цим залишаєтеся. Це може бути як перевагою, так і недоліком (докладніше про це в Розділі XXX). Наприклад, функція <em>my_adder</em> була створена з припущенням, що вхідні аргументи будуть числовими типами, або int, або float. Однак користувач може випадково передати список або рядок у <em>my_adder</em>, що є неправильним. Якщо ви спробуєте передати нечисловий тип вхідного аргументу в <em>my_adder</em>, Python продовжуватиме виконувати функцію, доки щось не піде не так.</p>
<p><strong>СПРОБУЙТЕ!</strong> Використайте рядок ‘1’ як один із вхідних аргументів для <em>my_adder</em>. Також використайте список як один із вхідних аргументів для <em>my_adder</em>.</p>


<pre><span></span><span>d</span> <span>=</span> <span>my_adder</span><span>(</span><span>'1'</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>)</span>
</pre>



<pre><span></span><span>---------------------------------------------------------------------------</span>
<span>TypeError</span><span>                                 </span>Traceback (most recent call last)
<span>&lt;</span><span>ipython</span><span>-</span><span>input</span><span>-</span><span>10</span><span>-</span><span>245</span><span>d0f4254a9</span><span>&gt;</span> <span>in</span> <span>&lt;</span><span>module</span><span>&gt;</span>
<span>----&gt; </span><span>1</span> <span>d</span> <span>=</span> <span>my_adder</span><span>(</span><span>'1'</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>)</span>

<span>&lt;ipython-input-4-72d064c3ba7a&gt;</span> in <span>my_adder</span><span>(a, b, c)</span>
<span>      </span><span>9</span> 
<span>     </span><span>10</span>     <span># this is the summation</span>
<span>---&gt; </span><span>11</span>     <span>out</span> <span>=</span> <span>a</span> <span>+</span> <span>b</span> <span>+</span> <span>c</span>
<span>     </span><span>12</span> 
<span>     </span><span>13</span>     <span>return</span> <span>out</span>

<span>TypeError</span>: must be str, not int
</pre>





<pre><span></span><span>d</span> <span>=</span> <span>my_adder</span><span>(</span><span>1</span><span>,</span> <span>2</span><span>,</span> <span>[</span><span>2</span><span>,</span> <span>3</span><span>])</span>
</pre>



<pre><span></span><span>---------------------------------------------------------------------------</span>
<span>TypeError</span><span>                                 </span>Traceback (most recent call last)
<span>&lt;</span><span>ipython</span><span>-</span><span>input</span><span>-</span><span>11</span><span>-</span><span>04</span><span>f0428ffc51</span><span>&gt;</span> <span>in</span> <span>&lt;</span><span>module</span><span>&gt;</span>
<span>----&gt; </span><span>1</span> <span>d</span> <span>=</span> <span>my_adder</span><span>(</span><span>1</span><span>,</span> <span>2</span><span>,</span> <span>[</span><span>2</span><span>,</span> <span>3</span><span>])</span>

<span>&lt;ipython-input-4-72d064c3ba7a&gt;</span> in <span>my_adder</span><span>(a, b, c)</span>
<span>      </span><span>9</span> 
<span>     </span><span>10</span>     <span># this is the summation</span>
<span>---&gt; </span><span>11</span>     <span>out</span> <span>=</span> <span>a</span> <span>+</span> <span>b</span> <span>+</span> <span>c</span>
<span>     </span><span>12</span> 
<span>     </span><span>13</span>     <span>return</span> <span>out</span>

<span>TypeError</span>: unsupported operand type(s) for +: 'int' and 'list'
</pre>



<p><strong>ПОРАДА!</strong> Не забувайте читати помилки, які видає Python. Вони зазвичай точно вказують, де виникла проблема. У цьому випадку помилка говорить <em>—&gt; 11     out = a + b + c</em>, що означає, що сталася помилка в my_adder на 11-му рядку. Причиною помилки є <strong>TypeError</strong>, оскільки <em>unsupported operand type(s) for +: ‘int` and ‘list`</em>, що означає, що ми не могли додати int та list.</p>
<p>На даному етапі ви не маєте контролю над тим, які вхідні аргументи користувач передає вашій функції, і чи відповідають вони тому, що ви очікували. Тому наразі пишіть свої функції, припускаючи, що їх будуть використовувати правильно. Ви можете допомогти собі та іншим користувачам правильно використовувати вашу функцію, добре коментуючи свій код.</p>
<p>Ви можете комбінувати функції, передаючи виклики одних функцій як вхідні дані для інших. Відповідно до порядку операцій, Python спочатку виконає виклик найбільш вкладеної функції. Ви також можете передавати математичні вирази як вхідні дані для функцій. У цьому випадку Python спочатку обчислить математичні вирази.</p>
<p><strong>СПРОБУЙТЕ!</strong> Використайте функцію <em>my_adder</em> для обчислення суми <span>\(sin ({\pi})\)</span>, <span>\(cos ({\pi})\)</span> та <span>\(tan ({\pi})\)</span>. Використовуйте математичні вирази як вхідні дані для <em>my_adder</em> та перевірте, що вона виконує операції правильно.</p>


<pre><span></span><span>d</span> <span>=</span> <span>my_adder</span><span>(</span><span>np</span><span>.</span><span>sin</span><span>(</span><span>np</span><span>.</span><span>pi</span><span>),</span> <span>np</span><span>.</span><span>cos</span><span>(</span><span>np</span><span>.</span><span>pi</span><span>),</span> <span>np</span><span>.</span><span>tan</span><span>(</span><span>np</span><span>.</span><span>pi</span><span>))</span>
<span>d</span>
</pre>



<pre><span></span>-1.0
</pre>





<pre><span></span><span>d</span> <span>=</span> <span>my_adder</span><span>(</span><span>5</span> <span>+</span> <span>2</span><span>,</span> <span>3</span> <span>*</span> <span>4</span><span>,</span> <span>12</span> <span>/</span> <span>6</span><span>)</span>
<span>d</span>
</pre>



<pre><span></span>21.0
</pre>





<pre><span></span><span>d</span> <span>=</span> <span>(</span><span>5</span> <span>+</span> <span>2</span><span>)</span> <span>+</span> <span>3</span> <span>*</span> <span>4</span> <span>+</span> <span>12</span> <span>/</span> <span>6</span>
<span>d</span>
</pre>



<pre><span></span>21.0
</pre>



<p>Функції Python можуть мати кілька вихідних параметрів. При виклику функції з кількома вихідними параметрами ви можете вказати кілька змінних для присвоєння, розділивши їх комами. Функція, по суті, поверне кілька параметрів-результатів у кортежі, тому ви можете розпакувати повернутий кортеж. Розгляньте наступну функцію (зверніть увагу, що вона має кілька вихідних параметрів):</p>


<pre><span></span><span>def</span> <span>my_trig_sum</span><span>(</span><span>a</span><span>,</span> <span>b</span><span>):</span>
    <span>"""</span>
<span>    функція для демонстрації повернення кількох значень</span>
<span>    автор</span>
<span>    дата</span>
<span>    """</span>
    <span>out1</span> <span>=</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>a</span><span>)</span> <span>+</span> <span>np</span><span>.</span><span>cos</span><span>(</span><span>b</span><span>)</span>
    <span>out2</span> <span>=</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>b</span><span>)</span> <span>+</span> <span>np</span><span>.</span><span>cos</span><span>(</span><span>a</span><span>)</span>
    <span>return</span> <span>out1</span><span>,</span> <span>out2</span><span>,</span> <span>[</span><span>out1</span><span>,</span> <span>out2</span><span>]</span>
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Обчисліть функцію <em>my_trig_sum</em> для <em>a=2</em> та <em>b=3</em>. Присвойте перший вихідний параметр змінній <em>c</em>, другий вихідний параметр змінній <em>d</em>, а третій параметр змінній <em>e</em>.</p>


<pre><span></span><span>c</span><span>,</span> <span>d</span><span>,</span> <span>e</span> <span>=</span> <span>my_trig_sum</span><span>(</span><span>2</span><span>,</span> <span>3</span><span>)</span>
<span>print</span><span>(</span><span>f</span><span>"c =</span><span>{</span><span>c</span><span>}</span><span>, d=</span><span>{</span><span>d</span><span>}</span><span>, e=</span><span>{</span><span>e</span><span>}</span><span>"</span><span>)</span>
</pre>



<pre><span></span>c =-0.0806950697747637, d=-0.2750268284872752, e=[-0.0806950697747637, -0.2750268284872752]
</pre>



<p>Якщо ви присвоїте результати одній змінній, ви отримаєте кортеж, який містить усі вихідні параметри.</p>
<p><strong>СПРОБУЙТЕ!</strong> Обчисліть функцію <em>my_trig_sum</em> для <em>a=2</em> та <em>b=3</em>. Перевірте, що вихідні дані є кортежем.</p>


<pre><span></span><span>c</span> <span>=</span> <span>my_trig_sum</span><span>(</span><span>2</span><span>,</span> <span>3</span><span>)</span>
<span>print</span><span>(</span><span>f</span><span>"c=</span><span>{</span><span>c</span><span>}</span><span>, і повернутий тип </span><span>{</span><span>type</span><span>(</span><span>c</span><span>)</span><span>}</span><span>"</span><span>)</span>
</pre>



<pre><span></span>c=(-0.0806950697747637, -0.2750268284872752, [-0.0806950697747637, -0.2750268284872752]), і повернутий тип &lt;class 'tuple'&gt;
</pre>



<p>Функцію можна визначити без вхідних аргументів і без повернення будь-якого значення. Наприклад:</p>


<pre><span></span><span>def</span> <span>print_hello</span><span>():</span>
    <span>print</span><span>(</span><span>'Hello'</span><span>)</span>
</pre>





<pre><span></span><span>print_hello</span><span>()</span>
</pre>



<pre><span></span>Hello
</pre>



<p><strong>Примітка!</strong> Навіть якщо немає вхідних аргументів, при виклику функції все одно потрібні дужки.</p>
<p>Для вхідних аргументів ми також можемо мати значення за замовчуванням. Дивіться наступний приклад.</p>
<p><strong>ПРИКЛАД:</strong> Запустіть наступну функцію з вхідними даними та без них.</p>


<pre><span></span><span>def</span> <span>print_greeting</span><span>(</span><span>day</span> <span>=</span> <span>'Monday'</span><span>,</span> <span>name</span> <span>=</span> <span>'Qingkai'</span><span>):</span>
    <span>print</span><span>(</span><span>f</span><span>'Greetings, </span><span>{</span><span>name</span><span>}</span><span>, today is </span><span>{</span><span>day</span><span>}</span><span>'</span><span>)</span>
</pre>





<pre><span></span><span>print_greeting</span><span>()</span>
</pre>



<pre><span></span>Greetings, Qingkai, today is Monday
</pre>





<pre><span></span><span>print_greeting</span><span>(</span><span>name</span> <span>=</span> <span>'Timmy'</span><span>,</span> <span>day</span> <span>=</span> <span>'Friday'</span><span>)</span>
</pre>



<pre><span></span>Greetings, Timmy, today is Friday
</pre>





<pre><span></span><span>print_greeting</span><span>(</span><span>name</span> <span>=</span> <span>'Alex'</span><span>)</span>
</pre>



<pre><span></span>Greetings, Alex, today is Monday
</pre>



<p>Ми бачимо, що якщо ми надаємо значення аргументу при визначенні функції, це значення стає значенням за замовчуванням для цієї функції. Якщо користувач не надає вхідних даних для цього аргументу, то під час виклику функції буде використано це значення за замовчуванням. Крім того, порядок аргументів не важливий при виклику функції, якщо ви вказуєте ім'я аргументу.</p>
