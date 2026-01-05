<h1>Степеневий метод<a href="#the-power-method" title="Постійне посилання на цей заголовок"></a></h1>

<h2>Знаходження найбільшого власного значення<a href="#find-the-largest-eigenvalue" title="Постійне посилання на цей заголовок"></a></h2>
<p>У деяких задачах нам потрібно знайти лише найбільше домінуюче власне значення та відповідний йому власний вектор. У цьому випадку ми можемо використовувати степеневий метод — ітераційний метод, який збігатиметься до найбільшого власного значення. Розглянемо, як працює степеневий метод.</p>
<p>Розглянемо <span>\(n\times{n}\)</span> матрицю <span>\(A\)</span>, яка має <span>\(n\)</span> лінійно незалежних дійсних власних значень <span>\(\lambda_1, \lambda_2, \dots, \lambda_n\)</span> та відповідні власні вектори <span>\(v_1, v_2, \dots, v_n\)</span>. Оскільки власні значення є скалярами, ми можемо впорядкувати їх так, що <span>\(|\lambda_1| &gt; |\lambda_2| &gt; \dots &gt; |\lambda_n| \)</span> (насправді, нам потрібно лише <span>\(|\lambda_1| &gt; |\lambda_2|\)</span>, інші власні значення можуть бути рівними).</p>
<p>Оскільки власні вектори є незалежними, вони утворюють базис, що означає, що будь-який вектор у тому ж просторі може бути записаний як лінійна комбінація базисних векторів. Тобто, для будь-якого вектора <span>\(x_0\)</span> його можна записати як:</p>

\[ x_0 = c_1v_1+c_2v_2+\dots+c_nv_n\]
<p>де <span>\(c_1\ne0\)</span> є обмеженням. Якщо воно дорівнює нулю, то нам потрібно вибрати інший початковий вектор так, щоб <span>\(c_1\ne0\)</span>.</p>
<p>Тепер помножимо обидві сторони на <span>\(A\)</span>:</p>

\[ Ax_0 = c_1Av_1+c_2Av_2+\dots+c_nAv_n\]
<p>Оскільки <span>\(Av_i = \lambda{v_i}\)</span>, ми отримаємо:</p>

\[ Ax_0 = c_1\lambda_1v_1+c_2\lambda_2v_2+\dots+c_n\lambda_nv_n\]
<p>Ми можемо змінити вищезазначене рівняння на:</p>

\[ Ax_0 = c_1\lambda_1[v_1+\frac{c_2}{c_1}\frac{\lambda_2}{\lambda_1}v_2+\dots+\frac{c_n}{c_1}\frac{\lambda_n}{\lambda_1}v_n]= c_1\lambda_1x_1\]
<p>де <span>\(x_1\)</span> — новий вектор, і <span>\(x_1 = v_1+\frac{c_2}{c_1}\frac{\lambda_2}{\lambda_1}v_2+\dots+\frac{c_n}{c_1}\frac{\lambda_n}{\lambda_1}v_n\)</span>.</p>
<p>Це завершує першу ітерацію. І ми можемо помножити <span>\(A\)</span> на <span>\(x_1\)</span>, щоб розпочати 2-гу ітерацію:</p>

\[ Ax_1 = \lambda_1{v_1}+\frac{c_2}{c_1}\frac{\lambda_2^2}{\lambda_1}v_2+\dots+\frac{c_n}{c_1}\frac{\lambda_n^2}{\lambda_1}v_n \]
<p>Аналогічно, ми можемо перегрупувати вищезазначене рівняння на:</p>

\[ Ax_1 = \lambda_1[v_1+\frac{c_2}{c_1}\frac{\lambda_2^2}{\lambda_1^2}v_2+\dots+\frac{c_n}{c_1}\frac{\lambda_n^2}{\lambda_1^2}v_n] = \lambda_1x_2\]
<p>де <span>\(x_2\)</span> — ще один новий вектор, і <span>\(x_2 = v_1+\frac{c_2}{c_1}\frac{\lambda_2^2}{\lambda_1^2}v_2+\dots+\frac{c_n}{c_1}\frac{\lambda_n^2}{\lambda_1^2}v_n\)</span>.</p>
<p>Ми можемо продовжувати множити <span>\(A\)</span> на новий вектор, який ми отримуємо з кожної ітерації <span>\(k\)</span> разів:</p>

