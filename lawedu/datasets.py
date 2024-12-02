from typing import List, Optional, Dict
import json
from abc import ABC, abstractmethod


class DictionaryTerm:
	def __init__(self, term: str, definition: str, example: str):
		self.term = term
		self.definition = definition
		self.example = example


class LegalDictionary:
	def __init__(self, terms: List[DictionaryTerm]):
		self.terms = {term.term: term for term in terms}

	def search_term(self, term: str) -> Optional[DictionaryTerm]:
		return self.terms.get(term.lower())


class LegalSystems:
	def __init__(self, data: Dict[str, str]):
		self.data = data

	def get_system_info(self, country: str) -> Optional[str]:
		return self.data.get(country.lower())


class Question(ABC):
	@abstractmethod
	def check_answer(self, user_answer: int) -> bool:
		pass


class MultipleChoiceQuestion(Question):
	def __init__(self, question: str, options: List[str], correct_answer_index: int):
		self.question = question
		self.options = options
		self.correct_answer_index = correct_answer_index

	def check_answer(self, user_answer: int) -> bool:
		return user_answer == self.correct_answer_index

	def __str__(self):
		options_str = "\n".join(
			f"[{idx + 1}] {option}" for idx, option in enumerate(self.options)
		)
		return f"[bold cyan]{self.question}[/bold cyan]\n{options_str}"


class Quiz:
	def __init__(self, questions: List[Question]):
		self.questions = questions
		self.score = 0

	def start(self) -> None:
		for question in self.questions:
			console.print(str(question))
			user_answer = Prompt.ask(
				"Ваш ответ (введите номер)",
				choices=[str(i + 1) for i in range(len(question.options))],
			)
			if question.check_answer(int(user_answer) - 1):
				console.print("[bold green]Правильно![/bold green]")
				self.score += 1
			else:
				console.print(
					f"[bold red]Неправильно! Правильный ответ: {question.options[question.correct_answer_index]}[/bold red]"
				)
		self.display_score()

	def display_score(self) -> None:
		console.print(
			f"[bold magenta]Ваш общий балл: {self.score}/{len(self.questions)}[/bold magenta]"
		)


class QuizLoader:
	@staticmethod
	def load_questions(file_path: str) -> List[Question]:
		questions = []
		try:
			with open(file_path, "r", encoding="utf-8") as file:
				data = json.load(file)
				for item in data["questions"]:
					question = MultipleChoiceQuestion(
						question=item["question"],
						options=item["options"],
						correct_answer_index=item["correct_answer_index"],
					)
					questions.append(question)
		except (FileNotFoundError, json.JSONDecodeError) as e:
			console.print(f"[bold red]Ошибка загрузки вопросов: {e}[/bold red]")
		return questions
