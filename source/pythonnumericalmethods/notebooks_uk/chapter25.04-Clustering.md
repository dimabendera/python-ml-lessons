<h1>Кластеризація<a href="#clustering" title="Permalink to this headline"></a></h1>
<p>Кластеризація — це набір алгоритмів некерованого навчання. Вони корисні, коли у нас немає жодних міток для даних, і алгоритми намагатимуться знайти закономірності внутрішньої структури або подібності даних, щоб розподілити їх по різних групах. Оскільки з точками даних не пов'язані жодні мітки (справжні відповіді), ми не можемо використовувати цю додаткову інформацію для обмеження задачі. Але натомість існують інші способи вирішення проблеми, і в цьому розділі ми розглянемо дуже популярний алгоритм кластеризації — K-середніх.</p>

<h2>Основи K-середніх<a href="#k-means-basics" title="Permalink to this headline"></a></h2>
<p>Існує багато різних алгоритмів кластеризації, K-середніх є широко використовуваним алгоритмом кластеризації завдяки своїй простій ідеї та ефективності.</p>
<p><strong>Ідея K-середніх</strong></p>
<p>Основна ідея K-середніх полягає в тому, що якщо дві точки знаходяться ближче одна до одної, ніж до решти точок, вони будуть схожими. Тому метод базується на відстані між двома точками. Для двовимірної задачі (може бути і у вищих вимірах), K-середніх використовує <strong>Евклідову відстань</strong> для обчислення відстані між двома заданими точками:</p>

\[dist = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}\]
<p>Літера «K» у назві означає, що буде K кластерів. K-середніх — це ітеративний алгоритм для оновлення центроїдів кластерів, доки він не досягне найкращого рішення. Розгляньмо приклад його роботи на двовимірній задачі.</p>
<p><strong>Крок 1: Випадково розмістити K центроїдів</strong></p>
<p>Перший крок K-середніх — це випадкове розміщення K центроїдів для даних, як показано на наступному малюнку, де точки даних нанесені на двовимірні ознаки. Ми не знаємо, які точки даних до якого кластера належать, тому ми розміщуємо два початкові центроїди, показані у вигляді двох трикутників.
<img alt="K-середніх" src="images/25.04.01-clustering_0.html" title="Випадковий центроїд" width="500"/></p>
<p><strong>Крок 2: Призначити точки до центроїдів</strong></p>
<p>На цьому кроці ми призначаємо точки до найближчого центроїда. Ми використовуємо вищезгаданий розрахунок відстані, щоб оцінити відстань від точки до двох центроїдів і призначити точку до найближчого з них. Ми робимо це для всіх точок даних, як показано на наступному малюнку.</p>

<p><strong>Крок 3: Оновити центроїди</strong></p>
<p>Оскільки ми маємо початкове призначення точок, у нас є два кластери. Вони не ідеальні, але ми можемо перерахувати центроїд для кожного кластера. На малюнку нижче показані новообчислені центроїди.</p>

<p><strong>Крок 4: Повторювати кроки 2 і 3, доки центроїди не перестануть рухатися</strong></p>
<p>Ми можемо ітеративно повторювати два вищевказані кроки, щоб перепризначити точки та оновити центроїди на основі перепризначених точок.</p>

<p>Цей процес триває, доки обчислені центроїди більше не змінюються. Це означає, що ми досягаємо стабільного стану, коли всі точки призначені до найближчих центроїдів, і жодна точка не змінює свою приналежність/кластер.</p>



<h2>K-середніх у Python<a href="#k-means-in-python" title="Permalink to this headline"></a></h2>
<p>Використаймо дані Iris, які ми використовували раніше, але цього разу припустимо, що ми не знаємо мітки для кожної точки даних. Тому, коли ми відображаємо точки даних без міток, це виглядає наступним чином.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>
<span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>
<span>from</span> <span>sklearn</span> <span>import</span> <span>datasets</span>
<span>plt</span><span>.</span><span>style</span><span>.</span><span>use</span><span>(</span><span>'seaborn-poster'</span><span>)</span>
<span>%</span><span>matplotlib</span> inline
</pre>





