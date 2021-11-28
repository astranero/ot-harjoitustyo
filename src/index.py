import tkinter as tk
import ui.register_ui as create
import ui.login_ui as login
import ui.user_ui as user_view


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
        if self._current_view is not None:
            self._current_view.destroy()
        self._current_view = login.LoginScreen(
            self._root, self._show_register_view, self._show_user_view)
        self._current_view.pack()

    def _show_user_view(self, email, password):
        self._current_view.destroy()
        self._current_view = user_view.User(
            self._root, email, password, self._show_login_view)
        self._current_view.pack()


window = tk.Tk()
window.title("SoftFit-Assist")
window.geometry("400x400")
window.minsize(300, 300)
window.maxsize(1280, 1020)
ui = UI(window)
ui._start()
window.mainloop()
