<h1>Розв'язки систем лінійних рівнянь<a href="#solutions-to-systems-of-linear-equations" title="Постійне посилання на цей заголовок"></a></h1>
<p>Розглянемо систему лінійних рівнянь у матричній формі, <span>\(Ax=y\)</span>, де <span>\(A\)</span> — матриця розміром <span>\(m \times n\)</span>. Нагадаємо, що це означає, що в нашій системі є <span>\(m\)</span> рівнянь та <span>\(n\)</span> невідомих. <strong>Розв'язком</strong> системи лінійних рівнянь є <span>\(x\)</span> в <span>\({\mathbb{R}}^n\)</span>, що задовольняє матричне рівняння. Залежно від значень, що заповнюють <span>\(A\)</span> та <span>\(y\)</span>, існують три різні можливості розв'язку для <span>\(x\)</span>. Або немає розв'язку для <span>\(x\)</span>, або є один, унікальний розв'язок для <span>\(x\)</span>, або існує нескінченна кількість розв'язків для <span>\(x\)</span>. Цей факт не демонструється в цьому тексті.</p>
<p><strong>Випадок 1: Немає розв'язку для <span>\(x\)</span>.</strong> Якщо <span>\({rank}([A,y]) = {rank}(A) + 1\)</span>, то <span>\(y\)</span> лінійно незалежний від стовпців <span>\(A\)</span>. Отже, <span>\(y\)</span> не належить до образу <span>\(A\)</span>, і за визначенням не може існувати <span>\(x\)</span>, що задовольняє рівняння. Таким чином, порівняння рангу(<span>\([A,y]\)</span>) та рангу(<span>\(A\)</span>) надає простий спосіб перевірити, чи немає розв'язків у системі лінійних рівнянь.</p>
<p><strong>Випадок 2: Існує єдиний розв'язок для <span>\(x\)</span>.</strong> Якщо <span>\({rank}([A,y]) = {rank}(A)\)</span>, то <span>\(y\)</span> може бути записаний як лінійна комбінація стовпців <span>\(A\)</span>, і існує принаймні один розв'язок для матричного рівняння. Щоб існував лише один розв'язок, також має виконуватися <span>\({rank}(A) = n\)</span>. Іншими словами, кількість рівнянь повинна бути точно дорівнювати кількості невідомих. Щоб зрозуміти, чому ця властивість призводить до єдиного розв'язку, розглянемо наступні три співвідношення між <span>\(m\)</span> та <span>\(n: m &lt; n, m = n\)</span>, та <span>\(m > n\)</span>.</p>
<ul>
<li><p>У випадку, коли <span>\(m < n\)</span>, <span>\({rank}(A) = n\)</span> не може бути істинним, оскільки це означає, що ми маємо "широку" матрицю з меншою кількістю рівнянь, ніж невідомих. Отже, нам не потрібно розглядати цей підрозділ.</p></li>
<li><p>Коли <span>\(m = n\)</span> і <span>\({rank}(A) = n\)</span>, тоді <span>\(A\)</span> є квадратною та оборотною. Оскільки обернена матриця є унікальною, то матричне рівняння <span>\(Ax = y\)</span> можна розв'язати, помноживши кожну сторону рівняння зліва на <span>\(A^{-1}\)</span>. Це призводить до <span>\(A^{-1}Ax = A^{-1}y\rightarrow Ix = A^{-1}y\rightarrow x = A^{-1}y\)</span>, що дає єдиний розв'язок рівняння.</p></li>
<li><p>Якщо <span>\(m > n\)</span>, то рівнянь більше, ніж невідомих. Однак, якщо <span>\({rank}(A) = n\)</span>, то можна вибрати <span>\(n\)</span> рівнянь (тобто рядків A) таким чином, що якщо ці рівняння задовольняються, то решта <span>\(m - n\)</span> рівнянь також будуть задоволені. Іншими словами, вони є надлишковими. Якщо <span>\(m-n\)</span> надлишкових рівнянь видалити з системи, то отримана система матиме матрицю <span>\(A\)</span> розміром <span>\(n \times n\)</span>, яка є оборотною. Ці факти не доведені в цьому тексті. Нова система тоді матиме єдиний розв'язок, який є дійсним для всієї системи.</p></li>
</ul>
<p><strong>Випадок 3: Існує нескінченна кількість розв'язків для <span>\(x\)</span>.</strong> Якщо <span>\({rank}([A, y]) = {rank}(A)\)</span>, то <span>\(y\)</span> належить до образу <span>\(A\)</span>, і існує принаймні один розв'язок для матричного рівняння. Однак, якщо ранг(<span>\(A\)</span>) <span>\(&lt;\)</span> <span>\(n\)</span>, то існує нескінченна кількість розв'язків. Причина цього факту така: хоча тут це не показано, якщо ранг(<span>\(A\)</span>) <span>\(&lt;\)</span> <span>\(n\)</span>, то існує принаймні один ненульовий вектор <span>\(n\)</span>, який знаходиться в нуль-просторі <span>\(A\)</span> (Насправді, за цих умов існує нескінченна кількість векторів нуль-простору). Якщо <span>\(n\)</span> знаходиться в нуль-просторі <span>\(A\)</span>, то за визначенням <span>\(An = 0\)</span>. Тепер нехай <span>\(x^{{\ast}}\)</span> буде розв'язком матричного рівняння <span>\(Ax = y\)</span>; тоді обов'язково <span>\(Ax^{{\ast}} = y\)</span>. Однак, <span>\(Ax^{{\ast}} + An = y\)</span> або <span>\(A(x^{{\ast}} + n) = y\)</span>. Отже, <span>\(x^{{\ast}} + n\)</span> також є розв'язком для <span>\(Ax = y\)</span>. Насправді, оскільки <span>\(A\)</span> є лінійним перетворенням, <span>\(x^{{\ast}} + \alpha n\)</span> є розв'язком для будь-якого дійсного числа <span>\(\alpha\)</span> (спробуйте показати це самостійно). Оскільки існує нескінченна кількість допустимих значень для <span>\(\alpha\)</span>, існує нескінченна кількість розв'язків для матричного рівняння.</p>
<p>У решті розділу ми обговоримо лише те, як розв'язувати системи рівнянь, коли вони мають єдиний розв'язок. У цьому розділі ми обговоримо деякі поширені методи, з якими ви часто стикаєтеся у своїй роботі. А в наступному розділі ми покажемо, як розв'язувати їх у Python.</p>
<p>Припустимо, ми маємо n рівнянь з n змінними, <span>\(Ax=y\)</span>, як показано нижче:</p>

