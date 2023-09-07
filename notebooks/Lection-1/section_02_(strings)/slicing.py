# Приклади slice
# Slicing дозволяє нам бачити один шматок або «фрагмент» елемента, як один символ (або набір символів) у рядку


# Почнемо зі створення змінної з назвою github_handle; він буде містити рядок з моїм маркером GitHub
github_handle = '@dimabendera'


# За допомогою коми можна відокремити різні елементи, які потрібно надрукувати, як показано нижче
print("My github handle is ", github_handle)


# Це наш перший приклад slice.
# Зверніть увагу на квадратні дужки, прикріплені безпосередньо до імені змінної без пробілів між ними.
# Два числа посередині, розділені двокрапкою, називаються індексами slice
print("My first name is ", github_handle[1:5])


# Ось як можна візуалізувати наведену вище інструкцію
#       @dimabendera
#       01234567....

# Примітка: Python починає відлік з нуля, а останні кілька букв (d, e, r, a) прив'язані до 8, 9, 10, 11

# Всі індекси виглядабть так:

# -      0		@
# -      1		d
# -      2		i
# -      3		m
# -      4		a
# -      5		b
# -      6		e
# -      7		n
# -      8		d
# -      9		e
# -      10		r
# -      11		a


# Отже, у прикладі github_handle[1:5] зверніть увагу, що b (на фрагменті #5) не включено, але d (на фрагменті #1) є.
# Це тому, що значення першого фрагмента є інклюзивним, але значення другого фрагмента є ексклюзивним.


print("My last name is ", github_handle[5:12])

# Зверніть увагу, що індексу 12 немає.
# Якщо другий індекс вищий за існуючий, Python вважатиме, що ви маєте на увазі "до самого кінця"

# Другий індекс можна опустити; Python розуміє це як «йти до кінця»
print("My last name is ", github_handle[5:])

# І якщо ви опустите перший індекс, Python розуміє це як "почати з початку"
print("My twitter handle is NOT ", github_handle[:5])

# Що станеться, якщо використовувати від'ємний індекс розрізання?

# Від'ємні індекси фрагментів можна використовувати для зворотного відліку від кінця, наприклад:

# -       -12		@
# -       -11		d
# -       -10		i
# -       -9		m
# -       -8		a
# -       -7		b
# -       -6		e
# -       -5		n
# -       -4		d
# -       -3		e
# -       -2		r
# -       -1		a

print("My last name is ", github_handle[-7:])

# Ви також можете змішувати та поєднувати позитивні та негативні індекси slice за потреби

print("My first name is ", github_handle[1:-7])

# У цих прикладах ми покладаємося на знання точних індексів.
# Але що робити, якщо наш рядок зміниться в розмірі або вмісті?
# З короткими рядками досить легко розібратися, які slice-и вам потрібні.

# Але більш поширеним і практичним способом поділу, а не прямим використанням чисел, є створення змінної,
# яка містить потрібне число (але може змінюватися в міру необхідності)

# Примітка: тут можна використовувати str.find()

print("### Part Two ###")

text = "My GitHub handle is @dimabendera and my Instagram handle is @dm.bendea"

# Давайте витягнемо дескриптор GitHub за допомогою str.find() та slice-ів.

snail_index = text.find('@')

# Отже, перший індекс нарізки задається змінною,
# але ми все ще покладаємося на знання точної кількості символів (14).  Ми можемо це покращити.
print(text[snail_index:snail_index + 12])

# Зауважте, що ми використовуємо slice тут, щоб вказати початок .find() після того, як перша собачка знайдена.
space_after_first_snail_index = text[snail_index:].find(' ')

# Навіщо нам додавати snail_index до другого індексу slice? Погляньте:
print(text[snail_index:snail_index + space_after_first_snail_index])

print("snail_index is: ", snail_index)
print("space_after_first_snail_index is: ", space_after_first_snail_index)

print("Отже, це, по суті, text[20:32] --> ", text[20:32])

# Замість того, щоб створювати окрему змінну, ви можете просто додати str.find(), прямо в slice, наприклад:
print(text[text.find('@'):text.find('@')+text[text.find('@'):].find(' ')])  # Але, як бачите, він не дуже читабельний.

print("Чи можете ви використовувати методи строк(такі як str.find()) та slice-и, "
      "щоб витягти маркер Instagram з тексту?")
