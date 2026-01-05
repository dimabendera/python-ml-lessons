<h1>Основи хвиль<a href="#the-basics-of-waves" title="Постійне посилання на цей заголовок"></a></h1>
<p>У нашому житті існує багато типів хвиль, наприклад, якщо кинути камінь у ставок, можна побачити, як хвилі утворюються та поширюються у воді. Звісно, є багато інших прикладів хвиль, деякі з них навіть важко побачити, такі як звукові хвилі, хвилі землетрусів, мікрохвилі (які ми використовуємо для приготування їжі на кухні). Але у фізиці хвиля — це збурення, що поширюється у просторі та матерії, передаючи енергію з одного місця в інше. Важливо вивчати хвилі в нашому житті, щоб зрозуміти, як вони утворюються, поширюються тощо. У цьому розділі ми розглянемо основний інструмент, який допомагає нам розуміти та вивчати хвилі — **перетворення Фур'є**. Але перш ніж продовжити, давайте спочатку ознайомимося з тим, як ми насправді моделюємо та вивчаємо хвилі.</p>

<h2>Моделювання хвилі за допомогою математичних інструментів<a href="#model-a-wave-using-mathematical-tools" title="Постійне посилання на цей заголовок"></a></h2>
<p>Ми можемо змоделювати одну хвилю як поле за допомогою функції <span>\(F(x, t)\)</span>, де <span>\(x\)</span> — це розташування точки в просторі, а <span>\(t\)</span> — час. Найпростіший випадок — це зміна форми синусоїдальної хвилі за <span>\(x\)</span>.</p>


<pre><span></span><span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>
<span>import</span> <span>numpy</span> <span>as</span> <span>np</span>

<span>plt</span><span>.</span><span>style</span><span>.</span><span>use</span><span>(</span><span>'seaborn-poster'</span><span>)</span>
<span>%</span><span>matplotlib</span> inline
</pre>





<pre><span></span><span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>20</span><span>,</span> <span>201</span><span>)</span>
<span>y</span> <span>=</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>x</span><span>)</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>8</span><span>,</span> <span>6</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>'b'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Amplitude'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'Location (x)'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="../_images/chapter24.01-The-Basics-of-waves_5_0.png" src="../_images/chapter24.01-The-Basics-of-waves_5_0.png"/>


<p>Ми можемо уявити, що синусоїдальна хвиля може змінюватися як у часі, так і в просторі. Якщо ми побудуємо графік змін у різних місцях, кожен часовий знімок буде синусоїдальною хвилею, що змінюється залежно від розташування. Дивіться наступний малюнок із фіксованою точкою в <span>\(x=2.5\)</span>, показаною червоною крапкою. Звісно, ви також можете побачити зміни в часі в певному місці, ви можете побудувати цей графік самостійно.</p>


<pre><span></span><span>fig</span> <span>=</span> <span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>8</span><span>,</span><span>8</span><span>))</span>

<span>times</span> <span>=</span> <span>np</span><span>.</span><span>arange</span><span>(</span><span>5</span><span>)</span>

<span>n</span> <span>=</span> <span>len</span><span>(</span><span>times</span><span>)</span>

<span>for</span> <span>t</span> <span>in</span> <span>times</span><span>:</span>
    <span>plt</span><span>.</span><span>subplot</span><span>(</span><span>n</span><span>,</span> <span>1</span><span>,</span> <span>t</span><span>+</span><span>1</span><span>)</span>
    <span>y</span> <span>=</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>x</span> <span>+</span> <span>t</span><span>)</span>
    <span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y</span> <span>,</span> <span>'b'</span><span>)</span>
    <span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>[</span><span>25</span><span>],</span> <span>y</span> <span>[</span><span>25</span><span>],</span> <span>'ro'</span><span>)</span>
    <span>plt</span><span>.</span><span>ylim</span><span>(</span><span>-</span><span>1.1</span><span>,</span> <span>1.1</span><span>)</span>
    <span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'y'</span><span>)</span>
    <span>plt</span><span>.</span><span>title</span><span>(</span><span>f</span><span>'t = </span><span>{</span><span>t</span><span>}</span><span>'</span><span>)</span>

<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'location (x)'</span><span>)</span>
<span>plt</span><span>.</span><span>tight_layout</span><span>()</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="../_images/chapter24.01-The-Basics-of-waves_7_0.png" src="../_images/chapter24.01-The-Basics-of-waves_7_0.png"/>




<h2>Характеристики хвилі<a href="#characteristics-of-a-wave" title="Постійне посилання на цей заголовок"></a></h2>
<p>Ми бачимо, що хвилі можуть бути безперервною сутністю як у часі, так і в просторі. Але в реальності ми часто дискретизуємо час і простір у різних точках. Наприклад, ми можемо використовувати датчики, такі як акселерометри (які можуть вимірювати прискорення руху), у різних місцях на Землі для моніторингу землетрусів, що є просторовою дискретизацією. Аналогічно, ці датчики зазвичай записують дані в певний час, що є часовою дискретизацією. Для однієї хвилі існують різні характеристики. Дивіться наступні два малюнки.</p>


