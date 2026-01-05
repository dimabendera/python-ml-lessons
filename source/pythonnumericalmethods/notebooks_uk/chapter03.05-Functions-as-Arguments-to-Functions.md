<h1>Функції як аргументи для функцій<a href="#functions-as-arguments-to-functions" title="Постійне посилання на цей заголовок"></a></h1>
<p>До цього часу ви присвоювали різні структури даних іменам змінних. Можливість присвоювати структуру даних змінній дозволяє нам передавати інформацію функціям і отримувати інформацію від них акуратним і впорядкованим способом. Іноді корисно мати можливість передавати функцію як змінну іншій функції. Іншими словами, вхідними даними для деяких функцій можуть бути інші функції. В останньому розділі ми бачили, що лямбда-функція повертає об'єкт функції змінній. У цьому розділі ми продовжимо розглядати, як об'єкт функції може бути використаний як вхідні дані для іншої функції.</p>
<p><strong>СПРОБУЙТЕ!</strong> Присвойте функцію <em>max</em> змінній <em>f</em>. Перевірте тип <em>f</em>.</p>


<pre><span></span><span>f</span> <span>=</span> <span>max</span>
<span>print</span><span>(</span><span>type</span><span>(</span><span>f</span><span>))</span>
</pre>



<pre><span></span>&lt;class 'builtin_function_or_method'&gt;
</pre>



<p>У попередньому прикладі <em>f</em> тепер еквівалентна функції <em>max</em>. Так само, як <em>x = 1</em> означає, що <em>x</em> і 1 є взаємозамінними, <em>f</em> і функція <em>max</em> тепер є взаємозамінними.</p>
<p><strong>СПРОБУЙТЕ!</strong> Отримайте максимальне значення зі списку [2, 3, 5] за допомогою <em>f</em>. Перевірте, що результат такий самий, як при використанні <em>max</em>.</p>


<pre><span></span><span>print</span><span>(</span><span>f</span><span>([</span><span>2</span><span>,</span> <span>3</span><span>,</span> <span>5</span><span>]))</span>
<span>print</span><span>(</span><span>max</span><span>([</span><span>2</span><span>,</span> <span>3</span><span>,</span> <span>5</span><span>]))</span>
</pre>



<pre><span></span>5
5
</pre>



<p><strong>СПРОБУЙТЕ!</strong> Напишіть функцію <em>my_fun_plus_one</em>, яка приймає об'єкт функції, <em>f</em>, і число з плаваючою комою <em>x</em> як вхідні аргументи. <em>my_fun_plus_one</em> повинна повертати <em>f</em>, обчислену в точці <em>x</em>, і результат, до якого додано значення 1. Перевірте, що вона працює для різних функцій і значень <em>x</em>.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>

<span>def</span> <span>my_fun_plus_one</span><span>(</span><span>f</span><span>,</span> <span>x</span><span>):</span>
    <span>return</span> <span>f</span><span>(</span><span>x</span><span>)</span> <span>+</span> <span>1</span>

<span>print</span><span>(</span><span>my_fun_plus_one</span><span>(</span><span>np</span><span>.</span><span>sin</span><span>,</span> <span>np</span><span>.</span><span>pi</span><span>/</span><span>2</span><span>))</span>
<span>print</span><span>(</span><span>my_fun_plus_one</span><span>(</span><span>np</span><span>.</span><span>cos</span><span>,</span> <span>np</span><span>.</span><span>pi</span><span>/</span><span>2</span><span>))</span>
<span>print</span><span>(</span><span>my_fun_plus_one</span><span>(</span><span>np</span><span>.</span><span>sqrt</span><span>,</span> <span>25</span><span>))</span>
</pre>



<pre><span></span>2.0
1.0
6.0
</pre>



<p>Ми бачимо з наведеного вище прикладу, що різні функції використовуються як вхідні дані для функції. Звісно, ми також можемо використовувати лямбда-функції.</p>


<pre><span></span><span>print</span><span>(</span><span>my_fun_plus_one</span><span>(</span><span>lambda</span> <span>x</span><span>:</span> <span>x</span> <span>+</span> <span>2</span><span>,</span> <span>2</span><span>))</span>
</pre>



<pre><span></span>5
</pre>
