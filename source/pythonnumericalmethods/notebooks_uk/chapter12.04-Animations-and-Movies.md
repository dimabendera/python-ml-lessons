<h1>Анімації та відео<a href="#animations-and-movies" title="Постійне посилання на цей заголовок"></a></h1>
<p>Анімація — це послідовність нерухомих кадрів або графіків, які відображаються досить швидко, щоб створити ілюзію безперервного руху. Анімації та відео часто передають інформацію краще, ніж окремі графіки. Ви можете створювати анімації в Python, викликаючи функцію побудови графіка всередині циклу (зазвичай циклу for). Основним інструментом для створення анімацій в Python є базовий клас <em>matplotlib.animation.Animation</em>, який надає основу для побудови функціональності анімації. Розглянемо приклад.</p>
<p><strong>СПРОБУЙТЕ!</strong> Створіть анімацію червоного кола, що рухається вздовж синьої синусоїди.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
<span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>
<span>import</span> <span>matplotlib.animation</span> <span>as</span> <span>manimation</span>
</pre>





<pre><span></span><span>n</span> <span>=</span> <span>1000</span>
<span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>6</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>,</span> <span>n</span><span>)</span>
<span>y</span> <span>=</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>x</span><span>)</span>

<span># Визначення метаданих для відео</span>
<span>FFMpegWriter</span> <span>=</span> <span>manimation</span><span>.</span><span>writers</span><span>[</span><span>'ffmpeg'</span><span>]</span>
<span>metadata</span> <span>=</span> <span>dict</span><span>(</span><span>title</span><span>=</span><span>'Movie Test'</span><span>,</span> <span>artist</span><span>=</span><span>'Matplotlib'</span><span>,</span>
                <span>comment</span><span>=</span><span>'червоне коло рухається вздовж синьої синусоїди'</span><span>)</span>
<span>writer</span> <span>=</span> <span>FFMpegWriter</span><span>(</span><span>fps</span><span>=</span><span>15</span><span>,</span> <span>metadata</span><span>=</span><span>metadata</span><span>)</span>

<span># Ініціалізація відео</span>
<span>fig</span> <span>=</span> <span>plt</span><span>.</span><span>figure</span><span>()</span>

<span># побудова лінії синусоїди</span>
<span>sine_line</span><span>,</span> <span>=</span> <span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>'b'</span><span>)</span>
<span>red_circle</span><span>,</span> <span>=</span> <span>plt</span><span>.</span><span>plot</span><span>([],</span> <span>[],</span> <span>'ro'</span><span>,</span> <span>markersize</span> <span>=</span> <span>10</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'x'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'sin(x)'</span><span>)</span>

<span># Оновлення кадрів для відео</span>
<span>with</span> <span>writer</span><span>.</span><span>saving</span><span>(</span><span>fig</span><span>,</span> <span>"writer_test.mp4"</span><span>,</span> <span>100</span><span>):</span>
    <span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>n</span><span>):</span>
        <span>x0</span> <span>=</span> <span>x</span><span>[</span><span>i</span><span>]</span>
        <span>y0</span> <span>=</span> <span>y</span><span>[</span><span>i</span><span>]</span>
        <span>red_circle</span><span>.</span><span>set_data</span><span>(</span><span>x0</span><span>,</span> <span>y0</span><span>)</span>
        <span>writer</span><span>.</span><span>grab_frame</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.04-Animations-and-Movies_5_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.04-Animations-and-Movies_5_0.png"/>




<pre><span></span><span># не турбуйтеся про код у цій клітинці, він лише для того, щоб ви могли</span>
<span># відобразити створені вище відео в Jupyter notebook</span>
<span>from</span> <span>IPython.display</span> <span>import</span> <span>HTML</span>

<span>HTML</span><span>(</span><span>"""</span>
<span>&lt;div align="middle"&gt;</span>
<span>&lt;video width="80%" controls&gt;</span>
<span>      &lt;source src="writer_test.mp4" type="video/mp4"&gt;</span>
<span>&lt;/video&gt;&lt;/div&gt;"""</span><span>)</span>
</pre>




<div align="middle">
<video controls="" width="80%">
<source src="writer_test.html" type="video/mp4">
</source></video>

