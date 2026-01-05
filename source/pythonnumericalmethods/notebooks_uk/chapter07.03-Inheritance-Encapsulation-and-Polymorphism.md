```html
<h1>Успадкування, інкапсуляція та поліморфізм<a href="#inheritance-encapsulation-and-polymorphism" title="Permalink to this headline"></a></h1>
<p>Ми вже бачили потужність моделювання ООП за допомогою класів та об'єктів, поєднуючи дані та методи. Існують ще три важливі концепції: <strong>успадкування</strong>, яке робить код ООП більш модульним, легшим для повторного використання та побудови зв'язків між класами. <strong>Інкапсуляція</strong> може приховувати деякі приватні деталі класу від інших об'єктів, тоді як <strong>поліморфізм</strong> дозволяє нам використовувати спільну операцію різними способами. У цьому розділі ми коротко їх обговоримо.</p>

<h2>Успадкування<a href="#inheritance" title="Permalink to this headline"></a></h2>
<p>Успадкування дозволяє нам визначити клас, який успадковує всі методи та атрибути від іншого класу. За угодою, новий клас називається <strong>дочірнім класом</strong>, а той, від якого він успадковує, називається <strong>батьківським класом</strong> або <strong>суперкласом</strong>. Якщо ми повернемося до визначення структури класу, то побачимо, що структура для базового успадкування — це <strong>class ClassName(superclass)</strong>, що означає, що новий клас може отримати доступ до всіх атрибутів та методів суперкласу. Успадкування будує зв'язок між дочірнім та батьківським класами, зазвичай таким чином, що батьківський клас є загальним типом, а дочірній — специфічним. Спробуймо розглянути приклад.</p>
<p><strong>СПРОБУЙТЕ!</strong> Визначте клас з назвою <code><span>Sensor</span></code> з атрибутами <code><span>name</span></code>, <code><span>location</span></code> та <code><span>record_date</span></code>, які передаються при створенні об'єкта, та атрибутом <code><span>data</span></code> як порожнім словником для зберігання даних. Створіть один метод <em>add_data</em> з вхідними параметрами <code><span>t</span></code> та <code><span>data</span></code> для прийому часових міток та масивів даних. У цьому методі присвойте <code><span>t</span></code> та <code><span>data</span></code> атрибуту <code><span>data</span></code> з ключами ‘time` та ‘data`. Крім того, він повинен мати один метод <code><span>clear_data</span></code> для видалення даних.</p>


<pre><span></span><span>class</span> <span>Sensor</span><span>():</span>
    <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>,</span> <span>name</span><span>,</span> <span>location</span><span>,</span> <span>record_date</span><span>):</span>
        <span>self</span><span>.</span><span>name</span> <span>=</span> <span>name</span>
        <span>self</span><span>.</span><span>location</span> <span>=</span> <span>location</span>
        <span>self</span><span>.</span><span>record_date</span> <span>=</span> <span>record_date</span>
        <span>self</span><span>.</span><span>data</span> <span>=</span> <span>{}</span>
        
    <span>def</span> <span>add_data</span><span>(</span><span>self</span><span>,</span> <span>t</span><span>,</span> <span>data</span><span>):</span>
        <span>self</span><span>.</span><span>data</span><span>[</span><span>'time'</span><span>]</span> <span>=</span> <span>t</span>
        <span>self</span><span>.</span><span>data</span><span>[</span><span>'data'</span><span>]</span> <span>=</span> <span>data</span>
        <span>print</span><span>(</span><span>f</span><span>'Збережено </span><span>{</span><span>len</span><span>(</span><span>data</span><span>)</span><span>}</span><span> точок'</span><span>)</span>        
        
    <span>def</span> <span>clear_data</span><span>(</span><span>self</span><span>):</span>
        <span>self</span><span>.</span><span>data</span> <span>=</span> <span>{}</span>
        <span>print</span><span>(</span><span>'Дані очищено!'</span><span>)</span>
</pre>



<p>Тепер, коли у нас є клас для зберігання загальної інформації про сенсор, ми можемо створити об'єкт сенсора для зберігання деяких даних.</p>
<p><strong>ПРИКЛАД:</strong> Створіть об'єкт сенсора.</p>


<pre><span></span><span>import</span> <span>numpy</span> <span>as</span> <span>np</span>

<span>sensor1</span> <span>=</span> <span>Sensor</span><span>(</span><span>'sensor1'</span><span>,</span> <span>'Berkeley'</span><span>,</span> <span>'2019-01-01'</span><span>)</span>
<span>data</span> <span>=</span> <span>np</span><span>.</span><span>random</span><span>.</span><span>randint</span><span>(</span><span>-</span><span>10</span><span>,</span> <span>10</span><span>,</span> <span>10</span><span>)</span>
<span>sensor1</span><span>.</span><span>add_data</span><span>(</span><span>np</span><span>.</span><span>arange</span><span>(</span><span>10</span><span>),</span> <span>data</span><span>)</span>
<span>sensor1</span><span>.</span><span>data</span>
</pre>



<pre><span></span>Збережено 10 точок
</pre>

<pre><span></span>{'time': array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
 'data': array([-4, -7,  2, -3, -8,  6,  4,  3,  5, -9])}
</pre>




<h3>Успадкування та розширення новим методом<a href="#inherit-and-extend-new-method" title="Permalink to this headline"></a></h3>
<p>Припустимо, у нас є інший тип сенсора: акселерометр. Він має ті ж атрибути та методи, що й клас <code><span>Sensor</span></code>, але також має інші атрибути або методи, які потрібно додати або змінити порівняно з оригінальним класом. Що нам робити? Створювати інший клас з нуля? Саме тут успадкування може полегшити життя. Цей новий клас успадкує від класу <code><span>Sensor</span></code> усі атрибути та методи. Ми можемо вирішити, чи хочемо ми розширити атрибути або методи. Давайте спочатку створимо цей новий клас, <code><span>Accelerometer</span></code>, і додамо новий метод, <code><span>show_type</span></code>, щоб повідомляти, який це тип сенсора.</p>


<pre><span></span><span>class</span> <span>Accelerometer</span><span>(</span><span>Sensor</span><span>):</span>
    
    <span>def</span> <span>show_type</span><span>(</span><span>self</span><span>):</span>
        <span>print</span><span>(</span><span>'Я акселерометр!'</span><span>)</span>
        
<span>acc</span> <span>=</span> <span>Accelerometer</span><span>(</span><span>'acc1'</span><span>,</span> <span>'Oakland'</span><span>,</span> <span>'2019-02-01'</span><span>)</span>
<span>acc</span><span>.</span><span>show_type</span><span>()</span>
<span>data</span> <span>=</span> <span>np</span><span>.</span><span>random</span><span>.</span><span>randint</span><span>(</span><span>-</span><span>10</span><span>,</span> <span>10</span><span>,</span> <span>10</span><span>)</span>
<span>acc</span><span>.</span><span>add_data</span><span>(</span><span>np</span><span>.</span><span>arange</span><span>(</span><span>10</span><span>),</span> <span>data</span><span>)</span>
<span>acc</span><span>.</span><span>data</span>
</pre>



<pre><span></span>Я акселерометр!
Збережено 10 точок
</pre>

<pre><span></span>{'time': array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
 'data': array([ -2,   2, -10,   6,   2,  -8,   2,   3,   7,  -6])}
</pre>



<p>Створення цього нового класу <code><span>Accelerometer</span></code> дуже просте. Ми успадковуємо від <code><span>Sensor</span></code> (позначеного як суперклас), і новий клас фактично містить усі атрибути та методи суперкласу. Потім ми додаємо новий метод, <code><span>show_type</span></code>, якого немає в класі <code><span>Sensor</span></code>, але ми можемо успішно розширити дочірній клас, додавши новий метод. Це демонструє силу успадкування: ми повторно використали більшу частину класу <code><span>Sensor</span></code> у новому класі та розширили його функціональність. Крім того, успадкування встановлює логічний зв'язок для моделювання сутностей реального світу: клас <code><span>Sensor</span></code> як батьківський клас є більш загальним і передає всі характеристики дочірньому класу <code><span>Accelerometer</span></code>.</p>


<h3>Успадкування та перевизначення методів<a href="#inherit-and-method-overriding" title="Permalink to this headline"></a></h3>
<p>Коли ми успадковуємо від батьківського класу, ми можемо змінити реалізацію методу, наданого батьківським класом, це називається перевизначенням методу. Розглянемо наступний приклад.</p>
<p><strong>ПРИКЛАД:</strong> Створіть клас <code><span>UCBAcc</span></code> (специфічний тип акселерометра, створений в Університеті Каліфорнії в Берклі), який успадковує від <code><span>Accelerometer</span></code>, але замінює метод <code><span>show_type</span></code>, щоб він виводив назву сенсора.</p>


<pre><span></span><span>class</span> <span>UCBAcc</span><span>(</span><span>Accelerometer</span><span>):</span>
    
    <span>def</span> <span>show_type</span><span>(</span><span>self</span><span>):</span>
        <span>print</span><span>(</span><span>f</span><span>'Я </span><span>{</span><span>self</span><span>.</span><span>name</span><span>}</span><span>, створений в Університеті Каліфорнії в Берклі!'</span><span>)</span>
        
<span>acc_ucb</span> <span>=</span> <span>UCBAcc</span><span>(</span><span>'UCBAcc'</span><span>,</span> <span>'Berkeley'</span><span>,</span> <span>'2019-03-01'</span><span>)</span>
<span>acc_ucb</span><span>.</span><span>show_type</span><span>()</span>
</pre>



<pre><span></span>Я UCBAcc, створений в Університеті Каліфорнії в Берклі!
</pre>



<p>Ми бачимо, що наш новий клас <code><span>UCBAcc</span></code> фактично перевизначає метод <code><span>show_type</span></code> з новими можливостями. У цьому прикладі ми не тільки успадковуємо властивості від нашого батьківського класу, але й модифікуємо/покращуємо деякі методи.</p>


<h3>Успадкування та оновлення атрибутів за допомогою super<a href="#inherit-and-update-attributes-with-super" title="Permalink to this headline"></a></h3>
<p>Давайте створимо клас <code><span>NewSensor</span></code>, який успадковує від класу <code><span>Sensor</span></code>, але з оновленими атрибутами шляхом додавання нового атрибута <code><span>brand</span></code>. Звичайно, ми можемо перевизначити весь метод <code><span>__init__</span></code>, як показано нижче, і перевизначити батьківську функцію.</p>


<pre><span></span><span>class</span> <span>NewSensor</span><span>(</span><span>Sensor</span><span>):</span>
    <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>,</span> <span>name</span><span>,</span> <span>location</span><span>,</span> <span>record_date</span><span>,</span> <span>brand</span><span>):</span>
        <span>self</span><span>.</span><span>name</span> <span>=</span> <span>name</span>
        <span>self</span><span>.</span><span>location</span> <span>=</span> <span>location</span>
        <span>self</span><span>.</span><span>record_date</span> <span>=</span> <span>record_date</span>
        <span>self</span><span>.</span><span>brand</span> <span>=</span> <span>brand</span>
        <span>self</span><span>.</span><span>data</span> <span>=</span> <span>{}</span>
        
<span>new_sensor</span> <span>=</span> <span>NewSensor</span><span>(</span><span>'OK'</span><span>,</span> <span>'SF'</span><span>,</span> <span>'2019-03-01'</span><span>,</span> <span>'XYZ'</span><span>)</span>
<span>new_sensor</span><span>.</span><span>brand</span>
</pre>



<pre><span></span>'XYZ'
</pre>



<p>Однак, є кращий спосіб досягти того ж самого. Ми можемо використовувати метод <code><span>super</span></code>, щоб уникнути явного посилання на батьківський клас. Давайте подивимося, як це зробити, на наступному прикладі:</p>
<p><strong>ПРИКЛАД:</strong> Перевизначте атрибути при успадкуванні.</p>


<pre><span></span><span>class</span> <span>NewSensor</span><span>(</span><span>Sensor</span><span>):</span>
    <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>,</span> <span>name</span><span>,</span> <span>location</span><span>,</span> <span>record_date</span><span>,</span> <span>brand</span><span>):</span>
        <span>super</span><span>()</span><span>.</span><span>__init__</span><span>(</span><span>name</span><span>,</span> <span>location</span><span>,</span> <span>record_date</span><span>)</span>
        <span>self</span><span>.</span><span>brand</span> <span>=</span> <span>brand</span>
        
<span>new_sensor</span> <span>=</span> <span>NewSensor</span><span>(</span><span>'OK'</span><span>,</span> <span>'SF'</span><span>,</span> <span>'2019-03-01'</span><span>,</span> <span>'XYZ'</span><span>)</span>
<span>new_sensor</span><span>.</span><span>brand</span>
</pre>



<pre><span></span>'XYZ'
</pre>



<p>Тепер ми бачимо, що з методом <em>super</em> ми уникаємо перелічення всіх визначень атрибутів, що допомагає підтримувати ваш код у майбутньому. Але це особливо корисно, коли ви використовуєте множинне успадкування, що виходить за рамки нашого обговорення.</p>



<h2>Інкапсуляція<a href="#encapsulation" title="Permalink to this headline"></a></h2>
<p><strong>Інкапсуляція</strong> — одна з фундаментальних концепцій в ООП. Вона описує ідею обмеження доступу до методів та атрибутів у класі. Це приховує складні деталі від користувачів і запобігає випадковій зміні даних. У Python це досягається за допомогою приватних методів або атрибутів з використанням підкреслення як префікса, тобто одинарного "_" або подвійного "__". Розглянемо наступний приклад.</p>
<p><strong>ПРИКЛАД:</strong></p>


<pre><span></span><span>class</span> <span>Sensor</span><span>():</span>
    <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>,</span> <span>name</span><span>,</span> <span>location</span><span>):</span>
        <span>self</span><span>.</span><span>name</span> <span>=</span> <span>name</span>
        <span>self</span><span>.</span><span>_location</span> <span>=</span> <span>location</span>
        <span>self</span><span>.</span><span>__version</span> <span>=</span> <span>'1.0'</span>
    
    <span># функція getter</span>
    <span>def</span> <span>get_version</span><span>(</span><span>self</span><span>):</span>
        <span>print</span><span>(</span><span>f</span><span>'Версія сенсора </span><span>{</span><span>self</span><span>.</span><span>__version</span><span>}</span><span>'</span><span>)</span>
    
    <span># функція setter</span>
    <span>def</span> <span>set_version</span><span>(</span><span>self</span><span>,</span> <span>version</span><span>):</span>
        <span>self</span><span>.</span><span>__version</span> <span>=</span> <span>version</span>
</pre>





<pre><span></span><span>sensor1</span> <span>=</span> <span>Sensor</span><span>(</span><span>'Acc'</span><span>,</span> <span>'Berkeley'</span><span>)</span>
<span>print</span><span>(</span><span>sensor1</span><span>.</span><span>name</span><span>)</span>
<span>print</span><span>(</span><span>sensor1</span><span>.</span><span>_location</span><span>)</span>
<span>print</span><span>(</span><span>sensor1</span><span>.</span><span>__version</span><span>)</span>
</pre>



<pre><span></span>Acc
Berkeley
</pre>

<pre><span></span><span>---------------------------------------------------------------------------</span>
<span>AttributeError</span><span>                            </span>Traceback (most recent call last)
<span>&lt;</span><span>ipython</span><span>-</span><span>input</span><span>-</span><span>8</span><span>-</span><span>ca9b481690ba</span><span>&gt;</span> <span>in</span> <span>&lt;</span><span>module</span><span>&gt;</span>
<span>      </span><span>2</span> <span>print</span><span>(</span><span>sensor1</span><span>.</span><span>name</span><span>)</span>
<span>      </span><span>3</span> <span>print</span><span>(</span><span>sensor1</span><span>.</span><span>_location</span><span>)</span>
<span>----&gt; </span><span>4</span> <span>print</span><span>(</span><span>sensor1</span><span>.</span><span>__version</span><span>)</span>

<span>AttributeError</span>: 'Sensor' object has no attribute '__version'
</pre>



<p>Наведений вище приклад показує, як працює інкапсуляція. За допомогою одного підкреслення ми визначили приватну змінну, і до неї не слід звертатися напряму. Але це лише угода, ніщо не заважає вам це робити. Ви все ще можете отримати до неї доступ, якщо захочете. З подвійним підкресленням ми бачимо, що до атрибута <code><span>__version</span></code> не можна отримати доступ або змінити його напряму. Тому, щоб отримати доступ до атрибутів з подвійним підкресленням, нам потрібно використовувати функції getter та setter для доступу до них внутрішньо, як показано в наступному прикладі.</p>


<pre><span></span><span>sensor1</span><span>.</span><span>get_version</span><span>()</span>
</pre>



<pre><span></span>Версія сенсора 1.0
</pre>





<pre><span></span><span>sensor1</span><span>.</span><span>set_version</span><span>(</span><span>'2.0'</span><span>)</span>
<span>sensor1</span><span>.</span><span>get_version</span><span>()</span>
</pre>



<pre><span></span>Версія сенсора 2.0
</pre>



<p>Одинарне та подвійне підкреслення також застосовуються до приватних методів, ми не будемо їх обговорювати, оскільки вони схожі на приватні атрибути.</p>


<h2>Поліморфізм<a href="#polymorphism" title="Permalink to this headline"></a></h2>
<p><strong>Поліморфізм</strong> — ще одна фундаментальна концепція в ООП, що означає "багато форм". Поліморфізм дозволяє нам використовувати єдиний інтерфейс з різними базовими формами, такими як типи даних або класи. Наприклад, ми можемо мати методи з однаковими назвами в різних класах або дочірніх класах. Ми вже бачили один приклад вище, коли перевизначали метод <code><span>show_type</span></code> у класі <code><span>UCBAcc</span></code>. І батьківський клас <code><span>Accelerometer</span></code>, і дочірній клас <code><span>UCBAcc</span></code> мають метод з назвою <code><span>show_type</span></code>, але вони мають різну реалізацію. Ця здатність використовувати одну назву з багатьма формами, що діють по-різному в різних ситуаціях, значно зменшує складність. Ми не будемо детальніше обговорювати поліморфізм; якщо вам цікаво, пошукайте більше інформації в Інтернеті для глибшого розуміння.</p>
```
