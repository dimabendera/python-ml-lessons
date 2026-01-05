```html
<h1>Тернарні оператори<a href="#ternary-operators" title="Постійне посилання на цей заголовок"></a></h1>
<p>Більшість мов програмування мають <strong>тернарні оператори</strong>, які зазвичай відомі як <strong>умовні вирази</strong>. Вони надають спосіб, за допомогою якого ми можемо в одному рядку коду обчислити перший вираз, якщо умова істинна, або другий вираз, якщо вона хибна. Python має свій спосіб реалізації тернарного оператора, який можна сконструювати наступним чином:</p>
<p><strong>КОНСТРУКЦІЯ</strong>: тернарний оператор у Python</p>
<pre><span></span>вираз_якщо_істина if умова else вираз_якщо_хибність
</pre>

<p><strong>ПРИКЛАД:</strong> Тернарний оператор</p>


<pre><span></span><span>is_student</span> <span>=</span> <span>True</span>
<span>person</span> <span>=</span> <span>'student'</span> <span>if</span> <span>is_student</span> <span>else</span> <span>'not student'</span>
<span>print</span><span>(</span><span>person</span><span>)</span>
</pre>



<pre><span></span>student
</pre>



<p>З наведеного вище прикладу ми бачимо, що цей однорядковий код еквівалентний наступному блоку коду.</p>


<pre><span></span><span>is_student</span> <span>=</span> <span>True</span>
<span>if</span> <span>is_student</span><span>:</span>
    <span>person</span> <span>=</span> <span>'student'</span>
<span>else</span><span>:</span>
    <span>person</span> <span>=</span> <span>'not student'</span>
<span>print</span><span>(</span><span>person</span><span>)</span>
</pre>



<pre><span></span>student
</pre>



<p>Тернарний оператор надає простий спосіб для розгалуження і може зробити наш код більш лаконічним. Крім того, в наступному розділі ви побачите, що він часто використовується у спискових включеннях (list comprehensions), що є дуже корисним.</p>
```
