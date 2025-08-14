import tkinter as tk
from tkinter import messagebox

class VotingSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Voting System")

        self.create_gui()

    def create_gui(self):
        self.label = tk.Label(self.master, text="Vote for your favorite candidate:")
        self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.candidates = [
            "Candidate A",
            "Candidate B",
            "Candidate C",
            "Candidate D"
        ]

        for i, candidate in enumerate(self.candidates):
            button = tk.Button(self.master, text=candidate, command=lambda c=candidate: self.vote(c))
            button.grid(row=i+1, column=0, padx=10, pady=5)

        self.quit_button = tk.Button(self.master, text="Quit", command=self.quit)
        self.quit_button.grid(row=len(self.candidates)+2, column=0, columnspan=2, padx=10, pady=10)

        self.votes = {candidate: 0 for candidate in self.candidates}
        self.vote_counter = 0
        self.total_votes = None

        self.get_total_votes()

    def get_total_votes(self):
        self.total_votes = int(input("Enter the total number of votes: "))

    def vote(self, candidate):
        self.votes[candidate] += 1
        self.vote_counter += 1
        messagebox.showinfo("Success", f"Your vote for {candidate} has been recorded!")

        if self.vote_counter == self.total_votes:
            self.show_results()

    def show_results(self):
        result_message = "Vote counts:\n"
        for candidate, votes in self.votes.items():
            result_message += f"{candidate}: {votes} votes\n"
        messagebox.showinfo("Vote Results", result_message)

    def quit(self):
        # Display the vote counts before quitting
        for candidate, votes in self.votes.items():
            print(f"{candidate}: {votes} votes")
        self.master.destroy()

def main():
    root = tk.Tk()
    app = VotingSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()
