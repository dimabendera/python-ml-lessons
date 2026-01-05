<h1>Метод бісекції<a href="#bisection-method" title="Permalink to this headline"></a></h1>
<p><strong>Теорема про проміжне значення</strong> стверджує, що якщо <span>\(f(x)\)</span> є неперервною функцією між <span>\(a\)</span> та <span>\(b\)</span>, і <span>\({\text{sign}}(f(a)) \ne {\text{sign}}(f(b))\)</span>, тоді має існувати <span>\(c\)</span>, таке що <span>\(a &lt; c &lt; b\)</span> і <span>\(f(c) = 0\)</span>. Це проілюстровано на наступному малюнку.</p>

<p><strong>Метод бісекції</strong> використовує теорему про проміжне значення ітеративно для знаходження коренів. Нехай <span>\(f(x)\)</span> є неперервною функцією, а <span>\(a\)</span> та <span>\(b\)</span> — дійсними скалярними значеннями такими, що <span>\(a &lt; b\)</span>. Припустимо, не обмежуючи загальності, що <span>\(f(a) &gt; 0\)</span> і <span>\(f(b) &lt; 0\)</span>. Тоді за теоремою про проміжне значення, на відкритому інтервалі <span>\((a,b)\)</span> має існувати корінь. Тепер нехай <span>\(m = \frac{b + a}{2}\)</span>, середина між <span>\(a\)</span> та <span>\(b\)</span>. Якщо <span>\(f(m) = 0\)</span> або є достатньо близьким до нуля, то <span>\(m\)</span> є коренем. Якщо <span>\(f(m) &gt; 0\)</span>, то <span>\(m\)</span> є покращенням лівої межі, <span>\(a\)</span>, і гарантовано існує корінь на відкритому інтервалі <span>\((m,b)\)</span>. Якщо <span>\(f(m) &lt; 0\)</span>, то <span>\(m\)</span> є покращенням правої межі, <span>\(b\)</span>, і гарантовано існує корінь на відкритому інтервалі <span>\((a,m)\)</span>. Цей сценарій зображено на наступному малюнку.</p>

<p>Процес оновлення <span>\(a\)</span> та <span>\(b\)</span> можна повторювати, доки похибка не стане прийнятно низькою.</p>
<p><strong>СПРОБУЙТЕ!</strong> Запрограмуйте функцію <em>my_bisection(f, a, b, tol)</em>, яка наближено обчислює корінь <span>\(r\)</span> функції <span>\(f\)</span>, обмежений <span>\(a\)</span> та <span>\(b\)</span> з точністю до <span>\(|f(\frac{a + b}{2})| &lt; {\text{tol}}\)</span>.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>

<span>def</span> <span>my_bisection</span><span>(</span><span>f</span><span>,</span> <span>a</span><span>,</span> <span>b</span><span>,</span> <span>tol</span><span>):</span> 
    <span># наближено обчислює корінь, R, функції f, обмежений</span>
    <span># a та b з точністю до</span>
    <span># | f(m) | < tol, де m - середина</span>
    <span># між a та b. Рекурсивна реалізація</span>
    
    <span># перевірка, чи a та b обмежують корінь</span>
    <span>if</span> <span>np</span><span>.</span><span>sign</span><span>(</span><span>f</span><span>(</span><span>a</span><span>))</span> <span>==</span> <span>np</span><span>.</span><span>sign</span><span>(</span><span>f</span><span>(</span><span>b</span><span>)):</span>
        <span>raise</span> <span>Exception</span><span>(</span>
         <span>"Скаляри a та b не обмежують корінь"</span><span>)</span>
        
    <span># знайти середину</span>
    <span>m</span> <span>=</span> <span>(</span><span>a</span> <span>+</span> <span>b</span><span>)</span><span>/</span><span>2</span>
    
    <span>if</span> <span>np</span><span>.</span><span>abs</span><span>(</span><span>f</span><span>(</span><span>m</span><span>))</span> <span>&lt;</span> <span>tol</span><span>:</span>
        <span># умова зупинки, повернути m як корінь</span>
        <span>return</span> <span>m</span>
    <span>elif</span> <span>np</span><span>.</span><span>sign</span><span>(</span><span>f</span><span>(</span><span>a</span><span>))</span> <span>==</span> <span>np</span><span>.</span><span>sign</span><span>(</span><span>f</span><span>(</span><span>m</span><span>)):</span>
        <span># випадок, коли m є покращенням для a.</span>
        <span># Зробити рекурсивний виклик з a = m</span>
        <span>return</span> <span>my_bisection</span><span>(</span><span>f</span><span>,</span> <span>m</span><span>,</span> <span>b</span><span>,</span> <span>tol</span><span>)</span>
    <span>elif</span> <span>np</span><span>.</span><span>sign</span><span>(</span><span>f</span><span>(</span><span>b</span><span>))</span> <span>==</span> <span>np</span><span>.</span><span>sign</span><span>(</span><span>f</span><span>(</span><span>m</span><span>)):</span>
        <span># випадок, коли m є покращенням для b.</span>
        <span># Зробити рекурсивний виклик з b = m</span>
        <span>return</span> <span>my_bisection</span><span>(</span><span>f</span><span>,</span> <span>a</span><span>,</span> <span>m</span><span>,</span> <span>tol</span><span>)</span>
