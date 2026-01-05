<h1>Вкладені функції<a href="#nested-functions" title="Постійне посилання на цей заголовок"></a></h1>
<p>Після створення та збереження нової функції вона поводиться так само, як будь-яка інша вбудована функція Python. Ви можете викликати функцію з будь-якого місця в блокноті, і будь-яка інша функція також може викликати її. <strong>Вкладена функція</strong> – це функція, яка визначена всередині іншої функції – <strong>батьківської функції</strong>. Тільки батьківська функція може викликати вкладену функцію. Однак вкладена функція зберігає окремий блок пам'яті від своєї батьківської функції.</p>
<p><strong>СПРОБУЙТЕ!</strong> Розгляньте наступну функцію та вкладену функцію.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>

<span>def</span> <span>my_dist_xyz</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>z</span><span>):</span>
    <span>"""</span>
<span>    x, y, z - це 2D координати, що містяться в кортежі</span>
<span>    вихід:</span>
<span>    d - список, де</span>
<span>        d[0] - це відстань між x та y</span>
<span>        d[1] - це відстань між x та z</span>
<span>        d[2] - це відстань між y та z</span>
<span>    """</span>
    
    <span>def</span> <span>my_dist</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>):</span>
        <span>"""</span>
<span>        підфункція для my_dist_xyz</span>
<span>        Вихід - це відстань між x та y, </span>
<span>        обчислена за формулою відстані</span>
<span>        """</span>
        <span>out</span> <span>=</span> <span>np</span><span>.</span><span>sqrt</span><span>((</span><span>x</span><span>[</span><span>0</span><span>]</span><span>-</span><span>y</span><span>[</span><span>0</span><span>])</span><span>**</span><span>2</span><span>+</span><span>(</span><span>x</span><span>[</span><span>1</span><span>]</span><span>-</span><span>y</span><span>[</span><span>1</span><span>])</span><span>**</span><span>2</span><span>)</span>
        <span>return</span> <span>out</span>
    
    <span>d0</span> <span>=</span> <span>my_dist</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>)</span>
    <span>d1</span> <span>=</span> <span>my_dist</span><span>(</span><span>x</span><span>,</span> <span>z</span><span>)</span>
    <span>d2</span> <span>=</span> <span>my_dist</span><span>(</span><span>y</span><span>,</span> <span>z</span><span>)</span>
    
    <span>return</span> <span>[</span><span>d0</span><span>,</span> <span>d1</span><span>,</span> <span>d2</span><span>]</span>
</pre>



<p>Зверніть увагу, що змінні <em>x</em> та <em>y</em> з'являються як у <em>my_dist_xyz</em>, так і в <em>my_dist</em>. Це дозволено, оскільки вкладена функція має окремий блок пам'яті від своєї батьківської функції. Вкладені функції корисні, коли завдання має бути виконано багато разів усередині функції, але не поза нею. Таким чином, вкладені функції допомагають батьківській функції виконувати своє завдання, залишаючись прихованими в ній.</p>
<p><strong>СПРОБУЙТЕ!</strong> Викличте функцію <em>my_dist_xyz</em> для x = (0, 0), y = (0, 1), z = (1, 1). Спробуйте викликати вкладену функцію <em>my_dist</em> у наступній комірці.</p>


<pre><span></span><span>d</span> <span>=</span> <span>my_dist_xyz</span><span>((</span><span>0</span><span>,</span> <span>0</span><span>),</span> <span>(</span><span>0</span><span>,</span> <span>1</span><span>),</span> <span>(</span><span>1</span><span>,</span> <span>1</span><span>))</span>
<span>print</span><span>(</span><span>d</span><span>)</span>
<span>d</span> <span>=</span> <span>my_dist</span><span>((</span><span>0</span><span>,</span> <span>0</span><span>),</span> <span>(</span><span>0</span><span>,</span> <span>1</span><span>))</span>
</pre>



<pre><span></span>[1.0, 1.4142135623730951, 1.0]
</pre>

<pre><span></span><span>---------------------------------------------------------------------------</span>
<span>NameError</span><span>                                 </span>Traceback (most recent call last)
<span>&lt;</span><span>ipython</span><span>-</span><span>input</span><span>-</span><span>2</span><span>-</span><span>1</span><span>bec838581d7</span><span>&gt;</span> <span>in</span> <span>&lt;</span><span>module</span><span>&gt;</span>
<span>      </span><span>1</span> <span>d</span> <span>=</span> <span>my_dist_xyz</span><span>((</span><span>0</span><span>,</span> <span>0</span><span>),</span> <span>(</span><span>0</span><span>,</span> <span>1</span><span>),</span> <span>(</span><span>1</span><span>,</span> <span>1</span><span>))</span>
<span>      </span><span>2</span> <span>print</span><span>(</span><span>d</span><span>)</span>
<span>----&gt; </span><span>3</span> <span>d</span> <span>=</span> <span>my_dist</span><span>((</span><span>0</span><span>,</span> <span>0</span><span>),</span> <span>(</span><span>0</span><span>,</span> <span>1</span><span>))</span>

<span>NameError</span>: name 'my_dist' is not defined
</pre>



<p>Нижче наведено повторений код без використання вкладеної функції. Зверніть увагу, наскільки завантаженішою та захаращенішою виглядає функція і наскільки складніше зрозуміти, що відбувається. Також зверніть увагу, що ця версія набагато більш схильна до помилок, оскільки у вас є три шанси неправильно ввести формулу відстані. Варто зазначити, що цю функцію можна було б написати більш компактно, використовуючи векторні операції. Ми залишаємо це як вправу.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>

<span>def</span> <span>my_dist_xyz</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>z</span><span>):</span>
    <span>"""</span>
<span>    x, y, z - це 2D координати, що містяться в кортежі</span>
<span>    вихід:</span>
<span>    d - список, де</span>
<span>        d[0] - це відстань між x та y</span>
<span>        d[1] - це відстань між x та z</span>
<span>        d[2] - це відстань між y та z</span>
<span>    """</span>
    
    <span>d0</span> <span>=</span> <span>np</span><span>.</span><span>sqrt</span><span>((</span><span>x</span><span>[</span><span>0</span><span>]</span><span>-</span><span>y</span><span>[</span><span>0</span><span>])</span><span>**</span><span>2</span><span>+</span><span>(</span><span>x</span><span>[</span><span>1</span><span>]</span><span>-</span><span>y</span><span>[</span><span>1</span><span>])</span><span>**</span><span>2</span><span>)</span>
    <span>d1</span> <span>=</span> <span>np</span><span>.</span><span>sqrt</span><span>((</span><span>x</span><span>[</span><span>0</span><span>]</span><span>-</span><span>z</span><span>[</span><span>0</span><span>])</span><span>**</span><span>2</span><span>+</span><span>(</span><span>x</span><span>[</span><span>1</span><span>]</span><span>-</span><span>z</span><span>[</span><span>1</span><span>])</span><span>**</span><span>2</span><span>)</span>
    <span>d2</span> <span>=</span> <span>np</span><span>.</span><span>sqrt</span><span>((</span><span>y</span><span>[</span><span>0</span><span>]</span><span>-</span><span>z</span><span>[</span><span>0</span><span>])</span><span>**</span><span>2</span><span>+</span><span>(</span><span>y</span><span>[</span><span>1</span><span>]</span><span>-</span><span>z</span><span>[</span><span>1</span><span>])</span><span>**</span><span>2</span><span>)</span>
    
    <span>return</span> <span>[</span><span>d0</span><span>,</span> <span>d1</span><span>,</span> <span>d2</span><span>]</span>
</pre>
