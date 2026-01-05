<h1>Структура даних - Кортежі<a href="#data-structure-tuples" title="Постійне посилання на цей заголовок"></a></h1>
<p>Давайте вивчимо ще одну відмінну послідовну структуру даних у Python - Кортежі. Зазвичай вони визначаються за допомогою пари дужок ( ), а їхні елементи розділяються комами. Наприклад:</p>


<pre><span></span><span>tuple_1</span> <span>=</span> <span>(</span><span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>,</span> <span>2</span><span>)</span>
<span>tuple_1</span>
</pre>



<pre><span></span>(1, 2, 3, 2)
</pre>



<p>Як і рядки та списки, спосіб індексування кортежів, нарізка елементів і навіть деякі методи дуже схожі.</p>
<p><strong>СПРОБУЙТЕ!</strong> Отримайте довжину tuple_1.</p>


<pre><span></span><span>len</span><span>(</span><span>tuple_1</span><span>)</span>
</pre>



<pre><span></span>4
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Отримайте елементи з індексу 1 до 3 для tuple_1.</p>


<pre><span></span><span>tuple_1</span><span>[</span><span>1</span><span>:</span><span>4</span><span>]</span>
</pre>



<pre><span></span>(2, 3, 2)
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Підрахуйте кількість входжень числа 2 у tuple_1.</p>


<pre><span></span><span>tuple_1</span><span>.</span><span>count</span><span>(</span><span>2</span><span>)</span>
</pre>



<pre><span></span>2
</pre>



<p>Ви можете запитати, яка різниця між списками та кортежами? Якщо вони схожі один на одного, навіщо нам ще одна послідовна структура даних?</p>
<p>Що ж, кортежі створені не просто так. З <a href="https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences">документації Python</a>:</p>
<blockquote>
<p>Хоча кортежі можуть здаватися схожими на списки, вони часто використовуються в різних ситуаціях і для різних цілей. Кортежі є <strong>незмінними</strong>, і зазвичай містять <strong>гетерогенну</strong> послідовність елементів, до яких звертаються за допомогою розпакування (див. далі в цьому розділі) або індексування (або навіть за атрибутом у випадку іменованих кортежів). Списки є <strong>змінними</strong>, а їхні елементи зазвичай <strong>гомогенними</strong> і доступ до них здійснюється шляхом ітерування по списку.</p>
</blockquote>
<p>Що означає незмінний? Це означає, що елементи в кортежі, після визначення, не можуть бути змінені. Але елементи в списку можуть бути змінені без будь-яких проблем. Наприклад:</p>


<pre><span></span><span>list_1</span> <span>=</span> <span>[</span><span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>]</span>
<span>list_1</span><span>[</span><span>2</span><span>]</span> <span>=</span> <span>1</span>
<span>list_1</span>
</pre>



<pre><span></span>[1, 2, 1]
</pre>





<pre><span></span><span>tuple_1</span><span>[</span><span>2</span><span>]</span> <span>=</span> <span>1</span>
</pre>



<pre><span></span><span>---------------------------------------------------------------------------</span>
<span>TypeError</span><span>                                 </span>Traceback (most recent call last)
<span>&lt;ipython-input-6-76fb6b169c14&gt;</span> in <span>&lt;module&gt;</span><span>()</span>
<span>----&gt; </span><span>1</span> <span>tuple_1</span><span>[</span><span>2</span><span>]</span> <span>=</span> <span>1</span>

<span>TypeError</span>: 'tuple' object does not support item assignment
</pre>



<p>Що означає гетерогенний? Кортежі зазвичай містять гетерогенну послідовність елементів, тоді як списки зазвичай містять гомогенну послідовність. Розглянемо приклад, коли у нас є список, що містить різні фрукти. Зазвичай назви фруктів можуть зберігатися у списку, оскільки вони гомогенні. Тепер ми хочемо мати структуру даних для зберігання кількості фруктів кожного типу, і саме тут на допомогу приходять кортежі, оскільки назва фрукта та число є гетерогенними. Наприклад, ('apple', 3) означає, що у нас є 3 яблука.</p>


<pre><span></span><span># список фруктів</span>
<span>[</span><span>'apple'</span><span>,</span> <span>'banana'</span><span>,</span> <span>'orange'</span><span>,</span> <span>'pear'</span><span>]</span>
</pre>



<pre><span></span>['apple', 'banana', 'orange', 'pear']
</pre>





<pre><span></span><span># список пар (фрукт, кількість)</span>
<span>[(</span><span>'apple'</span><span>,</span> <span>3</span><span>),</span> <span>(</span><span>'banana'</span><span>,</span> <span>4</span><span>)</span> <span>,</span> <span>(</span><span>'orange'</span><span>,</span> <span>1</span><span>),</span> <span>(</span><span>'pear'</span><span>,</span> <span>4</span><span>)]</span>
</pre>



<pre><span></span>[('apple', 3), ('banana', 4), ('orange', 1), ('pear', 4)]
</pre>



<p>До кортежів можна отримати доступ за допомогою розпакування; це вимагає, щоб кількість змінних з лівого боку знака рівності дорівнювала кількості елементів у послідовності.</p>


<pre><span></span><span>a</span><span>,</span> <span>b</span><span>,</span> <span>c</span> <span>=</span> <span>list_1</span>
<span>print</span><span>(</span><span>a</span><span>,</span> <span>b</span><span>,</span> <span>c</span><span>)</span>
</pre>



<pre><span></span>1 2 1
</pre>



<p><strong>ПРИМІТКА!</strong> Протилежною операцією до розпакування є пакування, як показано в наступному прикладі. Ми бачимо, що нам не потрібні дужки для визначення кортежу, але завжди краще їх використовувати.</p>


<pre><span></span><span>list_2</span> <span>=</span> <span>2</span><span>,</span> <span>4</span><span>,</span> <span>5</span>
<span>list_2</span>
</pre>



<pre><span></span>(2, 4, 5)
</pre>
