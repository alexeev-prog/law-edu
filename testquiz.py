import json
from abc import ABC, abstractmethod
from lawedu.datasets import Quiz, LegalDictionary, LegalSystems, QuizLoader, DictionaryTerm
from rich.console import Console
from rich.prompt import Prompt

console = Console()


class LegalApp:
	def __init__(self, questions_file: str, terms_file: str, legal_systems_file: str):
		self.quiz = Quiz(QuizLoader.load_questions(questions_file))
		self.dictionary = self.load_dictionary(terms_file)
		self.legal_systems = self.load_legal_systems(legal_systems_file)

	@staticmethod
	def load_dictionary(file_path: str) -> LegalDictionary:
		terms = []
		try:
			with open(file_path, "r", encoding="utf-8") as file:
				data = json.load(file)
				for item in data["terms"]:
					terms.append(
						DictionaryTerm(
							item["term"], item["definition"], item["example"]
						)
					)
		except (FileNotFoundError, json.JSONDecodeError) as e:
			console.print(
				f"[bold red]Ошибка загрузки юридического словаря: {e}[/bold red]"
			)
		return LegalDictionary(terms)

	@staticmethod
	def load_legal_systems(file_path: str) -> LegalSystems:
		data = {}
		try:
			with open(file_path, "r", encoding="utf-8") as file:
				data = json.load(file)
		except (FileNotFoundError, json.JSONDecodeError) as e:
			console.print(f"[bold red]Ошибка загрузки правовых систем: {e}[/bold red]")
		return LegalSystems(data)

	def run_quiz(self) -> None:
		console.print("[bold blue]Тестирование знаний по праву:[/bold blue]")
		self.quiz.start()

	def search_term(self) -> None:
		term = Prompt.ask("Введите юридический термин для поиска")
		result = self.dictionary.search_term(term)
		if result:
			console.print(
				f"[bold green]{result.term}:[/bold green] {result.definition}\n[italic]{result.example}[/italic]"
			)
		else:
			console.print("[bold red]Термин не найден.[/bold red]")

	def get_legal_system(self) -> None:
		country = Prompt.ask("Введите название страны")
		info = self.legal_systems.get_system_info(country)
		if info:
			console.print(f"[bold blue]Правовая система {country}:[/bold blue] {info}")
		else:
			console.print(
				"[bold red]Информация о правовой системе не найдена.[/bold red]"
			)

	def run(self) -> None:
		while True:
			console.print("\n[bold white]Выберите опцию:[/bold white]")
			console.print("[green]1. Тестирование знаний по праву[/green]")
			console.print("[green]2. Поиск юридического термина[/green]")
			console.print("[green]3. Информация о правовых системах стран[/green]")
			console.print("[red]4. Выйти[/red]")

			choice = Prompt.ask("Ваш выбор", choices=["1", "2", "3", "4"])
			if choice == "1":
				self.run_quiz()
			elif choice == "2":
				print(f'Доступные термины: {", ".join(self.dictionary.terms.keys())}')
				self.search_term()
			elif choice == "3":
				print(f'Доступные страны: {", ".join(self.legal_systems.data.keys())}')
				self.get_legal_system()
			elif choice == "4":
				console.print(
					"[bold green]Спасибо за использование приложения![/bold green]"
				)
				break


# Функция для запуска приложения
def main() -> None:
	questions_file = "questions.json"
	terms_file = "terms.json"  # Путь к файлу с терминами
	legal_systems_file = "legal_systems.json"  # Путь к файлу с правовыми системами
	app = LegalApp(questions_file, terms_file, legal_systems_file)
	app.run()


if __name__ == "__main__":
	main()