<pre><span></span><span># import the iris data</span>
<span>iris</span> <span>=</span> <span>datasets</span><span>.</span><span>load_iris</span><span>()</span>
<span># let's just use two features, so that we can </span>
<span># easily visualize them</span>
<span>X</span> <span>=</span> <span>iris</span><span>.</span><span>data</span><span>[:,</span> <span>[</span><span>0</span><span>,</span> <span>2</span><span>]]</span>
<span>y</span> <span>=</span> <span>iris</span><span>.</span><span>target</span>
<span>target_names</span> <span>=</span> <span>iris</span><span>.</span><span>target_names</span>
<span>feature_names</span> <span>=</span> <span>iris</span><span>.</span><span>feature_names</span>
<span># get the classes</span>
<span>n_class</span> <span>=</span> <span>len</span><span>(</span><span>set</span><span>(</span><span>y</span><span>))</span>

<span># let's have a look of the data first</span>
<span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span><span>8</span><span>))</span>

<span>plt</span><span>.</span><span>scatter</span><span>(</span><span>X</span><span>[:,</span> <span>0</span><span>],</span> <span>X</span><span>[:,</span> <span>1</span><span>],</span> \
            <span>color</span> <span>=</span> <span>'b'</span><span>,</span> <span>marker</span> <span>=</span> <span>'o'</span><span>,</span> <span>s</span> <span>=</span> <span>60</span><span>)</span>

<span>plt</span><span>.</span><span>xlabel</span><span>(</span><span>'Feature 1 - '</span> <span>+</span> <span>feature_names</span><span>[</span><span>0</span><span>])</span>
<span>plt</span><span>.</span><span>ylabel</span><span>(</span><span>'Feature 2 - '</span> <span>+</span> <span>feature_names</span><span>[</span><span>2</span><span>])</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter25.04-Clustering_5_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter25.04-Clustering_5_0.png"/>


<p>Тепер ми можемо використовувати K-середніх, як і раніше, тобто ініціалізувати модель і використати функцію <em>fit</em> для навчання алгоритму.</p>


<pre><span></span><span>from</span> <span>sklearn.cluster</span> <span>import</span> <span>KMeans</span>

<span>kmean</span> <span>=</span> <span>KMeans</span><span>(</span><span>n_clusters</span><span>=</span><span>3</span><span>,</span> <span>random_state</span> <span>=</span> <span>0</span><span>)</span>
<span>kmean</span><span>.</span><span>fit</span><span>(</span><span>X</span><span>)</span>
</pre>



<pre><span></span>KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
    n_clusters=3, n_init=10, n_jobs=None, precompute_distances='auto',
    random_state=0, tol=0.0001, verbose=0)
</pre>



<p>Результати знайдених кластерів зберігаються в атрибуті <em>labels_</em>, а центроїди — в <em>cluster_centers_</em>. Побудуймо графік результатів кластеризації та реальних видів на наступному малюнку. Лівий малюнок показує результати кластеризації, де більший символ позначає центроїди кластерів.</p>


