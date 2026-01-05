<h1>Підсумок<a href="#summary" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Лінійна алгебра є основою багатьох інженерних галузей.</p></li>
<li><p>Вектори можна розглядати як точки в <span>\({\mathbb{R}}^n\)</span>; для них визначені додавання та множення, хоча не обов'язково такі ж, як для скалярів.</p></li>
<li><p>Набір векторів є лінійно незалежним, якщо жоден з векторів не може бути записаний як лінійна комбінація інших.</p></li>
<li><p>Матриці — це таблиці чисел. Вони мають кілька важливих властивостей, включаючи визначник, ранг та обернену матрицю.</p></li>
<li><p>Система лінійних рівнянь може бути представлена матричним рівнянням <span>\(Ax = y\)</span>.</p></li>
<li><p>Кількість розв'язків системи лінійних рівнянь пов'язана з рангом(<span>\(A\)</span>) та рангом(<span>\([A,y]\)</span>). Вона може бути нульовою, одиничною або нескінченною.</p></li>
<li><p>Ми можемо розв'язувати рівняння за допомогою методу Гауса, методу Гауса-Жордана, LU-розкладу та методу Гауса-Зейделя.</p></li>
<li><p>Ми представили методи знаходження оберненої матриці.</p></li>
</ol>


<h1>Задачі<a href="#problems" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Покажіть, що множення матриць є дистрибутивним відносно додавання матриць: покажіть <span>\(A(B + C) = AB + AC\)</span>, припускаючи, що <span>\(A, B\)</span> та <span>\(C\)</span> є матрицями сумісного розміру.</p></li>
<li><p>Напишіть функцію <em>my_is_orthogonal(v1,v2, tol)</em>, де <span>\(v1\)</span> та <span>\(v2\)</span> — стовпцеві вектори однакового розміру, а <span>\(tol\)</span> — скалярне значення, строго більше 0. Результат має бути 1, якщо кут між <span>\(v1\)</span> та <span>\(v2\)</span> знаходиться в межах tol від <span>\(\pi/2\)</span>; тобто <span>\(|\pi/2 - \theta| &lt; \text{tol}\)</span>, і 0 в іншому випадку. Можна припустити, що <span>\(v1\)</span> та <span>\(v2\)</span> — стовпцеві вектори однакового розміру, а <span>\(tol\)</span> — додатний скаляр.</p></li>
</ol>


<pre><span></span><span># Test cases for problem 2</span>
<span>a</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>1</span><span>],</span> <span>[</span><span>0.001</span><span>]])</span>
<span>b</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>0.001</span><span>],</span> <span>[</span><span>1</span><span>]])</span>
<span># output: 1</span>
<span>my_is_orthogonal</span><span>(</span><span>a</span><span>,</span><span>b</span><span>,</span> <span>0.01</span><span>)</span>

<span># output: 0</span>
<span>my_is_orthogonal</span><span>(</span><span>a</span><span>,</span><span>b</span><span>,</span> <span>0.001</span><span>)</span>

<span># output: 0</span>
<span>a</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>1</span><span>],</span> <span>[</span><span>0.001</span><span>]])</span>
<span>b</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>1</span><span>],</span> <span>[</span><span>1</span><span>]])</span>
<span>my_is_orthogonal</span><span>(</span><span>a</span><span>,</span><span>b</span><span>,</span> <span>0.01</span><span>)</span>

<span># output: 1</span>
<span>a</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>1</span><span>],</span> <span>[</span><span>1</span><span>]])</span>
<span>b</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>-</span><span>1</span><span>],</span> <span>[</span><span>1</span><span>]])</span>
<span>my_is_orthogonal</span><span>(</span><span>a</span><span>,</span><span>b</span><span>,</span> <span>1e-10</span><span>)</span>
</pre>



<ol>
<li><p>Напишіть функцію <em>my_is_similar(s1,s2,tol)</em>, де <span>\(s1\)</span> та <span>\(s2\)</span> — рядки, не обов'язково однакового розміру, а <span>\(tol\)</span> — скалярне значення, строго більше 0. З <span>\(s1\)</span> та <span>\(s2\)</span>, функція повинна побудувати два вектори, <span>\(v1\)</span> та <span>\(v2\)</span>, де <span>\(v1[0]\)</span> — кількість літер 'a' в <span>\(s1\)</span>, <span>\(v1[1]\)</span> — кількість літер 'b' в <span>\(s1\)</span>, і так далі до <span>\(v1[25]\)</span>, що є кількістю літер 'z' в <span>\(v1\)</span>. Вектор <span>\(v2\)</span> повинен бути аналогічно побудований з <span>\(s2\)</span>. Результат має бути 1, якщо абсолютне значення кута між <span>\(v1\)</span> та <span>\(v2\)</span> менше tol; тобто <span>\(|\theta| &lt; \text{tol}\)</span>.</p></li>
</ol>
<ol>
<li><p>Напишіть функцію <em>my_make_lin_ind(A)</em>, де <span>\({A}\)</span> та <span>\({B}\)</span> — матриці. Нехай <span>\({rank(A) = n}\)</span>. Тоді <span>\({B}\)</span> повинна бути матрицею, що містить перші <span>\(n\)</span> стовпців <span>\({A}\)</span>, які є лінійно незалежними. Зауважте, що це означає, що <span>\({B}\)</span> має повний ранг.</p></li>
</ol>


