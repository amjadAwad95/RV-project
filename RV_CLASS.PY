from math import factorial, exp, log
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from functools import partial
from tkinter import messagebox
import sys

# --------------------- The main class ---------------------------


class probability:
    class binomial:
        def __init__(self, p, n):
            self.p = p
            self.n = n

        def pmf(self, r):
            if (self.p > 1 or self.p < 0):
                return None
            combinations = factorial(self.n)/(factorial(self.n-r)*factorial(r))
            return combinations*(pow(self.p, r))*(pow(1-self.p, self.n-r))

        def E(self):
            return self.p*self.n

        def var(self):
            return self.p*self.n*(1-self.p)

    class uniform:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def pmf(self, k):
            if (k > self.b or k < self.a):
                return 0
            else:
                p = 1/(self.b-self.a)
                if (p > 1 or p < 0):
                    return None
                else:
                    return p

        def E(self):
            return (self.a+self.b)/2

        def var(self):
            return (self.b-self.a)*(self.b-self.a+2)/12

    class geometric:
        def __init__(self, p):
            self.p = p

        def pmf(self, n):
            if (0 < self.p <= 1):
                pro = pow((1-self.p), n)*self.p
                return pro
            else:
                return None

        def E(self):
            E_x_ = 1/self.p
            return E_x_

        def var(self):
            varians = self.p/(pow((1-self.p), 2))
            return varians

    class bernouli:
        def __init__(self, p):
            self.p = p
            self.f = 1 - self.p

        def pmf(self):
            if (0 <= self.p <= 1):
                return [1-self.p, self.p]
            else:
                return [None, None]

        def E(self):
            return self.p

        def var(self):
            return (self.p * (1 - self.p))

    class poisson:
        def __init__(self, lambdaa):
            self.lambdaa = lambdaa

        def pmf(self, k):
            p = exp(-self.lambdaa + k * log(self.lambdaa) - log(factorial(k)))
            # p = float((pow(self.lambdaa, k)*exp(-self.lambdaa))/factorial(k))
            return p

        def E(self):
            return self.lambdaa

        def var(self):
            return self.lambdaa

# ------------------------ Compute RV function ---------------------------


def binomial_compute(p, n):
    rv_model = probability.binomial(p, n)
    rv_value = list(range(n+1))
    prob = [rv_model.pmf(x) for x in rv_value]
    plt.vlines(rv_value, 0, prob, label="Binomial")
    plt.show()


def uniform_compute(a, b):
    rv_model = probability.uniform(a, b)
    rv_value = list(range(a, b+1))
    prob = [rv_model.pmf(x) for x in rv_value]
    plt.vlines(rv_value, 0, prob, label="Uniform")
    plt.show()


def geometric_compute(p, n):
    rv_model = probability.geometric(p)
    rv_value = list(range(1, n))
    prob = [rv_model.pmf(x) for x in rv_value]
    plt.vlines(rv_value, 0, prob, label="Geometric")
    plt.show()


def bernouli_compute(p):
    rv_model = probability.bernouli(p)
    rv_value = [0, 1]
    prob = rv_model.pmf()
    plt.vlines(rv_value, 0, prob, label="Bernouli")
    plt.show()


def poisson_compute(lambdaa, n):
    rv_model = probability.poisson(lambdaa)
    rv_value = list(range(n+1))
    prob = [rv_model.pmf(x) for x in rv_value]
    plt.vlines(rv_value, 0, prob, label="Poisson")
    plt.show()

# ---------------------------Expect value for RV --------------------------


def bernouli_expect(p):
    rv_model = probability.bernouli(p)
    top = Tk()
    top.geometry("300x100")
    labelframe1 = LabelFrame(
        top, text="Bernouli expect value", font=("Arial", 12, "bold"))
    labelframe1.pack(fill="both", expand="yes")
    value = rv_model.E()
    toplabel = Label(
        labelframe1, text=f"E[x]={value}", font=("Arial", 10, "bold"))
    toplabel.pack()
    top.mainloop()


