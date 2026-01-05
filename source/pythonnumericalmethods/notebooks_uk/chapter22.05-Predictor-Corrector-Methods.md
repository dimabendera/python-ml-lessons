<h1>Методи предиктора-коректора та Рунге-Кутти<a href="#predictor-corrector-and-runge-kutta-methods" title="Permalink to this headline"></a></h1>

<h2>Методи предиктора-коректора<a href="#predictor-corrector-methods" title="Permalink to this headline"></a></h2>
<p>Для будь-якого значення часу та стану, функція <span>\(F(t, S(t))\)</span> повертає зміну стану <span>\(\frac{dS(t)}{dt}\)</span>. Методи <strong>предиктора-коректора</strong> для розв'язання задач з початковими умовами покращують точність апроксимації методів без предиктора-коректора шляхом декількох запитів до функції <span>\(F\)</span> у різних точках (прогнози), а потім використовують зважене середнє результатів (корекції) для оновлення стану. По суті, він використовує дві формули: <strong>предиктор</strong> та <strong>коректор</strong>. Предиктор — це явна формула, яка спочатку оцінює розв'язок у точці <span>\(t_{j+1}\)</span>, тобто для цього кроку ми можемо використовувати метод Ейлера або інші методи. Після того, як ми отримаємо розв'язок <span>\(S(t_{j+1})\)</span>, ми можемо застосувати коректор для підвищення точності. Використовуючи знайдений <span>\(S(t_{j+1})\)</span> у правій частині неявної в іншому випадку формули, коректор може обчислити новий, більш точний розв'язок.</p>
<p><strong>Метод середньої точки</strong> має крок предиктора:</p>

\[
S\left(t_{j} + \frac{h}{2}\right) = S(t_j) + \frac{h}{2}F(t_j, S(t_j)),
\]
<p>що є прогнозом значення розв'язку на півдорозі між <span>\(t_j\)</span> та <span>\(t_{j+1}\)</span>.</p>
<p>Потім він обчислює крок коректора:</p>

\[
S(t_{j+1}) = S(t_j) + hF\left(t_j + \frac{h}{2}, S\left(t_{j} +
\frac{h}{2}\right)\right) \]
<p>який обчислює розв'язок у точці <span>\(S(t_{j+1})\)</span> з <span>\(S(t_j)\)</span>, але використовуючи похідну з <span>\(S\left(t_{j} + \frac{h}{2}\right)\)</span>.</p>


<h2>Методи Рунге-Кутти<a href="#runge-kutta-methods" title="Permalink to this headline"></a></h2>
<p>Методи <strong>Рунге-Кутти</strong> (РК) є одними з найпоширеніших методів для розв'язання звичайних диференціальних рівнянь (ЗДР). Нагадаємо, що метод Ейлера використовує перші два члени ряду Тейлора для апроксимації чисельного інтегрування, яке є лінійним: <span>\(S(t_{j+1}) = S(t_j + h) = S(t_j) + h \cdot S'(t_j)\)</span>.</p>
<p>Ми можемо значно покращити точність чисельного інтегрування, якщо збережемо більше членів ряду в</p>

\[S(t_{j+1}) = S(t_j + h) = S(t_j) + S'(t_j)h + \frac{1}{2!}S''(t_j)h^2 + \cdots + \frac{1}{n!}S^{(n)}(t_j)h^n \label{eq:taylor} \tag{1}\]
<p>Щоб отримати цей більш точний розв'язок, нам потрібно вивести вирази для <span>\(S''(t_j), S'''(t_j), \cdots, S^{(n)}(t_j)\)</span>. Цієї додаткової роботи можна уникнути, використовуючи методи РК, які базуються на усіченому ряді Тейлора, але не вимагають обчислення цих вищих похідних.</p>

<h3>Метод Рунге-Кутти другого порядку<a href="#second-order-runge-kutta-method" title="Permalink to this headline"></a></h3>
<p>Спочатку виведемо метод РК другого порядку. Нехай <span>\(\frac{dS(t)}{dt} = F(t,S(t))\)</span>, тоді ми можемо припустити формулу інтегрування у вигляді</p>

\[ S(t + h) = S(t) + c_1F(t, S(t))h + c_2F[t+ph, S(t)+qhF(t, S(t))]h \label{eq:integration} \tag{2}\]
<p>Ми можемо спробувати знайти ці параметри <span>\(c_1, c_2, p, q\)</span>, зіставляючи наведене вище рівняння з рядом Тейлора другого порядку, що дає нам</p>

