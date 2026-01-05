<h1>Регресія методом найменших квадратів для нелінійних функцій<a href="#least-square-regression-for-nonlinear-functions" title="Permalink to this headline"></a></h1>
<p>Регресія методом найменших квадратів вимагає, щоб функція оцінки була лінійною комбінацією базисних функцій. Існують деякі функції, які неможливо представити в такій формі, але для яких регресія методом найменших квадратів все ще є доцільною.</p>
<p>Нижче наведено кілька способів роботи з нелінійними функціями.</p>
<ul>
<li><p>Ми можемо досягти цього, скориставшись властивостями логарифмів і перетворивши нелінійну функцію на лінійну</p></li>
<li><p>Ми можемо використовувати функцію <code><span>curve_fit</span></code> з бібліотеки <code><span>scipy</span></code> для прямої оцінки параметрів нелінійної функції за допомогою методу найменших квадратів.</p></li>
</ul>

<h2>Логарифмічні трюки для експоненціальних функцій<a href="#log-tricks-for-exponential-functions" title="Permalink to this headline"></a></h2>
<p>Припустимо, у вас є функція у формі <span>\(\hat{y}(x) = {\alpha} e^{{\beta} x}\)</span> та дані для <span>\(x\)</span> і <span>\(y\)</span>, і ви хочете виконати регресію методом найменших квадратів, щоб знайти <span>\({\alpha}\)</span> та <span>\({\beta}\)</span>. Очевидно, що попередній набір базисних функцій (лінійних) був би недоречним для опису <span>\(\hat{y}(x)\)</span>; однак, якщо ми візьмемо <span>\(\log\)</span> від обох частин, ми отримаємо <span>\(\log(\hat{y}(x)) = \log({\alpha}) + {\beta} x\)</span>. Тепер, нехай <span>\(\tilde{y}(x) = \log(\hat{y}(x))\)</span> та <span>\(\tilde{{\alpha}} = \log({\alpha})\)</span>, тоді <span>\(\tilde{y}(x) = \tilde{{\alpha}} + {\beta} x\)</span>. Тепер ми можемо виконати регресію методом найменших квадратів для лінеаризованого виразу, щоб знайти <span>\(\tilde{y}(x), \tilde{{\alpha}}\)</span> та <span>\({\beta}\)</span>, а потім відновити <span>\({\alpha}\)</span>, використовуючи вираз <span>\({\alpha} = e^{\tilde{{\alpha}}}\)</span>.</p>
<p>Для прикладу нижче ми згенеруємо дані, використовуючи <span>\(\alpha = 0.1\)</span> та <span>\(\beta = 0.3\)</span>.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
<span>from</span> <span>scipy</span> <span>import</span> <span>optimize</span>
<span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>

<span>plt</span><span>.</span><span>style</span><span>.</span><span>use</span><span>(</span><span>'seaborn-poster'</span><span>)</span>
</pre>





<pre><span></span><span># згенеруємо x та y, і додамо трохи шуму до y</span>
<span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>10</span><span>,</span> <span>101</span><span>)</span>
<span>y</span> <span>=</span> <span>0.1</span><span>*</span><span>np</span><span>.</span><span>exp</span><span>(</span><span>0.3</span><span>*</span><span>x</span><span>)</span> <span>+</span> <span>0.1</span><span>*</span><span>np</span><span>.</span><span>random</span><span>.</span><span>random</span><span>(</span><span>len</span><span>(</span><span>x</span><span>))</span>
</pre>





<pre><span></span><span># Погляньмо на дані</span>
<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span><span>8</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>'b.'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'x'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'y'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter16.05-Least-Square-Regression-for-Nonlinear-Functions_6_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter16.05-Least-Square-Regression-for-Nonlinear-Functions_6_0.png"/>


<p>Підберемо параметри для даних після застосування логарифмічного трюку.</p>


