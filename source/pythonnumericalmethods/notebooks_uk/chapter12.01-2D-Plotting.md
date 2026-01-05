<h1>2D Побудова графіків<a href="#d-plotting" title="Постійне посилання на цей заголовок"></a></h1>
<p>У Python *matplotlib* є найважливішим пакетом для побудови графіків. Ви можете переглянути <a href="https://matplotlib.org/gallery/index.html#gallery">галерею matplotlib</a>, щоб зрозуміти, що там можна зробити. Зазвичай перше, що нам потрібно зробити для побудови графіка, це імпортувати пакет matplotlib. У Jupyter Notebook ми можемо відображати фігуру безпосередньо в блокноті, а також мати інтерактивні операції, такі як панорамування, збільшення/зменшення тощо, використовуючи магічну команду - *%matplotlib notebook*. Розглянемо кілька прикладів.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
<span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>
<span>%</span><span>matplotlib</span> notebook
</pre>



<p>Основна функція для побудови графіків — *plot(x,y)*. Функція *plot* приймає два списки/масиви, x та y, і створює візуальне відображення відповідних точок x та y.</p>
<p><strong>СПРОБУЙТЕ!</strong> Маючи списки x = [0, 1, 2, 3] та y = [0, 1, 4, 9], використайте функцію plot для побудови графіка x відносно y.</p>


<pre><span></span><span>x</span> <span>=</span> <span>[</span><span>0</span><span>,</span> <span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>]</span>
<span>y</span> <span>=</span> <span>[</span><span>0</span><span>,</span> <span>1</span><span>,</span> <span>4</span><span>,</span> <span>9</span><span>]</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.01-2D-Plotting_6_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.01-2D-Plotting_6_0.png"/>


<p>На наведеному вище малюнку ви помітите, що за замовчуванням функція plot з'єднує кожну точку синьою лінією. Щоб функція виглядала плавно, використовуйте дрібніші точки дискретизації. Функція *plt.plot* виконала основну роботу з побудови фігури, а *plt.show()* повідомляє Python, що ми закінчили побудову і просимо показати фігуру. Крім того, ви можете побачити кілька кнопок під графіком, які можна використовувати для переміщення лінії, збільшення або зменшення масштабу, збереження фігури. Зверніть увагу, що перед побудовою наступної фігури вам потрібно вимкнути інтерактивний графік, натиснувши кнопку *stop interaction* у верхньому правому куті фігури. В іншому випадку наступна фігура буде побудована в тому ж кадрі. Або ми можемо просто використовувати магічну функцію *%matplotlib inline*, щоб вимкнути інтерактивні функції.</p>
<p><strong>СПРОБУЙТЕ!</strong> Побудуйте графік функції <span>\(f(x) = x^2\) для \(-5\le x \le 5\)</span>.</p>


<pre><span></span><span>%</span><span>matplotlib</span> inline
</pre>





<pre><span></span><span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>-</span><span>5</span><span>,</span><span>5</span><span>,</span> <span>100</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>x</span><span>**</span><span>2</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.01-2D-Plotting_9_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.01-2D-Plotting_9_0.png"/>


