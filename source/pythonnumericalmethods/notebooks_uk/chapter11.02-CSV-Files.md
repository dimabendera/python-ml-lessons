<h1>CSV файли<a href="#csv-files" title="Постійне посилання на цей заголовок"></a></h1>
<p>Багато наукових даних зберігаються у форматі файлів <strong>значень, розділених комами</strong> (CSV), текстовому файлі з роздільниками, який використовує кому для розділення значень. Це дуже корисний формат, який може зберігати великі таблиці даних (чисел і тексту) у простому тексті. Кожен рядок у даних є одним записом даних, і кожен запис складається з одного або кількох полів, розділених комами. Його також можна відкрити за допомогою Microsoft Excel та візуалізувати рядки та стовпці.</p>
<p>Python має власний модуль csv, який може обробляти читання та запис файлів csv, деталі можна знайти в <a href="https://docs.python.org/3/library/csv.html">документації</a>. Але ми не будемо представляти цей модуль csv тут. Натомість ми будемо використовувати пакет numpy для роботи з файлами csv, оскільки часто ми будемо читати файли csv безпосередньо в масив numpy.</p>

<h2>Запис та відкриття CSV файлу<a href="#write-and-open-a-csv-file" title="Постійне посилання на цей заголовок"></a></h2>
<p>Розглянемо простий приклад генерації 100 рядків і 5 стовпців даних.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
</pre>





<pre><span></span><span>data</span> <span>=</span> <span>np</span><span>.</span><span>random</span><span>.</span><span>random</span><span>((</span><span>100</span><span>,</span><span>5</span><span>))</span>
</pre>





<pre><span></span><span>np</span><span>.</span><span>savetxt</span><span>(</span><span>'test.csv'</span><span>,</span> <span>data</span><span>,</span> <span>fmt</span> <span>=</span> <span>'</span><span>%.2f</span><span>'</span><span>,</span> <span>delimiter</span><span>=</span><span>','</span><span>,</span> <span>header</span> <span>=</span> <span>'c1, c2, c3, c4, c5'</span><span>)</span>
</pre>



<p>Спочатку ми генеруємо випадкові дані для 100 рядків і 5 стовпців за допомогою функції <em>np.random</em> і присвоюємо їх змінній <em>data</em>. Ми використовуємо функцію <em>np.savetxt</em> для збереження даних у файл csv. Ми бачимо, що перші 3 аргументи такі ж, як і ті, що використовувалися в попередньому розділі, але тут ми встановлюємо аргумент `delimiter` на `,`, що вказує на те, що ми хочемо розділити дані за допомогою коми.</p>
<p>Ми можемо відкрити файл csv за допомогою Microsoft Excel.</p>
<p><img alt="Відкрити_csv" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/11.02.01-Write_csv.png"/></p>
<p>Ми також можемо відкрити файл csv за допомогою текстового редактора, де ми побачимо, що значення розділені комами.</p>
<p><img alt="Відкрити_csv_текст" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/11.02.02-Open_csv_text.png"/></p>


<h2>Читання CSV файлу<a href="#read-a-csv-file" title="Постійне посилання на цей заголовок"></a></h2>
<p>Як і раніше, ми можемо прочитати файл csv за допомогою функції <em>np.loadtxt</em>. Давайте прочитаємо файл csv, який ми щойно зберегли на диск, у змінну <em>my_csv</em> і виведемо перші 5 рядків. Зауважте, що тут ми знову використовуємо <em>delimiter</em>, щоб вказати, що дані у файлі розділені комами.</p>


<pre><span></span><span>my_csv</span> <span>=</span> <span>np</span><span>.</span><span>loadtxt</span><span>(</span><span>'./test.csv'</span><span>,</span> <span>delimiter</span><span>=</span><span>','</span><span>)</span>
<span>my_csv</span><span>[:</span><span>5</span><span>,</span> <span>:]</span>
</pre>



<pre><span></span>array([[0.84, 0.99, 0.56, 0.24, 0.71],
       [0.33, 0.8 , 0.32, 0.28, 0.83],
       [0.89, 0.19, 0.25, 0.63, 0.84],
       [0.08, 0.49, 0.76, 0.34, 0.69],
       [0.66, 0.65, 0.73, 0.48, 0.12]])
</pre>





<h2>За межами Numpy<a href="#beyond-numpy" title="Постійне посилання на цей заголовок"></a></h2>
<p>Numpy дуже зручний для роботи з файлами csv, але безумовно існує більше пакетів, які можуть обробляти файли csv. Дуже популярним є пакет <em>Pandas</em>, який може легко працювати з табличними даними у Dataframe; ви можете ознайомитися з ним, якщо зацікавлені дізнатися більше.</p>
