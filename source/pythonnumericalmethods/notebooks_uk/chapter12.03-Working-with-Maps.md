<h1>Робота з картами<a href="#working-with-maps" title="Постійне посилання на цей заголовок"></a></h1>
<p>В інженерії та науці часто доводиться взаємодіяти з картами. Існує багато різних пакетів Python, які можуть малювати карти, наприклад, <a href="https://matplotlib.org/basemap/">basemap</a>, <a href="https://scitools.org.uk/cartopy/docs/latest/">cartopy</a>, <a href="https://github.com/python-visualization/folium">folium</a> тощо. Пакет <em>folium</em> дозволяє створювати інтерактивні карти для веб-сторінок. Але найчастіше нам потрібно лише побудувати статичну карту, щоб показати деякі просторові особливості, і для цього підійдуть <em>basemap</em> та <em>cartopy</em>. У минулому <em>basemap</em> був офіційним картографічним пакетом, що йшов разом з <em>matplotlib</em>, але з 2016 року було оголошено, що <em>cartopy</em> замінить <em>basemap</em>. Тому в цьому розділі ми коротко познайомимо вас з тим, як малювати карти з даними за допомогою <em>cartopy</em>. Вам потрібно встановити <em>cartopy</em> за допомогою команди <em>conda install cartopy</em>.</p>
<p>Основи карти прості: це 2D-графік з певними <a href="https://en.wikipedia.org/wiki/Map_projection">проєкціями</a>. Вісь X — це довгота в діапазоні від -180 до 180, яка визначає положення точки на поверхні Землі зі сходу на захід. Вісь Y — це широта в діапазоні від -90 до 90, яка описує положення точки з півдня на північ. Якщо ви вкажете пару широти та довготи, ми зможемо однозначно визначити, де знаходиться точка на Землі.</p>
<p><em>cartopy</em> має дуже хороший API для взаємодії з <em>matplotlib</em>. Щоб побудувати карту, нам потрібно лише вказати <em>matplotlib</em> використовувати певну картографічну проєкцію, а потім ми можемо додати до графіка інші елементи карти.</p>
<p><strong>СПРОБУЙТЕ!</strong> Побудуйте карту світу за допомогою <em>cartopy</em>, використовуючи проєкцію Plate Carrée (погугліть), і нанесіть на карту берегову лінію.</p>


<pre><span></span><span>import</span> <span>cartopy.crs</span> <span>as</span> <span>ccrs</span>
<span>import</span> <span>matplotlib.pyplot</span> <span>as</span> <span>plt</span>
<span>%</span><span>matplotlib</span> inline
</pre>





<pre><span></span><span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>12</span><span>,</span> <span>8</span><span>))</span>
<span>ax</span> <span>=</span> <span>plt</span><span>.</span><span>axes</span><span>(</span><span>projection</span><span>=</span><span>ccrs</span><span>.</span><span>PlateCarree</span><span>())</span>
<span>ax</span><span>.</span><span>coastlines</span><span>()</span>
<span>ax</span><span>.</span><span>gridlines</span><span>(</span><span>draw_labels</span><span>=</span><span>True</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.03-Working-with-Maps_5_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.03-Working-with-Maps_5_0.png"/>


<p>У наведеному вище прикладі ми побудували карту з проєкцією Plate Carrée, ви можете ознайомитися з іншими <a href="https://scitools.org.uk/cartopy/docs/v0.16/crs/projections.html#cartopy-projections">проєкціями, що підтримуються cartopy</a>. Також ми увімкнули лінії сітки та нанесли на карту підписи.</p>
<p>Фон карти, який ми намалювали вище, не дуже гарний. Ми можемо легко додати гарний фон карти в cartopy. Зауважте, що на момент написання статті <em>stock_img</em> має лише одне зображення зі зменшеної версії растру затіненого рельєфу Natural Earth.</p>


<pre><span></span><span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>12</span><span>,</span> <span>8</span><span>))</span>
<span>ax</span> <span>=</span> <span>plt</span><span>.</span><span>axes</span><span>(</span><span>projection</span><span>=</span><span>ccrs</span><span>.</span><span>PlateCarree</span><span>())</span>
<span>ax</span><span>.</span><span>coastlines</span><span>()</span>
<span>ax</span><span>.</span><span>stock_img</span><span>()</span>
<span>ax</span><span>.</span><span>gridlines</span><span>(</span><span>draw_labels</span><span>=</span><span>True</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.03-Working-with-Maps_7_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.03-Working-with-Maps_7_0.png"/>


<p>Звісно, ми можемо збільшити масштаб карти до будь-якого місця на Землі за допомогою функції <em>ax.set_extent</em>, яка приймає список, де перші два числа є межами осі X, а останні два — межами осі Y.</p>
<p><strong>СПРОБУЙТЕ!</strong> Збільште масштаб карти до США.</p>


<pre><span></span><span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span> <span>5</span><span>))</span>
<span>ax</span> <span>=</span> <span>plt</span><span>.</span><span>axes</span><span>(</span><span>projection</span><span>=</span><span>ccrs</span><span>.</span><span>PlateCarree</span><span>())</span>
<span>ax</span><span>.</span><span>coastlines</span><span>()</span>
<span>ax</span><span>.</span><span>set_extent</span><span>([</span><span>-</span><span>125</span><span>,</span> <span>-</span><span>75</span><span>,</span> <span>25</span><span>,</span> <span>50</span><span>])</span>
<span>ax</span><span>.</span><span>gridlines</span><span>(</span><span>draw_labels</span><span>=</span><span>True</span><span>)</span>
<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.03-Working-with-Maps_9_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.03-Working-with-Maps_9_0.png"/>


