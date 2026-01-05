```html
<h1>Підсумок<a href="#summary" title="Permalink to this headline"></a></h1>
<ol>
<li><p>Звичайні диференціальні рівняння (ЗДР) — це рівняння, які пов'язують функцію з її похідними, а задачі з початковими умовами є специфічним видом задач розв'язання ЗДР.</p></li>
<li><p>Більшість задач з початковими умовами неможливо проінтегрувати аналітично, тому вони вимагають чисельних розв'язків.</p></li>
<li><p>Існують явні, неявні та предиктор-коректорні методи для чисельного розв'язання задач з початковими умовами.</p></li>
<li><p>Точність використовуваної схеми залежить від її порядку апроксимації ЗДР.</p></li>
<li><p>Стійкість використовуваної схеми залежить від ЗДР, самої схеми та вибору параметрів інтегрування.</p></li>
</ol>


<h1>Задачі<a href="#problems" title="Permalink to this headline"></a></h1>
<ol>
<li><p>Логістичне рівняння — це проста модель диференціального рівняння, яку можна використовувати для зв'язку зміни популяції <span>\(\frac{dP}{dt}\)</span> з поточною популяцією, <span>\(P\)</span>, за заданого темпу зростання, <span>\(r\)</span>, та ємності середовища, <span>\(K\)</span>. Логістичне рівняння можна виразити так:</p></li>
</ol>

\[
\frac{dP}{dt}=rP\left(1-\frac{P}{K}\right)
\]
<p>Напишіть функцію <span>\(my\_logistics\_eq(t, P, r, K)\)</span>, яка представляє логістичне рівняння і повертає <span>\(dP\)</span>. Зауважте, що такий формат дозволяє використовувати <span>\(my\_logistics\_eq\)</span> як вхідний аргумент для <em>solve_ivp</em>. Можна припустити, що аргументи <span>\(dP\)</span>, <span>\(t\)</span>, <span>\(P\)</span>, <span>\(r\)</span> та <span>\(K\)</span> є скалярами, а <span>\(dP\)</span> — це значення <span>\(\frac{dP}{dt}\)</span> для заданих <span>\(r\)</span>, <span>\(P\)</span> та <span>\(K\)</span>. Зауважте, що вхідний аргумент <span>\(t\)</span> є обов'язковим, якщо <span>\(my\_logistics\_eq\)</span> буде використовуватися як вхідний аргумент для <em>solve_ivp</em>, хоча він і є частиною диференціального рівняння.</p>
<p>Примітка: Логістичне рівняння має аналітичний розв'язок, що визначається:</p>

\[
P(t)=\frac{KP_0e^{rt}}{K + P_0(e^{rt}-1)}
\]
<p>де <span>\(P_0\)</span> — початкова популяція. Як вправу, перевірте, що це рівняння є розв'язком логістичного рівняння.</p>
<p>Тестові приклади:</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
<span>from</span> <span>scipy.integrate</span> <span>import</span> <span>solve_ivp</span>
<span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>
<span>from</span> <span>functools</span> <span>import</span> <span>partial</span>
<span>plt</span><span>.</span><span>style</span><span>.</span><span>use</span><span>(</span><span>'seaborn-poster'</span><span>)</span>

<span>%</span><span>matplotlib</span> inline
</pre>





<pre><span></span><span>def</span> <span>my_logisitcs_eq</span><span>(</span><span>t</span><span>,</span> <span>P</span><span>,</span> <span>r</span><span>,</span> <span>K</span><span>):</span>
    <span># вставте ваш код тут</span>
    
    <span>return</span> <span>dP</span>

<span>dP</span> <span>=</span> <span>my_logisitcs_eq</span><span>(</span><span>0</span><span>,</span> <span>10</span><span>,</span> <span>1.1</span><span>,</span> <span>15</span><span>)</span>
<span>dP</span>
</pre>



<pre><span></span>3.666666666666667
</pre>





<pre><span></span><span>from</span> <span>functools</span> <span>import</span> <span>partial</span>

<span>t0</span> <span>=</span> <span>0</span>
<span>tf</span> <span>=</span> <span>20</span>
<span>P0</span> <span>=</span> <span>10</span>
<span>r</span> <span>=</span> <span>1.1</span>
<span>K</span> <span>=</span> <span>20</span>
<span>t</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>20</span><span>,</span> <span>2001</span><span>)</span>

<span>f</span> <span>=</span> <span>partial</span><span>(</span><span>my_logisitcs_eq</span><span>,</span> <span>r</span><span>=</span><span>r</span><span>,</span> <span>K</span><span>=</span><span>K</span><span>)</span>
<span>sol</span><span>=</span><span>solve_ivp</span><span>(</span><span>f</span><span>,[</span><span>t0</span><span>,</span><span>tf</span><span>],[</span><span>P0</span><span>],</span><span>t_eval</span><span>=</span><span>t</span><span>)</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span> <span>8</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>sol</span><span>.</span><span>t</span><span>,</span> <span>sol</span><span>.</span><span>y</span><span>[</span><span>0</span><span>])</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>t</span><span>,</span> \
  <span>K</span><span>*</span><span>P0</span><span>*</span><span>np</span><span>.</span><span>exp</span><span>(</span><span>r</span><span>*</span><span>t</span><span>)</span><span>/</span><span>(</span><span>K</span><span>+</span><span>P0</span><span>*</span><span>(</span><span>np</span><span>.</span><span>exp</span><span>(</span><span>r</span><span>*</span><span>t</span><span>)</span><span>-</span><span>1</span><span>)),</span><span>'r:'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'час'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'популяція'</span><span>)</span>

<span>plt</span><span>.</span><span>legend</span><span>([</span><span>'Чисельний розв\\'язок'</span><span>,</span> \
            <span>'Точний розв\\'язок'</span><span>])</span>
<span>plt</span><span>.</span><span>grid</span><span>(</span><span>True</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter22.08-Summary-and-Problems_6_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter22.08-Summary-and-Problems_6_0.png"/>


<ol>
<li><p>Атрактор Лоренца — це система звичайних диференціальних рівнянь, яка спочатку була розроблена для моделювання конвекційних потоків в атмосфері. Рівняння Лоренца можна записати так:
$$</p></li>
</ol>

\[\begin{eqnarray*}
&amp;&amp; \frac{dx}{dt}=\sigma (y-x)\\
&amp;&amp; \frac{dy}{dt} = x(\rho -z)-y\\
&amp;&amp; \frac{dz}{dt} = xy-\beta z
\end{eqnarray*}\]
<p>$$</p>
<p>де <span>\(x\)</span>, <span>\(y\)</span> та <span>\(z\)</span> представляють положення в трьох вимірах, а <span>\(\sigma, \rho\)</span> та <span>\(\beta\)</span> є скалярними параметрами системи. Ви можете прочитати більше про атрактор Лоренца у Вікіпедії: <a href="https://uk.wikipedia.org/wiki/Атрактор_Лоренца">Система Лоренца</a>.</p>
<p>Напишіть функцію <span>\(my\_lorenz(t,S,sigma,rho,beta)\)</span>, де <span>\(t\)</span> — скаляр, що позначає час, <span>\(S\)</span> — масив розміром <span>\((3, )\)</span>, що позначає положення <span>\((x,y,z)\)</span>, а <span>\(sigma\)</span>, <span>\(rho\)</span> та <span>\(beta\)</span> — строго додатні скаляри, що представляють <span>\(\sigma, \rho\)</span> та <span>\(\beta\)</span>. Вихідний аргумент <span>\(dS\)</span> повинен мати такий самий розмір, як і <span>\(S\)</span>.</p>
<p>Тестові приклади:</p>


<pre><span></span><span>def</span> <span>my_lorenz</span><span>(</span><span>t</span><span>,</span> <span>S</span><span>,</span> <span>sigma</span><span>,</span> <span>rho</span><span>,</span> <span>beta</span><span>):</span>
    <span># вставте ваш код тут</span>

    <span>return</span> <span>dS</span>

<span>s</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([</span><span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>])</span>
<span>dS</span> <span>=</span> <span>my_lorenz</span><span>(</span><span>0</span><span>,</span> <span>s</span><span>,</span> <span>10</span><span>,</span> <span>28</span><span>,</span> <span>8</span><span>/</span><span>3</span><span>)</span>
<span>dS</span>
</pre>



<pre><span></span>array([10., 23., -6.])
</pre>



<ol>
<li><p>Напишіть функцію <span>\(my\_lorenz\_solver(t\_span, s0, sigma, rho, beta)\)</span>, яка розв'язує рівняння Лоренца за допомогою <span>\(solve\_ivp\)</span>, функція повертає [T, X, Y, Z]. Вхідний аргумент <span>\(t\_span\)</span> повинен бути списком у формі <span>\([t0, tf]\)</span>, де <span>\(t0\)</span> — початковий час, а <span>\(tf\)</span> — кінцевий час розгляду. Вхідний аргумент <span>\(s0\)</span> повинен бути масивом розміром <span>\((3,)\)</span> у формі <span>\([x0; y0; z0]\)</span>, де <span>\((x_0, y_0, z_0)\)</span> представляє початкове положення. Нарешті, вхідні аргументи <span>\(sigma\)</span>, <span>\(rho\)</span> та <span>\(beta\)</span> є скалярними параметрами <span>\(\sigma, \rho\)</span> та <span>\(\beta\)</span> системи Лоренца. Вихідні аргументи <span>\(T\)</span> повинні бути масивом часів, отриманим як вихідний аргумент <span>\(solve\_ivp\)</span>. Вихідні аргументи <span>\(X\)</span>, <span>\(Y\)</span> та <span>\(Z\)</span> повинні бути чисельно проінтегрованим розв'язком, отриманим з <span>\(my\_lorenz\)</span> з попередньої задачі та <span>\(solve\_ivp\)</span>.</p></li>
</ol>
<p>Тестові приклади:</p>


<pre><span></span><span>def</span> <span>my_lorenz_solver</span><span>(</span><span>t_span</span><span>,</span> <span>s0</span><span>,</span> <span>sigma</span><span>,</span> <span>rho</span><span>,</span> <span>beta</span><span>):</span>
    <span># вставте ваш код тут</span>
    
    <span>return</span> <span>[</span><span>T</span><span>,</span> <span>X</span><span>,</span> <span>Y</span><span>,</span> <span>Z</span><span>]</span>

<span>sigma</span> <span>=</span> <span>10</span>
<span>rho</span> <span>=</span> <span>28</span>
<span>beta</span> <span>=</span> <span>8</span><span>/</span><span>3</span>
<span>t0</span> <span>=</span> <span>0</span>
<span>tf</span> <span>=</span> <span>50</span>
<span>s0</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([</span><span>0</span><span>,</span> <span>1</span><span>,</span> <span>1.05</span><span>])</span>

<span>[</span><span>T</span><span>,</span> <span>X</span><span>,</span> <span>Y</span><span>,</span> <span>Z</span><span>]</span> <span>=</span> <span>my_lorenz_solver</span><span>([</span><span>t0</span><span>,</span> <span>tf</span><span>],</span> \
                        <span>s0</span><span>,</span> <span>sigma</span><span>,</span> <span>rho</span><span>,</span> <span>beta</span><span>)</span>

<span>from</span> <span>mpl_toolkits</span> <span>import</span> <span>mplot3d</span>

<span>fig</span> <span>=</span> <span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span><span>10</span><span>))</span>
<span>ax</span> <span>=</span> <span>plt</span><span>.</span><span>axes</span><span>(</span><span>projection</span><span>=</span><span>'3d'</span><span>)</span>
<span>ax</span><span>.</span><span>grid</span><span>()</span>

<span>ax</span><span>.</span><span>plot3D</span><span>(</span><span>X</span><span>,</span> <span>Y</span><span>,</span> <span>Z</span><span>)</span>

<span># Встановити мітки осей</span>
<span>ax</span><span>.</span><span>set_xlabel</span><span>(</span><span>'x'</span><span>,</span> <span>labelpad</span><span>=</span><span>20</span><span>)</span>
<span>ax</span><span>.</span><span>set_ylabel</span><span>(</span><span>'y'</span><span>,</span> <span>labelpad</span><span>=</span><span>20</span><span>)</span>
<span>ax</span><span>.</span><span>set_zlabel</span><span>(</span><span>'z'</span><span>,</span> <span>labelpad</span><span>=</span><span>20</span><span>)</span>

<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter22.08-Summary-and-Problems_10_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter22.08-Summary-and-Problems_10_0.png"/>


<ol>
<li><p>Розглянемо наступну модель системи маса-пружина-демпфер (МПД) в одному вимірі. На цьому рисунку <span>\(m\)</span> позначає масу блоку, <span>\(c\)</span> називається коефіцієнтом демпфування, а <span>\(k\)</span> — жорсткістю пружини. Демпфер — це механізм, який розсіює енергію в системі, створюючи опір швидкості. Система МПД є спрощеною моделлю для багатьох інженерних застосувань, таких як амортизатори та конструкційні системи.</p></li>
</ol>

<p>Зв'язок між прискоренням, швидкістю та зміщенням можна виразити наступним диференціальним рівнянням системи маса-пружина-демпфер (МПД):</p>

\[
m\ddot{x} + c\dot{x} +kx = 0
\]
<p>яке можна переписати так:
$<span>\(
\ddot{x}=\frac{-(c\dot{x}+kx)}{m}
\)</span>$</p>
<p>Нехай стан системи позначається вектором <span>\(S = [x; v]\)</span>, де <span>\(x\)</span> — зміщення маси від її положення спокою, а <span>\(v\)</span> — її швидкість. Перепишіть рівняння МПД як диференціальне рівняння першого порядку в термінах стану <span>\(S\)</span>. Іншими словами, перепишіть рівняння МПД як <span>\(dS/dt = f(t, S)\)</span>.</p>
<p>Напишіть функцію <span>\(my\_msd(t, S, m, c, k)\)</span>, де <span>\(t\)</span> — скаляр, що позначає час, <span>\(S\)</span> — вектор розміром <span>\((2,)\)</span>, що позначає стан системи МПД, а <span>\(m\)</span>, <span>\(c\)</span> та <span>\(k\)</span> — коефіцієнти маси, демпфування та жорсткості рівняння МПД відповідно.</p>
<p>Тестові приклади:</p>


<pre><span></span><span>def</span> <span>my_msd</span><span>(</span><span>t</span><span>,</span> <span>S</span><span>,</span> <span>m</span><span>,</span> <span>c</span><span>,</span> <span>k</span><span>):</span>
    <span># вставте ваш код тут</span>
    <span>return</span> <span>ds</span>

<span>my_msd</span><span>(</span><span>0</span><span>,</span> <span>[</span><span>1</span><span>,</span> <span>-</span><span>1</span><span>],</span> <span>10</span><span>,</span> <span>1</span><span>,</span> <span>100</span><span>)</span>
</pre>



<pre><span></span>array([-1. , -9.9])
</pre>





<pre><span></span><span>m</span> <span>=</span> <span>1</span>
<span>k</span> <span>=</span> <span>10</span>
<span>f</span> <span>=</span> <span>partial</span><span>(</span><span>my_msd</span><span>,</span> <span>m</span><span>=</span><span>m</span><span>,</span> <span>c</span><span>=</span><span>0</span><span>,</span> <span>k</span><span>=</span><span>k</span><span>)</span>
<span>t_e</span> <span>=</span> <span>np</span><span>.</span><span>arange</span><span>(</span><span>0</span><span>,</span> <span>20</span><span>,</span> <span>0.1</span><span>)</span>
<span>sol_1</span><span>=</span><span>solve_ivp</span><span>(</span><span>f</span><span>,[</span><span>0</span><span>,</span><span>20</span><span>],[</span><span>1</span><span>,</span><span>0</span><span>],</span><span>t_eval</span><span>=</span><span>t_e</span><span>)</span>

<span>f</span> <span>=</span> <span>partial</span><span>(</span><span>my_msd</span><span>,</span> <span>m</span><span>=</span><span>m</span><span>,</span> <span>c</span><span>=</span><span>1</span><span>,</span> <span>k</span><span>=</span><span>k</span><span>)</span>
<span>sol_2</span><span>=</span><span>solve_ivp</span><span>(</span><span>f</span><span>,[</span><span>0</span><span>,</span><span>20</span><span>],[</span><span>1</span><span>,</span><span>0</span><span>],</span><span>t_eval</span><span>=</span><span>t_e</span><span>)</span>

<span>f</span> <span>=</span> <span>partial</span><span>(</span><span>my_msd</span><span>,</span> <span>m</span><span>=</span><span>m</span><span>,</span> <span>c</span><span>=</span><span>10</span><span>,</span> <span>k</span><span>=</span><span>k</span><span>)</span>
<span>sol_3</span><span>=</span><span>solve_ivp</span><span>(</span><span>f</span><span>,[</span><span>0</span><span>,</span><span>20</span><span>],[</span><span>1</span><span>,</span><span>0</span><span>],</span><span>t_eval</span><span>=</span><span>t_e</span><span>)</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span> <span>8</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>sol_1</span><span>.</span><span>t</span><span>,</span> <span>sol_1</span><span>.</span><span>y</span><span>[</span><span>0</span><span>])</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>sol_2</span><span>.</span><span>t</span><span>,</span> <span>sol_2</span><span>.</span><span>y</span><span>[</span><span>0</span><span>])</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>sol_3</span><span>.</span><span>t</span><span>,</span> <span>sol_3</span><span>.</span><span>y</span><span>[</span><span>0</span><span>])</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>'Чисельний розв\\'язок системи МПД </span><span>\
</span><span>зі змінним демпфуванням'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'час'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'зміщення'</span><span>)</span>
<span>plt</span><span>.</span><span>legend</span><span>([</span><span>'без демпфування'</span><span>,</span> <span>'c=1'</span><span>,</span> \
           <span>'&gt;критичне демпфування'</span><span>],</span> <span>loc</span><span>=</span><span>1</span><span>)</span>
</pre>



<pre><span></span>&lt;matplotlib.legend.Legend at 0x1531a2f400&gt;
</pre>

<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter22.08-Summary-and-Problems_13_1.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter22.08-Summary-and-Problems_13_1.png"/>


<ol>
<li><p>Напишіть функцію <span>\(my\_forward\_euler(ds, t\_span, s0)\)</span>, де <em>ds</em> — це об'єкт-функція <span>\(f(t, s)\)</span>, що описує диференціальне рівняння першого порядку, <span>\(t\_span\)</span> — масив часів, для яких потрібні чисельні розв'язки диференціального рівняння, а <em>s0</em> — початкова умова системи. Припустимо, що розмірність стану дорівнює одиниці. Вихідний аргумент повинен бути списком [t, s] таким, що <span>\(t[i] = t\_span[i]\)</span> для всіх <span>\(i\)</span>, а <span>\(s\)</span> — проінтегровані значення <em>ds</em> у моменти часу <em>t</em>. Ви повинні виконати інтегрування за допомогою явного методу Ейлера: <span>\(s[t_i] = s[t_{i-1}] + (t_i - t_{i-1}) ds(t_{i-1}, s[t_{i-1}])\)</span>. Примітка: <span>\(s[0]\)</span> має дорівнювати <span>\(s0\)</span>.</p></li>
</ol>
<p>Тестові приклади:</p>


<pre><span></span><span>def</span> <span>my_forward_euler</span><span>(</span><span>ds</span><span>,</span> <span>t_span</span><span>,</span> <span>s0</span><span>):</span>
    <span># вставте ваш код тут</span>
    
    <span>return</span> <span>[</span><span>t</span><span>,</span> <span>s</span><span>]</span>

<span>t_span</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>1</span><span>,</span> <span>10</span><span>)</span>
<span>s0</span> <span>=</span> <span>1</span>

<span># Визначення параметрів</span>
<span>f</span> <span>=</span> <span>lambda</span> <span>t</span><span>,</span> <span>s</span><span>:</span> <span>t</span><span>*</span><span>np</span><span>.</span><span>exp</span><span>(</span><span>-</span><span>s</span><span>)</span>

<span>t_eul</span><span>,</span> <span>s_eul</span> <span>=</span> <span>my_forward_euler</span><span>(</span><span>f</span><span>,</span> <span>t_span</span><span>,</span> <span>s0</span><span>)</span>

<span>print</span><span>(</span><span>t_eul</span><span>)</span>
<span>print</span><span>(</span><span>s_eul</span><span>)</span>
</pre>



<pre><span></span>[0.         0.11111111 0.22222222 0.33333333 0.44444444 0.55555556
 0.66666667 0.77777778 0.88888889 1.        ]
[1.         1.         1.00454172 1.013584   1.02702534 1.04470783
 1.06642355 1.09192262 1.12092255 1.153118  ]
</pre>





<pre><span></span><span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span> <span>8</span><span>))</span>

<span># Точний розв'язок</span>
<span>t</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>1</span><span>,</span> <span>1000</span><span>)</span>
<span>s</span> <span>=</span> <span>np</span><span>.</span><span>log</span><span>(</span><span>np</span><span>.</span><span>exp</span><span>(</span><span>s0</span><span>)</span> <span>+</span> <span>(</span><span>t</span><span>**</span><span>2</span><span>-</span><span>t</span><span>[</span><span>0</span><span>])</span><span>/</span><span>2</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>t</span><span>,</span> <span>s</span><span>,</span> <span>'r'</span><span>,</span> <span>label</span><span>=</span><span>'Точний'</span><span>)</span>

<span># Явний метод Ейлера</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>t_eul</span><span>,</span> <span>s_eul</span><span>,</span> <span>'g'</span><span>,</span> <span>label</span><span>=</span><span>'Ейлер'</span><span>)</span>

<span># Розв'язувач Python</span>
<span>sol</span> <span>=</span> <span>solve_ivp</span><span>(</span><span>f</span><span>,</span> <span>[</span><span>0</span><span>,</span> <span>1</span><span>],</span> <span>[</span><span>s0</span><span>],</span> <span>t_eval</span><span>=</span><span>t</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>sol</span><span>.</span><span>t</span><span>,</span> <span>sol</span><span>.</span><span>y</span><span>[</span><span>0</span><span>],</span> <span>'b--'</span><span>,</span> \
         <span>label</span><span>=</span><span>'Розв\\'язувач Python'</span><span>)</span>

<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'t'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'f(t)'</span><span>)</span>
<span>plt</span><span>.</span><span>grid</span><span>()</span>
<span>plt</span><span>.</span><span>legend</span><span>(</span><span>loc</span><span>=</span><span>2</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter22.08-Summary-and-Problems_16_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter22.08-Summary-and-Problems_16_0.png"/>


<ol>
<li><p>Напишіть функцію <span>\(myRK4(ds, t_span, s0)\)</span>, де вхідні та вихідні аргументи такі ж, як у задачі 5. Функція <span>\(myRK4\)</span> повинна чисельно інтегрувати <em>ds</em> за допомогою методу Рунге-Кутти четвертого порядку.</p></li>
</ol>
<p>Тестові приклади:</p>


<pre><span></span><span>def</span> <span>myRK4</span><span>(</span><span>ds</span><span>,</span> <span>t_span</span><span>,</span> <span>s0</span><span>):</span>
    <span># вставте ваш код тут</span>
    
    <span>return</span> <span>[</span><span>t</span><span>,</span> <span>s</span><span>]</span>

<span>f</span> <span>=</span> <span>lambda</span> <span>t</span><span>,</span> <span>s</span><span>:</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>np</span><span>.</span><span>exp</span><span>(</span><span>s</span><span>))</span><span>/</span><span>(</span><span>t</span><span>+</span><span>1</span><span>)</span>
<span>t_span</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>2</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>,</span> <span>10</span><span>)</span>
<span>s0</span> <span>=</span> <span>0</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span> <span>8</span><span>))</span>

<span># Метод Рунге-Кутти</span>
<span>t</span><span>,</span> <span>s</span> <span>=</span> <span>myRK4</span><span>(</span><span>f</span><span>,</span> <span>t_span</span><span>,</span> <span>s0</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>t</span><span>,</span> <span>s</span><span>,</span> <span>'r'</span><span>,</span> <span>label</span><span>=</span><span>'РК4'</span><span>)</span>

<span># Розв'язувач Python</span>
<span>sol</span> <span>=</span> <span>solve_ivp</span><span>(</span><span>f</span><span>,</span> <span>[</span><span>0</span><span>,</span> <span>2</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>],</span> <span>[</span><span>s0</span><span>],</span> <span>t_eval</span><span>=</span><span>t</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>sol</span><span>.</span><span>t</span><span>,</span> <span>sol</span><span>.</span><span>y</span><span>[</span><span>0</span><span>],</span> \
         <span>'b--'</span><span>,</span> <span>label</span><span>=</span><span>'Розв\\'язувач Python'</span><span>)</span>

<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'t'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'f(t)'</span><span>)</span>
<span>plt</span><span>.</span><span>grid</span><span>()</span>
<span>plt</span><span>.</span><span>legend</span><span>(</span><span>loc</span><span>=</span><span>2</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter22.08-Summary-and-Problems_18_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter22.08-Summary-and-Problems_18_0.png"/>
```
