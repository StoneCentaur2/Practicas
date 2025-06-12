import tkinter as tk

class ProgressBarApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Barra de Recarga")

        self.progressbar = tk.Canvas(master, width=300, height=20, bg='white', relief='raised', borderwidth=1)
        self.progressbar.pack(pady=10)

        self.progressbar_fill = self.progressbar.create_rectangle(0, 0, 0, 20, fill='blue')

        self.progressbar_label = tk.Label(master, text="Progreso: 0%", bg='white')
        self.progressbar_label.pack(pady=5)

        self.progress = 0
        self.max_progress = 100

        self.update_progressbar()

    def update_progressbar(self):
        if self.progress <= self.max_progress:
            self.progressbar.coords(self.progressbar_fill, 0, 0, 3 * self.progress, 20)
            self.progressbar_label.config(text=f"Progreso: {self.progress}%")
            self.progress += 1
            self.master.after(100, self.update_progressbar)

root = tk.Tk()
app = ProgressBarApp(root)
root.mainloop()
