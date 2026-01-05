<h1>Основи лінійної алгебри<a href="#basics-of-linear-algebra" title="Постійне посилання на цей заголовок"></a></h1>
<p>Перш ніж ми представимо системи лінійних рівнянь, давайте спочатку розглянемо деякі основи лінійної алгебри, які будуть використовуватися для опису та розв'язання лінійних рівнянь. У цьому розділі ми розглянемо лише найосновніші поняття, а докладніше ви можете дізнатися, прочитавши книгу з лінійної алгебри.</p>

<h2>Множини<a href="#sets" title="Постійне посилання на цей заголовок"></a></h2>
<p>Ми вже обговорювали структуру даних — множини у розділі 2, тут ми розглянемо їх з математичної точки зору, використовуючи математичну термінологію. У математиці <strong>множина</strong> — це сукупність об'єктів. Як ми показували раніше, множини зазвичай позначаються фігурними дужками {}. Наприклад, <span>\(S = {orange, apple, banana}\)</span> означає "S — це множина, що містить 'апельсин', 'яблуко' та 'банан'".</p>
<p><strong>Порожня множина</strong> — це множина, що не містить жодних об'єктів, і зазвичай позначається порожніми фігурними дужками, такими як <span>\(\{\}\)</span>, або символом <span>\(\emptyset\)</span>. Для двох множин, <span>\(A\)</span> та <span>\(B\)</span>, <strong>об'єднання</strong> <span>\(A\)</span> та <span>\(B\)</span> позначається як <span>\(A \cup B\)</span> і дорівнює множині, що містить усі елементи <span>\(A\)</span> та <span>\(B\)</span>. <strong>Перетин</strong> <span>\(A\)</span> та <span>\(B\)</span> позначається як <span>\(A \cap B\)</span> і дорівнює множині, що містить усі елементи, які належать як <span>\(A\)</span>, так і <span>\(B\)</span>. У позначеннях множин двокрапка використовується для позначення <strong>"такий, що"</strong>. Використання цих термінів незабаром стане зрозумілим. Символ <strong><span>\(\in\)</span></strong> використовується для позначення того, що об'єкт міститься в множині. Наприклад, <span>\(a \in A\)</span> означає "<span>\(a\)</span> є елементом <span>\(A\)</span>" або "<span>\(a\)</span> належить <span>\(A\)</span>". Зворотна коса риска, <span>\(\backslash\)</span>, у позначеннях множин означає <strong>різницю множин</strong>. Отже, якщо <span>\(a\in A\)</span>, то <span>\(A\backslash a\)</span> означає "<span>\(A\)</span> без елемента <span>\(a\)</span>".</p>
<p>Існує кілька стандартних множин, пов'язаних з числами, наприклад, <strong>натуральні числа</strong>, <strong>цілі невід'ємні числа</strong>, <strong>цілі числа</strong>, <strong>раціональні числа</strong>, <strong>ірраціональні числа</strong>, <strong>дійсні числа</strong> та <strong>комплексні числа</strong>. Опис кожної множини та символ, що використовується для їх позначення, наведено в наступній таблиці.</p>
<table>
<thead>
<tr><th><p>Назва множини</p></th>
<th><p>Символ</p></th>
<th><p>Опис</p></th>
</tr>
</thead>
<tbody>
<tr><td><p>Натуральні числа</p></td>
<td><p><span>\(\mathbb{N}\)</span></p></td>
<td><p><span>\({\mathbb{N}} = \{1, 2, 3, 4, \cdots\}\)</span></p></td>
</tr>
<tr><td><p>Цілі невід'ємні числа</p></td>
<td><p><span>\(\mathbb{W}\)</span></p></td>
<td><p><span>\({\mathbb{W}} = \mathbb{N} \cup \{0\}\)</span></p></td>
</tr>
<tr><td><p>Цілі числа</p></td>
<td><p><span>\(\mathbb{Z}\)</span></p></td>
<td><p><span>\({\mathbb{Z}} = \mathbb{W} \cup \{-1, -2, -3, \cdots\}\)</span></p></td>
</tr>
<tr><td><p>Раціональні числа</p></td>
<td><p><span>\(\mathbb{Q}\)</span></p></td>
<td><p><span>\({\mathbb{Q}} = \{\frac{p}{q} : p\in {\mathbb{Z}}, q\in {\mathbb{Z}} \backslash \{0\}\}\)</span></p></td>
</tr>
<tr><td><p>Ірраціональні числа</p></td>
<td><p><span>\(\mathbb{I}\)</span></p></td>
<td><p><span>\({\mathbb{I}}\)</span> — це множина дійсних чисел, які не можуть бути виражені як дріб цілих чисел.</p></td>
</tr>
<tr><td><p>Дійсні числа</p></td>
<td><p><span>\(\mathbb{R}\)</span></p></td>
<td><p><span>\({\mathbb{R}} = \mathbb{Q} \cup \mathbb{I}\)</span></p></td>
</tr>
<tr><td><p>Комплексні числа</p></td>
<td><p><span>\(\mathbb{C}\)</span></p></td>
<td><p><span>\({\mathbb{C}} = \{a + bi : a,b\in {\mathbb{R}}, i = \sqrt{-1}\}\)</span></p></td>
</tr>
</tbody>
</table>
<p><strong>СПРОБУЙТЕ!</strong> Нехай <span>\(S\)</span> — це множина всіх дійсних пар <span>\((x,y)\)</span> таких, що <span>\(x^2 + y^2 = 1\)</span>. Запишіть <span>\(S\)</span> за допомогою позначень множин.</p>
<p><span>\(S = \{(x,y) : x,y \in {\mathbb{R}}, x^2 + y^2 = 1\}\)</span></p>