\[\begin{split}\begin{bmatrix}
a_{1,1} &amp; a_{1,2} &amp; ... &amp; a_{1,n}\\
a_{2,1} &amp; a_{2,2} &amp; ... &amp; a_{2,n}\\
... &amp; ... &amp; ... &amp; ... \\
a_{n,1} &amp; a_{n,2} &amp; ... &amp; a_{n,n}
\end{bmatrix}\left[\begin{array}{c} x_1 \\x_2 \\ ... \\x_n \end{array}\right] =
\left[\begin{array}{c} y_1 \\y_2 \\ ... \\y_n \end{array}\right]\end{split}\]

<h2>Метод Гаусса<a href="#gauss-elimination-method" title="Постійне посилання на цей заголовок"></a></h2>
<p><strong>Метод Гаусса</strong> — це процедура перетворення матриці <span>\(A\)</span> на <strong>верхню трикутну</strong> форму для розв'язання системи рівнянь. Використаємо систему з 4 рівнянь та 4 змінних, щоб проілюструвати ідею. Метод Гаусса по суті перетворює систему рівнянь на:</p>

\[\begin{split}\begin{bmatrix}
a_{1,1} &amp; a_{1,2} &amp; a_{1,3} &amp; a_{1,4}\\
0 &amp; a_{2,2}' &amp; a_{2,3}' &amp; a_{2,4}'\\
0 &amp; 0 &amp; a_{3,3}' &amp; a_{3,4}' \\
0 &amp; 0 &amp; 0 &amp; a_{4,4}'
\end{bmatrix}\left[\begin{array}{c} x_1 \\x_2 \\ x_3 \\x_4 \end{array}\right] =
\left[\begin{array}{c} y_1 \\y_2' \\ y_3' \\y_4' \end{array}\right]\end{split}\]
<p>Перетворивши матричну форму на таку, ми бачимо, що рівняння перетворюються на:</p>

\[\begin{eqnarray*}
\begin{array}{}
 a_{1,1} x_1 &amp;+&amp; a_{1,2} x_2 &amp; + &amp; a_{1,3} x_{3} &amp;+&amp;a_{1,4} x_4 &amp;=&amp; y_1,\\
&amp; &amp; a_{2,2}' x_{2} &amp;+ &amp; a_{2,3}' x_{3} &amp;+&amp; a_{2,4}' x_4 &amp;=&amp; y_{2}' \\
&amp;&amp; &amp; &amp; a_{3,3}' x_{3} &amp;+&amp; a_{3,4}' x_4 &amp;=&amp; y_{3}',\\
&amp;&amp; &amp;&amp; &amp;&amp; a_{4,4}' x_4 &amp;=&amp; y_{4}'.
\end{array}
\end{eqnarray*}\]
<p>Ми бачимо, що, перетворивши на цю форму, <span>\(x_4\)</span> можна легко розв'язати, поділивши обидві сторони на <span>\(a_{4,4}'\)</span>, потім ми можемо підставити його назад у 3-тє рівняння, щоб розв'язати <span>\(x_3\)</span>. Маючи <span>\(x_3\)</span> та <span>\(x_4\)</span>, ми можемо підставити їх у 2-ге рівняння, щоб розв'язати <span>\(x_2\)</span>. Нарешті, ми можемо отримати всі розв'язки для <span>\(x\)</span>. Ми розв'язуємо систему рівнянь знизу вгору, це називається <strong>зворотна підстановка</strong>. Зауважте, що якщо <span>\(A\)</span> є нижньою трикутною матрицею, ми б розв'язували систему зверху вниз за допомогою <strong>прямої підстановки</strong>.</p>
<p>Розглянемо приклад, щоб проілюструвати, як ми розв'язуємо рівняння за допомогою методу Гаусса.</p>
<p><strong>СПРОБУЙТЕ!</strong> Використайте метод Гаусса для розв'язання наступних рівнянь.</p>

\[\begin{eqnarray*}
4x_1 + 3x_2 - 5x_3 &amp;=&amp; 2 \\
-2x_1 - 4x_2 + 5x_3 &amp;=&amp; 5 \\
8x_1 + 8x_2  &amp;=&amp; -3 \\
\end{eqnarray*}\]
<p>Крок 1: Перетворіть ці рівняння на матричну форму <span>\(Ax=y\)</span>.</p>

\[\begin{split}
\begin{bmatrix}
4 &amp; 3 &amp; -5\\
-2 &amp; -4 &amp; 5\\
8 &amp; 8 &amp; 0\\
\end{bmatrix}\left[\begin{array}{c} x_1 \\x_2 \\x_3 \end{array}\right] =
\left[\begin{array}{c} 2 \\5 \\-3\end{array}\right]\end{split}\]
<p>Крок 2: Отримайте розширену матрицю [A, y]</p>

\[\begin{split}
[A, y]  = \begin{bmatrix}
4 &amp; 3 &amp; -5 &amp; 2\\
-2 &amp; -4 &amp; 5 &amp; 5\\
8 &amp; 8 &amp; 0 &amp; -3\\
\end{bmatrix}\end{split}\]
<p>Крок 3: Тепер ми починаємо виключати елементи в матриці, робимо це, вибираючи <strong>опорне рівняння</strong>, яке використовується для виключення елементів в інших рівняннях. Виберемо перше рівняння як опорне і перетворимо перший елемент 2-го рядка на 0. Для цього ми можемо помножити 1-й рядок (опорне рівняння) на -0.5 і відняти його від 2-го рядка. Множник дорівнює <span>\(m_{2,1}=-0.5\)</span>. Отримаємо:</p>

\[\begin{split}
\begin{bmatrix}
4 &amp; 3 &amp; -5 &amp; 2\\
0 &amp; -2.5 &amp; 2.5 &amp; 6\\
8 &amp; 8 &amp; 0 &amp; -3\\
\end{bmatrix}\end{split}\]
<p>Крок 4: Перетворіть перший елемент 3-го рядка на 0. Ми можемо зробити щось подібне: помножити 1-й рядок на 2 і відняти його від 3-го рядка. Множник дорівнює <span>\(m_{3,1}=2\)</span>. Отримаємо:</p>

\[\begin{split}
\begin{bmatrix}
4 &amp; 3 &amp; -5 &amp; 2\\
0 &amp; -2.5 &amp; 2.5 &amp; 6\\
0 &amp; 2 &amp; 10 &amp; -7\\
\end{bmatrix}\end{split}\]
<p>Крок 5: Перетворіть другий елемент 3-го рядка на 0. Ми можемо помножити 2-й рядок на -4/5 і відняти його від 3-го рядка. Множник дорівнює <span>\(m_{3,2}=-0.8\)</span>. Отримаємо:</p>

\[\begin{split}
\begin{bmatrix}
4 &amp; 3 &amp; -5 &amp; 2\\
0 &amp; -2.5 &amp; 2.5 &amp; 6\\
0 &amp; 0 &amp; 12 &amp; -2.2\\
\end{bmatrix}\end{split}\]
<p>Крок 6: Отже, ми отримуємо <span>\(x_3=-2.2/12=-0.183\)</span>.</p>
<p>Крок 7: Підставивши <span>\(x_3\)</span> у 2-ге рівняння, отримуємо <span>\(x_2=-2.583\)</span></p>
<p>Крок 8: Підставивши <span>\(x_2\)</span> та <span>\(x_3\)</span> у перше рівняння, отримуємо <span>\(x_1=2.208\)</span>.</p>
<p><strong>Примітка!</strong> Іноді перший елемент у 1-му рядку може бути 0, просто поміняйте місцями перший рядок з рядком, що має ненульовий перший елемент, тоді ви зможете виконати ту ж процедуру, що й вище.</p>
<p>Тут ми використовуємо метод Гаусса з "вибором опорного елемента", але ви повинні знати, що існує також "наївний" метод Гаусса з припущенням, що опорні значення ніколи не будуть нульовими.</p>


<h2>Метод Гаусса-Жордана<a href="#gauss-jordan-elimination-method" title="Постійне посилання на цей заголовок"></a></h2>
<p>Метод Гаусса-Жордана розв'язує системи рівнянь за допомогою процедури перетворення <span>\(A\)</span> на діагональну форму, так що матрична форма рівнянь стає</p>

\[\begin{split}\begin{bmatrix}
1 &amp; 0 &amp; 0 &amp; 0\\
0 &amp; 1 &amp; 0 &amp; 0\\
0 &amp; 0 &amp; 1 &amp; 0 \\
0 &amp; 0 &amp; 0 &amp; 1
\end{bmatrix}\left[\begin{array}{c} x_1 \\x_2 \\ x_3 \\x_4 \end{array}\right] =
\left[\begin{array}{c} y_1' \\y_2' \\ y_3' \\y_4' \end{array}\right]\end{split}\]
<p>По суті, рівняння стають:</p>

\[\begin{eqnarray*}
\begin{array}{}
x_1 &amp;+&amp; 0 &amp; + &amp; 0 &amp;+&amp;0 &amp;=&amp; y_1',\\
0 &amp;+&amp; x_2 &amp; + &amp; 0 &amp;+&amp;0 &amp;=&amp; y_2' \\
0 &amp;+&amp; 0 &amp; + &amp; x_3 &amp;+&amp;0 &amp;=&amp; y_3',\\
0 &amp;+&amp; 0 &amp; + &amp; 0 &amp;+&amp;x_4 &amp;=&amp; y_4'.
\end{array}
\end{eqnarray*}\]
<p>Давайте все ж подивимося, як ми можемо це зробити, використовуючи наведений вище приклад.</p>
<p><strong>СПРОБУЙТЕ!</strong> Використайте метод Гаусса-Жордана для розв'язання наступних рівнянь.</p>

\[\begin{eqnarray*}
4x_1 + 3x_2 - 5x_3 &amp;=&amp; 2 \\
-2x_1 - 4x_2 + 5x_3 &amp;=&amp; 5 \\
8x_1 + 8x_2  &amp;=&amp; -3 \\
\end{eqnarray*}\]
<p>Крок 1: Отримайте розширену матрицю [A, y]</p>

\[\begin{split}
[A, y]  = \begin{bmatrix}
4 &amp; 3 &amp; -5 &amp; 2\\
-2 &amp; -4 &amp; 5 &amp; 5\\
8 &amp; 8 &amp; 0 &amp; -3\\
\end{bmatrix}\end{split}\]
<p>Крок 2: Перетворіть перший елемент у 1-му рядку на 1, для цього ділимо рядок на 4:
$$</p>

<span>(6)<a href="#equation-cf990690-b946-4d40-bc52-3d8a8dfee0ba" title="Постійне посилання на це рівняння"></a></span>\[\begin{bmatrix}
1 &amp; 3/4 &amp; -5/4 &amp; 1/2\\
-2 &amp; -4 &amp; 5 &amp; 5\\
8 &amp; 8 &amp; 0 &amp; -3\\
\end{bmatrix}\]
<p>Крок 3: Виключіть перший елемент у 2-му та 3-му рядках, для цього помножимо 1-й рядок на -2 та 8 відповідно і віднімемо його від 2-го та 3-го рядків.</p>

\[\begin{split}
\begin{bmatrix}
1 &amp; 3/4 &amp; -5/4 &amp; 1/2\\
0 &amp; -5/2 &amp; 5/2 &amp; 6\\
0 &amp; 2 &amp; 10 &amp; -7\\
\end{bmatrix}\end{split}\]
<p>Крок 4: Нормалізуйте 2-й елемент у 2-му рядку до 1, для цього ділимо на -5/2.</p>

\[\begin{split}
\begin{bmatrix}
1 &amp; 3/4 &amp; -5/4 &amp; 1/2\\
0 &amp; 1 &amp; -1 &amp; -12/5\\
0 &amp; 2 &amp; 10 &amp; -7\\
\end{bmatrix}\end{split}\]
<p>Крок 5: Виключіть 2-й елемент у 3-му рядку, для цього помножимо 2-й рядок на 2 і віднімемо його від 3-го рядка.</p>

\[\begin{split}
\begin{bmatrix}
1 &amp; 3/4 &amp; -5/4 &amp; 1/2\\
0 &amp; 1 &amp; -1 &amp; -12/5\\
0 &amp; 0 &amp; 12 &amp; -11/5\\
\end{bmatrix}\end{split}\]
<p>Крок 6: Нормалізуйте останній рядок, поділивши на 8.</p>

\[\begin{split}
\begin{bmatrix}
1 &amp; 3/4 &amp; -5/4 &amp; 1/2\\
0 &amp; 1 &amp; -1 &amp; -12/5\\
0 &amp; 0 &amp; 1 &amp; -11/60\\
\end{bmatrix}\end{split}\]
<p>Крок 7: Виключіть 3-й елемент у 2-му рядку, помноживши 3-й рядок на -1 і віднявши його від 2-го рядка.</p>

\[\begin{split}
\begin{bmatrix}
1 &amp; 3/4 &amp; -5/4 &amp; 1/2\\
0 &amp; 1 &amp; 0 &amp; -155/60\\
0 &amp; 0 &amp; 1 &amp; -11/60\\
\end{bmatrix}\end{split}\]
<p>Крок 8: Виключіть 3-й елемент у 1-му рядку, помноживши 3-й рядок на -5/4 і віднявши його від 1-го рядка.</p>

\[\begin{split}
\begin{bmatrix}
1 &amp; 3/4 &amp; 0 &amp; 13/48\\
0 &amp; 1 &amp; 0 &amp; -2.583\\
0 &amp; 0 &amp; 1 &amp; -0.183\\
\end{bmatrix}\end{split}\]
<p>Крок 9: Виключіть 2-й елемент у 1-му рядку, помноживши 2-й рядок на 3/4 і віднявши його від 1-го рядка.</p>

\[\begin{split}
\begin{bmatrix}
1 &amp; 0 &amp; 0 &amp; 2.208\\
0 &amp; 1 &amp; 0 &amp; -2.583\\
0 &amp; 0 &amp; 1 &amp; -0.183\\
\end{bmatrix}\end{split}\]


<h2>Метод LU-розкладу<a href="#lu-decomposition-method" title="Постійне посилання на цей заголовок"></a></h2>
<p>Ми бачимо, що вищезгадані два методи передбачають одночасне змінення як <span>\(A\)</span>, так і <span>\(y\)</span> при спробі перетворити A на верхню трикутну або діагональну матричну форму. Це вимагає багатьох операцій. Але іноді ми можемо мати один і той же набір рівнянь, але різні набори <span>\(y\)</span> для різних експериментів. Це досить поширено в реальному світі, коли ми маємо різні експериментальні спостереження <span>\(y_a, y_b, y_c, ...\)</span>. Тому нам доводиться розв'язувати <span>\(Ax=y_a\)</span>, <span>\(Ax=y_b\)</span>, … багато разів, оскільки щоразу <span>\([A, y]\)</span> буде змінюватися. Це дуже неефективно, чи існує метод, за якого ми змінюємо лише ліву сторону <span>\(A\)</span>, але не праву сторону <span>\(y\)</span>? Метод LU-розкладу є одним з рішень, при якому ми змінюємо лише матрицю <span>\(A\)</span> замість <span>\(y\)</span>. Він має переваги для розв'язання систем, які мають однакові матриці коефіцієнтів <span>\(A\)</span>, але різні вектори констант <span>\(y\)</span>.</p>
<p>Метод LU-розкладу має на меті перетворити <span>\(A\)</span> на добуток двох матриць <span>\(L\)</span> та <span>\(U\)</span>, де <span>\(L\)</span> є нижньою трикутною матрицею, а <span>\(U\)</span> — верхньою трикутною матрицею. Завдяки цьому розкладу ми перетворюємо систему рівнянь на наступну форму:</p>

\[\begin{split}LUx=y\rightarrow
\begin{bmatrix}
l_{1,1} &amp; 0 &amp; 0 &amp; 0\\
l_{2,1} &amp; l_{2,2} &amp; 0 &amp; 0\\
l_{3,1} &amp; l_{3,2} &amp; l_{3,3} &amp; 0 \\
l_{4,1} &amp; l_{4,2} &amp; l_{4,3} &amp; l_{4,4}
\end{bmatrix}
\begin{bmatrix}
u_{1,1} &amp; u_{1,2} &amp; u_{1,3} &amp; u_{1,4}\\
0 &amp; u_{2,2} &amp; u_{2,3} &amp; u_{2,4}\\
0 &amp; 0 &amp; u_{3,3} &amp; u_{3,4} \\
0 &amp; 0 &amp; 0 &amp; u_{4,4}
\end{bmatrix}\left[\begin{array}{c} x_1 \\x_2 \\ x_3 \\x_4 \end{array}\right] =
\left[\begin{array}{c} y_1 \\y_2 \\ y_3 \\y_4 \end{array}\right]\end{split}\]
<p>Якщо ми визначимо <span>\(Ux=M\)</span>, то вищезгадані рівняння стають:</p>

\[\begin{split}
\begin{bmatrix}
l_{1,1} &amp; 0 &amp; 0 &amp; 0\\
l_{2,1} &amp; l_{2,2} &amp; 0 &amp; 0\\
l_{3,1} &amp; l_{3,2} &amp; l_{3,3} &amp; 0 \\
l_{4,1} &amp; l_{4,2} &amp; l_{4,3} &amp; l_{4,4}
\end{bmatrix}M =
\left[\begin{array}{c} y_1 \\y_2 \\ y_3 \\y_4 \end{array}\right]\end{split}\]
<p>Ми можемо легко розв'язати вищезгадану задачу за допомогою прямої підстановки (протилежної зворотній підстановці, як ми бачили в методі Гаусса). Після того, як ми розв'яжемо M, ми можемо легко розв'язати решту задачі за допомогою зворотної підстановки:</p>

\[\begin{split}
\begin{bmatrix}
u_{1,1} &amp; u_{1,2} &amp; u_{1,3} &amp; u_{1,4}\\
0 &amp; u_{2,2} &amp; u_{2,3} &amp; u_{2,4}\\
0 &amp; 0 &amp; u_{3,3} &amp; u_{3,4} \\
0 &amp; 0 &amp; 0 &amp; u_{4,4}
\end{bmatrix}\left[\begin{array}{c} x_1 \\x_2 \\ x_3 \\x_4 \end{array}\right] =
\left[\begin{array}{c} m_1 \\m_2 \\ m_3 \\m_4 \end{array}\right]\end{split}\]
<p>Але як ми можемо обчислити та отримати матриці <span>\(L\)</span> та <span>\(U\)</span>? Існують різні способи отримання LU-розкладу, давайте розглянемо один спосіб, використовуючи метод Гаусса. З вищесказаного ми знаємо, що після проведення методу Гаусса ми отримуємо верхню трикутну матрицю. Але водночас ми також отримуємо нижню трикутну матрицю, просто ми ніколи не записуємо її явно. Під час процедури методу Гаусса матриця <span>\(A\)</span> фактично перетворюється на добуток двох матриць, як показано нижче. При цьому права верхня трикутна форма — це та, яку ми отримали раніше, а нижня трикутна матриця має одиниці на діагоналі та множники, які множать опорне рівняння для виключення елементів під час процедури, як елементи під діагоналлю.</p>

\[\begin{split}A=
\begin{bmatrix}
1 &amp; 0 &amp; 0 &amp; 0\\
m_{2,1} &amp; 1 &amp; 0 &amp; 0\\
m_{3,1} &amp; m_{3,2} &amp; 1 &amp; 0 \\
m_{4,1} &amp; m_{4,2} &amp; m_{4,3} &amp; 1
\end{bmatrix}
\begin{bmatrix}
u_{1,1} &amp; u_{1,2} &amp; u_{1,3} &amp; u_{1,4}\\
0 &amp; u_{2,2} &amp; u_{2,3} &amp; u_{2,4}\\
0 &amp; 0 &amp; u_{3,3} &amp; u_{3,4} \\
0 &amp; 0 &amp; 0 &amp; u_{4,4}
\end{bmatrix}\end{split}\]
<p>Ми бачимо, що ми можемо отримати як <span>\(L\)</span>, так і <span>\(U\)</span> одночасно, коли виконуємо метод Гаусса. Розглянемо вищезгаданий приклад, де <span>\(U\)</span> — це та, яку ми використовували раніше для розв'язання рівнянь, а <span>\(L\)</span> складається з множників (ви можете перевірити приклади в розділі "Метод Гаусса").</p>

\[\begin{split}
L = \begin{bmatrix}
1 &amp; 0 &amp; 0 \\
-0.5 &amp; 1 &amp; 0 \\
2 &amp; -0.8 &amp; 1 \\
\end{bmatrix}\end{split}\]

\[\begin{split}
U = \begin{bmatrix}
4 &amp; 3 &amp; -5 \\
0 &amp; -2.5 &amp; 2.5 \\
0 &amp; 0 &amp; 60 \\
\end{bmatrix}\end{split}\]
<p><strong>СПРОБУЙТЕ!</strong> Перевірте, чи є вищезгадані матриці <span>\(L\)</span> та <span>\(U\)</span> LU-розкладом матриці <span>\(A\)</span>. Ми повинні побачити, що <span>\(A=LU\)</span>.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>

<span>u</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>4</span><span>,</span> <span>3</span><span>,</span> <span>-</span><span>5</span><span>],</span> 
              <span>[</span><span>0</span><span>,</span> <span>-</span><span>2.5</span><span>,</span> <span>2.5</span><span>],</span> 
              <span>[</span><span>0</span><span>,</span> <span>0</span><span>,</span> <span>12</span><span>]])</span>
