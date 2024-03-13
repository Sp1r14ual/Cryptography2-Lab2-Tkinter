from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
from scramblers import get_gamma
from xor import xor, random_key

def click_button():
    message_filename = message_entry.get()
    message_file = None
    message = None

    key_filename = key_entry.get()
    key_file = None
    key = None

    init_state_filename = init_state_entry.get()
    init_state_file = None
    init_state = None

    try:
        if not (".txt" in message_filename):
            raise FileExistsError("Некорректное имя файла")

        if not (".txt" in key_filename):
            raise FileExistsError("Некорректное имя файла")

        if not (".txt" in init_state_filename) and ScramblerOption.get() != "Random":
            raise FileExistsError("Некорректное имя файла")

        if ModeOption.get() == "Decode":
            try:
                key_filename = key_entry.get()
                key_file = open(key_filename, "r")
                key = key_file.read()
            except:
                raise FileNotFoundError("Не удалось открыть файл")

        if ScramblerOption.get() in ("First", "Second"):
            try:
                init_state_file = open(init_state_filename, "r")
                init_state = init_state_file.read()
                init_state = int(init_state, base=2) if init_state[:2] == "0b" else int(init_state)
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
            key = get_gamma(len(message), init_state, "First")
        elif ScramblerOption.get() == "Random":
            key = random_key(len(message))
        else:
            key = get_gamma(len(message), init_state, "Second")
        with open("key.txt", mode="w", encoding="utf-8") as key_file:
            key_file.write(key)


    result = xor(message, key)

    with open("output.txt", mode="w", encoding="utf-8") as output_file:
        output_file.write(result)


    showinfo("Выполнено", "Результат работы программы записаны в файлы key.txt и output.txt")

    return

def change_key():
    key = None
    with open("key.txt", mode="r", encoding="utf-8") as key_file:
        key = key_file.read()

    key_edit_entry.delete(0, "end")

    if key[:2] == "0b":
        key = int(key, base=2)
    elif key[:2] == "0x":
        key = int(key, base=16)
    else:
        key = int(key)

    if KeyViewOption.get() == "Binary":
        key_edit_entry.insert(0, bin(key))
    elif KeyViewOption.get() == "Hexadecimal":
        key_edit_entry.insert(0, hex(key))
    else:
        key_edit_entry.insert(0, str(key))


def save_key():
    key = key_edit_entry.get()
    with open("key.txt", mode="w", encoding="utf-8") as key_file:
        key_file.write(key)

def change_init_state():
    init_state = None
    with open("init_state.txt", mode="r", encoding="utf-8") as init_state_file:
        init_state = init_state_file.read()

    init_state_edit_entry.delete(0, "end")

    if StateViewOption.get() == "Binary":
        init_state_edit_entry.insert(0, bin(int(init_state, base=2)))
    elif StateViewOption.get() == "Hexadecimal":
        init_state_edit_entry.insert(0, hex(int(init_state, base=2)))
    else:
        init_state_edit_entry.insert(0, str(int(init_state, base=2)))


def save_init_state():
    pass

root = Tk()
root.title("XOR Cipher")
root.geometry("600x600+200+150")
root.resizable(False, False)

message_label = ttk.Label(text="Файл с сообщением", font=("Arial", 14))
message_label.grid(row=0, column=0)

message_entry = ttk.Entry(justify=CENTER)
message_entry.grid(row=1, column=0, pady=10)

key_label = ttk.Label(text="Файл с ключом", font=("Arial", 14))
key_label.grid(row=2, column=0)

key_entry = ttk.Entry(justify=CENTER)
key_entry.grid(row=3, column=0, pady=10)

init_state_label = ttk.Label(text="Файл с нач.сост. скремблера", font=("Arial", 14))
init_state_label.grid(row=4, column=0)

init_state_entry = ttk.Entry(justify=CENTER)
init_state_entry.grid(row=5, column=0, pady=10)

scrambler_label = ttk.Label(
    text="Генерация ключа", font=("Arial", 14))
scrambler_label.grid(row=6, column=0)

ScramblerOption = StringVar(value="First")

RandomKeyOption = ttk.Radiobutton(
    text="Случайный ключ", value="Random", variable=ScramblerOption)
