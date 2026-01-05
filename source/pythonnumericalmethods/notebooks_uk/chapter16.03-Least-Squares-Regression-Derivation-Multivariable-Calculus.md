<h1>Виведення регресії методом найменших квадратів (Багатовимірне числення)<a href="#least-squares-regression-derivation-multivariable-calculus" title="Постійне посилання на цей заголовок"></a></h1>
<p>Нагадаємо, що загальна похибка для <span>\(m\)</span> точок даних та <span>\(n\)</span> базисних функцій становить:</p>

\[
E = \sum_{i=1}^m e_i^2 = \sum_{i=1}^m (\hat{y}(x_i) - y_i)^2 = \sum_{i=1}^m \left(\sum_{j=1}^n {\alpha}_j f_j(x_i) - y_i\right)^2.
\]
<p>що є <span>\(n\)</span>-вимірним параболоїдом у <span>\({\alpha}_k\)</span>. З числення ми знаємо, що мінімум параболоїда знаходиться там, де всі частинні похідні дорівнюють нулю. Отже, взяття часткової похідної <span>\(E\)</span> відносно змінної <span>\({\alpha}_k\)</span> (пам'ятайте, що в цьому випадку параметри є нашими змінними), прирівнювання системи рівнянь до 0 та розв'язання для <span>\({\alpha}_k\)</span> повинно дати правильні результати.</p>
<p>Часткова похідна відносно <span>\({\alpha}_k\)</span>, прирівняна до 0, дає:
$<span>\(
\frac{\partial E}{\partial {\alpha}_k} = \sum_{i=1}^m 2\left(\sum_{j=1}^n {\alpha}_j f_j(x_i) - y_i\right)f_k(x_i) = 0.
\)</span>$</p>
<p>Після деяких перетворень попередній вираз можна перетворити на наступний:
$<span>\(
\sum_{i=1}^m \sum_{j=1}^n {\alpha}_j f_j(x_i)f_k(x_i) - \sum_{i=1}^m y_i f_k(x_i) = 0,
\)</span>$</p>
<p>і подальше перетворення, що використовує властивість комутативності додавання, призводить до:
$<span>\(
\sum_{j=1}^n {\alpha}_j \sum_{i=1}^m f_j(x_i)f_k(x_i) = \sum_{i=1}^m y_i f_k(x_i).
\)</span><span>\(
Тепер нехай \)</span>X<span>\( буде вектор-стовпцем, такий що \)</span>i<span>\(-й елемент \)</span>X<span>\( є \)</span>x_i<span>\(, а \)</span>Y<span>\( побудований аналогічно, і нехай \)</span>F_j(X)<span>\( буде вектор-стовпцем, такий що \)</span>i<span>\(-й елемент \)</span>F_j(X)<span>\( є \)</span>f_j(x_i)<span>\(. Використовуючи це позначення, попередній вираз можна переписати у векторному вигляді як:
\)</span><span>\(
\left[F_k^T(X)F_1(X), F_k^T(X)F_2(X), \ldots, F_k^T(X)F_j(X), \ldots, F_k^T(X)F_n(X)\right]
\left[\begin{array}{c} {\alpha}_1 \\
{\alpha}_2 \\
\cdots \\
{\alpha}_j \\
\cdots \\
{\alpha}_n
\end{array}\right] = F_k^T(X)Y.
\)</span><span>\(
Якщо ми повторимо це рівняння для кожного \)</span>k$, ми отримаємо наступну систему лінійних рівнянь у матричній формі:</p>

\[\begin{split}
\left[\begin{array}{cc}
F_1^T(X)F_1(X), F_1^T(X)F_2(X), \ldots, F_1^T(X)F_j(X), \ldots, F_1^T(X)F_n(X)&amp;\\ 
F_2^T(X)F_1(X), F_2^T(X)F_2(X), \ldots, F_2^T(X)F_j(X), \ldots, F_2^T(X)F_n(X)&amp;\\
&amp; \cdots \ \cdots\\
F_n^T(X)F_1(X), F_n^T(X)F_2(X), \ldots, F_n^T(X)F_j(X), \ldots, F_n^T(X)F_n(X)
\end{array}\right]
\left[\begin{array}{c} {\alpha}_1 \\
{\alpha}_2 \\
\cdots \\
{\alpha}_j \\
\cdots \\
{\alpha}_n
\end{array}\right] =
\left[\begin{array}{c} F_1^T(X)Y \\
F_2^T(X)Y \\
\cdots \\
F_n^T(X)Y
\end{array}\right].
\end{split}\]
<p>Якщо ми позначимо <span>\(A = [F_1(X), F_2(X), \ldots, F_j(X), \ldots, F_n(X)]\)</span>, а <span>\({\beta}\)</span> буде вектор-стовпцем, такий що <span>\(j\)</span>-й елемент <span>\({\beta}\)</span> є <span>\({\alpha}_j\)</span>, тоді попередня система рівнянь стає
$<span>\(
A^T A {\beta} = A^T Y,
\)</span><span>\(
і розв'язання цього матричного рівняння для \)</span>{\beta}<span>\( дає \)</span>{\beta} = (A^T A)^{-1} A^T Y$, що є точно такою ж формулою, як і в попередньому виведенні.</p>
