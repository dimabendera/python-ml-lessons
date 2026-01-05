<h1>Методи пристрілки<a href="#the-shooting-methods" title="Постійне посилання на цей заголовок"></a></h1>
<p>**Методи пристрілки** розроблені з метою перетворення крайових задач для ЗДР (звичайних диференціальних рівнянь) на еквівалентні задачі з початковими умовами, які потім можна розв'язати методами, вивченими в попередньому розділі. У задачах з початковими умовами ми можемо почати з початкового значення і рухатися вперед, щоб отримати розв'язок. Але цей метод не працює для крайових задач, оскільки недостатньо початкових умов для розв'язання ЗДР та отримання унікального розв'язку. Тому методи пристрілки були розроблені для подолання цієї труднощі.</p>

<p>Назва методу пристрілки походить від аналогії зі стрільбою по мішені: як показано на малюнку вище, ми стріляємо по мішені та спостерігаємо, куди вона влучає, на основі помилок ми можемо скоригувати нашу ціль і стріляти знову в надії, що вона влучить близько до мішені. З цієї аналогії видно, що метод пристрілки є ітераційним методом.</p>
<p>Розглянемо, як працюють методи пристрілки, використовуючи ЗДР другого порядку, задане <span>\(f(a) = f_a\)</span> та <span>\(f(b) = f_b\)</span></p>