<h2>Вектори<a href="#vectors" title="Постійне посилання на цей заголовок"></a></h2>
<p>Множина <span>\({\mathbb{R}}^n\)</span> — це множина всіх <span>\(n\)</span>-кортежів дійсних чисел. У позначеннях множин це <span>\({\mathbb{R}}^n = \{(x_1, x_2, x_3, \cdots, x_n): x_1, x_2, x_3, \cdots, x_n \in {\mathbb{R}}\}\)</span>. Наприклад, множина <span>\({\mathbb{R}}^3\)</span> представляє множину дійсних трійок, координат <span>\((x,y,z)\)</span>, у тривимірному просторі.</p>
<p><strong>Вектор</strong> у <span>\({\mathbb{R}}^n\)</span> — це <span>\(n\)</span>-кортеж, або точка, у <span>\({\mathbb{R}}^n\)</span>. Вектори можуть бути записані горизонтально (тобто, елементи вектора розташовані поруч один з одним) як <strong>вектор-рядок</strong>, або вертикально (тобто, елементи вектора розташовані один над одним) як <strong>вектор-стовпець</strong>. Якщо контекст вектора неоднозначний, зазвичай мається на увазі, що вектор є вектором-стовпцем. <span>\(i\)</span>-й елемент вектора <span>\(v\)</span> позначається як <span>\(v_i\)</span>. Транспонований вектор-стовпець є вектором-рядком тієї ж довжини, а транспонований вектор-рядок є вектором-стовпцем. У математиці транспонування позначається верхнім індексом <span>\(T\)</span>, або <span>\(v^T\)</span>. <strong>Нульовий вектор</strong> — це вектор у <span>\({\mathbb{R}}^n\)</span>, що містить усі нулі.</p>
<p><strong>Норма</strong> вектора — це міра його довжини. Існує багато способів визначення довжини вектора залежно від використовуваної метрики (тобто обраної формули відстані). Найпоширенішою є норма <span>\(L_2\)</span>, яка обчислюється за формулою відстані, з якою ви, ймовірно, знайомі зі школи. <strong>Норма <span>\(L_2\)</span></strong> вектора <span>\(v\)</span> позначається як <span>\(\Vert v \Vert_{2}\)</span>, і <span>\(\Vert v \Vert_{2} = \sqrt{\sum_i v_i^2}\)</span>. Її іноді також називають евклідовою довжиною і вона позначає "фізичну" довжину вектора в одновимірному, двовимірному або тривимірному просторі. Норма <span>\(L_1\)</span>, або "Манхеттенська відстань", обчислюється як <span>\(\Vert v \Vert_{1} = \sum_i |v_i|\)</span> і названа на честь сітчастої дорожньої структури Нью-Йорка. Загалом, <strong>p-норма</strong>, <span>\(L_p\)</span>, вектора дорівнює <span>\(\Vert v \Vert_{p} = \sqrt[p]{(\sum_i v_i^p)}\)</span>. <strong>Норма <span>\(L_\infty\)</span></strong> — це <span>\(p\)</span>-норма, де <span>\(p = \infty\)</span>. Норма <span>\(L_\infty\)</span> записується як <span>\(||v||_\infty\)</span> і дорівнює максимальному абсолютному значенню у <span>\(v\)</span>.</p>
<p><strong>СПРОБУЙТЕ!</strong> Створіть вектор-рядок та вектор-стовпець і покажіть форму цих векторів.</p>

<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
<span>vector_row</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>1</span><span>,</span> <span>-</span><span>5</span><span>,</span> <span>3</span><span>,</span> <span>2</span><span>,</span> <span>4</span><span>]])</span>
<span>vector_column</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>1</span><span>],</span> 
                          <span>[</span><span>2</span><span>],</span> 
                          <span>[</span><span>3</span><span>],</span> 
                          <span>[</span><span>4</span><span>]])</span>
<span>print</span><span>(</span><span>vector_row</span><span>.</span><span>shape</span><span>)</span>
<span>print</span><span>(</span><span>vector_column</span><span>.</span><span>shape</span><span>)</span>
</pre>

<pre><span></span>(1, 5)
(4, 1)
</pre>

