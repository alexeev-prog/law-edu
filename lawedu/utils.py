from rich.console import Console


def print_correct(points: int):
	Console().print(f'[green][bold][+{points}][/bold] Верно![/green]', no_wrap=False, soft_wrap=True)


def print_incorrect(correct_answer: str):
	Console().print(f'[red]Неверно![/red] Верный ответ: {correct_answer}', no_wrap=False, soft_wrap=True)
