# First task Скласти програму, яка визначає і виводить на екран кількість слів у реченні, які закінчуються на літеру «р».

# Jump up and stop at top level, Philip.

found_letter = "p"
str_with_found_letter = ""
str = ""

while (len(str.split(' ')) < 7):
  str = input("Enter a string with at least 7 characters: ")

split_str = str.split(' ')
for word in split_str:
  if word.endswith(found_letter):
    str_with_found_letter += word + ' '

print(str_with_found_letter)    
print(len(str_with_found_letter.split(' ')))



# Second task Видалення зі списку повторень.

import re

inputtingSchedule = input("Enter a schedule: ")
if len(inputtingSchedule) <= 0:
  inputtingSchedule = "Ukraine, Poland, Germany, France, Italy, Spain, Ukraine, Poland"

list = re.findall("\w+", inputtingSchedule)

print(inputtingSchedule)
print(set(list))


# Third task Задано множини символiв А i символ «х». Скласти програму, яка формує множину В з множини А за таким правилом: а) додавання елемента х, якщо він відсутній в А; б) видалення елемента х, якщо він наявний в А.

set_a = {'a', 'b', 'c', 'd', 'e'}
set_b = set(set_a)
symbol_x = 'x'

if symbol_x not in set_a:
  set_b.add(symbol_x)
else:
  set_b.discard(symbol_x)

print(set_b)