\[ Ax_{k-1} = \lambda_1[v_1+\frac{c_2}{c_1}\frac{\lambda_2^k}{\lambda_1^k}v_2+\dots+\frac{c_n}{c_1}\frac{\lambda_n^k}{\lambda_1^k}v_n] = \lambda_1x_k\]
<p>Оскільки <span>\(\lambda_1\)</span> є найбільшим власним значенням, співвідношення <span>\(\frac{\lambda_i}{\lambda_1}&lt;1\)</span> для всіх <span>\(i&gt;1\)</span>. Таким чином, коли ми збільшуємо <span>\(k\)</span> до достатньо великого значення, співвідношення <span>\((\frac{\lambda_n}{\lambda_1})^{k}\)</span> буде близьким до 0. Отже, всі члени, що містять це співвідношення, можуть бути знехтувані зі зростанням <span>\(k\)</span>:</p>

\[ Ax_{k-1} = {\lambda_1}v_1 \]
<p>По суті, коли <span>\(k\)</span> є достатньо великим, ми отримаємо найбільше власне значення та відповідний йому власний вектор. При реалізації цього степеневого методу ми зазвичай нормалізуємо отриманий вектор на кожній ітерації. Це можна зробити, винісши за дужки найбільший елемент у векторі, що зробить найбільший елемент у векторі рівним 1. Ця нормалізація дозволить нам одночасно отримати найбільше власне значення та відповідний йому власний вектор. Розглянемо наступний приклад.</p>
<p>Ви можете запитати, коли слід зупиняти ітерацію? Основними критеріями зупинки мають бути один із трьох: у послідовних ітераціях (1) різниця між власними значеннями менша за заданий допуск; (2) кут між власними векторами менший за поріг; або норма залишкового вектора є достатньо малою.</p>
<p><strong>СПРОБУЙТЕ!</strong> З попереднього розділу ми знаємо, що найбільше власне значення для матриці <span>\(A = \begin{bmatrix}
0 &amp; 2\\
2 &amp; 3\\
\end{bmatrix}\)</span> дорівнює 4. Тепер використайте степеневий метод, щоб знайти найбільше власне значення та пов'язаний з ним власний вектор. Ви можете використовувати початковий вектор [1, 1] для початку ітерації.</p>
<p>1-ша ітерація: $$</p>

<span>(7)<a href="#equation-dc529aa0-2d60-43bc-993b-933a519297a4" title="Постійне посилання на це рівняння"></a></span>\[\begin{bmatrix}
0 &amp; 2\\
2 &amp; 3\\
\end{bmatrix}\]

<span>(8)<a href="#equation-583dd37d-602e-44d1-a5e5-f08d43edd6c1" title="Постійне посилання на це рівняння"></a></span>\[\begin{bmatrix}
1\\1\\
\end{bmatrix}\]
<p>=\begin{bmatrix}
2\5\
\end{bmatrix}
=5\begin{bmatrix}
0.4\1\
\end{bmatrix}
$$</p>
<p>2-га ітерація:
$$</p>

<span>(9)<a href="#equation-b9193944-c1b9-4a65-ae40-4e95a2677ac2" title="Постійне посилання на це рівняння"></a></span>\[\begin{bmatrix}
0 &amp; 2\\
2 &amp; 3\\
\end{bmatrix}\]

<span>(10)<a href="#equation-22e16cb0-2cfc-400d-b8cb-c3b6fe5eb648" title="Постійне посилання на це рівняння"></a></span>\[\begin{bmatrix}
0.4\\1\\
\end{bmatrix}\]
<p>=\begin{bmatrix}
2\3.8\
\end{bmatrix}
=3.8\begin{bmatrix}
0.5263\1\
\end{bmatrix}
$$</p>
<p>3-тя ітерація:
$$</p>

<span>(11)<a href="#equation-ccf134ea-9f51-4dba-80b5-49fec70ded9f" title="Постійне посилання на це рівняння"></a></span>\[\begin{bmatrix}
0 &amp; 2\\
2 &amp; 3\\
\end{bmatrix}\]

<span>(12)<a href="#equation-1d6b70bd-03e0-4a5f-93f7-fc47382970e6" title="Постійне посилання на це рівняння"></a></span>\[\begin{bmatrix}
0.5263\\1\\
\end{bmatrix}\]
<p>=\begin{bmatrix}
2\ 4.0526\
\end{bmatrix}
= 4.0526\begin{bmatrix}
0.4935\1\
\end{bmatrix}
$$</p>
<p>4-та ітерація:
$$</p>