<p><strong>Примітка!</strong> У Python вектори-рядки та вектори-стовпці є дещо незвичайними. З наведеного вище ви можете побачити, що для отримання векторів з 1 рядком і 4 стовпцями або 4 рядками і 1 стовпцем, ми повинні використовувати список списків для їх визначення. Ви можете визначити np.array([1,2,3,4]), але незабаром помітите, що він не містить інформації про рядок або стовпець.</p>
<p><strong>СПРОБУЙТЕ!</strong> Транспонуйте вектор-рядок, який ми визначили вище, у вектор-стовпець і обчисліть його норми <span>\(L_1\)</span>, <span>\(L_2\)</span> та <span>\(L_\infty\)</span>. Перевірте, що норма <span>\(L_\infty\)</span> вектора еквівалентна максимальному абсолютному значенню елементів у векторі.</p>

<pre><span></span><span>from</span> <span>numpy.linalg</span> <span>import</span> <span>norm</span>
<span>new_vector</span> <span>=</span> <span>vector_row</span><span>.</span><span>T</span>
<span>print</span><span>(</span><span>new_vector</span><span>)</span>
<span>norm_1</span> <span>=</span> <span>norm</span><span>(</span><span>new_vector</span><span>,</span> <span>1</span><span>)</span>
<span>norm_2</span> <span>=</span> <span>norm</span><span>(</span><span>new_vector</span><span>,</span> <span>2</span><span>)</span>
<span>norm_inf</span> <span>=</span> <span>norm</span><span>(</span><span>new_vector</span><span>,</span> <span>np</span><span>.</span><span>inf</span><span>)</span>
<span>print</span><span>(</span><span>'L_1 дорівнює: </span><span>%.1f</span><span>'</span><span>%</span><span>norm_1</span>)
<span>print</span><span>(</span><span>'L_2 дорівнює: </span><span>%.1f</span><span>'</span><span>%</span><span>norm_2</span>)
<span>print</span><span>(</span><span>'L_inf дорівнює: </span><span>%.1f</span><span>'</span><span>%</span><span>norm_inf</span>)
</pre>

<pre><span></span>[[ 1]
 [-5]
 [ 3]
 [ 2]
 [ 4]]
L_1 дорівнює: 15.0
L_2 дорівнює: 7.4
L_inf дорівнює: 5.0
</pre>

<p><strong>Додавання векторів</strong> визначається як попарне додавання кожного з елементів доданих векторів. Наприклад, якщо <span>\(v\)</span> та <span>\(w\)</span> є векторами в <span>\({\mathbb{R}}^n\)</span>, то <span>\(u = v + w\)</span> визначається як <span>\(u_i = v_i + w_i\)</span>.</p>
<p><strong>Множення векторів</strong> може бути визначено кількома способами залежно від контексту. <strong>Множення вектора на скаляр</strong> — це добуток вектора та <strong>скаляра</strong> (тобто числа з <span>\({\mathbb{R}}\)</span>). Множення на скаляр визначається як добуток кожного елемента вектора на скаляр. Точніше, якщо <span>\(\alpha\)</span> — скаляр, а <span>\(v\)</span> — вектор, то <span>\(u = \alpha v\)</span> визначається як <span>\(u_i = \alpha v_i\)</span>. Зауважте, що саме так Python реалізує множення вектора на скаляр.</p>
<p><strong>СПРОБУЙТЕ!</strong> Покажіть, що <span>\(a(v + w) = av + aw\)</span> (тобто, множення вектора на скаляр розподіляється відносно додавання векторів).</p>
<p>За визначенням додавання векторів, <span>\(u = v + w\)</span> — це вектор з <span>\(u_i = v_i + w_i\)</span>. За визначенням множення вектора на скаляр, <span>\(x = \alpha u\)</span> — це вектор з <span>\(x_i = \alpha(v_i + w_i)\)</span>. Оскільки <span>\(\alpha, v_i\)</span> та <span>\(w_i\)</span> є скалярами, множення розподіляється, і <span>\(x_i = \alpha v_i + \alpha w_i\)</span>. Отже, <span>\(a(v + w) = av + aw\)</span>.</p>
<p><strong>Скалярний добуток</strong> двох векторів — це сума добутків відповідних елементів кожного вектора, позначається символом <span>\(\cdot\)</span>, а <span>\(v \cdot w\)</span> читається як "v скалярно помножити на w". Отже, для <span>\(v\)</span> та <span>\(w\)</span> <span>\(\in {\mathbb{R}}^n, d = v\cdot w\)</span> визначається як <span>\(d = \sum_{i = 1}^{n} v_iw_i\)</span>. <strong>Кут між двома векторами</strong>, <span>\(\theta\)</span>, визначається за формулою:</p>