def binomial_expect(p, n):
    rv_model = probability.binomial(p, n)
    top = Tk()
    top.geometry("300x100")
    labelframe1 = LabelFrame(
        top, text="Binomial expect value", font=("Arial", 12, "bold"))
    labelframe1.pack(fill="both", expand="yes")
    value = rv_model.E()
    toplabel = Label(
        labelframe1, text=f"E[x]={value}", font=("Arial", 10, "bold"))
    toplabel.pack()
    top.mainloop()


def geometric_expect(p):
    rv_model = probability.geometric(p)
    top = Tk()
    top.geometry("300x100")
    labelframe1 = LabelFrame(
        top, text="Geometric expect value", font=("Arial", 12, "bold"))
    labelframe1.pack(fill="both", expand="yes")
    value = rv_model.E()
    toplabel = Label(
        labelframe1, text=f"E[x]={value}", font=("Arial", 10, "bold"))
    toplabel.pack()
    top.mainloop()


def poisson_expect(lambdaa):
    rv_model = probability.poisson(lambdaa)
    top = Tk()
    top.geometry("300x100")
    labelframe1 = LabelFrame(
        top, text="Poisson expect value", font=("Arial", 12, "bold"))
    labelframe1.pack(fill="both", expand="yes")
    value = rv_model.E()
    toplabel = Label(
        labelframe1, text=f"E[x]={value}", font=("Arial", 10, "bold"))
    toplabel.pack()
    top.mainloop()


def uniform_expect(a, b):
    rv_model = probability.uniform(a, b)
    top = Tk()
    top.geometry("300x100")
    labelframe1 = LabelFrame(
        top, text="Uniform expect value", font=("Arial", 12, "bold"))
    labelframe1.pack(fill="both", expand="yes")
    value = rv_model.E()
    toplabel = Label(
        labelframe1, text=f"E[x]={value}", font=("Arial", 10, "bold"))
    toplabel.pack()
    top.mainloop()

# ---------------------------var value for RV --------------------------


def bernouli_var(p):
    rv_model = probability.bernouli(p)
    top = Tk()
    top.geometry("300x100")
    labelframe1 = LabelFrame(
        top, text="Bernouli variance value", font=("Arial", 12, "bold"))
    labelframe1.pack(fill="both", expand="yes")
    value = rv_model.var()
    toplabel = Label(
        labelframe1, text=f"var[x]={value}", font=("Arial", 10, "bold"))
    toplabel.pack()
    top.mainloop()


def binomial_var(p, n):
    rv_model = probability.binomial(p, n)
    top = Tk()
    top.geometry("300x100")
    labelframe1 = LabelFrame(
        top, text="Binomial variance value", font=("Arial", 12, "bold"))
    labelframe1.pack(fill="both", expand="yes")
    value = rv_model.var()
    toplabel = Label(
        labelframe1, text=f"var[x]={value}", font=("Arial", 10, "bold"))
    toplabel.pack()
    top.mainloop()


def geometric_var(p):
    rv_model = probability.geometric(p)
    top = Tk()
    top.geometry("300x100")
    labelframe1 = LabelFrame(
        top, text="Geometric variance value", font=("Arial", 12, "bold"))
    labelframe1.pack(fill="both", expand="yes")
    value = rv_model.var()
    toplabel = Label(
        labelframe1, text=f"var[x]={value}", font=("Arial", 10, "bold"))
    toplabel.pack()
    top.mainloop()


def poisson_var(lambdaa):
    rv_model = probability.poisson(lambdaa)
    top = Tk()
    top.geometry("300x100")
    labelframe1 = LabelFrame(
        top, text="Poisson variance value", font=("Arial", 12, "bold"))
    labelframe1.pack(fill="both", expand="yes")
    value = rv_model.var()
    toplabel = Label(
        labelframe1, text=f"var[x]={value}", font=("Arial", 10, "bold"))
    toplabel.pack()
    top.mainloop()


def uniform_var(a, b):
    rv_model = probability.uniform(a, b)
    top = Tk()
    top.geometry("300x100")
    labelframe1 = LabelFrame(
        top, text="Uniform variance value", font=("Arial", 12, "bold"))
    labelframe1.pack(fill="both", expand="yes")
    value = rv_model.var()
    toplabel = Label(
        labelframe1, text=f"var[x]={value}", font=("Arial", 10, "bold"))
    toplabel.pack()
    top.mainloop()
# ------------------------ windows function ------------------------------


