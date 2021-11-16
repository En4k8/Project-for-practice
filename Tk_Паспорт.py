from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox

def btn_Doing(event=None):
    from datetime import datetime

    NowDay = datetime.now().day
    NowMonth = datetime.now().month
    NowYear = datetime.now().year   
    
    Dy = int(d.get())
    Mnth = int(m.get())
    Yr = int(y.get())
    
    if Mnth > 12:
        messagebox.WARNING(title = "Ошибка", message = 'Введите правильное число месяца')

    month_in_day = 0
    monthN_in_day = 0
    if Mnth == 1:
        month_in_day += 31
    elif Mnth == 2:
        month_in_day += 59
    elif Mnth == 3:
        month_in_day += 90
    elif Mnth == 4:
        month_in_day += 120
    elif Mnth == 5:
        month_in_day += 151
    elif Mnth == 6:
        month_in_day += 181
    elif Mnth == 7:
        month_in_day += 212
    elif Mnth == 8:
        month_in_day += 243
    elif Mnth == 9:
        month_in_day += 273
    elif Mnth == 10:
        month_in_day += 304
    elif Mnth == 11:
        month_in_day += 334
    elif Mnth == 12:
        month_in_day += 365
        
    if NowMonth == 1:
        monthN_in_day += 31
    elif NowMonth == 2:
        monthN_in_day += 59
    elif NowMonth == 3:
        monthN_in_day += 90
    elif NowMonth == 4:
        monthN_in_day += 120
    elif NowMonth == 5:
        monthN_in_day += 151
    elif NowMonth == 6:
        monthN_in_day += 181
    elif NowMonth == 7:
        monthN_in_day += 212
    elif NowMonth == 8:
        monthN_in_day += 243
    elif NowMonth == 9:
        monthN_in_day += 273
    elif NowMonth == 10:
        monthN_in_day += 304
    elif NowMonth == 11:
        monthN_in_day += 334
    elif NowMonth == 12:
        monthN_in_day += 365
        
    Fs = str(first.get())
    Scnd = str(second.get())
    Mdll = str(middle.get())
    
    Let = NowYear - Yr
    
    first_pasport = 14
    second_pasport = 20
    third_pasport = 45
    
    if Let <= 14:
        Ostalos1 = (((first_pasport - Let) *365) - ((monthN_in_day + NowDay) - (month_in_day + Dy)))#рассчитываю время сколько осталось до замены паспорта, если ждать придётся её несколько лет
    elif Let <= 20:
        Ostalos1 = (((second_pasport - Let) *365) - ((monthN_in_day + NowDay) - (month_in_day + Dy)))
    elif Let <=45:
        Ostalos1 = (((third_pasport - Let) *365) - ((monthN_in_day + NowDay) - (month_in_day + Dy)))
        
    Ostalos2 = 31 - Dy
    
    if Mnth > 12 or Dy > 31 or Yr > NowYear:
        messagebox.showinfo(title = "Ошибка", message = 'Введите правильное число месяца или дня, а также проверьте, правильно ли написан год, он не должен превышать текущий год')
    elif Let < 14:
        messagebox.showinfo(title = 'Результат', message = 'Здравствуйте '+Fs+ ' ' +Scnd+ ' ' +Mdll+ '. Вам ' + str(NowYear - Yr)+ ' лет. Ваш первый паспорт вы сможете получить через '+ str(Ostalos1) + ' дней в ближайщем МФЦ. У вас также будет 30 дней на то, чтобы успеть получить свой паспорт, Если вы не успеете, на вас будет наложен штраф.')
    elif Let == 14:
        messagebox.showinfo(title = 'Результат', message = 'Здравствуйте '+Fs+ ' ' +Scnd+ ' ' +Mdll+'. Вам ' + str(NowYear - Yr)+ ' лет. Через '+ str(Ostalos2) + ' день Вам необходимо обратиться в ближайший МФЦ для замены паспорта. Если вы не поменяете паспорт в течении 30 дней, на Вас будет наложен штраф.')
    elif Let < 20:
        messagebox.showinfo(title = 'Результат', message = 'Здравствуйте '+Fs+ ' ' +Scnd+ ' ' +Mdll+'. Вам ' + str(NowYear - Yr)+ ' лет. Ваш второй паспорт вы сможете получить через '+ str(Ostalos1) +' дней в ближайшем МФЦ. У вас также будет 90 дней на то, чтобы сменить свой паспорт. Если вы не успеете, на вас будет наложен штраф.')
    elif Let == 20:
        messagebox.showinfo(title = 'Результат', message = 'Здравствуйте '+Fs+ ' ' +Scnd+ ' ' +Mdll+'. Вам ' + str(NowYear - Yr)+ ' лет. Через '+ str(Ostalos1)+ ' день Вам необходимо обратиться в ближайший МФЦ для замены паспорта. Если вы не поменяете паспорт в течении 90 дней, на Вас будет наложен штраф.')
    elif Let < 45:
        messagebox.showinfo(title = 'Результат', message = 'Здравствуйте '+Fs+ ' ' +Scnd+ ' ' +Mdll+'. Вам ' + str(NowYear - Yr)+ ' лет. Ваш третий паспорт вы сможете получить через '+ str(Ostalos1) +' дней в ближайшем МФЦ. У вас также будет 90 дней на то, чтобы сменить свой паспорт. Если вы не успеете, на вас будет наложен штраф. ')
    elif Let == 45:
        messagebox.showinfo(title = 'Результат', message = 'Здравствуйте '+Fs+ ' ' +Scnd+ ' ' +Mdll+'. Вам ' + str(NowYear - Yr)+ ' лет. Через '+ str(Ostalos1)+ ' день Вам необходимо обратиться в ближайший МФЦ для замены паспорта. Если вы не поменяете паспорт в течении 90 дней, на Вас будет наложен штраф.')
    elif Let > 45:
        messagebox.showinfo(title = 'Результат', message = 'Здравствуйте '+Fs+ ' ' +Scnd+ ' ' +Mdll+'. Вам ' + str(NowYear - Yr)+ ' лет. Вам не нужно менять ваш паспорт, он у вас теперь до коцна жизни.')  

