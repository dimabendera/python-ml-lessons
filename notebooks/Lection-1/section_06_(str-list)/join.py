states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
          "District Of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
          "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
          "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
          "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "PALAU",
          "Pennsylvania", "PUERTO RICO", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
          "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

# .join() — це метод string (функція, яка працює лише з рядками), який склеює список назад у рядок.

# .join() має дві основні частини: клей і список

# Клей - це нитка, яку ви хочете вклеїти між кожним фрагментом списку, коли ви збираєте його разом як рядок.
# Клей - це нитка, яка йде безпосередньо перед точкою.

# Список - це список, який ви хочете склеїти.

# Отже, якщо ми запустили таку команду:
print("glue".join(states))

# Смішно (і корисно для запам'ятовування), але це виглядає не дуже добре.

# Замість цього давайте скористаємося корисним шматочком клею.
# Давайте склеїмо його разом з новою лінією між кожним станом.
print("\n".join(states))

# Тепер отримуємо:
# Alabama
# Alaska
# Arizona
# Arkansas
# California
# Colorado
# Connecticut
# Delaware
# District Of Columbia
# Florida
# Georgia
# Hawaii
# Idaho
# Illinois
# Indiana
# Iowa
# Kansas
# Kentucky
# Louisiana
# Maine
# Maryland
# Massachusetts
# Michigan
# Minnesota
# Mississippi
# Missouri
# Montana
# Nebraska
# Nevada
# New Hampshire
# New Jersey
# New Mexico
# New York
# North Carolina
# North Dakota
# Ohio
# Oklahoma
# Oregon
# PALAU
# Pennsylvania
# PUERTO RICO
# Rhode Island
# South Carolina
# South Dakota
# Tennessee
# Texas
# Utah
# Vermont
# Virginia
# Washington
# West Virginia
# Wisconsin
# Wyoming
