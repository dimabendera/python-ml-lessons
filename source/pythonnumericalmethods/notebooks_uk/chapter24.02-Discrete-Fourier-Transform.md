<h1>Дискретне перетворення Фур'є (ДПФ)<a href="#discrete-fourier-transform-dft" title="Постійне посилання на цей заголовок"></a></h1>
<p>З попереднього розділу ми дізналися, як легко можна охарактеризувати хвилю за періодом/частотою, амплітудою, фазою. Але це легко для простих періодичних сигналів, таких як синусоїдальні або косинусоїдальні хвилі. Для складних хвиль охарактеризувати їх так непросто. Наприклад, нижче наведено відносно складніші хвилі, і важко сказати, яка частота, амплітуда хвилі, чи не так?</p>

<p>У реальному світі існують складніші випадки, і було б чудово мати метод, який ми могли б використовувати для аналізу характеристик хвилі. <strong>Перетворення Фур'є</strong> можна використовувати для цієї мети, оскільки воно розкладає будь-який сигнал на суму простих синусоїдальних і косинусоїдальних хвиль, для яких ми можемо легко виміряти частоту, амплітуду та фазу. Перетворення Фур'є може бути застосоване до неперервних або дискретних хвиль, у цьому розділі ми будемо говорити лише про Дискретне перетворення Фур'є (ДПФ).</p>
<p>Використовуючи ДПФ, ми можемо розкласти вищезгаданий сигнал на ряд синусоїд, і кожна з них матиме різну частоту. Наступний 3D-малюнок показує ідею, що стоїть за ДПФ: вищезгаданий сигнал насправді є результатом суми 3 різних синусоїдальних хвиль. Сигнал у часовій області, який є вищезгаданим сигналом, що ми бачили, може бути перетворений у фігуру в частотній області, яка називається амплітудним спектром ДПФ, де частоти сигналу відображаються як вертикальні смуги. Висота смуги після нормалізації є амплітудою сигналу в часовій області. Ви можете бачити, що 3 вертикальні смуги відповідають 3 частотам синусоїдальної хвилі, які також зображені на малюнку.</p>

<p>У цьому розділі ми дізнаємося, як використовувати ДПФ для обчислення та побудови амплітудного спектра ДПФ.</p>

<h2>ДПФ<a href="#dft" title="Постійне посилання на цей заголовок"></a></h2>
<p>ДПФ може перетворити послідовність рівномірно розташованих сигналів на інформацію про частоту всіх синусоїдальних хвиль, які необхідно підсумувати для отримання сигналу в часовій області. Воно визначається як:</p>

\[ X_k = \sum_{n=0}^{N-1}{x_n\cdot e^{-i2\pi{kn/N}}} = \sum_{n=0}^{N-1}{x_n[cos(2\pi{kn/N}) -i\cdot sin(2\pi{kn/N})]}\]
<p>де</p>
<ul>
<li><p>N = кількість відліків</p></li>
<li><p>n = поточний відлік</p></li>
<li><p>k = поточна частота, де <span>\( k\in [0,N-1]\)</span></p></li>
<li><p><span>\(x_n\)</span> = значення синуса при відліку n</p></li>
<li><p><span>\(X_k\)</span> = ДПФ, яке містить інформацію як про амплітуду, так і про фазу</p></li>
</ul>
<p>Крім того, останній вираз у наведеному вище рівнянні виведено з <em>формули Ейлера</em>, яка пов'язує тригонометричні функції з комплексною експоненційною функцією: <span>\(e^{i\cdot x} = cosx+i\cdot sinx\)</span></p>
<p>Через природу перетворення, <span>\(X_0 = \sum_{n=0}^{N-1}x_n\)</span>. Якщо <span>\(N\)</span> є непарним числом, елементи <span>\(X_1, X_2, ..., X_{(N-1)/2}\)</span> містять члени позитивної частоти, а елементи <span>\(X_{(N+1)/2}, ..., X_{N-1}\)</span> містять члени негативної частоти, в порядку спадання негативної частоти. Якщо ж <span>\(N\)</span> є парним, елементи <span>\(X_1, X_2, ..., X_{N/2-1}\)</span> містять члени позитивної частоти, а елементи <span>\(X_{N/2},...,X_{N-1}\)</span> містять члени негативної частоти, в порядку спадання негативної частоти. У випадку, коли наш вхідний сигнал <span>\(x\)</span> є послідовністю дійсних значень, вихід ДПФ <span>\(X_n\)</span> для позитивних частот є спряженим до значень <span>\(X_n\)</span> для негативних частот, спектр буде симетричним. Тому зазвичай ми будуємо лише ДПФ, що відповідає позитивним частотам.</p>
<p>Зауважте, що <span>\(X_k\)</span> є комплексним числом, яке кодує інформацію як про амплітуду, так і про фазу комплексної синусоїдальної компоненти <span>\(e^{i\cdot 2\pi kn/N}\)</span> функції <span>\(x_n\)</span>. Амплітуда та фаза сигналу можуть бути розраховані як:</p>

