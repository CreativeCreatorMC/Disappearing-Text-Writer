#Copyright©️  CreativeCreatorMC(Arin Ruj). DO NOT COPY!
#Fully programmed and designed by CreativeCreatorMC(Arin Ruj)

import tkinter as tk
import time


class WritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Writing App")
        # Create the text box and bind the key events
        self.text_box = tk.Text(self.root)
        self.text_box.pack()

        self.text_box.bind('<Key>', self.reset_timer)

        # Create the timer for clearing the text
        self.timer = None

        # Start the GUI loop
        self.root.mainloop()

    def reset_timer(self, event):
        """Reset the timer when the user types"""
        if self.timer:
            self.root.after_cancel(self.timer)
        self.timer = self.root.after(5500, self.clear_text)

    def clear_text(self):
        """Clear the text in the box"""
        self.text_box.delete(1.0, tk.END)


# Start the application
if __name__ == '__main__':
    root = tk.Tk()
    app = WritingApp(root)
