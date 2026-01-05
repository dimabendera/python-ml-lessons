<h1>Знайомство з масивами Numpy<a href="#introducing-numpy-arrays" title="Permalink to this headline"></a></h1>
<p>У другій частині ми вивчатимемо чисельні методи з використанням Python. Пізніше в книзі ми будемо часто використовувати масиви/матриці. Тому тут ми представимо найпоширеніший спосіб роботи з масивами в Python за допомогою <a href="http://www.numpy.org/">модуля Numpy</a>. Numpy, ймовірно, є найфундаментальнішим модулем для числових обчислень у Python.</p>
<p>NumPy є важливим у наукових обчисленнях, він написаний як на Python, так і на C (для швидкості). На його веб-сайті перелічено кілька важливих особливостей Numpy:</p>
<ul>
<li><p>потужний N-вимірний об'єкт масиву</p></li>
<li><p>складні функції (трансляції)</p></li>
<li><p>інструменти для інтеграції коду C/C++ та Fortran</p></li>
<li><p>корисні можливості лінійної алгебри, перетворення Фур'є та генерації випадкових чисел</p></li>
</ul>
<p>Тут ми лише познайомимо вас з масивом Numpy, який пов'язаний зі структурою даних, але ми поступово торкнемося інших аспектів Numpy в наступних розділах.</p>
<p>Щоб використовувати модуль Numpy, нам потрібно спочатку його імпортувати. Загальноприйнятим способом імпорту є використання "np" як скороченої назви.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
</pre>



<p><strong>УВАГА!</strong> Звісно, ви можете назвати його будь-яким ім'ям, але зазвичай "np" прийнято всією спільнотою, і це є хорошою практикою використовувати його для очевидних цілей.</p>
<p>Щоб визначити масив у Python, ви можете використати функцію <em>np.array</em> для перетворення списку.</p>
<p><strong>СПРОБУЙТЕ!</strong> Створіть наступні масиви:</p>
<p><span>\(x = \begin{pmatrix} 
1 &amp; 4 &amp; 3 \\
\end{pmatrix}\)</span></p>
<p><span>\(y = \begin{pmatrix} 
1 &amp; 4 &amp; 3 \\
9 &amp; 2 &amp; 7 \\
\end{pmatrix}\)</span></p>


<pre><span></span><span>x</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([</span><span>1</span><span>,</span> <span>4</span><span>,</span> <span>3</span><span>])</span>
<span>x</span>
</pre>



<pre><span></span>array([1, 4, 3])
</pre>





<pre><span></span><span>y</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>1</span><span>,</span> <span>4</span><span>,</span> <span>3</span><span>],</span> <span>[</span><span>9</span><span>,</span> <span>2</span><span>,</span> <span>7</span><span>]])</span>
<span>y</span>
</pre>



<pre><span></span>array([[1, 4, 3],
       [9, 2, 7]])
</pre>



<p><strong>ПРИМІТКА!</strong> 2-D масив можна представити за допомогою вкладених списків, де внутрішній список представляє кожен рядок.</p>
<p>Часто нам потрібно знати розмір або довжину масиву. Атрибут <em>shape</em> викликається для масиву M і повертає кортеж, де перший елемент — це кількість рядків у матриці M, а другий — кількість стовпців у M. Зауважте, що вивід атрибута <em>shape</em> є кортежем. Атрибут <em>size</em> викликається для масиву M і повертає загальну кількість елементів у матриці M.</p>
<p><strong>СПРОБУЙТЕ!</strong> Знайдіть кількість рядків, стовпців та загальний розмір для масиву y.</p>


<pre><span></span><span>y</span><span>.</span><span>shape</span>
</pre>



<pre><span></span>(2, 3)
</pre>





<pre><span></span><span>y</span><span>.</span><span>size</span>
</pre>



<pre><span></span>6
</pre>



<p><strong>ПРИМІТКА!</strong> Ви можете помітити різницю в тому, що ми використовуємо лише <em>y.shape</em> замість <em>y.shape()</em>, це тому, що <em>shape</em> є атрибутом, а не методом цього об'єкта масиву. Ми розглянемо більше про об'єктно-орієнтоване програмування в наступному розділі. Наразі вам потрібно пам'ятати, що коли ми викликаємо метод об'єкта, ми повинні використовувати дужки, а для атрибутів — ні.</p>
<p>Дуже часто нам потрібно генерувати масиви, які мають певну структуру або шаблон. Наприклад, ми можемо захотіти створити масив z = [1 2 3 … 2000]. Було б дуже громіздко вводити весь опис z у Python. Для генерації впорядкованих та рівномірно розподілених масивів корисно використовувати функцію <em>arange</em> у Numpy.</p>
<p><strong>СПРОБУЙТЕ!</strong> Створіть масив <em>z</em> від 1 до 2000 з кроком 1.</p>


