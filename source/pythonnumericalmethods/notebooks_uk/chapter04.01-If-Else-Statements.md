<h1>Оператори If-Else<a href="#if-else-statements" title="Постійне посилання на цей заголовок"></a></h1>
<p><strong>Оператор розгалуження</strong>, <strong>оператор If-Else</strong>, або скорочено <strong>оператор If</strong>, — це конструкція коду, яка виконує блоки коду лише за умови виконання певних умов. Ці умови представлені як логічні вирази. Нехай <span>\(P\)</span>, <span>\(Q\)</span> та <span>\(R\)</span> — деякі логічні вирази в Python. Нижче показано конструкцію оператора if.</p>
<p><strong>КОНСТРУКЦІЯ</strong>: Простий синтаксис оператора If-Else</p>
<pre><span></span>if logical expression:
    code block
</pre>

<p>Слово "if" є ключовим словом. Коли Python зустрічає оператор if, він визначає, чи є пов'язаний логічний вираз істинним. Якщо він істинний, тоді код у <em>блоці коду</em> буде виконано. Якщо він хибний, тоді код в операторі if не буде виконано. Це слід читати так: "Якщо логічний вираз істинний, тоді виконати блок коду".</p>
<p>Коли є кілька умов для розгляду, ви можете включити оператори elif; якщо ви хочете мати умову, яка охоплює будь-який інший випадок, тоді ви можете використовувати оператор else.</p>
<p><strong>Примітка!</strong> Python надає однаковий рівень відступу кожному рядку коду в межах умовного оператора.</p>
<p><strong>КОНСТРУКЦІЯ</strong>: Розширений синтаксис оператора If-Else</p>
<pre><span></span>if logical expression P:
    code block 1
elif logical expression Q:
    code block 2
elif logical expression R:
    code block 3
else:
    code block 4
   
</pre>

