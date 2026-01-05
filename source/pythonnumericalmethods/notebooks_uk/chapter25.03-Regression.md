<h1>Регресія<a href="#regression" title="Постійне посилання на цей заголовок"></a></h1>
<p>Регресія — це набір алгоритмів у керованому навчанні, де вихідними даними є кількісні числа замість категоріальних даних. Ми розглядали регресію найменших квадратів у розділі 16 для простих випадків, коли ми маємо аналітичну форму для апроксимації даних. Але підхід машинного навчання є більш гнучким, оскільки ви можете апроксимувати будь-які функції даних, не знаючи при цьому базової аналітичної форми. Наприклад, для регресії можна використовувати випадковий ліс, штучні нейронні мережі, метод опорних векторів тощо. У цьому розділі ми представимо підхід штучних нейронних мереж (ШНМ), який є дуже гнучкою моделлю, що легко працює як з класифікацією, так і з регресією.</p>

<h2>Основи штучних нейронних мереж<a href="#artificial-neural-network-basics" title="Постійне посилання на цей заголовок"></a></h2>
<p>Метод <strong>штучних нейронних мереж</strong> розроблений для імітації роботи нашого мозку, тобто нейрони в нашому мозку отримують та обробляють інформацію, а потім певний процес контролює, чи буде нейрон надсилати сигнал сусіднім або специфічним нейронам. Наступний рисунок показує типову структуру багатошарової штучної нейронної мережі. Вона має 3 різні шари: вхідний шар, прихований шар та вихідний шар. У кожному шарі є нейрони, які показані на рисунку у вигляді кіл. З рисунка видно, що вхідний шар у цьому випадку має 3 нейрони, що відповідають 3 ознакам, які подаються на вхід мережі (ви, безумовно, можете мати більше ознак, а отже, більше нейронів у вхідному шарі). Середній шар — це прихований шар; ви також можете мати багато прихованих шарів, на цьому рисунку ми маємо лише 1 прихований шар для ілюстрації. Нейрони в прихованих шарах є основними обробними одиницями в мережі для обробки даних; зазвичай у кожному нейроні виконуються дві дії: (1) сумування інформації, переданої з попереднього шару, (2) передача суми інформації до функції активації, щоб вирішити, чи надсилати сигнал. Вихідний шар також має нейрони для генерації виходу; для класифікації він генерує число від 0 до 1, а для задачі регресії ми можемо генерувати будь-які числа. Ми бачимо багато стрілок між різними шарами, вони називаються зв'язками в нейронній мережі, і вони відповідають за передачу інформації від одного шару до іншого. Кожен зв'язок має пов'язану з ним вагу; це настроювані параметри, які ми можемо налаштовувати в моделі. Коли інформація надходить з вхідного шару, вона проходить через зв'язки до прихованого шару для обробки, а потім до вихідного шару для генерації результатів. Зазвичай це називається <strong>прямим поширенням</strong>.</p>

<p>Як описано вище, навчання алгоритму ШНМ полягає в пошуку способу налаштування ваг на кожному зі зв'язків. У ШНМ це робиться за допомогою функції втрат, яка обчислює помилки між оцінками моделі та справжніми цільовими значеннями. Спочатку ми виконуємо пряме поширення, щоб отримати оцінку та обчислити помилку, а потім поширюємо цю помилку назад від вихідного шару до вхідного шару. Залежно від внеску в помилки для кожного зв'язку, ми можемо оновити ваги на зв'язках, щоб переконатися, що наступного разу, коли ми будемо передавати інформацію вперед, помилка зменшиться. Це називається <strong>зворотним поширенням помилки</strong>; ми можемо передавати ту саму інформацію вперед і назад багато разів (це зазвичай називається епохами), щоб постійно зменшувати помилку, доки вона не задовольнить нашу мету. Так ми навчаємо алгоритм ШНМ. Зазвичай для оновлення ваг ми використовуємо алгоритм оптимізації, який називається <strong>градієнтним спуском</strong>.</p>
<p>Розглянемо приклад ШНМ у scikit-learn.</p>
<p><strong>Генерація даних</strong></p>
<p>По-перше, нам потрібно згенерувати іграшковий набір даних, який ми будемо використовувати для навчання моделі. Ми генеруємо періодичний набір даних, використовуючи дві синусоїди з різними періодами, а потім додаємо до нього трохи шуму. Його можна візуалізувати на наступному рисунку:</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
<span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>
<span>from</span> <span>sklearn.metrics</span> <span>import</span> <span>mean_squared_error</span>
<span>plt</span><span>.</span><span>style</span><span>.</span><span>use</span><span>(</span><span>'seaborn-poster'</span><span>)</span>
<span>%</span><span>matplotlib</span> inline
</pre>





