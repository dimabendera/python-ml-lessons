<h1>Файли HDF5<a href="#hdf5-files" title="Постійне посилання на цей заголовок"></a></h1>
<p>У наукових обчисленнях іноді нам потрібно зберігати великі обсяги даних зі швидким доступом, і формати файлів, які ми представляли раніше, не підходять для цього. Ви незабаром виявите, що в багатьох випадках HDF5 (Hierarchical Data Format – Ієрархічний Формат Даних) є рішенням. Це потужний бінарний формат даних без обмежень на розмір файлу. Він забезпечує паралельний ввід/вивід (input/output) і виконує безліч низькорівневих оптимізацій, щоб прискорити запити та зменшити вимоги до зберігання.</p>
<p>Файл HDF5 зберігає два типи об'єктів: <em>набори даних</em> (datasets), які є масивоподібними колекціями даних (як масиви NumPy), та <em>групи</em> (groups), які є контейнерами, схожими на папки, що містять набори даних та інші групи. Існують також атрибути, які можуть бути пов'язані з наборами даних та групами для опису деяких властивостей. Так звана <em>ієрархічна</em> структура в HDF5 означає, що дані можуть бути збережені як файлова система, з папкоподібними структурами, такими як папка, підпапка (в HDF5 це називається група, підгрупа). Групи працюють як словники з <em>ключами</em> та <em>значеннями</em>, де <em>ключі</em> – це назви груп, а <em>значення</em> – це підгрупи або набори даних.</p>
<p>Щоб використовувати HDF5 для читання/запису в Python, існують деякі пакети або обгортки для цих цілей. Два найпоширеніші пакети – це <a href="https://www.pytables.org/">PyTables</a> та <a href="https://www.h5py.org/">h5py</a>. Тут ми розглянемо лише h5py. Ви можете встановити h5py за допомогою conda (сподіваємося, ви ще пам'ятаєте, як це робити; якщо забули, будь ласка, поверніться до Розділу 1).</p>
<p>Після встановлення h5py ви можете скористатися посібником зі швидкого старту в <a href="http://docs.h5py.org/en/latest/quick.html">документації h5py</a>, щоб швидко розпочати роботу. Але тут ми використаємо один приклад, щоб показати, як створювати та читати файл HDF5. Спочатку імпортуємо NumPy та h5py.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
<span>import</span> <span>h5py</span>
</pre>



<p><strong>Приклад:</strong> Припустимо, ми розгорнули кілька інструментів для моніторингу прискорень та GPS-місцезнаходження в районі затоки, Каліфорнія. Ми встановили два акселерометри в Берклі та Окленді, а також одну GPS-станцію в Сан-Франциско. Вони записують дані з різними частотами дискретизації: акселерометр у Берклі відбирає дані кожні 0.04 с, а датчик в Окленді – кожні 0.01 с. GPS відбирає місцезнаходження кожні 60 секунд у Сан-Франциско. Тепер ми хочемо зберегти ці два типи даних у HDF5, а також деякі атрибути, що вказують місце запису даних, час початку запису, назву станції та інтервал дискретизації.</p>


<pre><span></span><span># Generate random data for recording</span>
<span>acc_1</span> <span>=</span> <span>np</span><span>.</span><span>random</span><span>.</span><span>random</span><span>(</span><span>1000</span><span>)</span>
<span>station_number_1</span> <span>=</span> <span>'1'</span>
<span># unix timestamp</span>
<span>start_time_1</span> <span>=</span> <span>1542000276</span>
<span># time interval for recording</span>
<span>dt_1</span> <span>=</span> <span>0.04</span>
<span>location_1</span> <span>=</span> <span>'Berkeley'</span>

<span>acc_2</span> <span>=</span> <span>np</span><span>.</span><span>random</span><span>.</span><span>random</span><span>(</span><span>500</span><span>)</span>
<span>station_number_2</span> <span>=</span> <span>'2'</span>
<span>start_time_2</span> <span>=</span> <span>1542000576</span>
<span>dt_2</span> <span>=</span> <span>0.01</span>
<span>location_2</span> <span>=</span> <span>'Oakland'</span>
</pre>





<pre><span></span><span>hf</span> <span>=</span> <span>h5py</span><span>.</span><span>File</span><span>(</span><span>'station.hdf5'</span><span>,</span> <span>'w'</span><span>)</span>
</pre>





<pre><span></span><span>hf</span><span>[</span><span>'/acc/1/data'</span><span>]</span> <span>=</span> <span>acc_1</span>
<span>hf</span><span>[</span><span>'/acc/1/data'</span><span>]</span><span>.</span><span>attrs</span><span>[</span><span>'dt'</span><span>]</span> <span>=</span> <span>dt_1</span>
<span>hf</span><span>[</span><span>'/acc/1/data'</span><span>]</span><span>.</span><span>attrs</span><span>[</span><span>'start_time'</span><span>]</span> <span>=</span> <span>start_time_1</span>
<span>hf</span><span>[</span><span>'/acc/1/data'</span><span>]</span><span>.</span><span>attrs</span><span>[</span><span>'location'</span><span>]</span> <span>=</span> <span>location_1</span>

<span>hf</span><span>[</span><span>'/acc/2/data'</span><span>]</span> <span>=</span> <span>acc_2</span>
<span>hf</span><span>[</span><span>'/acc/2/data'</span><span>]</span><span>.</span><span>attrs</span><span>[</span><span>'dt'</span><span>]</span> <span>=</span> <span>dt_2</span>
<span>hf</span><span>[</span><span>'/acc/2/data'</span><span>]</span><span>.</span><span>attrs</span><span>[</span><span>'start_time'</span><span>]</span> <span>=</span> <span>start_time_2</span>
<span>hf</span><span>[</span><span>'/acc/2/data'</span><span>]</span><span>.</span><span>attrs</span><span>[</span><span>'location'</span><span>]</span> <span>=</span> <span>location_2</span>

<span>hf</span><span>[</span><span>'/gps/1/data'</span><span>]</span> <span>=</span> <span>np</span><span>.</span><span>random</span><span>.</span><span>random</span><span>(</span><span>100</span><span>)</span>
<span>hf</span><span>[</span><span>'/gps/1/data'</span><span>]</span><span>.</span><span>attrs</span><span>[</span><span>'dt'</span><span>]</span> <span>=</span> <span>60</span>
<span>hf</span><span>[</span><span>'/gps/1/data'</span><span>]</span><span>.</span><span>attrs</span><span>[</span><span>'start_time'</span><span>]</span> <span>=</span> <span>1542000000</span>
<span>hf</span><span>[</span><span>'/gps/1/data'</span><span>]</span><span>.</span><span>attrs</span><span>[</span><span>'location'</span><span>]</span> <span>=</span> <span>'San Francisco'</span>
</pre>





<pre><span></span><span>hf</span><span>.</span><span>close</span><span>()</span>
</pre>



<p>Наведений вище код демонструє основні концепції HDF5: групи, набори даних, атрибути. Спочатку ми створюємо об'єкт HDF5 для запису – station.hdf5. Потім ми починаємо зберігати дані в різні групи. Ми бачимо, що у нас є дві групи верхнього рівня, а саме acc і gps, обидві з яких містять підгрупи 1 або 2, що вказують назви станцій. Кожна станція міститиме підгрупу наступного рівня, data, яка використовується для зберігання створених нами масивних даних. Потім ми можемо додати атрибути до груп або даних. Тут ми додали лише <em>dt</em>, <em>start_time</em> та <em>location</em> як атрибути до наборів даних, які ми тут зберігаємо. Ви бачите, що це досить схоже на папкову структуру, де дані <em>acc_1</em> збережені за адресою <em>/acc/1/data</em>. Нарешті, ми закриваємо об'єкт файлу.</p>
<p>Тепер ми бачимо, що зберігати дані в HDF5 легко, і ми могли б використовувати функції <em>create_dataset</em> та <em>create_group</em>, як показано в <a href="http://docs.h5py.org/en/latest/quick.html">посібнику зі швидкого старту</a>. Але я віддаю перевагу вищезгаданому підходу для неявного створення кількох проміжних груп, отримуючи доступ до структури папок.</p>

<h2>Читання файлів HDF5<a href="#read-in-the-hdf5-files" title="Постійне посилання на цей заголовок"></a></h2>
<p>Тепер припустимо, ви надсилаєте файл <em>station.hdf5</em> колезі, який хоче отримати доступ до даних. Ось як він/вона це зробить.</p>


<pre><span></span><span>hf_in</span> <span>=</span> <span>h5py</span><span>.</span><span>File</span><span>(</span><span>'station.hdf5'</span><span>,</span> <span>'r'</span><span>)</span>
</pre>





<pre><span></span><span>list</span><span>(</span><span>hf_in</span><span>.</span><span>keys</span><span>())</span>
</pre>



<pre><span></span>['acc', 'gps']
</pre>





<pre><span></span><span>acc</span> <span>=</span> <span>hf_in</span><span>[</span><span>'acc'</span><span>]</span>
</pre>





<pre><span></span><span>list</span><span>(</span><span>acc</span><span>.</span><span>keys</span><span>())</span>
</pre>



<pre><span></span>['1', '2']
</pre>





<pre><span></span><span>data_1</span> <span>=</span> <span>hf_in</span><span>[</span><span>'acc/1/data'</span><span>]</span>
</pre>





<pre><span></span><span>data_1</span><span>.</span><span>value</span><span>[:</span><span>10</span><span>]</span>
</pre>



<pre><span></span>array([0.41820889, 0.89832446, 0.40229251, 0.41287538, 0.16173359,
       0.75855904, 0.89288185, 0.82944522, 0.84228139, 0.50365515])
</pre>





<pre><span></span><span>list</span><span>(</span><span>data_1</span><span>.</span><span>attrs</span><span>)</span>
</pre>



<pre><span></span>['dt', 'start_time', 'location']
</pre>





<pre><span></span><span>data_1</span><span>.</span><span>attrs</span><span>[</span><span>'dt'</span><span>]</span>
</pre>



<pre><span></span>0.04
</pre>





<pre><span></span><span>data_1</span><span>.</span><span>attrs</span><span>[</span><span>'location'</span><span>]</span>
</pre>



<pre><span></span>'Berkeley'
</pre>



<p>Ми бачимо, що читати HDF5 також легко за допомогою <em>h5py</em>. Після того, як ми прочитали HDF5 в <em>hf_in</em>, ми можемо побачити, які групи є в HDF5, використовуючи функцію <em>keys</em>. Потім ми можемо отримати доступ до членів групи та побачити, що міститься в підгрупах, як <em>hf_in[‘acc`]</em>, або безпосередньо вказати шлях до наборів даних як <em>hf_in[‘acc/1/data`]</em> та отримати дані масиву. Звісно, атрибути, пов'язані з даними, також можуть бути доступні як словник.</p>
