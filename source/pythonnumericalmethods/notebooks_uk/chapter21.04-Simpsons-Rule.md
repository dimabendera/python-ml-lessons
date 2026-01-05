<h1>Правило Сімпсона<a href="#simpson-s-rule" title="Постійне посилання на цей заголовок"></a></h1>
<p>Розглянемо <em>два</em> послідовні підінтервали, <span>\([x_{i-1}, x_i]\)</span> та <span>\([x_i, x_{i+1}]\)</span>. <strong>Правило Сімпсона</strong> апроксимує площу під <span>\(f(x)\)</span> на цих двох підінтервалах шляхом побудови квадратичного полінома через точки <span>\((x_{i-1}, f(x_{i-1})), (x_i, f(x_i))\)</span> та <span>\((x_{i+1}, f(x_{i+1}))\)</span>, що є унікальним поліномом, а потім точного інтегрування цього квадратичного полінома. Нижче показано цю інтегральну апроксимацію для довільної функції.</p>

<p>Спочатку ми будуємо квадратичну поліноміальну апроксимацію функції на двох підінтервалах. Найпростіший спосіб зробити це — використати поліноми Лагранжа, які обговорювалися в Розділі 17. Застосовуючи формулу для побудови поліномів Лагранжа, ми отримуємо поліном</p>

\[\begin{eqnarray*}P_i(x) &amp;=&amp; f(x_{i-1})\frac{(x - x_i)(x - x_{i+1})}{(x_{i-1} - x_i)(x_{i-1} - x_{i+1})} + f(x_i)\frac{(x - x_{i-1})(x - x_{i+1})}{(x_{i} - x_{i-1})(x_{i} - x_{i+1})}\\
&amp;&amp;+ f(x_{i+1})\frac{(x - x_{i-1})(x - x_{i})}{(x_{i+1} - x_{i-1})(x_{i+1} -
x_{i})},\end{eqnarray*}\]
<p>і з підстановками для <span>\(h\)</span> отримуємо</p>

\[P_i(x) = \frac{f(x_{i-1})}{2h^2} (x - x_i)(x - x_{i+1}) - \frac{f(x_i)}{h^2} (x - x_{i-1})(x - x_{i+1}) + \frac{f(x_{i+1})}{2h^2} (x - x_{i-1})(x - x_{i}).\]
<p>Ви можете переконатися, що поліном перетинає бажані точки. За допомогою деяких алгебраїчних перетворень та маніпуляцій, інтеграл <span>\(P_i(x)\)</span> на двох підінтервалах дорівнює</p>