<span>l</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>1</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>],</span> 
              <span>[</span><span>-</span><span>0.5</span><span>,</span> <span>1</span><span>,</span> <span>0</span><span>],</span> 
              <span>[</span><span>2</span><span>,</span> <span>-</span><span>0.8</span><span>,</span> <span>1</span><span>]])</span>

<span>print</span><span>(</span><span>'LU='</span><span>,</span> <span>np</span><span>.</span><span>dot</span><span>(</span><span>l</span><span>,</span> <span>u</span><span>))</span>
</pre>



<pre><span></span>LU= [[ 4.  3. -5.]
 [-2. -4.  5.]
 [ 8.  8.  0.]]
</pre>





<h2>Ітераційні методи - Метод Гаусса-Зейделя<a href="#iterative-methods-gauss-seidel-method" title="Постійне посилання на цей заголовок"></a></h2>
<p>Вищезгадані методи, які ми представили, є прямими методами, в яких ми обчислюємо розв'язок за скінченну кількість операцій. У цьому розділі ми представимо інший клас методів: <strong>ітераційні методи</strong>, або <strong>непрямі методи</strong>. Вони починаються з початкового припущення щодо розв'язку, а потім багаторазово покращують розв'язок, доки зміна розв'язку не стане нижчою за поріг. Щоб використовувати цей ітераційний процес, нам спочатку потрібно записати явну форму системи рівнянь. Якщо ми маємо систему лінійних рівнянь:</p>

