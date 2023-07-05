from getpass import getpass
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as mb
import bd as bd

user = input("Имя пользователя: ")
password = getpass("Пароль (скрыт): ")
#if getpass does not work for you in pycharm, try editing run/debug configurations - turn on execution/ emulate terminal in output console

root = Tk()
ttk.Style().configure("TLabel", font="helvetica 13", padding=2, background="#71C9CE", foreground="#E3FDFD")
ttk.Style().configure("TButton", font="helvetica 10", background="#3DC2C7", foreground="#222831")
x, y = (root.winfo_screenwidth() // 2) - (750 // 2), (root.winfo_screenheight() // 2) - (450 // 2)
root.geometry(f"{750}x{450}+{x}+{y}")
root.title("Информационная система, Орлов Дмитрий, студент группы 7221-12")

frame = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)

root["bg"] = frame["bg"] = frame2["bg"] = frame3["bg"] = "#71C9CE"

frame2.pack(expand=True, fill=BOTH)
frame.pack(expand=True)
frame3.pack(expand=True)


def create_window():
    global window, window_frame, entr2, entr3, entr4, entr5

    window = tk.Toplevel(root)
    x, y = (window.winfo_screenwidth() // 2) - (500 // 2), (window.winfo_screenheight() // 2) - (300 // 2)
    window.geometry(f"{500}x{300}+{x}+{y}")
    window.title("Добавить квартиру")
    window_frame = Frame(window)
    window_frame.pack(expand=True)
    window["bg"] = window_frame["bg"] = "#71C9CE"

    ttk.Label(window_frame, text="Площадь: ").grid(row=0, column=0)

    entr2 = ttk.Entry(window_frame)
    entr2.grid(row=0, column=1)

    ttk.Label(window_frame, text="Кол-во комнат: ").grid(row=1, column=0)

    entr3 = ttk.Entry(window_frame)
    entr3.grid(row=1, column=1)

    ttk.Label(window_frame, text="Цена за месяц: ").grid(row=2, column=0)

    entr4 = ttk.Entry(window_frame)
    entr4.grid(row=2, column=1)

    ttk.Label(window_frame, text="Адрес: ").grid(row=3, column=0)

    entr5 = ttk.Entry(window_frame)
    entr5.grid(row=3, column=1)

    ttk.Button(window_frame, text="Добавить квартиру ", command=button4_click).grid(row=4, column=0, columnspan=2,
                                                                                    pady=5, ipadx=10)


def func():
    global s, l, entry1, entry2
    s, l = bd.connection_(password, user)

    for widgets in [frame.winfo_children(), frame3.winfo_children(), frame2.winfo_children()]:
        for widget in widgets:
            widget.destroy()

    ttk.Label(frame, text="Логин:").grid(row=0, column=0)

    entry1 = ttk.Entry(frame)
    entry1.grid(row=0, column=1, padx=10)

    ttk.Label(frame, text="Пароль:").grid(row=1, column=0)

    entry2 = ttk.Entry(frame)
    entry2.grid(row=1, column=1, padx=10)

    ttk.Button(frame, text="Войти", command=button1_click).grid(row=2, column=1, pady=10, ipadx=22)

    ttk.Button(frame, text="Зарегистрироваться", command=button2_click).grid(row=3, column=1)

    root.update_idletasks()

    root.mainloop()


def table():
    global tree

    def sort(col, reverse, key=str):
        m = [(tree.set(k, col), k) for k in tree.get_children()]
        m.sort(reverse=reverse, key=lambda t: key(t[0]))
        for index, (_, k) in enumerate(m):
            tree.move(k, "", index)
        tree.heading(col, command=lambda: sort(col, not reverse, key=key))

    columns = ("Номер", "Площадь", "Кол-во комнат", "Цена за месяц", "Адрес")
    tree = ttk.Treeview(columns=columns, show="headings")
    scrollbar = ttk.Scrollbar(orient="vertical", command=tree.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    tree["yscrollcommand"] = scrollbar.set
    tree.pack(anchor=N, expand=True, fill=BOTH, ipady=100)
    tree.heading("Номер", text="ID", anchor=W, command=lambda: sort(0, False, key=int))
    tree.heading("Площадь", text="Площадь", anchor=W, command=lambda: sort(1, False, key=float))
    tree.heading("Кол-во комнат", text="Кол-во комнат", anchor=W, command=lambda: sort(2, False, key=int))
    tree.heading("Цена за месяц", text="Цена за месяц", anchor=W, command=lambda: sort(3, False, key=int))
    tree.heading("Адрес", text="Адрес", anchor=W, command=lambda: sort(4, False))
    tree.column("#1", width=5), tree.column("#2", width=60), tree.column("#3", width=100), \
        tree.column("#4", width=100), tree.column("#5", width=120)
    for apartment in s:
        tree.insert("", END, values=apartment)

    def search_apartments():
        def search():
            area = entr_area.get()
            rooms = entr_rooms.get()
            price = entr_price.get()

            filtered_apartments = []

            for apartment in s:
                if (area and float(apartment[1]) != float(area)) or \
                        (rooms and int(apartment[2]) != int(rooms)) or \
                        (price and int(apartment[3]) != int(price)):
                    continue
                filtered_apartments.append(apartment)

            tree.delete(*tree.get_children())

            for apartment in filtered_apartments:
                tree.insert("", END, values=apartment)

        create_window()
        window.title("Поиск")
        for widget in window_frame.winfo_children():
            widget.destroy()

        ttk.Label(window_frame, text="Площадь:").grid(row=0, column=0)

        entr_area = ttk.Entry(window_frame)
        entr_area.grid(row=0, column=1)

        ttk.Label(window_frame, text="Кол-во комнат:").grid(row=2, column=0)

        entr_rooms = ttk.Entry(window_frame)
        entr_rooms.grid(row=2, column=1)

        ttk.Label(window_frame, text="Цена за месяц:").grid(row=3, column=0)

        entr_price = ttk.Entry(window_frame)
        entr_price.grid(row=3, column=1)

        ttk.Button(window_frame, text="Поиск", command=search).grid(row=4, column=0, pady=5)

    ttk.Button(frame2, text="Поиск", command=search_apartments).pack(side=LEFT, padx=5, pady=5)

    # для работы с ролью администратора добавьте в бд users пользователя с логином (first_name) admin
    # add 'admin' in 'users' database 
    
    if a == 'admin':
        ttk.Button(frame2, text="Добавить квартиру", command=create_window).pack(side=LEFT, padx=5)

        def edit_apartment(event):
            selected_item = tree.selection()
            if not selected_item:
                return

            apartment_data = tree.item(selected_item)["values"]
            create_window()
            window.title("Редактирование")
            for widget in window_frame.winfo_children():
                widget.destroy()

            ttk.Label(window_frame, text="Площадь: ").grid(row=0, column=0)

            entr_edit_area1 = ttk.Entry(window_frame)
            entr_edit_area1.grid(row=0, column=1)

            ttk.Label(window_frame, text="Кол-во комнат: ").grid(row=1, column=0)

            entr_edit_area2 = ttk.Entry(window_frame)
            entr_edit_area2.grid(row=1, column=1)

            ttk.Label(window_frame, text="Цена за месяц: ").grid(row=2, column=0)

            entr_edit_area3 = ttk.Entry(window_frame)
            entr_edit_area3.grid(row=2, column=1)

            ttk.Label(window_frame, text="Адрес: ").grid(row=3, column=0)

            entr_edit_area4 = ttk.Entry(window_frame)
            entr_edit_area4.grid(row=3, column=1)

            def edit_button_click():
                a_1, a_2, a_3, a_4 = entr_edit_area1.get(), entr_edit_area2.get(), entr_edit_area3.get(), entr_edit_area4.get()
                arr = [a_1, a_2, a_3, a_4]
                confirmation = mb.askyesno("Подтверждение", "Вы уверены, что хотите применить изменения?")
                if not confirmation:
                    return
                for i in range(len(arr)):
                    if arr[i] != '':
                        apartment_data[i + 1] = arr[i]
                tree.item(selected_item, values=apartment_data)
                bd.edit_apartment_bd(password, user, apartment_data)
                window.destroy()

            ttk.Button(window_frame, text="Подтвердить", command=edit_button_click).grid(row=4, column=1, pady=7)

        def delete_apartment():
            selected_item = tree.selection()
            if not selected_item:
                return
            apartment_data = tree.item(selected_item)["values"]
            apartment_id = apartment_data[0]
            confirmation = mb.askyesno("Подтверждение", "Вы уверены, что хотите удалить выбранную квартиру?")
            if not confirmation:
                return
            tree.delete(selected_item)
            bd.delete_apartment_bd(password, user, apartment_id)

        def delete_apartment_del(event):
            delete_apartment()

        ttk.Button(frame2, text="Удалить квартиру", command=delete_apartment).pack(side=LEFT, pady=5, padx=5)

        tree.bind("<Double-1>", edit_apartment)
        tree.bind("<Delete>", delete_apartment_del)


def button1_click():
    global a
    a = entry1.get()
    b = entry2.get()
    if (a, b) in l:
        frame.destroy()
        table()
    else:
        mb.showwarning("Ошибка", 'Данные введены неверно')


def button2_click():
    global ent1, ent2, ent3
    for widget in frame.winfo_children():
        widget.destroy()

    ttk.Label(frame, text="Придумайте логин:").grid(row=0, column=0, sticky=W)

    ent1 = ttk.Entry(frame)
    ent1.grid(row=0, column=1)

    ttk.Label(frame, text="Придумайте пароль:").grid(row=1, column=0, sticky=W)

    ent2 = ttk.Entry(frame)
    ent2.grid(row=1, column=1)

    ttk.Label(frame, text="Подтвердите пароль:").grid(row=2, column=0, sticky=W)

    ent3 = ttk.Entry(frame)
    ent3.grid(row=2, column=1)

    ttk.Button(frame, text="Подтвердить", command=button3_click).grid(row=3, column=1, pady=10, ipadx=20)

    ttk.Label(frame2).grid(row=0, column=0)

    ttk.Button(frame3, text="Назад", command=func).grid(row=0, column=1, padx=100, sticky=NW)


def button3_click():
    if ent2.get() == ent3.get() and ent2.get() != '':
        for i in l:
            if ent1.get() == i[0]:
                mb.showwarning('Ошибка', 'Вы уже зарегистрированы')
                func()
                break
        else:
            bd.add_user(password, user, ent1.get(), ent2.get())
            mb.showinfo('Регистрация успешна', 'Вы успешно зарегистрированы')
            func()
    else:
        mb.showwarning('Ошибка', 'Пароли не совпадают')


def button4_click():
    new_s, _ = bd.connection_(password, user)
    a_1, a_2, a_3, a_4 = entr2.get(), entr3.get(), entr4.get(), entr5.get()
    c = bd.add_apartment(password, user, a_1, a_2, a_3, a_4)
    if c:
        mb.showinfo('Успешно!', 'Успешно добавлено')
        window.destroy()
        tree.insert("", END, values=(new_s[-1][0] + 1, a_1, a_2, a_3, a_4))
    else:
        mb.showwarning('Ошибка', 'Все поля должны быть заполнены!')


if __name__ == '__main__':
    func()