<pre><span></span><span>A</span> <span>=</span> <span>np</span><span>.</span><span>vstack</span><span>([</span><span>x</span><span>,</span> <span>np</span><span>.</span><span>ones</span><span>(</span><span>len</span><span>(</span><span>x</span><span>))])</span><span>.</span><span>T</span>
<span>beta</span><span>,</span> <span>log_alpha</span> <span>=</span> <span>np</span><span>.</span><span>linalg</span><span>.</span><span>lstsq</span><span>(</span><span>A</span><span>,</span> <span>np</span><span>.</span><span>log</span><span>(</span><span>y</span><span>),</span> <span>rcond</span> <span>=</span> <span>None</span><span>)[</span><span>0</span><span>]</span>
<span>alpha</span> <span>=</span> <span>np</span><span>.</span><span>exp</span><span>(</span><span>log_alpha</span><span>)</span>
<span>print</span><span>(</span><span>f</span><span>'alpha=</span><span>{</span><span>alpha</span><span>}</span><span>, beta=</span><span>{</span><span>beta</span><span>}</span><span>'</span><span>)</span>
</pre>



<pre><span></span>alpha=0.13233125271210974, beta=0.27092999595397904
</pre>





<pre><span></span><span># Погляньмо на дані</span>
<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span><span>8</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>'b.'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>alpha</span><span>*</span><span>np</span><span>.</span><span>exp</span><span>(</span><span>beta</span><span>*</span><span>x</span><span>),</span> <span>'r'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'x'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'y'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter16.05-Least-Square-Regression-for-Nonlinear-Functions_9_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter16.05-Least-Square-Regression-for-Nonlinear-Functions_9_0.png"/>




<h2>Логарифмічні трюки для степеневих функцій<a href="#log-tricks-for-power-functions" title="Permalink to this headline"></a></h2>
<p>Випадок зі степеневою функцією дуже схожий. Припустимо, у нас є функція у формі <span>\(\hat{y}(x) = bx^m\)</span> та дані для <span>\(x\)</span> і <span>\(y\)</span>. Тоді ми можемо перетворити цю функцію на лінійну, взявши <span>\(\log\)</span> від обох частин: <span>\(\log(\hat{y}(x)) = m\log(x) + \log{b}\)</span>. Отже, ми можемо розв'язати цю задачу як лінійну регресію. Оскільки це дуже схоже на попередній приклад, ми не будемо витрачати на це більше часу.</p>


<h2>Поліноміальна регресія<a href="#polynomial-regression" title="Permalink to this headline"></a></h2>
<p>Ми також можемо використовувати поліноми та метод найменших квадратів для апроксимації нелінійної функції. Раніше всі наші функції були в лінійній формі, тобто <span>\(y = ax + b\)</span>. Але <strong>поліноми</strong> — це функції наступного вигляду:</p>

\[f(x) = a_nx^n + a_{n-1}x^{n-1} + \cdots + a_2x^2 + a_1x^1 + a_0\]
<p>де <span>\(a_n, a_{n-1}, \cdots, a_2, a_1, a_0\)</span> — це коефіцієнти, що є дійсними числами, а <span>\(n\)</span>, невід'ємне ціле число, — це <strong>порядок</strong> або <strong>степінь</strong> полінома. Якщо у нас є набір точок даних, ми можемо використовувати поліноми різного порядку для їх апроксимації. Коефіцієнти поліномів можна оцінити за допомогою методу найменших квадратів, як і раніше, тобто мінімізуючи помилку між реальними даними та результатами поліноміальної апроксимації.</p>
<p>У Python ми можемо використовувати <code><span>numpy.polyfit</span></code> для отримання коефіцієнтів поліномів різного порядку за допомогою методу найменших квадратів. Маючи коефіцієнти, ми можемо використовувати <code><span>numpy.polyval</span></code> для отримання конкретних значень для заданих коефіцієнтів. Розглянемо приклад, як це зробити в Python.</p>


