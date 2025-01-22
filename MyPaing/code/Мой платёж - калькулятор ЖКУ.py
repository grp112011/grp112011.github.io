#The last version
import tkinter
from tkinter import scrolledtext
from tkinter import ttk
import datetime
import os
import requests
from functools import partial
infosp = ['Мой платёж - калькулятор ЖКУ', '1.0', '13.12.24', ]

fonts = None
fontl = None
pokchet = None
winkv = None
En = None
En1 = None
En2 = None
En3 = None
nokon = None
vkvk = None
tarele, tarcwe, tarhwe, targae = None, None, None, None
tarw = None
arw = None
setw = None
infow = None
fontw = None
fonts = None
colorw = None
colorsp = ['Светло-голубой', 'Салатовый', 'Бирюзовый', 'Голубой', 'Серый']
colorsl = {'Светло-голубой': 'azure2', 'Салатовый': 'darkolivegreen1', 'Бирюзовый': 'cyan', 'Голубой': 'lightblue', 'Серый': 'lightgrey'}
colorc = None
are = None
ars = None
lmde = None
IT = None
lmdw = None
lmdl = None
sendb = None

def validate(new_value):
    return new_value == '' or new_value.isdigit()

def validated(text, val):
    return (val == '' or val.isdigit() or val == '.' or text == '') and text.count('.') <= 2

def validate1(text, val):
    return (val == '' or val.isdigit() or val == '.' or text == '') and text.count('.') <= 1

def check_message(user):
    sp = {}
    for i in requests.get(f'https://api.telegram.org/bot*************************************/getUpdates?offset=0').json()['result']:
        sp[i['message']['from']['username']] = i['message']['chat']['id']
    for u, i in sp.items():
        if u == user:
            return str(i)
            break
    return False

a = open('font.txt', 'r')
fnt = a.read()
a.close()

a = open('colour.txt', 'r')
colr = a.read()
a.close()

a = open('тариф.txt', 'r')
tarif = a.read().split('\n')
a.close()
spsps = []

wind = tkinter.Tk()
wind.configure(bg=colr)

wind.title('Мой платёж - калькулятор ЖКУ')
wind.geometry('400x400')
wind.iconbitmap(default="поксчт.ico")

vc1 = (wind.register(validate1), '%P', '%S')
vcd = (wind.register(validated), '%P', '%S')

n = 0
vkvk = 0

kvb = tkinter.Button(wind, text='Выбор квартиры', pady=10, padx=10, font=fnt, fg='black')
kvb.pack()
kvb.place(relwidth=0.5, relx=0.0, relheight=0.10)

btn2 = tkinter.Button(wind, text='Ввод', font=fnt, fg='black', pady=10, padx=10)
btn2.pack()
btn2.place(relwidth=0.5, relx=0.5, relheight=0.10)

datal = tkinter.Label(wind, text='Дата', font=fnt, fg='black', bg=colr)
datal.pack()
datal.place(relwidth=1, rely=0.11)

datae = tkinter.Entry(wind, width=25, validate='key', validatecommand=vcd)
datae.pack()
datae.place(relwidth=1, relheight=0.065, rely=0.18)

lgv = tkinter.Label(wind, text='Холодная вода', font=fnt, fg='black', bg=colr)
lgv.pack()
lgv.place(relwidth=1.0, rely=0.26)
enthol = tkinter.Entry(wind, width=50, validate='key', validatecommand=vc1)
enthol.pack()
enthol.place(relwidth=1.0, rely=0.34, relheight=0.065)


lgv1 = tkinter.Label(wind, text='Горячая вода', font=fnt, fg='black', bg=colr)
lgv1.pack()
lgv1.place(relwidth=1.0, rely=0.42)
enthot = tkinter.Entry(wind, width=50, validate='key', validatecommand=vc1)
enthot.pack()
enthot.place(relwidth=1.0, rely=0.49, relheight=0.065)