\[amp = \frac{|X_k|}{N}= \frac{\sqrt{Re(X_k)^2 + Im(X_k)^2}}{N}\]

\[phase = atan2(Im(X_k), Re(X_k))\]
<p>де <span>\(Im(X_k)\)</span> та <span>\(Re(X_k)\)</span> є уявною та дійсною частинами комплексного числа, <span>\(atan2\)</span> є двоаргументною формою функції <span>\(arctan\)</span>.</p>
<p>Амплітуди, повернені ДПФ, дорівнюють амплітудам сигналів, поданих на ДПФ, якщо ми нормалізуємо їх за кількістю точок вибірки. Зауважте, що це розділить потужність між позитивною та негативною сторонами; якщо вхідний сигнал є послідовністю дійсних значень, як ми описали вище, спектр позитивних та негативних частот буде симетричним, тому ми будемо розглядати лише одну сторону результату ДПФ, і замість ділення на <span>\(N\)</span>, ми ділимо на <span>\(N/2\)</span>, щоб отримати амплітуду, що відповідає сигналу в часовій області.</p>
<p>Тепер, коли ми маємо базові знання про ДПФ, давайте подивимося, як ми можемо його використовувати.</p>
<p><strong>СПРОБУЙТЕ!</strong> Згенеруйте 3 синусоїдальні хвилі з частотами 1 Гц, 4 Гц і 7 Гц, амплітудами 3, 1 і 0.5, і фазою, що дорівнює нулю. Додайте ці 3 синусоїдальні хвилі разом з частотою дискретизації 100 Гц, і ви побачите, що це той самий сигнал, який ми щойно показали на початку розділу.</p>


<pre><span></span><span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>
<span>import</span> <span>numpy</span> <span>as</span> <span>np</span>

<span>plt</span><span>.</span><span>style</span><span>.</span><span>use</span><span>(</span><span>'seaborn-poster'</span><span>)</span>
<span>%</span><span>matplotlib</span> inline
</pre>





<pre><span></span><span># частота дискретизації</span>
<span>sr</span> <span>=</span> <span>100</span>
<span># інтервал дискретизації</span>
<span>ts</span> <span>=</span> <span>1.0</span><span>/</span><span>sr</span>
<span>t</span> <span>=</span> <span>np</span><span>.</span><span>arange</span><span>(</span><span>0</span><span>,</span><span>1</span><span>,</span><span>ts</span><span>)</span>

<span>freq</span> <span>=</span> <span>1.</span>
<span>x</span> <span>=</span> <span>3</span><span>*</span><span>np</span><span>.</span><span>sin</span><span>(</span><span>2</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>*</span><span>freq</span><span>*</span><span>t</span><span>)</span>

<span>freq</span> <span>=</span> <span>4</span>
<span>x</span> <span>+=</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>2</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>*</span><span>freq</span><span>*</span><span>t</span><span>)</span>

<span>freq</span> <span>=</span> <span>7</span>   
<span>x</span> <span>+=</span> <span>0.5</span><span>*</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>2</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>*</span><span>freq</span><span>*</span><span>t</span><span>)</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>8</span><span>,</span> <span>6</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>t</span><span>,</span> <span>x</span><span>,</span> <span>'r'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Амплітуда'</span><span>)</span>

<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.02-Discrete-Fourier-Transform_5_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.02-Discrete-Fourier-Transform_5_0.png"/>


<p><strong>СПРОБУЙТЕ!</strong> Напишіть функцію <em>DFT(x)</em>, яка приймає один аргумент, <em>x</em> - вхідний 1-вимірний сигнал з дійсними значеннями. Функція обчислить ДПФ сигналу та поверне значення ДПФ. Застосуйте цю функцію до сигналу, який ми згенерували вище, та побудуйте результат.</p>