<pre><span></span><span>z</span> <span>=</span> <span>np</span><span>.</span><span>arange</span><span>(</span><span>1</span><span>,</span> <span>2000</span><span>,</span> <span>1</span><span>)</span>
<span>z</span>
</pre>



<pre><span></span>array([   1,    2,    3, ..., 1997, 1998, 1999])
</pre>



<p>Використовуючи <em>np.arange</em>, ми можемо легко створити <em><em>z</em></em>. Перші два числа — це початок і кінець послідовності, а останнє — крок. Оскільки дуже часто крок дорівнює 1, якщо крок не вказано, Python використовуватиме значення за замовчуванням 1. Тому <em><em>np.arange(1, 2000)</em></em> дасть той самий результат, що й <em>np.arange(1, 2000, 1)</em>. Також можна використовувати від'ємні або нецілочисельні кроки. Якщо крок "пропускає" останнє значення, послідовність буде розширена лише до значення, що передує кінцевому. Наприклад, <em>x = np.arange(1,8,2)</em> буде [1, 3, 5, 7].</p>
<p><strong>СПРОБУЙТЕ!</strong> Згенеруйте масив [0.5, 1, 1.5, 2, 2.5].</p>


<pre><span></span><span>np</span><span>.</span><span>arange</span><span>(</span><span>0.5</span><span>,</span> <span>3</span><span>,</span> <span>0.5</span><span>)</span>
</pre>



<pre><span></span>array([ 0.5,  1. ,  1.5,  2. ,  2.5])
</pre>



<p>Іноді ми хочемо гарантувати початкову та кінцеву точки для масиву, але при цьому мати рівномірно розподілені елементи. Наприклад, нам може знадобитися масив, який починається з 1, закінчується 8 і містить рівно 10 елементів. Для цього можна використовувати функцію <em>np.linspace</em>. <em>linspace</em> приймає три вхідні значення, розділені комами. Отже, <em>A = linspace(a,b,n)</em> генерує масив з n рівновіддалених елементів, що починається з a і закінчується b.</p>
<p><strong>СПРОБУЙТЕ!</strong> Використовуйте <em>linspace</em>, щоб згенерувати масив, який починається з 3, закінчується 9 і містить 10 елементів.</p>


<pre><span></span><span>np</span><span>.</span><span>linspace</span><span>(</span><span>3</span><span>,</span> <span>9</span><span>,</span> <span>10</span><span>)</span>
</pre>



<pre><span></span>array([ 3.        ,  3.66666667,  4.33333333,  5.        ,  5.66666667,
        6.33333333,  7.        ,  7.66666667,  8.33333333,  9.        ])
</pre>



<p>Доступ до 1D масиву numpy схожий на те, що ми описували для списків або кортежів, він має індекс для вказівки місцезнаходження. Наприклад:</p>


<pre><span></span><span># отримати 2-й елемент x</span>
<span>x</span><span>[</span><span>1</span><span>]</span>
</pre>



<pre><span></span>4
</pre>





<pre><span></span><span># отримати всі елементи після 2-го елемента x</span>
<span>x</span><span>[</span><span>1</span><span>:]</span>
</pre>



<pre><span></span>array([4, 3])
</pre>





<pre><span></span><span># отримати останній елемент x</span>
<span>x</span><span>[</span><span>-</span><span>1</span><span>]</span>
</pre>



<pre><span></span>3
</pre>



<p>Для 2D масивів це трохи інакше, оскільки ми маємо рядки та стовпці. Щоб отримати доступ до даних у 2D масиві M, нам потрібно використовувати M[r, c], де рядок r і стовпець c розділені комою. Це називається індексацією масиву. r і c можуть бути одним числом, списком тощо. Якщо ви думаєте лише про індекс рядка або індекс стовпця, то це схоже на 1D масив. Давайте використаємо <span>\(y = \begin{pmatrix}
1 &amp; 4 &amp; 3 \\
9 &amp; 2 &amp; 7 \\
\end{pmatrix}\)</span> як приклад.</p>
<p><strong>СПРОБУЙТЕ!</strong> Отримайте елемент у першому рядку та другому стовпці масиву <em>y</em>.</p>


<pre><span></span><span>y</span><span>[</span><span>0</span><span>,</span><span>1</span><span>]</span>
</pre>



<pre><span></span>4
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Отримайте перший рядок масиву <em>y</em>.</p>