<pre><span></span><span>x_d</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([</span><span>0</span><span>,</span> <span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>,</span> <span>4</span><span>,</span> <span>5</span><span>,</span> <span>6</span><span>,</span> <span>7</span><span>,</span> <span>8</span><span>])</span>
<span>y_d</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([</span><span>0</span><span>,</span> <span>0.8</span><span>,</span> <span>0.9</span><span>,</span> <span>0.1</span><span>,</span> <span>-</span><span>0.6</span><span>,</span> <span>-</span><span>0.8</span><span>,</span> <span>-</span><span>1</span><span>,</span> <span>-</span><span>0.9</span><span>,</span> <span>-</span><span>0.4</span><span>])</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>12</span><span>,</span> <span>8</span><span>))</span>
<span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>1</span><span>,</span> <span>7</span><span>):</span>
    
    <span># отримуємо коефіцієнти полінома</span>
    <span>y_est</span> <span>=</span> <span>np</span><span>.</span><span>polyfit</span><span>(</span><span>x_d</span><span>,</span> <span>y_d</span><span>,</span> <span>i</span><span>)</span>
    <span>plt</span><span>.</span><span>subplot</span><span>(</span><span>2</span><span>,</span><span>3</span><span>,</span><span>i</span><span>)</span>
    <span>plt</span><span>.</span><span>plot</span><span>(</span><span>x_d</span><span>,</span> <span>y_d</span><span>,</span> <span>'o'</span><span>)</span>
    <span># обчислюємо значення для полінома</span>
    <span>plt</span><span>.</span><span>plot</span><span>(</span><span>x_d</span><span>,</span> <span>np</span><span>.</span><span>polyval</span><span>(</span><span>y_est</span><span>,</span> <span>x_d</span><span>))</span>
    <span>plt</span><span>.</span><span>title</span><span>(</span><span>f</span><span>'Поліном порядку </span><span>{</span><span>i</span><span>}</span><span>'</span><span>)</span>

<span>plt</span><span>.</span><span>tight_layout</span><span>()</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter16.05-Least-Square-Regression-for-Nonlinear-Functions_11_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter16.05-Least-Square-Regression-for-Nonlinear-Functions_11_0.png"/>


<p>Наведений вище рисунок показує, що ми можемо використовувати поліноми різного порядку для апроксимації одних і тих самих даних. Чим вищий порядок, тим гнучкішою буде крива, яку ми використовуємо для апроксимації даних. Але питання про те, який порядок використовувати, не є простим; це залежить від конкретних задач у науці та інженерії.</p>


<h2>Використання optimize.curve_fit з scipy<a href="#use-optimize-curve-fit-from-scipy" title="Permalink to this headline"></a></h2>
<p>Ми можемо використовувати функцію <code><span>curve_fit</span></code> для апроксимації функції будь-якої форми та оцінки її параметрів. Ось як ми розв'язуємо вищезгадану задачу з розділу про логарифмічні трюки за допомогою функції <code><span>curve_fit</span></code>.</p>


<pre><span></span><span># визначимо форму функції</span>
<span>def</span> <span>func</span><span>(</span><span>x</span><span>,</span> <span>a</span><span>,</span> <span>b</span><span>):</span>
    <span>y</span> <span>=</span> <span>a</span><span>*</span><span>np</span><span>.</span><span>exp</span><span>(</span><span>b</span><span>*</span><span>x</span><span>)</span>
    <span>return</span> <span>y</span>

<span>alpha</span><span>,</span> <span>beta</span> <span>=</span> <span>optimize</span><span>.</span><span>curve_fit</span><span>(</span><span>func</span><span>,</span> <span>xdata</span> <span>=</span> <span>x</span><span>,</span> <span>ydata</span> <span>=</span> <span>y</span><span>)[</span><span>0</span><span>]</span>
<span>print</span><span>(</span><span>f</span><span>'alpha=</span><span>{</span><span>alpha</span><span>}</span><span>, beta=</span><span>{</span><span>beta</span><span>}</span><span>'</span><span>)</span>
</pre>



<pre><span></span>alpha=0.12420824748558632, beta=0.28005793982974525
</pre>





<pre><span></span><span># Погляньмо на дані</span>
<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span><span>8</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>'b.'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>alpha</span><span>*</span><span>np</span><span>.</span><span>exp</span><span>(</span><span>beta</span><span>*</span><span>x</span><span>),</span> <span>'r'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'x'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'y'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter16.05-Least-Square-Regression-for-Nonlinear-Functions_15_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter16.05-Least-Square-Regression-for-Nonlinear-Functions_15_0.png"/>