<pre><span></span><span>## Test cases for problem 4</span>

<span>A</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>12</span><span>,</span><span>24</span><span>,</span><span>0</span><span>,</span><span>11</span><span>,</span><span>-</span><span>24</span><span>,</span><span>18</span><span>,</span><span>15</span><span>],</span> 
              <span>[</span><span>19</span><span>,</span><span>38</span><span>,</span><span>0</span><span>,</span><span>10</span><span>,</span><span>-</span><span>31</span><span>,</span><span>25</span><span>,</span><span>9</span><span>],</span> 
              <span>[</span><span>1</span><span>,</span><span>2</span><span>,</span><span>0</span><span>,</span><span>21</span><span>,</span><span>-</span><span>5</span><span>,</span><span>3</span><span>,</span><span>20</span><span>],</span>
              <span>[</span><span>6</span><span>,</span><span>12</span><span>,</span><span>0</span><span>,</span><span>13</span><span>,</span><span>-</span><span>10</span><span>,</span><span>8</span><span>,</span><span>5</span><span>],</span>
              <span>[</span><span>22</span><span>,</span><span>44</span><span>,</span><span>0</span><span>,</span><span>2</span><span>,</span><span>-</span><span>12</span><span>,</span><span>17</span><span>,</span><span>23</span><span>]])</span>

<span>B</span> <span>=</span> <span>my_make_lin_ind</span><span>(</span><span>A</span><span>)</span>

<span># B = [[12,11,-24,15],</span>
<span>#      [19,10,-31,9],</span>
<span>#      [1,21,-5,20],</span>
<span>#      [6,13,-10,5],</span>
<span>#      [22,2,-12,23]]</span>
</pre>



