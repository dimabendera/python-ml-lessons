<h1>Власні значення та власні вектори в Python<a href="#eigenvalues-and-eigenvectors-in-python" title="Постійне посилання на цей заголовок"></a></h1>
<p>Хоча методи, які ми розглянули досі, виглядають складними, фактичний розрахунок власних значень та власних векторів у Python досить простий. Основною вбудованою функцією в Python для розв'язання задачі власних значень/власних векторів для квадратної матриці є функція <em>eig</em> у модулі numpy.linalg. Давайте подивимося, як ми можемо її використовувати.</p>
<p><strong>СПРОБУЙТЕ</strong> Обчисліть власні значення та власні вектори для матриці <span>\(A = \begin{bmatrix}
0 &amp; 2\\
2 &amp; 3\\
\end{bmatrix}\)</span>.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
<span>from</span> <span>numpy.linalg</span> <span>import</span> <span>eig</span>
</pre>





<pre><span></span><span>a</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>0</span><span>,</span> <span>2</span><span>],</span>
              <span>[</span><span>2</span><span>,</span> <span>3</span><span>]])</span>
<span>w</span><span>,</span><span>v</span><span>=</span><span>eig</span><span>(</span><span>a</span><span>)</span>
<span>print</span><span>(</span><span>'Власні значення:'</span><span>,</span> <span>w</span><span>)</span>
<span>print</span><span>(</span><span>'Власні вектори'</span><span>,</span> <span>v</span><span>)</span>
</pre>



<pre><span></span>Власні значення: [-1.  4.]
Власні вектори [[-0.89442719 -0.4472136 ]
 [ 0.4472136  -0.89442719]]
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Обчисліть власні значення та власні вектори для матриці <span>\(A = \begin{bmatrix}
2 &amp; 2 &amp; 4\\
1 &amp; 3 &amp; 5\\
2 &amp; 3 &amp; 4\\
\end{bmatrix}\)</span>.</p>


<pre><span></span><span>a</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>2</span><span>,</span> <span>2</span><span>,</span> <span>4</span><span>],</span>
              <span>[</span><span>1</span><span>,</span> <span>3</span><span>,</span> <span>5</span><span>],</span>
              <span>[</span><span>2</span><span>,</span> <span>3</span><span>,</span> <span>4</span><span>]])</span>
<span>w</span><span>,</span><span>v</span><span>=</span><span>eig</span><span>(</span><span>a</span><span>)</span>
<span>print</span><span>(</span><span>'Власні значення:'</span><span>,</span> <span>w</span><span>)</span>
<span>print</span><span>(</span><span>'Власні вектори'</span><span>,</span> <span>v</span><span>)</span>
</pre>



<pre><span></span>Власні значення: [ 8.80916362  0.92620912 -0.73537273]
Власні вектори [[-0.52799324 -0.77557092 -0.36272811]
 [-0.604391    0.62277013 -0.7103262 ]
 [-0.59660259 -0.10318482  0.60321224]]
</pre>