lgv2 = tkinter.Label(wind, text='Электричество', font=fnt, fg='black', bg=colr)
lgv2.pack()
lgv2.place(relwidth=1.0, rely=0.57)
entel = tkinter.Entry(wind, width=50, validate='key', validatecommand=vc1)
entel.pack()
entel.place(relwidth=1.0, rely=0.64, relheight=0.065)

lgv3 = tkinter.Label(wind, text='Газ', font=fnt, fg='black', bg=colr)
lgv3.pack()
lgv3.place(relwidth=1.0, rely=0.71)
entga = tkinter.Entry(wind, width=50, validate='key', validatecommand=vc1)
entga.pack()
entga.place(relwidth=1.0, rely=0.78, relheight=0.065)

tarb = tkinter.Button(wind, text='Изменить тариф', font=fnt, fg='black')
tarb.pack()
tarb.place(relwidth=0.53, rely=0.85, relx=0.0, relheight=0.15)

arb = tkinter.Button(wind, text='Архив', font=fnt, fg='black', pady=10, padx=10)
arb.pack()
arb.place(relwidth=0.15, relx=0.7, rely=0.85, relheight=0.15)

ourb1 = tkinter.PhotoImage(file='Мусор.png')
ourb1 = ourb1.subsample(19, 19)

deb = tkinter.Button(wind, image=ourb1)
deb.pack()
deb.place(relwidth=0.17, relx=0.53, rely=0.85, relheight=0.15)

ourb = tkinter.PhotoImage(file='Безымянный-3333.png')
ourb = ourb.subsample(37,37)

setb = tkinter.Button(wind, image=ourb)
setb.pack()
setb.place(rely=0.85, relx=0.85, relwidth=0.15, relheight=0.15)
spskv = []

def winddel(event):
    global datae, enthot, enthol, entel, entga
    datae.delete(0, 'end')
    enthot.delete(0, 'end')
    enthol.delete(0, 'end')
    entel.delete(0, 'end')
    entga.delete(0, 'end')

def winkvd():
    global winkv
    winkv.destroy()
    winkv = None

def nokond():
    global nokon
    nokon.destroy()
    nokon = None

def tarwd():
    global tarw
    tarw.destroy()
    tarw = None

def setwd():
    global setw
    setw.destroy()
    setw = None

def infowd():
    global infow
    infow.destroy()
    infow = None

def arwd():
    global arw
    arw.destroy()
    arw = None

def fontwd():
    global fontw
    fontw.destroy()
    fontw = None

def colorwd():
    global colorw
    colorw.destroy()
    colorw = None



def kv(event):
    global n
    global spskv
    global winkv
    global spsps
    global vkvk
    global fnt, colr
    if winkv == None:
        winkv = tkinter.Tk()
        winkv.configure(bg=colr)
        winkv.resizable(False, False)
        winkv.title('Адрес и номер квартиры')
        winkv.iconbitmap(default="поксчт.ico")
        winkv.protocol('WM_DELETE_WINDOW', winkvd)
        kv_list = []
        
        vrsp = open('квартиры.txt', 'r').read().split('\n')

        if vrsp != ['']:
        
            for x in vrsp:
                kv_list.append(tkinter.Button(winkv, text=str(x), width=40, pady=10, padx=10, font=fnt, fg='black', command=partial(butt, x)))
                kv_list[-1].pack()

        dob = tkinter.Button(winkv, text='+ Добавить квартиру', width=40, pady=10, padx=10, font=fnt, fg='black')
        dob.pack()
        delde = tkinter.Button(winkv, text='- Удалить квартиру', width=40, pady=10, padx=10, font=fnt, fg='black')
        delde.pack()
        dob.bind('<ButtonRelease-1>', dobkv)
        delde.bind('<ButtonRelease-1>', delkv)