\[\begin{split}\begin{bmatrix}
a_{1,1} &amp; a_{1,2} &amp; ... &amp; a_{1,n}\\
a_{2,1} &amp; a_{2,2} &amp; ... &amp; a_{2,n}\\
... &amp; ... &amp; ... &amp; ... \\
a_{m,1} &amp; a_{m,2} &amp; ... &amp; a_{m,n}
\end{bmatrix}\left[\begin{array}{c} x_1 \\x_2 \\ ... \\x_n \end{array}\right] =
\left[\begin{array}{c} y_1 \\y_2 \\ ... \\y_m \end{array}\right]\end{split}\]
<p>ми можемо записати її явну форму як:</p>

\[
x_i = \frac{1}{a_{i,i}}\Big[y_i - \sum_{j=1, j \ne i}^{j=n}{a_{i,j}x_j} \Big]
\]
<p>Це основи ітераційних методів: ми можемо припустити початкові значення для всіх <span>\(x\)</span> і використовувати їх як <span>\(x^{(0)}\)</span>. У першій ітерації ми можемо підставити <span>\(x^{(0)}\)</span> у праву частину явного рівняння вище і отримати розв'язок першої ітерації <span>\(x^{(1)}\)</span>. Таким чином, ми можемо підставити <span>\(x^{(1)}\)</span> у рівняння і отримати <span>\(x^{(2)}\)</span>. Ітерації продовжуються, доки різниця між <span>\(x^{(k)}\)</span> та <span>\(x^{(k-1)}\)</span> не стане меншою за деяке заздалегідь визначене значення.</p>
<p>Щоб ітераційні методи працювали, нам потрібна конкретна умова для збіжності розв'язку. Достатньою, але не необхідною умовою збіжності є те, що матриця коефіцієнтів <span>\(a\)</span> є <strong>діагонально домінантною</strong>. Це означає, що в кожному рядку матриці коефіцієнтів <span>\(a\)</span> абсолютне значення діагонального елемента більше, ніж сума абсолютних значень недіагональних елементів. Якщо матриця коефіцієнтів задовольняє цю умову, ітерація зійдеться до розв'язку. Розв'язок може все ще збігатися, навіть якщо ця умова не виконується.</p>

