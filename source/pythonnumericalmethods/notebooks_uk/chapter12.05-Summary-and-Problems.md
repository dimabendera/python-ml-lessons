<h1>Підсумок<a href="#summary" title="Permalink to this headline"></a></h1>
<ol>
<li><p>Візуалізація даних є важливим інструментом в інженерії та науці.</p></li>
<li><p>Python має багато різних бібліотек інструментів для побудови графіків, які можна використовувати для візуалізації даних.</p></li>
<li><p>2D, 3D графіки та карти зазвичай використовуються в інженерії та науці для представлення результатів досліджень.</p></li>
<li><p>Відео — це послідовність статичних зображень, що відображаються з певною швидкістю.</p></li>
</ol>


<h1>Задачі<a href="#problems" title="Permalink to this headline"></a></h1>
<ol>
<li><p>Циклоїда — це крива, яку описує точка, розташована на ободі колеса, що котиться по плоскій поверхні. Координати <span>\((x,y)\)</span> циклоїди, утвореної колесом радіусом <span>\(r\)</span>, можна описати параметричними рівняннями:</p></li>
</ol>
<p><span>\(x = r(\phi - \sin{\phi})\)</span></p>
<p><span>\(y = r(1 - \cos{\phi})\)</span></p>
<p>де <span>\(\phi\)</span> — це кількість радіанів, на яку прокотилося колесо.</p>
<p>Побудуйте графік циклоїди для <span>\(0 \le \phi \le 2\pi\)</span>, використовуючи 1000 кроків та <span>\(r = 3\)</span>. Дайте вашому графіку назву та підписи осей. Увімкніть сітку та змініть межі осей, щоб графік виглядав охайно.</p>
<ol>
<li><p>Розгляньте наступну функцію:</p></li>
</ol>
<p><span>\(y(x) = \sqrt{\frac{100(1-0.01x^2)^2 + 0.02x^2}{(1-x^2)^2 + 0.1x^2}}.\)</span></p>
<p>Створіть сітку графіків <span>\(2 \times 2\)</span> для <span>\(y(x)\)</span> в діапазоні <span>\(0 \le x \le 100\)</span>, використовуючи <em>plot</em>, <em>semilogx</em>, <em>semilogy</em> та <em>loglog</em>. Використовуйте достатньо дрібну дискретизацію по <em>x</em>, щоб графік виглядав гладким. Дайте кожному графіку підписи осей та назву. Увімкніть сітку. Який графік, на вашу думку, передає найбільше інформації?</p>
<ol>
<li><p>Побудуйте графіки функцій <span>\(y_1(x) = 3 + \exp{-x}\sin{(6x)}\)</span> та <span>\(y_2(x) = 4 + \exp{(-x)}\cos{(6x)}\)</span> для <span>\(0 \le x \le 5\)</span> на одній осі. Дайте графіку підписи осей, назву та легенду.</p></li>
<li><p>Згенеруйте 1000 нормально розподілених випадкових чисел за допомогою функції <em>np.random.randn</em>. Перегляньте документацію для функції <em>plt.hist</em>. Використовуйте функцію <em>plt.hist</em>, щоб побудувати гістограму згенерованих випадкових чисел. Використовуйте функцію <em>plt.hist</em>, щоб розподілити згенеровані випадкові числа на 10 стовпців (бінів). Створіть стовпчасту діаграму з виводу hist за допомогою функції <em>plt.bar</em>. Вона повинна виглядати дуже схоже на графік, створений <em>plt.hist</em>.</p></li>
</ol>
<p>Чи вважаєте ви, що функція <em>np.random.randn</em> є хорошою апроксимацією нормально розподіленого числа?</p>
<ol>
<li><p>Нехай кількість студентів з оцінками A, B, C, D та F міститься у списку <em>grade_dist = [42, 85, 67, 20, 5]</em>. Використовуйте функцію <em>plt.pie</em>, щоб створити кругову діаграму для <em>grade_dist</em>. Додайте до діаграми назву та легенду.</p></li>
<li><p>Нехай <span>\(-4 \le x \le 4, -3 \le y \le 3\)</span>, та <span>\(z(x,y) = \frac{xy(x^2 - y^2)}{x^2 + y^2}\)</span>. Створіть масиви <em>x</em> та <em>y</em> зі 100 рівномірно розташованими точками в заданому інтервалі. Створіть координатні сітки <em>X</em> та <em>Y</em> для <em>x</em> та <em>y</em> за допомогою функції <em>meshgrid</em>. Обчисліть матрицю <em>Z</em> з <em>X</em> та <em>Y</em>. Створіть сітку графіків <span>\(1 \times 2\)</span>, де перший графік — це 3D-поверхня <em>Z</em>, побудована за допомогою <em>plt.plot_surface</em>, а другий — 3D-каркасний графік, побудований за допомогою <em>plt.plot_wireframe</em>. Дайте кожному графіку назву та підписи осей.</p></li>
<li><p>Напишіть функцію <em>my_polygon(n)</em>, яка будує правильний багатокутник з <em>n</em> сторонами та радіусом 1. Нагадаємо, що радіус правильного багатокутника — це відстань від його центра до вершин. Використовуйте <em>plt.axis(‘equal`)</em>, щоб багатокутник виглядав правильним. Не забудьте дати осям підписи та назву. Ви можете використовувати <em>plt.title</em>, щоб назвати графік відповідно до кількості сторін. Підказка: ця задача значно простіша, якщо думати в полярних координатах. Нагадаємо, що повний оберт навколо одиничного кола становить <span>\(2\pi\)</span> радіан. Примітка: перша та остання точки на багатокутнику повинні бути точками, що відповідають полярним кутам <span>\(0\)</span> та <span>\(2\pi\)</span> відповідно.</p></li>
</ol>
<p>Тестові випадки:</p>
<pre><span></span><span>my_polygon</span><span>(</span><span>5</span><span>)</span>
</pre>


<ol>
<li><p>Напишіть функцію <em>my_fun_plotter(f, x)</em>, де f — це лямбда-функція, а x — масив. Функція повинна будувати графік <em>f</em>, обчисленої в точках <em>x</em>. Не забудьте підписати осі x та y.</p></li>
</ol>
<p>Тестові випадки:</p>
<pre><span></span><span>my_fun_plotter</span><span>(</span><span>lambda</span> <span>x</span><span>:</span> <span>np</span><span>.</span><span>sqrt</span><span>(</span><span>x</span><span>)</span> <span>+</span> <span>np</span><span>.</span><span>exp</span><span>(</span><span>np</span><span>.</span><span>sin</span><span>(</span><span>x</span><span>)),</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>2</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>,</span> <span>100</span><span>))</span>
</pre>


<ol>
<li><p>Напишіть функцію <em>my_poly_plotter (n,x)</em>, яка будує графіки поліномів <span>\(p_k(x) = x^k\)</span> для <span>\(k = 1,\ldots,n\)</span>. Переконайтеся, що ваш графік має підписи осей та назву.</p></li>
</ol>
<p>Тестові випадки:</p>
<pre><span></span><span>my_poly_plotter</span><span>(</span><span>5</span><span>,</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>-</span><span>1</span><span>,</span> <span>1</span><span>,</span> <span>200</span><span>))</span>
</pre>


<ol>
<li><p>Припустимо, у вас є три точки у вершинах рівностороннього трикутника: <span>\(P_1 = (0,0), P_2 = (0.5,\sqrt{2}/2)\)</span> та <span>\(P_3 = (1,0)\)</span>. Тепер ви хочете згенерувати інший набір точок <span>\(p_i = (x_i, y_i)\)</span> так, що <span>\(p_1 = (0,0)\)</span>, а <span>\(p_{i+1}\)</span> є серединою відрізка між <span>\(p_i\)</span> та <span>\(P_1\)</span> з імовірністю 33%, серединою відрізка між <span>\(p_i\)</span> та <span>\(P_2\)</span> з імовірністю 33%, і серединою відрізка між <span>\(p_i\)</span> та <span>\(P_3\)</span> з імовірністю 33%. Напишіть функцію <em>my_sierpinski (n)</em>, яка генерує точки <span>\(p_i\)</span> для <span>\(i = 1,\cdots,n\)</span>. Функція повинна побудувати графік точок, використовуючи сині крапки (тобто ‘b.` як третій аргумент функції <em>plt.plot</em>).</p></li>
</ol>
<p>Тестові випадки:</p>
<pre><span></span><span>my_sierpinski</span><span>(</span><span>100</span><span>)</span>
</pre>