<pre><span></span><span>y</span><span>[</span><span>0</span><span>,</span> <span>:]</span>
</pre>



<pre><span></span>array([1, 4, 3])
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Отримайте останній стовпець масиву <em>y</em>.</p>


<pre><span></span><span>y</span><span>[:,</span> <span>-</span><span>1</span><span>]</span>
</pre>



<pre><span></span>array([3, 7])
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Отримайте перший та третій стовпці масиву <em>y</em>.</p>


<pre><span></span><span>y</span><span>[:,</span> <span>[</span><span>0</span><span>,</span> <span>2</span><span>]]</span>
</pre>



<pre><span></span>array([[1, 3],
       [9, 7]])
</pre>



<p>Існують деякі попередньо визначені масиви, які є дуже корисними. Наприклад, <em>np.zeros</em>, <em>np.ones</em> та <em>np.empty</em> — це 3 корисні функції. Розглянемо приклади.</p>
<p><strong>СПРОБУЙТЕ!</strong> Згенеруйте масив розміром 3 на 5, заповнений нулями.</p>


<pre><span></span><span>np</span><span>.</span><span>zeros</span><span>((</span><span>3</span><span>,</span> <span>5</span><span>))</span>
</pre>



<pre><span></span>array([[ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.]])
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Згенеруйте масив розміром 5 на 3, заповнений одиницями.</p>


<pre><span></span><span>np</span><span>.</span><span>ones</span><span>((</span><span>5</span><span>,</span> <span>3</span><span>))</span>
</pre>



<pre><span></span>array([[ 1.,  1.,  1.],
       [ 1.,  1.,  1.],
       [ 1.,  1.,  1.],
       [ 1.,  1.,  1.],
       [ 1.,  1.,  1.]])
</pre>



<p><strong>ПРИМІТКА!</strong> Форма масиву визначається в кортежі, де перший елемент — це рядок, а другий — стовпець. Якщо вам потрібен лише 1D масив, то вхідним даними може бути лише одне число: <em>np.ones(5)</em>.</p>
<p><strong>СПРОБУЙТЕ!</strong> Згенеруйте порожній 1D масив з 3 елементами.</p>


<pre><span></span><span>np</span><span>.</span><span>empty</span><span>(</span><span>3</span><span>)</span>
</pre>



<pre><span></span>array([ 0.,  0.,  0.])
</pre>



<p><strong>ПРИМІТКА!</strong> Порожній масив насправді не порожній, він заповнений випадковими дуже малими числами.</p>
<p>Ви можете перепризначити значення елемента масиву, використовуючи індексацію масиву та оператор присвоєння. Ви можете перепризначити кілька елементів одному числу, використовуючи індексацію масиву зліва. Ви також можете перепризначити кілька елементів масиву, якщо кількість елементів, яким присвоюється значення, і кількість присвоюваних елементів однакові. Ви можете створити масив за допомогою індексації.</p>
<p><strong>СПРОБУЙТЕ!</strong> Нехай a = [1, 2, 3, 4, 5, 6]. Перепризначте четвертому елементу A значення 7. Перепризначте першому, другому та третьому елементам значення 1. Перепризначте другому, третьому та четвертому елементам значення 9, 8 та 7.</p>


<pre><span></span><span>a</span> <span>=</span> <span>np</span><span>.</span><span>arange</span><span>(</span><span>1</span><span>,</span> <span>7</span><span>)</span>
<span>a</span>
</pre>



<pre><span></span>array([1, 2, 3, 4, 5, 6])
</pre>





<pre><span></span><span>a</span><span>[</span><span>3</span><span>]</span> <span>=</span> <span>7</span>
<span>a</span>
</pre>



<pre><span></span>array([1, 2, 3, 7, 5, 6])
</pre>





<pre><span></span><span>a</span><span>[:</span><span>3</span><span>]</span> <span>=</span> <span>1</span>
<span>a</span>
</pre>



<pre><span></span>array([1, 1, 1, 7, 5, 6])
</pre>





<pre><span></span><span>a</span><span>[</span><span>1</span><span>:</span><span>4</span><span>]</span> <span>=</span> <span>[</span><span>9</span><span>,</span> <span>8</span><span>,</span> <span>7</span><span>]</span>
<span>a</span>
</pre>



<pre><span></span>array([1, 9, 8, 7, 5, 6])
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Створіть нульовий масив b розміром 2 на 2 і встановіть <span>\(b = \begin{pmatrix} 
1 &amp; 2 \\
3 &amp; 4  \\
\end{pmatrix}\)</span> за допомогою індексації масиву.</p>


