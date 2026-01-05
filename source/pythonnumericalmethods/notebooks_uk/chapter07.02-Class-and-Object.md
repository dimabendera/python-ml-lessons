<h1>Клас та Об'єкт<a href="#class-and-object" title="Постійне посилання на цей заголовок"></a></h1>
<p>У попередньому розділі було представлено два основні компоненти ООП: <strong>Клас</strong>, який є шаблоном, що використовується для визначення логічного групування даних і функцій, та <strong>Об'єкт</strong>, який є екземпляром визначеного класу з фактичними значеннями. У цьому розділі ми детальніше розглянемо обидва ці компоненти.</p>

<h2>Клас<a href="#class" title="Постійне посилання на цей заголовок"></a></h2>
<p><strong>Клас</strong> — це визначення бажаної структури. Подібно до функції, він визначається як блок коду, що починається з оператора <code>class</code>. Синтаксис визначення класу такий:</p>
<pre><span></span><span>class</span> <span>ClassName</span><span>(</span><span>superclass</span><span>):</span>
    
    <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>,</span> <span>arguments</span><span>):</span>
        <span># визначити або присвоїти атрибути об'єкта</span>
        
    <span>def</span> <span>other_methods</span><span>(</span><span>self</span><span>,</span> <span>arguments</span><span>):</span>
        <span># тіло методу</span>

</pre>

<p>Примітка: визначення класу дуже схоже на функцію. Його потрібно спочатку інстанціювати, перш ніж ви зможете його використовувати. Для назви класу стандартною конвенцією є використання "CapWords" (слова з великої літери). <strong>Суперклас</strong> використовується, коли ви хочете створити новий клас, щоб <strong>успадкувати</strong> атрибути та методи від іншого вже визначеного класу. Детальніше про <strong>успадкування</strong> ми поговоримо в наступному розділі. Метод <strong>__init__</strong> є одним із спеціальних методів у класах Python, який виконується одразу після інстанціювання (створення) об'єкта класу. Він присвоює початкові значення об'єкту, перш ніж той буде готовий до використання. Зверніть увагу на два підкреслення на початку та в кінці
<code><span>init</span></code>, що вказує на те, що це спеціальний метод, зарезервований для особливого використання в мові.
У цьому методі <code><span>init</span></code> ви можете присвоювати атрибути безпосередньо під час створення об'єкта. Функції <code><span>other_methods</span></code>
використовуються для визначення методів екземпляра, які будуть застосовуватися до атрибутів, так само як функції, які ми обговорювали раніше. Ви можете помітити, що існує параметр <code><span>self</span></code> для визначення цього методу в класі. Чому? Метод екземпляра класу повинен мати цей додатковий аргумент як перший аргумент при його визначенні. Цей конкретний аргумент посилається на сам об'єкт; зазвичай ми використовуємо <code><span>self</span></code> для його назви. Завдяки цьому параметру <code><span>self</span></code> методи екземпляра можуть вільно отримувати доступ до атрибутів та інших методів того ж об'єкта. Коли ми визначаємо або викликаємо метод екземпляра в класі, нам потрібно використовувати цей параметр <code><span>self</span></code>. Розглянемо приклад нижче.</p>
<p><strong>ПРИКЛАД:</strong> Визначте клас з назвою <code><span>Student</span></code>, з атрибутами <code><span>sid</span></code> (ідентифікатор студента), <code><span>name</span></code> (ім'я), <code><span>gender</span></code> (стать), <code><span>type</span></code> (тип) у методі <code><span>init</span></code> та методом <code><span>say_name</span></code> для виведення імені студента. Усі атрибути будуть передані, крім <code><span>type</span></code>, який матиме значення 'learning'.</p>


<pre><span></span><span>class</span> <span>Student</span><span>():</span>
    
    <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>,</span> <span>sid</span><span>,</span> <span>name</span><span>,</span> <span>gender</span><span>):</span>
        <span>self</span><span>.</span><span>sid</span> <span>=</span> <span>sid</span>
        <span>self</span><span>.</span><span>name</span> <span>=</span> <span>name</span>
        <span>self</span><span>.</span><span>gender</span> <span>=</span> <span>gender</span>
        <span>self</span><span>.</span><span>type</span> <span>=</span> <span>'learning'</span>
        
    <span>def</span> <span>say_name</span><span>(</span><span>self</span><span>):</span>
        <span>print</span><span>(</span><span>"My name is "</span> <span>+</span> <span>self</span><span>.</span><span>name</span><span>)</span>
</pre>



