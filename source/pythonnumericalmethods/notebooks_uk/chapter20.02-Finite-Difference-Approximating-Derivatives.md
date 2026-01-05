<h1>Апроксимація похідних скінченними різницями<a href="#finite-difference-approximating-derivatives" title="Постійне посилання на цей заголовок"></a></h1>
<p>Похідна <span>\(f'(x)\)</span> функції <span>\(f(x)\)</span> у точці <span>\(x=a\)</span> визначається як:</p>

\[f'(a) = \lim\limits_{x \to a}\frac{f(x) - f(a)}{x-a}\]
<p>Похідна в <span>\(x=a\)</span> є нахилом у цій точці. В апроксимаціях цього нахилу <strong>скінченними різницями</strong>, ми можемо використовувати значення функції в околі точки <span>\(x=a\)</span> для досягнення мети. Існують різні формули скінченних різниць, що використовуються в різних застосуваннях, і три з них, де похідна обчислюється за значеннями двох точок, представлені нижче.</p>
<p><strong>Пряма різниця (forward difference)</strong> полягає в оцінці нахилу функції в <span>\(x_j\)</span>, використовуючи лінію, що з'єднує <span>\((x_j, f(x_j))\)</span> та <span>\((x_{j+1}, f(x_{j+1}))\)</span>:</p>

\[f'(x_j) = \frac{f(x_{j+1}) - f(x_j)}{x_{j+1}-x_j}\]
<p><strong>Зворотна різниця (backward difference)</strong> полягає в оцінці нахилу функції в <span>\(x_j\)</span>, використовуючи лінію, що з'єднує <span>\((x_{j-1}, f(x_{j-1}))\)</span> та <span>\((x_j, f(x_j))\)</span>:</p>

\[f'(x_j) = \frac{f(x_j) - f(x_{j-1})}{x_j - x_{j-1}}\]
<p><strong>Центральна різниця (central difference)</strong> полягає в оцінці нахилу функції в <span>\(x_j\)</span>, використовуючи лінію, що з'єднує <span>\((x_{j-1}, f(x_{j-1}))\)</span> та <span>\((x_{j+1}, f(x_{j+1}))\)</span>:</p>

\[f'(x_j) = \frac{f(x_{j+1}) - f(x_{j-1})}{x_{j+1} - x_{j-1}}\]
<p>Наступний рисунок ілюструє три різні типи формул для оцінки нахилу.</p>


<h2>Апроксимація похідних скінченними різницями за допомогою ряду Тейлора<a href="#finite-difference-approximating-derivatives-with-taylor-series" title="Постійне посилання на цей заголовок"></a></h2>
<p>Щоб вивести апроксимацію для похідної <span>\(f\)</span>, ми повертаємося до ряду Тейлора. Для довільної функції <span>\(f(x)\)</span> ряд Тейлора <span>\(f\)</span> навколо <span>\(a = x_j\)</span> є
$<span>\(
f(x) = \frac{f(x_j)(x - x_j)^0}{0!} + \frac{f^{\prime}(x_j)(x - x_j)^1}{1!} + \frac{f''(x_j)(x - x_j)^2}{2!} + \frac{f'''(x_j)(x - x_j)^3}{3!} + \cdots.
\)</span>$</p>
<p>Якщо <span>\(x\)</span> знаходиться на сітці точок з кроком <span>\(h\)</span>, ми можемо обчислити ряд Тейлора в <span>\(x = x_{j+1}\)</span>, щоб отримати</p>

\[
f(x_{j+1}) = \frac{f(x_j)(x_{j+1} - x_j)^0}{0!} + \frac{f^{\prime}(x_j)(x_{j+1}- x_j)^1}{1!} + \frac{f''(x_j)(x_{j+1} - x_j)^2}{2!} + \frac{f'''(x_j)(x_{j+1} - x_j)^3}{3!} + \cdots.
\]
<p>Підставляючи <span>\(h = x_{j+1} - x_j\)</span> і розв'язуючи для <span>\(f^{\prime}(x_j)\)</span>, отримуємо рівняння</p>

\[
f^{\prime}(x_j) = \frac{f(x_{j+1}) - f(x_j)}{h} + \left(-\frac{f''(x_j)h}{2!} -\frac{f'''(x_j)h^2}{3!} - \cdots\right).
\]
<p>Члени, що знаходяться в дужках, <span>\(-\frac{f''(x_j)h}{2!} -\frac{f'''(x_j)h^2}{3!} - \cdots\)</span>, називаються <strong>членами вищого порядку</strong> <span>\(h\)</span>. Члени вищого порядку можна переписати як</p>

\[
-\frac{f''(x_j)h}{2!} -\frac{f'''(x_j)h^2}{3!} - \cdots = h(\alpha + \epsilon(h)),
\]
<p>де <span>\(\alpha\)</span> є деякою константою, а <span>\(\epsilon(h)\)</span> є функцією від <span>\(h\)</span>, яка прямує до нуля, коли <span>\(h\)</span> прямує до 0. Ви можете перевірити це за допомогою деяких алгебраїчних перетворень. Ми використовуємо скорочення "<span>\(O(h)\)</span>" для <span>\(h(\alpha + \epsilon(h))\)</span>, і загалом ми використовуємо скорочення "<span>\(O(h^p)\)</span>" для позначення <span>\(h^p(\alpha + \epsilon(h))\)</span>.</p>
<p>Підставляючи <span>\(O(h)\)</span> у попередні рівняння, отримуємо</p>

\[
f^{\prime}(x_j) = \frac{f(x_{j+1}) - f(x_j)}{h} + O(h).
\]
<p>Це дає формулу <strong>прямої різниці</strong> для апроксимації похідних як</p>

\[
f^{\prime}(x_j) \approx \frac{f(x_{j+1}) - f(x_j)}{h},
\]
<p>і ми говоримо, що ця формула є <span>\(O(h)\)</span>.</p>
<p>Тут, <span>\(O(h)\)</span> описує <strong>точність</strong> формули прямої різниці для апроксимації похідних. Для апроксимації, яка є <span>\(O(h^p)\)</span>, ми говоримо, що <span>\(p\)</span> є <strong>порядком</strong> точності апроксимації. За невеликими винятками, точність вищого порядку краща за точність нижчого порядку. Щоб проілюструвати це, припустимо <span>\(q &lt; p\)</span>. Тоді, коли крок, <span>\(h &gt; 0\)</span>, прямує до 0, <span>\(h^p\)</span> прямує до 0 швидше, ніж <span>\(h^q\)</span>. Отже, коли <span>\(h\)</span> прямує до 0, апроксимація значення, яка є <span>\(O(h^p)\)</span>, наближається до істинного значення швидше, ніж та, що є <span>\(O(h^q)\)</span>.</p>
<p>Обчисливши ряд Тейлора навколо <span>\(a = x_j\)</span> в <span>\(x = x_{j-1}\)</span> і знову розв'язавши для <span>\(f^{\prime}(x_j)\)</span>, ми отримуємо формулу <strong>зворотної різниці</strong></p>

\[
f^{\prime}(x_j) \approx \frac{f(x_j) - f(x_{j-1})}{h},
\]
<p>, яка також є <span>\(O(h)\)</span>. Ви повинні спробувати перевірити цей результат самостійно.</p>
<p>Інтуїтивно, формули прямої та зворотної різниці для похідної в <span>\(x_j\)</span> є просто нахилами між точкою в <span>\(x_j\)</span> та точками <span>\(x_{j+1}\)</span> та <span>\(x_{j-1}\)</span>, відповідно.</p>
<p>Ми можемо побудувати покращену апроксимацію похідної шляхом розумної маніпуляції членами ряду Тейлора, взятими в різних точках. Для ілюстрації, ми можемо обчислити ряд Тейлора навколо <span>\(a = x_j\)</span> як в <span>\(x_{j+1}\)</span>, так і в <span>\(x_{j-1}\)</span>. Записані, ці рівняння виглядають так:</p>

\[
f(x_{j+1}) = f(x_j) + f^{\prime}(x_j)h + \frac{1}{2}f''(x_j)h^2 + \frac{1}{6}f'''(x_j)h^3 + \cdots
\]
<p>та</p>

\[
f(x_{j-1}) = f(x_j) - f^{\prime}(x_j)h + \frac{1}{2}f''(x_j)h^2 - \frac{1}{6}f'''(x_j)h^3 + \cdots.
\]
<p>Віднімаючи вищезазначені формули, отримуємо</p>

\[
f(x_{j+1}) - f(x_{j-1}) = 2f^{\prime}(x_j) + \frac{2}{3}f'''(x_j)h^3 + \cdots,
\]
<p>, що при розв'язанні для <span>\(f^{\prime}(x_j)\)</span> дає формулу <strong>центральної різниці</strong></p>

\[
f^{\prime}(x_j) \approx \frac{f(x_{j+1}) - f(x_{j-1})}{2h}.
\]
<p>Через те, як ми відняли два рівняння, члени з <span>\(h\)</span> скоротилися; отже, формула центральної різниці є <span>\(O(h^2)\)</span>, хоча вона вимагає такої ж кількості обчислювальних зусиль, як і формули прямої та зворотної різниці! Таким чином, формула центральної різниці отримує додатковий порядок точності безкоштовно. Загалом, формули, які використовують симетричні точки навколо <span>\(x_j\)</span>, наприклад, <span>\(x_{j-1}\)</span> та <span>\(x_{j+1}\)</span>, мають кращу точність, ніж асиметричні, такі як формули прямої та зворотної різниці.</p>
<p>Наступний рисунок показує апроксимацію похідної функції <span>\(f\)</span> за допомогою прямої різниці (лінія, що з'єднує <span>\((x_j, y_j)\)</span> та <span>\((x_{j+1}, y_{j+1})\)</span>), зворотної різниці (лінія, що з'єднує <span>\((x_j, y_j)\)</span> та <span>\((x_{j-1}, y_{j-1})\)</span>), та центральної різниці (лінія, що з'єднує <span>\((x_{j-1}, y_{j-1})\)</span> та <span>\((x_{j+1}, y_{j+1})\)</span>). Як видно, різниця в значенні нахилу може суттєво відрізнятися залежно від розміру кроку <span>\(h\)</span> та характеру функції.</p>

<p><strong>СПРОБУЙТЕ!</strong> Візьміть ряд Тейлора для <span>\(f\)</span> навколо <span>\(a = x_j\)</span> і обчисліть ряд в <span>\(x = x_{j-2}, x_{j-1}, x_{j+1}, x_{j+2}\)</span>. Покажіть, що отримані рівняння можна скомбінувати, щоб утворити апроксимацію для <span>\(f^{\prime}(x_j)\)</span>, яка є <span>\(O(h^4)\)</span>.</p>
<p>Спочатку обчисліть ряд Тейлора в зазначених точках.</p>

\[\begin{split}
\begin{eqnarray*}
f(x_{j-2}) &amp;=&amp; f(x_j) - 2hf^{\prime}(x_j) + \frac{4h^2f''(x_j)}{2} - \frac{8h^3f'''(x_j)}{6} + \frac{16h^4f''''(x_j)}{24} - \frac{32h^5f'''''(x_j)}{120} + \cdots\\
f(x_{j-1}) &amp;=&amp; f(x_j) - hf^{\prime}(x_j) + \frac{h^2f''(x_j)}{2} - \frac{h^3f'''(x_j)}{6} + \frac{h^4f''''(x_j)}{24} - \frac{h^5f'''''(x_j)}{120} + \cdots\\
f(x_{j+1}) &amp;=&amp; f(x_j) + hf^{\prime}(x_j) + \frac{h^2f''(x_j)}{2} + \frac{h^3f'''(x_j)}{6} + \frac{h^4f''''(x_j)}{24} + \frac{h^5f'''''(x_j)}{120} + \cdots\\
f(x_{j+2}) &amp;=&amp; f(x_j) + 2hf^{\prime}(x_j) + \frac{4h^2f''(x_j)}{2} + \frac{8h^3f'''(x_j)}{6} + \frac{16h^4f''''(x_j)}{24} + \frac{32h^5f'''''(x_j)}{120} + \cdots
\end{eqnarray*}
\end{split}\]
<p>Щоб члени з <span>\(h^2, h^3\)</span>, та <span>\(h^4\)</span> скоротилися, ми можемо обчислити</p>

\[f(x_{j-2}) - 8f(x_{j-1}) + 8f(x_{j-1}) - f(x_{j+2}) = 12hf^{\prime}(x_j) - \frac{48h^5f'''''(x_j)}{120}\]
<p>, що можна перегрупувати в</p>

\[f^{\prime}(x_j) = \frac{f(x_{j-2}) - 8f(x_{j-1}) + 8f(x_{j-1}) - f(x_{j+2})}{12h} + O(h^4).\]
<p>Ця формула є кращою апроксимацією для похідної в <span>\(x_j\)</span>, ніж формула центральної різниці, але вимагає вдвічі більше обчислень.</p>
<p><strong>ПОРАДА!</strong> Python має команду, яку можна використовувати для безпосереднього обчислення скінченних різниць: для вектора <span>\(f\)</span>, команда <span>\(d=np.diff(f)\)</span> створює масив <span>\(d\)</span>, в якому елементи є різницями сусідніх елементів у початковому масиві <span>\(f\)</span>. Іншими словами <span>\(d(i) = f(i+1) - f(i)\)</span>.</p>
<p><strong>УВАГА!</strong> При використанні команди <em>np.diff</em>, розмір вихідних даних на одиницю менший за розмір вхідних даних, оскільки для обчислення різниці потрібні два аргументи.</p>
<p><strong>ПРИКЛАД:</strong> Розглянемо функцію <span>\(f(x) = \cos(x)\)</span>. Ми знаємо, що похідна від <span>\(\cos(x)\)</span> є <span>\(-\sin(x)\)</span>. Хоча на практиці ми можемо не знати базової функції, для якої ми знаходимо похідну, ми використовуємо простий приклад, щоб проілюструвати вищезгадані методи чисельного диференціювання та їх точність. Наступний код обчислює похідні чисельно.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
<span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>
<span>plt</span><span>.</span><span>style</span><span>.</span><span>use</span><span>(</span><span>'seaborn-poster'</span><span>)</span>
<span>%</span><span>matplotlib</span> inline
</pre>





<pre><span></span><span># step size</span>
<span>h</span> <span>=</span> <span>0.1</span>
<span># define grid</span>
<span>x</span> <span>=</span> <span>np</span><span>.</span><span>arange</span><span>(</span><span>0</span><span>,</span> <span>2</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>,</span> <span>h</span><span>)</span> 
<span># compute function</span>
<span>y</span> <span>=</span> <span>np</span><span>.</span><span>cos</span><span>(</span><span>x</span><span>)</span> 

<span># compute vector of forward differences</span>
<span>forward_diff</span> <span>=</span> <span>np</span><span>.</span><span>diff</span><span>(</span><span>y</span><span>)</span><span>/</span><span>h</span> 
<span># compute corresponding grid</span>
<span>x_diff</span> <span>=</span> <span>x</span><span>[:</span><span>-</span><span>1</span><span>:]</span> 
<span># compute exact solution</span>
<span>exact_solution</span> <span>=</span> <span>-</span><span>np</span><span>.</span><span>sin</span><span>(</span><span>x_diff</span><span>)</span> 

<span># Plot solution</span>
<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>12</span><span>,</span> <span>8</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x_diff</span><span>,</span> <span>forward_diff</span><span>,</span> <span>'--'</span><span>,</span> \
         <span>label</span> <span>=</span> <span>'Finite difference approximation'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x_diff</span><span>,</span> <span>exact_solution</span><span>,</span> \
         <span>label</span> <span>=</span> <span>'Exact solution'</span><span>)</span>
<span>plt</span><span>.</span><span>legend</span><span>()</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>

<span># Compute max error between </span>
<span># numerical derivative and exact solution</span>
<span>max_error</span> <span>=</span> <span>max</span><span>(</span><span>abs</span><span>(</span><span>exact_solution</span> <span>-</span> <span>forward_diff</span><span>))</span>
<span>print</span><span>(</span><span>max_error</span><span>)</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter20.02-Finite-Difference-Approximating-Derivatives_5_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter20.02-Finite-Difference-Approximating-Derivatives_5_0.png"/>
<pre><span></span>0.049984407218554114
</pre>



<p>Як показує вищезгаданий рисунок, існує невелике зміщення між двома кривими, що є результатом чисельної похибки при обчисленні чисельних похідних. Максимальна похибка між двома чисельними результатами становить близько 0.05 і очікується, що вона зменшуватиметься зі зменшенням розміру кроку.</p>
<p>Як показано в попередньому прикладі, схема скінченних різниць містить чисельну похибку через апроксимацію похідної. Ця різниця зменшується зі зменшенням розміру кроку дискретизації, що проілюстровано в наступному прикладі.</p>
<p><strong>ПРИКЛАД:</strong> Наступний код обчислює чисельну похідну <span>\(f(x) = \cos(x)\)</span>, використовуючи формулу прямої різниці для зменшення розмірів кроку, <span>\(h\)</span>. Потім він будує графік максимальної похибки між апроксимованою похідною та істинною похідною відносно <span>\(h\)</span>, як показано на згенерованому рисунку.</p>


<pre><span></span><span># define step size</span>
<span>h</span> <span>=</span> <span>1</span>
<span># define number of iterations to perform</span>
<span>iterations</span> <span>=</span> <span>20</span> 
<span># list to store our step sizes</span>
<span>step_size</span> <span>=</span> <span>[]</span> 
<span># list to store max error for each step size</span>
<span>max_error</span> <span>=</span> <span>[]</span> 

<span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>iterations</span><span>):</span>
    <span># halve the step size</span>
    <span>h</span> <span>/=</span> <span>2</span> 
    <span># store this step size</span>
    <span>step_size</span><span>.</span><span>append</span><span>(</span><span>h</span><span>)</span> 
    <span># compute new grid</span>
    <span>x</span> <span>=</span> <span>np</span><span>.</span><span>arange</span><span>(</span><span>0</span><span>,</span> <span>2</span> <span>*</span> <span>np</span><span>.</span><span>pi</span><span>,</span> <span>h</span><span>)</span> 
    <span># compute function value at grid</span>
    <span>y</span> <span>=</span> <span>np</span><span>.</span><span>cos</span><span>(</span><span>x</span><span>)</span> 
    <span># compute vector of forward differences</span>
    <span>forward_diff</span> <span>=</span> <span>np</span><span>.</span><span>diff</span><span>(</span><span>y</span><span>)</span><span>/</span><span>h</span> 
    <span># compute corresponding grid</span>
    <span>x_diff</span> <span>=</span> <span>x</span><span>[:</span><span>-</span><span>1</span><span>]</span> 
    <span># compute exact solution</span>
    <span>exact_solution</span> <span>=</span> <span>-</span><span>np</span><span>.</span><span>sin</span><span>(</span><span>x_diff</span><span>)</span> 
    
    <span># Compute max error between </span>
    <span># numerical derivative and exact solution</span>
    <span>max_error</span><span>.</span><span>append</span><span>(</span>\
            <span>max</span><span>(</span><span>abs</span><span>(</span><span>exact_solution</span> <span>-</span> <span>forward_diff</span><span>)))</span>

<span># produce log-log plot of max error versus step size</span>
<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>12</span><span>,</span> <span>8</span><span>))</span>
<span>plt</span><span>.</span><span>loglog</span><span>(</span><span>step_size</span><span>,</span> <span>max_error</span><span>,</span> <span>'v'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter20.02-Finite-Difference-Approximating-Derivatives_7_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter20.02-Finite-Difference-Approximating-Derivatives_7_0.png"/>


<p>Нахил лінії в логарифмічному масштабі дорівнює 1; отже, похибка пропорційна <span>\(h^1\)</span>, що означає, що, як і очікувалося, формула прямої різниці є <span>\(O(h)\)</span>.</p>