window = Tk()
window.geometry('240x250')
window.title('Паспорта')
                       
inf = Label (window, text = 'ФИО ПОЛЬЗОВАТЕЛЯ:', font = 15)
inf.place(x = 4, y = 2)        
data = Label (window, text = 'ДАТА РОЖДЕНИЯ:', font = 5)
data.place (x = 25,y = 120)
imya = Label(window, text = 'Имя')
imya.place(y = 38)
familia = Label (window, text = 'Фамилия')
familia.place(y = 64)
otchestvo = Label (window, text = 'Отчество')
otchestvo.place (y = 89)

Day = Label (window, text = 'День')
Day.place (y =155)
Month = Label (window, text = 'Месяц')
Month.place (x = 50,y = 155)
Year = Label (window, text = 'Год')
Year.place (x = 100, y = 155)

first = StringVar()
first_name = Entry(textvariable = first)
first_name.place(x = 80 , y = 38)
second = StringVar()
second_name = Entry(textvariable = second)
second_name.place(x =80 ,y = 64 )
middle = StringVar()
middle_name = Entry(textvariable = middle)
middle_name.place(x = 80, y = 89)

d = IntVar()
day = Entry(window,textvariable = d)
day.place (x = 3,y = 180)
m = IntVar()
month = Entry(window,textvariable = m)
month.place (x = 52,y = 180)
y = IntVar()
year = Entry(window,textvariable = y)
year.place (x = 102,y = 180)
    
Doing = Button(window, text = 'Выполнить', command = btn_Doing)
Doing.place(x = 80, y = 214)

window.mainloop()
