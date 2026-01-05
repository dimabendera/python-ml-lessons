<h1>Файли JSON<a href="#json-files" title="Постійне посилання на цей заголовок"></a></h1>
<p><strong>JSON</strong> — це ще один формат, який ми збираємося представити. Він розшифровується як <strong>JavaScript Object Notation</strong>. Файл JSON зазвичай має розширення ".json". На відміну від pickle, який залежить від Python, JSON є мовно-незалежним форматом даних, що робить його привабливим для використання. Крім того, він зазвичай займає менше місця на диску, а маніпуляції з ним швидші, ніж з pickle (якщо вам цікаво, пошукайте в Інтернеті додаткові матеріали про це). Тому це хороший варіант для зберігання ваших даних за допомогою JSON. У цьому розділі ми коротко розглянемо, як працювати з файлами JSON у Python.</p>

<h2>Формат JSON<a href="#json-format" title="Постійне посилання на цей заголовок"></a></h2>
<p>Текст у JSON формується за допомогою рядків у лапках, що містять значення в парах ключ-значення всередині {}. Це насправді дуже схоже на словник, який ми бачили в Python. Наприклад:</p>
<pre><span></span><span>{</span>
  <span>"school"</span><span>:</span> <span>"UC Berkeley"</span><span>,</span>
  <span>"address"</span><span>:</span> <span>{</span>
    <span>"city"</span><span>:</span> <span>"Berkeley"</span><span>,</span> 
    <span>"state"</span><span>:</span> <span>"California"</span><span>,</span>
    <span>"postal"</span><span>:</span> <span>"94720"</span>
  <span>},</span> 
    
  <span>"list"</span><span>:[</span>
      <span>"student 1"</span><span>,</span>
      <span>"student 2"</span><span>,</span>
      <span>"student 3"</span>
      <span>]</span>
<span>}</span>
</pre>



<h2>Запис файлу JSON<a href="#write-a-json-file" title="Постійне посилання на цей заголовок"></a></h2>
<p>У Python найпростіший спосіб роботи з JSON — це використання бібліотеки <code><span>json</span></code>. Існують й інші бібліотеки, такі як <code><span>simplejson</span></code>, <code><span>jyson</span></code> тощо. У цьому розділі ми будемо використовувати <code><span>json</span></code>, який нативно підтримується Python, для запису та завантаження файлів JSON.</p>
<p><strong>СПРОБУЙТЕ!</strong> Створіть словник і збережіть його у файл JSON на диску. Щоб використовувати pickle, спочатку потрібно імпортувати модуль.</p>


<pre><span></span><span>import</span> <span>json</span>
</pre>





<pre><span></span><span>school</span> <span>=</span> <span>{</span>
  <span>"school"</span><span>:</span> <span>"UC Berkeley"</span><span>,</span>
  <span>"address"</span><span>:</span> <span>{</span>
    <span>"city"</span><span>:</span> <span>"Berkeley"</span><span>,</span> 
    <span>"state"</span><span>:</span> <span>"California"</span><span>,</span>
    <span>"postal"</span><span>:</span> <span>"94720"</span>
  <span>},</span> 
    
  <span>"list"</span><span>:[</span>
      <span>"student 1"</span><span>,</span>
      <span>"student 2"</span><span>,</span>
      <span>"student 3"</span>
      <span>],</span>
    
  <span>"array"</span><span>:[</span><span>1</span><span>,</span> <span>2</span><span>,</span> <span>3</span><span>]</span>
<span>}</span>
<span>json</span><span>.</span><span>dump</span><span>(</span><span>school</span><span>,</span> <span>open</span><span>(</span><span>'school.json'</span><span>,</span> <span>'w'</span><span>))</span>
</pre>



<p>Щоб використовувати json для серіалізації об'єкта, ми використовуємо функцію <code><span>json.dump</span></code>, яка приймає два аргументи: перший — це об'єкт, а другий — об'єкт файлу, повернений функцією <code><span>open</span></code>. Зверніть увагу, що режим функції <code><span>open</span></code> тут 'w', що вказує на запис файлу.</p>


<h2>Читання файлу JSON<a href="#read-a-json-file" title="Постійне посилання на цей заголовок"></a></h2>
<p>Тепер завантажимо файл JSON, який ми щойно зберегли на диску, за допомогою функції <code><span>json.load</span></code>.</p>


<pre><span></span><span>my_school</span> <span>=</span> <span>json</span><span>.</span><span>load</span><span>(</span><span>open</span><span>(</span><span>'./school.json'</span><span>,</span> <span>'r'</span><span>))</span>
<span>my_school</span>
</pre>



<p>Ми бачимо, що використання <code><span>json</span></code> насправді дуже схоже на <code><span>pickle</span></code> з попереднього розділу. JSON підтримує різні типи, такі як рядки та числа, а також вкладені списки, кортежі та об'єкти; ми залишимо це для вас, щоб ви дослідили далі.</p>
