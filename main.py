from lawedu.quiz import Quiz, questions_dataset


def main():
	quiz = Quiz(questions_dataset)
	quiz.generate(len(questions_dataset['questions']))


if __name__ == '__main__':
	main()
