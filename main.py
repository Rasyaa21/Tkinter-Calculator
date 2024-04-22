from tkinter import *

def button_press(num):
    global placeHolderText  # Mengakses variabel global placeHolderText
    placeHolderText = placeHolderText + str(num)  # Menggabungkan angka yang ditekan ke teks placeholder yang ada
    placeHolderLabel.set(placeHolderText)  # mengupdate label dari text place holder yang sudah ada


def equals():
    global placeHolderText
    try:
        # mengubah expresi logika dalam string menjadi arithmatic
        total = str(eval(placeHolderText))
        # Mengatur label placeholder untuk menampilkan hasil
        placeHolderLabel.set(total)
        # Memperbarui placeHolderText dengan hasilnya
        placeHolderText = total
    except ZeroDivisionError:
        placeHolderLabel.set("Error")
        placeHolderText = ""

    except SyntaxError:
        placeHolderLabel.set("Syntax Error")
        placeHolderText = ""

def clear():
    global placeHolderText
    placeHolderText = ""
    placeHolderLabel.set(placeHolderText)


root = Tk()

root.geometry("700x700")
root.title("Calculator")

placeHolderText = ""

placeHolderLabel = StringVar()

label = Label(
    root,
    textvariable=placeHolderLabel,
    font=("Arial", 20, "bold"),
    bg="white",
    width=30,
    height=2
)
label.pack()

frame = Frame(root)
frame.pack()

button1 = Button(
    frame,
    text=1,
    height=2,
    width=5,
    font=("Arial", 30, "bold"),
    command= lambda:button_press(1)
)
button1.grid(row=0, column=0)

button2 = Button(
    frame,
    text=2,
    height=2,
    width=5,
    font=("Arial", 30, "bold"),
    command= lambda:button_press(2)
)
button2.grid(row=0, column=1)

button3 = Button(
    frame,
    text=3,
    height=2,
    width=5,
    font=("Arial", 30, "bold"),
    command= lambda:button_press(3)
)
button3.grid(row=0, column=2)

button4 = Button(
    frame,
    text=4,
    height=2,
    width=5,
    font=("Arial", 30, "bold"),
    command= lambda:button_press(4)
)
button4.grid(row=1, column=0)

button5 = Button(
    frame,
    text=5,
    height=2,
    width=5,
    font=("Arial", 30, "bold"),
    command= lambda:button_press(5)
)
button5.grid(row=1, column=1)

button6 = Button(
    frame,
    text=6,
    height=2,
    width=5,
    font=("Arial", 30, "bold"),
    command= lambda:button_press(6)
)
button6.grid(row=1, column=2)

button7 = Button(
    frame,
    text=7,
    height=2,
    width=5,
    font=("Arial", 30, "bold"),
    command= lambda:button_press(7)
)
button7.grid(row=2, column=0)

button8 = Button(
    frame,
    text=8,
    height=2,
    width=5,
    font=("Arial", 30, "bold"),
    command= lambda:button_press(8)
)
button8.grid(row=2, column=1)

button9 = Button(
    frame,
    text=9,
    height=2,
    width=5,
    font=("Arial", 30, "bold"),
    command= lambda:button_press(9)
)
button9.grid(row=2, column=2)

button10 = Button(
    frame,
    text=0,
    height=2,
    width=5,
    font=("Arial", 30, "bold"),
    command= lambda:button_press(9)
)
button10.grid(row=3, column=0)

buttonPlus = Button(
    frame,
    text="+",
    height=2,
    width=5,
    font=("Arial", 30, "bold"),
    command= lambda:button_press("+")
)
buttonPlus.grid(row=0, column=3)

buttonMinus = Button(
    frame,
    text="-",
    height=2,
    width=5,
    font=("Arial", 30, "bold"),
    command= lambda:button_press("-")
)
buttonMinus.grid(row=1, column=3)

buttonMultiply = Button(
    frame,
    text="x",
    height=2,
    width=5,
    font=("Arial", 30, "bold"),
    command= lambda:button_press("*")
)
buttonMultiply.grid(row=2, column=3)

buttonDivide = Button(
    frame,
    text="/",
    height=2,
    width=5,
    font=("Arial", 30, "bold"),
    command= lambda:button_press("/")
)
buttonDivide.grid(row=3, column=3)

buttonSum = Button(
    frame,
    text="=",
    height=2,
    width=21,
    font=("Arial", 30, "bold"),
    command= equals
)
buttonSum.grid(row=4, column=0, columnspan=4)

buttonClear = Button(
    frame,
    text="C",
    height=2,
    width=5,
    font=("Arial", 30, "bold"),
    command=clear
)
buttonClear.grid(row=3, column=2)

buttonDecimal = Button(
    frame,
    text=".",
    height=2,
    width=5,
    font=("Arial", 30, "bold"),
    command=lambda :button_press(".")
)
buttonDecimal.grid(row=3, column=1)

root.mainloop()