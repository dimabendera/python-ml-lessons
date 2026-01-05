<h1>Файли Pickle<a href="#pickle-files" title="Постійне посилання на цей заголовок"></a></h1>
<p>У цьому розділі ми розглянемо ще один спосіб зберігання даних на диск – <strong>pickle</strong>. Ми вже говорили про збереження даних у текстові файли або файли CSV. Але в деяких випадках ми хочемо зберігати словники, кортежі, списки або будь-які інші типи даних на диск і використовувати їх пізніше або надсилати колегам. Саме тут на допомогу приходить pickle: він може серіалізувати об'єкти, щоб їх можна було зберегти у файл і завантажити знову пізніше.</p>
<p>Pickle можна використовувати для серіалізації структур об'єктів Python, що означає процес перетворення об'єкта в пам'яті на потік байтів, який можна зберегти як бінарний файл на диску. Коли ми завантажуємо його назад у програму Python, цей бінарний файл може бути десеріалізований назад в об'єкт Python.</p>

<h2>Запис файлу pickle<a href="#write-a-pickle-file" title="Постійне посилання на цей заголовок"></a></h2>
<p><strong>СПРОБУЙТЕ!</strong> Створіть словник і збережіть його у файл pickle на диску. Щоб використовувати pickle, спочатку потрібно імпортувати модуль.</p>


<pre><span></span><span>import</span> <span>pickle</span>
</pre>





<pre><span></span><span>dict_a</span> <span>=</span> <span>{</span><span>'A'</span><span>:</span><span>0</span><span>,</span> <span>'B'</span><span>:</span><span>1</span><span>,</span> <span>'C'</span><span>:</span><span>2</span><span>}</span>
<span>pickle</span><span>.</span><span>dump</span><span>(</span><span>dict_a</span><span>,</span> <span>open</span><span>(</span><span>'test.pkl'</span><span>,</span> <span>'wb'</span><span>))</span>
</pre>



<p>Щоб використовувати pickle для серіалізації об'єкта, ми використовуємо функцію <em>pickle.dump</em>, яка приймає два аргументи: перший – це об'єкт, а другий – файловий об'єкт, повернений функцією <em>open</em>. Зверніть увагу, що режим функції <em>open</em> тут ‘wb`, що вказує на запис бінарного файлу.</p>


<h2>Читання файлу pickle<a href="#read-a-pickle-file" title="Постійне посилання на цей заголовок"></a></h2>
<p>Тепер завантажимо файл pickle, який ми щойно зберегли на диск, використовуючи функцію <em>pickle.load</em>.</p>


<pre><span></span><span>my_dict</span> <span>=</span> <span>pickle</span><span>.</span><span>load</span><span>(</span><span>open</span><span>(</span><span>'./test.pkl'</span><span>,</span> <span>'rb'</span><span>))</span>
<span>my_dict</span>
</pre>



<pre><span></span>{'A': 0, 'B': 1, 'C': 2}
</pre>



<p>Ми бачимо, що завантаження файлу pickle дуже схоже на процес збереження, але тут режим функції <em>open</em> – ‘rb`, що вказує на читання бінарного файлу. І ця функція десеріалізує бінарний файл назад до оригінального об'єкта, який у нашому випадку є словником.</p>


<h2>Читання файлу pickle з Python 2<a href="#read-in-python-2-pickle-file" title="Постійне посилання на цей заголовок"></a></h2>
<p>Іноді вам може знадобитися відкрити файл pickle від колеги, який створив його за допомогою Python 2 замість Python 3. Ви можете або десеріалізувати його за допомогою Python 2, або використовувати Python 3 з *encoding=`latin1` у функції <em>pickle.load</em>.</p>
<pre><span></span><span>infile</span> <span>=</span> <span>open</span><span>(</span><span>filename</span><span>,</span><span>'rb'</span><span>)</span>
<span>new_dict</span> <span>=</span> <span>pickle</span><span>.</span><span>load</span><span>(</span><span>infile</span><span>,</span> <span>encoding</span><span>=</span><span>'latin1'</span><span>)</span>
</pre>

<p><strong>УВАГА!</strong> Одним з недоліків файлу pickle є те, що це не універсальний формат файлу, тобто його нелегко використовувати іншим мовам програмування. Файли TXT та CSV можна легко передавати колегам, які не використовують Python, і вони можуть відкривати їх за допомогою R, Matlab, Java тощо. Але файл pickle спеціально розроблений для Python, тому дані з нього нелегко використовувати з іншими мовами.</p>