<p>Щоб змінити маркер або лінію, ви можете додати третій вхідний аргумент до функції plot, який є рядком, що вказує колір та стиль лінії, які будуть використовуватися на графіку. Наприклад, *plot(x,y,`ro`)* побудує елементи x відносно елементів y, використовуючи червоні, r, кола, ‘o`. Можливі специфікації наведені нижче в таблиці.</p>
<table>
<thead>
<tr><th><p>Символ</p></th>
<th><p>Опис</p></th>
<th><p>Символ</p></th>
<th><p>Опис</p></th>
</tr>
</thead>
<tbody>
<tr><td><p>b</p></td>
<td><p>синій</p></td>
<td><p>T</p></td>
<td><p>T</p></td>
</tr>
<tr><td><p>g</p></td>
<td><p>зелений</p></td>
<td><p>s</p></td>
<td><p>квадрат</p></td>
</tr>
<tr><td><p>r</p></td>
<td><p>червоний</p></td>
<td><p>d</p></td>
<td><p>ромб</p></td>
</tr>
<tr><td><p>c</p></td>
<td><p>блакитний</p></td>
<td><p>v</p></td>
<td><p>трикутник (вниз)</p></td>
</tr>
<tr><td><p>m</p></td>
<td><p>пурпуровий</p></td>
<td><p>^</p></td>
<td><p>трикутник (вгору)</p></td>
</tr>
<tr><td><p>y</p></td>
<td><p>жовтий</p></td>
<td><p>&lt;</p></td>
<td><p>трикутник (вліво)</p></td>
</tr>
<tr><td><p>k</p></td>
<td><p>чорний</p></td>
<td><p>&gt;</p></td>
<td><p>трикутник (вправо)</p></td>
</tr>
<tr><td><p>w</p></td>
<td><p>білий</p></td>
<td><p>p</p></td>
<td><p>пентаграма</p></td>
</tr>
<tr><td><p>.</p></td>
<td><p>точка</p></td>
<td><p>h</p></td>
<td><p>гексаграма</p></td>
</tr>
<tr><td><p>o</p></td>
<td><p>коло</p></td>
<td><p>-</p></td>
<td><p>суцільна</p></td>
</tr>
<tr><td><p>x</p></td>
<td><p>хрестик</p></td>
<td><p>:</p></td>
<td><p>пунктирна</p></td>
</tr>
<tr><td><p>+</p></td>
<td><p>плюс</p></td>
<td><p>-.</p></td>
<td><p>штрихпунктирна</p></td>
</tr>
<tr><td><p>*</p></td>
<td><p>зірка</p></td>
<td><p>–</p></td>
<td><p>штрихова</p></td>
</tr>
</tbody>
</table>
<p><strong>СПРОБУЙТЕ!</strong> Побудуйте графік функції <span>\(f(x) = x^2\) для \(-5\le x \le 5\)</span>, використовуючи пунктирну зелену лінію.</p>


<pre><span></span><span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>-</span><span>5</span><span>,</span><span>5</span><span>,</span> <span>100</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>x</span><span>**</span><span>2</span><span>,</span> <span>'g--'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.01-2D-Plotting_11_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.01-2D-Plotting_11_0.png"/>


<p>Перед оператором *plt.show()* ви можете додати та побудувати більше наборів даних в одній фігурі.</p>
<p><strong>СПРОБУЙТЕ!</strong> Побудуйте графік функцій <span>\(f(x) = x^2\) та \(g(x) = x^3\) для \(-5\le x \le 5\)</span>. Використовуйте різні кольори та маркери для кожної функції.</p>


<pre><span></span><span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>-</span><span>5</span><span>,</span><span>5</span><span>,</span><span>20</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>x</span><span>**</span><span>2</span><span>,</span> <span>'ko'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>x</span><span>**</span><span>3</span><span>,</span> <span>'r*'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.01-2D-Plotting_13_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.01-2D-Plotting_13_0.png"/>


<p>У техніці та науці прийнято завжди давати графіку заголовок та підписи осей, щоб люди розуміли, про що ваш графік. Крім того, іноді ви також хочете змінити розмір фігури. Ви можете додати заголовок до свого графіка за допомогою функції *title*, яка приймає рядок як вхідні дані та встановлює його як заголовок графіка. Функції *xlabel* та *ylabel* працюють так само для назви підписів осей. Щоб змінити розмір фігури, ми можемо створити об'єкт фігури та змінити його розмір. Зауважте, що кожного разу, коли ми викликаємо функцію *plt.figure*, ми створюємо новий об'єкт фігури для малювання на ньому.</p>
<p><strong>СПРОБУЙТЕ!</strong> Додайте заголовок та підписи осей до попереднього графіка. Зробіть фігуру більшою з шириною 10 дюймів та висотою 6 дюймів.</p>


<pre><span></span><span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span><span>6</span><span>))</span>

<span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>-</span><span>5</span><span>,</span><span>5</span><span>,</span><span>20</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>x</span><span>**</span><span>2</span><span>,</span> <span>'ko'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>x</span><span>**</span><span>3</span><span>,</span> <span>'r*'</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>f</span><span>'Plot of Various Polynomials from </span><span>{</span><span>x</span><span>[</span><span>0</span><span>]</span><span>}</span><span> to </span><span>{</span><span>x</span><span>[</span><span>-</span><span>1</span><span>]</span><span>}</span><span>'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'X axis'</span><span>,</span> <span>fontsize</span> <span>=</span> <span>18</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Y axis'</span><span>,</span> <span>fontsize</span> <span>=</span> <span>18</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.01-2D-Plotting_15_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.01-2D-Plotting_15_0.png"/>


<p>Ми бачимо, що ми можемо змінити будь-яку частину фігури, наприклад, розмір підписів осей x та y, вказавши аргумент *fontsize* у функції *plt.xlabel*. Але є деякі попередньо визначені стилі, які ми можемо використовувати для автоматичної зміни стилю. Ось список стилів.</p>


<pre><span></span><span>print</span><span>(</span><span>plt</span><span>.</span><span>style</span><span>.</span><span>available</span><span>)</span>
</pre>



<pre><span></span>['seaborn-dark', 'seaborn-darkgrid', 'seaborn-ticks', 'fivethirtyeight', 'seaborn-whitegrid', 'classic', '_classic_test', 'fast', 'seaborn-talk', 'seaborn-dark-palette', 'seaborn-bright', 'seaborn-pastel', 'grayscale', 'seaborn-notebook', 'ggplot', 'seaborn-colorblind', 'seaborn-muted', 'seaborn', 'Solarize_Light2', 'seaborn-paper', 'bmh', 'tableau-colorblind10', 'seaborn-white', 'dark_background', 'seaborn-poster', 'seaborn-deep']
</pre>



<p>Один з моїх улюблених — стиль *seaborn*. Ми можемо змінити його за допомогою функції *plt.style.use*, і давайте подивимося, якщо ми змінимо його на ‘seaborn-poster`, це зробить усе більшим.</p>