<pre><span></span><span>my_sierpinski</span><span>(</span><span>10000</span><span>)</span>
</pre>


<ol>
<li><p>Припустимо, ви генеруєте набір точок <span>\((x_i, y_i)\)</span>, де <span>\(x_1 = 0\)</span> та <span>\(y_1 = 0\)</span>. Точки <span>\((x_i, y_i)\)</span> для <span>\(i = 2,\cdots,n\)</span> генеруються відповідно до наступного імовірнісного співвідношення:</p></li>
</ol>
<p>З імовірністю 1%:</p>
<p><span>\(x_i = 0\)</span></p>
<p><span>\(y_i = 0.16y_{i-1}\)</span></p>
<p>З імовірністю 7%:</p>
<p><span>\(x_i = 0.2x_{i-1} - 0.26y_{i-1}\)</span></p>
<p><span>\(y_i = 0.23x_{i-1} + 0.22y_{i-1} + 1.6\)</span></p>
<p>З імовірністю 7%:</p>
<p><span>\(x_i = -0.15x_{i-1} + 0.28y_{i-1}\)</span></p>
<p><span>\(y_i = 0.26x_{i-1} + 0.24y_{i-1} + 0.44\)</span></p>
<p>З імовірністю 85%:</p>
<p><span>\(x_i = 0.85x_{i-1} + 0.04y_{i-1}\)</span></p>
<p><span>\(y_i = -0.04x_{i-1} + 0.85y_{i-1} + 1.6\)</span></p>
<p>Напишіть функцію <em>my_fern (n)</em>, яка генерує точки <span>\((x_i,y_i)\)</span> для <span>\(i = 1,\ldots,n\)</span> та будує їх графік, використовуючи сині крапки. Також використовуйте <em>plt.axis(‘equal`)</em> та <em>plt.axis(‘off`)</em>, щоб графік виглядав краще.</p>
<p>Тестові випадки:</p>
<pre><span></span><span>my_fern</span><span>(</span><span>100</span><span>)</span>
</pre>


