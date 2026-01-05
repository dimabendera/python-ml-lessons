<h1>Початок роботи з Python</h1>
<h2>Налаштування робочого середовища</h2>
<p>Перш ніж ми почнемо використовувати Python, нам потрібно налаштувати наше робоче середовище Python на комп'ютері. У цьому розділі ми ознайомимося з процесами, необхідними для початку роботи.</p>
<p>Існують різні способи встановлення Python та пов'язаних з ним пакетів, тут ми рекомендуємо використовувати <a href="https://www.anaconda.com/download/">Anaconda</a> або <a href="https://conda.io/miniconda.html">Miniconda</a> для встановлення та керування вашими пакетами. Залежно від <em>операційної системи</em> (ОС), яку ви використовуєте, тобто Windows, Mac OS X або Linux, вам потрібно завантажити певний інсталятор для вашого комп'ютера. І Anaconda, і Miniconda мають на меті забезпечити прості способи керування робочим середовищем Python для наукових обчислень та наук про дані.</p>
<p>Тут ми використаємо Mac OS X як приклад, щоб показати вам процеси встановлення. Користувачам Windows слід пропустити решту цього розділу та прочитати Додаток А, де описані всі процеси. Основні відмінності між Anaconda та Miniconda такі:</p>
<ul>
<li><p><strong>Anaconda</strong> — це повний дистрибутив, що включає інтерпретатор Python, менеджер пакетів, а також пакети, що часто використовуються в наукових обчисленнях.</p></li>
<li><p><strong>Miniconda</strong> — це полегшена версія Anaconda, яка не містить поширених пакетів, тому вам доведеться встановлювати всі необхідні пакети самостійно. Але вона містить інтерпретатор Python та менеджер пакетів.</p></li>
</ul>
<p>Ми обираємо Miniconda для керування встановленням пакетів. Таким чином, ми можемо встановити лише ті, які нам потрібні.</p>
<p>Процес встановлення Miniconda описаний нижче:</p>
<p><strong>Крок 1: Завантажте інсталятор Miniconda з <a href="https://conda.io/miniconda.html">вебсайту</a></strong></p>
<p>Тут ви можете обрати інсталятор залежно від вашої ОС. Ми оберемо Mac OS X та Python 3.7 як приклад.</p>
<p><img alt="Завантаження Miniconda" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/01.01.1-miniconda_page.png"/></p>
<p><strong>Крок 2: Запустіть інсталятор з термінала:</strong></p>
<p>Після запуску інсталятора, дотримуйтесь інструкцій, і ви успішно його встановите.</p>
<p><img alt="Запуск інсталятора" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/01.01.2-run_miniconda_installer.png"/></p>
<p>Варто зазначити, що ви можете змінити місце встановлення, вказавши альтернативне розташування на вашому комп'ютері, але за замовчуванням це ваш домашній каталог.</p>
<p><img alt="Розташування за замовчуванням" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/01.01.3-default_miniconda_location.png"/></p>
<p>Після встановлення ви можете перевірити встановлені пакети, ввівши наступні команди:</p>
<p><img alt="Швидка перевірка" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/01.01.4-miniconda_check.png"/></p>
<p><strong>Крок 3: Встановіть базові пакети, що використовуються в цій книзі</strong></p>
<p>Спочатку встановимо деякі пакети - <code>ipython</code>, <code>numpy</code>, <code>scipy</code>, <code>pandas</code>, <code>matplotlib</code> та <code>jupyter notebook</code>. Ми поговоримо більше про керування пакетами за допомогою <code>pip</code> та <code>conda</code> пізніше.</p>
<p><img alt="Встановлення пакетів" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/01.01.5-install_packages.png"/></p>
<h2>Три способи запуску коду Python</h2>
<p>Існують різні способи запуску коду Python, і всі вони мають різне призначення. У цьому розділі ми коротко ознайомимо вас із трьома різними способами, щоб ви могли почати.</p>
<p><strong>Використання оболонки Python або Ipython</strong></p>
<p>Найпростіший спосіб запустити код Python — це через оболонку Python або Ipython (що означає Interactive Python). Оболонка Ipython багатша за оболонку Python, вона має такі функції, як автодоповнення по табу, підсвічування помилок кольором, базову інтеграцію з оболонкою UNIX тощо. Оскільки ми щойно встановили Ipython, давайте спробуємо запустити на ньому приклад "hello world". Щоб запустити оболонку Python або Ipython, потрібно ввести її назву в терміналі (дивіться малюнок нижче). Потім ми можемо виконати команду Python, ввівши її в оболонку і натиснувши <code>Enter</code>, і ми одразу побачимо результати виконання команди. Наприклад, ми можемо вивести "Hello World", ввівши <code>print("Hello World")</code>:</p>
<p><img alt="Привіт, світ" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/01.01.6-ipython_example.png"/></p>
<p>У наведеній вище команді, <em>print()</em> — це функція в Python, а "Hello World" — це тип даних рядок, про які ми розповімо пізніше в книзі.</p>
<p><strong>Запуск скрипту/файлу Python з командного рядка</strong></p>
<p>Другий спосіб запустити код Python — це помістити всі команди у файл і зберегти його з розширенням <code>.py</code> (розширення файлу може бути будь-яким, але за традицією зазвичай використовується <code>.py</code>). Наприклад, використайте ваш улюблений текстовий редактор (тут показано <a href="https://code.visualstudio.com/">Visual Studio Code</a>), помістіть команду у файл з назвою <em>hello_world.py</em>:</p>
<p><img alt="Файл Python" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/01.01.7-python_file_example.png"/></p>
<p>Потім просто запустіть його з термінала:</p>
<p><img alt="Запуск Python" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/01.01.8-run_python_file.png"/></p>
<p><strong>Використання Jupyter Notebook</strong></p>
<p>Третій спосіб запустити Python — це через <strong>Jupyter notebook</strong>. Це дуже потужне середовище Python на основі браузера, про яке ми детальніше поговоримо пізніше в цьому розділі. Тут ми лише коротко подивимося, як можна запустити код з Jupyter Notebook. Запустіть <code>jupyter notebook</code> у командному рядку bash:</p>
<pre>jupyter notebook
</pre>
<p>Потім ви побачите, як з'явиться локальна веб-сторінка, де за допомогою кнопки у верхньому правому куті можна створити новий блокнот Python3:</p>
<p><img alt="Запуск Jupyter" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/01.01.9-launching_jupyter.png"/></p>
<p>Запускати код у Jupyter Notebook легко: ви вводите свій код у комірку і натискаєте <code>shift + enter</code>, щоб виконати комірку, а результати будуть показані під кодом.</p>
<p><img alt="Приклад блокнота" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/01.01.10-run_code_jupyter.png"/></p>
<h2>Дзен Пайтона</h2>
<p>Гаразд, у попередньому розділі ми дізналися, як налаштувати наше робоче середовище та запускати Python різними способами. Давайте завершимо цей розділ, ознайомившись зі знаменитим "Дзеном Пайтона", виконавши наступну команду одним із трьох способів. Можливо, ви не зрозумієте вивід зараз, але з часом, я впевнений, ви зрозумієте, наскільки він корисний.</p>
<pre>import this
</pre>
<pre>Дзен Пайтона, Тім Петерс

Красиве краще за потворне.
Явне краще за неявне.
Просте краще за складне.
Складне краще за заплутане.
Плоске краще за вкладене.
Розріджене краще за щільне.
Читабельність має значення.
Особливі випадки не настільки особливі, щоб порушувати правила.
Хоча практичність важливіша за чистоту.
Помилки ніколи не повинні замовчуватися.
Якщо вони не приглушені явно.
Перед лицем неоднозначності відмовтеся від спокуси вгадувати.
Має бути один — і бажано лише один — очевидний спосіб зробити це.
Хоча спочатку цей спосіб може бути неочевидним, якщо ви не голландець.
Зараз краще, ніж ніколи.
Хоча "ніколи" часто краще, ніж "прямо* зараз".
Якщо реалізацію важко пояснити — це погана ідея.
Якщо реалізацію легко пояснити — це може бути гарною ідеєю.
Простори імен — чудова ідея, давайте використовувати їх частіше!
</pre>
