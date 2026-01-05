<h1>Структура даних - Множини<a href="#data-structure-sets" title="Permalink to this headline"></a></h1>
<p>Ще одним типом даних у Python є множини. Це тип, який може зберігати невпорядковану колекцію без дублікатів елементів. Він також підтримує математичні операції, такі як об'єднання, перетин, різниця та симетрична різниця. Множина визначається за допомогою пари фігурних дужок { }, а її елементи розділяються комами.</p>


<pre><span></span><span>{</span><span>3</span><span>,</span> <span>3</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>,</span> <span>1</span><span>,</span> <span>4</span><span>,</span> <span>5</span><span>,</span> <span>6</span><span>,</span> <span>4</span><span>,</span> <span>2</span><span>}</span>
</pre>



<pre><span></span>{1, 2, 3, 4, 5, 6}
</pre>



<p>Один зі швидких способів використання множин — це пошук унікальних елементів у рядку, списку або кортежі.</p>
<p><strong>СПРОБУЙТЕ!</strong> Знайдіть унікальні елементи у списку [1, 2, 2, 3, 2, 1, 2].</p>


<pre><span></span><span>set_1</span> <span>=</span> <span>set</span><span>([</span><span>1</span><span>,</span> <span>2</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>,</span> <span>2</span><span>,</span> <span>1</span><span>,</span> <span>2</span><span>])</span>
<span>set_1</span>
</pre>



<pre><span></span>{1, 2, 3}
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Знайдіть унікальні елементи в кортежі (2, 4, 6, 5, 2).</p>


<pre><span></span><span>set_2</span> <span>=</span> <span>set</span><span>((</span><span>2</span><span>,</span> <span>4</span><span>,</span> <span>6</span><span>,</span> <span>5</span><span>,</span> <span>2</span><span>))</span>
<span>set_2</span>
</pre>



<pre><span></span>{2, 4, 5, 6}
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Знайдіть унікальні символи в рядку "Banana".</p>


<pre><span></span><span>set</span><span>(</span><span>'Banana'</span><span>)</span>
</pre>



<pre><span></span>{'B', 'a', 'n'}
</pre>



<p>Ми згадували, що множини підтримують математичні операції, такі як об'єднання, перетин, різниця та симетрична різниця.</p>
<p><strong>СПРОБУЙТЕ!</strong> Знайдіть об'єднання множин set_1 та set_2.</p>


<pre><span></span><span>print</span><span>(</span><span>set_1</span><span>)</span>
<span>print</span><span>(</span><span>set_2</span><span>)</span>
</pre>



<pre><span></span>{1, 2, 3}
{2, 4, 5, 6}
</pre>





<pre><span></span><span>set_1</span><span>.</span><span>union</span><span>(</span><span>set_2</span><span>)</span>
</pre>



<pre><span></span>{1, 2, 3, 4, 5, 6}
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Знайдіть перетин множин set_1 та set_2.</p>


<pre><span></span><span>set_1</span><span>.</span><span>intersection</span><span>(</span><span>set_2</span><span>)</span>
</pre>



<pre><span></span>{2}
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Чи є set_1 підмножиною {1, 2, 3, 3, 4, 5}?</p>


<pre><span></span><span>set_1</span><span>.</span><span>issubset</span><span>({</span><span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>,</span> <span>3</span><span>,</span> <span>4</span><span>,</span> <span>5</span><span>})</span>
</pre>



<pre><span></span>True
</pre>