</pre>



<p><strong>СПРОБУЙТЕ!</strong> <span>\(\sqrt{2}\)</span> можна обчислити як корінь функції <span>\(f(x) = x^2 - 2\)</span>. Починаючи з <span>\(a = 0\)</span> та <span>\(b = 2\)</span>, використовуйте <em>my_bisection</em> для наближеного обчислення <span>\(\sqrt{2}\)</span> з точністю <span>\(|f(x)| &lt; 0.1\)</span> та <span>\(|f(x)| &lt; 0.01\)</span>. Переконайтеся, що результати близькі до кореня, підставивши знайдений корінь назад у функцію.</p>


<pre><span></span><span>f</span> <span>=</span> <span>lambda</span> <span>x</span><span>:</span> <span>x</span><span>**</span><span>2</span> <span>-</span> <span>2</span>

<span>r1</span> <span>=</span> <span>my_bisection</span><span>(</span><span>f</span><span>,</span> <span>0</span><span>,</span> <span>2</span><span>,</span> <span>0.1</span><span>)</span>
<span>print</span><span>(</span><span>"r1 ="</span><span>,</span> <span>r1</span><span>)</span>
<span>r01</span> <span>=</span> <span>my_bisection</span><span>(</span><span>f</span><span>,</span> <span>0</span><span>,</span> <span>2</span><span>,</span> <span>0.01</span><span>)</span>
<span>print</span><span>(</span><span>"r01 ="</span><span>,</span> <span>r01</span><span>)</span>

<span>print</span><span>(</span><span>"f(r1) ="</span><span>,</span> <span>f</span><span>(</span><span>r1</span><span>))</span>
<span>print</span><span>(</span><span>"f(r01) ="</span><span>,</span> <span>f</span><span>(</span><span>r01</span><span>))</span>
</pre>



<pre><span></span>r1 = 1.4375
r01 = 1.4140625
f(r1) = 0.06640625
f(r01) = -0.00042724609375
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Подивіться, що станеться, якщо ви використаєте <span>\(a = 2\)</span> та <span>\(b = 4\)</span> для наведеної вище функції.</p>


<pre><span></span><span>my_bisection</span><span>(</span><span>f</span><span>,</span> <span>2</span><span>,</span> <span>4</span><span>,</span> <span>0.01</span><span>)</span>
</pre>



<pre><span></span><span>---------------------------------------------------------------------------</span>
<span>Exception</span><span>                                 </span>Traceback (most recent call last)
<span>&lt;</span><span>ipython</span><span>-</span><span>input</span><span>-</span><span>3</span><span>-</span><span>4158</span><span>b7a9ae67</span><span>&gt;</span> <span>in</span> <span>&lt;</span><span>module</span><span>&gt;</span>
<span>----&gt; </span><span>1</span> <span>my_bisection</span><span>(</span><span>f</span><span>,</span> <span>2</span><span>,</span> <span>4</span><span>,</span> <span>0.01</span><span>)</span>

<span>&lt;ipython-input-1-36f06123e87c&gt;</span> in <span>my_bisection</span><span>(f, a, b, tol)</span>
<span>     </span><span>10</span>     <span>if</span> <span>np</span><span>.</span><span>sign</span><span>(</span><span>f</span><span>(</span><span>a</span><span>))</span> <span>==</span> <span>np</span><span>.</span><span>sign</span><span>(</span><span>f</span><span>(</span><span>b</span><span>)):</span>
<span>     </span><span>11</span>         <span>raise</span> <span>Exception</span><span>(</span>
<span>---&gt; </span><span>12</span>          <span>"Скаляри a та b не обмежують корінь"</span><span>)</span>
<span>     </span><span>13</span> 
<span>     </span><span>14</span>     <span># знайти середину</span>

<span>Exception</span>: Скаляри a та b не обмежують корінь
</pre>