\[
v \cdot w = \Vert v \Vert_{2} \Vert w \Vert_{2} \cos{\theta}
\]
<p>Скалярний добуток є мірою того, наскільки схоже спрямовані два вектори. Наприклад, вектори (1,1) і (2,2) паралельні. Якщо ви обчислите кут між ними за допомогою скалярного добутку, ви побачите, що <span>\(\theta = 0\)</span>. Якщо кут між векторами, <span>\(\theta = \pi/2\)</span>, то вектори вважаються перпендикулярними або <strong>ортогональними</strong>, а скалярний добуток дорівнює 0.</p>
<p><strong>СПРОБУЙТЕ!</strong> Обчисліть кут між векторами <span>\(v = [10, 9, 3]\)</span> та <span>\(w = [2, 5, 12]\)</span>.</p>

<pre><span></span><span>from</span> <span>numpy</span> <span>import</span> <span>arccos</span><span>,</span> <span>dot</span>

<span>v</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>10</span><span>,</span> <span>9</span><span>,</span> <span>3</span><span>]])</span>
<span>w</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>2</span><span>,</span> <span>5</span><span>,</span> <span>12</span><span>]])</span>
<span>theta</span> <span>=</span> \
    <span>arccos</span><span>(</span><span>dot</span><span>(</span><span>v</span><span>,</span> <span>w</span><span>.</span><span>T</span><span>)</span><span>/</span><span>(</span><span>norm</span><span>(</span><span>v</span><span>)</span><span>*</span><span>norm</span><span>(</span><span>w</span><span>)))</span>
<span>print</span><span>(</span><span>theta</span><span>)</span>
</pre>

<pre><span></span>[[0.97992471]]
</pre>

<p>Нарешті, <strong>векторний добуток</strong> між двома векторами, <span>\(v\)</span> та <span>\(w\)</span>, записується як <span>\(v \times w\)</span>. Він визначається як <span>\(v \times w = \Vert v \Vert_{2}\Vert w \Vert_{2}\sin{(\theta)} \textit{n}\)</span>, де <span>\(\theta\)</span> — кут між <span>\(v\)</span> та <span>\(w\)</span> (який можна обчислити за допомогою скалярного добутку), а <strong><span>\(n\)</span></strong> — вектор, перпендикулярний як до <span>\(v\)</span>, так і до <span>\(w\)</span>, з одиничною довжиною (тобто, довжина дорівнює одиниці). Геометрична інтерпретація векторного добутку — це вектор, перпендикулярний як до <span>\(v\)</span>, так і до <span>\(w\)</span>, довжина якого дорівнює площі паралелограма, утвореного цими двома векторами.</p>
<p><strong>СПРОБУЙТЕ!</strong> Маючи вектори <span>\(v = [0, 2, 0]\)</span> та <span>\(w = [3, 0, 0]\)</span>, використайте функцію Numpy cross для обчислення векторного добутку v та w.</p>

<pre><span></span><span>v</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>0</span><span>,</span> <span>2</span><span>,</span> <span>0</span><span>]])</span>
<span>w</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>3</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>]])</span>
<span>print</span><span>(</span><span>np</span><span>.</span><span>cross</span><span>(</span><span>v</span><span>,</span> <span>w</span><span>))</span>
</pre>

<pre><span></span>[[ 0  0 -6]]
</pre>

<p>Припускаючи, що <span>\(S\)</span> — це множина, в якій визначені додавання та множення на скаляр, <strong>лінійна комбінація</strong> <span>\(S\)</span> визначається як
$<span>\(
\sum \alpha_i s_i,
\)</span>$</p>
<p>де <span>\(\alpha_i\)</span> — будь-яке дійсне число, а <span>\(s_i\)</span> — <span>\(i^{\text{th}}\)</span> об'єкт у <span>\(S\)</span>. Іноді значення <span>\(\alpha_i\)</span> називають <strong>коефіцієнтами</strong> <span>\(s_i\)</span>. Лінійні комбінації можуть бути використані для опису багатьох речей. Наприклад, рахунок за продукти можна записати як <span>\(\displaystyle{\sum c_i n_i}\)</span>, де <span>\(c_i\)</span> — вартість товару <span>\(i\)</span>, а <span>\(n_i\)</span> — кількість придбаного товару <span>\(i\)</span>. Таким чином, загальна вартість є лінійною комбінацією придбаних товарів.</p>
<p>Множина називається <strong>лінійно незалежною</strong>, якщо жоден об'єкт у множині не може бути записаний як лінійна комбінація інших об'єктів у множині. Для наших цілей ми розглядатимемо лише лінійну незалежність множини векторів. Множина векторів, яка не є лінійно незалежною, є <strong>лінійно залежною</strong>.</p>
<p><strong>СПРОБУЙТЕ!</strong> Маючи вектори-рядки <span>\(v = [0, 3, 2]\)</span>, <span>\(w = [4, 1, 1]\)</span> та <span>\(u = [0, -2, 0]\)</span>, запишіть вектор <span>\(x = [-8, -1, 4]\)</span> як лінійну комбінацію <span>\(v\)</span>, <span>\(w\)</span> та <span>\(u\)</span>.</p>