<p>З наведеного прикладу ми бачимо, що цей простий клас містить усі необхідні частини, згадані раніше. Метод <code><span>__init__</span></code> ініціалізує атрибути при створенні об'єкта. Нам потрібно передати початкові значення для <code><span>sid</span></code>, <code><span>name</span></code> та <code><span>gender</span></code>, тоді як атрибут <code><span>type</span></code> має фіксоване значення "learning".</p>
<p>До цих атрибутів можна отримати доступ з усіх інших методів, визначених у класі, за допомогою <code><span>self.attribute</span></code>, наприклад, у методі <code><span>say_name</span></code> ми можемо використовувати атрибут <code><span>name</span></code> за допомогою <code><span>self.name</span></code>. Методи, визначені в класі, також можуть бути доступні та використані в інших методах за допомогою <code><span>self.method</span></code>. Розглянемо наступний приклад.</p>
<p><strong>СПРОБУЙТЕ!</strong> Додайте метод <strong>report</strong>, який виводить не лише ім'я студента, а й ідентифікатор студента. Метод матиме ще один аргумент <em>score</em> (оцінка), який передаватиме число від 0 до 100 як частину звіту.</p>


<pre><span></span><span>class</span> <span>Student</span><span>():</span>
    
    <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>,</span> <span>sid</span><span>,</span> <span>name</span><span>,</span> <span>gender</span><span>):</span>
        <span>self</span><span>.</span><span>sid</span> <span>=</span> <span>sid</span>
        <span>self</span><span>.</span><span>name</span> <span>=</span> <span>name</span>
        <span>self</span><span>.</span><span>gender</span> <span>=</span> <span>gender</span>
        <span>self</span><span>.</span><span>type</span> <span>=</span> <span>'learning'</span>
        
    <span>def</span> <span>say_name</span><span>(</span><span>self</span><span>):</span>
        <span>print</span><span>(</span><span>"My name is "</span> <span>+</span> <span>self</span><span>.</span><span>name</span><span>)</span>
        
    <span>def</span> <span>report</span><span>(</span><span>self</span><span>,</span> <span>score</span><span>):</span>
        <span>self</span><span>.</span><span>say_name</span><span>()</span>
        <span>print</span><span>(</span><span>"My id is: "</span> <span>+</span> <span>self</span><span>.</span><span>sid</span><span>)</span>
        <span>print</span><span>(</span><span>"My score is: "</span> <span>+</span> <span>str</span><span>(</span><span>score</span><span>))</span>
</pre>





<h2>Об'єкт<a href="#object" title="Постійне посилання на цей заголовок"></a></h2>
<p>Як згадувалося раніше, <strong>об'єкт</strong> — це екземпляр визначеного класу з фактичними значеннями. Ми можемо мати багато екземплярів з різними значеннями, пов'язаними з класом, і кожен з цих екземплярів буде незалежним один від одного, як ми бачили раніше. Також, після створення об'єкта та виклику цього методу екземпляра з об'єкта, нам не потрібно надавати значення параметру <code><span>self</span></code>, оскільки Python автоматично його надає. Дивіться наступний приклад:</p>
<p><strong>ПРИКЛАД:</strong> Створіть два об'єкти ("001", "Susan", "F") та ("002", "Mike", "M") і викличте метод <em>say_name</em>.</p>


<pre><span></span><span>student1</span> <span>=</span> <span>Student</span><span>(</span><span>"001"</span><span>,</span> <span>"Susan"</span><span>,</span> <span>"F"</span><span>)</span>
<span>student2</span> <span>=</span> <span>Student</span><span>(</span><span>"002"</span><span>,</span> <span>"Mike"</span><span>,</span> <span>"M"</span><span>)</span>

<span>student1</span><span>.</span><span>say_name</span><span>()</span>
<span>student2</span><span>.</span><span>say_name</span><span>()</span>
<span>print</span><span>(</span><span>student1</span><span>.</span><span>type</span><span>)</span>
<span>print</span><span>(</span><span>student1</span><span>.</span><span>gender</span><span>)</span>
</pre>



<pre><span></span>My name is Susan
My name is Mike
learning
F
</pre>



<p>У наведеному вище коді ми створили два об'єкти, <code><span>student1</span></code> та <code><span>student2</span></code>, з двома різними наборами значень. Кожен об'єкт є екземпляром класу <code><span>Student</span></code> і має різний набір атрибутів. Введіть <code><span>student1.+TAB</span></code>, щоб побачити визначені атрибути та методи. Щоб отримати доступ до одного атрибута, введіть <code><span>object.attribute</span></code>, наприклад, <code><span>student1.type</span></code>. На відміну від цього, для виклику методу потрібні дужки, оскільки ви викликаєте функцію, наприклад, <code><span>student1.say_name()</span></code>.</p>
<p><strong>СПРОБУЙТЕ!</strong> Викличте метод <em>report</em> для student1 та student2 з оцінками 95 та 90 відповідно. Примітка: тут нам не потрібен "self" як аргумент.</p>


<pre><span></span><span>student1</span><span>.</span><span>report</span><span>(</span><span>95</span><span>)</span>
<span>student2</span><span>.</span><span>report</span><span>(</span><span>90</span><span>)</span>
</pre>



<pre><span></span>My name is Susan
My id is: 001
My score is: 95
My name is Mike
My id is: 002
My score is: 90
</pre>



<p>Ми бачимо, що обидва методи викликаються для виведення даних, пов'язаних з двома об'єктами. Примітка: значення оцінки, яке ми передали, доступне лише методу <code><span>report</span></code> (в межах області дії цього методу). Ми також бачимо, що виклик методу <code><span>say_name</span></code> у методі <code><span>report</span></code> також працює, якщо ви викликаєте метод з <code><span>self</span></code>.</p>