\[\int_{x_{i-1}}^{x_{i+1}} P_i(x) dx = \frac{h}{3}(f(x_{i-1}) + 4f(x_i) + f(x_{i+1}).\]
<p>Щоб апроксимувати інтеграл на <span>\((a, b)\)</span>, ми повинні просумувати інтеграли <span>\(P_i(x)\)</span> над кожними <em>двома</em> підінтервалами, оскільки <span>\(P_i(x)\)</span> охоплює два підінтервали. Підставляючи <span>\(\frac{h}{3}(f(x_{i-1}) + 4f(x_i) + f(x_{i+1}))\)</span> для інтеграла <span>\(P_i(x)\)</span> і перегруповуючи члени для ефективності, отримуємо формулу</p>

\[\int_a^b f(x) dx \approx \frac{h}{3} \left[f(x_0)+4 \left(\sum_{i=1, i\  {\text{odd}}}^{n-1}f(x_i)\right)+2 \left(\sum_{i=2, i\  {\text{even}}}^{n-2}f(x_i)\right)+f(x_n)\right].\]
<p>Це перегрупування проілюстровано на малюнку нижче:</p>

<p><strong>УВАГА!</strong> Зауважте, що для використання Правила Сімпсона ви <strong>повинні</strong> мати парну кількість інтервалів і, отже, непарну кількість вузлових точок.</p>
<p>Щоб обчислити точність Правила Сімпсона, ми беремо наближення ряду Тейлора для <span>\(f(x)\)</span> навколо <span>\(x_i\)</span>, яке є</p>

\[f(x) = f(x_i) + f^{\prime}(x_i)(x - x_i) + \frac{f''(x_i)(x-x_i)^2}{2!} + \frac{f'''(x_i)(x-x_i)^3}{3!} + \frac{f''''(x_i)(x-x_i)^4}{4!} + \cdots\]
<p>Обчислюючи ряд Тейлора в <span>\(x_{i-1}\)</span> та <span>\(x_{i+1}\)</span> і підставляючи для <span>\(h\)</span>, де це доречно, отримуємо вирази</p>

\[f(x_{i-1}) = f(x_i) - hf^{\prime}(x_i) + \frac{h^2f''(x_i)}{2!} - \frac{h^3f'''(x_i)}{3!} + \frac{h^4f''''(x_i)}{4!} - \cdots\]
<p>та</p>

\[f(x_{i+1}) = f(x_i) + hf^{\prime}(x_i) + \frac{h''(x_i)}{2!} + \frac{h^3f'''(x_i)}{3!} + \frac{h^4f''''(x_i)}{4!} + \cdots\]
<p>Тепер розглянемо вираз <span>\(\frac{f(x_{i-1}) + 4f(x_i) + f(x_{i+1})}{6}\)</span>. Підставляючи ряд Тейлора для відповідних значень чисельника, отримуємо рівняння</p>

\[\frac{f(x_{i-1}) + 4f(x_i) + f(x_{i+1})}{6} = f(x_i) + \frac{h^2}{6}f''(x_i) + \frac{h^4}{72}f''''(x_i) + \cdots\]
<p>Зауважте, що непарні члени скорочуються. Це означає</p>

\[f(x_i) =\frac{f(x_{i-1}) + 4f(x_i) + f(x_{i+1})}{6} - \frac{h^2}{6}f''(x_i) + O(h^4).\]
<p>Шляхом підстановки ряду Тейлора для <span>\(f(x)\)</span>, інтеграл <span>\(f(x)\)</span> на двох підінтервалах тоді дорівнює</p>

\[\begin{eqnarray*}\int_{x_{i-1}}^{x_{i+1}} f(x) dx &amp;=&amp; \int_{x_{i-1}}^{x_{i+1}} \left(f(x_i) + f^{\prime}(x_i)(x - x_i) + \frac{f''(x_i)(x-x_i)^2}{2!}\right.\\
&amp;&amp;\qquad\qquad\left. + \frac{f'''(x_i)(x-x_i)^3}{3!}+ \frac{f''''(x_i)(x-x_i)^4}{4!} + \cdots\right)
dx.\end{eqnarray*}\]
<p>Знову ж таки, ми розподіляємо інтеграл і, не показуючи цього, відкидаємо інтеграли членів з непарними степенями, оскільки вони дорівнюють нулю.</p>

\[\int_{x_{i-1}}^{x_{i+1}} f(x) dx = \int_{x_{i-1}}^{x_{i+1}} f(x_i) dx + \int_{x_{i-1}}^{x_{i+1}}\frac{f''(x_i)(x-x_i)^2}{2!}dx + \int_{x_{i-1}}^{x_{i+1}}\frac{f''''(x_i)(x-x_i)^4}{4!}dx + \cdots.\]
<p>Потім ми виконуємо інтегрування. Як незабаром стане зрозуміло, нам вигідно обчислити інтеграл другого члена точно. Отримане рівняння є</p>

\[\int_{x_{i-1}}^{x_{i+1}} f(x) dx = 2h f(x_i) + \frac{h^3}{3}f''(x_i) + O(h^5).\]
<p>Підставляючи вираз для <span>\(f(x_i)\)</span>, отриманий раніше, права частина стає</p>

\[2h \left(\frac{f(x_{i-1}) + 4f(x_i) + f(x_{i+1})}{6} - \frac{h^2}{6}f''(x_i) + O(h^4)\right) + \frac{h^3}{3}f''(x_i) + O(h^5),\]
<p>яке можна перегрупувати в</p>

\[\left[\frac{h}{3}(f(x_{i-1}) + 4f(x_i) + f(x_{i+1})) - \frac{h^3}{3}f''(x_i) + O(h^5)\right] + \frac{h^3}{3}f''(x_i) + O(h^5).\]
<p>Скорочення та об'єднання відповідних членів призводить до інтегрального виразу</p>

\[\int_{x_{i-1}}^{x_{i+1}} f(x) dx = \frac{h}{3}(f(x_{i-1}) + 4f(x_i) + f(x_{i+1})) + O(h^5).\]
<p>Визнаючи, що <span>\(\frac{h}{3}(f(x_{i-1}) + 4f(x_i) + f(x_{i+1}))\)</span> є точною апроксимацією Правила Сімпсона для інтеграла на цьому підінтервалі, це рівняння означає, що Правило Сімпсона є <span>\(O(h^5)\)</span> на підінтервалі та <span>\(O(h^4)\)</span> на всьому інтервалі. Оскільки члени <span>\(h^3\)</span> точно скорочуються, Правило Сімпсона отримує ще <em>два</em> порядки точності!</p>
<p><strong>СПРОБУЙТЕ!</strong> Використайте Правило Сімпсона для апроксимації <span>\(\int_{0}^{\pi} \text{sin} (x)dx\)</span> з 11 рівномірно розташованими вузловими точками на всьому інтервалі. Порівняйте це значення з точним значенням 2.</p>

<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>

<span>a</span> <span>=</span> <span>0</span>
<span>b</span> <span>=</span> <span>np</span><span>.</span><span>pi</span>
<span>n</span> <span>=</span> <span>11</span>
<span>h</span> <span>=</span> <span>(</span><span>b</span> <span>-</span> <span>a</span><span>)</span> <span>/</span> <span>(</span><span>n</span> <span>-</span> <span>1</span><span>)</span>
<span>x</span> <span>=</span> <span>np</span><span>.</span><span>linspace</span><span>(</span><span>a</span><span>,</span> <span>b</span><span>,</span> <span>n</span><span>)</span>
<span>f</span> <span>=</span> <span>np</span><span>.</span><span>sin</span><span>(</span><span>x</span><span>)</span>

<span>I_simp</span> <span>=</span> <span>(</span><span>h</span><span>/</span><span>3</span><span>)</span> <span>*</span> <span>(</span><span>f</span><span>[</span><span>0</span><span>]</span> <span>+</span> <span>2</span><span>*</span><span>sum</span><span>(</span><span>f</span><span>[:</span><span>n</span><span>-</span><span>2</span><span>:</span><span>2</span><span>])</span> \
            <span>+</span> <span>4</span><span>*</span><span>sum</span><span>(</span><span>f</span><span>[</span><span>1</span><span>:</span><span>n</span><span>-</span><span>1</span><span>:</span><span>2</span><span>])</span> <span>+</span> <span>f</span><span>[</span><span>n</span><span>-</span><span>1</span><span>])</span>
<span>err_simp</span> <span>=</span> <span>2</span> <span>-</span> <span>I_simp</span>

<span>print</span><span>(</span><span>I_simp</span><span>)</span>
<span>print</span><span>(</span><span>err_simp</span><span>)</span>
</pre>

<pre><span></span>2.0001095173150043
-0.00010951731500430384
</pre>
