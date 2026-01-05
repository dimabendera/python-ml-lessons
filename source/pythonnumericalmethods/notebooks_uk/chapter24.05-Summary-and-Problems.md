<h1>Підсумок<a href="#summary" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Ми вивчили основи хвиль: частота, період, амплітуда та довжина хвилі є характеристиками хвиль.</p></li>
<li><p>Дискретне перетворення Фур'є (ДПФ) — це спосіб перетворення сигналу з часової області в частотну область за допомогою суми послідовності синусоїдальних хвиль.</p></li>
<li><p>Швидке перетворення Фур'є (ШПФ) — це алгоритм для ефективного обчислення ДПФ, використовуючи властивості симетрії в ДПФ.</p></li>
</ol>


<h1>Задачі<a href="#problems" title="Постійне посилання на цей заголовок"></a></h1>
<ol>
<li><p>Вам доручено виміряти температуру в кімнаті. Щодня опівдні ви вимірюєте температуру та записуєте значення. Ви проводили вимірювання протягом 30 днів. Яка частота температурного сигналу, який ви отримали?</p></li>
<li><p>Який зв'язок між частотою та періодом хвилі?</p></li>
<li><p>Яка різниця між періодом та довжиною хвилі? Які між ними подібності?</p></li>
<li><p>Що таке представлення сигналу в часовій та частотній областях?</p></li>
<li><p>Згенеруйте два сигнали: сигнал 1 — синусоїдальна хвиля з частотою 5 Гц, амплітудою 3 та фазовим зсувом 3; сигнал 2 — синусоїдальна хвиля з частотою 2 Гц, амплітудою 2 та фазовим зсувом -2. Побудуйте графік сигналу за 2 секунди. Приклади:</p></li>
</ol>


<pre><span></span><span># sampling rate</span>
<span>sr</span> <span>=</span> <span>100</span>
<span># sampling interval</span>
<span>ts</span> <span>=</span> <span>1.0</span><span>/</span><span>sr</span>
<span>t</span> <span>=</span> <span>np</span><span>.</span><span>arange</span><span>(</span><span>0</span><span>,</span><span>2</span><span>,</span><span>ts</span><span>)</span>

<span>freq</span> <span>=</span> <span>5.</span>
<span>x</span> <span>=</span> <span>3</span><span>*</span><span>np</span><span>.</span><span>sin</span><span>(</span><span>2</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>*</span><span>freq</span><span>*</span><span>t</span> <span>+</span> <span>3</span><span>)</span>

<span>freq</span> <span>=</span> <span>2</span>
<span>x</span> <span>+=</span> <span>2</span><span>*</span><span>np</span><span>.</span><span>sin</span><span>(</span><span>2</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>*</span><span>freq</span><span>*</span><span>t</span> <span>-</span> <span>2</span><span>)</span>


<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>8</span><span>,</span> <span>6</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>t</span><span>,</span> <span>x</span><span>,</span> <span>'r'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Amplitude'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'Time (s)'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="../_images/chapter24.05-Summary-and-Problems_4_0.png" src="../_images/chapter24.05-Summary-and-Problems_4_0.png"/>


<ol>
<li><p>Оцифруйте сигнал, який ви згенерували в задачі 5, використовуючи частоту дискретизації 5, 10, 20, 50 та 100 Гц, і подивіться на відмінності між різними частотами дискретизації.</p></li>
<li><p>Дано сигнал t = [0, 1, 2, 3] та y = [0, 3, 2, 0], знайдіть дійсне ДПФ для X. Запишіть вираз для оберненого ДПФ. Зауважте, не використовуйте Python для пошуку результатів, замість цього запишіть рівняння та обчисліть значення.</p></li>
<li><p>Які амплітуда та фаза значень ДПФ для сигналу?</p></li>
<li><p>Ми реалізували ДПФ раніше, чи можете ви аналогічно реалізувати обернене дискретне перетворення Фур'є в Python?</p></li>
<li><p>Використайте функцію ДПФ та оберненого ДПФ, які ми реалізували, та згенеруйте амплітудний спектр для сигналу, який ви згенерували в задачі 5. Нормалізуйте амплітуду ДПФ, щоб отримати правильну відповідну амплітуду в часовій області.</p></li>
<li><p>Чи можете ви описати прийоми, що використовуються в ШПФ для прискорення обчислень?</p></li>
<li><p>Використайте функції fft та ifft з scipy, щоб повторити задачу 10.</p></li>
<li><p>Додайте випадковий шум з нормальним розподілом до сигналу в задачі 5 за допомогою numpy та побудуйте графік амплітудного спектра ШПФ, що ви бачите? Сигнал із шумом буде показано як наступний приклад.</p></li>
</ol>
<p>Приклад:</p>


<pre><span></span><span>np</span><span>.</span><span>random</span><span>.</span><span>seed</span><span>(</span><span>10</span><span>)</span>
<span>x_noise</span> <span>=</span> <span>x</span> <span>+</span> \
  <span>np</span><span>.</span><span>random</span><span>.</span><span>normal</span><span>(</span><span>0</span><span>,</span> <span>2</span><span>,</span> <span>size</span> <span>=</span> <span>len</span><span>(</span><span>x</span><span>))</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>8</span><span>,</span> <span>6</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>t</span><span>,</span> <span>x_noise</span><span>,</span> <span>'r'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Amplitude'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'Time (s)'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="../_images/chapter24.05-Summary-and-Problems_6_0.png" src="../_images/chapter24.05-Summary-and-Problems_6_0.png"/>
