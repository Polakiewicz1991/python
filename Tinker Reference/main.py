import tkinter as tk
from gui import CSVCompareApp

if __name__ == "__main__":
    root = tk.Tk()
    root.title("CSV Compare Tool (Tkinter)")
    root.geometry("1200x700")
    app = CSVCompareApp(root)
    root.mainloop()
