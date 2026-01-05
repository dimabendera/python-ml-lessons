<h1>Обернення матриці<a href="#matrix-inversion" title="Постійне посилання на цей заголовок"></a></h1>
<p>Ми визначили, що обернена матриця для квадратної матриці <span>\(M\)</span> це матриця того ж розміру, <span>\(M^{-1}\)</span>, така, що <span>\(M \cdot M^{-1} = M^{-1} \cdot M = I\)</span>. Якщо розмірність матриці велика, аналітичне рішення для обернення матриці буде складним. Тому нам потрібні інші ефективні способи для знаходження оберненої матриці.</p>
<p>Використаємо <span>\(4 \times 4\)</span> матрицю для ілюстрації. Якщо ми маємо <span>\(M = \begin{bmatrix}
m_{1,1} &amp; m_{1,2} &amp; m_{1,3} &amp; m_{1,4}\\
m_{2,1} &amp; m_{2,2} &amp; m_{2,3} &amp; m_{2,4}\\
m_{3,1} &amp; m_{3,2} &amp; m_{3,3} &amp; m_{3,4} \\
m_{4,1} &amp; m_{4,2} &amp; m_{4,3} &amp; m_{4,4}
\end{bmatrix}\)</span>, і обернена до <span>\(M\)</span> є <span>\(X = \begin{bmatrix}
x_{1,1} &amp; x_{1,2} &amp; x_{1,3} &amp; x_{1,4}\\
x_{2,1} &amp; x_{2,2} &amp; x_{2,3} &amp; x_{2,4}\\
x_{3,1} &amp; x_{3,2} &amp; x_{3,3} &amp; x_{3,4} \\
x_{4,1} &amp; x_{4,2} &amp; x_{4,3} &amp; x_{4,4}
\end{bmatrix}\)</span>, тоді ми отримаємо:</p>

\[\begin{split}M \cdot X = \begin{bmatrix}
m_{1,1} &amp; m_{1,2} &amp; m_{1,3} &amp; m_{1,4}\\
m_{2,1} &amp; m_{2,2} &amp; m_{2,3} &amp; m_{2,4}\\
m_{3,1} &amp; m_{3,2} &amp; m_{3,3} &amp; m_{3,4} \\
m_{4,1} &amp; m_{4,2} &amp; m_{4,3} &amp; m_{4,4}
\end{bmatrix} \begin{bmatrix}
x_{1,1} &amp; x_{1,2} &amp; x_{1,3} &amp; x_{1,4}\\
x_{2,1} &amp; x_{2,2} &amp; x_{2,3} &amp; x_{2,4}\\
x_{3,1} &amp; x_{3,2} &amp; x_{3,3} &amp; x_{3,4} \\
x_{4,1} &amp; x_{4,2} &amp; x_{4,3} &amp; x_{4,4}
\end{bmatrix} = \begin{bmatrix}
1 &amp; 0 &amp; 0 &amp; 0\\
0 &amp; 1 &amp; 0 &amp; 0\\
0 &amp; 0 &amp; 1 &amp; 0\\
0 &amp; 0 &amp; 0 &amp; 1
\end{bmatrix}\end{split}\]
<p>Ми можемо переписати вищезгадане рівняння у чотири окремі рівняння, наприклад:</p>

\[\begin{split}
\begin{bmatrix}
m_{1,1} &amp; m_{1,2} &amp; m_{1,3} &amp; m_{1,4}\\
m_{2,1} &amp; m_{2,2} &amp; m_{2,3} &amp; m_{2,4}\\
m_{3,1} &amp; m_{3,2} &amp; m_{3,3} &amp; m_{3,4} \\
m_{4,1} &amp; m_{4,2} &amp; m_{4,3} &amp; m_{4,4}
\end{bmatrix}\left[\begin{array}{c} x_{1,1} \\x_{2,1} \\ x_{3,1} \\x_{4,1} \end{array}\right] =
\left[\begin{array}{c} 1\\0 \\0 \\0 \end{array}\right]\end{split}\]

