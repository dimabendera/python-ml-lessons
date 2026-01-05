<h1>Швидке перетворення Фур'є (ШПФ)<a href="#fast-fourier-transform-fft" title="Permalink to this headline"></a></h1>
<p><strong>Швидке перетворення Фур'є (ШПФ)</strong> — це ефективний алгоритм для обчислення ДПФ послідовності. Вперше він був описаний у класичній статті Кулі та Тьюкі в 1965 році, але насправді ідея сягає неопублікованої роботи Гаусса в 1805 році. Це алгоритм «розділяй і володарюй», який рекурсивно розбиває ДПФ на менші ДПФ, щоб зменшити обчислення. В результаті він успішно зменшує складність ДПФ з <span>\(O(n^2)\)</span> до <span>\(O(nlogn)\)</span>, де <span>\(n\)</span> — розмір даних. Це скорочення часу обчислень є значним, особливо для даних з великим <span>\(N\)</span>, тому ШПФ широко використовується в інженерії, науці та математиці. Алгоритм ШПФ входить до <a href="https://www.computer.org/csdl/magazine/cs/2000/01/c1022/13rRUxBJhBm">10 найкращих алгоритмів 20-го століття</a> за версією журналу Computing in Science &amp; Engineering.</p>
<p>У цьому розділі ми розповімо, як ШПФ скорочує час обчислень. Зміст цього розділу значною мірою базується на цьому <a href="https://jakevdp.github.io/blog/2013/08/28/understanding-the-fft/">чудовому посібнику</a>, створеному <a href="http://vanderplas.com/">Джейком ВандерПласом</a>.</p>

<h2>Симетрії в ДПФ<a href="#symmetries-in-the-dft" title="Permalink to this headline"></a></h2>
<p>Відповідь на те, як ШПФ прискорює обчислення ДПФ, полягає у використанні симетрій в ДПФ. Давайте розглянемо симетрії в ДПФ. З визначення рівняння ДПФ</p>

\[X_k = \sum_{n=0}^{N-1}{x_n\cdot e^{-i2\pi{kn/N}}}\]
<p>ми можемо обчислити</p>

\[X_{k+N} = \sum_{n=0}^{N-1}{x_n\cdot e^{-i2\pi{(k+N)n/N}}} = \sum_{n=0}^{N-1}{x_n\cdot e^{-i2\pi{n}}\cdot e^{-i2\pi{kn/N}}}\]
<p>Зауважте, що <span>\(e^{-i2\pi{n}} = 1\)</span>, отже, ми маємо</p>

\[X_{k+N} = \sum_{n=0}^{N-1}{x_n\cdot e^{-i2\pi{kn/N}}} = X_k\]
<p>з невеликим розширенням, ми можемо отримати</p>

\[X_{k+i\cdot N} = X_k, \text{ для будь-якого цілого i}\]
<p>Це означає, що в межах ДПФ ми маємо симетрії, які можна використати для зменшення обчислень.</p>


<h2>Прийоми в ШПФ<a href="#tricks-in-fft" title="Permalink to this headline"></a></h2>
<p>Оскільки ми знаємо, що в ДПФ є симетрії, ми можемо розглянути їх використання для зменшення обчислень, бо якщо нам потрібно обчислити і <span>\(X_k\)</span>, і <span>\(X_{k+N}\)</span>, нам потрібно зробити це лише один раз. Саме ця ідея лежить в основі ШПФ. Кулі та Тьюкі показали, що ми можемо обчислювати ДПФ ефективніше, якщо продовжувати ділити задачу на менші. Давайте спочатку розділимо всю послідовність на дві частини, тобто на парну та непарну:</p>