<pre><span></span><span>v</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>0</span><span>,</span> <span>3</span><span>,</span> <span>2</span><span>]])</span>
<span>w</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>4</span><span>,</span> <span>1</span><span>,</span> <span>1</span><span>]])</span>
<span>u</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>0</span><span>,</span> <span>-</span><span>2</span><span>,</span> <span>0</span><span>]])</span>
<span>x</span> <span>=</span> <span>3</span><span>*</span><span>v</span><span>-</span><span>2</span><span>*</span><span>w</span><span>+</span><span>4</span><span>*</span><span>u</span>
<span>print</span><span>(</span><span>x</span><span>)</span>
</pre>

<pre><span></span>[[-8 -1  4]]
</pre>

<p><strong>СПРОБУЙТЕ!</strong> Визначте шляхом огляду, чи є наступна множина векторів лінійно незалежною: <span>\(v = [1, 1, 0]\)</span>, <span>\(w = [1, 0, 0]\)</span>, <span>\(u = [0, 0, 1]\)</span>.</p>
<p>Очевидно, що <span>\(u\)</span> лінійно незалежний від <span>\(v\)</span> та <span>\(w\)</span>, оскільки лише <span>\(u\)</span> має ненульовий третій елемент. Вектори <span>\(v\)</span> та <span>\(w\)</span> також лінійно незалежні, оскільки лише <span>\(v\)</span> має ненульовий другий елемент. Отже, <span>\(v, w\)</span> та <span>\(u\)</span> є лінійно незалежними.</p>

<h2>Матриці<a href="#matrices" title="Постійне посилання на цей заголовок"></a></h2>
<p>Матриця розміром <span>\({m} \times {n}\)</span> — це прямокутна таблиця чисел, що складається з <span>\(m\)</span> рядків та <span>\(n\)</span> стовпців. Норму матриці можна розглядати як особливий вид векторної норми: якщо ми розглядаємо <span>\({m} \times {n}\)</span> елементів <span>\(M\)</span> як елементи <span>\(mn\)</span>-вимірного вектора, то p-норму цього вектора можна записати як:</p>

\[\Vert M \Vert_{p} = \sqrt[p]{(\sum_i^m \sum_j^n |a_{ij}|^p)}\]
<p>Ви можете обчислити норму матриці за допомогою тієї ж функції <code><span>norm</span></code> у <code><span>Numpy</span></code>, що й для вектора.</p>
<p>Додавання матриць та множення на скаляр для матриць працюють так само, як і для векторів. Однак <strong>множення матриць</strong> між двома матрицями, <span>\(P\)</span> та <span>\(Q\)</span>, визначено, коли <span>\(P\)</span> є матрицею розміром <span>\({m} \times {p}\)</span>, а <span>\(Q\)</span> — матрицею розміром <span>\({p} \times {n}\)</span>. Результатом <span>\(M = PQ\)</span> є матриця <span>\(M\)</span> розміром <span>\(m \times n\)</span>. Розмірність <span>\(p\)</span> називається <strong>внутрішньою розмірністю матриці</strong>, і внутрішні розмірності матриць повинні збігатися (тобто, кількість стовпців у <span>\(P\)</span> та кількість рядків у <span>\(Q\)</span> повинні бути однаковими), щоб множення матриць було визначено. Розмірності <span>\(m\)</span> та <span>\(n\)</span> називаються <strong>зовнішніми розмірностями матриці</strong>. Формально, якщо <span>\(P\)</span> має розмір <span>\({m} \times {p}\)</span>, а <span>\(Q\)</span> — <span>\({p} \times {n}\)</span>, то <span>\(M = PQ\)</span> визначається як</p>

\[
M_{ij} = \sum_{k=1}^p P_{ik}Q_{kj}
\]
<p>Добуток двох матриць <span>\(P\)</span> та <span>\(Q\)</span> у Python досягається за допомогою методу <strong>dot</strong> у Numpy. <strong>Транспонована матриця</strong> — це матриця, отримана шляхом заміни її рядків на стовпці. Транспонування позначається верхнім індексом <span>\(T\)</span>, наприклад, <span>\(M^T\)</span> — це транспонована матриця <span>\(M\)</span>. У Python для отримання транспонованої матриці використовується метод <strong>T</strong> для масиву Numpy. Наприклад, якщо <span>\(M\)</span> — матриця, то <span>\(M.T\)</span> — це її транспонована матриця.</p>
<p><strong>СПРОБУЙТЕ!</strong> Нехай матриці Python <span>\(P = [[1, 7], [2, 3], [5, 0]]\)</span> та <span>\(Q = [[2, 6, 3, 1], [1, 2, 3, 4]]\)</span>. Обчисліть добуток матриць <span>\(P\)</span> та <span>\(Q\)</span>. Покажіть, що добуток <span>\(Q\)</span> та <span>\(P\)</span> призведе до помилки.</p>

