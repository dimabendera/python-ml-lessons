<h1>Розв'язувачі ОДЄ Python (ЗКЗ)<a href="#python-ode-solvers-bvp" title="Постійне посилання на цей заголовок"></a></h1>
<p>У <em>scipy</em> також є базовий розв'язувач для розв'язання задач з крайовими значеннями, а саме функція <em>scipy.integrate.solve_bvp</em>. Ця функція розв'язує систему ОДЄ першого порядку з двоточковими крайовими умовами. Конструкція функції показана нижче:</p>
<p><strong>КОНСТРУКЦІЯ:</strong></p>
<p>Нехай <span>\(F\)</span> буде об'єктом-функцією, яка обчислює</p>

\[\frac{dy}{dx} = F(t, S(t))\]

\[S(t0)=S0\]
<p><span>\(t\)</span> — це одновимірна незалежна змінна (час), <span>\(S(t)\)</span> — це n-вимірна векторнозначна функція (стан), а <span>\(F(t, S(t))\)</span> визначає диференціальні рівняння. <span>\(S0\)</span> — це початкове значення для <span>\(S\)</span>. Функція <span>\(F\)</span> *повинна* мати вигляд <span>\(dS = F(t, S)\)</span>, хоча назва не обов'язково має бути <span>\(F\)</span>. Мета полягає в тому, щоб знайти <span>\(S(t)\)</span>, що приблизно задовольняє диференціальні рівняння, враховуючи початкове значення <span>\(S(t0)=S0\)</span>.</p>
<p>Спосіб використання розв'язувача для розв'язання диференціального рівняння такий: $<span>\(solve\_ivp(fun, t\_span, s0, method = 'RK45', t\_eval=None)\)</span>$</p>
<p>де <span>\(fun\)</span> приймає функцію з правої частини системи. <span>\(t\_span\)</span> — це інтервал інтегрування <span>\((t0, tf)\)</span>, де <span>\(t0\)</span> — початок, а <span>\(tf\)</span> — кінець інтервалу. <span>\(s0\)</span> — це початковий стан. Є кілька методів, які ми можемо вибрати, за замовчуванням це ‘RK45`, який є явним методом Рунге-Кутти порядку 5(4). Є й інші методи, які ви можете використовувати, дивіться кінець цього розділу для отримання додаткової інформації. <span>\(t\_eval\)</span> приймає часи, в які потрібно зберігати обчислене рішення, і вони повинні бути відсортовані та знаходитися в межах <span>\(t\_span\)</span>.</p>
<p>Спробуймо один приклад нижче.</p>


<pre><span></span><span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>
<span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
<span>from</span> <span>scipy.integrate</span> <span>import</span> <span>solve_bvp</span>

<span>plt</span><span>.</span><span>style</span><span>.</span><span>use</span><span>(</span><span>'seaborn-poster'</span><span>)</span>

<span>%</span><span>matplotlib</span> inline

<span>F</span> <span>=</span> <span>lambda</span> <span>t</span><span>,</span> <span>s</span><span>:</span> <span>np</span><span>.</span><span>cos</span><span>(</span><span>t</span><span>)</span>

<span>t_eval</span> <span>=</span> <span>np</span><span>.</span><span>arange</span><span>(</span><span>0</span><span>,</span> <span>np</span><span>.</span><span>pi</span><span>,</span> <span>0.1</span><span>)</span>
<span>sol</span> <span>=</span> <span>solve_ivp</span><span>(</span><span>F</span><span>,</span> <span>[</span><span>0</span><span>,</span> <span>np</span><span>.</span><span>pi</span><span>],</span> <span>[</span><span>0</span><span>],</span> <span>t_eval</span><span>=</span><span>t_eval</span><span>)</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>12</span><span>,</span> <span>4</span><span>))</span>
<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>121</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>sol</span><span>.</span><span>t</span><span>,</span> <span>sol</span><span>.</span><span>y</span><span>[</span><span>0</span><span>])</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'t'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'S(t)'</span><span>)</span>
<span>plt</span><span>.</span><span>subplot</span><span>(</span><span>122</span><span>)</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>sol</span><span>.</span><span>t</span><span>,</span> <span>sol</span><span>.</span><span>y</span><span>[</span><span>0</span><span>]</span> <span>-</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>sol</span><span>.</span><span>t</span><span>))</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'t'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'S(t) - sin(t)'</span><span>)</span>
<span>plt</span><span>.</span><span>tight_layout</span><span>()</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter23.05-Python-ODE-Solvers_5_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter23.05-Python-ODE-Solvers_5_0.png"/>




<pre><span></span><span>def</span> <span>fun</span><span>(</span><span>t</span><span>,</span> <span>y</span><span>):</span>
    <span>print</span><span>(</span><span>y</span><span>[</span><span>1</span><span>]</span><span>.</span><span>shape</span><span>)</span>
    <span>return</span> <span>np</span><span>.</span><span>vstack</span><span>((</span><span>y</span><span>[</span><span>1</span><span>],</span> <span>-</span><span>9.8</span><span>))</span>

<span>f</span> <span>=</span> <span>lambda</span> <span>t</span><span>,</span> <span>s</span><span>:</span> \
  <span>np</span><span>.</span><span>dot</span><span>(</span><span>np</span><span>.</span><span>array</span><span>([[</span><span>0</span><span>,</span><span>1</span><span>],[</span><span>0</span><span>,</span><span>-</span><span>9.8</span><span>/</span><span>s</span><span>[</span><span>1</span><span>]]]),</span><span>s</span><span>)</span>

<span>def</span> <span>bc</span><span>(</span><span>ya</span><span>,</span> <span>yb</span><span>):</span>
    <span>return</span> <span>np</span><span>.</span><span>array</span><span>([</span><span>ya</span><span>[</span><span>0</span><span>],</span> <span>yb</span><span>[</span><span>0</span><span>]])</span>
</pre>





<pre><span></span><span>t</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>5</span><span>,</span> <span>11</span><span>)</span>

<span>y_a</span> <span>=</span> <span>np</span><span>.</span><span>zeros</span><span>((</span><span>2</span><span>,</span> <span>t</span><span>.</span><span>size</span><span>))</span>
<span>y_a</span><span>[</span><span>-</span><span>1</span><span>]</span><span>=</span> <span>50</span>

<span>res_a</span> <span>=</span> <span>solve_bvp</span><span>(</span><span>f</span><span>,</span> <span>bc</span><span>,</span> <span>t</span><span>,</span> <span>y_a</span><span>)</span>
</pre>



<pre><span></span><span>---------------------------------------------------------------------------</span>
<span>ValueError</span><span>                                </span>Traceback (most recent call last)
<span>&lt;</span><span>ipython</span><span>-</span><span>input</span><span>-</span><span>23</span><span>-</span><span>2946</span><span>ad05c3b2</span><span>&gt;</span> <span>in</span> <span>&lt;</span><span>module</span><span>&gt;</span>
<span>      </span><span>4</span> <span>y_a</span><span>[</span><span>-</span><span>1</span><span>]</span><span>=</span> <span>50</span>
<span>      </span><span>5</span> 
<span>----&gt; </span><span>6</span> <span>res_a</span> <span>=</span> <span>solve_bvp</span><span>(</span><span>f</span><span>,</span> <span>bc</span><span>,</span> <span>t</span><span>,</span> <span>y_a</span><span>)</span>

<span>~/miniconda3/lib/python3.6/site-packages/scipy/integrate/_bvp.py</span> in <span>solve_bvp</span><span>(fun, bc, x, y, p, S, fun_jac, bc_jac, tol, max_nodes, verbose)</span>
<span>   </span><span>1053</span>         <span>fun</span><span>,</span> <span>bc</span><span>,</span> <span>fun_jac</span><span>,</span> <span>bc_jac</span><span>,</span> <span>k</span><span>,</span> <span>a</span><span>,</span> <span>S</span><span>,</span> <span>D</span><span>,</span> <span>dtype</span><span>)</span>
<span>   </span><span>1054</span> 
<span>-&gt; </span><span>1055</span>     <span>f</span> <span>=</span> <span>fun_wrapped</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>p</span><span>)</span>
<span>   </span><span>1056</span>     <span>if</span> <span>f</span><span>.</span><span>shape</span> <span>!=</span> <span>y</span><span>.</span><span>shape</span><span>:</span>
<span>   </span><span>1057</span>         <span>raise</span> <span>ValueError</span><span>(</span><span>"`fun` return is expected to have shape </span><span>{}</span><span>, "</span>

<span>~/miniconda3/lib/python3.6/site-packages/scipy/integrate/_bvp.py</span> in <span>fun_p</span><span>(x, y, _)</span>
<span>    </span><span>649</span>     <span>if</span> <span>k</span> <span>==</span> <span>0</span><span>:</span>
<span>    </span><span>650</span>         <span>def</span> <span>fun_p</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>_</span><span>):</span>
<span>--&gt; </span><span>651</span>             <span>return</span> <span>np</span><span>.</span><span>asarray</span><span>(</span><span>fun</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>),</span> <span>dtype</span><span>)</span>
<span>    </span><span>652</span> 
<span>    </span><span>653</span>         <span>def</span> <span>bc_wrapped</span><span>(</span><span>ya</span><span>,</span> <span>yb</span><span>,</span> <span>_</span><span>):</span>

<span>~/miniconda3/lib/python3.6/site-packages/numpy/core/numeric.py</span> in <span>asarray</span><span>(a, dtype, order)</span>
<span>    </span><span>536</span> 
<span>    </span><span>537</span>     <span>"""</span>
<span>--&gt; </span><span>538</span><span>     return array(a, dtype, copy=False, order=order)</span>
<span>    </span><span>539</span><span> </span>
<span>    </span><span>540</span><span> </span>

<span>ValueError</span>: setting an array element with a sequence.
</pre>





<pre><span></span><span>def</span> <span>fun</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>):</span>
    <span>return</span> <span>np</span><span>.</span><span>vstack</span><span>((</span><span>y</span><span>[</span><span>1</span><span>],</span> <span>-</span><span>np</span><span>.</span><span>exp</span><span>(</span><span>y</span><span>[</span><span>0</span><span>])))</span>

<span>def</span> <span>bc</span><span>(</span><span>ya</span><span>,</span> <span>yb</span><span>):</span>
    <span>return</span> <span>np</span><span>.</span><span>array</span><span>([</span><span>ya</span><span>[</span><span>0</span><span>],</span> <span>yb</span><span>[</span><span>0</span><span>]])</span>

<span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>0</span><span>,</span> <span>1</span><span>,</span> <span>5</span><span>)</span>

<span>y_a</span> <span>=</span> <span>np</span><span>.</span><span>zeros</span><span>((</span><span>2</span><span>,</span> <span>x</span><span>.</span><span>size</span><span>))</span>
<span>y_b</span> <span>=</span> <span>np</span><span>.</span><span>zeros</span><span>((</span><span>2</span><span>,</span> <span>x</span><span>.</span><span>size</span><span>))</span>
<span>#y_b[0] = 3</span>
</pre>





<pre><span></span><span>res_a</span> <span>=</span> <span>solve_bvp</span><span>(</span><span>fun</span><span>,</span> <span>bc</span><span>,</span> <span>x</span><span>,</span> <span>y_a</span><span>)</span>
</pre>



<pre><span></span>/Users/qingkaikong/miniconda3/lib/python3.6/site-packages/ipykernel_launcher.py:6: RuntimeWarning: divide by zero encountered in true_divide
  
/Users/qingkaikong/miniconda3/lib/python3.6/site-packages/ipykernel_launcher.py:6: RuntimeWarning: invalid value encountered in multiply
  
</pre>

<pre><span></span><span>---------------------------------------------------------------------------</span>
<span>ValueError</span><span>                                </span>Traceback (most recent call last)
<span>&lt;</span><span>ipython</span><span>-</span><span>input</span><span>-</span><span>27</span><span>-</span><span>845</span><span>fe81f85d9</span><span>&gt;</span> <span>in</span> <span>&lt;</span><span>module</span><span>&gt;</span>
<span>----&gt; </span><span>1</span> <span>res_a</span> <span>=</span> <span>solve_bvp</span><span>(</span><span>F</span><span>,</span> <span>bc</span><span>,</span> <span>x</span><span>,</span> <span>y_a</span><span>)</span>

<span>~/miniconda3/lib/python3.6/site-packages/scipy/integrate/_bvp.py</span> in <span>solve_bvp</span><span>(fun, bc, x, y, p, S, fun_jac, bc_jac, tol, max_nodes, verbose)</span>
<span>   </span><span>1053</span>         <span>fun</span><span>,</span> <span>bc</span><span>,</span> <span>fun_jac</span><span>,</span> <span>bc_jac</span><span>,</span> <span>k</span><span>,</span> <span>a</span><span>,</span> <span>S</span><span>,</span> <span>D</span><span>,</span> <span>dtype</span><span>)</span>
<span>   </span><span>1054</span> 
<span>-&gt; </span><span>1055</span>     <span>f</span> <span>=</span> <span>fun_wrapped</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>p</span><span>)</span>
<span>   </span><span>1056</span>     <span>if</span> <span>f</span><span>.</span><span>shape</span> <span>!=</span> <span>y</span><span>.</span><span>shape</span><span>:</span>
<span>   </span><span>1057</span>         <span>raise</span> <span>ValueError</span><span>(</span><span>"`fun` return is expected to have shape </span><span>{}</span><span>, "</span>

<span>~/miniconda3/lib/python3.6/site-packages/scipy/integrate/_bvp.py</span> in <span>fun_p</span><span>(x, y, _)</span>
<span>    </span><span>649</span>     <span>if</span> <span>k</span> <span>==</span> <span>0</span><span>:</span>
<span>    </span><span>650</span>         <span>def</span> <span>fun_p</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>,</span> <span>_</span><span>):</span>
<span>--&gt; </span><span>651</span>             <span>return</span> <span>np</span><span>.</span><span>asarray</span><span>(</span><span>fun</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>),</span> <span>dtype</span><span>)</span>
<span>    </span><span>652</span> 
<span>    </span><span>653</span>         <span>def</span> <span>bc_wrapped</span><span>(</span><span>ya</span><span>,</span> <span>yb</span><span>,</span> <span>_</span><span>):</span>

<span>~/miniconda3/lib/python3.6/site-packages/numpy/core/numeric.py</span> in <span>asarray</span><span>(a, dtype, order)</span>
<span>    </span><span>536</span> 
<span>    </span><span>537</span>     <span>"""</span>
<span>--&gt; </span><span>538</span><span>     return array(a, dtype, copy=False, order=order)</span>
<span>    </span><span>539</span><span> </span>
<span>    </span><span>540</span><span> </span>

<span>ValueError</span>: setting an array element with a sequence.
</pre>





<pre><span></span><span>res_b</span> <span>=</span> <span>solve_bvp</span><span>(</span><span>fun</span><span>,</span> <span>bc</span><span>,</span> <span>x</span><span>,</span> <span>y_a</span><span>)</span>
</pre>





<pre><span></span>       message: 'The algorithm converged to the desired accuracy.'
         niter: 1
             p: None
 rms_residuals: array([9.86500717e-05, 1.05360602e-04, 1.05360602e-04, 9.86500717e-05])
           sol: &lt;scipy.interpolate.interpolate.PPoly object at 0x1832058938&gt;
        status: 0
       success: True
             x: array([0.  , 0.25, 0.5 , 0.75, 1.  ])
             y: array([[ 0.00000000e+00,  1.04784145e-01,  1.40534773e-01,
         1.04784145e-01,  0.00000000e+00],
       [ 5.49349275e-01,  2.84320977e-01, -1.28752555e-18,
        -2.84320977e-01, -5.49349275e-01]])
            yp: array([[ 5.49349275e-01,  2.84320977e-01, -1.28752555e-18,
        -2.84320977e-01, -5.49349275e-01],
       [-1.00000000e+00, -1.11047088e-00, -1.15088910e-00,
        -1.11047088e-00, -1.00000000e+00]])
</pre>



<p>Наведена вище фігура показує відповідні числові результати. Як і в попередньому прикладі, різниця між результатом <em>solve_ivp</em> та оцінкою аналітичного розв'язку за допомогою Python дуже мала порівняно зі значенням функції.</p>
<p><strong>ПРИКЛАД:</strong></p>
<p>Нехай стан системи визначається як <span>\(S(t) = \left[\begin{array}{c} x(t) \\y(t) \end{array}\right]\)</span>, а еволюція системи визначається ОДЄ</p>

\[\begin{split}
\frac{dS(t)}{dt} = \left[\begin{array}{cc}
0 &amp; t^2 \\
-t &amp; 0
\end{array}\right]S(t).
\end{split}\]
<p>Використайте <em>solve_ivp</em> для розв'язання цього ОДЄ для часового інтервалу <span>\([0, 10]\)</span> з початковим значенням <span>\(S_0 = \left[\begin{array}{c} 1 \\1 \end{array}\right]\)</span>. Побудуйте розв'язок у (<span>\(x(t), y(t)\)</span>).</p>


<pre><span></span><span>F</span> <span>=</span> <span>lambda</span> <span>t</span><span>,</span> <span>s</span><span>:</span> <span>np</span><span>.</span><span>dot</span><span>(</span><span>np</span><span>.</span><span>array</span><span>([[</span><span>0</span><span>,</span> <span>t</span><span>**</span><span>2</span><span>],</span> <span>[</span><span>-</span><span>t</span><span>,</span> <span>0</span><span>]]),</span> <span>s</span><span>)</span>

<span>t_eval</span> <span>=</span> <span>np</span><span>.</span><span>arange</span><span>(</span><span>0</span><span>,</span> <span>10.01</span><span>,</span> <span>0.01</span><span>)</span>
<span>sol</span> <span>=</span> <span>solve_ivp</span><span>(</span><span>F</span><span>,</span> <span>[</span><span>0</span><span>,</span> <span>10</span><span>],</span> <span>[</span><span>1</span><span>,</span> <span>1</span><span>],</span> <span>t_eval</span><span>=</span><span>t_eval</span><span>)</span>

<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>12</span><span>,</span> <span>8</span><span>))</span>
<span>plt</span><span>.</span><span>plot</span><span>(</span><span>sol</span><span>.</span><span>y</span><span>.</span><span>T</span><span>[:,</span> <span>0</span><span>],</span> <span>sol</span><span>.</span><span>y</span><span>.</span><span>T</span><span>[:,</span> <span>1</span><span>])</span>
<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'x'</span><span>)</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'y'</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter23.05-Python-ODE-Solvers_13_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter23.05-Python-ODE-Solvers_13_0.png"/>


<p>На практиці деякі ОДЄ мають погану поведінку, відому як **жорсткість**. У широкому сенсі, жорсткість стосується систем, які можуть мати дуже різкі зміни похідної. Прикладом жорсткої системи є м'яч, що відскакує, який раптово змінює напрямок, коли вдаряється об землю. Залежно від властивостей ОДЄ, яку ви розв'язуєте, та бажаного рівня точності, вам може знадобитися використовувати різні методи для *solve_ivp*. Існує багато методів, які ви можете вибрати для аргументу *method* у *solve_ivp*, перегляньте <a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html#scipy.integrate.solve_ivp">документацію</a>, щоб дізнатися більше. Як пропонує документація, слід використовувати метод ‘RK45` або ‘RK23` для нежорстких задач та ‘Radau` або ‘BDF` для жорстких задач. Якщо ви не впевнені, спочатку спробуйте запустити ‘RK45`. Якщо потрібно надзвичайно багато ітерацій, розходиться або не вдається, ваша задача, ймовірно, є жорсткою, і вам слід використовувати ‘Radau` або ‘BDF`. ‘LSODA` також може бути хорошим універсальним вибором, але з ним може бути дещо менш зручно працювати, оскільки він обгортає старий код Fortran.</p>
