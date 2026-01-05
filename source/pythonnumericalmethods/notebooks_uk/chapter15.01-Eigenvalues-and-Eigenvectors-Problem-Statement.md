```html
<h1>Постановка задачі про власні значення та власні вектори<a href="#eigenvalues-and-eigenvectors-problem-statement" title="Permalink to this headline"></a></h1>

<h2>Власні значення та власні вектори<a href="#eigenvalues-and-eigenvectors" title="Permalink to this headline"></a></h2>
<p>З попереднього розділу ми дізналися, що застосування матриці <span>\(A\)</span> до вектора-стовпця <span>\(x\)</span>, тобто <span>\(Ax\)</span>, є лінійним перетворенням <span>\(x\)</span>. Існує особливе перетворення у такій формі:</p>

\[Ax = \lambda{x}\]
<p>Де <span>\(A\)</span> — матриця розміром <span>\(n\times{n}\)</span>, <span>\(x\)</span> — вектор-стовпець розміром <span>\(n\times{1}\)</span> (<span>\(X\neq{0}\)</span>), а <span>\(\lambda\)</span> — деякий скаляр. Будь-яке <span>\(\lambda\)</span>, що задовольняє наведене вище рівняння, називається <strong>власним значенням</strong> матриці <span>\(A\)</span>, а пов'язаний з ним вектор <span>\(x\)</span> називається <strong>власним вектором</strong>, що відповідає <span>\(\lambda\)</span>.</p>


<h2>Мотивація<a href="#the-motivation-behind" title="Permalink to this headline"></a></h2>
<p>Мотивація, що стоїть за власними значеннями та власними векторами, полягає в тому, що вони допомагають нам зрозуміти характеристики лінійного перетворення, тим самим спрощуючи завдання. Ми знаємо, що вектор <span>\(x\)</span> може бути перетворений в інший вектор шляхом множення на <span>\(A\)</span> - <span>\(Ax\)</span>. Ефект перетворення полягає у зміні довжини вектора (масштабуванні) та/або його повороті. Наведене вище рівняння вказує на те, що для деяких векторів ефект перетворення <span>\(Ax\)</span> полягає лише в масштабуванні (розтягуванні, стисненні та віддзеркаленні). Власні вектори — це вектори, що мають цю властивість, а власні значення <span>\(\lambda\)</span> — це коефіцієнти масштабування. Розглянемо наступний приклад.</p>
<p><strong>СПРОБУЙТЕ</strong> Побудуйте графік вектора <span>\(x\)</span> = [[1], [1]] та вектора <span>\(b = Ax\)</span>, де <span>\(A\)</span> = [[2, 0], [0, 1]]</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
<span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>

<span>plt</span><span>.</span><span>style</span><span>.</span><span>use</span><span>(</span><span>'seaborn-poster'</span><span>)</span>

<span>%</span><span>matplotlib</span> inline

<span>def</span> <span>plot_vect</span><span>(</span><span>x</span><span>,</span> <span>b</span><span>,</span> <span>xlim</span><span>,</span> <span>ylim</span><span>):</span>
    <span>'''</span>
<span>    функція для побудови двох векторів,</span>
<span>    x - початковий вектор</span>
<span>    b - трансформований вектор</span>
<span>    xlim - межа для x</span>
<span>    ylim - межа для y</span>
<span>    '''</span>
    <span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span> <span>6</span><span>))</span>
    <span>plt</span><span>.</span><span>quiver</span><span>(</span><span>0</span><span>,</span><span>0</span><span>,</span><span>x</span><span>[</span><span>0</span><span>],</span><span>x</span><span>[</span><span>1</span><span>],</span>\
        <span>color</span><span>=</span><span>'k'</span><span>,</span><span>angles</span><span>=</span><span>'xy'</span><span>,</span>\
        <span>scale_units</span><span>=</span><span>'xy'</span><span>,</span><span>scale</span><span>=</span><span>1</span><span>,</span>\
        <span>label</span><span>=</span><span>'Початковий вектор'</span><span>)</span>
    <span>plt</span><span>.</span><span>quiver</span><span>(</span><span>0</span><span>,</span><span>0</span><span>,</span><span>b</span><span>[</span><span>0</span><span>],</span><span>b</span><span>[</span><span>1</span><span>],</span>\
        <span>color</span><span>=</span><span>'g'</span><span>,</span><span>angles</span><span>=</span><span>'xy'</span><span>,</span>\
        <span>scale_units</span><span>=</span><span>'xy'</span><span>,</span><span>scale</span><span>=</span><span>1</span><span>,</span>\
        <span>label</span> <span>=</span><span>'Трансформований вектор'</span><span>)</span>
    <span>plt</span><span>.</span><span>xlim</span><span>(</span><span>xlim</span><span>)</span>
    <span>plt</span><span>.</span><span>ylim</span><span>(</span><span>ylim</span><span>)</span>
    <span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'X'</span><span>)</span>
    <span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Y'</span><span>)</span>
    <span>plt</span><span>.</span><span>legend</span><span>()</span>
    <span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>





<pre><span></span><span>A</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>2</span><span>,</span> <span>0</span><span>],[</span><span>0</span><span>,</span> <span>1</span><span>]])</span>

<span>x</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>1</span><span>],[</span><span>1</span><span>]])</span>
<span>b</span> <span>=</span> <span>np</span><span>.</span><span>dot</span><span>(</span><span>A</span><span>,</span> <span>x</span><span>)</span>
<span>plot_vect</span><span>(</span><span>x</span><span>,</span><span>b</span><span>,(</span><span>0</span><span>,</span><span>3</span><span>),(</span><span>0</span><span>,</span><span>2</span><span>))</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter15.01-Eigenvalues-and-Eigenvectors-Problem-Statement_5_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter15.01-Eigenvalues-and-Eigenvectors-Problem-Statement_5_0.png"/>


<p>З отриманого графіка видно, що початковий вектор <span>\(x\)</span> повернувся і розтягнувся після перетворення матрицею <span>\(A\)</span>. Вектор [[1], [1]] перетворився на [[2], [1]]. Спробуймо виконати ту ж вправу з іншим вектором [[1], [0]].</p>
<p><strong>СПРОБУЙТЕ!</strong> Побудуйте графік вектора <span>\(x\)</span> = [[1], [0]] та вектора <span>\(b = Ax\)</span>, де <span>\(A\)</span> = [[2, 0], [0, 1]]</p>


<pre><span></span><span>x</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>1</span><span>],</span> <span>[</span><span>0</span><span>]])</span>
<span>b</span> <span>=</span> <span>np</span><span>.</span><span>dot</span><span>(</span><span>A</span><span>,</span> <span>x</span><span>)</span>

<span>plot_vect</span><span>(</span><span>x</span><span>,</span><span>b</span><span>,(</span><span>0</span><span>,</span><span>3</span><span>),(</span><span>-</span><span>0.5</span><span>,</span><span>0.5</span><span>))</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter15.01-Eigenvalues-and-Eigenvectors-Problem-Statement_7_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter15.01-Eigenvalues-and-Eigenvectors-Problem-Statement_7_0.png"/>


<p>Тепер ми бачимо, що для цього нового вектора єдине, що змінилося після перетворення, — це його довжина, він розтягнувся. Новий вектор — [[2], [0]], отже, перетворення має вигляд</p>

\[ Ax = 2x\]
<p>де <span>\(x\)</span> = [[1], [0]] та <span>\(\lambda=2\)</span>. Напрямок вектора зовсім не змінився (немає обертання). Ви також можете спробувати перевірити, що [[0], [1]] є ще одним власним вектором.</p>


<h2>Характеристичне рівняння<a href="#the-characteristic-equation" title="Permalink to this headline"></a></h2>
<p>Щоб знайти власні значення та власні вектори, з рівняння <span>\(Ax=\lambda{x}\)</span> ми можемо отримати наступну форму:</p>

\[(A-\lambda{I})x=0\]
<p>Де <span>\(I\)</span> — одинична матриця тієї ж розмірності, що й <span>\(A\)</span>. Якщо матриця <span>\(A-\lambda{I}\)</span> має обернену, то, помноживши обидві частини на <span>\((A-\lambda{I})^{-1}\)</span>, ми отримаємо тривіальний розв'язок <span>\(x=0\)</span>. Отже, коли матриця <span>\(A-\lambda{I}\)</span> є сингулярною (виродженою, не має оберненої), ми маємо нетривіальний розв'язок, що означає, що її визначник дорівнює нулю:</p>

\[det(A-\lambda{I})=0\]
<p>це рівняння називається <strong>характеристичним рівнянням</strong>, яке приводить до поліноміального рівняння відносно <span>\(\lambda\)</span>, з якого ми можемо знайти власні значення. Розглянемо один приклад.</p>
<p><strong>СПРОБУЙТЕ!</strong> Знайдіть власні значення для матриці [[0, 2], [2, 3]]</p>
<p>Характеристичне рівняння дає нам</p>

\[\begin{split}
\begin{vmatrix}
0-\lambda &amp; 2 \\ 
2 &amp; 3-\lambda
\end{vmatrix}
=0
\end{split}\]
<p>Отже, ми маємо</p>

\[-\lambda(3-\lambda)-4 = 0 \Rightarrow \lambda^2-3\lambda-4=0\]
<p>Ми отримуємо два власні значення:</p>

\[\lambda_1 = 4, \lambda_2 = -1\]
<p><strong>СПРОБУЙТЕ!</strong> Знайдіть власні вектори для двох наведених вище власних значень.</p>
<p>Знайдемо перший власний вектор для <span>\(\lambda_1 = 4\)</span>. Ми можемо просто підставити це значення назад у рівняння <span>\((A-\lambda{I})x=0\)</span>, звідки маємо:</p>

\[\begin{split}
\begin{bmatrix}
-4 &amp; 2 \\
2 &amp; -1 \\
\end{bmatrix}
\begin{bmatrix}
x_1\\x_2\\
\end{bmatrix}
=\begin{bmatrix}
0\\0\\
\end{bmatrix}
\end{split}\]
<p>Отже, ми маємо два рівняння <span>\(-4x_1+2x_2=0\)</span> та <span>\(2x_1-x_2=0\)</span>, обидва з яких вказують на те, що <span>\(x_2=2x_1\)</span>. Таким чином, перший власний вектор може бути представлений як</p>

\[\begin{split}x_1 = k_1\begin{bmatrix}
1\\2\\
\end{bmatrix}\end{split}\]
<p><span>\(k_1\)</span> — це скаляр (<span>\(k_1 \neq 0\)</span>). Доки співвідношення між <span>\(x_2\)</span> та <span>\(x_1\)</span> дорівнює 2, вектор буде власним. Ми можемо перевірити, що вектор [[1], [2]] є власним вектором, підставивши його назад:</p>

\[\begin{split}
\begin{bmatrix}
0 &amp; 2 \\
2 &amp; 3 \\
\end{bmatrix}
\begin{bmatrix}
1\\2\\
\end{bmatrix}
=\begin{bmatrix}
4\\8\\
\end{bmatrix}
=4\begin{bmatrix}
1\\2\\
\end{bmatrix}
\end{split}\]
<p>Підставивши <span>\(\lambda_2=-1\)</span> аналогічно до попереднього, ми можемо отримати інший власний вектор у такому вигляді, де <span>\(k_2 \neq 0\)</span>:
$<span>\(x_2 = k_2\begin{bmatrix}
-2\\1\\
\end{bmatrix}\)</span>$</p>
<p>З наведеного вище прикладу ми бачимо, як можна отримати власні значення та власні вектори з матриці <span>\(A\)</span>, і що вибір власних векторів для системи не є унікальним. Але все стає набагато складнішим, коли ви маєте справу з більшою матрицею <span>\(A\)</span> і намагаєтеся розв'язати характеристичне рівняння <span>\(n\)</span>-го степеня. На щастя, було розроблено багато різних чисельних методів для розв'язання задач на власні значення для великих матриць. У наступних двох розділах ми розглянемо степеневий метод та QR-метод.</p>
```