<pre><span></span><span>def</span> <span>DFT</span><span>(</span><span>x</span><span>):</span>
    <span>"""</span>
<span>    Функція для обчислення </span>
<span>    дискретного перетворення Фур'є </span>
<span>    1D сигналу з дійсними значеннями x</span>
<span>    """</span>

    <span>N</span> <span>=</span> <span>len</span><span>(</span><span>x</span><span>)</span>
    <span>n</span> <span>=</span> <span>np</span><span>.</span><span>arange</span><span>(</span><span>N</span><span>)</span>
    <span>k</span> <span>=</span> <span>n</span><span>.</span><span>reshape</span><span>((</span><span>N</span><span>,</span> <span>1</span><span>))</span>
    <span>e</span> <span>=</span> <span>np</span><span>.</span><span>exp</span><span>(</span><span>-</span><span>2</span><span>j</span> <span>*</span> <span>np</span><span>.</span><span>pi</span> <span>*</span> <span>k</span> <span>*</span> <span>n</span> <span>/</span> <span>N</span><span>)</span>
    
    <span>X</span> <span>=</span> <span>np</span><span>.</span><span>dot</span><span>(</span><span>e</span><span>,</span> <span>x</span><span>)</span>
    
    <span>return</span> <span>X</span>
</pre>





<pre><span></span><span>X</span> <span>=</span> <span>DFT</span><span>(</span><span>x</span><span>)</span>

<span># обчислення частоти</span>
<span>N</span> <span>=</span> <span>len</span><span>(</span><span>X</span><span>)</span>
<span>n</span> <span>=</span> <span>np</span><span>.</span><span>arange</span><span>(</span><span>N</span><span>)</span>
<span>T</span> <span>=</span> <span>N</span><span>/</span><span>sr</span>
<span>freq</span> <span>=</span> <span>n</span><span>/</span><span>T</span> 

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>8</span><span>,</span> <span>6</span><span>))</span>
<span>plt</span><span>.</span><span>stem</span><span>(</span><span>freq</span><span>,</span> <span>abs</span><span>(</span><span>X</span><span>),</span> <span>'b'</span><span>,</span> \
         <span>markerfmt</span><span>=</span><span>" "</span><span>,</span> <span>basefmt</span><span>=</span><span>"-b"</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'Частота (Гц)'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Амплітуда ДПФ |X(freq)|'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.02-Discrete-Fourier-Transform_8_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.02-Discrete-Fourier-Transform_8_0.png"/>


<p>Звідси ми бачимо, що вихід ДПФ симетричний відносно половини частоти дискретизації (ви можете спробувати різні частоти дискретизації для перевірки). Ця половина частоти дискретизації називається <strong>частотою Найквіста</strong> або частотою згортання, вона названа на честь інженера-електронника Гаррі Найквіста. Він і Клод Шеннон мають теорему дискретизації Найквіста-Шеннона, яка стверджує, що сигнал, дискретизований з певною швидкістю, може бути повністю реконструйований, якщо він містить лише частотні компоненти нижче половини цієї частоти дискретизації, таким чином, найвища вихідна частота з ДПФ становить половину частоти дискретизації.</p>


<pre><span></span><span>n_oneside</span> <span>=</span> <span>N</span><span>//</span><span>2</span>
<span># отримати односторонню частоту</span>
<span>f_oneside</span> <span>=</span> <span>freq</span><span>[:</span><span>n_oneside</span><span>]</span>

<span># нормалізувати амплітуду</span>
<span>X_oneside</span> <span>=</span><span>X</span><span>[:</span><span>n_oneside</span><span>]</span><span>/</span><span>n_oneside</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>12</span><span>,</span> <span>6</span><span>))</span>
<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>121</span><span>)</span>
<span>plt</span><span>.</span><span>stem</span><span>(</span><span>f_oneside</span><span>,</span> <span>abs</span><span>(</span><span>X_oneside</span><span>),</span> <span>'b'</span><span>,</span> \
         <span>markerfmt</span><span>=</span><span>" "</span><span>,</span> <span>basefmt</span><span>=</span><span>"-b"</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'Частота (Гц)'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Амплітуда ДПФ |X(freq)|'</span><span>)</span>

<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>122</span><span>)</span>
<span>plt</span><span>.</span><span>stem</span><span>(</span><span>f_oneside</span><span>,</span> <span>abs</span><span>(</span><span>X_oneside</span><span>),</span> <span>'b'</span><span>,</span> \
         <span>markerfmt</span><span>=</span><span>" "</span><span>,</span> <span>basefmt</span><span>=</span><span>"-b"</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'Частота (Гц)'</span><span>)</span>
