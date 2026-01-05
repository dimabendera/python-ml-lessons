<h1>Розв'язання систем лінійних рівнянь у Python<a href="#solve-systems-of-linear-equations-in-python" title="Постійне посилання на цей заголовок"></a></h1>
<p>Хоча ми обговорювали різні методи розв'язання систем лінійних рівнянь, насправді це дуже легко зробити в Python. У цьому розділі ми використаємо Python для розв'язання систем рівнянь. Найпростіший спосіб отримати розв'язок — за допомогою функції <em>solve</em> у Numpy.</p>
<p><strong>СПРОБУЙТЕ!</strong> Використайте numpy.linalg.solve для розв'язання наступних рівнянь.</p>

\[\begin{eqnarray*}
4x_1 + 3x_2 - 5x_3 &amp;=&amp; 2 \\
-2x_1 - 4x_2 + 5x_3 &amp;=&amp; 5 \\
8x_1 + 8x_2  &amp;=&amp; -3 \\
\end{eqnarray*}\]


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>

<span>A</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>4</span><span>,</span> <span>3</span><span>,</span> <span>-</span><span>5</span><span>],</span> 
              <span>[</span><span>-</span><span>2</span><span>,</span> <span>-</span><span>4</span><span>,</span> <span>5</span><span>],</span> 
              <span>[</span><span>8</span><span>,</span> <span>8</span><span>,</span> <span>0</span><span>]])</span>
<span>y</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([</span><span>2</span><span>,</span> <span>5</span><span>,</span> <span>-</span><span>3</span><span>])</span>

<span>x</span> <span>=</span> <span>np</span><span>.</span><span>linalg</span><span>.</span><span>solve</span><span>(</span><span>A</span><span>,</span> <span>y</span><span>)</span>
<span>print</span><span>(</span><span>x</span><span>)</span>
</pre>



<pre><span></span>[ 2.20833333 -2.58333333 -0.18333333]
</pre>



<p>Ми бачимо, що отримуємо ті ж результати, що й у попередньому розділі, коли розраховували вручну. Під капотом, розв'язувач насправді виконує LU-розклад для отримання результатів. Ви можете перевірити довідку функції; вона вимагає, щоб вхідна матриця була квадратною та повного рангу, тобто всі рядки (або, еквівалентно, стовпці) повинні бути лінійно незалежними.</p>
<p><strong>СПРОБУЙТЕ!</strong> Спробуйте розв'язати вищезазначені рівняння за допомогою підходу обернення матриці.</p>


<pre><span></span><span>A_inv</span> <span>=</span> <span>np</span><span>.</span><span>linalg</span><span>.</span><span>inv</span><span>(</span><span>A</span><span>)</span>

<span>x</span> <span>=</span> <span>np</span><span>.</span><span>dot</span><span>(</span><span>A_inv</span><span>,</span> <span>y</span><span>)</span>
<span>print</span><span>(</span><span>x</span><span>)</span>
</pre>



<pre><span></span>[ 2.20833333 -2.58333333 -0.18333333]
</pre>



<p>Ми також можемо отримати матриці <span>\(L\)</span> та <span>\(U\)</span>, що використовуються в LU-розкладі, за допомогою пакета scipy.</p>
<p><strong>СПРОБУЙТЕ!</strong> Отримайте <span>\(L\)</span> та <span>\(U\)</span> для вищезазначеної матриці A.</p>


<pre><span></span><span>from</span> <span>scipy.linalg</span> <span>import</span> <span>lu</span>

<span>P</span><span>,</span> <span>L</span><span>,</span> <span>U</span> <span>=</span> <span>lu</span><span>(</span><span>A</span><span>)</span>
<span>print</span><span>(</span><span>'P:</span><span>\n</span><span>'</span><span>,</span> <span>P</span><span>)</span>
<span>print</span><span>(</span><span>'L:</span><span>\n</span><span>'</span><span>,</span> <span>L</span><span>)</span>
<span>print</span><span>(</span><span>'U:</span><span>\n</span><span>'</span><span>,</span> <span>U</span><span>)</span>
<span>print</span><span>(</span><span>'LU:</span><span>\n</span><span>'</span><span>,</span><span>np</span><span>.</span><span>dot</span><span>(</span><span>L</span><span>,</span> <span>U</span><span>))</span>
</pre>



<pre><span></span>P:
 [[0. 0. 1.]
 [0. 1. 0.]
 [1. 0. 0.]]
L:
 [[ 1.    0.    0.  ]
 [-0.25  1.    0.  ]
 [ 0.5   0.5   1.  ]]
U:
 [[ 8.   8.   0. ]
 [ 0.  -2.   5. ]
 [ 0.   0.  -7.5]]
LU:
 [[ 8.  8.  0.]
 [-2. -4.  5.]
 [ 4.  3. -5.]]
</pre>



<p>Ми бачимо, що отримані нами <span>\(L\)</span> та <span>\(U\)</span> відрізняються від тих, що ми отримали вручну в попередньому розділі. Ви також побачите, що функція <em>lu</em> повертає <strong>матрицю перестановки</strong> <span>\(P\)</span>. Ця матриця перестановки фіксує, як ми змінюємо порядок рівнянь для спрощення обчислень (наприклад, якщо перший елемент у першому рядку дорівнює нулю, він не може бути опорним рівнянням, оскільки ви не можете перетворити перші елементи в інших рядках на нуль. Тому нам потрібно змінити порядок рівнянь, щоб отримати нове опорне рівняння). Якщо ви помножите <span>\(P\)</span> на <span>\(A\)</span>, ви побачите, що ця матриця перестановки змінює порядок рівнянь для цього випадку.</p>
<p><strong>СПРОБУЙТЕ!</strong> Помножте <span>\(P\)</span> на <span>\(A\)</span> і подивіться, який ефект має матриця перестановки на <span>\(A\)</span>.</p>


<pre><span></span><span>print</span><span>(</span><span>np</span><span>.</span><span>dot</span><span>(</span><span>P</span><span>,</span> <span>A</span><span>))</span>
</pre>



<pre><span></span>[[ 8.  8.  0.]
 [-2. -4.  5.]
 [ 4.  3. -5.]]
</pre>
