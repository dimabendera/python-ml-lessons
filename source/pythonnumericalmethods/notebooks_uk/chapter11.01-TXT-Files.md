<h1>Текстові файли<a href="#txt-files" title="Постійне посилання на цей заголовок"></a></h1>
<p>Досі ми використовували функцію <em>print</em> для відображення даних на екрані. Але існує багато способів зберігати дані на диск і ділитися ними з іншими програмами чи колегами. Наприклад, якщо у мене є деякі рядки в цьому блокноті, але я хочу використовувати їх в іншому блокноті, найпростіший спосіб — зберегти рядки в текстовий файл, а потім відкрити його в іншому блокноті. <strong>Текстовий</strong> файл, часто з розширенням <strong>.txt</strong>, — це файл, що містить лише звичайний текст. Однак програми, які ви пишете, і програми, які читають ваш текстовий файл, зазвичай очікують, що текстовий файл буде у певному форматі; тобто організований певним чином.</p>
<p>Для роботи з текстовими файлами нам потрібно використовувати функцію <em>open</em>, яка повертає <em>об'єкт файлу</em>. Вона зазвичай використовується з двома аргументами:</p>
<pre><span></span><span>f</span> <span>=</span> <span>open</span><span>(</span><span>filename</span><span>,</span> <span>mode</span><span>)</span>
</pre>

<p><em>f</em> — це повернутий об'єкт файлу. Ім'я файлу — це рядок, що вказує розташування файлу, який ви хочете відкрити, а <em>режим</em> — це інший рядок, що містить кілька символів, які описують спосіб використання файлу; поширені режими:</p>
<ul>
<li><p>‘r`, це режим за замовчуванням, який відкриває файл для читання</p></li>
<li><p>‘w`, цей режим відкриває файл для запису; якщо файл не існує, він створює новий файл.</p></li>
<li><p>‘a`, відкриває файл у режимі дозапису, додає дані в кінець файлу. Якщо файл не існує, він створює новий файл.</p></li>
<li><p>‘b`, відкриває файл у бінарному режимі.</p></li>
<li><p>‘r+`, відкриває файл (не створює) для читання та запису.</p></li>
<li><p>‘w+`, відкриває або створює файл для запису та читання, відкидає існуючий вміст.</p></li>
<li><p>‘a+`, відкриває або створює файл для читання та запису, і додає дані в кінець файлу.</p></li>
</ul>

<h2>Запис у файл<a href="#write-a-file" title="Постійне посилання на цей заголовок"></a></h2>
<p><strong>СПРОБУЙТЕ!</strong> Створіть текстовий файл під назвою <em>test.txt</em> і запишіть у нього кілька рядків.</p>


<pre><span></span><span>f</span> <span>=</span> <span>open</span><span>(</span><span>'test.txt'</span><span>,</span> <span>'w'</span><span>)</span>
<span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>5</span><span>):</span>
    <span>f</span><span>.</span><span>write</span><span>(</span><span>f</span><span>"This is line </span><span>{</span><span>i</span><span>}</span><span>\n</span><span>"</span><span>)</span>
    
<span>f</span><span>.</span><span>close</span><span>()</span>
</pre>



<p>Ми бачимо з коду вище, що ми спочатку відкрили об'єкт файлу <em>f</em> з ім'ям файлу ‘test.txt`. Ми використали "w+" для режиму, що вказує на запис. Потім ми записуємо 5 рядків (зверніть увагу на символ нового рядка ‘\n` в кінці рядка), а потім закриваємо об'єкт файлу. Вміст файлу можна побачити на наступному малюнку.</p>
<p><img alt="Запис_тексту" src="../_images/11.01.01-Write_text_file.png"/></p>
<p><strong>ПРИМІТКА!</strong> Рекомендується закривати файл за допомогою <code><span>f.close()</span></code> в кінці. Якщо ви не закриєте їх самостійно, Python зрештою закриє їх за вас. Але іноді, при записі у файл, дані можуть не бути записані на диск, доки ви не закриєте файл. Тому, чим довше ви тримаєте файл відкритим, тим більші шанси втратити ваші дані.</p>


<h2>Дозапис у файл<a href="#append-to-a-file" title="Постійне посилання на цей заголовок"></a></h2>
<p>Тепер давайте додамо деякий рядок до файлу <em>test.txt</em>. Це дуже схоже на те, як ми записуємо файл, з однією лише відмінністю — змініть режим на ‘a`.</p>


<pre><span></span><span>f</span> <span>=</span> <span>open</span><span>(</span><span>'test.txt'</span><span>,</span> <span>'a'</span><span>)</span>
<span>f</span><span>.</span><span>write</span><span>(</span><span>f</span><span>"This is another line</span><span>\n</span><span>"</span><span>)</span>
<span>f</span><span>.</span><span>close</span><span>()</span>
</pre>



<p><img alt="Дозапис_тексту" src="../_images/11.01.02-Append_text_file.png"/></p>


<h2>Читання файлу<a href="#read-a-file" title="Постійне посилання на цей заголовок"></a></h2>
<p>Ми можемо прочитати файл з диска і зберегти весь вміст у змінну. Давайте прочитаємо файл <em>test.txt</em>, який ми створили вище, і збережемо весь вміст файлу у змінну <em>content</em>.</p>


<pre><span></span><span>f</span> <span>=</span> <span>open</span><span>(</span><span>'./test.txt'</span><span>,</span> <span>'r'</span><span>)</span>
<span>content</span> <span>=</span> <span>f</span><span>.</span><span>read</span><span>()</span>
<span>f</span><span>.</span><span>close</span><span>()</span>
<span>print</span><span>(</span><span>content</span><span>)</span>
</pre>



<pre><span></span>This is line 0
This is line 1
This is line 2
This is line 3
This is line 4
This is another line
</pre>



<p>Таким чином ми можемо зберегти всі рядки файлу в одну рядкову змінну, ми можемо перевірити, що змінна <em>content</em> є рядком.</p>


<pre><span></span><span>type</span><span>(</span><span>content</span><span>)</span>
</pre>



<pre><span></span>str
</pre>



<p>Але іноді ми хочемо читати вміст файлів рядок за рядком і зберігати його у список. Для цього ми можемо використовувати <em>f.readlines()</em>.</p>


<pre><span></span><span>f</span> <span>=</span> <span>open</span><span>(</span><span>'./test.txt'</span><span>,</span> <span>'r'</span><span>)</span>
<span>contents</span> <span>=</span> <span>f</span><span>.</span><span>readlines</span><span>()</span>
<span>f</span><span>.</span><span>close</span><span>()</span>
<span>print</span><span>(</span><span>contents</span><span>)</span>
</pre>



<pre><span></span>['This is line 0\n', 'This is line 1\n', 'This is line 2\n', 'This is line 3\n', 'This is line 4\n', 'This is another line\n']
</pre>





<pre><span></span><span>type</span><span>(</span><span>contents</span><span>)</span>
</pre>



<pre><span></span>list
</pre>





<h2>Робота з числами та масивами<a href="#dealing-with-numbers-and-arrays" title="Постійне посилання на цей заголовок"></a></h2>
<p>Оскільки пізніше ми будемо працювати з чисельними методами, і багато разів ми працюємо з числами або масивами. Ми могли б використовувати вищезгадані методи для збереження чисел або масивів у файл і зчитування їх назад у пам'ять. Але це не так зручно. Натомість, зазвичай ми використовуємо пакет <em>numpy</em> для прямого збереження/зчитування масиву. Давайте розглянемо приклад.</p>
<p><strong>СПРОБУЙТЕ!</strong> Збережіть масив [[1.20, 2.20, 3.00], [4.14, 5.65, 6.42]] у файл з назвою <em>my_array.txt</em> і прочитайте його назад у змінну під назвою <em>my_arr</em>.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
</pre>





<pre><span></span><span>arr</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>1.20</span><span>,</span> <span>2.20</span><span>,</span> <span>3.00</span><span>],</span> <span>[</span><span>4.14</span><span>,</span> <span>5.65</span><span>,</span> <span>6.42</span><span>]])</span>
<span>arr</span>
</pre>