<p>Перш ніж створювати відео, краще спочатку підготувати 3 наступні елементи:</p>
<ol>
<li><p>визначити метадані для відео</p></li>
<li><p>вирішити, що на фоні не потребує змін</p></li>
<li><p>вирішити, які об'єкти повинні змінюватися в кожному кадрі відео</p></li>
</ol>
<p>Коли вищевказані елементи визначені, створення відео в Python стає відносно простим, нам потрібно виконати лише 3 кроки:</p>
<ol>
<li><p>визначити метадані для відео</p></li>
<li><p>ініціалізувати фонове зображення для відео</p></li>
<li><p>оновлювати кадри для відео</p></li>
</ol>
<p>У наведеному вище прикладі ми можемо чітко побачити код, пов'язаний з цими 3 кроками.</p>
<p><strong>1. Визначення метаданих для відео</strong></p>
<pre><span></span><span>FFMpegWriter</span> <span>=</span> <span>manimation</span><span>.</span><span>writers</span><span>[</span><span>'ffmpeg'</span><span>]</span>
<span>metadata</span> <span>=</span> <span>dict</span><span>(</span><span>title</span><span>=</span><span>'Movie Test'</span><span>,</span> <span>artist</span><span>=</span><span>'Matplotlib'</span><span>,</span>
                <span>comment</span><span>=</span><span>'червоне коло рухається вздовж синьої синусоїди'</span><span>)</span>
<span>writer</span> <span>=</span> <span>FFMpegWriter</span><span>(</span><span>fps</span><span>=</span><span>15</span><span>,</span> <span>metadata</span><span>=</span><span>metadata</span><span>)</span>
</pre>

<p>У цьому блоці коду ми повідомляємо Python, що починаємо створювати записувач відео (writer) і надаємо йому назву, автора та коментар. Крім того, ми також вказуємо Python частоту кадрів у відео, тобто <em>fps=15</em>, що означає відображення 15 послідовних кадрів за 1 секунду (fps — кадри в секунду).</p>
<p><strong>2. Ініціалізація фонового зображення для відео</strong></p>
<pre><span></span><span>fig</span> <span>=</span> <span>plt</span><span>.</span><span>figure</span><span>()</span>

<span># побудова лінії синусоїди</span>
<span>sine_line</span><span>,</span> <span>=</span> <span>plt</span><span>.</span><span>plot</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>'b'</span><span>)</span>
<span>red_circle</span><span>,</span> <span>=</span> <span>plt</span><span>.</span><span>plot</span><span>([],</span> <span>[],</span> <span>'ro'</span><span>,</span> <span>markersize</span> <span>=</span> <span>10</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'x'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'sin(x)'</span><span>)</span>
</pre>

<p>Тут ми починаємо ініціалізацію фонового зображення для відео. Причина, чому ми називаємо його фоновим зображенням, полягає в тому, що елементи, які ми тут будуємо, не змінюватимуться протягом відео; у цьому прикладі крива синусоїди не зміниться. Водночас ми будуємо порожню червону точку (яка не з'явиться на зображенні). Вона слугує заповнювачем для елементів, які будуть змінюватися пізніше у відео, що еквівалентно повідомленню Python, що у нас буде червона точка, розташування якої ми будемо оновлювати. Оскільки підписи осей x та y також не змінюватимуться, ми будуємо їх тут.</p>
<p><strong>3. Оновлення кадрів для відео</strong></p>
<pre><span></span><span>with</span> <span>writer</span><span>.</span><span>saving</span><span>(</span><span>fig</span><span>,</span> <span>"writer_test.mp4"</span><span>,</span> <span>100</span><span>):</span>
    <span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>n</span><span>):</span>
        <span>x0</span> <span>=</span> <span>x</span><span>[</span><span>i</span><span>]</span>
        <span>y0</span> <span>=</span> <span>y</span><span>[</span><span>i</span><span>]</span>
        <span>red_circle</span><span>.</span><span>set_data</span><span>(</span><span>x0</span><span>,</span> <span>y0</span><span>)</span>
        <span>writer</span><span>.</span><span>grab_frame</span><span>()</span>
</pre>

<p>У цьому блоці коду ми вказуємо назву вихідного файлу, формат і роздільну здатність зображення (dpi - точок на дюйм), у цьому випадку ми хочемо, щоб вихідний файл мав назву 'writer_test' у форматі 'mp4', і щоб dpi зображення було 100. Далі ми переходимо до основної частини створення відео — оновлення зображення. Ми використовуємо цикл for для оновлення зображення, і в кожній ітерації циклу ми змінюємо розташування (координати x, y) червоного кола. Функція <em>writer.grab_frame</em> фіксуватиме цю зміну в кожному кадрі та відображатиме її відповідно до встановленого нами fps.</p>
<p>Це весь процес створення цього відео.</p>
<p>Існує багато прикладів створення відео в <a href="https://matplotlib.org/api/animation_api.html">посібнику з анімації matplotlib</a>, перегляньте та запустіть деякі з них, щоб краще зрозуміти, як створювати відео в Python.</p>
</div>