<span>(13)<a href="#equation-7678b301-94ac-43d9-8719-707918824810" title="Постійне посилання на це рівняння"></a></span>\[\begin{bmatrix}
0 &amp; 2\\
2 &amp; 3\\
\end{bmatrix}\]

<span>(14)<a href="#equation-216f2d4f-2c6e-4644-b595-bee663ab6d7a" title="Постійне посилання на це рівняння"></a></span>\[\begin{bmatrix}
0.4935\\1\\
\end{bmatrix}\]
<p>=\begin{bmatrix}
2\ 3.987\
\end{bmatrix}
= 3.987\begin{bmatrix}
0.5016\1\
\end{bmatrix}
$$</p>
<p>5-та ітерація:
$$</p>

<span>(15)<a href="#equation-10cb33da-f46a-4554-b0d3-fb919d4ff93a" title="Постійне посилання на це рівняння"></a></span>\[\begin{bmatrix}
0 &amp; 2\\
2 &amp; 3\\
\end{bmatrix}\]

<span>(16)<a href="#equation-5a769ee7-a78e-4362-bd29-33871a0deb7e" title="Постійне посилання на це рівняння"></a></span>\[\begin{bmatrix}
0.5016\\1\\
\end{bmatrix}\]
<p>=\begin{bmatrix}
2\ 4.0032\
\end{bmatrix}
= 4.0032\begin{bmatrix}
0.4996\1\
\end{bmatrix}
$$</p>
<p>6-та ітерація:
$$</p>

<span>(17)<a href="#equation-0da61863-b5d2-4055-9071-8ea8a24bdfcd" title="Постійне посилання на це рівняння"></a></span>\[\begin{bmatrix}
0 &amp; 2\\
2 &amp; 3\\
\end{bmatrix}\]

<span>(18)<a href="#equation-ab6cb2fa-225e-427c-ba67-59dcd0656ded" title="Постійне посилання на це рівняння"></a></span>\[\begin{bmatrix}
0.4996\\1\\
\end{bmatrix}\]
<p>=\begin{bmatrix}
2\ 3.9992\
\end{bmatrix}
= 3.9992\begin{bmatrix}
0.5001\1\
\end{bmatrix}
$$</p>
<p>7-ма ітерація:
$$</p>

<span>(19)<a href="#equation-23dbb265-bf7f-4a00-8adf-a1e713228dee" title="Постійне посилання на це рівняння"></a></span>\[\begin{bmatrix}
0 &amp; 2\\
2 &amp; 3\\
\end{bmatrix}\]

<span>(20)<a href="#equation-415887ea-c410-415d-93ec-e11c760ef87e" title="Постійне посилання на це рівняння"></a></span>\[\begin{bmatrix}
0.5001\\1\\
\end{bmatrix}\]
<p>=\begin{bmatrix}
2\ 4.0002\
\end{bmatrix}
= 4.0002\begin{bmatrix}
0.5000\1\
\end{bmatrix}
$$</p>
<p>Ми бачимо, що після 7 ітерацій власне значення збіглося до 4, а відповідний власний вектор до [0.5, 1].</p>
<p><strong>СПРОБУЙТЕ!</strong> Реалізуйте степеневий метод на Python</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
</pre>





<pre><span></span><span>def</span> <span>normalize</span><span>(</span><span>x</span><span>):</span>
    <span>fac</span> <span>=</span> <span>abs</span><span>(</span><span>x</span><span>)</span><span>.</span><span>max</span><span>()</span>
    <span>x_n</span> <span>=</span> <span>x</span> <span>/</span> <span>x</span><span>.</span><span>max</span><span>()</span>
    <span>return</span> <span>fac</span><span>,</span> <span>x_n</span>
</pre>





<pre><span></span><span>x</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([</span><span>1</span><span>,</span> <span>1</span><span>])</span>
<span>a</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>0</span><span>,</span> <span>2</span><span>],</span> 
              <span>[</span><span>2</span><span>,</span> <span>3</span><span>]])</span>

<span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>8</span><span>):</span>
    <span>x</span> <span>=</span> <span>np</span><span>.</span><span>dot</span><span>(</span><span>a</span><span>,</span> <span>x</span><span>)</span>
    <span>lambda_1</span><span>,</span> <span>x</span> <span>=</span> <span>normalize</span><span>(</span><span>x</span><span>)</span>
    