<p>Спробуйте вашу функцію для n = 10000. Згенероване зображення називається стохастичним фракталом. Часто дешевше (тобто вимагає менше місця) зберігати код, що генерує фрактал, аніж саме зображення. Це робить стохастичні фрактали корисними для стиснення зображень.</p>
<pre><span></span><span>my_fern</span><span>(</span><span>10000</span><span>)</span>
</pre>


<ol>
<li><p>Напишіть функцію <em>my_parametric_plotter (x,y,t)</em>, де <em>x</em> та <em>y</em> є об'єктами-функціями <em>x (t)</em> та <em>y (t)</em> відповідно, а <em>t</em> — одновимірний масив. Функція <em>my_parametric_plotter</em> повинна створювати криву <span>\((x(t), y(t), t)\)</span> на тривимірному графіку. Обов'язково дайте вашому графіку назву та підписи осей.</p></li>
</ol>
<p>Тестові випадки:</p>
<pre><span></span><span>from</span> <span>mpl_toolkits</span> <span>import</span> <span>mplot3d</span>
<span>f</span> <span>=</span> <span>lambda</span> <span>t</span><span>:</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>t</span><span>)</span>
<span>g</span> <span>=</span> <span>lambda</span> <span>t</span><span>:</span> <span>t</span><span>**</span><span>2</span>
<span>my_parametric_plotter</span><span>(</span><span>f</span><span>,</span> <span>g</span><span>,</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>6</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>,</span> <span>100</span><span>))</span>
   
</pre>


<ol>
<li><p>Напишіть функцію <em>my_surface_plotter(f, x, y, option)</em>, де <em>f</em> — це об'єкт-функція <em>f (x,y)</em>. Функція <em>my_surface_plotter</em> повинна створювати 3D-графік поверхні <em>f (x,y)</em> за допомогою <em>plot_surface</em>, якщо `option` — це рядок ‘surface`. Вона повинна створювати контурний графік <em>f (x,y)</em>, якщо `option` — це рядок ‘contour`. Припустимо, що <em>x</em> та <em>y</em> є одновимірними масивами або списками. Не забудьте дати графіку назву та підписи осей.</p></li>
</ol>
<p>Тестові випадки:</p>
<pre><span></span><span>from</span> <span>mpl_toolkits</span> <span>import</span> <span>mplot3d</span>
<span>f</span> <span>=</span> <span>lambda</span> <span>x</span><span>,</span> <span>y</span><span>:</span> <span>np</span><span>.</span><span>cos</span><span>(</span><span>y</span><span>)</span><span>*</span><span>np</span><span>.</span><span>sin</span><span>(</span><span>np</span><span>.</span><span>exp</span><span>(</span><span>x</span><span>))</span>
<span>my_surface_plotter</span><span>(</span><span>f</span><span>,</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>-</span><span>1</span><span>,</span> <span>1</span><span>,</span> <span>20</span><span>),</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>-</span><span>2</span><span>,</span> <span>2</span><span>,</span> <span>40</span><span>),</span> <span>'surface'</span><span>)</span>
<span>my_surface_plotter</span><span>(</span><span>f</span><span>,</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>-</span><span>1</span><span>,</span> <span>1</span><span>,</span> <span>20</span><span>),</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>-</span><span>2</span><span>,</span> <span>2</span><span>,</span> <span>40</span><span>),</span> <span>'contour'</span><span>)</span>
</pre>



<ol>
<li><p>Напишіть рядок коду, який генерує наступну помилку:</p></li>
</ol>
<pre><span></span><span>ValueError</span><span>:</span> <span>x</span> <span>and</span> <span>y</span> <span>must</span> <span>have</span> <span>same</span> <span>first</span> <span>dimension</span><span>,</span> <span>...</span>
</pre>

<ol>
<li><p>Ми можемо створювати карти, використовуючи різні онлайн-сервіси Web Map Tile Service (WMTS) у <em>cartopy</em>. Побудуйте карту нічної Землі, подібну до наведеної нижче, для основної частини Північної Америки, з широтою від 19.50139 до 64.85694 та довготою від -128.75583 до -68.01197. Підказка: перегляньте галерею на веб-сайті <em>cartopy</em>.</p></li>
</ol>
