<h1>Відлагодження<a href="#debugging" title="Постійне посилання на цей заголовок"></a></h1>
<p>Відлагодження — це процес систематичного видалення помилок, або багів, з вашого коду. Python має функціональні можливості, які можуть допомогти вам під час відлагодження. Стандартним інструментом відлагодження в Python є <em>pdb</em> (Python DeBugger) для інтерактивного відлагодження. Він дозволяє вам покроково переглядати код, щоб з'ясувати, що може спричиняти складну помилку. Версія цього для IPython — це <em>ipdb</em> (IPython DeBugger). Ми не будемо надто багато про це розповідати тут, ви можете переглянути <a href="https://docs.python.org/3/library/pdb.html">документацію для деталей</a>. У цьому розділі будуть представлені основні кроки відлагодження в Jupyter notebook. Ми покажемо вам, як використовувати дві дійсно корисні магічні команди %debug та %pdb, щоб знайти проблемний код.</p>
<p>Існує два способи відлагодження вашого коду: (1) активувати відладчик після виникнення винятку; (2) активувати відладчик перед запуском коду.</p>

<h2>Активація відладчика після виникнення винятку<a href="#activate-the-debugger-after-we-run-into-an-exception" title="Постійне посилання на цей заголовок"></a></h2>
<p>Якщо ми запускаємо код, який зупиняється на винятку, ми можемо викликати %debug. Наприклад, у нас є функція, яка підносить вхідне число до квадрату, а потім додає його до себе, як показано нижче:</p>

<pre><span></span><span>def</span> <span>square_number</span><span>(</span><span>x</span><span>):</span>
    
    <span>sq</span> <span>=</span> <span>x</span><span>**</span><span>2</span>
    <span>sq</span> <span>+=</span> <span>x</span>
    
    <span>return</span> <span>sq</span>
</pre>

<pre><span></span><span>square_number</span><span>(</span><span>'10'</span><span>)</span>
</pre>

<pre><span></span><span>---------------------------------------------------------------------------</span>
<span>TypeError</span><span>                                 </span>Traceback (most recent call last)
<span>&lt;</span><span>ipython</span><span>-</span><span>input</span><span>-</span><span>2</span><span>-</span><span>e0b77a2957d5</span><span>&gt;</span> <span>in</span> <span>&lt;</span><span>module</span><span>&gt;</span>
<span>----&gt; </span><span>1</span> <span>square_number</span><span>(</span><span>'10'</span><span>)</span>

<span>&lt;ipython-input-1-3fc6a3900214&gt;</span> in <span>square_number</span><span>(x)</span>
<span>      </span><span>1</span> <span>def</span> <span>square_number</span><span>(</span><span>x</span><span>):</span>
<span>      </span><span>2</span> 
<span>----&gt; </span><span>3</span>     <span>sq</span> <span>=</span> <span>x</span><span>**</span><span>2</span>
<span>      </span><span>4</span>     <span>sq</span> <span>+=</span> <span>x</span>
<span>      </span><span>5</span> 

<span>TypeError</span>: unsupported operand type(s) for ** or pow(): 'str' and 'int'
</pre>

<p>Після виникнення цього винятку ми можемо активувати відладчик за допомогою магічної команди %debug, яка відкриє для вас інтерактивний відладчик. Ви можете вводити команди у відладчику, щоб отримати корисну інформацію.</p>

<pre><span></span><span>%</span><span>debug</span>
</pre>

<pre><span></span>&gt; <span>&lt;ipython-input-1-3fc6a3900214&gt;</span>(3)<span>square_number</span><span>()</span>
<span>      1 def</span> square_number<span>(</span>x<span>):</span>
<span>      2 </span>
<span>----&gt; 3 </span><span>    </span>sq <span>=</span> x<span>**</span><span>2</span>
<span>      4 </span><span>    </span>sq <span>+=</span> x
<span>      5 </span>

ipdb&gt; h

Documented commands (type help &lt;topic&gt;):
========================================
EOF    cl         disable  interact  next    psource  rv         unt   
a      clear      display  j         p       q        s          until 
alias  commands   down     jump      pdef    quit     source     up    
args   condition  enable   l         pdoc    r        step       w     
b      cont       exit     list      pfile   restart  tbreak     whatis
break  continue   h        ll        pinfo   return   u          where 
bt     d          help     longlist  pinfo2  retval   unalias  
c      debug      ignore   n         pp      run      undisplay

Miscellaneous help topics:
========================================
exec  pdb

ipdb&gt; p x
'10'
ipdb&gt; type(x)
&lt;class 'str'&gt;
ipdb&gt; p locals()
{'x': '10'}
ipdb&gt; q
</pre>

