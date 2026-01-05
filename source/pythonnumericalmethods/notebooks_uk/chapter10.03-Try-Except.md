<h1>Try/Except<a href="#try-except" title="Постійне посилання на цей заголовок"></a></h1>
<p>Часто важливо писати програми, які можуть коректно обробляти певні типи помилок або винятків. Точніше, помилка або виняток не повинні викликати критичну помилку, яка призводить до завершення роботи вашої програми. Інструкція <strong>Try-Except</strong> — це блок коду, який дозволяє вашій програмі виконувати альтернативні дії у випадку виникнення помилки.</p>
<p><strong>КОНСТРУКЦІЯ:</strong> Інструкція Try-Except</p>
<pre><span></span>
<span>try</span><span>:</span>
    <span>блок</span> <span>коду</span> <span>1</span>
<span>except</span> <span>ExceptionName</span><span>:</span>
    <span>блок</span> <span>коду</span> <span>2</span>

</pre>

<p>Python спочатку спробує виконати код в інструкції <em>try</em> (блок коду 1). Якщо виняток не виникає, інструкція <em>except</em> пропускається, і виконання інструкції <em>try</em> завершується. Якщо виникає будь-який виняток, решта блоку пропускається. Потім, якщо тип винятку відповідає винятку, вказаному після ключового слова <em>except</em> (<em>ExceptionName</em>), буде виконано код в інструкції <em>except</em> (блок коду 2). Якщо ніщо в цьому блоці не зупиняє програму, вона продовжить виконувати решту коду поза блоками <em>try-except</em>. Якщо виняток не відповідає <em>ExceptionName</em>, він передається зовнішнім інструкціям <em>try</em>. Якщо інший обробник не знайдено, виконання зупиняється з повідомленням про помилку.</p>
<p><strong>ПРИКЛАД:</strong> Перехоплення винятку.</p>


<pre><span></span><span>x</span> <span>=</span> <span>'6'</span>
<span>try</span><span>:</span>
    <span>if</span> <span>x</span> <span>&gt;</span> <span>3</span><span>:</span>
        <span>print</span><span>(</span><span>'X більше за 3'</span><span>)</span>
<span>except</span> <span>TypeError</span><span>:</span>
    <span>print</span><span>(</span><span>"Ой! x не є допустимим числом. Спробуйте ще раз..."</span><span>)</span>
</pre>



<pre><span></span>Ой! x не є допустимим числом. Спробуйте ще раз...
</pre>



<p><strong>ПРИКЛАД:</strong> Якщо ваш обробник намагається перехопити виняток іншого типу, який <em>except</em> не перехоплює, ми отримаємо помилку, і виконання зупиниться.</p>


<pre><span></span><span>x</span> <span>=</span> <span>'6'</span>
<span>try</span><span>:</span>
    <span>if</span> <span>x</span> <span>&gt;</span> <span>3</span><span>:</span>
        <span>print</span><span>(</span><span>'X більше за 3'</span><span>)</span>
<span>except</span> <span>ValueError</span><span>:</span>
    <span>print</span><span>(</span><span>"Ой! x не є допустимим числом. Спробуйте ще раз..."</span><span>)</span>
</pre>



<pre><span></span><span>---------------------------------------------------------------------------</span>
<span>TypeError</span><span>                                 </span>Traceback (most recent call last)
<span>&lt;</span><span>ipython</span><span>-</span><span>input</span><span>-</span><span>2</span><span>-</span><span>899</span><span>d928e7a1f</span><span>&gt;</span> <span>in</span> <span>&lt;</span><span>module</span><span>&gt;</span>
<span>      </span><span>1</span> <span>x</span> <span>=</span> <span>'6'</span>
<span>      </span><span>2</span> <span>try</span><span>:</span>
<span>----&gt; </span><span>3</span>     <span>if</span> <span>x</span> <span>&gt;</span> <span>3</span><span>:</span>
<span>      </span><span>4</span>         <span>print</span><span>(</span><span>'X більше за 3'</span><span>)</span>
<span>      </span><span>5</span> <span>except</span> <span>ValueError</span><span>:</span>

<span>TypeError</span>: '&gt;' not supported between instances of 'str' and 'int'
</pre>



