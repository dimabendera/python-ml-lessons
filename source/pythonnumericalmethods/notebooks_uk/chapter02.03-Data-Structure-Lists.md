<h1>Структура даних - Списки<a href="#data-structure-lists" title="Постійне посилання на цей заголовок"></a></h1>
<p>У попередньому розділі ми розглянули рядки, які можуть містити послідовність символів. Тепер давайте розглянемо більш універсальну послідовну структуру даних у Python - списки. Спосіб їх визначення полягає у використанні пари квадратних дужок [ ], а елементи всередині них розділяються комами. Список може містити будь-який тип даних: числові, рядкові або інші типи. Наприклад:</p>


<pre><span></span><span>list_1</span> <span>=</span> <span>[</span><span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>]</span>
<span>list_1</span>
</pre>



<pre><span></span>[1, 2, 3]
</pre>





<pre><span></span><span>list_2</span> <span>=</span> <span>[</span><span>'Hello'</span><span>,</span> <span>'World'</span><span>]</span>
<span>list_2</span>
</pre>



<pre><span></span>['Hello', 'World']
</pre>



<p>Ми також можемо розміщувати в списку змішані типи даних</p>


<pre><span></span><span>list_3</span> <span>=</span> <span>[</span><span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>,</span> <span>'Apple'</span><span>,</span> <span>'orange'</span><span>]</span>
<span>list_3</span>
</pre>



<pre><span></span>[1, 2, 3, 'Apple', 'orange']
</pre>



<p>Ми також можемо вкладати списки один в одного, наприклад:</p>


<pre><span></span><span>list_4</span> <span>=</span> <span>[</span><span>list_1</span><span>,</span> <span>list_2</span><span>]</span>
<span>list_4</span>
</pre>



<pre><span></span>[[1, 2, 3], ['Hello', 'World']]
</pre>



<p>Спосіб отримання елемента зі списку дуже схожий на роботу з рядками, дивіться індексацію на наступному малюнку</p>
<p><img alt="Індексація_списку" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/02.03.01-list_index.png"/></p>
<p><strong>СПРОБУЙТЕ!</strong> Отримайте 3-й елемент зі списку list_3</p>


<pre><span></span><span>list_3</span><span>[</span><span>2</span><span>]</span>
</pre>



<pre><span></span>3
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Отримайте перші 3 елементи зі списку list_3</p>


<pre><span></span><span>list_3</span><span>[:</span><span>3</span><span>]</span>
</pre>



<pre><span></span>[1, 2, 3]
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Отримайте останній елемент зі списку list_3</p>


<pre><span></span><span>list_3</span><span>[</span><span>-</span><span>1</span><span>]</span>
</pre>



<pre><span></span>'orange'
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Отримайте перший список зі списку list_4.</p>


<pre><span></span><span>list_4</span><span>[</span><span>0</span><span>]</span>
</pre>



<pre><span></span>[1, 2, 3]
</pre>



<p>Аналогічно, ми можемо отримати довжину списку за допомогою функції <em>len</em>.</p>


<pre><span></span><span>len</span><span>(</span><span>list_3</span><span>)</span>
</pre>



<pre><span></span>5
</pre>



<p>Ми також можемо об'єднувати (конкатенувати) два списки, просто використовуючи знак <em>+</em>.</p>
<p><strong>СПРОБУЙТЕ!</strong> Додайте list_1 та list_2 в один список.</p>


<pre><span></span><span>list_1</span> <span>+</span> <span>list_2</span>
</pre>



<pre><span></span>[1, 2, 3, 'Hello', 'World']
</pre>



<p>Нові елементи можна додавати до існуючого списку за допомогою методу <em>append</em>.</p>


<pre><span></span><span>list_1</span><span>.</span><span>append</span><span>(</span><span>4</span><span>)</span>
<span>list_1</span>
</pre>



<pre><span></span>[1, 2, 3, 4]
</pre>



<p><strong>Примітка!</strong> Функція <em>append</em> працює безпосередньо зі списком, як показано у прикладі вище, де число 4 додається до списку. Але в прикладі `list_1 + list_2`, списки `list_1` та `list_2` не зміняться. Ви можете перевірити `list_2`, щоб переконатися в цьому.</p>
<p>Ми також можемо вставляти або видаляти елементи зі списку за допомогою методів <em>insert</em> та <em>remove</em>, але вони також працюють безпосередньо зі списком.</p>


<pre><span></span><span>list_1</span><span>.</span><span>insert</span><span>(</span><span>2</span><span>,</span><span>'center'</span><span>)</span>
<span>list_1</span>
</pre>



<pre><span></span>[1, 2, 'center', 3, 4]
</pre>



<p><strong>Примітка!</strong> Використання методу <em>remove</em> видалить лише перше входження елемента (прочитайте документацію методу). Існує інший спосіб видалити елемент за його індексом - функція <em>del</em>.</p>


<pre><span></span><span>del</span> <span>list_1</span><span>[</span><span>2</span><span>]</span>
<span>list_1</span>
</pre>



<pre><span></span>[1, 2, 3, 4]
</pre>



<p>Ми також можемо визначити порожній список і додавати до нього нові елементи пізніше за допомогою методу <em>append</em>. Це часто використовується в Python, коли потрібно перебирати послідовність елементів; ми дізнаємося про це більше в розділі про ітерації.</p>
<p><strong>СПРОБУЙТЕ!</strong> Створіть порожній список і додайте до нього значення 5 та 6.</p>


<pre><span></span><span>list_5</span> <span>=</span> <span>[]</span>
<span>list_5</span><span>.</span><span>append</span><span>(</span><span>5</span><span>)</span>
<span>list_5</span>
</pre>



<pre><span></span>[5]
</pre>





<pre><span></span><span>list_5</span><span>.</span><span>append</span><span>(</span><span>6</span><span>)</span>
<span>list_5</span>
</pre>



<pre><span></span>[5, 6]
</pre>



<p>Ми також можемо швидко перевірити, чи є елемент у списку, за допомогою оператора <em>in</em>.</p>
<p><strong>СПРОБУЙТЕ!</strong> Перевірте, чи є число 5 у списку <em>list_5</em>.</p>


<pre><span></span><span>5</span> <span>in</span> <span>list_5</span>
</pre>



<pre><span></span>True
</pre>



<p>Використовуючи функцію <em>list</em>, ми можемо перетворити інші послідовності на список.</p>
<p><strong>СПРОБУЙТЕ!</strong> Перетворіть рядок ‘Hello World` на список символів.</p>


<pre><span></span><span>list</span><span>(</span><span>'Hello World'</span><span>)</span>
</pre>



<pre><span></span>['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
</pre>



<p>Списки дуже часто використовуються в Python при роботі з даними, вони мають багато різних варіантів застосування, які ви побачите в наступних розділах.</p>