<ol>
<li><p>Правило Крамера — це метод обчислення визначника матриці. Розглянемо квадратну матрицю <span>\(M\)</span> розміром <span>\({n} \times {n}\)</span>. Нехай <span>\(M(i,j)\)</span> буде елементом <span>\(M\)</span> в <span>\(i\)`-му рядку та <span>\(j\)`-му стовпці <span>\(M\)</span>, а <span>\(m_{i,j}\)</span> — мінором <span>\(M\)</span>, утвореним видаленням <span>\(i\)`-го рядка та <span>\(j\)`-го стовпця з <span>\(M\)</span>. Правило Крамера стверджує, що
$<span>\(
\text{det(M)} = \sum_{i = 1}^{n} (-1)^{i-1} M(1,i) \text{det}(m_{i,j}).
\)</span>$</p></li>
</ol>
<p>Напишіть функцію <em>my_rec_det(M)</em>, де результатом є <span>\(det(M)\)</span>. Функція повинна використовувати правило Крамера для обчислення визначника, а не функцію Numpy.</p>
<ol>
<li><p>Яка складність функції <em>my_rec_det</em> у попередній задачі? Чи вважаєте ви це ефективним способом визначення, чи є матриця виродженою?</p></li>
<li><p>Нехай <span>\({p}\)</span> — вектор довжини <span>\({L}\)</span>, що містить коефіцієнти полінома порядку <span>\({L-1}\)</span>. Наприклад, вектор <span>\({p = [1,0,2]}\)</span> є представленням полінома <span>\(f(x) = 1 x^2 + 0 x + 2\)</span>. Напишіть функцію <em>my_poly_der_mat(p)</em>, де <span>\({p}\)</span> — вищезгаданий вектор, а результатом <span>\(D\)</span> є матриця, яка повертатиме коефіцієнти похідної <span>\({p}\)</span> при лівосторонньому множенні <span>\({p}\)</span> на <span>\({D}\)</span>. Наприклад, похідна <span>\(f(x)\)</span> є <span>\(f'(x) = 2x\)</span>, і тому <span>\(d = Dp\)</span> повинно дати <span>\({d = [2,0]}\)</span>. Зауважте, що це означає, що розмірність <span>\(D\)</span> становить <span>\({L-1} \times {L}\)</span>. Мета цієї задачі — показати, що інтегрування поліномів насправді є лінійним перетворенням.</p></li>
</ol>
<ol>
<li><p>Використайте метод Гауса для розв'язання наступних рівнянь.</p></li>
</ol>

\[\begin{eqnarray*}
3x_1 - x_2 + 4x_3 &amp;=&amp; 2 \\
17x_1 + 2x_2 + x_3 &amp;=&amp; 14 \\
x_1 + 12x_2 -7z &amp;=&amp; 54 \\
\end{eqnarray*}\]
<ol>
<li><p>Використайте метод Гауса-Жордана для розв'язання вищезгаданих рівнянь у задачі 8.</p></li>
<li><p>Отримайте нижню трикутну матрицю <span>\(L\)</span> та верхню трикутну матрицю <span>\(U\)</span> з рівнянь у задачі 8.</p></li>
<li><p>Покажіть, що скалярний добуток є дистрибутивним відносно додавання векторів, тобто покажіть, що <span>\(u \cdot (v + w) = u \cdot v + u \cdot w\)</span>.</p></li>
<li><p>Розгляньте наступну мережу, що складається з двох станцій електропостачання, позначених <span>\(S1\)</span> та <span>\(S2\)</span>, та п'яти вузлів-споживачів електроенергії, позначених від <span>\(N1\)</span> до <span>\(N5\)</span>. Вузли з'єднані лініями електропередач, які позначені стрілками, і електроенергія може текти між вузлами по цих лініях в обох напрямках.</p></li>
</ol>
<p>Нехай <span>\(d_{i}\)</span> — додатний скаляр, що позначає потреби в електроенергії для вузла <span>\(i\)</span>, і припустимо, що ця потреба повинна бути задоволена точно. Потужність станцій електропостачання позначається <span>\(S\)</span>. Станції електропостачання повинні працювати на повну потужність. Для кожної стрілки нехай <span>\(f_{j}\)</span> буде потоком електроенергії вздовж цієї стрілки. Негативний потік означає, що електроенергія тече в протилежному напрямку до стрілки.</p>
<img alt="Problem 11" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/14.01.01-problem_11.png"/>
<p>Напишіть функцію <em>my_flow_calculator(S, d)</em>, де <span>\(S\)</span> — вектор <span>\(1 \times 2\)</span>, що представляє потужність кожної станції електропостачання, а <span>\(d\)</span> — вектор-рядок <span>\(1 \times 5\)</span>, що представляє потреби в кожному вузлі (тобто <span>\(d[0]\)</span> — це потреба у вузлі 1). Вихідний аргумент <span>\(f\)</span> повинен бути вектором-рядком <span>\(1 \times 7\)</span>, що позначає потоки в мережі (тобто <span>\(f[0] = f_1\)</span> на діаграмі). Потоки, що містяться в <span>\(f\)</span>, повинні задовольняти всі обмеження системи, такі як генерація електроенергії та потреби. Зауважте, що система рівнянь може мати більше одного розв'язку.</p>
<p>Загальний потік у вузол повинен дорівнювати загальному потоку з вузла плюс потреба; тобто, для кожного вузла <span>\(i, f_{\text{inflow}} = f_{\text{outflow}} + d_{i}\)</span>. Можна припустити, що <span>\(\Sigma{S_j} = \Sigma{d_i}\)</span>.</p>


<pre><span></span><span>## Test cases for problem 4</span>

<span>s</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>10</span><span>,</span> <span>10</span><span>]])</span>
<span>d</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>4</span><span>,</span> <span>4</span><span>,</span> <span>4</span><span>,</span> <span>4</span><span>,</span> <span>4</span><span>]])</span>

<span># f = [[10.0, 4.0, -2.0, 4.5, 5.5, 2.5, 1.5]]</span>
<span>f</span> <span>=</span> <span>my_flow_calculator</span><span>(</span><span>s</span><span>,</span> <span>d</span><span>)</span>

<span>s</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>10</span><span>,</span> <span>10</span><span>]])</span>
<span>d</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>3</span><span>,</span> <span>4</span><span>,</span> <span>5</span><span>,</span> <span>4</span><span>,</span> <span>4</span><span>]])</span>
<span># f = [[10.0, 5.0, -1.0, 4.5, 5.5, 2.5, 1.5]]</span>
<span>f</span> <span>=</span> <span>my_flow_calculator</span><span>(</span><span>s</span><span>,</span> <span>d</span><span>)</span>
</pre>
