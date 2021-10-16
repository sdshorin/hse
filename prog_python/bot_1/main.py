import telebot
# from  telebot import types
from  telebot import types 
import config
from matrix import Matrix, MatrixError
from collections import defaultdict
import random
import time
# token from bot @BotFather
bot = telebot.TeleBot(config.TOKEN)

user_data = defaultdict(lambda: {"vars": {}})
import re


name = ''
surname = ''


class BotException(BaseException):
	def __init__(self, str_d) -> None:
		self.str = str_d

@bot.message_handler(commands=['start', 'help'])
def start_command(message):
   keyboard = telebot.types.InlineKeyboardMarkup()
   keyboard.add(
       telebot.types.InlineKeyboardButton(
           "Message the developer", url='telegram.me/shorins'
       )
   )
   bot.send_message(
       message.chat.id,
	   """
Матричный калькулятор для решения выражений.
Бот умеет складывать, перемножать, транспонировать матрицы.
/try -  сгенерировать 6 случайных матриц для проверки
/vars - Показать все локальные переменные 

Синтаксис:
Имя матрицы - любой символ из диапазона A-Z.

Для создания новой матрицы - введите 
```
A = 1 2 3
4 5 6
```
Эта команда добавит переменную A с матрицей 2x3.

Для вычисления новой матрицы - ведите
```
C = 4 * A + B^T - D```
Эта команда добавит переменную C, равную соответствующему выражению, и выведет С.

Для решения выражения введите его:
```4 * A + B^T - D```

Для печати матрицы введите ее название.

	   """,
       reply_markup=keyboard
   )

@bot.message_handler(commands=['try'])
def start_command(message):
	def create_random_matrix(x, y):
		return Matrix([[random.randrange(-10, 50) for _ in range(x)] for _ in range(y)])
	global user_data
	for matrix_data in [("A", 2, 2),("B", 2, 3), ("C", 3, 4), ("D", 3, 3), ("F", 4, 4), ("L", 2, 4)]:
		matrix:Matrix = create_random_matrix(*matrix_data[1:])
		user_data[message.from_user.id]["vars"][matrix_data[0]] = matrix
		bot.send_message(message.from_user.id,f"Матрица {matrix_data[0]} добавлена\nРазмер {matrix.size()}\n" + matrix.print_pretty())

@bot.message_handler(commands=['clear'])
def start_command(message):
	global user_data
	user_data[message.from_user.id]["vars"] = {}
	bot.send_message(message.from_user.id, "Все сохраненные матрицы удалены")
		

	


@bot.message_handler(content_types=["text"])
def get_text_message(message):
	# bot.send_message(message.from_user.id, eval(message.text))
	# return
	bot.send_message(message.from_user.id,"input: "+ message.text)
	try:
		if message.text.find("=") != -1:
			add_new_var_for_user(message)
		elif is_valid_matrix_name(message.text):
			print_var(message, message.text)
	except BotException as e:
		bot.send_message(message.from_user.id, e.str)
	except MatrixError as e:
		bot.send_message(message.from_user.id, "MatrixError: " + str(e))
	return

	if message.text == "Hello":
		bot.send_message(message.from_user.id, "Hello!")
		bot.send_message(message.from_user.id, "What is you name?")
		bot.register_next_step_handler(message, get_name)
	else:
		bot.send_message(message.from_user.id, "Unknown comand!")


def print_var(message, var):
	global user_data
	if not var in user_data[message.from_user.id]["vars"]:
		raise BotException("Переменная не найдена")
	matrix: Matrix = user_data[message.from_user.id]["vars"][var]
	send_matrix(message, matrix, var)

def send_matrix(message, matrix, matrix_name = ""):
	if matrix_name:
		bot.send_message(message.from_user.id, f"{matrix_name} =\n{matrix.print_pretty()}")
	else:
		bot.send_message(message.from_user.id, f"{str(matrix.print_pretty())}")	
	




def is_valid_matrix_name(input_str):
	return len(input_str) == 1 and input_str.isupper() and input_str.isascii()



is_only_nums = re.compile('-?\d+$')
def add_new_var_for_user(message):
	global user_data
	new_var_name = message.text.split("=")[0]
	input_data = message.text.split("=")[1].strip()
	new_var_name = new_var_name.strip()
	if not is_valid_matrix_name(new_var_name):
		raise BotException("Error: bad var name! Use one uppercace acsii letter, for example `A`, `B`")
	if not input_data:
		bot.send_message(message.from_user.id, f"Запущен интерактивный режим ввода матрицы. Вводите матрицу построчно, когда закончите - отправьте любое сообщение без чисел")	
		raise BotException("Интерактивный режим находится в разработке")
	is_pure_matrix = True
	for num in input_data.split():
		if not is_only_nums.match(num):
			is_pure_matrix = False
			break
			# raise BotException(f"Error: matrix can have only natural values! Error in: {num}.")
	if is_pure_matrix:
		user_data[message.from_user.id]["vars"][new_var_name] = Matrix(input_data)
		bot.send_message(message.from_user.id,f"Матрица {new_var_name} добавлена")
	else:
		new_matrix: Matrix = eval_matrix_expression(input_data, user_data[message.from_user.id]["vars"])
		user_data[message.from_user.id]["vars"][new_var_name] = new_matrix
		bot.send_message(message.from_user.id,f"Матрица {new_var_name} добавлена")
		send_matrix(message, new_matrix, new_var_name)

def eval_matrix_expression(expression, vars):
	return Matrix(eval(check_expression(expression), vars, {}))

def check_expression(expression: str)-> str:
	

# def get_name(message):
# 	global name
# 	name = message.text
# 	bot.send_message(message.from_user.id, "What is you surname?")
# 	bot.register_next_step_handler(message, get_surname)
# 	# bot.send_message(message.from_user.id, "Hello! " + str(name))

# def get_surname(message):
# 	global surname
# 	surname = message.text
# 	bot.send_message(message.from_user.id, "Hello! " +str(name) + " "+  str(surname))
# 	keyboard = types.InlineKeyboardMarkup()
# 	# keyboard = types.InLineKeyboardMarkup()
# 	key_yes = types.InlineKeyboardButton(text= "yes",callback_data = "yes" )
# 	key_no = types.InlineKeyboardButton(text= "no",callback_data = "no" )
# 	keyboard.add(key_yes)
# 	keyboard.add(key_no)
# 	bot.send_message(message.from_user.id, text = "Right?", reply_markup = keyboard)

@bot.callback_query_handler(func = lambda call: True)
def callback_worker(call):
	if call.data == "yes":
		bot.send_message(call.message.chat.id, "Great!")
	elif call.data == "no":
		bot.send_message(call.message.chat.id, "it's a pirty!")

# print(1)
# bot.polling(none_stop = True, interval = 0, timeout=30, long_polling_timeout = 5)
# print(2)
while True:
	try:
		bot.polling(none_stop = True, interval = 0, timeout=30, long_polling_timeout = 5)
	except Exception as e:
		print(e)
		time.sleep(1)
		continue
	break