<h3>Метод Гаусса-Зейделя<a href="#gauss-seidel-method" title="Постійне посилання на цей заголовок"></a></h3>
<p><strong>Метод Гаусса-Зейделя</strong> — це специфічний ітераційний метод, який завжди використовує останнє оцінене значення для кожного елемента в <span>\(x\)</span>. Наприклад, ми спочатку припускаємо початкові значення для <span>\(x_2, x_3, \cdots, x_n\)</span> (крім <span>\(x_1\)</span>), а потім можемо обчислити <span>\(x_1\)</span>. Використовуючи обчислене <span>\(x_1\)</span> та решту <span>\(x\)</span> (крім <span>\(x_2\)</span>), ми можемо обчислити <span>\(x_2\)</span>. Ми можемо продовжувати таким же чином і обчислити всі елементи в <span>\(x\)</span>. Це завершить першу ітерацію. Ми бачимо, що унікальність методу Гаусса-Зейделя полягає в тому, що ми завжди використовуємо останнє значення для обчислення наступного значення в <span>\(x\)</span>. Потім ми можемо продовжувати ітерації, доки значення не зійдеться. Використаємо цей метод для розв'язання тієї ж задачі, яку ми щойно розв'язали вище.</p>
<p><strong>ПРИКЛАД:</strong> Розв'яжіть наступну систему лінійних рівнянь за допомогою методу Гаусса-Зейделя, використовуючи заздалегідь визначений поріг <span>\(\epsilon = 0.01\)</span>. Не забудьте перевірити, чи виконується умова збіжності.</p>

