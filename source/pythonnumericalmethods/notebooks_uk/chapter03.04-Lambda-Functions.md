<h1>Лямбда-функції<a href="#lambda-functions" title="Permalink to this headline"></a></h1>
<p>Іноді ми не хочемо використовувати звичайний спосіб визначення функції, особливо якщо наша функція складається лише з одного рядка. У цьому випадку ми можемо використовувати анонімну функцію в Python, яка є функцією, що визначається без імені. Цей тип функцій також називають <strong>лямбда-функцією</strong>, оскільки вони визначаються за допомогою ключового слова <em>lambda</em>. Типова лямбда-функція визначається так:</p>
<pre><span></span><span>lambda</span> <span>аргументи</span><span>:</span> <span>вираз</span>
</pre>

<p>Вона може мати будь-яку кількість аргументів, але лише один вираз.</p>
<p><strong>СПРОБУЙТЕ!</strong> Визначте лямбда-функцію, яка підносить вхідне число до квадрата. І викличте функцію з вхідними даними 2 та 5.</p>


<pre><span></span><span>square</span> <span>=</span> <span>lambda</span> <span>x</span><span>:</span> <span>x</span><span>**</span><span>2</span>

<span>print</span><span>(</span><span>square</span><span>(</span><span>2</span><span>))</span>
<span>print</span><span>(</span><span>square</span><span>(</span><span>5</span><span>))</span>
</pre>



<pre><span></span>4
25
</pre>



<p>У наведеній вище лямбда-функції <em>x</em> є аргументом, а <em>x**2</em> — виразом, який обчислюється та повертається. Сама функція не має імені, і вона повертає об'єкт функції (про що ми поговоримо детальніше в наступних розділах) у змінну <em>square</em>. Після визначення ми можемо викликати її як звичайну функцію. Лямбда-функція еквівалентна:</p>
<pre><span></span><span>def</span> <span>square</span><span>(</span><span>x</span><span>):</span>
    <span>return</span> <span>x</span><span>**</span><span>2</span>
</pre>

<p><strong>СПРОБУЙТЕ!</strong> Визначте лямбда-функцію, яка додає <em>x</em> та <em>y</em>.</p>


<pre><span></span><span>my_adder</span> <span>=</span> <span>lambda</span> <span>x</span><span>,</span> <span>y</span><span>:</span> <span>x</span> <span>+</span> <span>y</span>

<span>print</span><span>(</span><span>my_adder</span><span>(</span><span>2</span><span>,</span> <span>4</span><span>))</span>
</pre>



<pre><span></span>6
</pre>



<p>Лямбда-функції можуть бути корисними в багатьох випадках, ми побачимо більше прикладів їх використання в наступних розділах. Тут ми просто покажемо поширений випадок використання лямбда-функції.</p>
<p><strong>ПРИКЛАД:</strong> Відсортуйте <em>[(1, 2), (2, 0), (4, 1)]</em> на основі другого елемента в кортежі.</p>


<pre><span></span><span>sorted</span><span>([(</span><span>1</span><span>,</span> <span>2</span><span>),</span> <span>(</span><span>2</span><span>,</span> <span>0</span><span>),</span> <span>(</span><span>4</span><span>,</span> <span>1</span><span>)],</span> <span>key</span><span>=</span><span>lambda</span> <span>x</span><span>:</span> <span>x</span><span>[</span><span>1</span><span>])</span>
</pre>



<pre><span></span>[(2, 0), (4, 1), (1, 2)]
</pre>



<p>Що відбувається? Функція <em>sorted</em> має аргумент <em>key</em>, якому можна надати власну функцію-ключ для налаштування порядку сортування. Ми використовуємо лямбда-функцію як скорочений запис для цієї власної функції-ключа.</p>