\[\begin{split}
\begin{bmatrix}
m_{1,1} &amp; m_{1,2} &amp; m_{1,3} &amp; m_{1,4}\\
m_{2,1} &amp; m_{2,2} &amp; m_{2,3} &amp; m_{2,4}\\
m_{3,1} &amp; m_{3,2} &amp; m_{3,3} &amp; m_{3,4} \\
m_{4,1} &amp; m_{4,2} &amp; m_{4,3} &amp; m_{4,4}
\end{bmatrix}\left[\begin{array}{c} x_{1,2} \\x_{2,2} \\ x_{3,2} \\x_{4,2} \end{array}\right] =
\left[\begin{array}{c} 0\\1 \\0 \\0 \end{array}\right]\end{split}\]

\[\begin{split}
\begin{bmatrix}
m_{1,1} &amp; m_{1,2} &amp; m_{1,3} &amp; m_{1,4}\\
m_{2,1} &amp; m_{2,2} &amp; m_{2,3} &amp; m_{2,4}\\
m_{3,1} &amp; m_{3,2} &amp; m_{3,3} &amp; m_{3,4} \\
m_{4,1} &amp; m_{4,2} &amp; m_{4,3} &amp; m_{4,4}
\end{bmatrix}\left[\begin{array}{c} x_{1,3} \\x_{2,3} \\ x_{3,3} \\x_{4,3} \end{array}\right] =
\left[\begin{array}{c} 0\\0 \\1 \\0 \end{array}\right]\end{split}\]

\[\begin{split}
\begin{bmatrix}
m_{1,1} &amp; m_{1,2} &amp; m_{1,3} &amp; m_{1,4}\\
m_{2,1} &amp; m_{2,2} &amp; m_{2,3} &amp; m_{2,4}\\
m_{3,1} &amp; m_{3,2} &amp; m_{3,3} &amp; m_{3,4} \\
m_{4,1} &amp; m_{4,2} &amp; m_{4,3} &amp; m_{4,4}
\end{bmatrix}\left[\begin{array}{c} x_{1,4} \\x_{2,4} \\ x_{3,4} \\x_{4,4} \end{array}\right] =
\left[\begin{array}{c} 0\\0 \\0 \\1 \end{array}\right]\end{split}\]
<p>Отже, якщо ми розв'яжемо вищезгадані чотири системи рівнянь, ми отримаємо обернену матрицю. Ми можемо використовувати будь-який метод, який ми розглядали раніше для розв'язання цих рівнянь, такий як метод Гауса, метод Гауса-Жордана та LU-розклад. Тут ми просто покажемо приклад обернення матриці за допомогою методу Гауса-Жордана.</p>
<p>Нагадаємо, що в методі Гауса-Жордана ми перетворюємо нашу задачу з</p>

\[\begin{split}
\begin{bmatrix}
m_{1,1} &amp; m_{1,2} &amp; m_{1,3} &amp; m_{1,4}\\
m_{2,1} &amp; m_{2,2} &amp; m_{2,3} &amp; m_{2,4}\\
m_{3,1} &amp; m_{3,2} &amp; m_{3,3} &amp; m_{3,4} \\
m_{4,1} &amp; m_{4,2} &amp; m_{4,3} &amp; m_{4,4}
\end{bmatrix}\left[\begin{array}{c} x_1 \\x_2 \\ x_3 \\x_4 \end{array}\right] =
\left[\begin{array}{c} y_1 \\y_2 \\ y_3 \\y_4 \end{array}\right]\end{split}\]
<p>на</p>