<pre><span></span><span>P</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>1</span><span>,</span> <span>7</span><span>],</span> <span>[</span><span>2</span><span>,</span> <span>3</span><span>],</span> <span>[</span><span>5</span><span>,</span> <span>0</span><span>]])</span>
<span>Q</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>2</span><span>,</span> <span>6</span><span>,</span> <span>3</span><span>,</span> <span>1</span><span>],</span> <span>[</span><span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>,</span> <span>4</span><span>]])</span>
<span>print</span><span>(</span><span>P</span><span>)</span>
<span>print</span><span>(</span><span>Q</span><span>)</span>
<span>print</span><span>(</span><span>np</span><span>.</span><span>dot</span><span>(</span><span>P</span><span>,</span> <span>Q</span><span>))</span>
<span>np</span><span>.</span><span>dot</span><span>(</span><span>Q</span><span>,</span> <span>P</span><span>)</span>
</pre>

<pre><span></span>[[1 7]
 [2 3]
 [5 0]]
[[2 6 3 1]
 [1 2 3 4]]
[[ 9 20 24 29]
 [ 7 18 15 14]
 [10 30 15  5]]
</pre>

<pre><span></span><span>---------------------------------------------------------------------------</span>
<span>ValueError</span><span>                                </span>Traceback (most recent call last)
<span>&lt;</span><span>ipython</span><span>-</span><span>input</span><span>-</span><span>6</span><span>-</span><span>29</span><span>a4b2da4cb8</span><span>&gt;</span> <span>in</span> <span>&lt;</span><span>module</span><span>&gt;</span>
<span>      </span><span>4</span> <span>print</span><span>(</span><span>Q</span><span>)</span>
<span>      </span><span>5</span> <span>print</span><span>(</span><span>np</span><span>.</span><span>dot</span><span>(</span><span>P</span><span>,</span> <span>Q</span><span>))</span>
<span>----&gt; </span><span>6</span> <span>np</span><span>.</span><span>dot</span><span>(</span><span>Q</span><span>,</span> <span>P</span><span>)</span>

<span>ValueError</span>: shapes (2,4) and (3,2) not aligned: 4 (dim 1) != 3 (dim 0)
</pre>

<p><strong>Квадратна матриця</strong> — це матриця розміром <span>\({n} \times {n}\)</span>; тобто, вона має однакову кількість рядків та стовпців. <strong>Визначник</strong> є важливою властивістю квадратних матриць. Визначник позначається як <span>\(det(M)\)</span>, як у математиці, так і в пакеті <code><span>linalg</span></code> бібліотеки Numpy, іноді він також позначається як <span>\(|M|\)</span>. Деякі приклади використання визначника будуть описані пізніше.</p>
<p>У випадку матриці <span>\(2 \times 2\)</span> визначник дорівнює:</p>

\[\begin{split}
|M| = \begin{bmatrix}
a &amp; b \\
c &amp; d\\
\end{bmatrix} = ad - bc\end{split}\]
<p>Аналогічно, у випадку матриці <span>\(3 \times 3\)</span> визначник дорівнює:</p>

\[\begin{split}
\begin{eqnarray*}
|M| = \begin{bmatrix}
a &amp; b &amp; c \\
d &amp; e &amp; f \\
g &amp; h &amp; i \\
\end{bmatrix} &amp; = &amp; a\begin{bmatrix}
\Box &amp;\Box  &amp;\Box  \\
\Box &amp; e &amp; f \\
\Box &amp; h &amp; i \\
\end{bmatrix} - b\begin{bmatrix}
\Box &amp;\Box  &amp;\Box  \\
d &amp; \Box &amp; f \\
g &amp; \Box &amp; i \\
\end{bmatrix}+c\begin{bmatrix}
\Box &amp;\Box  &amp;\Box  \\
d &amp; e &amp; \Box \\
g &amp; h &amp; \Box \\
\end{bmatrix} \\
&amp;&amp;\\
&amp; = &amp; a\begin{bmatrix}
e &amp; f \\
h &amp; i \\
\end{bmatrix} - b\begin{bmatrix}
d &amp; f \\
g &amp; i \\
\end{bmatrix}+c\begin{bmatrix}
d &amp; e \\
g &amp; h \\
\end{bmatrix} \\ 
&amp;&amp;\\
&amp; = &amp; aei + bfg + cdh - ceg - bdi - afh
\end{eqnarray*}\end{split}\]
<p>Ми можемо використовувати подібний підхід для обчислення визначника для матриць вищої розмірності, але набагато простіше обчислити його за допомогою Python. Нижче ми побачимо приклад, як обчислити визначник у Python.</p>
<p><strong>Одинична матриця</strong> — це квадратна матриця з одиницями на головній діагоналі та нулями в інших місцях. Одинична матриця зазвичай позначається як <span>\(I\)</span> і є аналогічною одиниці дійсних чисел, 1. Тобто, множення будь-якої матриці на <span>\(I\)</span> (сумісного розміру) дасть ту саму матрицю.</p>
<p><strong>СПРОБУЙТЕ!</strong> Використайте Python, щоб знайти визначник матриці <span>\(M = [[0, 2, 1, 3], [3, 2, 8, 1], [1, 0, 0, 3], [0, 3, 2, 1]]\)</span>. Використайте функцію <em>np.eye</em> для створення одиничної матриці <span>\({4} \times {4}\)</span>, <span>\(I\)</span>. Помножте <span>\(M\)</span> на <span>\(I\)</span>, щоб показати, що результатом є <span>\(M\)</span>.</p>