<pre><span></span><span>plt</span><span>.</span><span>style</span><span>.</span><span>use</span><span>(</span><span>'seaborn-poster'</span><span>)</span>
</pre>





<pre><span></span><span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span><span>6</span><span>))</span>

<span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>-</span><span>5</span><span>,</span><span>5</span><span>,</span><span>20</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>x</span><span>**</span><span>2</span><span>,</span> <span>'ko'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>x</span><span>**</span><span>3</span><span>,</span> <span>'r*'</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>f</span><span>'Plot of Various Polynomials from </span><span>{</span><span>x</span><span>[</span><span>0</span><span>]</span><span>}</span><span> to </span><span>{</span><span>x</span><span>[</span><span>-</span><span>1</span><span>]</span><span>}</span><span>'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'X axis'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Y axis'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.01-2D-Plotting_20_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.01-2D-Plotting_20_0.png"/>


<p>Ви можете додати легенду до свого графіка, використовуючи функцію *legend*. І додати аргумент *label* у функцію *plot*. Функція legend також приймає аргумент *loc*, щоб вказати, де розмістити легенду; спробуйте змінити його від 0 до 10.</p>


<pre><span></span><span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span><span>6</span><span>))</span>

<span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>-</span><span>5</span><span>,</span><span>5</span><span>,</span><span>20</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>x</span><span>**</span><span>2</span><span>,</span> <span>'ko'</span><span>,</span> <span>label</span> <span>=</span> <span>'quadratic'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>x</span><span>**</span><span>3</span><span>,</span> <span>'r*'</span><span>,</span> <span>label</span> <span>=</span> <span>'cubic'</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>f</span><span>'Plot of Various Polynomials from </span><span>{</span><span>x</span><span>[</span><span>0</span><span>]</span><span>}</span><span> to </span><span>{</span><span>x</span><span>[</span><span>-</span><span>1</span><span>]</span><span>}</span><span>'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'X axis'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Y axis'</span><span>)</span>
<span>plt</span><span>.</span><span>legend</span><span>(</span><span>loc</span> <span>=</span> <span>2</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.01-2D-Plotting_22_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.01-2D-Plotting_22_0.png"/>


<p>Нарешті, ви можете додатково налаштувати вигляд свого графіка, щоб змінити межі кожної осі за допомогою функцій *xlim* або *ylim*. Також ви можете використовувати функцію *grid*, щоб увімкнути сітку на фігурі.</p>
<p><strong>СПРОБУЙТЕ!</strong> Змініть межі графіка так, щоб x був видимим від -6 до 6, а y — від -10 до 10. Увімкніть сітку.</p>


<pre><span></span><span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span><span>6</span><span>))</span>

