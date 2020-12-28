# ppkn-discord-bot

### Opis

Projekt oficjalnie stworzony przez xdexer (xdexer)[https://github.com/xdexer], SoulVictus [soulvictus](https://github.com/soulvictus), kacperma [kacperma](https://github.com/kacperma), aktualnie w fazie refraktoryzacji, modyfikacji i dodawania nowych funkcjonalności.

# Code convention

### Ogólne:

Używaj pełnych i zrozumiałych nazw.
Zachowuj dwie linie odstępu między definicjami klas oraz funkcji.
Zachowuj jedną linię odstępu między definicjami metod.
Parametry funkcji, metod oraz elementy w liście oddzielaj przecinkiem i spacją.

```python
def sum_two_numbers(number1, number2):
	result = number1 + number2
	return result


class ConnectionManager:
	def __init__(self, connection_string):
		self.connection_string = connection_string

	def connect_to_database(self):
		#do something
```

Kiedy funkcja, metoda jest rozbudowana i wykonuje kilka kroków, odziel je spacjami.

```python
def calculate_variance(number_list):
    sum_list = 0
    for number in number_list:
        sum_list = sum_list + number
    mean = sum_list / len(number_list)

    sum_squares = 0
    for number in number_list:
        sum_squares = sum_squares + number**2
    mean_squares = sum_squares / len(number_list)

    return mean_squares - mean**2    
```

Operacje oddzielaj spacjami:

```python
# Recommended
y = x**2 + 5
z = (x+y) * (x-y)

# Not Recommended
y = x ** 2 + 5
z = (x + y) * (x - y)
```

Zbyt długie linie kodu załamuj (powyżej 79 linii kodu):

```python
def function(arg_one, arg_two,
             arg_three, arg_four):
    return arg_one
    
total = (first_variable
         + second_variable
         - third_variable)
	 
list_of_numbers = [
	1, 2, 3
	4, 5, 6
	7, 8, 9
	]
```

Używaj komentarzy do każdej funkcji i metody:

```python
"""
calculator_add
Function that adds two numbers
@param number1 INT/FLOAT - Number one to add
@param number2 INT/FLOAT - Number two to add
@return INT/FLOAT - Result of adding two numbers
"""
def calculator_add(number1, number2):
    return number1 + number2
```
Do problematycznych linii kodu używaj komentarzy jednolinijkowych:
```python
x = b**2 - 4*a*c # delta for quadratic equation
```

### 1. Funkcje i zmienne:

Nazwy funkcji i zmiennych zapisuj małymi literami.
Stałe zapisuj dużymi literami,
Słowa powinny być oddzielone podkreśleniem:

```python
first_name = "Janusz"
last_name = "Kowalski"
id = "532137420"
PI = 3.14
CONSTANT_NUMBER = 5
def my_function():
```

### 2. Klasy i metody:

Nazwy klas zapisuj dużymi literami, każde słowo powinno być zapisane dużą literą,
nie używaj podkreśleń.

Nazwy metod zapisuj małymi literami, słowa odzielaj podkreśleniem.

```python
class Class:
	def my_function(self, variable, second_variable):

	def multiply_by_two(self, number):


class CarClass:
	def __init__(self, name, production_year, id_number="0000000"):
		self.name = name
		self.production_year = production_year
		self.id_number = id_number
	
	def __str__(self):
		return f"Name: {self.name}, Year: {self.production_year}, ID: {self.id_number}"
```
### 3. Pliki:

Nazwy plików zapisuj małą literą, słowa odzielaj podkreśleniem:

```python
module.py
my_module.py
student_list.txt
```

### Źródło:
https://realpython.com/python-pep8/#code-layout
https://www.python.org/dev/peps/pep-0008/