def delkv(event):
    global En
    global nokon
    global fnt, colr
    if nokon == None:
        nokon = tkinter.Tk()
        nokon.configure(bg=colr)
        nokon.resizable(False, False)
        nokon.title('Мой платёж - калькулятор ЖКУ')
        nokon.iconbitmap(default="поксчт.ico")
        nokon.protocol('WM_DELETE_WINDOW', nokond)
        vc = (nokon.register(validate), '%P')
        
        Ls = tkinter.Label(nokon, text='Введите номер квартиры', font=fnt, fg='black', bg=colr)
        Ls.pack()
        En = tkinter.Entry(nokon, width=25, validate='key', validatecommand=vc)
        En.focus()
        En.pack(padx=10, pady=10)

        btnEnter = tkinter.Button(nokon, text='Ввод', width=25, font=fnt, fg='black')
        btnEnter.pack(pady=10)
        btnEnter.bind('<ButtonRelease-1>', b)
        nokon.bind('<Return>', b)

def b(event):
    global En, nokon, winkv
    
    nad = open('квартиры.txt', 'r')
    d = nad.read().split('\n')
    ddd = En.get()
    if ddd in d:
        d.remove(ddd)
        os.remove(ddd + '.txt')
    nokon.destroy()
    nokon = None
    nad.close()
    nad = open('квартиры.txt', 'w')
    x = nad.write('\n'.join(d))
    nad.close()
    winkv.destroy()
    winkv = None


def dobkv(event):
    global En
    global nokon
    global fnt, colr
    if nokon == None:
        nokon = tkinter.Tk()
        nokon.configure(bg=colr)
        nokon.resizable(False, False)
        nokon.protocol('WM_DELETE_WINDOW', nokond)
        nokon.title('Мой платёж - калькулятор ЖКУ')
        nokon.iconbitmap(default="поксчт.ico")
        
        vc = (nokon.register(validate), '%P')
        
        Ls = tkinter.Label(nokon, text='Введите номер квартиры', font=fnt, fg='black', bg=colr)
        Ls.pack()
        En = tkinter.Entry(nokon, width=25, validate='key', validatecommand=vc)
        En.pack(padx=10, pady=10)
        En.focus()

        btnEnter = tkinter.Button(nokon, text='Ввод', width=25, font=fnt, fg='black')
        btnEnter.pack(pady=10)
        btnEnter.bind('<ButtonRelease-1>', a)
        nokon.bind('<Return>', a)
    

    
def a(event):
    global En
    global En1
    global En2, En3
    global nokon, winkv, vkvk
    global fnt, colr
    nad = open('квартиры.txt', 'r')
    d = (nad.read()).split()
    vkvk = En.get()
    a = open(vkvk + '.txt', 'w')
    a.close()
    d.append(vkvk)
    nokon.destroy()
    nokon = tkinter.Tk()
    nokon.configure(bg=colr)
    nokon.resizable(False, False)
    nokon.title('Мой платёж - калькулятор ЖКУ')
    nokon.iconbitmap(default="поксчт.ico")
    nokon.protocol('WM_DELETE_WINDOW', nokond)
    vc1 = (nokon.register(validate1), '%P', '%S')
    
    Ls = tkinter.Label(nokon, text='Введите показания счётчиков холодной воды', font=fnt, fg='black', bg=colr)
    Ls.pack()
    En = tkinter.Entry(nokon, width=25, validate='key', validatecommand=vc1)
    En.pack(padx=10, pady=10)
    En.focus()
    
    Ls1 = tkinter.Label(nokon, text='Введите показания счётчиков горячей  воды', font=fnt, fg='black', bg=colr)
    Ls1.pack()
    En1 = tkinter.Entry(nokon, width=25, validate='key', validatecommand=vc1)
    En1.pack(padx=10, pady=10)
    
    Ls2 = tkinter.Label(nokon, text='Введите показания счётчиков электричества', font=fnt, fg='black', bg=colr)
    Ls2.pack()
    En2 = tkinter.Entry(nokon, width=25, validate='key', validatecommand=vc1)
    En2.pack(padx=10, pady=10)

    Ls3 = tkinter.Label(nokon, text='Введите показания счётчиков газа', font=fnt, fg='black', bg=colr)
    Ls3.pack()
    En3 = tkinter.Entry(nokon, width=25, validate='key', validatecommand=vc1)
    En3.pack(padx=10, pady=10)

    btnEnter = tkinter.Button(nokon, text='Ввод', width=25, font=fnt, fg='black')
    btnEnter.pack(pady=10)
    btnEnter.bind('<ButtonRelease-1>', xy)
    nokon.bind('<Return>', xy)
    
    nad.close()
    nad = open('квартиры.txt', 'w')
    x = nad.write('\n'.join(d))
    nad.close()
    winkv.destroy()
    winkv = None