<span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>-</span><span>5</span><span>,</span><span>5</span><span>,</span><span>100</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>x</span><span>**</span><span>2</span><span>,</span> <span>'ko'</span><span>,</span> <span>label</span> <span>=</span> <span>'quadratic'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>x</span><span>**</span><span>3</span><span>,</span> <span>'r*'</span><span>,</span> <span>label</span> <span>=</span> <span>'cubic'</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>f</span><span>'Plot of Various Polynomials from </span><span>{</span><span>x</span><span>[</span><span>0</span><span>]</span><span>}</span><span> to </span><span>{</span><span>x</span><span>[</span><span>-</span><span>1</span><span>]</span><span>}</span><span>'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'X axis'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Y axis'</span><span>)</span>
<span>plt</span><span>.</span><span>legend</span><span>(</span><span>loc</span> <span>=</span> <span>2</span><span>)</span>
<span>plt</span><span>.</span><span>xlim</span><span>(</span><span>-</span><span>6</span><span>,</span><span>6</span><span>)</span>
<span>plt</span><span>.</span><span>ylim</span><span>(</span><span>-</span><span>10</span><span>,</span><span>10</span><span>)</span>
<span>plt</span><span>.</span><span>grid</span><span>()</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.01-2D-Plotting_24_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.01-2D-Plotting_24_0.png"/>


<p>Ми можемо створити таблицю графіків на одній фігурі за допомогою функції *subplot*. Функція *subplot* приймає три вхідні дані: кількість рядків графіків, кількість стовпців графіків та номер підграфіка, на який мають бути спрямовані всі виклики функцій побудови графіків. Ви можете перейти до іншого підграфіка, викликавши subplot знову з іншим значенням для розташування графіка.</p>
<p>Існує кілька інших функцій для побудови графіків даних x відносно y. Деякі з них: *scatter*, *bar*, *loglog*, *semilogx* та *semilogy*. Функція *scatter* працює так само, як і plot, за винятком того, що за замовчуванням вона використовує червоні кола (тобто *plot(x,y,`ro`)* еквівалентно *scatter(x,y)*). Функція *bar* будує стовпці, центровані по x з висотою y. Функції *loglog*, *semilogx* та *semilogy* будують дані x та y з логарифмічною шкалою для обох осей, логарифмічною шкалою для осі x та лінійною для осі y, та логарифмічною шкалою для осі y та лінійною для осі x відповідно.</p>
<p><strong>СПРОБУЙТЕ!</strong> Маючи списки x = np.arange(11) та <span>\(y = x^2\)</span>, створіть підграфік 2 на 3, де кожен підграфік будує x відносно y, використовуючи *plot*, *scatter*, *bar*, *loglog*, *semilogx* та *semilogy*. Відповідно назвіть та підпишіть кожен графік. Використайте сітку, але легенда не потрібна.</p>


<pre><span></span><span>x</span> <span>=</span> <span>np</span><span>.</span><span>arange</span><span>(</span><span>11</span><span>)</span>
<span>y</span> <span>=</span> <span>x</span><span>**</span><span>2</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>14</span><span>,</span> <span>8</span><span>))</span>