\[ S(t + h) =  S(t) + S'(t)h + \frac{1}{2!}S''(t)h^2 = S(t) + F(t, S(t))h + \frac{1}{2!}F'(t, S(t))h^2 \label{eq:matching} \tag{3}\]
<p>Зауважимо, що $<span>\(F'(t, s(t)) = \frac{\partial F}{\partial t} + \frac{\partial F}{\partial S}\frac{\partial S}{\partial t} = \frac{\partial F}{\partial t} + \frac{\partial F}{\partial S}F\)</span>$</p>
<p>Отже, рівняння <span>\(\eqref{eq:matching}\)</span> можна записати як:</p>

\[ S(t + h) = S + Fh + \frac{1}{2!}\Big(\frac{\partial F}{\partial t} + \frac{\partial F}{\partial S}F\Big)h^2 \label{eq:rewrite-matching} \tag{4}\]
<p>У рівнянні <span>\(\eqref{eq:integration}\)</span>, ми можемо переписати останній член, застосувавши ряд Тейлора для кількох змінних, що дає нам:</p>

\[F[t+ph, S+qhF)] = F + \frac{\partial F}{\partial t}ph + qh\frac{\partial F}{\partial S}F\]
<p>таким чином, рівняння <span>\(\eqref{eq:integration}\)</span> стає:</p>

\[ S(t + h) = S + (c_1+c_2)Fh + c_1\Big[ \frac{\partial F}{\partial t}p + q\frac{\partial F}{\partial S}F \Big]h^2 \label{eq:rewrite-integration} \tag{5}\]
<p>Порівнюючи рівняння <span>\(\eqref{eq:rewrite-matching}\)</span> та <span>\(\eqref{eq:rewrite-integration}\)</span>, ми можемо легко отримати:</p>

\[c_1 + c_2 = 1, \space c_2p=\frac{1}{2}, \space c_2q=\frac{1}{2} \label{eq:result} \tag{6}\]
<p>Оскільки <span>\(\eqref{eq:result}\)</span> має чотири невідомі та лише три рівняння, ми можемо присвоїти будь-яке значення одному з параметрів і отримати решту параметрів. Одним з популярних варіантів є:</p>

\[c_1 =\frac{1}{2}, \space c_2 =\frac{1}{2}, \space p =1, \space q=1\]
<p>Ми також можемо визначити:
$$</p>

\[\begin{eqnarray*}
k_1 &amp; = &amp; F(t_j,S(t_j))\\
k_2 &amp; = &amp; F\left(t_j+ph, S(t_j)+qhk_1\right)\\
\end{eqnarray*}\]

\[ \begin{align}\begin{aligned}де ми будемо мати:\\$$S(t_{j+1}) = S(t_j) + \frac{1}{2}(k_1+k_2)h\end{aligned}\end{align} \]


<h3>Метод Рунге-Кутти четвертого порядку<a href="#fourth-order-runge-kutta-method" title="Permalink to this headline"></a></h3>
<p>Класичним методом інтегрування ЗДР з високим порядком точності є <strong>метод Рунге-Кутти четвертого порядку</strong> (РК4). Його отримують з ряду Тейлора, використовуючи аналогічний підхід, який ми щойно обговорювали для методу другого порядку. Цей метод використовує чотири точки <span>\(k_1, k_2, k_3\)</span>, та <span>\(k_4\)</span>. Зважене середнє цих значень використовується для отримання апроксимації розв'язку. Формула виглядає наступним чином.</p>

\[\begin{split}
\begin{eqnarray*}
k_1 &amp; = &amp; F(t_j,S(t_j))\\
k_2 &amp; = &amp; F\left(t_j+\frac{h}{2},S(t_j)+\frac{1}{2}k_1h\right)\\
k_3 &amp; = &amp; F\left(t_j+\frac{h}{2},S(t_j)+\frac{1}{2}k_2h\right)\\
k_4 &amp; = &amp; F(t_j+h,S(t_j)+k_3h)
\end{eqnarray*}
\end{split}\]
<p>Отже, ми будемо мати:</p>

\[
S(t_{j+1}) = S(t_j) + \frac{h}{6}\left(k_1 + 2k_2 + 2k_3 + k_4\right).
\]
<p>Як випливає з назви, метод РК4 має четвертий порядок точності, або <span>\(O(h^4)\)</span>.</p>
