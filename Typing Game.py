import tkinter as tk
import random
import time

class TypingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Game")

        self.difficulty = tk.StringVar()
        self.difficulty.set("Facile")

        self.word_lists = {
            "Facile": ["chat", "soleil", "maison", "table", "chien", "fruit", "oiseau", "fleur", "pomme", "eau", "arbre", "plante", "montagne", "route", "papillon", "étoile", "nuage", "lac", "herbe", "vent"],
            "Moyen": ["ordinateur", "fenêtre", "musique", "restaurant", "paris", "coffee", "library", "elephant", "giraffe", "umbrella", "technology", "creative", "discovery", "exploration", "jungle", "knowledge", "ocean", "robot", "science", "adventure", "galaxy", "island", "camera", "guitar", "butterfly", "keyboard"],
            "Difficile": ["programming", "challenge", "keyboard", "developer", "coding", "practice", "typing", "interface", "example", "improve", "functionality", "customize", "feature", "discovery", "exploration", "jungle", "knowledge", "ocean", "robot", "science", "adventure", "algorithm", "application", "efficiency", "optimization", "structure", "architecture", "inheritance", "polymorphism", "abstraction", "encapsulation"]
        }

        self.start_time = None
        self.total_time = 0
        self.correct_count = 0
        self.total_count = 0

        self.word_to_type = self.get_random_word()

        self.label = tk.Label(master, text="Tapez le mot suivant : {}".format(self.word_to_type), font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Helvetica", 14))
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', lambda event: self.check_input())

        self.info_label = tk.Label(master, text="", font=("Helvetica", 12))
        self.info_label.pack(pady=10)

        self.timer_label = tk.Label(master, text="Temps écoulé : 0s", font=("Helvetica", 12))
        self.timer_label.pack(pady=10)

        self.score_label = tk.Label(master, text="Score : 0", font=("Helvetica", 12))
        self.score_label.pack(pady=10)

        self.start_game()

    def start_game(self):
        self.start_time = time.time()

    def get_random_word(self):
        difficulty = self.difficulty.get()

        if difficulty not in self.word_lists:
            return "Aucun mot disponible pour cette difficulté."

        word_list = self.word_lists[difficulty]
        return random.choice(word_list)

    def check_input(self):
        if self.start_time is None:
            self.start_game()

        user_input = self.entry.get()
        self.total_count += 1

        if user_input == self.word_to_type:
            self.correct_count += 1
            self.info_label.config(text="Félicitations ! Vous avez tapé le mot correctement.", fg="green")
        else:
            self.info_label.config(text="Désolé, le mot que vous avez tapé est incorrect.", fg="red")

        self.update_score()
        self.reset_game()

    def update_score(self):
        accuracy = (self.correct_count / self.total_count) * 100 if self.total_count > 0 else 0
        speed = self.correct_count / self.total_time if self.total_time > 0 else 0
        score = accuracy * speed

        self.score_label.config(text="Score : {:.2f}".format(score))

    def reset_game(self):
        self.word_to_type = self.get_random_word()
        self.label.config(text="Tapez le mot suivant : {}".format(self.word_to_type))
        self.entry.delete(0, tk.END)
        self.start_time = time.time()
        self.correct_count = 0
        self.total_time = 0
        self.total_count = 0
        self.update_timer()

    def update_timer(self):
        elapsed_time = time.time() - self.start_time
        self.timer_label.config(text="Temps écoulé : {:.1f}s".format(elapsed_time))
        self.total_time = elapsed_time
        self.master.after(100, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x500")
    game = TypingGame(root)
    root.mainloop()