<pre><span></span><span>from</span> <span>numpy.linalg</span> <span>import</span> <span>det</span>

<span>M</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>0</span><span>,</span><span>2</span><span>,</span><span>1</span><span>,</span><span>3</span><span>],</span> 
             <span>[</span><span>3</span><span>,</span><span>2</span><span>,</span><span>8</span><span>,</span><span>1</span><span>],</span> 
             <span>[</span><span>1</span><span>,</span><span>0</span><span>,</span><span>0</span><span>,</span><span>3</span><span>],</span>
             <span>[</span><span>0</span><span>,</span><span>3</span><span>,</span><span>2</span><span>,</span><span>1</span><span>]])</span>
<span>print</span><span>(</span><span>'M:</span><span>\n</span><span>'</span><span>,</span> <span>M</span><span>)</span>

<span>print</span><span>(</span><span>'Визначник: </span><span>%.1f</span><span>'</span><span>%</span><span>det</span>(M))
<span>I</span> <span>=</span> <span>np</span><span>.</span><span>eye</span><span>(</span><span>4</span><span>)</span>
<span>print</span><span>(</span><span>'I:</span><span>\n</span><span>'</span><span>,</span> <span>I</span><span>)</span>
<span>print</span><span>(</span><span>'M*I:</span><span>\n</span><span>'</span><span>,</span> <span>np</span><span>.</span><span>dot</span><span>(</span><span>M</span><span>,</span> <span>I</span><span>))</span>
</pre>

<pre><span></span>M:
 [[0 2 1 3]
 [3 2 8 1]
 [1 0 0 3]
 [0 3 2 1]]
Визначник: -38.0
I:
 [[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
M*I:
 [[0. 2. 1. 3.]
 [3. 2. 8. 1.]
 [1. 0. 0. 3.]
 [0. 3. 2. 1.]]
</pre>

<p><strong>Обернена матриця</strong> до квадратної матриці <span>\(M\)</span> — це матриця того ж розміру, <span>\(N\)</span>, така, що <span>\(M \cdot N = I\)</span>. Обернена матриця аналогічна оберненому числу в дійсних числах. Наприклад, обернене до 3 є <span>\(\frac{1}{3}\)</span>, оскільки <span>\((3)(\frac{1}{3}) = 1\)</span>. Матриця називається <strong>оборотною</strong>, якщо вона має обернену. Обернена матриця є унікальною; тобто, для оборотної матриці існує лише одна обернена матриця. Якщо <span>\(M\)</span> — квадратна матриця, її обернена позначається як <span>\(M^{-1}\)</span> у математиці, і її можна обчислити в Python за допомогою функції <em>inv</em> з пакета <em>linalg</em> бібліотеки Numpy.</p>
<p>Для матриці <span>\(2 \times 2\)</span> аналітичний розв'язок оберненої матриці такий:</p>

\[\begin{split}
M^{-1} = \begin{bmatrix}
a &amp; b \\
c &amp; d\\
\end{bmatrix}^{-1} = \frac{1}{|M|}\begin{bmatrix}
d &amp; -b \\
-c &amp; a\\
\end{bmatrix}\end{split}\]
<p>Обчислення оберненої матриці для аналітичного розв'язку стає складним зі збільшенням розмірності матриці; існує багато інших методів, які можуть спростити це, таких як метод Гауса, метод Ньютона, розклад на власні значення тощо. Ми представимо деякі з цих методів після того, як навчимося розв'язувати системи лінійних рівнянь, оскільки процес по суті той самий.</p>
<p>Нагадаємо, що 0 не має оберненого для множення в множині дійсних чисел. Аналогічно, існують матриці, які не мають обернених. Ці матриці називаються <strong>виродженими</strong> (або сингулярними). Матриці, які мають обернену, називаються <strong>невиродженими</strong> (або несингулярними).</p>
<p>Один із способів визначити, чи є матриця виродженою, — обчислити її визначник. Якщо визначник дорівнює 0, то матриця є виродженою; якщо ні, то матриця є невиродженою.</p>
<p><strong>СПРОБУЙТЕ!</strong> Матриця <span>\(M\)</span> (у попередньому прикладі) має ненульовий визначник. Обчисліть обернену матрицю до <span>\(M\)</span>. Покажіть, що матриця <span>\(P = [[0, 1, 0], [0, 0, 0], [1, 0, 1]]\)</span> має визначник, що дорівнює 0, і тому не має оберненої.</p>

<pre><span></span><span>from</span> <span>numpy.linalg</span> <span>import</span> <span>inv</span>

<span>print</span><span>(</span><span>'Обернена M:</span><span>\n</span><span>'</span><span>,</span> <span>inv</span><span>(</span><span>M</span><span>))</span>
<span>P</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>0</span><span>,</span><span>1</span><span>,</span><span>0</span><span>],</span>
              <span>[</span><span>0</span><span>,</span><span>0</span><span>,</span><span>0</span><span>],</span>
              <span>[</span><span>1</span><span>,</span><span>0</span><span>,</span><span>1</span><span>]])</span>