<pre><span></span>array([[1.2 , 2.2 , 3.  ],
       [4.14, 5.65, 6.42]])
</pre>





<pre><span></span><span>np</span><span>.</span><span>savetxt</span><span>(</span><span>'my_arr.txt'</span><span>,</span> <span>arr</span><span>,</span> <span>fmt</span><span>=</span><span>'</span><span>%.2f</span><span>'</span><span>,</span> <span>header</span> <span>=</span> <span>'Col1 Col2 Col3'</span><span>)</span>
</pre>



<p>З наведеного вище прикладу ми бачимо, як зберегти 2D-масив у текстовий файл за допомогою <em>np.savetxt</em>. Перший аргумент — це ім'я файлу, другий аргумент — це об'єкт масиву, який ми хочемо зберегти, а третій аргумент — це визначення формату для виводу (я використовую ‘%.2f`, щоб вказати, що ми хочемо виводити числа з 2 десятковими знаками). Четвертий аргумент — це заголовок, який ми хочемо записати у файл.</p>
<p><img alt="Запис_масиву" src="../_images/11.01.03-Write_array.png"/></p>


<pre><span></span><span>my_arr</span> <span>=</span> <span>np</span><span>.</span><span>loadtxt</span><span>(</span><span>'my_arr.txt'</span><span>)</span>
<span>my_arr</span>
</pre>



<pre><span></span>array([[1.2 , 2.2 , 3.  ],
       [4.14, 5.65, 6.42]])
</pre>



<p>Ми бачимо, що зчитування файлу безпосередньо в масив дуже просте за допомогою функції <em>np.loadtxt</em>. І вона також пропускає перший заголовок. Існує багато різних аргументів, які можуть контролювати читання; ми не будемо вдаватися в надто багато деталей тут, ви можете перевірити документацію або використати знак питання, щоб отримати довідку. Ми також будемо використовувати її більше в наступному розділі.</p>