<p>Ми помічаємо, що на карту не додано жодних об'єктів, таких як кордони країн, межі штатів, озера/вода тощо. У cartopy всі ці об'єкти потрібно додавати окремо.</p>
<p><strong>СПРОБУЙТЕ!</strong> Для карти США, яку ми створили вище, додайте об'єкти: суходіл, океан, штати та кордони країн, озера та річки.</p>


<pre><span></span><span>import</span> <span>cartopy.feature</span> <span>as</span> <span>cfeature</span>
</pre>





<pre><span></span><span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span> <span>5</span><span>))</span>
<span>ax</span> <span>=</span> <span>plt</span><span>.</span><span>axes</span><span>(</span><span>projection</span><span>=</span><span>ccrs</span><span>.</span><span>PlateCarree</span><span>())</span>
<span>ax</span><span>.</span><span>coastlines</span><span>()</span>
<span>ax</span><span>.</span><span>set_extent</span><span>([</span><span>-</span><span>125</span><span>,</span> <span>-</span><span>75</span><span>,</span> <span>25</span><span>,</span> <span>50</span><span>])</span>

<span>ax</span><span>.</span><span>add_feature</span><span>(</span><span>cfeature</span><span>.</span><span>LAND</span><span>)</span>
<span>ax</span><span>.</span><span>add_feature</span><span>(</span><span>cfeature</span><span>.</span><span>OCEAN</span><span>)</span>
<span>ax</span><span>.</span><span>add_feature</span><span>(</span><span>cfeature</span><span>.</span><span>STATES</span><span>,</span> <span>linestyle</span><span>=</span><span>':'</span><span>)</span>
<span>ax</span><span>.</span><span>add_feature</span><span>(</span><span>cfeature</span><span>.</span><span>BORDERS</span><span>)</span>
<span>ax</span><span>.</span><span>add_feature</span><span>(</span><span>cfeature</span><span>.</span><span>LAKES</span><span>,</span> <span>alpha</span><span>=</span><span>0.5</span><span>)</span>
<span>ax</span><span>.</span><span>add_feature</span><span>(</span><span>cfeature</span><span>.</span><span>RIVERS</span><span>)</span>

<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.03-Working-with-Maps_12_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.03-Working-with-Maps_12_0.png"/>


<p>Ми можемо збільшити масштаб до меншої області, але тоді нам потрібно завантажити та використовувати берегові лінії та суходіл високої роздільної здатності, щоб отримати гарну карту.</p>
<p><strong>СПРОБУЙТЕ!</strong> Побудуйте карту затоки Сан-Франциско з береговими лініями та суходолом з роздільною здатністю 10 м. Спробуйте змінити один з них на 50 м і подивіться, що станеться.</p>


<pre><span></span><span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span> <span>8</span><span>))</span>
<span>ax</span> <span>=</span> <span>plt</span><span>.</span><span>axes</span><span>(</span><span>projection</span><span>=</span><span>ccrs</span><span>.</span><span>PlateCarree</span><span>())</span>
<span>ax</span><span>.</span><span>coastlines</span><span>(</span><span>resolution</span><span>=</span><span>'10m'</span><span>)</span>
<span>ax</span><span>.</span><span>set_extent</span><span>([</span><span>-</span><span>122.8</span><span>,</span> <span>-</span><span>122</span><span>,</span> <span>37.3</span><span>,</span> <span>38.3</span><span>])</span>

<span># we can add high-resolution land</span>
<span>LAND</span> <span>=</span> <span>cfeature</span><span>.</span><span>NaturalEarthFeature</span><span>(</span><span>'physical'</span><span>,</span> <span>'land'</span><span>,</span> <span>'10m'</span><span>,</span>
                                        <span>edgecolor</span><span>=</span><span>'face'</span><span>,</span>
                                        <span>facecolor</span><span>=</span><span>cfeature</span><span>.</span><span>COLORS</span><span>[</span><span>'land'</span><span>],</span>
                                        <span>linewidth</span><span>=.</span><span>1</span>
                                   <span>)</span>
