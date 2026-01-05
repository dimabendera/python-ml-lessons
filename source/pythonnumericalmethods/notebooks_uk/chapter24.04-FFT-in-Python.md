<h1>ШПФ у Python<a href="#fft-in-python" title="Permalink to this headline"></a></h1>
<p>У Python існують дуже розвинені функції ШПФ як у <em>numpy</em>, так і в <em>scipy</em>. У цьому розділі ми розглянемо обидва пакети та побачимо, як ми можемо легко використовувати їх у нашій роботі. Давайте спочатку згенеруємо сигнал, як і раніше.</p>


<pre><span></span><span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>
<span>import</span> <span>numpy</span> <span>as</span> <span>np</span>

<span>plt</span><span>.</span><span>style</span><span>.</span><span>use</span><span>(</span><span>'seaborn-poster'</span><span>)</span>
<span>%</span><span>matplotlib</span> inline
</pre>





<pre><span></span><span># частота дискретизації</span>
<span>sr</span> <span>=</span> <span>2000</span>
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



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.04-FFT-in-Python_5_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.04-FFT-in-Python_5_0.png"/>



<h2>ШПФ у Numpy<a href="#fft-in-numpy" title="Permalink to this headline"></a></h2>
<p><strong>ПРИКЛАД:</strong> Використайте функції <em>fft</em> та <em>ifft</em> з <em>numpy</em> для обчислення амплітудного спектра ШПФ та зворотного ШПФ для отримання вихідного сигналу. Побудуйте графіки обох результатів. Виміряйте час виконання функції <em>fft</em> для цього сигналу довжиною 2000.</p>


<pre><span></span><span>from</span> <span>numpy.fft</span> <span>import</span> <span>fft</span><span>,</span> <span>ifft</span>

<span>X</span> <span>=</span> <span>fft</span><span>(</span><span>x</span><span>)</span>
<span>N</span> <span>=</span> <span>len</span><span>(</span><span>X</span><span>)</span>
<span>n</span> <span>=</span> <span>np</span><span>.</span><span>arange</span><span>(</span><span>N</span><span>)</span>
<span>T</span> <span>=</span> <span>N</span><span>/</span><span>sr</span>
<span>freq</span> <span>=</span> <span>n</span><span>/</span><span>T</span> 

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>12</span><span>,</span> <span>6</span><span>))</span>
<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>121</span><span>)</span>

<span>plt</span><span>.</span><span>stem</span><span>(</span><span>freq</span><span>,</span> <span>np</span><span>.</span><span>abs</span><span>(</span><span>X</span><span>),</span> <span>'b'</span><span>,</span> \
         <span>markerfmt</span><span>=</span><span>" "</span><span>,</span> <span>basefmt</span><span>=</span><span>"-b"</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'Частота (Гц)'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Амплітуда ШПФ |X(freq)|'</span><span>)</span>
<span>plt</span><span>.</span><span>xlim</span><span>(</span><span>0</span><span>,</span> <span>10</span><span>)</span>

<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>122</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>t</span><span>,</span> <span>ifft</span><span>(</span><span>X</span><span>),</span> <span>'r'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'Час (с)'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Амплітуда'</span><span>)</span>
<span>plt</span><span>.</span><span>tight_layout</span><span>()</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<pre><span></span>/Users/qingkaikong/miniconda3/lib/python3.6/site-packages/ipykernel_launcher.py:13: UserWarning: In Matplotlib 3.3 individual lines on a stem plot will be added as a LineCollection instead of individual lines. This significantly improves the performance of a stem plot. To remove this warning and switch to the new behaviour, set the "use_line_collection" keyword argument to True.
  del sys.path[0]
/Users/qingkaikong/miniconda3/lib/python3.6/site-packages/numpy/core/numeric.py:538: ComplexWarning: Casting complex values to real discards the imaginary part
  return array(a, dtype, copy=False, order=order)
</pre>

<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.04-FFT-in-Python_7_1.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.04-FFT-in-Python_7_1.png"/>




<pre><span></span><span>%</span><span>timeit</span> fft(x)
</pre>



<pre><span></span>36.2 µs ± 775 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
</pre>





<h2>ШПФ у Scipy<a href="#fft-in-scipy" title="Permalink to this headline"></a></h2>
<p><strong>ПРИКЛАД:</strong> Використайте функції <em>fft</em> та <em>ifft</em> з <em>scipy</em> для обчислення амплітудного спектра ШПФ та зворотного ШПФ для отримання вихідного сигналу. Побудуйте графіки обох результатів. Виміряйте час виконання функції <em>fft</em> для цього сигналу довжиною 2000.</p>


<pre><span></span><span>from</span> <span>scipy.fftpack</span> <span>import</span> <span>fft</span><span>,</span> <span>ifft</span>

<span>X</span> <span>=</span> <span>fft</span><span>(</span><span>x</span><span>)</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>12</span><span>,</span> <span>6</span><span>))</span>
<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>121</span><span>)</span>

