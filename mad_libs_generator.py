import tkinter as tk
from tkinter import messagebox
import random

# ----- STORY TEMPLATES -----
templates = [
    "Today I went to the {place} and saw a {adjective} {noun} {verb}ing around!",
    "My {noun} loves to {verb} when it's feeling {adjective} at the {place}.",
    "At the {place}, I found a {adjective} {noun} trying to {verb}.",
    "The {adjective} {noun} jumped into the {place} and started to {verb} loudly.",
    "Once upon a time in a {place}, a {adjective} {noun} decided to {verb}."
]

# List of placeholders needed
placeholders = ["place", "adjective", "noun", "verb"]

# ----- GUI APP CLASS -----
class MadLibsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mad Libs Generator")
        self.root.geometry("400x450")
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        tk.Label(self.root, text="Mad Libs Generator", font=("Arial", 18, "bold")).pack(pady=10)

        # Entry fields for each placeholder
        self.entries = {}
        for word in placeholders:
            frame = tk.Frame(self.root)
            frame.pack(pady=5)
            tk.Label(frame, text=f"Enter a {word}:", width=15, anchor="w").pack(side=tk.LEFT)
            entry = tk.Entry(frame, width=20)
            entry.pack(side=tk.LEFT)
            self.entries[word] = entry

        # Button to generate story
        tk.Button(self.root, text="Generate Story", command=self.generate_story).pack(pady=15)

        # Result box
        self.result_box = tk.Text(self.root, height=6, width=40, wrap=tk.WORD)
        self.result_box.pack(pady=10)

        # Play again button
        tk.Button(self.root, text="Play Again", command=self.clear_fields).pack(pady=5)

    def generate_story(self):
        user_inputs = {}

        # Validate all entries
        for word, entry in self.entries.items():
            value = entry.get().strip()
            if not value:
                messagebox.showwarning("Input Error", f"Please enter a {word}.")
                return
            user_inputs[word] = value

        # Pick a random story template
        template = random.choice(templates)

        # Generate the story
        story = template.format(**user_inputs)

        # Display the story
        self.result_box.delete(1.0, tk.END)
        self.result_box.insert(tk.END, story)

    def clear_fields(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.result_box.delete(1.0, tk.END)

# ----- RUN THE APP -----
if __name__ == "__main__":
    root = tk.Tk()
    app = MadLibsApp(root)
    root.mainloop()