def xy(event):
    global vkvk
    global spsps, nokon
    spsps.append(En.get())
    spsps.append(En1.get())
    spsps.append(En2.get())
    spsps.append(En3.get())
    a = open(vkvk + '.txt', 'w')
    a.write('\n'.join(spsps))
    a.close()
    nokon.destroy()
    nokon = None

def instr(event):
    global lmde
    t = tkinter.Tk()
    t.iconbitmap(default="поксчт.ico")
    t.title('Мой платёж - калькулятор ЖКУ')
    tl = tkinter.Label(t, text='1. Наберите в поисковике пользователей в телеграмме @ZHKUbot и откройте чат с ботом\n2. Нажмите на кнопку "Старт" или наберите команду /start\n3. Повторите попытку отпраки подсчёта', font=fnt, fg='black', bg=colr)
    tl.pack()

def sendf(user, txt):
    global colr, fnt, lmdw, lmdl, sendb
    if lmdl == None:
        lmdl = tkinter.Label(lmdw, text='Пожалуйста, подождите...', font=fnt, bg=colr)
        lmdl.pack()
    a = open('names.txt' ,'r')
    spn = a.read().split()
    a.close()

    if user in spn:
        lmdl.configure(text='Успешно')
        requests.get(f"https://api.telegram.org/bot***************************************/sendMessage?chat_id={spn[spn.index(user) + 1]}&text={txt}")
    
    elif check_message(user) != False:
        a = open('names.txt', 'a')
        a.write(user + ' ' + check_message(user) + '\n')
        requests.get(f"https://api.telegram.org/bot***************************************/sendMessage?chat_id={check_message(user)}&text={txt}").json()
        lmdl.configure(text='Успешно')
        
    else:
        lmdl.configure(text='Имя пользователя не найдено')
        if sendb == None:
            sendb = tkinter.Button(lmdw, text='Инструкция по настройке бота', font=fnt, fg='black')
            sendb.pack()
            sendb.bind('<ButtonRelease-1>', instr)


def usertg(event):
    global lmde, IT
    if lmde.get()[0] == '@':
        user = lmde.get()[1:]
    else:
        user = lmde.get()
    sendf(user, IT)
        

def lmd(event):
    global fnt, colr, lmde, lmdw
    lmdw = tkinter.Tk()
    lmdw.configure(bg=colr)
    lmdw.resizable(False, False)
    lmdw.iconbitmap(default="поксчт.ico")
    lmdw.title('Мой платёж - калькулятор ЖКУ')
    
    lmdl = tkinter.Label(lmdw, text='Введите имя погльзователя в ТГ:', font=fnt, fg='black', bg=colr)
    lmdl.pack()
    lmde = tkinter.Entry(lmdw, width=50)
    lmde.pack(pady=10)
    lmdb = tkinter.Button(lmdw, text='Отправить', width=50, font=fnt, fg='black')
    lmdb.pack()
    lmdb.bind('<ButtonRelease-1>', usertg)
    lmdw.bind('<Return>', usertg)
    