<pre><span></span><span>np</span><span>.</span><span>random</span><span>.</span><span>seed</span><span>(</span><span>0</span><span>)</span>
<span>x</span> <span>=</span> <span>10</span> <span>*</span> <span>np</span><span>.</span><span>random</span><span>.</span><span>rand</span><span>(</span><span>100</span><span>)</span>

<span>def</span> <span>model</span><span>(</span><span>x</span><span>,</span> <span>sigma</span><span>=</span><span>0.3</span><span>):</span>
    <span>fast_oscillation</span> <span>=</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>5</span> <span>*</span> <span>x</span><span>)</span>
    <span>slow_oscillation</span> <span>=</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>0.5</span> <span>*</span> <span>x</span><span>)</span>
    <span>noise</span> <span>=</span> <span>sigma</span> <span>*</span> <span>np</span><span>.</span><span>random</span><span>.</span><span>randn</span><span>(</span><span>len</span><span>(</span><span>x</span><span>))</span>

    <span>return</span> <span>slow_oscillation</span> <span>+</span> <span>fast_oscillation</span> <span>+</span> <span>noise</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span><span>8</span><span>))</span>
<span>y</span> <span>=</span> <span>model</span><span>(</span><span>x</span><span>)</span>
<span>plt</span><span>.</span><span>errorbar</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>0.3</span><span>,</span> <span>fmt</span><span>=</span><span>'o'</span><span>)</span>
</pre>



<pre><span></span>&lt;ErrorbarContainer object of 3 artists&gt;
</pre>

<img alt="../_images/chapter25.03-Regression_5_1.png" src="../_images/chapter25.03-Regression_5_1.png"/>


<p>Потім ми можемо використовувати ШНМ для апроксимації даних; основна ідея полягає в тому, щоб використовувати кожну точку даних у <span>\(x\)</span> як вхідну ознаку для ШНМ, а виходом буде послідовність - <span>\(y\)</span>. У scikit-learn модель ШНМ для регресії називається <em>MLPRegressor</em>, що розшифровується як регресор багатошарового перцептрона. Використаємо вищезгадані зашумлені дані як вхідні для алгоритму ШНМ.</p>


<pre><span></span><span>from</span> <span>sklearn.neural_network</span> <span>import</span> <span>MLPRegressor</span>
</pre>





<pre><span></span><span>mlp</span> <span>=</span> <span>MLPRegressor</span><span>(</span><span>hidden_layer_sizes</span><span>=</span><span>(</span><span>200</span><span>,</span><span>200</span><span>,</span><span>200</span><span>),</span> \
                   <span>max_iter</span> <span>=</span> <span>2000</span><span>,</span> <span>solver</span><span>=</span><span>'lbfgs'</span><span>,</span> \
                   <span>alpha</span><span>=</span><span>0.01</span><span>,</span> <span>activation</span> <span>=</span> <span>'tanh'</span><span>,</span> \
                   <span>random_state</span> <span>=</span> <span>8</span><span>)</span>

<span>xfit</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>10</span><span>,</span> <span>1000</span><span>)</span>
<span>ytrue</span> <span>=</span> <span>model</span><span>(</span><span>xfit</span><span>,</span> <span>0</span><span>)</span>
<span>yfit</span> <span>=</span> <span>mlp</span><span>.</span><span>fit</span><span>(</span><span>x</span><span>[:,</span> <span>None</span><span>],</span> <span>y</span><span>)</span><span>.</span><span>predict</span><span>(</span><span>xfit</span><span>[:,</span> <span>None</span><span>])</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span><span>8</span><span>))</span>
<span>plt</span><span>.</span><span>errorbar</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>0.3</span><span>,</span> <span>fmt</span><span>=</span><span>'o'</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>xfit</span><span>,</span> <span>yfit</span><span>,</span> <span>'-r'</span><span>,</span> <span>label</span> <span>=</span> <span>'predicted'</span><span>,</span> \
         <span>zorder</span> <span>=</span> <span>10</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>xfit</span><span>,</span> <span>ytrue</span><span>,</span> <span>'-k'</span><span>,</span> <span>alpha</span><span>=</span><span>0.5</span><span>,</span> \
         <span>label</span> <span>=</span> <span>'true model'</span><span>,</span> <span>zorder</span> <span>=</span> <span>10</span><span>)</span>
<span>plt</span><span>.</span><span>legend</span><span>()</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="../_images/chapter25.03-Regression_8_0.png" src="../_images/chapter25.03-Regression_8_0.png"/>


<p>Ми бачимо, що апроксимація даних насправді непогана. Для вищезгаданої моделі ми використали 3 приховані шари, і в кожному шарі ми використали 200 нейронів. Ми використовуємо алгоритм оптимізації — 'lbfgs', який є оптимізатором із сімейства квазіньютонівських методів. Параметр <em>max_iter</em> визначає, що ми виконаємо щонайбільше 2000 ітерацій.</p>
