import tkinter as tk
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = tk.Tk()
        self.window.title("Quiz Game")
        self.window.geometry("350x350")

        self.score_label = tk.Label(text=f"Score: 0", font=("Arial", 14))
        self.score_label.grid(row=0, column=1)

        self.question_label = tk.Label(text="Question", font=("Arial", 16))
        self.question_label.grid(row=1, column=0, columnspan=2, pady=20)

        true_button = tk.Button(text="True", command=self.true_pressed)
        true_button.grid(row=2, column=0, padx=20)

        false_button = tk.Button(text="False", command=self.false_pressed)
        false_button.grid(row=2, column=1, padx=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.question_label.config(text=self.quiz.question_list[self.quiz.question_number].question_text)
        else:
            self.question_label.config(text="Quiz Completed!")
            self.window.after(3000, self.window.destroy)

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_correct):
        if is_correct:
            self.question_label.config(text="Correct!")
        else:
            self.question_label.config(text="Incorrect!")

        self.window.after(1000, self.update_score_and_question)

    def update_score_and_question(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.get_next_question()