def cwater(event):
    global vkvk
    global entel
    global enthol
    global enthot, entga
    global datae, IT
    global fnt, colr
    s1 = enthol.get()
    s2 = enthot.get()
    s3 = entel.get()
    s4 = entga.get()

    ar = open('архив.txt', 'a')

    try:
    
        b = open(str(vkvk) + '.txt', 'r')
        sct_old = b.read().split('\n')
        b.close()
        
        sct_new = []
        sct_new.append(s1)
        sct_new.append(s2)
        sct_new.append(s3)
        sct_new.append(s4)
        
        razn = []
        razn.append((float(sct_new[0]) - float(sct_old[0])) * float(tarif[0]))
        razn.append((float(sct_new[1]) - float(sct_old[1])) * float(tarif[1]))
        razn.append((float(sct_new[2]) - float(sct_old[2])) * float(tarif[2]))
        razn.append((float(sct_new[3]) - float(sct_old[3])) * float(tarif[3]))
        cw = 'Холодная вода' + ': (' + str(sct_new[0]) + ' - ' + str(sct_old[0]) + ') *  ' + str(tarif[0]) + ' = ' + str(int(round(int(razn[0]))))  + '₽'
        hw = 'Горячая вода' + ': (' + str(sct_new[1]) + ' - ' + str(sct_old[1]) + ') * ' + str(tarif[1]) + ' = ' + str(int(round(int(razn[1])))) + '₽'
        en = 'Электричество' + ': (' + str(sct_new[2]) + ' - ' + str(sct_old[2]) + ') * ' + str(tarif[2]) + ' = ' + str(int(round(int(razn[2])))) + '₽'
        ga = 'Газ' + ': (' + str(sct_new[3]) + ' - ' + str(sct_old[3]) + ') * ' + str(tarif[3]) + ' = ' + str(int(round(int(razn[3])))) + '₽'
        M = razn[0] + razn[1] + razn[2] + razn[3]
        Mt = 'Итого:' + ' ' + str(M) + '₽'
        IT = '\n' + cw + '\n\n' + hw + '\n\n' + en + '\n\n' + ga + '\n\n' + 'Итого: ' + str(razn[0] + razn[2] + razn[1] + razn[3]) + '\n'
        witu = tkinter.Tk()
        witu.configure(bg=colr)
        witu.title('Расчёт')
        witu.geometry('450x320')
        witu.resizable(False, False)
        witu.iconbitmap(default="поксчт.ico")
        
        Lab = tkinter.Label(witu, text=IT, font=fnt, fg='black', bg=colr)
        Lab.pack(pady=10)
        Lab.place(rely=0.0, relheight=0.9, relwidth=1.0)

        witb = tkinter.Button(witu, text='Отправить', font=fnt, fg='black')
        witb.pack()
        witb.place(relheight=0.2, relwidth=1, rely=0.8)
        witb.bind('<ButtonRelease-1>', lmd)
        
        b = open(str(vkvk) + '.txt', 'w')
        b.write(sct_new[0] + '\n' + sct_new[1] + '\n' + sct_new[2] + '\n' + sct_new[3])
        b.close()
        if datae.get() == '':
            datavar = str(datetime.date.today())
        else:
            datavar = datae.get()
        ar.write('Квартира: ' + vkvk + '\n' + 'Дата: ' + datavar + ':\n' + 'Холодная вода: ' + sct_new[0] + '\nГорячая вода: ' + sct_new[1] + '\nЭлектричество: ' + sct_new[2] + '\nГаз: ' + sct_new[3])
        ar.close()
    except:
        pass


def butt(button_press):
    global vkvk, winkv
    vkvk = button_press
    winkv.destroy()
    winkv = None


