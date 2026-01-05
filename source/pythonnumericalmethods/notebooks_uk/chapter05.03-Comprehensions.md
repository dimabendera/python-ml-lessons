<h1>Генератори<a href="#comprehensions" title="Постійне посилання на цей заголовок"></a></h1>
<p>У Python існують інші способи виконання ітерацій, і генератори списків (словників, множин) є важливим і популярним способом, який ви часто використовуватимете у своїй роботі. Генератори дозволяють створювати послідовності з інших послідовностей за допомогою дуже компактного синтаксису. Давайте спочатку розглянемо генератори списків.</p>

<h2>Генератор списків<a href="#list-comprehension" title="Постійне посилання на цей заголовок"></a></h2>
<p><strong>КОНСТРУКЦІЯ:</strong> Генератор списків</p>
<pre><span></span><span>[</span><span>Output</span> <span>Input_sequence</span> <span>Conditions</span><span>]</span>
</pre>

<p><strong>ПРИКЛАД!</strong> Якщо x = range(5), піднесіть кожне число в x до квадрату і збережіть його у списку y.</p>
<p>Якщо ми не використовуємо генератор списків, це виглядатиме приблизно так:</p>


<pre><span></span><span>x</span> <span>=</span> <span>range</span><span>(</span><span>5</span><span>)</span>
<span>y</span> <span>=</span> <span>[]</span>

<span>for</span> <span>i</span> <span>in</span> <span>x</span><span>:</span>
    <span>y</span><span>.</span><span>append</span><span>(</span><span>i</span><span>**</span><span>2</span><span>)</span>
<span>print</span><span>(</span><span>y</span><span>)</span>
</pre>



<pre><span></span>[0, 1, 4, 9, 16]
</pre>



<p>Але за допомогою генератора списків ми можемо написати це лише одним рядком.</p>


<pre><span></span><span>y</span> <span>=</span> <span>[</span><span>i</span><span>**</span><span>2</span> <span>for</span> <span>i</span> <span>in</span> <span>x</span><span>]</span>
<span>print</span><span>(</span><span>y</span><span>)</span>
</pre>



<pre><span></span>[0, 1, 4, 9, 16]
</pre>



<p>Крім того, ми можемо мати умови в генераторі списків. Наприклад, якщо ми хочемо зберегти лише парні числа у наведеному вище прикладі, ми можемо зробити це, додавши умову до генератора списків.</p>


<pre><span></span><span>y</span> <span>=</span> <span>[</span><span>i</span><span>**</span><span>2</span> <span>for</span> <span>i</span> <span>in</span> <span>x</span> <span>if</span> <span>i</span><span>%</span><span>2</span> == 0]
<span>print</span><span>(</span><span>y</span><span>)</span>
</pre>



<pre><span></span>[0, 4, 16]
</pre>



<p>Якщо у нас є два вкладені цикли for, ми також можемо використовувати генератори списків. Наприклад, ми маємо наступні дворівневі цикли for, які ми можемо реалізувати за допомогою генератора списків.</p>


<pre><span></span><span>y</span> <span>=</span> <span>[]</span>
<span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>5</span><span>):</span>
    <span>for</span> <span>j</span> <span>in</span> <span>range</span><span>(</span><span>2</span><span>):</span>
        <span>y</span><span>.</span><span>append</span><span>(</span><span>i</span> <span>+</span> <span>j</span><span>)</span>
<span>print</span><span>(</span><span>y</span><span>)</span>
</pre>



<pre><span></span>[0, 1, 1, 2, 2, 3, 3, 4, 4, 5]
</pre>





<pre><span></span><span>y</span> <span>=</span> <span>[</span><span>i</span> <span>+</span> <span>j</span> <span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>5</span><span>)</span> <span>for</span> <span>j</span> <span>in</span> <span>range</span><span>(</span><span>2</span><span>)]</span>
<span>print</span><span>(</span><span>y</span><span>)</span>
</pre>



<pre><span></span>[0, 1, 1, 2, 2, 3, 3, 4, 4, 5]
</pre>





<h2>Генератор словників<a href="#dictionary-comprehension" title="Постійне посилання на цей заголовок"></a></h2>
<p>Аналогічно, ми можемо використовувати генератори словників. Дивіться наступний приклад.</p>


<pre><span></span><span>x</span> <span>=</span> <span>{</span><span>'a'</span><span>:</span> <span>1</span><span>,</span> <span>'b'</span><span>:</span> <span>2</span><span>,</span> <span>'c'</span><span>:</span> <span>3</span><span>}</span>

<span>{</span><span>key</span><span>:</span><span>v</span><span>**</span><span>3</span> <span>for</span> <span>(</span><span>key</span><span>,</span> <span>v</span><span>)</span> <span>in</span> <span>x</span><span>.</span><span>items</span><span>()}</span>
</pre>



<pre><span></span>{'a': 1, 'b': 8, 'c': 27}
</pre>



<p>Ми можемо використовувати генератори множин у Python, це залишимо вам для самостійного вивчення.</p>