<span>print</span><span>(</span><span>'Власне значення:'</span><span>,</span> <span>lambda_1</span><span>)</span>
<span>print</span><span>(</span><span>'Власний вектор:'</span><span>,</span> <span>x</span><span>)</span>
</pre>



<pre><span></span>Власне значення: 3.999949137887188
Власний вектор: [0.50000636 1.        ]
</pre>





<h2>Обернений степеневий метод<a href="#the-inverse-power-method" title="Постійне посилання на цей заголовок"></a></h2>
<p>Власні значення оберненої матриці <span>\(A^{-1}\)</span> є оберненими до власних значень <span>\(A\)</span>. Ми можемо скористатися цією властивістю, а також степеневим методом, щоб отримати найменше власне значення <span>\(A\)</span>; це буде основою оберненого степеневого методу. Кроки дуже прості: замість множення на <span>\(A\)</span>, як описано вище, ми просто множимо на <span>\(A^{-1}\)</span> для нашої ітерації, щоб знайти найбільше значення <span>\(\frac{1}{\lambda_1}\)</span>, яке буде найменшим значенням серед власних значень для <span>\(A\)</span>. Що стосується оберненої матриці, на практиці ми можемо використовувати методи, які ми розглядали в попередньому розділі, для її обчислення. Ми не будемо вдаватися в деталі тут, але розглянемо приклад.</p>
<p><strong>СПРОБУЙТЕ!</strong> Знайдіть найменше власне значення та власний вектор для <span>\(A = \begin{bmatrix}
0 &amp; 2\\
2 &amp; 3\\
\end{bmatrix}\)</span>.</p>


<pre><span></span><span>from</span> <span>numpy.linalg</span> <span>import</span> <span>inv</span>
</pre>





<pre><span></span><span>a_inv</span> <span>=</span> <span>inv</span><span>(</span><span>a</span><span>)</span>

<span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>8</span><span>):</span>
    <span>x</span> <span>=</span> <span>np</span><span>.</span><span>dot</span><span>(</span><span>a_inv</span><span>,</span> <span>x</span><span>)</span>
    <span>lambda_1</span><span>,</span> <span>x</span> <span>=</span> <span>normalize</span><span>(</span><span>x</span><span>)</span>
    
<span>print</span><span>(</span><span>'Власне значення:'</span><span>,</span> <span>lambda_1</span><span>)</span>
<span>print</span><span>(</span><span>'Власний вектор:'</span><span>,</span> <span>x</span><span>)</span>
</pre>



<pre><span></span>Власне значення: 0.20000000000003912
Власний вектор: [1. 1.]
</pre>





<h2>Зміщений степеневий метод<a href="#the-shifted-power-method" title="Постійне посилання на цей заголовок"></a></h2>
<p>У деяких випадках нам потрібно знайти всі власні значення та власні вектори, а не лише найбільші та найменші. Один простий, але неефективний спосіб — використовувати зміщений степеневий метод (ми представимо вам ефективний спосіб у наступному розділі). Враховуючи <span>\(Ax = \lambda{x}\)</span>, і <span>\(\lambda_1\)</span> є найбільшим власним значенням, отриманим степеневим методом, тоді ми можемо мати:</p>

\[[A - \lambda_1I]x = \alpha{x}\]
<p>де <span>\(\alpha\)</span> — власні значення зміщеної матриці <span>\(A - \lambda_1I\)</span>, які будуть <span>\(0, \lambda_2-\lambda_1, \lambda_3-\lambda_1, \dots, \lambda_n-\lambda_1\)</span>.</p>
<p>Тепер, якщо ми застосуємо степеневий метод до зміщеної матриці, то зможемо визначити найбільше власне значення зміщеної матриці, тобто <span>\(\alpha_k\)</span>. Оскільки <span>\(\alpha_k = \lambda_k - \lambda_1\)</span>, ми можемо легко отримати власне значення <span>\(\lambda_k\)</span>. Ми можемо повторювати цей процес багато разів, щоб знайти всі інші власні значення. Але ви бачите, що це вимагає багато роботи! Кращий метод для знаходження всіх власних значень — це використання QR-методу, давайте подивимося в наступному розділі, як він працює!</p>