def tarf(event):
    global tarif, tarele, tarcwe, tarhwe, tarw, targae
    global fnt, colr
    if tarw == None:
        tarw = tkinter.Tk()
        tarw.title('Изменить тариф')
        tarw.configure(bg=colr)
        tarw.resizable(False, False)
        tarw.iconbitmap(default="поксчт.ico")
        
        tarw.protocol('WM_DELETE_WINDOW', tarwd)
        vc1 = (tarw.register(validate1), '%P', '%S')
        
        tarcwl = tkinter.Label(tarw, text='Введите тариф холодной воды:', font=fnt, fg='black', bg=colr)
        tarcwl.pack()
        tarcwe = tkinter.Entry(tarw, validate='key', validatecommand=vc1)
        tarcwe.pack()
        tarcwe.focus()
    
        tarhwl = tkinter.Label(tarw, text='Введите тариф горячей воды:', font=fnt, fg='black', bg=colr)
        tarhwl.pack()
        tarhwe = tkinter.Entry(tarw, validate='key', validatecommand=vc1)
        tarhwe.pack()
        
        tarell = tkinter.Label(tarw, text='Введите тариф электричества:', font=fnt, fg='black', bg=colr)
        tarell.pack()
        tarele = tkinter.Entry(tarw, validate='key', validatecommand=vc1)
        tarele.pack()

        targal = tkinter.Label(tarw, text='Введите тариф газа:', font=fnt, fg='black', bg=colr)
        targal.pack()
        targae = tkinter.Entry(tarw, validate='key', validatecommand=vc1)
        targae.pack()

        trwb = tkinter.Button(tarw, text='Ввод', font=fnt, fg='black')
        trwb.pack()
        trwb.bind('<ButtonRelease-1>', tc)
        tarw.bind('<Return>', tc)
    
def tc(event):
    global tarele, tarcwe, tarhwe, sasa, tarif, targae
    ntc = tarcwe.get()
    nth = tarhwe.get()
    nte = tarele.get()
    ntg = targae.get()
    vrtar = open('тариф.txt', 'w')
    vrtar.write(ntc + '\n' + nth + '\n' + nte + '\n' + ntg)
    vrtar.close()
    sasa = open('тариф.txt', 'r')
    tarif = sasa.read().split('\n')
    sasa.close()
    tarwd()

def infof(event):
    global infow, fnt, colr, infosp
    if infow == None:
        infow = tkinter.Tk()
        infow.title('Информация')
        infow.configure(bg=colr)
        infow.geometry('450x150')
        infow.resizable(False, False)
        infow.iconbitmap(default="поксчт.ico")
        
        infow.protocol('WM_DELETE_WINDOW', infowd)
        infol = tkinter.Label(infow, text='Название: ' + infosp[0] + '\nВерсия: ' + infosp[1] + '\nВыпущенно: ' + infosp[2] + '\nРазработчик: Грачев Роман', font=fnt, fg='black', width=50, bg=colr, justify='left')
        infol.pack()
        infol.place(relwidth=1.0, relheight=1.0)


def delar(event):
    a = open('архив.txt', 'w')
    a.write('')
    a.close()
    global arw
    arw.destroy()
    arw = None

def searchar(event):
    global ars, are
    a = open('архив.txt', 'r')
    sp = a.read().split('\n')
    a.close()
    se = are.get()
    ind = []
    for i, e in enumerate(sp):
        if se in e:
            ind.append(i)
    sps = []
    for i in ind:
        sps.append(sp[i])
        if i + 1 < len(sp):
            sps.append(sp[i + 1])
        if i + 2 < len(sp):
            sps.append(sp[i + 2])
        if i + 3 < len(sp):
            sps.append(sp[i + 3])
        if i + 4 < len(sp):
            sps.append(sp[i + 4])
    for i in sps:
        for x in range(sps.count(i) - 1):
            sps.remove(i)
    ars.delete(1.0, 'end')
    ars.insert('insert', '\n'.join(sps))




        
