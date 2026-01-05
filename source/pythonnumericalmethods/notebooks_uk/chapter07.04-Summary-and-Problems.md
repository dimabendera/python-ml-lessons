<h1>Підсумок<a href="#summary" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>ООП та ПОП відрізняються. ООП має багато переваг і часто є більш доцільним для використання у великомасштабних проєктах.</p></li>
<li><p>Клас — це шаблон структури, який дозволяє нам групувати дані та методи, тоді як об'єкт — це екземпляр класу.</p></li>
<li><p>Концепція "успадкування" є ключовою для ООП, що дозволяє нам посилатися на атрибути або методи суперкласу.</p></li>
<li><p>Концепція "ін капсуляції" дозволяє нам приховувати деякі приватні деталі класу від інших об'єктів.</p></li>
<li><p>Концепція "поліморфізму" дозволяє нам використовувати спільну операцію різними способами для різних вхідних даних.</p></li>
</ol>


<h1>Завдання<a href="#problems" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Опишіть відмінності між класами та об'єктами.</p></li>
<li><p>Опишіть, чому ми використовуємо self як перший аргумент у методах.</p></li>
<li><p>Що таке конструктор? І чому ми його використовуємо?</p></li>
<li><p>Опишіть відмінності між атрибутами класу та екземпляра.</p></li>
<li><p>Нижче наведено визначення класу <em>Point</em>, який приймає координати x, y. Додайте метод <em>plot_point</em>, який відображає положення точки.</p>
<pre><span></span><span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>

<span>class</span> <span>Point</span><span>():</span>
   <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>,</span> <span>x</span><span>,</span> <span>y</span><span>):</span>
       <span>self</span><span>.</span><span>x</span> <span>=</span> <span>x</span>
       <span>self</span><span>.</span><span>y</span> <span>=</span> <span>y</span>
</pre>

</li>
<li><p>Використовуючи клас із завдання 5, додайте метод <em>calculate_dist</em>, який приймає x та y іншої точки та повертає обчислену відстань між двома точками.</p></li>
<li><p>Що таке успадкування?</p></li>
<li><p>Як ми успадковуємо від суперкласу та додаємо нові методи?</p></li>
<li><p>Коли ми успадковуємо від суперкласу, нам потрібно замінити метод новим, як це зробити?</p></li>
<li><p>Що таке метод super? Навіщо він потрібен?</p></li>
<li><p>Створіть клас для моделювання об'єкта реального світу та створіть новий клас, який успадковує від нього. Один із прикладів може бути наступним. Ви повинні використовувати інший приклад і застосувати якомога більше вивчених речей.</p></li>
</ol>


<pre><span></span><span>class</span> <span>Car</span><span>():</span>
    <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>,</span> <span>brand</span><span>,</span> <span>color</span><span>):</span>
        <span>self</span><span>.</span><span>brand</span> <span>=</span> <span>brand</span>
        <span>self</span><span>.</span><span>color</span> <span>=</span> <span>color</span>
    
    <span>def</span> <span>start_my_car</span><span>(</span><span>self</span><span>):</span>
        <span>print</span><span>(</span><span>'I am ready to drive!'</span><span>)</span>
        
<span>class</span> <span>Truck</span><span>(</span><span>Car</span><span>):</span>
    <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>,</span> <span>brand</span><span>,</span> <span>color</span><span>,</span> <span>size</span><span>):</span>
        <span>super</span><span>()</span><span>.</span><span>__init__</span><span>(</span><span>brand</span><span>,</span> <span>color</span><span>)</span>
        <span>self</span><span>.</span><span>size</span> <span>=</span> <span>size</span>
        
    <span>def</span> <span>start_my_car</span><span>(</span><span>self</span><span>,</span> <span>key</span><span>):</span>
        <span>if</span> <span>key</span> <span>==</span> <span>'truck_key'</span><span>:</span>
            <span>print</span><span>(</span><span>'I am ready to drive!'</span><span>)</span>
        <span>else</span><span>:</span>
            <span>print</span><span>(</span><span>'Key is not right'</span><span>)</span>
            
    <span>def</span> <span>stop_my_car</span><span>(</span><span>self</span><span>,</span> <span>brake</span><span>):</span>
        <span>if</span> <span>brake</span><span>:</span>
            <span>print</span><span>(</span><span>'The engine is stopped!'</span><span>)</span>
        <span>else</span><span>:</span>
            <span>print</span><span>(</span><span>'I am still running!'</span><span>)</span>
            
<span>truck1</span> <span>=</span> <span>Truck</span><span>(</span><span>'Toyota'</span><span>,</span> <span>'Silver'</span><span>,</span> <span>'Large'</span><span>)</span>
<span>truck1</span><span>.</span><span>start_my_car</span><span>(</span><span>'truck_key'</span><span>)</span>
<span>truck1</span><span>.</span><span>stop_my_car</span><span>(</span><span>brake</span> <span>=</span> <span>False</span><span>)</span>
</pre>



<pre><span></span>I am ready to drive!
I am still running!
</pre>