\[
F\left(x, f(x), \frac{df(x)}{dx}\right) = \frac{d^{2}f(x)}{dx^{2}}
\]
<p>**Крок 1:** Ми починаємо весь процес, припускаючи <span>\(f'(a)=\alpha\)</span>, разом з <span>\(f(a) = f_a\)</span>, ми перетворюємо вищезгадану задачу на задачу з початковими умовами, де обидві умови задані для значення <span>\(x=a\)</span>. Це крок **наведення**.<br/>
**Крок 2:** Використовуючи те, що ми вивчили в попередньому розділі, тобто метод Рунге-Кутти, ми інтегруємо до іншої границі <span>\(b\)</span>, щоб знайти <span>\(f(b) = f_\beta\)</span>. Це крок **пристрілки**.<br/>
**Крок 3:** Тепер ми порівнюємо значення <span>\(f_\beta\)</span> з <span>\(f_b\)</span>, зазвичай наше початкове припущення не є вдалим, і <span>\(f_\beta \ne f_b\)</span>, але ми хочемо, щоб <span>\(f_\beta - f_b = 0\)</span>, тому ми коригуємо наші початкові припущення і повторюємо. Доки похибка не стане прийнятною, ми можемо зупинитися. Це ітераційний крок.</p>
<p>Ми бачимо, що ідеї, що лежать в основі методів пристрілки, дуже прості. Але порівняння та пошук найкращих припущень не є легкими, ця процедура дуже виснажлива. Але по суті, знаходження найкращого припущення для отримання <span>\(f_\beta - f_b = 0\)</span> є задачею пошуку коренів, і як тільки ми це усвідомлюємо, ми маємо систематичний спосіб пошуку найкращого припущення. Оскільки <span>\(f_\beta\)</span> є функцією <span>\(\alpha\)</span>, задача зводиться до знаходження кореня рівняння <span>\(g(\alpha) - f_b = 0 \)</span>. Для її розв'язання ми можемо використовувати будь-які методи з розділу 19.</p>
<p>**СПРОБУЙТЕ!** Ми збираємося запустити ракету, і нехай <span>\(y(t)\)</span> — це висота (метри від поверхні) ракети в момент часу t. Ми знаємо прискорення вільного падіння <span>\(g = 9.8 м/с^2\)</span>. Якщо ми хочемо, щоб ракета була на висоті 50 м над землею через 5 секунд після запуску, якою має бути швидкість при запуску? (ми ігноруємо опір повітря).</p>
<p>Щоб відповісти на це питання, ми можемо сформулювати задачу як крайову задачу для ЗДР другого порядку. ЗДР має вигляд:</p>

\[ \frac{d^2y}{dt^2} = -g\]
<p>з двома граничними умовами: <span>\(y(0) = 0\)</span> та <span>\(y(5) = 50\)</span>. І ми хочемо відповісти на питання, якою є <span>\(y'(0)\)</span> при запуску?</p>
<p>Це досить просте питання, ми можемо легко розв'язати його аналітично, отримавши правильну відповідь <span>\(y'(0) = 34.5\)</span>. Тепер розв'яжемо її за допомогою методу пристрілки. Спочатку ми зменшимо порядок функції, ЗДР другого порядку перетворюється на:</p>

\[ \frac{dy}{dt} = v\]

\[ \frac{dv}{dt} = -g\]
<p>Отже, ми маємо <span>\(S(t) = \left[\begin{array}{c} y(t) \\v(t) \end{array}\right]\)</span>:</p>

\[\begin{split}
\frac{dS(t)}{dt} = \left[\begin{array}{cc}
0 &amp; 1 \\
0 &amp; -g/v
\end{array}\right]S(t).
\end{split}\]


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
<span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>
<span>from</span> <span>scipy.integrate</span> <span>import</span> <span>solve_ivp</span>
<span>plt</span><span>.</span><span>style</span><span>.</span><span>use</span><span>(</span><span>'seaborn-poster'</span><span>)</span>
<span>%</span><span>matplotlib</span> inline
</pre>



<p>Почнемо з нашого першого припущення: ми припускаємо, що швидкість при запуску становить 25 м/с.</p>


<pre><span></span><span>F</span> <span>=</span> <span>lambda</span> <span>t</span><span>,</span> <span>s</span><span>:</span> \
  <span>np</span><span>.</span><span>dot</span><span>(</span><span>np</span><span>.</span><span>array</span><span>([[</span><span>0</span><span>,</span><span>1</span><span>],[</span><span>0</span><span>,</span><span>-</span><span>9.8</span><span>/</span><span>s</span><span>[</span><span>1</span><span>]]]),</span><span>s</span><span>)</span>

<span>t_span</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>5</span><span>,</span> <span>100</span><span>)</span>
<span>y0</span> <span>=</span> <span>0</span>
<span>v0</span> <span>=</span> <span>25</span>
<span>t_eval</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>5</span><span>,</span> <span>10</span><span>)</span>
<span>sol</span> <span>=</span> <span>solve_ivp</span><span>(</span><span>F</span><span>,</span> <span>[</span><span>0</span><span>,</span> <span>5</span><span>],</span> \
                <span>[</span><span>y0</span><span>,</span> <span>v0</span><span>],</span> <span>t_eval</span> <span>=</span> <span>t_eval</span><span>)</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span> <span>8</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>sol</span><span>.</span><span>t</span><span>,</span> <span>sol</span><span>.</span><span>y</span><span>[</span><span>0</span><span>])</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>5</span><span>,</span> <span>50</span><span>,</span> <span>'ro'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'час (с)'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'висота (м)'</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>f</span><span>'перше припущення v=</span><span>{</span><span>v0</span><span>}</span><span> м/с'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter23.02-The-Shooting-Method_6_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter23.02-The-Shooting-Method_6_0.png"/>


<p>З малюнка видно, що перше припущення трохи замале, оскільки з цією швидкістю через 5 с висота ракети менша за 10 м. Червона точка на малюнку — це ціль, яку ми хочемо вразити. Тепер скоригуємо наше припущення та збільшимо швидкість до 40 м/с.</p>


<pre><span></span><span>v0</span> <span>=</span> <span>40</span>
<span>sol</span> <span>=</span> <span>solve_ivp</span><span>(</span><span>F</span><span>,</span> <span>[</span><span>0</span><span>,</span> <span>5</span><span>],</span> \
            <span>[</span><span>y0</span><span>,</span> <span>v0</span><span>],</span> <span>t_eval</span> <span>=</span> <span>t_eval</span><span>)</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span> <span>8</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>sol</span><span>.</span><span>t</span><span>,</span> <span>sol</span><span>.</span><span>y</span><span>[</span><span>0</span><span>])</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>5</span><span>,</span> <span>50</span><span>,</span> <span>'ro'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'час (с)'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'висота (м)'</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>f</span><span>'друге припущення v=</span><span>{</span><span>v0</span><span>}</span><span> м/с'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter23.02-The-Shooting-Method_8_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter23.02-The-Shooting-Method_8_0.png"/>