<span>print</span><span>(</span><span>'det(p):</span><span>\n</span><span>'</span><span>,</span> <span>det</span><span>(</span><span>P</span><span>))</span>
</pre>

<pre><span></span>Inv M:
 [[-1.57894737 -0.07894737  1.23684211  1.10526316]
 [-0.63157895 -0.13157895  0.39473684  0.84210526]
 [ 0.68421053  0.18421053 -0.55263158 -0.57894737]
 [ 0.52631579  0.02631579 -0.07894737 -0.36842105]]
det(p):
 0.0
</pre>

<p>Матриця, яка близька до виродженої (тобто, визначник близький до 0), називається <strong>погано обумовленою</strong>. Хоча погано обумовлені матриці мають обернені, вони є проблематичними з чисельної точки зору так само, як і ділення числа на дуже, дуже мале число. Тобто, це може призвести до обчислень, які спричиняють переповнення, втрату значущості або числа, достатньо малі, щоб призвести до значних помилок округлення (якщо ви забули ці поняття, освіжіть їх у розділі 9). <strong>Число обумовленості</strong> — це міра того, наскільки погано обумовлена матриця, і його можна обчислити за допомогою функції <em>cond</em> з пакета <em>linalg</em> бібліотеки Numpy. Чим вище число обумовленості, тим ближче матриця до виродженої.</p>
<p><strong>Ранг</strong> матриці <span>\({m} \times {n}\)</span>, <span>\(A\)</span>, — це кількість лінійно незалежних стовпців або рядків <span>\(A\)</span>, і позначається як rank(<span>\(A\)</span>). Можна показати, що кількість лінійно незалежних рядків завжди дорівнює кількості лінійно незалежних стовпців для будь-якої матриці. Матриця називається <strong>матрицею повного рангу</strong>, якщо rank <span>\((A)=\min(m,n)\)</span>. Матриця <span>\(A\)</span> також є матрицею повного рангу, якщо всі її стовпці лінійно незалежні. <strong>Розширена матриця</strong> — це матриця <span>\(A\)</span>, об'єднана з вектором <span>\(y\)</span>, і записується як <span>\([A,y]\)</span>. Це зазвичай читається як "<span>\(A\)</span>, розширена <span>\(y\)</span>". Ви можете використовувати <em>np.concatenate</em> для їх об'єднання. Якщо <span>\(rank([A,y]) = {rank}(A) + 1\)</span>, то вектор <span>\(y\)</span> є "новою" інформацією. Тобто, його не можна створити як лінійну комбінацію стовпців у <span>\(A\)</span>. Ранг є важливою властивістю матриць через його зв'язок з розв'язками лінійних рівнянь, що обговорюється в останньому розділі цієї глави.</p>
<p><strong>СПРОБУЙТЕ!</strong> Матриця <span>\(A = [[1, 1, 0], [0, 1, 0], [1, 0, 1]]\)</span>. Обчисліть число обумовленості та ранг для цієї матриці. Якщо <span>\(y = [[1], [2], [1]]\)</span>, отримайте розширену матрицю [A, y].</p>

<pre><span></span><span>from</span> <span>numpy.linalg</span> <span>import</span> \
             <span>cond</span><span>,</span> <span>matrix_rank</span>

<span>A</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>1</span><span>,</span><span>1</span><span>,</span><span>0</span><span>],</span>
              <span>[</span><span>0</span><span>,</span><span>1</span><span>,</span><span>0</span><span>],</span>
              <span>[</span><span>1</span><span>,</span><span>0</span><span>,</span><span>1</span><span>]])</span>

<span>print</span><span>(</span><span>'Число обумовленості:</span><span>\n</span><span>'</span><span>,</span> <span>cond</span><span>(</span><span>A</span><span>))</span>
<span>print</span><span>(</span><span>'Ранг:</span><span>\n</span><span>'</span><span>,</span> <span>matrix_rank</span><span>(</span><span>A</span><span>))</span>
<span>y</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>1</span><span>],</span> <span>[</span><span>2</span><span>],</span> <span>[</span><span>1</span><span>]])</span>
<span>A_y</span> <span>=</span> <span>np</span><span>.</span><span>concatenate</span><span>((</span><span>A</span><span>,</span> <span>y</span><span>),</span> <span>axis</span> <span>=</span> <span>1</span><span>)</span>
<span>print</span><span>(</span><span>'Розширена матриця:</span><span>\n</span><span>'</span><span>,</span> <span>A_y</span><span>)</span>
</pre>

<pre><span></span>Condition number:
 4.048917339522305
Rank:
 3
Розширена матриця:
 [[1 1 0 1]
 [0 1 0 2]
 [1 0 1 1]]
</pre>