<span>plt</span><span>.</span><span>xlim</span><span>(</span><span>0</span><span>,</span> <span>10</span><span>)</span>
<span>plt</span><span>.</span><span>tight_layout</span><span>()</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.02-Discrete-Fourier-Transform_10_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.02-Discrete-Fourier-Transform_10_0.png"/>


<p>Ми бачимо, що, побудувавши першу половину результатів ДПФ, ми можемо побачити 3 чіткі піки на частотах 1 Гц, 4 Гц і 7 Гц, з амплітудами 3, 1, 0.5, як і очікувалося. Ось як ми можемо використовувати ДПФ для аналізу довільного сигналу, розкладаючи його на прості синусоїдальні хвилі.</p>


<h2>Обернене ДПФ<a href="#the-inverse-dft" title="Постійне посилання на цей заголовок"></a></h2>
<p>Звісно, ми можемо легко виконати обернене перетворення ДПФ.</p>

\[ x_n = \frac{1}{N}\sum_{k=0}^{N-1}{X_k\cdot e^{i\cdot 2\pi{kn/N}}}\]
<p>Ми залишимо це як вправу для вас, щоб написати функцію.</p>


<h2>Обмеження ДПФ<a href="#the-limit-of-dft" title="Постійне посилання на цей заголовок"></a></h2>
<p>Основна проблема з наведеною вище реалізацією ДПФ полягає в тому, що вона неефективна, якщо ми маємо сигнал з багатьма точками даних. Обчислення ДПФ може зайняти багато часу, якщо сигнал великий.</p>
<p><strong>СПРОБУЙТЕ</strong> Напишіть функцію для генерації простого сигналу з різною частотою дискретизації та подивіться різницю в часі обчислення, змінюючи частоту дискретизації.</p>


<pre><span></span><span>def</span> <span>gen_sig</span><span>(</span><span>sr</span><span>):</span>
    <span>'''</span>
<span>    функція для генерації</span>
<span>    простого 1D сигналу з</span>
<span>    різною частотою дискретизації</span>
<span>    '''</span>
    <span>ts</span> <span>=</span> <span>1.0</span><span>/</span><span>sr</span>
    <span>t</span> <span>=</span> <span>np</span><span>.</span><span>arange</span><span>(</span><span>0</span><span>,</span><span>1</span><span>,</span><span>ts</span><span>)</span>

    <span>freq</span> <span>=</span> <span>1.</span>
    <span>x</span> <span>=</span> <span>3</span><span>*</span><span>np</span><span>.</span><span>sin</span><span>(</span><span>2</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>*</span><span>freq</span><span>*</span><span>t</span><span>)</span>
    <span>return</span> <span>x</span>
</pre>





<pre><span></span><span># частота дискретизації = 2000</span>
<span>sr</span> <span>=</span> <span>2000</span>
<span>%</span><span>timeit</span> DFT(gen_sig(sr))
</pre>



<pre><span></span>120 ms ± 8.27 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
</pre>





<pre><span></span><span># частота дискретизації 20000</span>
<span>sr</span> <span>=</span> <span>20000</span>
<span>%</span><span>timeit</span> DFT(gen_sig(sr))
</pre>



<pre><span></span>15.9 s ± 1.51 s per loop (mean ± std. dev. of 7 runs, 1 loop each)
</pre>



<p>Ми бачимо, що зі збільшенням кількості точок даних ми можемо витрачати багато часу на обчислення за допомогою цього ДПФ. На щастя, Швидке перетворення Фур'є (ШПФ) було популяризовано Кулі та Тьюкі в їхній <a href="http://www.ams.org/journals/mcom/1965-19-090/S0025-5718-1965-0178586-1/">статті 1965 року</a>, яке ефективно вирішує цю проблему, що буде темою наступного розділу.</p>