<span>plt</span><span>.</span><span>stem</span><span>(</span><span>freq</span><span>,</span> <span>np</span><span>.</span><span>abs</span><span>(</span><span>X</span><span>),</span> <span>'b'</span><span>,</span> \
         <span>markerfmt</span><span>=</span><span>" "</span><span>,</span> <span>basefmt</span><span>=</span><span>"-b"</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'Частота (Гц)'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Амплітуда ШПФ |X(freq)|'</span><span>)</span>
<span>plt</span><span>.</span><span>xlim</span><span>(</span><span>0</span><span>,</span> <span>10</span><span>)</span>

<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>122</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>t</span><span>,</span> <span>ifft</span><span>(</span><span>X</span><span>),</span> <span>'r'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'Час (с)'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Амплітуда'</span><span>)</span>
<span>plt</span><span>.</span><span>tight_layout</span><span>()</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<pre><span></span>/Users/qingkaikong/miniconda3/lib/python3.6/site-packages/ipykernel_launcher.py:9: UserWarning: In Matplotlib 3.3 individual lines on a stem plot will be added as a LineCollection instead of individual lines. This significantly improves the performance of a stem plot. To remove this warning and switch to the new behaviour, set the "use_line_collection" keyword argument to True.
  if __name__ == '__main__':
</pre>

<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.04-FFT-in-Python_10_1.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.04-FFT-in-Python_10_1.png"/>




<pre><span></span><span>%</span><span>timeit</span> fft(x)
</pre>



<pre><span></span>14.8 µs ± 471 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
</pre>



<p>Тепер ми бачимо, що вбудовані функції ШПФ набагато швидші та простіші у використанні, особливо версія з scipy. Ось результати для порівняння:</p>
<ul>
<li><p>Реалізоване ДПФ: ~120 мс</p></li>
<li><p>Реалізоване ШПФ: ~16 мс</p></li>
<li><p>ШПФ з Numpy: ~40 мкс</p></li>
<li><p>ШПФ з Scipy: ~12 мкс</p></li>
</ul>


<h2>Більше прикладів<a href="#more-examples" title="Permalink to this headline"></a></h2>
<p>Давайте розглянемо ще кілька прикладів використання ШПФ у реальних застосунках.</p>

<h3>Попит на електроенергію в Каліфорнії<a href="#electricity-demand-in-california" title="Permalink to this headline"></a></h3>
<p>Спочатку ми дослідимо попит на електроенергію в Каліфорнії з 30.11.2019 по 30.12.2019. Ви можете завантажити дані з <a href="https://www.eia.gov/beta/electricity/gridmonitor/dashboard/electric_overview/US48/US48">Управління енергетичної інформації США</a>. Тут я вже завантажив дані, тому ми будемо використовувати їх безпосередньо.</p>
<p>Дані про попит на електроенергію в Каліфорнії зберігаються у файлі ‘930-data-export.csv` у 3 стовпцях. Пам'ятаєте, ми вчилися читати CSV-файли за допомогою <code><span>numpy</span></code>. Тут ми використаємо інший пакет - <code><span>pandas</span></code>, який є дуже популярним для роботи з часовими рядами. Ми не будемо навчати вас цьому пакету тут, як вправу, ви повинні навчитися використовувати його самостійно. Давайте спочатку зчитаємо дані.</p>


<pre><span></span><span>import</span> <span>pandas</span> <span>as</span> <span>pd</span>
</pre>



<p>Функція <code><span>read_csv</span></code> зчитує CSV-файл. Зверніть увагу на параметр <code><span>parse_dates</span></code>, який знайде дату та час у першому стовпці. Дані будуть зчитані в pandas <code><span>DataFrame</span></code>, ми використовуємо <code><span>df</span></code> для їх зберігання. Потім ми змінимо заголовок в оригінальному файлі на щось простіше у використанні.</p>


<pre><span></span><span>df</span> <span>=</span> <span>pd</span><span>.</span><span>read_csv</span><span>(</span><span>'./data/930-data-export.csv'</span><span>,</span>
                 <span>delimiter</span><span>=</span><span>','</span><span>,</span> <span>parse_dates</span><span>=</span><span>[</span><span>1</span><span>])</span>
<span>df</span><span>.</span><span>rename</span><span>(</span><span>columns</span><span>=</span><span>{</span><span>'Timestamp (Hour Ending)'</span><span>:</span><span>'hour'</span><span>,</span>
                   <span>'Total CAL Demand (MWh)'</span><span>:</span><span>'demand'</span><span>},</span>
          <span>inplace</span><span>=</span><span>True</span><span>)</span>
</pre>



<p>Ми можемо побудувати графік даних і побачити, як попит на електроенергію змінюється з часом.</p>


<pre><span></span><span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>12</span><span>,</span> <span>6</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>df</span><span>[</span><span>'hour'</span><span>],</span> <span>df</span><span>[</span><span>'demand'</span><span>])</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'Дата і час'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Попит на електроенергію в Каліфорнії (МВт·год)'</span><span>)</span>
<span>plt</span><span>.</span><span>xticks</span><span>(</span><span>rotation</span><span>=</span><span>25</span><span>)</span> 
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<pre><span></span>/Users/qingkaikong/miniconda3/lib/python3.6/site-packages/pandas/plotting/_converter.py:129: FutureWarning: Using an implicitly registered datetime converter for a matplotlib plotting method. The converter was registered by pandas on import. Future versions of pandas will require you to explicitly register matplotlib converters.

To register the converters:
	&gt;&gt;&gt; from pandas.plotting import register_matplotlib_converters
	&gt;&gt;&gt; register_matplotlib_converters()
  warnings.warn(msg, FutureWarning)
</pre>

<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.04-FFT-in-Python_18_1.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.04-FFT-in-Python_18_1.png"/>


<p>З побудованого часового ряду важко сказати, чи є якісь закономірності в даних. Давайте перетворимо дані в частотну область і подивимося, чи є щось цікаве.</p>


<pre><span></span><span>X</span> <span>=</span> <span>fft</span><span>(</span><span>df</span><span>[</span><span>'demand'</span><span>])</span>
<span>N</span> <span>=</span> <span>len</span><span>(</span><span>X</span><span>)</span>
<span>n</span> <span>=</span> <span>np</span><span>.</span><span>arange</span><span>(</span><span>N</span><span>)</span>
<span># отримати частоту дискретизації</span>
<span>sr</span> <span>=</span> <span>1</span> <span>/</span> <span>(</span><span>60</span><span>*</span><span>60</span><span>)</span>
<span>T</span> <span>=</span> <span>N</span><span>/</span><span>sr</span>
<span>freq</span> <span>=</span> <span>n</span><span>/</span><span>T</span> 

<span># Отримати односторонній спектр</span>
<span>n_oneside</span> <span>=</span> <span>N</span><span>//</span><span>2</span>
<span># отримати односторонню частоту</span>
<span>f_oneside</span> <span>=</span> <span>freq</span><span>[:</span><span>n_oneside</span><span>]</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>12</span><span>,</span> <span>6</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>f_oneside</span><span>,</span> <span>np</span><span>.</span><span>abs</span><span>(</span><span>X</span><span>[:</span><span>n_oneside</span><span>]),</span> <span>'b'</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'Частота (Гц)'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Амплітуда ШПФ |X(freq)|'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.04-FFT-in-Python_20_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.04-FFT-in-Python_20_0.png"/>


<p>Ми бачимо деякі чіткі піки на графіку амплітуди ШПФ, але важко сказати, що вони означають у термінах частоти. Давайте побудуємо результати, використовуючи години, і виділимо деякі години, пов'язані з піками.</p>


<pre><span></span><span># перетворити частоту в години</span>
<span>t_h</span> <span>=</span> <span>1</span><span>/</span><span>f_oneside</span> <span>/</span> <span>(</span><span>60</span> <span>*</span> <span>60</span><span>)</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span><span>=</span><span>(</span><span>12</span><span>,</span><span>6</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>t_h</span><span>,</span> <span>np</span><span>.</span><span>abs</span><span>(</span><span>X</span><span>[:</span><span>n_oneside</span><span>])</span><span>/</span><span>n_oneside</span><span>)</span>
<span>plt</span><span>.</span><span>xticks</span><span>([</span><span>12</span><span>,</span> <span>24</span><span>,</span> <span>84</span><span>,</span> <span>168</span><span>])</span>
<span>plt</span><span>.</span><span>xlim</span><span>(</span><span>0</span><span>,</span> <span>200</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'Період (година)'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<pre><span></span>/Users/qingkaikong/miniconda3/lib/python3.6/site-packages/ipykernel_launcher.py:2: RuntimeWarning: divide by zero encountered in true_divide
  
</pre>

<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.04-FFT-in-Python_22_1.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.04-FFT-in-Python_22_1.png"/>


<p>Тепер ми можемо побачити деякі цікаві закономірності, а саме три піки, пов'язані з 12, 24 та 84 годинами. Ці піки означають, що ми бачимо деякий повторюваний сигнал кожні 12, 24 та 84 години. Це має сенс і відповідає нашим патернам людської активності. ШПФ може допомогти нам зрозуміти деякі повторювані сигнали в нашому фізичному світі.</p>


<h3>Фільтрація сигналу за допомогою ШПФ<a href="#filtering-a-signal-using-fft" title="Permalink to this headline"></a></h3>
<p>Фільтрація — це процес в обробці сигналів для видалення небажаної частини сигналу в певному частотному діапазоні. Існують фільтри низьких частот, які намагаються видалити всі сигнали вище певної частоти зрізу, і фільтри високих частот, які роблять протилежне. Поєднуючи фільтри низьких і високих частот, ми отримаємо смуговий фільтр, що означає, що ми зберігаємо лише сигнали в межах пари частот. Використовуючи ШПФ, ми можемо легко це зробити. Давайте розглянемо наступний приклад, щоб проілюструвати основи смугового фільтра. Примітка: ми просто хочемо показати ідею фільтрації за допомогою дуже простих операцій, насправді процеси фільтрації набагато складніші.</p>
<p><strong>ПРИКЛАД:</strong> Ми можемо використати сигнал, який ми згенерували на початку цього розділу (змішані синусоїди з частотами 1, 4 та 7 Гц), і застосувати до нього фільтр високих частот з частотою зрізу 6 Гц. Побудуйте графік відфільтрованого сигналу та амплітуди ШПФ до та після фільтрації.</p>


<pre><span></span><span>from</span> <span>scipy.fftpack</span> <span>import</span> <span>fftfreq</span>
</pre>





<pre><span></span><span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>8</span><span>,</span> <span>6</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>t</span><span>,</span> <span>x</span><span>,</span> <span>'r'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Амплітуда'</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>'Вихідний сигнал'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.04-FFT-in-Python_25_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.04-FFT-in-Python_25_0.png"/>




<pre><span></span><span># ШПФ сигналу</span>
<span>sig_fft</span> <span>=</span> <span>fft</span><span>(</span><span>x</span><span>)</span>
<span># копіюємо результати ШПФ</span>
<span>sig_fft_filtered</span> <span>=</span> <span>sig_fft</span><span>.</span><span>copy</span><span>()</span>

<span># отримуємо частоти за допомогою функції scipy</span>
<span>freq</span> <span>=</span> <span>fftfreq</span><span>(</span><span>len</span><span>(</span><span>x</span><span>),</span> <span>d</span><span>=</span><span>1.</span><span>/</span><span>2000</span><span>)</span>

<span># визначаємо частоту зрізу</span>
<span>cut_off</span> <span>=</span> <span>6</span>

<span># фільтр високих частот шляхом присвоєння нулів</span>
<span># амплітудам ШПФ, де абсолютні</span>
<span># частоти менші за частоту зрізу</span>
<span>sig_fft_filtered</span><span>[</span><span>np</span><span>.</span><span>abs</span><span>(</span><span>freq</span><span>)</span> <span>&lt;</span> <span>cut_off</span><span>]</span> <span>=</span> <span>0</span>

<span># отримуємо відфільтрований сигнал у часовій області</span>
<span>filtered</span> <span>=</span> <span>ifft</span><span>(</span><span>sig_fft_filtered</span><span>)</span>

<span># будуємо графік відфільтрованого сигналу</span>
<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>12</span><span>,</span> <span>6</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>t</span><span>,</span> <span>filtered</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'Час (с)'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Амплітуда'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>

<span># будуємо графік амплітуди ШПФ до та після</span>
<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>12</span><span>,</span> <span>6</span><span>))</span>
<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>121</span><span>)</span>
<span>plt</span><span>.</span><span>stem</span><span>(</span><span>freq</span><span>,</span> <span>np</span><span>.</span><span>abs</span><span>(</span><span>sig_fft</span><span>),</span> <span>'b'</span><span>,</span> \
         <span>markerfmt</span><span>=</span><span>" "</span><span>,</span> <span>basefmt</span><span>=</span><span>"-b"</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>'До фільтрації'</span><span>)</span>
<span>plt</span><span>.</span><span>xlim</span><span>(</span><span>0</span><span>,</span> <span>10</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'Частота (Гц)'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Амплітуда ШПФ'</span><span>)</span>
<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>122</span><span>)</span>
<span>plt</span><span>.</span><span>stem</span><span>(</span><span>freq</span><span>,</span> <span>np</span><span>.</span><span>abs</span><span>(</span><span>sig_fft_filtered</span><span>),</span> <span>'b'</span><span>,</span> \
         <span>markerfmt</span><span>=</span><span>" "</span><span>,</span> <span>basefmt</span><span>=</span><span>"-b"</span><span>)</span>
<span>plt</span><span>.</span><span>title</span><span>(</span><span>'Після фільтрації'</span><span>)</span>
<span>plt</span><span>.</span><span>xlim</span><span>(</span><span>0</span><span>,</span> <span>10</span><span>)</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'Частота (Гц)'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Амплітуда ШПФ'</span><span>)</span>
<span>plt</span><span>.</span><span>tight_layout</span><span>()</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<pre><span></span>/Users/qingkaikong/miniconda3/lib/python3.6/site-packages/numpy/core/numeric.py:538: ComplexWarning: Casting complex values to real discards the imaginary part
  return array(a, dtype, copy=False, order=order)
</pre>

<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.04-FFT-in-Python_26_1.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.04-FFT-in-Python_26_1.png"/>
<pre><span></span>/Users/qingkaikong/miniconda3/lib/python3.6/site-packages/ipykernel_launcher.py:31: UserWarning: In Matplotlib 3.3 individual lines on a stem plot will be added as a LineCollection instead of individual lines. This significantly improves the performance of a stem plot. To remove this warning and switch to the new behaviour, set the "use_line_collection" keyword argument to True.
/Users/qingkaikong/miniconda3/lib/python3.6/site-packages/ipykernel_launcher.py:38: UserWarning: In Matplotlib 3.3 individual lines on a stem plot will be added as a LineCollection instead of individual lines. This significantly improves the performance of a stem plot. To remove this warning and switch to the new behaviour, set the "use_line_collection" keyword argument to True.
</pre>

<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.04-FFT-in-Python_26_3.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter24.04-FFT-in-Python_26_3.png"/>


<p>З наведеного вище прикладу, присвоюючи нулі амплітудам ШПФ для будь-яких абсолютних частот і повертаючись до сигналу в часовій області, ми за кілька кроків реалізуємо дуже простий фільтр високих частот. Ви можете спробувати самостійно реалізувати простий фільтр низьких частот або смуговий фільтр. Таким чином, ШПФ може допомогти нам отримати сигнал, який нас цікавить, і видалити небажані.</p>
<p>Існує також багато дивовижних застосувань ШПФ у науці та техніці, які ми залишаємо вам для самостійного дослідження.</p>
