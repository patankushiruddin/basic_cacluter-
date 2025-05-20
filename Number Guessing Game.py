import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x300")
        
        # Game variables
        self.low = 1
        self.high = 100
        self.attempts = 0
        self.current_guess = None
        
        # Create GUI elements
        self.create_widgets()
        
        # Start the game
        self.make_guess()
    
    def create_widgets(self):
        # Instruction label
        self.instruction = tk.Label(
            self.root,
            text="Think of a number between 1 and 100,\nthen click 'Start Game' when ready!",
            font=('Arial', 12),
            wraplength=350
        )
        self.instruction.pack(pady=20)
        
        # Guess display
        self.guess_label = tk.Label(
            self.root,
            text="",
            font=('Arial', 24, 'bold')
        )
        self.guess_label.pack(pady=10)
        
        # Response buttons frame
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=20)
        
        # Response buttons
        self.too_low_btn = tk.Button(
            self.button_frame,
            text="Too Low",
            command=self.guess_too_low,
            state=tk.DISABLED,
            bg='#ffcccc'
        )
        self.too_low_btn.pack(side=tk.LEFT, padx=10)
        
        self.correct_btn = tk.Button(
            self.button_frame,
            text="Correct!",
            command=self.guess_correct,
            state=tk.DISABLED,
            bg='#ccffcc'
        )
        self.correct_btn.pack(side=tk.LEFT, padx=10)
        
        self.too_high_btn = tk.Button(
            self.button_frame,
            text="Too High",
            command=self.guess_too_high,
            state=tk.DISABLED,
            bg='#ccccff'
        )
        self.too_high_btn.pack(side=tk.LEFT, padx=10)
        
        # Start button
        self.start_btn = tk.Button(
            self.root,
            text="Start Game",
            command=self.start_game,
            bg='#ffffcc'
        )
        self.start_btn.pack()
    
    def start_game(self):
        # Reset game variables
        self.low = 1
        self.high = 100
        self.attempts = 0
        
        # Enable response buttons
        self.too_low_btn.config(state=tk.NORMAL)
        self.correct_btn.config(state=tk.NORMAL)
        self.too_high_btn.config(state=tk.NORMAL)
        
        # Disable start button
        self.start_btn.config(state=tk.DISABLED)
        
        # Update instruction
        self.instruction.config(text="Is this your number?")
        
        # Make first guess
        self.make_guess()
    
    def make_guess(self):
        self.current_guess = (self.low + self.high) // 2
        self.attempts += 1
        self.guess_label.config(text=str(self.current_guess))
    
    def guess_too_low(self):
        self.low = self.current_guess + 1
        self.make_guess()
    
    def guess_too_high(self):
        self.high = self.current_guess - 1
        self.make_guess()
    
    def guess_correct(self):
        messagebox.showinfo(
            "Success!",
            f"I guessed your number {self.current_guess} in {self.attempts} attempts!"
        )
        
        # Reset UI
        self.instruction.config(text="Think of a number between 1 and 100,\nthen click 'Start Game' when ready!")
        self.guess_label.config(text="")
        self.too_low_btn.config(state=tk.DISABLED)
        self.correct_btn.config(state=tk.DISABLED)
        self.too_high_btn.config(state=tk.DISABLED)
        self.start_btn.config(state=tk.NORMAL)

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()