<p>Цього разу ми бачимо, що швидкість переоцінена. Отже, це випадкове припущення не дозволяє легко знайти найкращий результат. Як ми вже згадували вище, якщо ми розглядатимемо цю процедуру як пошук коренів, то матимемо хороший спосіб знайти найкращий результат. Використаємо функцію <em>fsolve</em> з Python, щоб знайти корінь. З наступного прикладу видно, що ми знаходимо правильну відповідь безпосередньо.</p>


<pre><span></span><span>from</span> <span>scipy.optimize</span> <span>import</span> <span>fsolve</span>

<span>def</span> <span>objective</span><span>(</span><span>v0</span><span>):</span>
    <span>sol</span> <span>=</span> <span>solve_ivp</span><span>(</span><span>F</span><span>,</span> <span>[</span><span>0</span><span>,</span> <span>5</span><span>],</span> \
            <span>[</span><span>y0</span><span>,</span> <span>v0</span><span>],</span> <span>t_eval</span> <span>=</span> <span>t_eval</span><span>)</span>
    <span>y</span> <span>=</span> <span>sol</span><span>.</span><span>y</span><span>[</span><span>0</span><span>]</span>
    <span>return</span> <span>y</span><span>[</span><span>-</span><span>1</span><span>]</span> <span>-</span> <span>50</span>

<span>v0</span><span>,</span> <span>=</span> <span>fsolve</span><span>(</span><span>objective</span><span>,</span> <span>10</span><span>)</span>
<span>print</span><span>(</span><span>v0</span><span>)</span>
</pre>



<pre><span></span>34.499999999999986
</pre>





<pre><span></span><span>sol</span> <span>=</span> <span>solve_ivp</span><span>(</span><span>F</span><span>,</span> <span>[</span><span>0</span><span>,</span> <span>5</span><span>],</span> \
            <span>[</span><span>y0</span><span>,</span> <span>v0</span><span>],</span> <span>t_eval</span> <span>=</span> <span>t_eval</span><span>)</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span> <span>8</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>sol</span><span>.</span><span>t</span><span>,</span> <span>sol</span><span>.</span><span>y</span><span>[</span><span>0</span><span>])</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>5</span><span>,</span> <span>50</span><span>,</span> <span>'ro'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'час (с)'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'висота (м)'</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>f</span><span>'пошук кореня v=</span><span>{</span><span>v0</span><span>}</span><span> м/с'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter23.02-The-Shooting-Method_11_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter23.02-The-Shooting-Method_11_0.png"/>


<p>**СПРОБУЙТЕ!** Змінимо початкове припущення і подивимося, чи це змінить наш результат.</p>


<pre><span></span><span>for</span> <span>v0_guess</span> <span>in</span> <span>range</span><span>(</span><span>1</span><span>,</span> <span>100</span><span>,</span> <span>10</span><span>):</span>
    <span>v0</span><span>,</span> <span>=</span> <span>fsolve</span><span>(</span><span>objective</span><span>,</span> <span>v0_guess</span><span>)</span>
    <span>print</span><span>(</span><span>'Поч. прип.: </span><span>%d</span><span>, Результат: </span><span>%.1f</span><span>'</span> \
          <span>%</span><span>(</span><span>v0_guess</span><span>,</span> <span>v0</span><span>))</span>
</pre>



<pre><span></span>Поч. прип.: 1, Результат: 34.5
Поч. прип.: 11, Результат: 34.5
Поч. прип.: 21, Результат: 34.5
Поч. прип.: 31, Результат: 34.5
Поч. прип.: 41, Результат: 34.5
Поч. прип.: 51, Результат: 34.5
Поч. прип.: 61, Результат: 34.5
Поч. прип.: 71, Результат: 34.5
Поч. прип.: 81, Результат: 34.5
Поч. прип.: 91, Результат: 34.5
</pre>



<p>Ми бачимо, що зміна початкових припущень не змінює результат тут, що означає, що стабільність (див. далі в розділі) методу є хорошою.</p>