\[\begin{eqnarray*}
X_{k} &amp;=&amp; \sum_{n=0}^{N-1}{x_n\cdot e^{-i2\pi{kn/N}}} \\
      &amp;=&amp; \sum_{m=0}^{N/2-1}{x_{2m}\cdot e^{-i2\pi{k(2m)/N}}} + \sum_{m=0}^{N/2-1}{x_{2m+1}\cdot e^{-i2\pi{k(2m+1)/N}}} \\
      &amp;=&amp; \sum_{m=0}^{N/2-1}{x_{2m}\cdot e^{-i2\pi{km/(N/2)}}} + e^{-i2\pi{k/N}}\sum_{m=0}^{N/2-1}{x_{2m+1}\cdot e^{-i2\pi{km/(N/2)}}}
\end{eqnarray*}\]
<p>Ми бачимо, що два менші доданки, які мають лише половину розміру (<span>\(\frac{N}{2}\)</span>) у наведеному вище рівнянні, є двома меншими ДПФ. Для кожного доданка <span>\( 0\leq m \le \frac{N}{2}\)</span>, але <span>\( 0\leq k \le N\)</span>, отже, ми бачимо, що половина значень буде однаковою через властивості симетрії, які ми описали вище. Таким чином, нам потрібно обчислити лише половину полів у кожному доданку. Звичайно, нам не потрібно зупинятися на цьому, ми можемо продовжувати ділити кожен доданок навпіл на парні та непарні значення, доки не дійдемо до останніх двох чисел, тоді обчислення буде справді простим.</p>
<p>Ось як працює ШПФ, використовуючи цей рекурсивний підхід. Давайте розглянемо швидку та просту реалізацію ШПФ. Зауважте, що вхідний сигнал для ШПФ повинен мати довжину, що є степенем 2. Якщо довжина не така, зазвичай нам потрібно доповнити нулями до наступного розміру, що є степенем 2.</p>


<pre><span></span><span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>
<span>import</span> <span>numpy</span> <span>as</span> <span>np</span>

<span>plt</span><span>.</span><span>style</span><span>.</span><span>use</span><span>(</span><span>'seaborn-poster'</span><span>)</span>
<span>%</span><span>matplotlib</span> inline
</pre>





<pre><span></span><span>def</span> <span>FFT</span><span>(</span><span>x</span><span>):</span>
    <span>"""</span>
<span>    Рекурсивна реалізація </span>
<span>    1D ШПФ Кулі-Тьюкі, </span>
<span>    вхідні дані повинні мати довжину, </span>
<span>    що є степенем 2. </span>
<span>    """</span>
    <span>N</span> <span>=</span> <span>len</span><span>(</span><span>x</span><span>)</span>
    
    <span>if</span> <span>N</span> <span>==</span> <span>1</span><span>:</span>
        <span>return</span> <span>x</span>
    <span>else</span><span>:</span>
        <span>X_even</span> <span>=</span> <span>FFT</span><span>(</span><span>x</span><span>[::</span><span>2</span><span>])</span>
        <span>X_odd</span> <span>=</span> <span>FFT</span><span>(</span><span>x</span><span>[</span><span>1</span><span>::</span><span>2</span><span>])</span>
        <span>factor</span> <span>=</span> \
          <span>np</span><span>.</span><span>exp</span><span>(</span><span>-</span><span>2</span><span>j</span><span>*</span><span>np</span><span>.</span><span>pi</span><span>*</span><span>np</span><span>.</span><span>arange</span><span>(</span><span>N</span><span>)</span><span>/</span> <span>N</span><span>)</span>
        
        <span>X</span> <span>=</span> <span>np</span><span>.</span><span>concatenate</span><span>(</span>\
            <span>[</span><span>X_even</span><span>+</span><span>factor</span><span>[:</span><span>int</span><span>(</span><span>N</span><span>/</span><span>2</span><span>)]</span><span>*</span><span>X_odd</span><span>,</span>
             <span>X_even</span><span>+</span><span>factor</span><span>[</span><span>int</span><span>(</span><span>N</span><span>/</span><span>2</span><span>):]</span><span>*</span><span>X_odd</span><span>])</span>
        <span>return</span> <span>X</span>
