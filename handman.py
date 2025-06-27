import tkinter as tk
from tkinter import messagebox
import random

# List of possible words
words = ["banana", "grapes", "mango", "apple", "orange", "peach", "melon"]

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game 🎮")
        self.root.geometry("500x400")
        self.root.config(bg="#f7f7f7")

        self.word = random.choice(words)
        self.display_word = ["_"] * len(self.word)
        self.attempts_left = 6
        self.guessed_letters = []

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Hangman Game", font=("Arial", 20, "bold"), bg="#f7f7f7", fg="#333")
        self.title_label.pack(pady=10)

        self.word_label = tk.Label(self.root, text="Word: " + " ".join(self.display_word), font=("Arial", 16), bg="#f7f7f7")
        self.word_label.pack(pady=10)

        self.info_label = tk.Label(self.root, text=f"Attempts Left: {self.attempts_left}", font=("Arial", 14), bg="#f7f7f7")
        self.info_label.pack(pady=5)

        self.guess_label = tk.Label(self.root, text="Enter a letter:", font=("Arial", 12), bg="#f7f7f7")
        self.guess_label.pack()

        self.entry = tk.Entry(self.root, font=("Arial", 14), width=5, justify='center')
        self.entry.pack(pady=5)

        self.submit_btn = tk.Button(self.root, text="Guess", font=("Arial", 12), command=self.check_guess, bg="#4caf50", fg="white")
        self.submit_btn.pack(pady=10)

        self.guessed_label = tk.Label(self.root, text="Guessed Letters: ", font=("Arial", 12), bg="#f7f7f7")
        self.guessed_label.pack()

    def check_guess(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if not guess.isalpha() or len(guess) != 1:
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            messagebox.showinfo("Already Guessed", f"You already guessed '{guess}'")
            return

        self.guessed_letters.append(guess)

        if guess in self.word:
            for idx, char in enumerate(self.word):
                if char == guess:
                    self.display_word[idx] = guess
        else:
            self.attempts_left -= 1

        self.update_display()

    def update_display(self):
        self.word_label.config(text="Word: " + " ".join(self.display_word))
        self.info_label.config(text=f"Attempts Left: {self.attempts_left}")
        self.guessed_label.config(text="Guessed Letters: " + ", ".join(self.guessed_letters))

        if "_" not in self.display_word:
            messagebox.showinfo("🎉 You Win!", f"Congratulations! You guessed the word: {self.word}")
            self.root.destroy()

        elif self.attempts_left == 0:
            messagebox.showerror("💀 Game Over", f"Out of attempts! The word was: {self.word}")
            self.root.destroy()

# Start the game
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