\[\begin{eqnarray*}
8x_1 + 3x_2 - 3x_3 &amp;=&amp; 14 \\
-2x_1 - 8x_2 + 5x_3 &amp;=&amp; 5 \\
3x_1 + 5x_2 + 10x_3 &amp; =&amp; -8 \\
\end{eqnarray*}\]
<p>Давайте спочатку перевіримо, чи є матриця коефіцієнтів діагонально домінантною.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>

<span>a</span> <span>=</span> <span>[[</span><span>8</span><span>,</span> <span>3</span><span>,</span> <span>-</span><span>3</span><span>],</span> <span>[</span><span>-</span><span>2</span><span>,</span> <span>-</span><span>8</span><span>,</span> <span>5</span><span>],</span> <span>[</span><span>3</span><span>,</span> <span>5</span><span>,</span> <span>10</span><span>]]</span>

<span># Знайти діагональні коефіцієнти</span>
<span>diag</span> <span>=</span> <span>np</span><span>.</span><span>diag</span><span>(</span><span>np</span><span>.</span><span>abs</span><span>(</span><span>a</span><span>))</span> 

<span># Знайти суму рядка без діагоналі</span>
<span>off_diag</span> <span>=</span> <span>np</span><span>.</span><span>sum</span><span>(</span><span>np</span><span>.</span><span>abs</span><span>(</span><span>a</span><span>),</span> <span>axis</span><span>=</span><span>1</span><span>)</span> <span>-</span> <span>diag</span> 