<p>У попередньому коді Python спочатку перевірить, чи є <span>\(\textit{P}\)</span> істинним. Якщо <span>\(\textit{P}\)</span> істинний, тоді буде виконано блок коду 1, а потім <span>\(\textit{оператор if}\)</span> завершиться. Іншими словами, Python <em>не</em> перевірятиме решту операторів, щойно він досягне істинного оператора. Однак, якщо <span>\(\textit{P}\)</span> хибний, тоді Python перевірить, чи є <span>\(\textit{Q}\)</span> істинним. Якщо <span>\(\textit{Q}\)</span> істинний, тоді буде виконано блок коду 2, і оператор if завершиться. Якщо він хибний, тоді буде виконано <span>\(\textit{R}\)</span>, і так далі. Якщо <span>\(\textit{P}\)</span>, <span>\(\textit{Q}\)</span> та <span>\(\textit{R}\)</span> є хибними, тоді буде виконано блок коду 4. Ви можете мати будь-яку кількість операторів elif (або жодного), якщо є принаймні один оператор if (перший оператор). Вам не потрібен оператор else, але ви можете мати щонайбільше один оператор else. Логічні вирази після if та elif (тобто, такі як P, Q та R) називатимуться умовними операторами.</p>
<p><strong>СПРОБУЙТЕ!</strong> Напишіть функцію *my_thermo_stat(temp, desired_temp)*. Повернене значення функції має бути рядком *‘Heat`* (Нагрівання), якщо temp менше desired_temp мінус 5 градусів, *‘AC`* (Кондиціонер), якщо temp більше desired_temp плюс 5, і *‘off`* (Вимкнено) в іншому випадку.</p>


<pre><span></span><span>def</span> <span>my_thermo_stat</span><span>(</span><span>temp</span><span>,</span> <span>desired_temp</span><span>):</span>
    <span>"""</span>
<span>    Змінює статус термостата на основі </span>
<span>    температури та бажаної температури</span>
<span>    автор</span>
<span>    дата</span>
<span>    :type temp: Int</span>
<span>    :type desiredTemp: Int</span>
<span>    :rtype: String</span>
<span>    """</span>
    <span>if</span> <span>temp</span> <span>&lt;</span> <span>desired_temp</span> <span>-</span> <span>5</span><span>:</span>
        <span>status</span> <span>=</span> <span>'Heat'</span>
    <span>elif</span> <span>temp</span> <span>&gt;</span> <span>desired_temp</span> <span>+</span> <span>5</span><span>:</span>
        <span>status</span> <span>=</span> <span>'AC'</span>
    <span>else</span><span>:</span>
        <span>status</span> <span>=</span> <span>'off'</span>
    <span>return</span> <span>status</span>
</pre>





<pre><span></span><span>status</span> <span>=</span> <span>my_thermo_stat</span><span>(</span><span>65</span><span>,</span><span>75</span><span>)</span>
<span>print</span><span>(</span><span>status</span><span>)</span>
</pre>



<pre><span></span>Heat
</pre>





<pre><span></span><span>status</span> <span>=</span> <span>my_thermo_stat</span><span>(</span><span>75</span><span>,</span><span>65</span><span>)</span>
<span>print</span><span>(</span><span>status</span><span>)</span>
</pre>



<pre><span></span>AC
</pre>





<pre><span></span><span>status</span> <span>=</span> <span>my_thermo_stat</span><span>(</span><span>65</span><span>,</span><span>63</span><span>)</span>
<span>print</span><span>(</span><span>status</span><span>)</span>
</pre>



<pre><span></span>off
</pre>



<p><strong>ПРИКЛАД</strong>: Яким буде значення y після виконання наступного скрипту?</p>


<pre><span></span><span>x</span> <span>=</span> <span>3</span>
<span>if</span> <span>x</span> <span>&gt;</span> <span>1</span><span>:</span>
    <span>y</span> <span>=</span> <span>2</span>
<span>elif</span> <span>x</span> <span>&gt;</span> <span>2</span><span>:</span>
    <span>y</span> <span>=</span> <span>4</span>
<span>else</span><span>:</span>
    <span>y</span> <span>=</span> <span>0</span>
<span>print</span><span>(</span><span>y</span><span>)</span>
</pre>



<pre><span></span>2
</pre>



<p>Ми також можемо вставляти складніші умовні оператори, використовуючи логічні оператори.</p>
<p><strong>ПРИКЛАД:</strong> Яким буде значення y після виконання наступного коду?</p>


<pre><span></span><span>x</span> <span>=</span> <span>3</span>
<span>if</span> <span>x</span> <span>&gt;</span> <span>1</span> <span>and</span> <span>x</span> <span>&lt;</span> <span>2</span><span>:</span>
    <span>y</span> <span>=</span> <span>2</span>
<span>elif</span> <span>x</span> <span>&gt;</span> <span>2</span> <span>and</span> <span>x</span> <span>&lt;</span> <span>4</span><span>:</span>
    <span>y</span> <span>=</span> <span>4</span>
<span>else</span><span>:</span>
    <span>y</span> <span>=</span> <span>0</span>
<span>print</span><span>(</span><span>y</span><span>)</span>
</pre>



<pre><span></span>4
</pre>



<p>Зауважте, що якщо ви хочете логічний вираз a < x < b, це два умовні оператори: *a < x і x < b*. У Python ви також можете написати a < x < b. Наприклад:</p>


<pre><span></span><span>x</span> <span>=</span> <span>3</span>
<span>if</span> <span>1</span> <span>&lt;</span> <span>x</span> <span>&lt;</span> <span>2</span><span>:</span>
    <span>y</span> <span>=</span> <span>2</span>
<span>elif</span> <span>2</span> <span>&lt;</span> <span>x</span> <span>&lt;</span> <span>4</span><span>:</span>
    <span>y</span> <span>=</span> <span>4</span>
<span>else</span><span>:</span>
    <span>y</span> <span>=</span> <span>0</span>
<span>print</span><span>(</span><span>y</span><span>)</span>
</pre>



<pre><span></span>4
</pre>



<p>Оператор називається **вкладеним**, якщо він повністю міститься в іншому операторі того ж типу. Наприклад, **вкладений оператор if** — це оператор if, який повністю міститься в пункті іншого оператора if.</p>
<p><strong>ПРИКЛАД:</strong> Подумайте, що станеться, коли буде виконано наступний код. Які всі можливі результати на основі вхідних значень x та y?</p>


<pre><span></span><span>def</span> <span>my_nested_branching</span><span>(</span><span>x</span><span>,</span><span>y</span><span>):</span>
    <span>"""</span>
<span>    Приклад вкладеного оператора розгалуження</span>
<span>    автор</span>
<span>    дата</span>
<span>    :type x: Int</span>
<span>    :type y: Int</span>
<span>    :rtype: Int</span>
<span>    """</span>
    <span>if</span> <span>x</span> <span>&gt;</span> <span>2</span><span>:</span>
        <span>if</span> <span>y</span> <span>&lt;</span> <span>2</span><span>:</span>
            <span>out</span> <span>=</span> <span>x</span> <span>+</span> <span>y</span>
        <span>else</span><span>:</span>
            <span>out</span> <span>=</span> <span>x</span> <span>-</span> <span>y</span>
    <span>else</span><span>:</span>
        <span>if</span> <span>y</span> <span>&gt;</span> <span>2</span><span>:</span>
            <span>out</span> <span>=</span> <span>x</span><span>*</span><span>y</span>
        <span>else</span><span>:</span>
            <span>out</span> <span>=</span> <span>0</span>
    <span>return</span> <span>out</span>
</pre>



<p><strong>Примітка!</strong> Як і раніше, Python надає однаковий рівень відступу кожному рядку коду в межах умовного оператора. Вкладений оператор if має глибший відступ за рахунок збільшення на чотири пробіли. Ви отримаєте **IndentationError**, якщо відступ неправильний, як ми бачили при визначенні функцій.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
</pre>





<pre><span></span><span>all</span><span>([</span><span>1</span><span>,</span> <span>1</span><span>,</span> <span>0</span><span>])</span>
</pre>



<pre><span></span>False
</pre>



<p>Існує багато логічних функцій, розроблених для допомоги у створенні операторів розгалуження. Наприклад, ви можете запитати, чи має змінна певний тип даних, за допомогою функції *isinstance*. Також існують функції, які можуть надати інформацію про масиви логічних значень, такі як *any*, яка повертає true, якщо будь-який елемент у масиві є true, і false в іншому випадку, та *all*, яка повертає true лише тоді, коли всі елементи в масиві є true.</p>
<p>Іноді ви можете захотіти розробити свою функцію для перевірки вхідних даних, щоб переконатися, що ваша функція буде використовуватися належним чином. Наприклад, функція *my_adder* у попередньому розділі очікує на вхідні дані типу double. Якщо користувач вводить *список* або *рядок* як одну з вхідних змінних, тоді функція видасть помилку або матиме несподівані результати. Щоб запобігти цьому, ви можете додати перевірку, щоб повідомити користувачеві, що функція використовується неправильно. Ця та інші методи контролю помилок детальніше розглядаються в Розділі 10. Наразі вам потрібно лише знати, що ми можемо використовувати оператор <span>\(\texttt{raise}\)</span> з винятком <span>\(\texttt{TypeError}\)</span>, щоб зупинити виконання функції та видати помилку з певним текстом.</p>
<p><strong>ПРИКЛАД</strong>: Змініть *my_adder*, щоб видавати попередження, якщо користувач не вводить числові значення. Спробуйте свою функцію для нечислових вхідних даних, щоб показати, що перевірка працює. Коли оператор занадто довгий, ми можемо використовувати символ ‘' для розбиття рядка на кілька рядків.</p>


<pre><span></span><span>def</span> <span>my_adder</span><span>(</span><span>a</span><span>,</span> <span>b</span><span>,</span> <span>c</span><span>):</span>
    <span>"""</span>
<span>    Обчислює суму трьох чисел</span>
<span>    автор</span>
<span>    дата</span>
<span>    """</span>
    
    <span># Перевірка на помилкові вхідні дані</span>
    <span>if</span> <span>not</span> <span>(</span><span>isinstance</span><span>(</span><span>a</span><span>,</span> <span>(</span><span>int</span><span>,</span> <span>float</span><span>))</span> \
            <span>or</span> <span>isinstance</span><span>(</span><span>b</span><span>,</span> <span>(</span><span>int</span><span>,</span> <span>float</span><span>))</span> \
            <span>or</span> <span>isinstance</span><span>(</span><span>c</span><span>,</span> <span>(</span><span>int</span><span>,</span> <span>float</span><span>))):</span>
        <span>raise</span> <span>TypeError</span><span>(</span><span>'Вхідні дані мають бути числами.'</span><span>)</span>
    <span># Повернути результат</span>
    <span>return</span> <span>a</span> <span>+</span> <span>b</span> <span>+</span> <span>c</span>
</pre>





<pre><span></span><span>x</span> <span>=</span> <span>my_adder</span><span>(</span><span>1</span><span>,</span><span>2</span><span>,</span><span>3</span><span>)</span>
<span>print</span><span>(</span><span>x</span><span>)</span>
</pre>



<pre><span></span>6
</pre>





<pre><span></span><span>x</span> <span>=</span> <span>my_adder</span><span>(</span><span>'1'</span><span>,</span><span>'2'</span><span>,</span><span>'3'</span><span>)</span>
<span>print</span><span>(</span><span>x</span><span>)</span>
</pre>



<pre><span></span><span>---------------------------------------------------------------------------</span>
<span>TypeError</span><span>                                 </span>Traceback (most recent call last)
<span>&lt;</span><span>ipython</span><span>-</span><span>input</span><span>-</span><span>13</span><span>-</span><span>c3e353c636b0</span><span>&gt;</span> <span>in</span> <span>&lt;</span><span>module</span><span>&gt;</span>
<span>----&gt; </span><span>1</span> <span>x</span> <span>=</span> <span>my_adder</span><span>(</span><span>'1'</span><span>,</span><span>'2'</span><span>,</span><span>'3'</span><span>)</span>
<span>      </span><span>2</span> <span>print</span><span>(</span><span>x</span><span>)</span>

<span>&lt;ipython-input-11-0f3d29eecee0&gt;</span> in <span>my_adder</span><span>(a, b, c)</span>
<span>     </span><span>10</span>             <span>or</span> <span>isinstance</span><span>(</span><span>b</span><span>,</span> <span>(</span><span>int</span><span>,</span> <span>float</span><span>))</span> \
<span>     </span><span>11</span>             <span>or</span> <span>isinstance</span><span>(</span><span>c</span><span>,</span> <span>(</span><span>int</span><span>,</span> <span>float</span><span>))):</span>
<span>---&gt; </span><span>12</span>         <span>raise</span> <span>TypeError</span><span>(</span><span>'Вхідні дані мають бути числами.'</span><span>)</span>
<span>     </span><span>13</span>     <span># Return output</span>
<span>     </span><span>14</span>     <span>return</span> <span>a</span> <span>+</span> <span>b</span> <span>+</span> <span>c</span>

<span>TypeError</span>: Вхідні дані мають бути числами.
</pre>



<p>Існує велика різноманітність помилкових вхідних даних, з якими ваша функція може зіткнутися від користувачів, і нерозумно очікувати, що ваша функція перехопить їх усі. Тому, якщо не зазначено інше, пишіть свої функції, припускаючи, що вони будуть використовуватися належним чином.</p>
<p>Решта розділу містить ще кілька прикладів операторів розгалуження.</p>
<p><strong>СПРОБУЙТЕ!</strong> Напишіть функцію під назвою is_odd, яка повертає ‘odd` (непарне), якщо вхідне значення непарне, і ‘even` (парне), якщо воно парне. Можна припустити, що вхідне значення буде додатним цілим числом.</p>


<pre><span></span><span>def</span> <span>is_odd</span><span>(</span><span>number</span><span>):</span>
    <span>"""</span>
<span>    функція повертає 'odd', якщо вхідне значення непарне, </span>
<span>       'even' в іншому випадку</span>
<span>    автор</span>
<span>    дата</span>
<span>    :type number: Int</span>
<span>    :rtype: String</span>
<span>    """</span>
    <span># використовуємо оператор ділення за модулем, щоб перевірити, чи ділиться вхідне значення на 2</span>
    <span>if</span> <span>number</span> <span>%</span> <span>2</span> <span>==</span> <span>0</span><span>:</span>
        <span># якщо ділиться на 2, то вхідне значення не є непарним</span>
        <span>return</span> <span>'even'</span>
    <span>else</span><span>:</span>
        <span>return</span> <span>'odd'</span>
</pre>





<pre><span></span><span>is_odd</span><span>(</span><span>11</span><span>)</span>
</pre>



<pre><span></span>'odd'
</pre>





<pre><span></span><span>is_odd</span><span>(</span><span>2</span><span>)</span>
</pre>



<pre><span></span>'even'
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Напишіть функцію під назвою *my_circ_calc*, яка приймає числове значення *r* та рядок *calc* як вхідні аргументи. Можна припустити, що r є додатним, а *calc* — це рядок ‘area` (площа) або ‘circumference` (довжина кола). Функція *my_circ_calc* повинна обчислювати площу кола з радіусом *r*, якщо рядок *calc* — ‘area`, і довжину кола з радіусом *r*, якщо *calc* — ‘circumference`.</p>


<pre><span></span><span>np</span><span>.</span><span>pi</span>
</pre>



<pre><span></span>3.141592653589793
</pre>





<pre><span></span><span>def</span> <span>my_circ_calc</span><span>(</span><span>r</span><span>,</span> <span>calc</span><span>):</span>
    <span>"""</span>
<span>    Обчислює різні виміри кола</span>
<span>    автор</span>
<span>    дата</span>
<span>    :type r: Int or Float</span>
<span>    :type calc: String</span>
<span>    :rtype: Int or Float</span>
<span>    """</span>
    <span>if</span> <span>calc</span> <span>==</span> <span>'area'</span><span>:</span>
        <span>return</span> <span>np</span><span>.</span><span>pi</span><span>*</span><span>r</span><span>**</span><span>2</span>
    <span>elif</span> <span>calc</span> <span>==</span> <span>'circumference'</span><span>:</span>
        <span>return</span> <span>2</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>*</span><span>r</span>
</pre>





<pre><span></span><span>my_circ_calc</span><span>(</span><span>2.5</span><span>,</span> <span>'area'</span><span>)</span>
</pre>



<pre><span></span>19.634954084936208
</pre>





<pre><span></span><span>my_circ_calc</span><span>(</span><span>3</span><span>,</span> <span>'circumference'</span><span>)</span>
</pre>



<pre><span></span>18.84955592153876
</pre>



<p><strong>Примітка!</strong> Функція, яку ми пишемо, працює не тільки з одним значенням, але й з масивами Numpy (тобто та сама операція буде застосована до кожного елемента масиву). Дивіться наступний приклад, де ми могли б обчислити довжини кіл для радіусів [2, 3, 4] за допомогою масиву Numpy.</p>


<pre><span></span><span>my_circ_calc</span><span>(</span><span>np</span><span>.</span><span>array</span><span>([</span><span>2</span><span>,</span> <span>3</span><span>,</span> <span>4</span><span>]),</span> <span>'circumference'</span><span>)</span>
</pre>



<pre><span></span>array([12.56637061, 18.84955592, 25.13274123])
</pre>
