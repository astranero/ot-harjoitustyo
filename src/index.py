import tkinter as tk
import ui.register_ui as create
import ui.login_ui as login

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        
    def _start(self):
        self._show_login_view()

    def _show_register_view(self):
        self._current_view.destroy()
        self._current_view = create.Register(self._root, self._show_login_view)
        self._current_view.pack()
    
    def _show_login_view(self):
        if self._current_view !=None:
            self._current_view.destroy()
        self._current_view = login.LoginScreen(self._root, self._show_register_view)
        self._current_view.pack()

window = tk.Tk()
window.title("SoftFit-Assist")

window.geometry("400x400")
window.minsize(400,400)
window.maxsize(400,400)

ui = UI(window)
ui._start()

window.mainloop()