def arf(event):
    global arw, fnt, colr, are, ars
    if arw == None:
        x = open('архив.txt', 'r')
        arw = tkinter.Tk()
        arw.title('Архив')
        arw.geometry('500x500')
        arw.configure(bg=colr)
        arw.iconbitmap(default="поксчт.ico")
        
        ars = tkinter.scrolledtext.ScrolledText(arw, font=fnt)
        ars.pack()
        ars.place(relwidth=1, relheight=0.86, rely=0, relx=0)
        rd = x.read()
        if rd != '':
            ars.insert('insert', rd)
        else:
            ars.insert('insert', 'Архив пуст...')
        x.close()
        arw.protocol('WM_DELETE_WINDOW', arwd)
        arw.bind('<Return>', searchar)
        delarb = tkinter.Button(arw, text='Отчистить архив', font=fnt, fg='black')
        delarb.pack()
        delarb.place(relwidth=1, relheight=0.14, rely=0.86, relx=0)
        delarb.bind('<ButtonRelease-1>', delar)
        

def fontsbf(event):
    global fnt
    global fonts
    global fontw, setw
    fnt = 'Arial ' + str(fonts.get())
    a = open('font.txt', 'w')
    a.write(fnt)
    a.close()
    fontw.destroy()
    fontw = None
    datal.configure(font=fnt)
    lgv.configure(font=fnt)
    lgv1.configure(font=fnt)
    lgv2.configure(font=fnt)
    lgv3.configure(font=fnt)
    kvb.configure(font=fnt)
    btn2.configure(font=fnt)
    tarb.configure(font=fnt)
    arb.configure(font=fnt)
    setw.destroy()
    setw = None


def fontch(event):
    global fonts, fontl
    f = 'Arial ' + str(fonts.get())
    fontl.configure(font=f)


def fontf(event):
    global fnt, corl
    global fontw
    global fonts, fontl
    if fontw == None:
        fontw = tkinter.Tk()
        fontw.resizable(False, False)
        fontw.title('Размер шрифта')
        fontw.configure(bg=colr)
        fontw.iconbitmap(default="поксчт.ico")
        fontw.protocol('WM_DELETE_WINDOW', fontwd)
        fonts = tkinter.Scale(fontw, orient='horizontal', from_=10, to=16, command=fontch)
        fonts.pack()
        fonts.place(relwidth=1.0)

        fontl = tkinter.Label(fontw, text='Аа Бб Вв', font=fnt)
        fontl.pack()
        fontl.place(relwidth=1.0, relheight=0.6, rely=0.2)
        
        fontsb = tkinter.Button(fontw, text='Ввод', font=fnt, fg='black')
        fontsb.pack()
        fontsb.place(relwidth=1.0, relheight=0.2, rely=0.8)
        fontsb.bind('<ButtonRelease-1>', fontsbf)
        fontw.bind('<Return>', fontsbf)

def setcolor1(event):
    global colr, colorsl, winkv, wind
    colr = 'azure2'
    a = open('colour.txt', 'w')
    a.write(colr)
    a.close()
    wind.configure(bg=colr)
    datal.configure(bg=colr)
    lgv.configure(bg=colr)
    lgv1.configure(bg=colr)
    lgv2.configure(bg=colr)
    lgv3.configure(bg=colr)
    colorwd()
    setwd()

def setcolor2(event):
    global colr, colorsl, winkv, wind
    colr = 'darkolivegreen1'
    a = open('colour.txt', 'w')
    a.write(colr)
    a.close()
    wind.configure(bg=colr)
    datal.configure(bg=colr)
    lgv.configure(bg=colr)
    lgv1.configure(bg=colr)
    lgv2.configure(bg=colr)
    lgv3.configure(bg=colr)
    colorwd()
    setwd()

def setcolor3(event):
    global colr, colorsl, winkv, wind
    colr = 'cyan'
    a = open('colour.txt', 'w')
    a.write(colr)
    a.close()
    wind.configure(bg=colr)
    datal.configure(bg=colr)
    lgv.configure(bg=colr)
    lgv1.configure(bg=colr)
    lgv2.configure(bg=colr)
    lgv3.configure(bg=colr)
    colorwd()
    setwd()

