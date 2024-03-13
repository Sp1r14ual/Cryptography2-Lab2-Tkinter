from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
from scramblers import get_gamma
from xor import xor

def click_button():
    message_filename = message_entry.get()
    message_file = None
    message = None
    key_filename = None
    key_file = None
    key = None

    try:
        if not (".txt" in message_filename):
            raise FileExistsError("Некорректное имя файла")

        if ModeOption.get() == "Decode":
            try:
                key_filename = key_entry.get()
                key_file = open(key_filename, "r")
            except:
                raise FileNotFoundError("Не удалось открыть файл")

        try:
            message_file = open(message_filename, "r")
        except:
            raise FileNotFoundError("Не удалось открыть файл")

    except Exception as E:
        showerror("Ошибка", str(E))
        return

    message = message_file.read()
    if ModeOption.get() == "Encode":
        if ScramblerOption.get() == "First":
            key = get_gamma(len(message), "First")
        else:
            key = get_gamma(len(message), "Second")
    else:
        key = key_file.read()

    with open("key.txt", mode="w", encoding="utf-8") as key_file:
        key_file.write(key)

    result = xor(message, key)

    with open("output.txt", mode="w", encoding="utf-8") as output_file:
        output_file.write(result)


    showinfo("Выполнено", "Результат работы программы записаны в файлы key.txt и output.txt")

    return


root = Tk()
root.title("XOR Cipher")
root.geometry("400x500+200+150")

root.resizable(False, False)

message_label = ttk.Label(text="Файл с сообщением", font=("Arial", 14))
message_label.pack(pady=10)

message_entry = ttk.Entry(justify=CENTER)
message_entry.pack()

key_label = ttk.Label(text="Файл с ключом (при декодировании)", font=("Arial", 14))
key_label.pack(pady=10)

key_entry = ttk.Entry(justify=CENTER)
key_entry.pack()

scrambler_label = ttk.Label(
    text="Скремблер", font=("Arial", 14))
scrambler_label.pack(pady=10)

ScramblerOption = StringVar(value="First")

FirstScramblerOption = ttk.Radiobutton(
    text="Скремблер 1", value="First", variable=ScramblerOption)
FirstScramblerOption.pack(ipady=5)

SecondScramblerOption = ttk.Radiobutton(
    text="Скремблер 2", value="Second", variable=ScramblerOption)
SecondScramblerOption.pack()

mode_label = ttk.Label(text="Режим работы", font=("Arial", 14))
mode_label.pack(pady=10)

ModeOption = StringVar(value="Encode")

EncodeOption = ttk.Radiobutton(
    text="Зашифровать", value="Encode", variable=ModeOption)
EncodeOption.pack(ipady=5)

DecodeOption = ttk.Radiobutton(
    text="Дешифровать", value="Decode", variable=ModeOption)
DecodeOption.pack()

btn = ttk.Button(text="Пуск", command=click_button)
btn.pack(pady=10)

root.mainloop()