\[\begin{split}
\begin{bmatrix}
1 &amp; 0 &amp; 0 &amp; 0\\
0 &amp; 1 &amp; 0 &amp; 0\\
0 &amp; 0 &amp; 1 &amp; 0\\
0 &amp; 0 &amp; 0 &amp; 1
\end{bmatrix} \left[\begin{array}{c} x_1 \\x_2 \\ x_3 \\x_4 \end{array}\right] =
\left[\begin{array}{c} y_1' \\y_2' \\ y_3' \\y_4' \end{array}\right]\end{split}\]
<p>і отримуємо розв'язок. По суті, ми перетворюємо</p>

\[\begin{split}
\begin{bmatrix}
m_{1,1} &amp; m_{1,2} &amp; m_{1,3} &amp; m_{1,4} &amp; y_1\\
m_{2,1} &amp; m_{2,2} &amp; m_{2,3} &amp; m_{2,4} &amp; y_2\\
m_{3,1} &amp; m_{3,2} &amp; m_{3,3} &amp; m_{3,4} &amp; y_3 \\
m_{4,1} &amp; m_{4,2} &amp; m_{4,3} &amp; m_{4,4} &amp; y_4
\end{bmatrix}
\end{split}\]
<p>на</p>

\[\begin{split}
\begin{bmatrix}
1 &amp; 0 &amp; 0 &amp; 0 &amp; y_1'\\
0 &amp; 1 &amp; 0 &amp; 0 &amp; y_2'\\
0 &amp; 0 &amp; 1 &amp; 0 &amp; y_3'\\
0 &amp; 0 &amp; 0 &amp; 1 &amp; y_4'
\end{bmatrix}
\end{split}\]
<p>Узагальнимо це тут: все, що нам потрібно зробити, це перетворити</p>

\[\begin{split}
\begin{bmatrix}
m_{1,1} &amp; m_{1,2} &amp; m_{1,3} &amp; m_{1,4} &amp; 1 &amp; 0 &amp; 0 &amp; 0\\
m_{2,1} &amp; m_{2,2} &amp; m_{2,3} &amp; m_{2,4} &amp; 0 &amp; 1 &amp; 0 &amp; 0\\
m_{3,1} &amp; m_{3,2} &amp; m_{3,3} &amp; m_{3,4} &amp; 0 &amp; 0 &amp; 1 &amp; 0\\
m_{4,1} &amp; m_{4,2} &amp; m_{4,3} &amp; m_{4,4} &amp; 0 &amp; 0 &amp; 0 &amp; 1
\end{bmatrix}
\end{split}\]
<p>на</p>

\[\begin{split}
\begin{bmatrix}
1 &amp; 0 &amp; 0 &amp; 0 &amp; m_{1,1}' &amp; m_{1,2}' &amp; m_{1,3}' &amp; m_{1,4}'\\
0 &amp; 1 &amp; 0 &amp; 0 &amp; m_{2,1}' &amp; m_{2,2}' &amp; m_{2,3}' &amp; m_{2,4}'\\
0 &amp; 0 &amp; 1 &amp; 0 &amp; m_{3,1}' &amp; m_{3,2}' &amp; m_{3,3}' &amp; m_{1,4}'\\
0 &amp; 0 &amp; 0 &amp; 1 &amp; m_{4,1}' &amp; m_{4,2}' &amp; m_{4,3}' &amp; m_{1,4}'
\end{bmatrix}
\end{split}\]
<p>Тоді матриця</p>

\[\begin{split}
\begin{bmatrix}
 m_{1,1}' &amp; m_{1,2}' &amp; m_{1,3}' &amp; m_{1,4}'\\
 m_{2,1}' &amp; m_{2,2}' &amp; m_{2,3}' &amp; m_{2,4}'\\
 m_{3,1}' &amp; m_{3,2}' &amp; m_{3,3}' &amp; m_{1,4}'\\
 m_{4,1}' &amp; m_{4,2}' &amp; m_{4,3}' &amp; m_{1,4}'
\end{bmatrix}
\end{split}\]
<p>є оберненою до <span>\(M\)</span>, яку ми шукаємо.</p>
<p>Чи можете ви пояснити, як використовувати LU-розклад для знаходження оберненої матриці?</p>