def setcolor4(event):
    global colr, colorsl, winkv, wind
    colr = 'lightblue'
    a = open('colour.txt', 'w')
    a.write(colr)
    a.close()
    wind.configure(bg=colr)
    datal.configure(bg=colr)
    lgv.configure(bg=colr)
    lgv1.configure(bg=colr)
    lgv2.configure(bg=colr)
    lgv3.configure(bg=colr)
    colorwd()
    setwd()

def setcolor5(event):
    global colr, colorsl, winkv, wind
    colr = 'lightgrey'
    a = open('colour.txt', 'w')
    a.write(colr)
    a.close()
    wind.configure(bg=colr)
    datal.configure(bg=colr)
    lgv.configure(bg=colr)
    lgv1.configure(bg=colr)
    lgv2.configure(bg=colr)
    lgv3.configure(bg=colr)
    colorwd()
    setwd()

def colorf(event):
    global colr, colorw, fnt, colorsp, colorc
    if colorw == None:
        colorw = tkinter.Tk()
        colorw.protocol('WM_DELETE_WINDOW', colorwd)
        colorw.title('Цвет')
        colorw.resizable(False, False)
        colorw.configure(bg = colr)
        colorw.iconbitmap(default="поксчт.ico")
        
        colorb1 = tkinter.Button(colorw, text='Светло-голубой', font=fnt, bg='azure2', width=50)
        colorb1.pack()
        colorb1.bind('<ButtonRelease-1>', setcolor1)
        
        colorb2 = tkinter.Button(colorw, text='Салатовый', font=fnt, bg='darkolivegreen1', width=50)
        colorb2.pack()
        colorb2.bind('<ButtonRelease-1>', setcolor2)
        
        colorb3 = tkinter.Button(colorw, text='Бирюзовый', font=fnt, bg='cyan', width=50)
        colorb3.pack()
        colorb3.bind('<ButtonRelease-1>', setcolor3)
        
        colorb4 = tkinter.Button(colorw, text='Голубой', font=fnt, bg='lightblue', width=50)
        colorb4.pack()
        colorb4.bind('<ButtonRelease-1>', setcolor4)
        
        colorb5 = tkinter.Button(colorw, text='Серый', font=fnt, bg='lightgrey', width=50)
        colorb5.pack()
        colorb5.bind('<ButtonRelease-1>', setcolor5)
        

def setf(event):
    global setw, fnt, colr
    if setw == None:
        setw = tkinter.Tk()
        setw.title('Настройки')
        setw.configure(bg=colr)
        setw.resizable(False, False)
        setw.protocol('WM_DELETE_WINDOW', setwd)
        setw.iconbitmap(default="поксчт.ico")
    
        info = tkinter.Button(setw, text='Информация', font=fnt, fg='black', width=50)
        info.pack(pady=10)
        info.bind('<ButtonRelease-1>', infof)

        fontb = tkinter.Button(setw, text='Размер шрифта', font=fnt, fg='black', width=50)
        fontb.pack()
        fontb.bind('<ButtonRelease-1>', fontf)

        colorb = tkinter.Button(setw, text='Цвет фона', font=fnt, fg='black', width=50)
        colorb.pack(pady=10)
        colorb.bind('<ButtonRelease-1>', colorf)
    
        

tarb.bind('<ButtonRelease-1>', tarf)
btn2.bind('<ButtonRelease-1>', cwater)
kvb.bind('<ButtonRelease-1>', kv)
setb.bind('<ButtonRelease-1>', setf)
arb.bind('<ButtonRelease-1>', arf)

wind.bind('<Return>', cwater)
wind.bind('<Return>', cwater)
deb.bind('<ButtonRelease-1>', winddel)

tkinter.mainloop()