<p>Ви бачите, що після активації <em>ipdb</em> ми можемо вводити команди, щоб отримати інформацію про код. У наведеному вище прикладі я ввів наступні команди:</p>
<ul>
<li><p><em>h</em>, щоб отримати список довідки</p></li>
<li><p><em>p x</em>, щоб вивести значення x</p></li>
<li><p><em>type(x)</em>, щоб отримати тип x</p></li>
<li><p><em>p locals()</em>, щоб вивести всі локальні змінні</p></li>
</ul>
<p>Ось деякі з найчастіших команд, які ви можете вводити в pdb:</p>
<ul>
<li><p>n(ext) — наступний рядок і виконати його</p></li>
<li><p>c(ontinue) — продовжувати виконання до наступної точки зупинки</p></li>
<li><p>p(rint) — вивести змінні</p></li>
<li><p>l(ist) — показати, де ви знаходитесь</p></li>
<li><p>‘Enter` — повторити попередню команду</p></li>
<li><p>s(tep) — зайти в підпрограму</p></li>
<li><p>r(eturn) — вийти з підпрограми</p></li>
<li><p>h(elp) — довідка</p></li>
<li><p>q(uit) — вийти з відладчика</p></li>
</ul>

<h2>Активація відладчика перед запуском коду<a href="#activate-debugger-before-we-run-the-code" title="Постійне посилання на цей заголовок"></a></h2>
<p>Ми також можемо увімкнути відладчик ще до запуску коду, а потім вимкнути його після завершення виконання коду.</p>

<pre><span></span><span>%</span><span>pdb</span> on
</pre>

<pre><span></span>Automatic pdb calling has been turned ON
</pre>

<pre><span></span><span>square_number</span><span>(</span><span>'10'</span><span>)</span>
</pre>

<pre><span></span><span>---------------------------------------------------------------------------</span>
<span>TypeError</span><span>                                 </span>Traceback (most recent call last)
<span>&lt;</span><span>ipython</span><span>-</span><span>input</span><span>-</span><span>5</span><span>-</span><span>e0b77a2957d5</span><span>&gt;</span> <span>in</span> <span>&lt;</span><span>module</span><span>&gt;</span>
<span>----&gt; </span><span>1</span> <span>square_number</span><span>(</span><span>'10'</span><span>)</span>

<span>&lt;ipython-input-1-3fc6a3900214&gt;</span> in <span>square_number</span><span>(x)</span>
<span>      </span><span>1</span> <span>def</span> <span>square_number</span><span>(</span><span>x</span><span>):</span>
<span>      </span><span>2</span> 
<span>----&gt; </span><span>3</span>     <span>sq</span> <span>=</span> <span>x</span><span>**</span><span>2</span>
<span>      </span><span>4</span>     <span>sq</span> <span>+=</span> <span>x</span>
<span>      </span><span>5</span> 

<span>TypeError</span>: unsupported operand type(s) for ** or pow(): 'str' and 'int'
</pre>

<pre><span></span>&gt; <span>&lt;ipython-input-1-3fc6a3900214&gt;</span>(3)<span>square_number</span><span>()</span>
<span>      1 def</span> square_number<span>(</span>x<span>):</span>
<span>      2 </span>
<span>----&gt; 3 </span><span>    </span>sq <span>=</span> x<span>**</span><span>2</span>
<span>      4 </span><span>    </span>sq <span>+=</span> x
<span>      5 </span>

ipdb&gt; p x
'10'
ipdb&gt; c
</pre>

<pre><span></span><span># вимкнемо відладчик</span>
<span>%</span><span>pdb</span> off
</pre>

<pre><span></span>Automatic pdb calling has been turned OFF
</pre>

<h2>Додавання точки зупинки<a href="#add-a-breakpoint" title="Постійне посилання на цей заголовок"></a></h2>
<p>Часто дуже корисно вставляти точку зупинки у ваш код. Точка зупинки — це рядок у вашому коді, на якому Python зупиниться під час виконання функції.</p>

<pre><span></span><span>import</span> <span>pdb</span>
</pre>

<pre><span></span><span>def</span> <span>square_number</span><span>(</span><span>x</span><span>):</span>
    
    <span>sq</span> <span>=</span> <span>x</span><span>**</span><span>2</span>
    
    <span># додаємо точку зупинки тут</span>
    <span>pdb</span><span>.</span><span>set_trace</span><span>()</span>
    
    <span>sq</span> <span>+=</span> <span>x</span>
    
    <span>return</span> <span>sq</span>
</pre>

<pre><span></span><span>square_number</span><span>(</span><span>3</span><span>)</span>
</pre>

<pre><span></span>&gt; &lt;ipython-input-8-e48ec2675aea&gt;(8)square_number()
-&gt; sq += x
(Pdb) l
  3  	    sq = x**2
  4  	
  5  	    # додаємо точку зупинки тут
  6  	    pdb.set_trace()
  7  	
  8  -&gt;	    sq += x
  9  	
 10  	    return sq
[EOF]
(Pdb) p x
3
(Pdb) p sq
9
(Pdb) c
</pre>

<pre><span></span>12
</pre>

<p>Ми бачимо, що після додавання <em>pdb.set_trace()</em> програма зупиняється на цьому рядку та активує відладчик <em>pdb</em>. Ми можемо перевірити всі значення змінних, які були присвоєні до цього рядка. І використовувати команду <em>c</em> для продовження виконання.</p>
<p>Використання відладчика Python може бути надзвичайно корисним для пошуку та виправлення помилок у вашому коді. Ми заохочуємо вас використовувати відладчик для великих програм.</p>