<h2>Атрибути класу проти атрибутів екземпляра<a href="#class-vs-instance-attributes" title="Постійне посилання на цей заголовок"></a></h2>
<p>Атрибути, які ми представили вище, насправді називаються атрибутами екземпляра, що означає, що вони належать лише до конкретного екземпляра; при їх використанні вам потрібно використовувати <code><span>self.attribute</span></code> всередині класу. Існує інший тип атрибутів, які називаються атрибутами класу, і вони будуть спільними для всіх екземплярів, створених з цього класу. Розглянемо приклад того, як визначити та використовувати атрибут класу.</p>
<p><strong>ПРИКЛАД:</strong> Змініть клас <code><span>Student</span></code>, щоб додати атрибут класу <code><span>n_instances</span></code>, який буде записувати, скільки об'єктів ми створюємо. Також додайте метод <code><span>num_instances</span></code> для виведення цього числа.</p>


<pre><span></span><span>class</span> <span>Student</span><span>():</span>
    
    <span>n_instances</span> <span>=</span> <span>0</span>
    
    <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>,</span> <span>sid</span><span>,</span> <span>name</span><span>,</span> <span>gender</span><span>):</span>
        <span>self</span><span>.</span><span>sid</span> <span>=</span> <span>sid</span>
        <span>self</span><span>.</span><span>name</span> <span>=</span> <span>name</span>
        <span>self</span><span>.</span><span>gender</span> <span>=</span> <span>gender</span>
        <span>self</span><span>.</span><span>type</span> <span>=</span> <span>'learning'</span>
        <span>Student</span><span>.</span><span>n_instances</span> <span>+=</span> <span>1</span>
        
    <span>def</span> <span>say_name</span><span>(</span><span>self</span><span>):</span>
        <span>print</span><span>(</span><span>"My name is "</span> <span>+</span> <span>self</span><span>.</span><span>name</span><span>)</span>
        
    <span>def</span> <span>report</span><span>(</span><span>self</span><span>,</span> <span>score</span><span>):</span>
        <span>self</span><span>.</span><span>say_name</span><span>()</span>
        <span>print</span><span>(</span><span>"My id is: "</span> <span>+</span> <span>self</span><span>.</span><span>sid</span><span>)</span>
        <span>print</span><span>(</span><span>"My score is: "</span> <span>+</span> <span>str</span><span>(</span><span>score</span><span>))</span>
        
    <span>def</span> <span>num_instances</span><span>(</span><span>self</span><span>):</span>
        <span>print</span><span>(</span><span>f</span><span>'We have </span><span>{</span><span>Student</span><span>.</span><span>n_instances</span><span>}</span><span>-instance in total'</span><span>)</span>
</pre>



<p>При визначенні атрибута класу ми повинні визначити його поза всіма іншими методами <code><span>без</span></code> використання <code><span>self</span></code>. Щоб використовувати атрибути класу, ми використовуємо <code><span>ClassName.attribute</span></code>, що в цьому випадку є <code><span>Student.n_instances</span></code>. Цей атрибут буде спільним для всіх екземплярів, створених з цього класу. Розглянемо наступний код, щоб продемонструвати цю ідею.</p>


<pre><span></span><span>student1</span> <span>=</span> <span>Student</span><span>(</span><span>"001"</span><span>,</span> <span>"Susan"</span><span>,</span> <span>"F"</span><span>)</span>
<span>student1</span><span>.</span><span>num_instances</span><span>()</span>
<span>student2</span> <span>=</span> <span>Student</span><span>(</span><span>"002"</span><span>,</span> <span>"Mike"</span><span>,</span> <span>"M"</span><span>)</span>
<span>student1</span><span>.</span><span>num_instances</span><span>()</span>
<span>student2</span><span>.</span><span>num_instances</span><span>()</span>
</pre>



<pre><span></span>We have 1-instance in total
We have 2-instance in total
We have 2-instance in total
</pre>



<p>Як і раніше, ми створили два об'єкти, атрибути екземпляра <code><span>sid</span></code>, <code><span>name</span></code>, але <code><span>gender</span></code> належить лише до конкретного об'єкта. Наприклад, <code><span>student1.name</span></code> — "Susan", а <code><span>student2.name</span></code> — "Mike". Але коли ми виводимо атрибут класу <code><span>Student.n_instances</span></code> після створення об'єкта <code><span>student2</span></code>, значення в <code><span>student1</span></code> також змінюється. Це те, чого ми очікуємо від атрибута класу, оскільки він є спільним для всіх створених об'єктів.</p>
<p>Тепер, коли ми розуміємо різницю між класом та екземпляром, ми готові використовувати базове ООП у Python. Перш ніж ми зможемо повною мірою скористатися перевагами ООП, нам все ще потрібно зрозуміти концепції успадкування, інкапсуляції та поліморфізму. Перейдемо до наступного розділу!</p>