def bernouli_window():
    new_window = tk.Toplevel()
    new_window.title("bernouli")
    new_window.geometry("500x500+300+100")
    p = StringVar()
    Label(new_window, text="Enter the probability", font=(
        "Arial", 10, "bold")).grid(row=0, column=0)
    enter_probability = Entry(new_window, textvariable=p)
    enter_probability.grid(row=0, column=1)
    result = Button(new_window, text="The distribution of PMF",
                    command=lambda: bernouli_compute(float(p.get())), fg='blue', font=("Arial", 10, "bold")).place(x=150, y=50)
    expect_value = Button(new_window, text="E[x]",
                          command=lambda: bernouli_expect(float(p.get())), fg='blue', font=("Arial", 10, "bold")).place(x=150, y=80)
    variance_value = Button(new_window, text="var[x]",
                            command=lambda: bernouli_var(float(p.get())), fg='blue', font=("Arial", 10, "bold")).place(x=150, y=110)
    destroy_button = Button(new_window, text="Move back", fg='white', bg='red',
                            command=new_window.destroy, font=("Arial", 12, "bold")).place(x=400, y=0)
    new_window.mainloop()


def binomial_window():
    new_window = tk.Toplevel()
    new_window.title("Binomial")
    new_window.geometry("500x500+300+100")
    p = StringVar()
    n = StringVar()
    Label(new_window, text="Enter the probability", font=(
        "Arial", 10, "bold")).grid(row=0, column=0)
    enter_probability = Entry(new_window, textvariable=p)
    enter_probability.grid(row=0, column=1)
    Label(new_window, text="Enter number of trials",
          font=("Arial", 10, "bold")).grid(row=1, column=0)
    enter_trials = Entry(new_window, textvariable=n)
    enter_trials.grid(row=1, column=1)
    result = Button(new_window, text="The distribution of PMF",
                    command=lambda: binomial_compute(float(p.get()), int(n.get())), fg='blue', font=("Arial", 10, "bold")).place(x=150, y=50)
    expect_value = Button(new_window, text="E[x]",
                          command=lambda: binomial_expect(float(p.get()), int(n.get())), fg='blue', font=("Arial", 10, "bold")).place(x=150, y=80)
    variance_value = Button(new_window, text="var[x]",
                            command=lambda: binomial_var(float(p.get()), int(n.get())), fg='blue', font=("Arial", 10, "bold")).place(x=150, y=110)
    destroy_button = Button(new_window, text="Move back", fg='white', bg='red',
                            command=new_window.destroy, font=("Arial", 12, "bold")).place(x=400, y=0)
    new_window.mainloop()


def geometric_window():
    new_window = tk.Toplevel()
    new_window.title("Geometric")
    new_window.geometry("500x500+300+100")
    p = StringVar()
    n = StringVar()
    Label(new_window, text="Enter the probability", font=(
        "Arial", 10, "bold")).grid(row=0, column=0)
    enter_probability = Entry(new_window, textvariable=p)
    enter_probability.grid(row=0, column=1)
    Label(new_window, text="Enter number of trials",
          font=("Arial", 10, "bold")).grid(row=1, column=0)
    enter_trials = Entry(new_window, textvariable=n)
    enter_trials.grid(row=1, column=1)
    result = Button(new_window, text="The distribution of PMF",
                    command=lambda: geometric_compute(float(p.get()), int(n.get())), fg='blue', font=("Arial", 10, "bold")).place(x=150, y=50)
    expect_value = Button(new_window, text="E[x]",
                          command=lambda: geometric_expect(float(p.get())), fg='blue', font=("Arial", 10, "bold")).place(x=150, y=80)
    variance_value = Button(new_window, text="var[x]",
                            command=lambda: geometric_var(float(p.get())), fg='blue', font=("Arial", 10, "bold")).place(x=150, y=110)
    destroy_button = Button(new_window, text="Move back", fg='white', bg='red',
                            command=new_window.destroy, font=("Arial", 12, "bold")).place(x=400, y=0)
    new_window.mainloop()


