<h1>Системи лінійних рівнянь<a href="#systems-of-linear-equations" title="Постійне посилання на цей заголовок"></a></h1>
<p><span>\(\textbf{Лінійне рівняння}\)</span> — це рівність вигляду
$<span>\(
\sum_{i = 1}^{n} (a_i x_i) = y,
\)</span><span>\(
де \)</span>a_i<span>\( є скалярами, \)</span>x_i<span>\( є невідомими змінними в \)</span>\mathbb{R}<span>\(, а \)</span>y$ є скаляром.</p>
<p><strong>СПРОБУЙТЕ!</strong> Визначте, яке з наступних рівнянь є лінійним, а яке ні. Для тих, що не є лінійними, чи можете ви маніпулювати ними так, щоб вони стали лінійними?</p>
<ol>
<li><p><span>\(3x_1 + 4x_2 - 3 = -5x_3\)</span></p></li>
<li><p><span>\(\frac{-x_1 + x_2}{x_3} = 2\)</span></p></li>
<li><p><span>\(x_1x_2 + x_3 = 5\)</span></p></li>
</ol>
<p>Рівняння 1 можна перегрупувати до вигляду <span>\(3x_1 + 4x_2 + 5x_3= 3\)</span>, яке
чітко має форму лінійного рівняння. Рівняння 2 не є лінійним,
але його можна перегрупувати до вигляду <span>\(-x_1 + x_2 - 2x_3 = 0\)</span>, яке є
лінійним. Рівняння 3 не є лінійним.</p>
<p><span>\(\textbf{Система лінійних рівнянь}\)</span> — це набір лінійних рівнянь, які мають спільні змінні. Розглянемо наступну систему лінійних рівнянь:</p>

\[\begin{eqnarray*}
\begin{array}{rcrcccccrcc}
a_{1,1} x_1 &amp;+&amp; a_{1,2} x_2 &amp;+&amp; {\ldots}&amp; +&amp; a_{1,n-1} x_{n-1} &amp;+&amp;a_{1,n} x_n &amp;=&amp; y_1,\\
a_{2,1} x_1 &amp;+&amp; a_{2,2} x_2 &amp;+&amp;{\ldots}&amp; +&amp; a_{2,n-1} x_{n-1} &amp;+&amp; a_{2,n} x_n &amp;=&amp; y_2, \\
&amp;&amp;&amp;&amp;{\ldots} &amp;&amp;{\ldots}&amp;&amp;&amp;&amp; \\
a_{m-1,1}x_1 &amp;+&amp; a_{m-1,2}x_2&amp;+ &amp;{\ldots}&amp; +&amp; a_{m-1,n-1} x_{n-1} &amp;+&amp; a_{m-1,n} x_n &amp;=&amp; y_{m-1},\\
a_{m,1} x_1 &amp;+&amp; a_{m,2}x_2 &amp;+ &amp;{\ldots}&amp; +&amp; a_{m,n-1} x_{n-1} &amp;+&amp; a_{m,n} x_n &amp;=&amp; y_{m}.
\end{array}
\end{eqnarray*}\]
<p>де <span>\(a_{i,j}\)</span> та <span>\(y_i\)</span> є дійсними числами. <span>\(\textbf{Матрична форма}\)</span> системи лінійних рівнянь — це <span>\(\textbf{\)</span>Ax = y<span>\(}\)</span>, де <span>\(A\)</span> — це матриця розміром <span>\({m} \times {n}\)</span>, <span>\(A(i,j) = a_{i,j}, y\)</span> — це вектор у <span>\({\mathbb{R}}^m\)</span>, а <span>\(x\)</span> — невідомий вектор у <span>\({\mathbb{R}}^n\)</span>. Матрична форма показана нижче:</p>

\[\begin{split}\begin{bmatrix}
a_{1,1} &amp; a_{1,2} &amp; ... &amp; a_{1,n}\\
a_{2,1} &amp; a_{2,2} &amp; ... &amp; a_{2,n}\\
... &amp; ... &amp; ... &amp; ... \\
a_{m,1} &amp; a_{m,2} &amp; ... &amp; a_{m,n}
\end{bmatrix}\left[\begin{array}{c} x_1 \\x_2 \\ ... \\x_n \end{array}\right] =
\left[\begin{array}{c} y_1 \\y_2 \\ ... \\y_m \end{array}\right]\end{split}\]
<p>Якщо ви виконаєте множення матриць, то побачите, що повернетеся до початкової системи рівнянь.</p>
<p><strong>СПРОБУЙТЕ!</strong> Запишіть наступну систему рівнянь у матричній формі.</p>

\[\begin{eqnarray*}
4x + 3y - 5z &amp;=&amp; 2 \\
-2x - 4y + 5z &amp;=&amp; 5 \\
7x + 8y   &amp;=&amp; -3 \\
x   + 2z &amp;=&amp; 1  \\
9 + y - 6z &amp;=&amp; 6 \\
\end{eqnarray*}\]

\[\begin{split}\begin{bmatrix}
4 &amp; 3 &amp; -5\\
-2 &amp; -4 &amp; 5\\
7 &amp; 8 &amp; 0\\
1 &amp; 0 &amp; 2\\
9 &amp; 1 &amp; -6
\end{bmatrix}\left[\begin{array}{c} x \\y \\z \end{array}\right] =
\left[\begin{array}{c} 2 \\5 \\-3 \\1 \\6 \end{array}\right]\end{split}\]
