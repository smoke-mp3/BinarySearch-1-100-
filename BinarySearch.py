import tkinter as tk

class BinarySearch:
    def __init__(self, root,):
        self.root = root
        self.root.configure(bg="#000000")
        tk.Label(self.root, text="Think of a secret number between 1 and 100!",font=("Times New Roman", 15, "bold"), bg="#FFFFFF", fg="#5A037D").pack(pady=10)

        tk.Label(self.root, text="The guess was...",font=("Times New Roman", 15, "bold"), bg="#FFFFFF", fg="#7A0574").pack(pady=10)

        self.guess_label = tk.Label(self.root, text="", font=("Arial", 20, "bold"), bg="#FFFFFF", fg="#000000")
        self.guess_label.pack(pady=10)

        self.root_btn = tk.Button(self.root, text="Lower", font=("Arial", 12, "bold"), bg="#FFFFFF", fg="#830730", command=self.lower)
        self.root_btn.pack(pady=10)
        self.root_btn2 = tk.Button(self.root, text="Higher", font=("Arial", 12, "bold"), bg="#FFFFFF", fg="#7A0646", command=self.higher)
        self.root_btn2.pack(pady=10)
        self.root_btn3 = tk.Button(self.root, text="Correct!", font=("Arial", 12, "bold"), bg="#FFFFFF", fg="#118000", command=self.correct)
        self.root_btn3.pack(pady=10)
        self.root_btn4 = tk.Button(self.root, text="Play again", font=("Arial", 12, "bold"), bg="#FFFFFF", fg="#183368", command =self.Playagain)
        self.root_btn4.pack(pady=10)
        
        
        self.low = 1
        self.high = 100
        self.attempts = 0
        self.current = None
        self.make_guess()

    def make_guess(self):
        if self.low > self.high:
            self.guess_label.config(text="No number found")
            return
        self.current = (self.low + self.high) // 2
        self.attempts += 1
        self.guess_label.config(text=str(self.current))

    def lower(self):
        if self.current is None:
            return
        self.high = self.current - 1
        self.make_guess()

    def higher(self):
        if self.current is None:
            return
        self.low = self.current + 1
        self.make_guess()

    def correct(self):
        if self.current is None:
            return
        self.guess_label.config(text=f"Guessed {self.current} in {self.attempts} tries")

    def Playagain(self):
        self.low = 1
        self.high = 100
        self.attempts = 0
        self.current = None
        self.guess_label.config(text="")
        self.make_guess()
    
if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("400x500")
    window.resizable(False, False)
    window.title("Binary Search")
    app = BinarySearch(window)
    window.mainloop()