<span>if</span> <span>np</span><span>.</span><span>all</span><span>(</span><span>diag</span> <span>&gt;</span> <span>off_diag</span><span>):</span>
    <span>print</span><span>(</span><span>'матриця є діагонально домінантною'</span><span>)</span>
<span>else</span><span>:</span>
    <span>print</span><span>(</span><span>'НЕ є діагонально домінантною'</span><span>)</span>
</pre>



<pre><span></span>матриця є діагонально домінантною
</pre>



<p>Оскільки гарантовано, що вона зійдеться, ми можемо використовувати метод Гаусса-Зейделя для її розв'язання.</p>


<pre><span></span><span>x1</span> <span>=</span> <span>0</span>
<span>x2</span> <span>=</span> <span>0</span>
<span>x3</span> <span>=</span> <span>0</span>
<span>epsilon</span> <span>=</span> <span>0.01</span>
<span>converged</span> <span>=</span> <span>False</span>

<span>x_old</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([</span><span>x1</span><span>,</span> <span>x2</span><span>,</span> <span>x3</span><span>])</span>

<span>print</span><span>(</span><span>'Результати ітерацій'</span><span>)</span>
<span>print</span><span>(</span><span>' k,    x1,    x2,    x3 '</span><span>)</span>
<span>for</span> <span>k</span> <span>in</span> <span>range</span><span>(</span><span>1</span><span>,</span> <span>50</span><span>):</span>
    <span>x1</span> <span>=</span> <span>(</span><span>14</span><span>-</span><span>3</span><span>*</span><span>x2</span><span>+</span><span>3</span><span>*</span><span>x3</span><span>)</span><span>/</span><span>8</span>
    <span>x2</span> <span>=</span> <span>(</span><span>5</span><span>+</span><span>2</span><span>*</span><span>x1</span><span>-</span><span>5</span><span>*</span><span>x3</span><span>)</span><span>/</span><span>(</span><span>-</span><span>8</span><span>)</span>
    <span>x3</span> <span>=</span> <span>(</span><span>-</span><span>8</span><span>-</span><span>3</span><span>*</span><span>x1</span><span>-</span><span>5</span><span>*</span><span>x2</span><span>)</span><span>/</span><span>(</span><span>-</span><span>5</span><span>)</span>
    <span>x</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([</span><span>x1</span><span>,</span> <span>x2</span><span>,</span> <span>x3</span><span>])</span>
    <span># перевірити, чи менше за поріг</span>
    <span>dx</span> <span>=</span> <span>np</span><span>.</span><span>sqrt</span><span>(</span><span>np</span><span>.</span><span>dot</span><span>(</span><span>x</span><span>-</span><span>x_old</span><span>,</span> <span>x</span><span>-</span><span>x_old</span><span>))</span>
    
    <span>print</span><span>(</span><span>"</span><span>%d</span><span>, </span><span>%.4f</span><span>, </span><span>%.4f</span><span>, </span><span>%.4f</span><span>"</span><span>%</span><span>(</span><span>k</span><span>,</span> <span>x1</span><span>,</span> <span>x2</span><span>,</span> <span>x3</span><span>))</span>
    <span>if</span> <span>dx</span> <span>&lt;</span> <span>epsilon</span><span>:</span>
        <span>converged</span> <span>=</span> <span>True</span>
        <span>print</span><span>(</span><span>'Зійшлося!'</span><span>)</span>
        <span>break</span>
        
    <span># присвоїти останнє значення x старому значенню</span>
    <span>x_old</span> <span>=</span> <span>x</span>

<span>if</span> <span>not</span> <span>converged</span><span>:</span>
    <span>print</span><span>(</span><span>'Не зійшлося, збільшіть кількість ітерацій'</span><span>)</span>
</pre>



<pre><span></span>Iteration results
 k,    x1,    x2,    x3 
1, 1.7500, -1.0625, 1.5875
2, 2.7437, -0.3188, 2.9275
3, 2.9673, 0.4629, 3.8433
4, 3.0177, 1.0226, 4.4332
5, 3.0290, 1.3885, 4.8059
6, 3.0315, 1.6208, 5.0397
7, 3.0321, 1.7668, 5.1861
8, 3.0322, 1.8582, 5.2776
9, 3.0322, 1.9154, 5.3348
10, 3.0323, 1.9512, 5.3705
11, 3.0323, 1.9735, 5.3929
12, 3.0323, 1.9875, 5.4068
13, 3.0323, 1.9962, 5.4156
14, 3.0323, 2.0017, 5.4210
Зійшлося!
</pre>
