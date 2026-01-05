<h1>Типи помилок<a href="#error-types" title="Постійне посилання на цей заголовок"></a></h1>
<p>Ми вже згадували про помилки раніше, але ще не говорили про них детально. Існує три основні типи помилок, про які програмістам потрібно знати: <strong>Синтаксичні помилки</strong>, <strong>помилки виконання</strong> та <strong>Логічні помилки</strong>. <strong>Синтаксис</strong> — це набір правил, що керують мовою. У письмовій та розмовній мові правила можуть бути змінені або навіть порушені, щоб пристосуватися до мовця чи письменника. Однак у мові програмування правила є жорсткими. Синтаксична помилка виникає, коли програміст пише інструкцію, використовуючи неправильний синтаксис, і Python не може зрозуміти, що ви говорите. Наприклад, <code><span>1</span> <span>=</span> <span>x</span></code> не є допустимим у мові програмування Python, оскільки числа не можуть бути присвоєні як змінні. Якщо програміст спробує виконати одну з цих інструкцій або будь-яку іншу синтаксично некоректну заяву, Python поверне помилку програмісту та вкаже рядок, де сталася помилка. Примітка: вказане місце є тим, де синтаксична помилка виявляється парсером; іноді місце, що спричиняє помилку, може бути далеко від вказаного рядка.</p>
<p><strong>ПРИКЛАД:</strong> Приклади синтаксичних помилок.</p>


<pre><span></span><span>1</span> <span>=</span> <span>x</span>
</pre>



<pre><span></span><span>  File</span><span> "&lt;ipython-input-1-7a7b257d8e3d&gt;"</span><span>, line </span><span>1</span>
<span>    </span><span>1</span> <span>=</span> <span>x</span>
         <span>^</span>
<span>SyntaxError</span>: can't assign to literal
</pre>





<pre><span></span><span>(</span><span>1</span><span>]</span>
</pre>



<pre><span></span><span>  File</span><span> "&lt;ipython-input-2-800df0a5e99c&gt;"</span><span>, line </span><span>1</span>
    <span>(</span><span>1</span><span>]</span>
      <span>^</span>
<span>SyntaxError</span>: invalid syntax
</pre>





<pre><span></span><span>if</span> <span>True</span>
    <span>print</span><span>(</span><span>'Here'</span><span>)</span>
</pre>



<pre><span></span><span>  File</span><span> "&lt;ipython-input-3-025e9fce1ee3&gt;"</span><span>, line </span><span>1</span>
    <span>if</span> <span>True</span>
           <span>^</span>
<span>SyntaxError</span>: invalid syntax
</pre>



<p>Останній рядок повідомлення про помилку показує, що сталося – <code><span>SyntaxError</span></code>, а попередні рядки вказують, де помилка виникає в контексті коду. Загалом, синтаксичні помилки зазвичай легко виявити, легко знайти та легко виправити.</p>
<p>Навіть якщо весь синтаксис у вашому коді правильний, це все одно може спричинити помилку під час виконання коду. Помилки, що виникають під час виконання, називаються <strong>винятками</strong> або <strong>помилками виконання</strong>. Винятки складніше знайти, і вони виявляються лише під час запуску програми. Примітка: винятки не є фатальними. Ми дізнаємося пізніше, як їх обробляти в Python. Якщо ми їх не обробимо, Python завершить програму. Розглянемо кілька прикладів нижче.</p>


<pre><span></span><span>1</span><span>/</span><span>0</span>
</pre>



<pre><span></span><span>---------------------------------------------------------------------------</span>
<span>ZeroDivisionError</span><span>                         </span>Traceback (most recent call last)
<span>&lt;</span><span>ipython</span><span>-</span><span>input</span><span>-</span><span>4</span><span>-</span><span>9e1622</span><span>b385b6</span><span>&gt;</span> <span>in</span> <span>&lt;</span><span>module</span><span>&gt;</span>
<span>----&gt; </span><span>1</span> <span>1</span><span>/</span><span>0</span>

<span>ZeroDivisionError</span>: division by zero
</pre>





<pre><span></span><span>x</span> <span>=</span> <span>[</span><span>2</span><span>]</span>
<span>x</span> <span>+</span> <span>2</span>
</pre>



