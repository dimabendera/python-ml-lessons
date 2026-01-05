```html
<h1>Перевірка типів<a href="#type-checking" title="Постійне посилання на цей заголовок"></a></h1>
<p>Python — це мова програмування з одночасно сильною та динамічною типізацією. Це означає, що будь-яка змінна може приймати будь-який тип даних у будь-який час (це динамічна типізація), але як тільки змінній присвоєно тип, він не може змінюватися несподіваним чином. Наприклад, ви можете написати <code><span>x</span> <span>=</span> <span>1</span></code> одразу після <code><span>x</span> <span>=</span> <span>"s"</span></code>, оскільки це мова з динамічною типізацією. Але ви не можете виконати <code><span>"3"</span> <span>+</span> <span>5</span></code>, оскільки це мова з сильною типізацією (рядок "3" не може бути перетворений на ціле число під час виконання). У мовах програмування зі статичною типізацією ви повинні оголосити, якого типу даних є ваша змінна, перед її використанням, і тип даних вашої змінної не може змінюватися в межах області видимості функції.</p>
<p>У випадку Python немає способу гарантувати, що користувач вашої функції вводить змінні очікуваного вами типу даних. Наприклад, функція <em>my_adder</em> з Розділу 3 призначена для додавання трьох чисел. Однак користувач може вводити рядки, списки, словники або функції, кожне з яких спричинить проблеми різного рівня складності. Ви можете змусити вашу функцію перевіряти тип вхідних змінних перед продовженням роботи та викликати помилку за допомогою функції помилки.</p>
<p><strong>СПРОБУЙТЕ!</strong> Змініть <em>my_adder</em> так, щоб вона перевіряла, чи є вхідні змінні числами з рухомою комою (floats). Якщо будь-яка з вхідних змінних не є числом з рухомою комою, функція повинна повернути відповідну помилку користувачеві за допомогою оператора <em>raise</em>. Перевірте свою функцію на помилкових вхідних аргументах, щоб переконатися, що перевірка працює.</p>


<pre><span></span><span>def</span> <span>my_adder</span><span>(</span><span>a</span><span>,</span> <span>b</span><span>,</span> <span>c</span><span>):</span>
    <span># перевірка типу</span>
    <span>if</span> <span>isinstance</span><span>(</span><span>a</span><span>,</span> <span>float</span><span>)</span> <span>and</span> <span>isinstance</span><span>(</span><span>b</span><span>,</span> <span>float</span><span>)</span> <span>and</span> <span>isinstance</span><span>(</span><span>c</span><span>,</span> <span>float</span><span>):</span>
        <span>pass</span>
    <span>else</span><span>:</span>
        <span>raise</span><span>(</span><span>TypeError</span><span>(</span><span>'Вхідні аргументи повинні бути числами з рухомою комою'</span><span>))</span>
        
    <span>out</span> <span>=</span> <span>a</span> <span>+</span> <span>b</span> <span>+</span> <span>c</span>
    <span>return</span> <span>out</span>
</pre>





<pre><span></span><span>my_adder</span><span>(</span><span>1.0</span><span>,</span> <span>2.0</span><span>,</span> <span>3.0</span><span>)</span>
</pre>



<pre><span></span>6.0
</pre>





<pre><span></span><span>my_adder</span><span>(</span><span>1.0</span><span>,</span> <span>2.0</span><span>,</span> <span>'3.0'</span><span>)</span>
</pre>



<pre><span></span><span>---------------------------------------------------------------------------</span>
<span>TypeError</span><span>                                 </span>Traceback (most recent call last)
<span>&lt;</span><span>ipython</span><span>-</span><span>input</span><span>-</span><span>6</span><span>-</span><span>14e4</span><span>b71b8c1d</span><span>&gt;</span> <span>in</span> <span>&lt;</span><span>module</span><span>&gt;</span>
<span>----&gt; </span><span>1</span> <span>my_adder</span><span>(</span><span>1.0</span><span>,</span> <span>2.0</span><span>,</span> <span>'3.0'</span><span>)</span>

<span>&lt;ipython-input-4-6073968d5755&gt;</span> in <span>my_adder</span><span>(a, b, c)</span>
<span>      </span><span>4</span>         <span>pass</span>
<span>      </span><span>5</span>     <span>else</span><span>:</span>
<span>----&gt; </span><span>6</span>         <span>raise</span><span>(</span><span>TypeError</span><span>(</span><span>'Вхідні аргументи повинні бути числами з рухомою комою'</span><span>))</span>
<span>      </span><span>7</span> 
<span>      </span><span>8</span>     <span>out</span> <span>=</span> <span>a</span> <span>+</span> <span>b</span> <span>+</span> <span>c</span>

<span>TypeError</span>: Вхідні аргументи повинні бути числами з рухомою комою
</pre>





<pre><span></span><span>my_adder</span><span>(</span><span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>)</span>
</pre>



<pre><span></span><span>---------------------------------------------------------------------------</span>
<span>TypeError</span><span>                                 </span>Traceback (most recent call last)
<span>&lt;</span><span>ipython</span><span>-</span><span>input</span><span>-</span><span>7</span><span>-</span><span>fc54adcab3d7</span><span>&gt;</span> <span>in</span> <span>&lt;</span><span>module</span><span>&gt;</span>
<span>----&gt; </span><span>1</span> <span>my_adder</span><span>(</span><span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>)</span>

<span>&lt;ipython-input-4-6073968d5755&gt;</span> in <span>my_adder</span><span>(a, b, c)</span>
<span>      </span><span>4</span>         <span>pass</span>
<span>      </span><span>5</span>     <span>else</span><span>:</span>
<span>----&gt; </span><span>6</span>         <span>raise</span><span>(</span><span>TypeError</span><span>(</span><span>'Вхідні аргументи повинні бути числами з рухомою комою'</span><span>))</span>
<span>      </span><span>7</span> 
<span>      </span><span>8</span>     <span>out</span> <span>=</span> <span>a</span> <span>+</span> <span>b</span> <span>+</span> <span>c</span>

<span>TypeError</span>: Вхідні аргументи повинні бути числами з рухомою комою
</pre>



<p>Ми помічаємо, що 1, 2, 3 є цілими числами, а не числами з рухомою комою, тому виникає помилка. Нам потрібно змінити функцію, щоб переконатися, що будь-які числа будуть додаватися.</p>


<pre><span></span><span>def</span> <span>my_adder</span><span>(</span><span>a</span><span>,</span> <span>b</span><span>,</span> <span>c</span><span>):</span>
    <span># перевірка типу</span>
    <span>if</span> <span>isinstance</span><span>(</span><span>a</span><span>,</span> <span>(</span><span>float</span><span>,</span> <span>int</span><span>,</span> <span>complex</span><span>))</span> <span>and</span> <span>isinstance</span><span>(</span><span>b</span><span>,</span> <span>(</span><span>float</span><span>,</span> <span>int</span><span>,</span> <span>complex</span><span>))</span> <span>and</span> <span>isinstance</span><span>(</span><span>c</span><span>,</span> <span>(</span><span>float</span><span>,</span> <span>int</span><span>,</span> <span>complex</span><span>)):</span>
        <span>pass</span>
    <span>else</span><span>:</span>
        <span>raise</span><span>(</span><span>Exception</span><span>(</span><span>'Вхідні аргументи повинні бути числами'</span><span>))</span>
        
    <span>out</span> <span>=</span> <span>a</span> <span>+</span> <span>b</span> <span>+</span> <span>c</span>
    <span>return</span> <span>out</span>
</pre>





<pre><span></span><span>my_adder</span><span>(</span><span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>)</span>
</pre>



<pre><span></span>6
</pre>





<pre><span></span><span>my_adder</span><span>(</span><span>1.0</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>)</span>
</pre>



<pre><span></span>6.0
</pre>





<pre><span></span><span>my_adder</span><span>(</span><span>1</span><span>j</span><span>,</span> <span>2</span><span>+</span><span>2</span><span>j</span><span>,</span> <span>3</span><span>+</span><span>2</span><span>j</span><span>)</span>
</pre>



<pre><span></span>(5+5j)
</pre>
```