<span># we can add high-resolution water</span>
<span>OCEAN</span> <span>=</span> <span>cfeature</span><span>.</span><span>NaturalEarthFeature</span><span>(</span><span>'physical'</span><span>,</span> <span>'ocean'</span><span>,</span> <span>'10m'</span><span>,</span>
                                        <span>edgecolor</span><span>=</span><span>'face'</span><span>,</span>
                                        <span>facecolor</span><span>=</span><span>cfeature</span><span>.</span><span>COLORS</span><span>[</span><span>'water'</span><span>],</span>
                                        <span>linewidth</span><span>=.</span><span>1</span>
                                   <span>)</span>

<span>ax</span><span>.</span><span>add_feature</span><span>(</span><span>LAND</span><span>,</span> <span>zorder</span><span>=</span><span>0</span><span>)</span>
<span>ax</span><span>.</span><span>add_feature</span><span>(</span><span>OCEAN</span><span>)</span>

<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.03-Working-with-Maps_14_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.03-Working-with-Maps_14_0.png"/>


<p>Звісно, у багатьох випадках ми хочемо нанести наші дані на карту та показати просторове розташування певних об'єктів. Дані можна додавати так само, як і до звичайних осей matplotlib. За замовчуванням система координат будь-яких доданих даних збігається з системою координат осей, яку ми визначили на початку побудови графіка. Спробуймо спочатку додати деякі дані на карту вище.</p>
<p><strong>СПРОБУЙТЕ!</strong> Додайте на наведену вище карту затоки Каліфорнійський університет у Берклі та Стенфордський університет.</p>


<pre><span></span><span>plt</span><span>.</span><span>figure</span><span>(</span><span>figsize</span> <span>=</span> <span>(</span><span>10</span><span>,</span> <span>8</span><span>))</span>

<span># plot the map related stuff</span>
<span>ax</span> <span>=</span> <span>plt</span><span>.</span><span>axes</span><span>(</span><span>projection</span><span>=</span><span>ccrs</span><span>.</span><span>PlateCarree</span><span>())</span>
<span>ax</span><span>.</span><span>coastlines</span><span>(</span><span>resolution</span><span>=</span><span>'10m'</span><span>)</span>
<span>ax</span><span>.</span><span>set_extent</span><span>([</span><span>-</span><span>122.8</span><span>,</span> <span>-</span><span>122</span><span>,</span> <span>37.3</span><span>,</span> <span>38.3</span><span>])</span>

<span># we can add high-resolution land</span>
<span>ax</span><span>.</span><span>add_feature</span><span>(</span><span>LAND</span><span>,</span> <span>zorder</span><span>=</span><span>0</span><span>)</span>
<span>ax</span><span>.</span><span>add_feature</span><span>(</span><span>OCEAN</span><span>,</span> <span>zorder</span><span>=</span><span>0</span><span>)</span>

<span># plot the data related stuff</span>
<span>berkeley_lon</span><span>,</span> <span>berkeley_lat</span> <span>=</span> <span>-</span><span>122.2585</span><span>,</span> <span>37.8719</span>
<span>stanford_lon</span><span>,</span> <span>stanford_lat</span> <span>=</span> <span>-</span><span>122.1661</span><span>,</span> <span>37.4241</span>

<span># plot the two universities as blue dots</span>
<span>ax</span><span>.</span><span>plot</span><span>([</span><span>berkeley_lon</span><span>,</span> <span>stanford_lon</span><span>],</span> <span>[</span><span>berkeley_lat</span><span>,</span> <span>stanford_lat</span><span>],</span>
         <span>color</span><span>=</span><span>'blue'</span><span>,</span> <span>linewidth</span><span>=</span><span>2</span><span>,</span> <span>marker</span><span>=</span><span>'o'</span><span>)</span>

<span># add labels for the two universities</span>
<span>ax</span><span>.</span><span>text</span><span>(</span><span>berkeley_lon</span> <span>+</span> <span>0.16</span><span>,</span> <span>berkeley_lat</span> <span>-</span> <span>0.02</span><span>,</span> <span>'UC Berkeley'</span><span>,</span>
         <span>horizontalalignment</span><span>=</span><span>'right'</span><span>)</span>

<span>ax</span><span>.</span><span>text</span><span>(</span><span>stanford_lon</span> <span>+</span> <span>0.02</span><span>,</span> <span>stanford_lat</span> <span>-</span> <span>0.02</span><span>,</span> <span>'Stanford'</span><span>,</span>
         <span>horizontalalignment</span><span>=</span><span>'left'</span><span>)</span>

<span>plt</span><span>.</span><span>show</span><span>()</span>
</pre>



<img alt="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.03-Working-with-Maps_16_0.png" src="https://raw.githubusercontent.com/dimabendera/python-ml-lessons/main/source/pythonnumericalmethods/_images/chapter12.03-Working-with-Maps_16_0.png"/>


<p>Є багато інших речей, які ми можемо побудувати за допомогою пакета cartopy. Ви можете знайти офіційну <a href="https://scitools.org.uk/cartopy/docs/latest/gallery/index.html">галерею прикладів</a> і дізнатися більше про створення гарних карт.</p>