<pre><span></span><span>---------------------------------------------------------------------------</span>
<span>TypeError</span><span>                                 </span>Traceback (most recent call last)
<span>&lt;</span><span>ipython</span><span>-</span><span>input</span><span>-</span><span>5</span><span>-</span><span>29</span><span>a14b9fefb9</span><span>&gt;</span> <span>in</span> <span>&lt;</span><span>module</span><span>&gt;</span>
<span>      </span><span>1</span> <span>x</span> <span>=</span> <span>[</span><span>2</span><span>]</span>
<span>----&gt; </span><span>2</span> <span>x</span> <span>+</span> <span>2</span>

<span>TypeError</span>: can only concatenate list (not "int") to list
</pre>





<pre><span></span><span>print</span><span>(</span><span>a</span><span>)</span>
</pre>



<pre><span></span><span>---------------------------------------------------------------------------</span>
<span>NameError</span><span>                                 </span>Traceback (most recent call last)
<span>&lt;</span><span>ipython</span><span>-</span><span>input</span><span>-</span><span>6</span><span>-</span><span>bca0e2660b9f</span><span>&gt;</span> <span>in</span> <span>&lt;</span><span>module</span><span>&gt;</span>
<span>----&gt; </span><span>1</span> <span>print</span><span>(</span><span>a</span><span>)</span>

<span>NameError</span>: name 'a' is not defined
</pre>



<p>Як показано в прикладах вище, існують різні типи вбудованих винятків: <code><span>ZeroDivisionError</span></code>, <code><span>TypeError</span></code> та <code><span>NameError</span></code>. Повний список вбудованих винятків можна знайти в <a href="https://docs.python.org/3/library/exceptions.html#bltin-exceptions">документації Python</a>. Звісно, ви можете визначити власні типи винятків, але ми не будемо розглядати це тут; якщо вам цікаво, як визначити власні винятки, перегляньте <a href="https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions">тут</a>.</p>
<p>Більшість винятків легко знайти, оскільки Python зупинить виконання та повідомить вам, де проблема. Після програмування функції досвідчені програмісти зазвичай запускають функцію кілька разів, дозволяючи функції "викидати" будь-які помилки, щоб вони могли їх виправити. Але відсутність винятків не означає, що функція працює правильно.</p>
<p>Один з найскладніших для виявлення типів помилок називається <strong>логічною помилкою</strong>. Логічна помилка не викликає винятку, і програма працюватиме безперебійно, але це помилка, оскільки отриманий результат не є очікуваним рішенням. Наприклад, розглянемо наступну помилкову реалізацію функції факторіалу.</p>


<pre><span></span><span>def</span> <span>my_bad_factorial</span><span>(</span><span>n</span><span>):</span>
    <span>out</span> <span>=</span> <span>0</span>
    <span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>1</span><span>,</span> <span>n</span><span>+</span><span>1</span><span>):</span>
        <span>out</span> <span>=</span> <span>out</span><span>*</span><span>i</span>
        
    <span>return</span> <span>out</span>
</pre>





<pre><span></span><span>my_bad_factorial</span><span>(</span><span>4</span><span>)</span>
</pre>



<pre><span></span>0
</pre>



<p>Ця функція не викличе помилки виконання для будь-якого вхідного значення, яке є дійсним для правильно реалізованої функції факторіалу; однак, якщо ви спробуєте використати <code><span>my_bad_factorial</span></code>, ви побачите, що відповідь завжди 0, оскільки `out` ініціалізується значенням 0 замість 1. Отже, рядок `out = 0` є логічною помилкою. Він не викликає помилки виконання Python, але призводить до неправильного обчислення факторіалу.</p>
<p>Хоча логічні помилки здаються малоймовірними – або принаймні такими ж легкими для виявлення, як інші види помилок – коли програми стають довшими та складнішими, ці типи помилок дуже легко генерувати та надзвичайно важко знайти. Коли виникають логічні помилки, у вас немає іншого вибору, окрім як ретельно переглядати кожен рядок вашого коду, доки ви не знайдете проблему. У таких випадках важливо точно знати, як Python реагуватиме на кожну вашу команду, і не робити жодних припущень. Ви також можете використовувати налагоджувач Python, який буде описаний в останньому розділі цієї глави.</p>