def poisson_window():
    new_window = tk.Toplevel()
    new_window.title("Poisson")
    new_window.geometry("500x500+300+100")
    lambdaa = StringVar()
    n = StringVar()
    Label(new_window, text="Enter the lambda", font=(
        "Arial", 10, "bold")).grid(row=0, column=0)
    enter_probability = Entry(new_window, textvariable=lambdaa)
    enter_probability.grid(row=0, column=1)
    Label(new_window, text="Enter number of trials",
          font=("Arial", 10, "bold")).grid(row=1, column=0)
    enter_trials = Entry(new_window, textvariable=n)
    enter_trials.grid(row=1, column=1)
    result = Button(new_window, text="The distribution of PMF",
                    command=lambda: poisson_compute(float(lambdaa.get()), int(n.get())), fg='blue', font=("Arial", 10, "bold")).place(x=150, y=50)
    expect_value = Button(new_window, text="E[x]",
                          command=lambda: poisson_expect(float(lambdaa.get())), fg='blue', font=("Arial", 10, "bold")).place(x=150, y=80)
    variance_value = Button(new_window, text="var[x]",
                            command=lambda: poisson_var(float(lambdaa.get())), fg='blue', font=("Arial", 10, "bold")).place(x=150, y=110)
    destroy_button = Button(new_window, text="Move back", fg='white', bg='red',
                            command=new_window.destroy, font=("Arial", 12, "bold")).place(x=400, y=0)
    new_window.mainloop()


def uniform_window():
    new_window = tk.Toplevel()
    new_window.title("Uniform")
    new_window.geometry("500x500+300+100")
    a = StringVar()
    b = StringVar()
    Label(new_window, text="Enter the start of interval",
          font=("Arial", 10, "bold")).grid(row=0, column=0)
    enter_probability = Entry(new_window, textvariable=a)
    enter_probability.grid(row=0, column=1)
    Label(new_window, text="Enter the end of interval",
          font=("Arial", 10, "bold")).grid(row=1, column=0)
    enter_trials = Entry(new_window, textvariable=b)
    enter_trials.grid(row=1, column=1)
    result = Button(new_window, text="The distribution of PMF",
                    command=lambda: uniform_compute(int(a.get()), int(b.get())), fg='blue', font=("Arial", 10, "bold")).place(x=150, y=50)
    expect_value = Button(new_window, text="E[x]",
                          command=lambda: uniform_expect(int(a.get()), int(b.get())), fg='blue', font=("Arial", 10, "bold")).place(x=150, y=80)
    variance_value = Button(new_window, text="var[x]",
                            command=lambda: uniform_var(int(a.get()), int(b.get())), fg='blue', font=("Arial", 10, "bold")).place(x=150, y=110)
    destroy_button = Button(new_window, text="Move back", fg='white', bg='red',
                            command=new_window.destroy, font=("Arial", 12, "bold")).place(x=400, y=0)
    new_window.mainloop()

# ------------------------ The main window -------------------------------


windos = Tk()
windos.geometry("500x500+300+100")
windos.title("Probability")


def create_circle_button(canvas, x, y, radius, text, command):
    button = canvas.create_oval(
        x-radius, y-radius, x+radius, y+radius, fill='teal', outline='black')
    canvas.create_text(x, y, text=text, font=("Arial", 10, "bold"))
    canvas.tag_bind(button, "<Button-1>", lambda event: command())


canvas = tk.Canvas(windos, width=450, height=700)
canvas.pack()

Label(windos, text="Types of Random Variable", fg='black',
      font=("Arial", 16, "bold")).place(x=102, y=0)


create_circle_button(canvas, 215, 70, 35, "Bernouli", bernouli_window)
create_circle_button(canvas, 215, 145, 35, "Binomial", binomial_window)
create_circle_button(canvas, 215, 220, 35, "Geometric", geometric_window)
create_circle_button(canvas, 215, 295, 35, "Poisson", poisson_window)
create_circle_button(canvas, 215, 370, 35, "Uniform", uniform_window)


def on_button_click():
    result = messagebox.askquestion("Confirm", "Are you sure?")

    if result == 'yes':
        print("User confirmed.")
        sys.exit(0)

    else:
        print("User canceled.")


destroy_button = Button(windos, text='End', fg='white', bg='red',
                        command=on_button_click, font=("Arial", 16, "bold")).place(x=211, y=430)

windos.mainloop()

# --------------------------------------------------------------