<pre><span></span><span>b</span> <span>=</span> <span>np</span><span>.</span><span>zeros</span><span>((</span><span>2</span><span>,</span> <span>2</span><span>))</span>
<span>b</span><span>[</span><span>0</span><span>,</span> <span>0</span><span>]</span> <span>=</span> <span>1</span>
<span>b</span><span>[</span><span>0</span><span>,</span> <span>1</span><span>]</span> <span>=</span> <span>2</span>
<span>b</span><span>[</span><span>1</span><span>,</span> <span>0</span><span>]</span> <span>=</span> <span>3</span>
<span>b</span><span>[</span><span>1</span><span>,</span> <span>1</span><span>]</span> <span>=</span> <span>4</span>
<span>b</span>
</pre>



<pre><span></span>array([[ 1.,  2.],
       [ 3.,  4.]])
</pre>



<p><strong>УВАГА!</strong> Хоча ви можете створити масив з нуля за допомогою індексації, ми не радимо цього робити. Це може вас заплутати, і помилки буде важче знайти у вашому коді пізніше. Наприклад, b[1, 1] = 1 дасть результат <span>\(b = \begin{pmatrix} 
0 &amp; 0 \\
0 &amp; 1  \\
\end{pmatrix}\)</span>, що дивно, оскільки b[0, 0], b[0, 1] та b[1, 0] ніколи не були вказані.</p>
<p>Для масивів визначена базова арифметика. Однак існують операції між скаляром (одним числом) і масивом, а також операції між двома масивами. Ми почнемо з операцій між скаляром і масивом. Для ілюстрації, нехай c — скаляр, а b — матриця.</p>
<p><em>b + c</em>, <em>b − c</em>, <em>b * c</em> та <em>b / c</em> додає c до кожного елемента b, віднімає c від кожного елемента b, множить кожен елемент b на c та ділить кожен елемент b на c відповідно.</p>
<p><strong>СПРОБУЙТЕ!</strong> Нехай <span>\(b = \begin{pmatrix} 
1 &amp; 2 \\
3 &amp; 4  \\
\end{pmatrix}\)</span>. Додайте та відніміть 2 від b. Помножте та поділіть b на 2. Піднесіть кожен елемент b до квадрату. Нехай c — скаляр. Самостійно перевірте комутативність скалярного додавання та множення: b + c = c + b та cb = bc.</p>


<pre><span></span><span>b</span> <span>+</span> <span>2</span>
</pre>



<pre><span></span>array([[ 3.,  4.],
       [ 5.,  6.]])
</pre>





<pre><span></span><span>b</span> <span>-</span> <span>2</span>
</pre>



<pre><span></span>array([[-1.,  0.],
       [ 1.,  2.]])
</pre>





<pre><span></span><span>2</span> <span>*</span> <span>b</span>
</pre>



<pre><span></span>array([[ 2.,  4.],
       [ 6.,  8.]])
</pre>





<pre><span></span><span>b</span> <span>/</span> <span>2</span>
</pre>



<pre><span></span>array([[ 0.5,  1. ],
       [ 1.5,  2. ]])
</pre>





<pre><span></span><span>b</span><span>**</span><span>2</span>
</pre>



<pre><span></span>array([[  1.,   4.],
       [  9.,  16.]])
</pre>



<p>Опис операцій між двома матрицями є складнішим. Нехай b і d — дві матриці однакового розміру. b − d бере кожен елемент b і віднімає відповідний елемент d. Аналогічно, b + d додає кожен елемент d до відповідного елемента b.</p>
<p><strong>СПРОБУЙТЕ!</strong> Нехай <span>\(b = \begin{pmatrix} 
1 &amp; 2 \\
3 &amp; 4  \\
\end{pmatrix}\)</span> та <span>\(d = \begin{pmatrix} 
3 &amp; 4 \\
5 &amp; 6  \\
\end{pmatrix}\)</span>. Обчисліть b + d та b - d.</p>


<pre><span></span><span>b</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>1</span><span>,</span> <span>2</span><span>],</span> <span>[</span><span>3</span><span>,</span> <span>4</span><span>]])</span>
<span>d</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>3</span><span>,</span> <span>4</span><span>],</span> <span>[</span><span>5</span><span>,</span> <span>6</span><span>]])</span>
</pre>





<pre><span></span><span>b</span> <span>+</span> <span>d</span>
</pre>



<pre><span></span>array([[ 4,  6],
       [ 8, 10]])
</pre>





<pre><span></span><span>b</span> <span>-</span> <span>d</span>
</pre>



<pre><span></span>array([[-2, -2],
       [-2, -2]])
</pre>



