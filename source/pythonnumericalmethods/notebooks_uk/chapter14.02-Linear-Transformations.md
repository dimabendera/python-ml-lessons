<h1>Лінійні перетворення<a href="#linear-transformations" title="Постійне посилання на цей заголовок"></a></h1>
<p>Для векторів <span>\(x\)</span> та <span>\(y\)</span>, і скалярів <span>\(a\)</span> та <span>\(b\)</span>, достатньо сказати, що функція <span>\(F\)</span> є <strong>лінійним перетворенням</strong>, якщо</p>

\[
F(ax + by) = aF(x) + bF(y).
\]
<p>Можна показати, що множення <span>\({m} \times {n}\)</span> матриці <span>\(A\)</span> та <span>\({n} \times {1}\)</span> вектора <span>\(v\)</span> сумісного розміру є лінійним перетворенням <span>\(v\)</span>. Тому надалі матриця буде синонімом функції лінійного перетворення.</p>
<p><strong>СПРОБУЙТЕ!</strong> Нехай <span>\(x\)</span> буде вектором, і нехай <span>\(F(x)\)</span> визначається як <span>\(F(x) = Ax\)</span>, де <span>\(A\)</span> є прямокутною матрицею відповідного розміру. Покажіть, що <span>\(F(x)\)</span> є лінійним перетворенням.</p>
<p>Доведення:
Оскільки <span>\(F(x) = Ax\)</span>, то
для векторів <span>\(v\)</span> та <span>\(w\)</span>, і скалярів <span>\(a\)</span> та <span>\(b\)</span>, <span>\(F(av +
bw) = A(av + bw)\)</span> (за визначенням <span>\(F\)</span>)<span>\(=\)</span><span>\(aAv + bAw\)</span> (за
дистрибутивною властивістю множення матриць)<span>\(=\)</span><span>\(aF(v) +
bF(w)\)</span> (за визначенням <span>\(F\)</span>).</p>
<p>Якщо <span>\(A\)</span> є <span>\({m} \times {n}\)</span> матрицею, то існують два важливі підпростори, пов'язані з <span>\(A\)</span>: один з яких <span>\({\mathbb{R}}^n\)</span>, інший <span>\({\mathbb{R}}^m\)</span>. <strong>Область визначення</strong> <span>\(A\)</span> є підпростором <span>\({\mathbb{R}}^n\)</span>. Це множина всіх векторів, які можуть бути помножені на <span>\(A\)</span> справа. <strong>Образ</strong> <span>\(A\)</span> є підпростором <span>\({\mathbb{R}}^m\)</span>. Це множина всіх векторів <span>\(y\)</span> таких, що <span>\(y=Ax\)</span>. Його можна позначити як <span>\(\mathcal{R}(\mathbf{A})\)</span>, де <span>\(\mathcal{R}(\mathbf{A}) = \{y \in {\mathbb{R}}^m: Ax = y\}\)</span>. Інший спосіб мислення про образ <span>\(A\)</span> — це множина всіх лінійних комбінацій стовпців у <span>\(A\)</span>, де <span>\(x_i\)</span> є коефіцієнтом i-го стовпця в <span>\(A\)</span>. <strong>Нуль-простір</strong> <span>\(A\)</span>, визначений як <span>\(\mathcal{N}(\mathbf{A}) = \{x \in {\mathbb{R}}^n: Ax = 0_m\}\)</span>, є підмножиною векторів в області визначення <span>\(A, x\)</span>, таких, що <span>\(Ax = 0_m\)</span>, де <span>\(0_m\)</span> є <strong>нульовим вектором</strong> (тобто вектором у <span>\({\mathbb{R}}^m\)</span> з усіма нулями).</p>
<p><strong>СПРОБУЙТЕ!</strong> Нехай <span>\(A = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]\)</span> і нехай область визначення <span>\(A\)</span> буде <span>\({\mathbb{R}}^3\)</span>. Охарактеризуйте образ і нуль-простір <span>\(A\)</span>.</p>
<p>Нехай <span>\(v = [x,y,z]\)</span> буде вектором у <span>\({\mathbb{R}}^3\)</span>. Тоді <span>\(u = Av\)</span> є вектором <span>\(u = [x,y,0]\)</span>. Оскільки <span>\(x,y\in {\mathbb{R}}\)</span>, образ <span>\(A\)</span> є <span>\(x\)</span>-<span>\(y\)</span>-площиною при <span>\(z = 0\)</span>.</p>
<p>Нехай <span>\(v = [0,0,z]\)</span> для <span>\(z\in {\mathbb{R}}\)</span>. Тоді <span>\(u = Av\)</span> є вектором <span>\(u = [0, 0, 0]\)</span>. Отже, нуль-простір <span>\(A\)</span> є <span>\(z\)</span>-віссю (тобто множиною векторів <span>\([0,0,z]\)</span>, <span>\(z\in {\mathbb{R}}\)</span>).</p>
<p>Отже, це лінійне перетворення "сплющує" будь-яку <span>\(z\)</span>-компоненту вектора.</p>
