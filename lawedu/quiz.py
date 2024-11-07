from random import randint
from lawedu.utils import print_correct, print_incorrect
from rich.prompt import Prompt, Confirm
from rich.console import Console

questions_dataset = {
	"info": "ВСОШ НСО 9 класс муниципальный этап 2023 г.",
	"questions": {
		'1': {
			"text": "Укажите лишний среди признаков права.",
			"desc": "a) обеспеченность государством; б) системность; в) избирательность применения",
			"choices": ["а", "б", "в"],
			"answer": "в"
		},
		'2': {
			"text": "Регистрация рождения ребенка производится не позднее",
			"desc": "а) одного месяца с момента рождения; б) трех месяцев с момента рождения; в) шести месяцев с момента рождения; г) двенадцати месяцев с момента рождения",
			"choices": ['а', 'б', "в", "г"],
			"answer": "а"
		},
		'3': {
			"text": "Работодатель обязан расторгнуть договор с работником по инициативе работника в течение.",
			"desc": "а) одной недели; б) двух недель; в) трех недель; г) четырех недель",
			"choices": ["а", "б", "в", "г"],
			"answer": "б"
		},
		"4": {
			"text": "13-летний гражданин П, будучи в гостях у одноклассника, похитил из шкатулки его бабушки золотые серьги. Какая ответственность его ожидает?",
			"desc": "а) административная; б) дисциплинарная; в) меры воспитательного воздействия; г) гражданско-правовая",
			"choices": ["а", "б", "в", "г"],
			"answer": "в"
		},
		"5": {
			"text": "Для какой профессии нет предельного возраста?",
			"desc": "а) мировой судья; б) прокурор района; в) депутат госдумы федерального собрания; г) нотариус",
			"choices": ["а", "б", "в", "г"],
			"answer": "в"
		},
		"6": {
			"text": 'Что означает фраза "Sine precio nulla venditio est"?',
			"desc": "а) закон суров, но это закон; б) деньги не могут менять природу; в) нет границ лжи; г) без цены нет продажи",
			"choices": ["а", "б", "в", "г"],
			"answer": "г"
		},
		"7": {
			"text": 'Что означает фраза "Naturam mutare pecunia nescit"?',
			"desc": "а) деньги не могут менять природу; б) в отношении всех ложь одинаково наказывается; в) наилучший толкователь законов - практика; г) без цены нет продажи",
			"choices": ["а", "б", "в", "г"],
			"answer": "а"
		},
		"8": {
			"text": "Согласно статье 81 УК РФ, лицо освобождается от уголовного наказния в связи с...",
			"desc": "а) наступлением психического расстройства, лишающего его возможности осозновать опасность своих бедствий; б) противоправностью или аморальностью поведения потерпевшего; в) возмщением в полном объеме ущерба, причененной бюджетной системе РФ; г) примирением с потерпевшим и компенсацией причиненному потерпевшему вреда",
			"choices": ["а", "б", "в", "г"],
			"answer": "а"
		},
		"9": {
			"text": "В какой главе Конституции РФ говорится о том, что местное самоуправление в Российской Федерации обеспечивает самостоятельное решение населением вопросов местного назначения, владение, пользование и распоряжение муниципальной собственностью?",
			"desc": "а) 4; б) 6; в) 8; г) 10",
			"choices": ["а", "б", "в", "г"],
			"answer": "в"
		},
		"10": {
			"text": "Укажите признак, не характерный для преступления",
			"desc": "а) наказуемость; б) виновность; в) общественная опасность; г) общественное порицание",
			"choices": ["а", "б", "в", "г"],
			"answer": "г"
		},
		"11": {
			"text": "Работодатель К. рассторгнул трудовой договор с гражданином Д (по инициативе гражданина). спустя 18 дней. Законно ли это?",
			"desc": "а) нет, т.к. работодатель должен расторгнуть договор за 14 дней; б) нет, т.к. работодатель должен расторгнуть договор сразу; в) нет, т.к. работодатель не имел права расторгнуть договор; г) да, закон соблюдается",
			"choices": ["а", "б", "в", "г"],
			"answer": "а"
		}
	}
}


class Quiz:
	def __init__(self, questions_dataset: dict):
		self.questions_dataset = questions_dataset
		self.console = Console()
		self.points = 0
		self.generated_questions = []

	def check_answer(self, correct_answer: str, answer: str):
		if correct_answer.lower() == answer.lower():
			print_correct(1)
			self.points += 1
		else:
			print_incorrect(correct_answer.lower())

	def generate_question(self, num: int):
		question = questions_dataset["questions"][str(num)]
		choices = question.get('choices', None)

		self.console.print(f'[bold]Вопрос N{num}: {question["text"]}[/bold]\n{question["desc"]}\n', no_wrap=False, soft_wrap=True)
		
		if choices is not None:
			answer = Prompt.ask("Введите ответ", choices=choices)
		else:
			answer = Prompt.ask("Введите ответ")

		self.check_answer(question['answer'], answer)

	def generate(self, questions_count: int):
		if questions_count > len(self.questions_dataset['questions']):
			questions_count = len(self.questions_dataset['questions'])

		print(self.questions_dataset["info"], '\n')

		for i in range(1, questions_count + 1):
			self.generate_question(i)
			print()
			self.console.print('=' * 48, no_wrap=True)
			print()

		self.console.print(f'\nИтого баллов: [bold]{self.points} из {questions_count}[/bold]', no_wrap=False, soft_wrap=True)
