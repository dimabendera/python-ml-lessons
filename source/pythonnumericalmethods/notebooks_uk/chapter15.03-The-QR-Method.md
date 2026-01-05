<h1>QR-метод<a href="#the-qr-method" title="Постійне посилання на цей заголовок"></a></h1>
<p>QR-метод є поширеним ітераційним методом для знаходження всіх власних значень матриці (але не власних векторів одночасно). Ідея базується на наступних двох концепціях</p>
<ol>
<li><p>подібні матриці матимуть однакові власні значення та відповідні власні вектори. Дві квадратні матриці <span>\(A\)</span> та <span>\(B\)</span> є подібними, якщо:</p></li>
</ol>

\[A = C^{-1}BC\]
<p>де <span>\(C\)</span> — оборотна матриця.</p>
<ol>
<li><p>QR-метод — це спосіб розкладання матриці на дві матриці <span>\(Q\)</span> та <span>\(R\)</span>, де <span>\(Q\)</span> — ортогональна матриця, а <span>\(R\)</span> — верхня трикутна матриця. Ортогональна матриця має властивості: <span>\(Q^{-1} = Q^T\)</span>, що означає <span>\(Q^{-1}Q=Q^TQ=I\)</span>.</p></li>
</ol>
<p>Як ми пов'язуємо ці дві концепції для знаходження власних значень? Припустимо, у нас є матриця <span>\(A_0\)</span>, власні значення якої потрібно визначити. На <span>\(k\)</span>-му кроці (починаючи з <span>\(k = 0\)</span>), ми можемо виконати QR-розклад і отримати <span>\(A_k = Q_kR_k\)</span>, де <span>\(Q_k\)</span> — ортогональна матриця, а <span>\(R_k\)</span> — верхня трикутна матриця. Потім ми формуємо <span>\(A_{k+1} = R_kQ_k\)</span>, і зауважимо, що</p>

\[A_{k+1} = R_kQ_k = Q^{-1}_kQ_kR_kQ_k = Q^{-1}_kA_kQ_k\]
<p>отже, всі <span>\(A_k\)</span> є подібними, і, як ми обговорювали вище, всі вони мають однакові власні значення.</p>
<p>З кожною ітерацією ми врешті-решт збігаємося до верхньої трикутної матричної форми:</p>

\[\begin{split} A_k = R_kQ_k = \begin{bmatrix}
\lambda_1 &amp; X &amp; \dots &amp; X\\
0 &amp; \lambda_2 &amp; \dots &amp; X\\
&amp; &amp;\dots &amp;\\
0 &amp; 0 &amp; \dots &amp; \lambda_n\\
\end{bmatrix}\end{split}\]
<p>де діагональні значення є власними значеннями матриці. У кожній ітерації QR-методу розкладання матриці на ортогональну та верхню трикутну матриці можна виконати за допомогою спеціальної матриці, що називається <strong>матрицею Хаусхолдера</strong>. Ми не будемо заглиблюватися в математичні деталі того, як отримати <span>\(Q\)</span> та <span>\(R\)</span> з матриці, натомість ми використаємо функцію Python для безпосереднього отримання цих двох матриць.</p>
<p><strong>СПРОБУЙТЕ!</strong> Використайте функцію <em>qr</em> з numpy.linalg для розкладання матриці <span>\(A = \begin{bmatrix}
0 &amp; 2\\
2 &amp; 3\\
\end{bmatrix}\)</span>. І перевірте результати.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
<span>from</span> <span>numpy.linalg</span> <span>import</span> <span>qr</span>
</pre>





<pre><span></span><span>a</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>0</span><span>,</span> <span>2</span><span>],</span>
              <span>[</span><span>2</span><span>,</span> <span>3</span><span>]])</span>

<span>q</span><span>,</span> <span>r</span> <span>=</span> <span>qr</span><span>(</span><span>a</span><span>)</span>

<span>print</span><span>(</span><span>'Q:'</span><span>,</span> <span>q</span><span>)</span>
<span>print</span><span>(</span><span>'R:'</span><span>,</span> <span>r</span><span>)</span>

<span>b</span> <span>=</span> <span>np</span><span>.</span><span>dot</span><span>(</span><span>q</span><span>,</span> <span>r</span><span>)</span>
<span>print</span><span>(</span><span>'QR:'</span><span>,</span> <span>b</span><span>)</span>
</pre>



<pre><span></span>Q: [[ 0. -1.]
 [-1.  0.]]
R: [[-2. -3.]
 [ 0. -2.]]
QR: [[0. 2.]
 [2. 3.]]
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Використайте QR-метод, щоб отримати власні значення матриці <span>\(A = \begin{bmatrix}
0 &amp; 2\\
2 &amp; 3\\
\end{bmatrix}\)</span>. Виконайте 20 ітерацій і виведіть результати 1-ї, 5-ї, 10-ї та 20-ї ітерацій.</p>


<pre><span></span><span>a</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>0</span><span>,</span> <span>2</span><span>],</span>
              <span>[</span><span>2</span><span>,</span> <span>3</span><span>]])</span>
<span>p</span> <span>=</span> <span>[</span><span>1</span><span>,</span> <span>5</span><span>,</span> <span>10</span><span>,</span> <span>20</span><span>]</span>
<span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>20</span><span>):</span>
    <span>q</span><span>,</span> <span>r</span> <span>=</span> <span>qr</span><span>(</span><span>a</span><span>)</span>
    <span>a</span> <span>=</span> <span>np</span><span>.</span><span>dot</span><span>(</span><span>r</span><span>,</span> <span>q</span><span>)</span>
    <span>if</span> <span>i</span><span>+</span><span>1</span> <span>in</span> <span>p</span><span>:</span>
        <span>print</span><span>(</span><span>f</span><span>'Ітерація </span><span>{</span><span>i</span><span>+</span><span>1</span><span>}</span><span>:'</span><span>)</span>
        <span>print</span><span>(</span><span>a</span><span>)</span>
</pre>



<pre><span></span>Ітерація 1:
[[3. 2.]
 [2. 0.]]
Ітерація 5:
[[ 3.99998093  0.00976559]
 [ 0.00976559 -0.99998093]]
Ітерація 10:
[[ 4.00000000e+00  9.53674316e-06]
 [ 9.53674316e-06 -1.00000000e+00]]
Ітерація 20:
[[ 4.00000000e+00  9.09484250e-12]
 [ 9.09494702e-12 -1.00000000e+00]]
</pre>



<p>Ми бачимо, що після 5-ї ітерації власні значення збігаються до правильних.</p>
<p>У наступному розділі ми розглянемо, як легко отримати власні значення та власні вектори в Python за допомогою вбудованої функції.</p>