<p>**Амплітуда** використовується для опису різниці між максимальними значеннями та базовим значенням (див. вищезазначені малюнки). Синусоїдальна хвиля є періодичним сигналом, що означає, що вона повторюється через певний час, який можна виміряти за допомогою **періоду**. Період хвилі — це час, необхідний для завершення повного циклу; на малюнку ми бачимо, що період можна виміряти за двома сусідніми піками. **Довжина хвилі** вимірює відстань між двома послідовними гребенями або западинами хвилі. **Частота** описує кількість хвиль, що проходять через фіксоване місце за певний проміжок часу. Частоту можна виміряти за кількістю циклів, що проходять за 1 секунду. Отже, одиницею частоти є цикли/секунду, або частіше використовується **Герц** (скорочено **Гц**). Частота відрізняється від періоду, але вони пов'язані між собою. Частота вказує, як часто щось відбувається, тоді як період вказує на час, необхідний для завершення чогось, математично,</p>

\[period = \frac{1}{frequency}\]
<p>З двох малюнків ми також бачимо сині крапки на синусоїдальних хвилях — це точки дискретизації, які ми зробили як у часі, так і в просторі. Отже, лише в цих точках ми взяли значення хвилі. Зазвичай, коли ми записуємо хвилю, нам потрібно вказати, як часто ми беремо зразки хвилі в часі, це називається **дискретизацією** (або **вибіркою**). І ця швидкість називається **частотою дискретизації** (або **частотою вибірки**), з одиницею Гц. Наприклад, якщо ми дискретизуємо хвилю з частотою 2 Гц, це означає, що кожну секунду ми беремо дві точки даних. Оскільки ми краще розуміємо основи хвилі, тепер давайте розглянемо синусоїдальну хвилю уважніше. Синусоїдальна хвиля може бути представлена наступним рівнянням:</p>

\[ y(t) = Asin(\omega{t}+\phi)\]
<p>де <span>\(A\)</span> — амплітуда хвилі, <span>\(\omega\)</span> — **кутова частота**, яка визначає, скільки циклів відбувається за секунду, у радіанах за секунду. <span>\(\phi\)</span> — **фаза** сигналу. Якщо <span>\(T\)</span> — період хвилі, а <span>\(f\)</span> — частота хвилі, то <span>\(\omega\)</span> має наступний зв'язок з ними:</p>

\[\omega = \frac{2\pi}{T} = 2\pi{f}\]
<p>**СПРОБУЙТЕ!** Згенеруйте дві синусоїдальні хвилі з часом від 0 до 1 секунди та частотою 5 Гц і 10 Гц, усі дискретизовані з частотою 100 Гц. Побудуйте графіки двох хвиль і подивіться різницю. Підрахуйте, скільки циклів відбувається за 1 секунду.</p>


<pre><span></span><span># sampling rate</span>
<span>sr</span> <span>=</span> <span>100.0</span>
<span># sampling interval</span>
<span>ts</span> <span>=</span> <span>1.0</span><span>/</span><span>sr</span>
<span>t</span> <span>=</span> <span>np</span><span>.</span><span>arange</span><span>(</span><span>0</span><span>,</span><span>1</span><span>,</span><span>ts</span><span>)</span>

<span># frequency of the signal</span>
<span>freq</span> <span>=</span> <span>5</span>   
<span>y</span> <span>=</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>2</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>*</span><span>freq</span><span>*</span><span>t</span><span>)</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>8</span><span>,</span> <span>8</span><span>))</span>
<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>211</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>t</span><span>,</span> <span>y</span><span>,</span> <span>'b'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Amplitude'</span><span>)</span>

<span>freq</span> <span>=</span> <span>10</span>   
<span>y</span> <span>=</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>2</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>*</span><span>freq</span><span>*</span><span>t</span><span>)</span>

<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>212</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>t</span><span>,</span> <span>y</span><span>,</span> <span>'b'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Amplitude'</span><span>)</span>

<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'Time (s)'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="../_images/chapter24.01-The-Basics-of-waves_9_0.png" src="../_images/chapter24.01-The-Basics-of-waves_9_0.png"/>


<p>**СПРОБУЙТЕ!** Згенеруйте дві синусоїдальні хвилі з часом від 0 до 1 секунди. Обидві хвилі мають частоту 5 Гц і дискретизовані з частотою 100 Гц, але фаза становить 0 і 10 відповідно. Також амплітуда двох хвиль становить 5 і 10. Побудуйте графіки двох хвиль і подивіться різницю.</p>


<pre><span></span><span># frequency of the signal</span>
<span>freq</span> <span>=</span> <span>5</span>   
<span>y</span> <span>=</span> <span>5</span><span>*</span><span>np</span><span>.</span><span>sin</span><span>(</span><span>2</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>*</span><span>freq</span><span>*</span><span>t</span><span>)</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>8</span><span>,</span> <span>8</span><span>))</span>
<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>211</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>t</span><span>,</span> <span>y</span><span>,</span> <span>'b'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Amplitude'</span><span>)</span>

<span>y</span> <span>=</span> <span>10</span><span>*</span><span>np</span><span>.</span><span>sin</span><span>(</span><span>2</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>*</span><span>freq</span><span>*</span><span>t</span> <span>+</span> <span>10</span><span>)</span>

<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>212</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>t</span><span>,</span> <span>y</span><span>,</span> <span>'b'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Amplitude'</span><span>)</span>

<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'Time (s)'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="../_images/chapter24.01-The-Basics-of-waves_11_0.png" src="../_images/chapter24.01-The-Basics-of-waves_11_0.png"/>