<p>Існує два різних види множення (і ділення) матриць. Є поелементне множення матриць і стандартне множення матриць. У цьому розділі ми покажемо лише, як працює поелементне множення та ділення матриць. Стандартне множення матриць буде описано в наступному розділі про лінійну алгебру. Python використовує символ * для позначення поелементного множення. Для матриць b і d однакового розміру, b * d бере кожен елемент b і множить його на відповідний елемент d. Те ж саме стосується / та **.</p>
<p><strong>СПРОБУЙТЕ!</strong> Обчисліть b * d, b / d та b**d.</p>


<pre><span></span><span>b</span> <span>*</span> <span>d</span>
</pre>



<pre><span></span>array([[ 3,  8],
       [15, 24]])
</pre>





<pre><span></span><span>b</span> <span>/</span> <span>d</span>
</pre>



<pre><span></span>array([[ 0.33333333,  0.5       ],
       [ 0.6       ,  0.66666667]])
</pre>





<pre><span></span><span>b</span><span>**</span><span>d</span>
</pre>



<pre><span></span>array([[   1,   16],
       [ 243, 4096]])
</pre>



<p>Транспонована матриця масиву b — це масив d, де b[i, j] = d[j, i]. Іншими словами, транспонування міняє місцями рядки та стовпці b. Ви можете транспонувати масив у Python за допомогою методу масиву <em>T</em>.</p>
<p><strong>СПРОБУЙТЕ!</strong> Обчисліть транспоновану матрицю масиву b.</p>


<pre><span></span><span>b</span><span>.</span><span>T</span>
</pre>



<pre><span></span>array([[1, 3],
       [2, 4]])
</pre>



<p>Numpy має багато арифметичних функцій, таких як sin, cos тощо, які можуть приймати масиви як вхідні аргументи. Виходом є функція, обчислена для кожного елемента вхідного масиву. Функція, яка приймає масив як вхідні дані та виконує над ним операцію, називається <strong>векторизованою</strong>.</p>
<p><strong>СПРОБУЙТЕ!</strong> Обчисліть <em>np.sqrt</em> для x = [1, 4, 9, 16].</p>


<pre><span></span><span>x</span> <span>=</span> <span>[</span><span>1</span><span>,</span> <span>4</span><span>,</span> <span>9</span><span>,</span> <span>16</span><span>]</span>
<span>np</span><span>.</span><span>sqrt</span><span>(</span><span>x</span><span>)</span>
</pre>



<pre><span></span>array([ 1.,  2.,  3.,  4.])
</pre>



<p>Логічні операції визначені лише між скаляром і масивом та між двома масивами однакового розміру. Між скаляром і масивом логічна операція виконується між скаляром і кожним елементом масиву. Між двома масивами логічна операція виконується поелементно.</p>
<p><strong>СПРОБУЙТЕ!</strong> Перевірте, які елементи масиву x = [1, 2, 4, 5, 9, 3] більші за 3. Перевірте, які елементи в x більші за відповідний елемент в y = [0, 2, 3, 1, 2, 3].</p>


<pre><span></span><span>x</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([</span><span>1</span><span>,</span> <span>2</span><span>,</span> <span>4</span><span>,</span> <span>5</span><span>,</span> <span>9</span><span>,</span> <span>3</span><span>])</span>
<span>y</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([</span><span>0</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>,</span> <span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>])</span>
</pre>





<pre><span></span><span>x</span> <span>&gt;</span> <span>3</span>
</pre>



<pre><span></span>array([False, False,  True,  True,  True, False], dtype=bool)
</pre>





<pre><span></span><span>x</span> <span>&gt;</span> <span>y</span>
</pre>



<pre><span></span>array([ True, False,  True,  True,  True, False], dtype=bool)
</pre>



<p>Python може індексувати елементи масиву, які задовольняють логічний вираз.</p>
<p><strong>СПРОБУЙТЕ!</strong> Нехай x — той самий масив, що й у попередньому прикладі. Створіть змінну y, яка містить усі елементи x, що строго більші за 3. Присвойте всім значенням x, які більші за 3, значення 0.</p>


<pre><span></span><span>y</span> <span>=</span> <span>x</span><span>[</span><span>x</span> <span>&gt;</span> <span>3</span><span>]</span>
<span>y</span>
</pre>



<pre><span></span>array([4, 5, 9])
</pre>





<pre><span></span><span>x</span><span>[</span><span>x</span> <span>&gt;</span> <span>3</span><span>]</span> <span>=</span> <span>0</span>
<span>x</span>
</pre>



<pre><span></span>array([1, 2, 0, 0, 0, 3])
</pre>
