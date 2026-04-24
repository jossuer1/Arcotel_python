import tkinter as tk
from tkinter import messagebox

class LoginView:
    def __init__(self, auth):
        # --- ventana ---
    
        self.auth = auth
        self.window = tk.Tk()
        self.window.geometry("300x200")
        self.window.title("Login")

        tk.Label(self.window, text="Cédula").pack()
        self.cedula = tk.Entry(self.window)
        self.cedula.pack()

        tk.Label(self.window, text="Contraseña").pack()
        self.password = tk.Entry(self.window, show="*")
        self.password.pack()

        tk.Button(self.window, text="Login", command=self.login).pack()

    def login(self):
        resultado = self.auth.auth(
            self.cedula.get(),
            self.password.get()
        )

        if resultado == "OK":
            messagebox.showinfo("OK", "Bienvenido")
            self.window.destroy()
        else:
            messagebox.showerror("Error", resultado)

    def run(self):
        self.window.mainloop()