</pre>





<pre><span></span><span># частота дискретизації</span>
<span>sr</span> <span>=</span> <span>128</span>
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



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.03-Fast-Fourier-Transform_6_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.03-Fast-Fourier-Transform_6_0.png"/>


<p><strong>СПРОБУЙТЕ!</strong> Використайте функцію FFT для обчислення перетворення Фур'є наведеного вище сигналу. Побудуйте амплітудний спектр для двосторонніх та односторонніх частот.</p>


<pre><span></span><span>X</span><span>=</span><span>FFT</span><span>(</span><span>x</span><span>)</span>

<span># обчислити частоту</span>
<span>N</span> <span>=</span> <span>len</span><span>(</span><span>X</span><span>)</span>
<span>n</span> <span>=</span> <span>np</span><span>.</span><span>arange</span><span>(</span><span>N</span><span>)</span>
<span>T</span> <span>=</span> <span>N</span><span>/</span><span>sr</span>
<span>freq</span> <span>=</span> <span>n</span><span>/</span><span>T</span> 

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>12</span><span>,</span> <span>6</span><span>))</span>
<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>121</span><span>)</span>
<span>plt</span><span>.</span><span>stem</span><span>(</span><span>freq</span><span>,</span> <span>abs</span><span>(</span><span>X</span><span>),</span> <span>'b'</span><span>,</span> \
         <span>markerfmt</span><span>=</span><span>" "</span><span>,</span> <span>basefmt</span><span>=</span><span>"-b"</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'Частота (Гц)'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Амплітуда ШПФ |X(freq)|'</span><span>)</span>

<span># Отримати односторонній спектр</span>
<span>n_oneside</span> <span>=</span> <span>N</span><span>//</span><span>2</span>
<span># отримати односторонню частоту</span>
<span>f_oneside</span> <span>=</span> <span>freq</span><span>[:</span><span>n_oneside</span><span>]</span>

<span># нормалізувати амплітуду</span>
<span>X_oneside</span> <span>=</span><span>X</span><span>[:</span><span>n_oneside</span><span>]</span><span>/</span><span>n_oneside</span>

<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>122</span><span>)</span>
<span>plt</span><span>.</span><span>stem</span><span>(</span><span>f_oneside</span><span>,</span> <span>abs</span><span>(</span><span>X_oneside</span><span>),</span> <span>'b'</span><span>,</span> \
         <span>markerfmt</span><span>=</span><span>" "</span><span>,</span> <span>basefmt</span><span>=</span><span>"-b"</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'Частота (Гц)'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Нормалізована амплітуда ШПФ |X(freq)|'</span><span>)</span>
<span>plt</span><span>.</span><span>tight_layout</span><span>()</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.03-Fast-Fourier-Transform_8_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.03-Fast-Fourier-Transform_8_0.png"/>


<p><strong>СПРОБУЙТЕ!</strong> Згенеруйте простий сигнал довжиною 2048, заміряйте час виконання ШПФ та порівняйте швидкість з ДПФ.</p>


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





<pre><span></span><span># частота дискретизації = 2048</span>
<span>sr</span> <span>=</span> <span>2048</span>
<span>%</span><span>timeit</span> FFT(gen_sig(sr))
</pre>



<pre><span></span>16.9 мс ± 1.3 мс на цикл (середнє ± стандартне відхилення для 7 запусків, по 100 циклів у кожному)
</pre>



<p>Ми бачимо, що для сигналу довжиною 2048 (близько 2000) ця реалізація ШПФ займає 16.9 мс замість 120 мс при використанні ДПФ. Зауважте, що існує також багато способів оптимізації реалізації ШПФ, які зроблять її швидшою. У наступному розділі ми розглянемо вбудовані функції ШПФ в Python, які працюють набагато швидше.</p>
