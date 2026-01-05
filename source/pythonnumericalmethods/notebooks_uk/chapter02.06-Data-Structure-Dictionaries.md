<h1>Структура даних - Словники<a href="#data-structure-dictionaries" title="Permalink to this headline"></a></h1>
<p>У попередніх розділах ми розглянули кілька послідовних типів даних. Зараз ми познайомимо вас з новим і корисним типом — словниками. Це тип-відображення, що робить його абсолютно відмінним від тих, про які ми говорили раніше. Замість використання послідовності чисел для індексації елементів (як у списках або кортежах), словники індексуються за ключами, якими можуть бути рядок, число або навіть кортеж (але не список). Словник — це пари ключ-значення, і кожен ключ відповідає певному значенню. Він визначається за допомогою пари фігурних дужок { }, а елементи є списком пар ключ:значення, розділених комами (зверніть увагу, що пара ключ:значення розділена двокрапкою, з ключем попереду та значенням в кінці).</p>


<pre><span></span><span>dict_1</span> <span>=</span> <span>{</span><span>'apple'</span><span>:</span><span>3</span><span>,</span> <span>'oragne'</span><span>:</span><span>4</span><span>,</span> <span>'pear'</span><span>:</span><span>2</span><span>}</span>
<span>dict_1</span>
</pre>



<pre><span></span>{'apple': 3, 'oragne': 4, 'pear': 2}
</pre>



<p>У словнику елементи зберігаються без певного порядку, тому ви не можете отримати доступ до словника за допомогою послідовності індексних номерів. Щоб отримати доступ до елемента словника, потрібно використовувати його ключ — <code>dictionary[key]</code>.</p>
<p><strong>СПРОБУЙТЕ!</strong> Отримайте елемент ‘apple` зі словника <code>dict_1</code>.</p>


<pre><span></span><span>dict_1</span><span>[</span><span>'apple'</span><span>]</span>
</pre>



<pre><span></span>3
</pre>



<p>Ми можемо отримати всі ключі в словнику за допомогою методу <code>keys</code>, або всі значення за допомогою методу <code>values</code>.</p>
<p><strong>СПРОБУЙТЕ</strong> Отримайте всі ключі та значення зі словника <code>dict_1</code>.</p>


<pre><span></span><span>dict_1</span><span>.</span><span>keys</span><span>()</span>
</pre>



<pre><span></span>dict_keys(['apple', 'oragne', 'pear'])
</pre>





<pre><span></span><span>dict_1</span><span>.</span><span>values</span><span>()</span>
</pre>



<pre><span></span>dict_values([3, 4, 2])
</pre>



<p>Ми також можемо отримати розмір словника за допомогою функції <code>len</code>.</p>


<pre><span></span><span>len</span><span>(</span><span>dict_1</span><span>)</span>
</pre>



<pre><span></span>3
</pre>



<p>Ми можемо визначити порожній словник, а потім додати до нього елементи. Або ми можемо перетворити список кортежів з парами (ключ, значення) на словник.</p>
<p><strong>СПРОБУЙТЕ!</strong> Створіть порожній словник з назвою <code>school_dict</code> та додайте до нього значення "UC Berkeley":"USA".</p>


<pre><span></span><span>school_dict</span> <span>=</span> <span>{}</span>
<span>school_dict</span><span>[</span><span>'UC Berkeley'</span><span>]</span> <span>=</span> <span>'USA'</span>
<span>school_dict</span>
</pre>



<pre><span></span>{'UC Berkeley': 'USA'}
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Додайте ще один елемент "Oxford":"UK" до <code>school_dict</code>.</p>


<pre><span></span><span>school_dict</span><span>[</span><span>'Oxford'</span><span>]</span> <span>=</span> <span>'UK'</span>
<span>school_dict</span>
</pre>



<pre><span></span>{'UC Berkeley': 'USA', 'Oxford': 'UK'}
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Перетворіть список кортежів <code>[("UC Berkeley", "USA"), ('Oxford', 'UK')]</code> на словник.</p>


<pre><span></span><span>dict</span><span>([(</span><span>"UC Berkeley"</span><span>,</span> <span>"USA"</span><span>),</span> <span>(</span><span>'Oxford'</span><span>,</span> <span>'UK'</span><span>)])</span>
</pre>



<pre><span></span>{'UC Berkeley': 'USA', 'Oxford': 'UK'}
</pre>



<p>Ми також можемо перевірити, чи належить ключ словнику, за допомогою оператора <code>in</code>.</p>
<p><strong>СПРОБУЙТЕ!</strong> Визначте, чи є "UC Berkeley" у словнику <code>school_dict</code>.</p>


<pre><span></span><span>"UC Berkeley"</span> <span>in</span> <span>school_dict</span>
</pre>



<pre><span></span>True
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Визначте, чи відсутній "Harvard" у словнику <code>school_dict</code>.</p>


<pre><span></span><span>"Harvard"</span> <span>not</span> <span>in</span> <span>school_dict</span>
</pre>



<pre><span></span>True
</pre>



<p>Ми також можемо використати функцію <code>list</code>, щоб перетворити словник на список його ключів. Наприклад:</p>


<pre><span></span><span>list</span><span>(</span><span>school_dict</span><span>)</span>
</pre>



<pre><span></span>['UC Berkeley', 'Oxford']
</pre>