<pre><span></span><span># let's have a look of the data first</span>
<span>colors</span> <span>=</span> <span>[</span><span>'b'</span><span>,</span> <span>'g'</span><span>,</span> <span>'r'</span><span>]</span>
<span>symbols</span> <span>=</span> <span>[</span><span>'o'</span><span>,</span> <span>'^'</span><span>,</span> <span>'*'</span><span>]</span>
<span>fig</span> <span>=</span> <span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span><span>8</span><span>))</span>
<span>ax</span> <span>=</span> <span>fig</span><span>.</span><span>add_subplot</span><span>(</span><span>121</span><span>)</span>
<span>ax2</span> <span>=</span> <span>fig</span><span>.</span><span>add_subplot</span><span>(</span><span>122</span><span>)</span>
<span>for</span> <span>i</span><span>,</span> <span>c</span><span>,</span> <span>s</span> <span>in</span> <span>(</span><span>zip</span><span>(</span><span>range</span><span>(</span><span>n_class</span><span>),</span> <span>colors</span><span>,</span> <span>symbols</span><span>)):</span>
    <span>ix</span> <span>=</span> <span>kmean</span><span>.</span><span>labels_</span> <span>==</span> <span>i</span>
    <span>ax</span><span>.</span><span>scatter</span><span>(</span><span>X</span><span>[:,</span> <span>0</span><span>][</span><span>ix</span><span>],</span> <span>X</span><span>[:,</span> <span>1</span><span>][</span><span>ix</span><span>],</span> \
                <span>color</span> <span>=</span> <span>c</span><span>,</span> <span>marker</span> <span>=</span> <span>s</span><span>,</span> <span>s</span> <span>=</span> <span>60</span><span>,</span> \
                <span>label</span> <span>=</span> <span>target_names</span><span>[</span><span>i</span><span>])</span>
    <span>loc</span> <span>=</span> <span>kmean</span><span>.</span><span>cluster_centers_</span><span>[</span><span>i</span><span>]</span>
    <span>ax</span><span>.</span><span>scatter</span><span>(</span><span>loc</span><span>[</span><span>0</span><span>],</span> <span>loc</span><span>[</span><span>1</span><span>],</span> <span>color</span> <span>=</span> <span>'k'</span><span>,</span> \
               <span>marker</span> <span>=</span> <span>s</span><span>,</span> <span>linewidth</span> <span>=</span> <span>5</span><span>)</span>
    
    <span>ix</span> <span>=</span> <span>y</span> <span>==</span> <span>i</span>
    <span>ax2</span><span>.</span><span>scatter</span><span>(</span><span>X</span><span>[:,</span> <span>0</span><span>][</span><span>ix</span><span>],</span> <span>X</span><span>[:,</span> <span>1</span><span>][</span><span>ix</span><span>],</span> \
                <span>color</span> <span>=</span> <span>c</span><span>,</span> <span>marker</span> <span>=</span> <span>s</span><span>,</span> <span>s</span> <span>=</span> <span>60</span><span>,</span> \
                <span>label</span> <span>=</span> <span>target_names</span><span>[</span><span>i</span><span>])</span>
    

<span>plt</span><span>.</span><span>legend</span><span>(</span><span>loc</span> <span>=</span> <span>4</span><span>,</span> <span>scatterpoints</span> <span>=</span> <span>1</span><span>)</span>
<span>ax</span><span>.</span><span>set_xlabel</span><span>(</span><span>'Feature 1 - '</span> <span>+</span> <span>feature_names</span><span>[</span><span>0</span><span>])</span>
<span>ax</span><span>.</span><span>set_ylabel</span><span>(</span><span>'Feature 2 - '</span> <span>+</span> <span>feature_names</span><span>[</span><span>2</span><span>])</span>
<span>ax2</span><span>.</span><span>set_xlabel</span><span>(</span><span>'Feature 1 - '</span> <span>+</span> <span>feature_names</span><span>[</span><span>0</span><span>])</span>
<span>ax2</span><span>.</span><span>set_ylabel</span><span>(</span><span>'Feature 2 - '</span> <span>+</span> <span>feature_names</span><span>[</span><span>2</span><span>])</span>
<span>plt</span><span>.</span><span>tight_layout</span><span>()</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter25.04-Clustering_9_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter25.04-Clustering_9_0.png"/>


<p>З наведеного вище малюнка ми бачимо, що результати непогані, вони насправді досить схожі на справжні класи. Але пам’ятайте, ми отримали ці результати без міток, лише на основі подібності між точками даних. Ми також можемо прогнозувати приналежність нових точок даних до кластерів за допомогою функції <em>predict</em>. Нижче наведено прогноз мітки кластера для двох нових точок.</p>


<pre><span></span><span>new_points</span> <span>=</span> <span>np</span><span>.</span><span>array</span><span>([[</span><span>5</span><span>,</span> <span>2</span><span>],</span>
                      <span>[</span><span>6</span><span>,</span> <span>5</span><span>]])</span>
<span>kmean</span><span>.</span><span>predict</span><span>(</span><span>new_points</span><span>)</span>
</pre>



<pre><span></span>array([0, 1], dtype=int32)
</pre>