RandomKeyOption.grid(row=7, column=0, pady=10)

FirstScramblerOption = ttk.Radiobutton(
    text="Скремблер 1", value="First", variable=ScramblerOption)
FirstScramblerOption.grid(row=8, column=0)

SecondScramblerOption = ttk.Radiobutton(
    text="Скремблер 2", value="Second", variable=ScramblerOption)
SecondScramblerOption.grid(row=9, column=0, pady=10)

mode_label = ttk.Label(text="Режим работы", font=("Arial", 14))
mode_label.grid(row=10, column=0)

ModeOption = StringVar(value="Encode")

EncodeOption = ttk.Radiobutton(
    text="Зашифровать", value="Encode", variable=ModeOption)
EncodeOption.grid(row=11, column=0, pady=10)

DecodeOption = ttk.Radiobutton(
    text="Дешифровать", value="Decode", variable=ModeOption)
DecodeOption.grid(row=12, column=0)

btn = ttk.Button(text="Пуск", command=click_button)
btn.grid(row=13, column=0, pady=10)

key_edit_label = ttk.Label(text="Ключ", font=("Arial", 14))
key_edit_label.grid(row=0, column=1)

key_edit_entry = ttk.Entry(justify=CENTER)
key_edit_entry.grid(row=1, column=1)

KeyViewOption = StringVar(value="Binary")

KeyBinaryViewOption = ttk.Radiobutton(
    text="Двоичный вид", value="Binary", variable=KeyViewOption)
KeyBinaryViewOption.grid(row=2, column=1)

KeyHexViewOption = ttk.Radiobutton(
    text="Шестнадцатеричный вид", value="Hexadecimal", variable=KeyViewOption)
KeyHexViewOption.grid(row=3, column=1)

KeySymbolicViewOption = ttk.Radiobutton(
    text="Символьный вид", value="Symbolic", variable=KeyViewOption)
KeySymbolicViewOption.grid(row=4, column=1)

show_key_button = ttk.Button(text="Показать", command=click_button)
show_key_button.grid(row=5, column=1)

save_key_button = ttk.Button(text="Сохранить", command=click_button)
save_key_button.grid(row=6, column=1)

KeyViewOption = StringVar(value="Binary")

KeyBinaryViewOption = ttk.Radiobutton(
    text="Двоичный вид", value="Binary", variable=KeyViewOption)
KeyBinaryViewOption.grid(row=2, column=1)

KeyHexViewOption = ttk.Radiobutton(
    text="Шестнадцатеричный вид", value="Hexadecimal", variable=KeyViewOption)
KeyHexViewOption.grid(row=3, column=1)

KeySymbolicViewOption = ttk.Radiobutton(
    text="Символьный вид", value="Symbolic", variable=KeyViewOption)
KeySymbolicViewOption.grid(row=4, column=1)

show_key_button = ttk.Button(text="Показать", command=change_key)
show_key_button.grid(row=5, column=1)

save_key_button = ttk.Button(text="Сохранить", command=save_key)
save_key_button.grid(row=6, column=1)

init_state_edit_label = ttk.Label(text="Нач. состояние скремблера", font=("Arial", 14))
init_state_edit_label.grid(row=7, column=1)

init_state_edit_entry = ttk.Entry(justify=CENTER)
init_state_edit_entry.grid(row=8, column=1)

StateViewOption = StringVar(value="Binary")

StateBinaryViewOption = ttk.Radiobutton(
    text="Двоичный вид", value="Binary", variable=StateViewOption)
StateBinaryViewOption.grid(row=9, column=1)

StateHexViewOption = ttk.Radiobutton(
    text="Шестнадцатеричный вид", value="Hexadecimal", variable=StateViewOption)
StateHexViewOption.grid(row=10, column=1)

StateSymbolicViewOption = ttk.Radiobutton(
    text="Символьный вид", value="Symbolic", variable=StateViewOption)
StateSymbolicViewOption.grid(row=11, column=1)

show_init_state_button = ttk.Button(text="Показать", command=change_init_state)
show_init_state_button.grid(row=12, column=1)

save_init_state_button = ttk.Button(text="Сохранить", command=save_init_state)
save_init_state_button.grid(row=13, column=1)

root.mainloop()