<p>Звісно, інструкція <em>try</em> може мати більше однієї інструкції except для обробки різних винятків, або ви можете не вказувати тип винятку, щоб <em>except</em> перехоплював будь-який виняток.</p>


<pre><span></span><span>x</span> <span>=</span> <span>'s'</span>

<span>try</span><span>:</span>
    <span>if</span> <span>x</span> <span>&gt;</span> <span>3</span><span>:</span>
        <span>print</span><span>(</span><span>x</span><span>)</span>
<span>except</span><span>:</span>
    <span>print</span><span>(</span><span>f</span><span>'Щось не так з x = </span><span>{</span><span>x</span><span>}</span><span>'</span><span>)</span>
</pre>



<pre><span></span>Щось не так з x = s
</pre>



<p><strong>ПРИКЛАД:</strong> Обробка кількох винятків.</p>


<pre><span></span><span>def</span> <span>test_exceptions</span><span>(</span><span>x</span><span>):</span>
    <span>try</span><span>:</span>
        <span>x</span> <span>=</span> <span>int</span><span>(</span><span>x</span><span>)</span>
        <span>if</span> <span>x</span> <span>&gt;</span> <span>3</span><span>:</span>
            <span>print</span><span>(</span><span>x</span><span>)</span>
    <span>except</span> <span>TypeError</span><span>:</span>
        <span>print</span><span>(</span><span>"Ой! x не є допустимим числом. Спробуйте ще раз..."</span><span>)</span>
    <span>except</span> <span>ValueError</span><span>:</span>
        <span>print</span><span>(</span><span>"Ой! Неможливо перетворити x на ціле число. Спробуйте ще раз..."</span><span>)</span>
    <span>except</span><span>:</span>
        <span>print</span><span>(</span><span>"Неочікувана помилка"</span><span>)</span>
</pre>





<pre><span></span><span>x</span> <span>=</span> <span>[</span><span>1</span><span>,</span> <span>2</span><span>]</span>
<span>test_exceptions</span><span>(</span><span>x</span><span>)</span>
</pre>



<pre><span></span>Ой! x не є допустимим числом. Спробуйте ще раз...
</pre>





<pre><span></span><span>x</span> <span>=</span> <span>'s'</span>
<span>test_exceptions</span><span>(</span><span>x</span><span>)</span>
</pre>



<pre><span></span>Ой! Неможливо перетворити x на ціле число. Спробуйте ще раз...
</pre>



<p>Ще одна корисна річ у Python — це можливість генерувати виняток у певних випадках за допомогою <em>raise</em>. Наприклад, якщо нам потрібно, щоб x було менше або дорівнювало 5, ми можемо використати наступний код, щоб згенерувати виняток, якщо x більше 5. Програма відобразить наш виняток і зупинить виконання.</p>


<pre><span></span><span>x</span> <span>=</span> <span>10</span>

<span>if</span> <span>x</span> <span>&gt;</span> <span>5</span><span>:</span>
    <span>raise</span><span>(</span><span>Exception</span><span>(</span><span>'x має бути меншим або дорівнювати 5'</span><span>))</span>
</pre>



<pre><span></span><span>---------------------------------------------------------------------------</span>
<span>Exception</span><span>                                 </span>Traceback (most recent call last)
<span>&lt;</span><span>ipython</span><span>-</span><span>input</span><span>-</span><span>7</span><span>-</span><span>99</span><span>b32b52c4f8</span><span>&gt;</span> <span>in</span> <span>&lt;</span><span>module</span><span>&gt;</span>
<span>      </span><span>2</span> 
<span>      </span><span>3</span> <span>if</span> <span>x</span> <span>&gt;</span> <span>5</span><span>:</span>
<span>----&gt; </span><span>4</span>     <span>raise</span><span>(</span><span>Exception</span><span>(</span><span>'x має бути меншим або дорівнювати 5'</span><span>))</span>

<span>Exception</span>: x має бути меншим або дорівнювати 5
</pre>



<p><strong>УВАГА!</strong> Інструкції Try-except ніколи не слід використовувати замість належної практики програмування. Наприклад, не варто писати код недбало, а потім обгортати вашу програму в інструкцію try-except, доки ви не вжили всіх можливих заходів, щоб переконатися, що ваша функція працює правильно.</p>