<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>2</span><span>,</span> <span>3</span><span>,</span> <span>1</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span><span>y</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>'Графік'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'X'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Y'</span><span>)</span>
<span>plt</span><span>.</span><span>grid</span><span>()</span>

<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>2</span><span>,</span> <span>3</span><span>,</span> <span>2</span><span>)</span>
<span>plt</span><span>.</span><span>scatter</span><span>(</span><span>x</span><span>,</span><span>y</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>'Діаграма розсіювання'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'X'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Y'</span><span>)</span>
<span>plt</span><span>.</span><span>grid</span><span>()</span>

<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>2</span><span>,</span> <span>3</span><span>,</span> <span>3</span><span>)</span>
<span>plt</span><span>.</span><span>bar</span><span>(</span><span>x</span><span>,</span><span>y</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>'Стовпчаста діаграма'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'X'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Y'</span><span>)</span>
<span>plt</span><span>.</span><span>grid</span><span>()</span>

<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>2</span><span>,</span> <span>3</span><span>,</span> <span>4</span><span>)</span>
<span>plt</span><span>.</span><span>loglog</span><span>(</span><span>x</span><span>,</span><span>y</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>'Логарифмічний графік'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'X'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Y'</span><span>)</span>
<span>plt</span><span>.</span><span>grid</span><span>(</span><span>which</span><span>=</span><span>'both'</span><span>)</span>

<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>2</span><span>,</span> <span>3</span><span>,</span> <span>5</span><span>)</span>
<span>plt</span><span>.</span><span>semilogx</span><span>(</span><span>x</span><span>,</span><span>y</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>'Напівлогарифмічний графік (вісь X)'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'X'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Y'</span><span>)</span>
<span>plt</span><span>.</span><span>grid</span><span>(</span><span>which</span><span>=</span><span>'both'</span><span>)</span>

<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>2</span><span>,</span> <span>3</span><span>,</span> <span>6</span><span>)</span>
<span>plt</span><span>.</span><span>semilogy</span><span>(</span><span>x</span><span>,</span><span>y</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>'Напівлогарифмічний графік (вісь Y)'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'X'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Y'</span><span>)</span>
<span>plt</span><span>.</span><span>grid</span><span>()</span>

<span>plt</span><span>.</span><span>tight_layout</span><span>()</span>

<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.01-2D-Plotting_26_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.01-2D-Plotting_26_0.png"/>


<p>Ми бачимо, що в кінці нашого графіка ми використали <code><span>plt.tight_layout</span></code>, щоб підфігури не перекривалися одна з одною. Ви можете спробувати і побачити ефект без цього оператора.</p>
<p>Крім того, іноді ви хочете зберегти фігури у певному форматі, наприклад, pdf, jpeg, png тощо. Ви можете зробити це за допомогою функції <code><span>plt.savefig</span></code>.</p>


<pre><span></span><span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>8</span><span>,</span><span>6</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span><span>y</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'X'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Y'</span><span>)</span>
<span>plt</span><span>.</span><span>savefig</span><span>(</span><span>'image.pdf'</span><span>)</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.01-2D-Plotting_28_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.01-2D-Plotting_28_0.png"/>


<p>Нарешті, існують інші функції для побудови 2D-даних. Функція <code><span>errorbar</span></code> будує дані x відносно y, але з смугами похибок для кожного елемента. Функція <code><span>polar</span></code> будує θ відносно r, а не x відносно y. Функція <code><span>stem</span></code> будує стовпчики в точках x з висотою y. Функція <code><span>hist</span></code> створює гістограму набору даних; <code><span>boxplot</span></code> надає статистичний опис набору даних; а <code><span>pie</span></code> створює кругову діаграму. Використання цих функцій залишається для вашого дослідження. Не забудьте перевірити приклади в <a href="https://matplotlib.org/gallery/index.html#gallery">галереї matplotlib</a>.</p>
