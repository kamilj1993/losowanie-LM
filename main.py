import openpyxl
import random


plik = 'Teams.xlsx'
book = openpyxl.load_workbook(plik)
sheet = book.active

GRUPY = [[],[],[],[],[],[],[],[]]


def losuj():
    wyn_los = []
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    for i in range(0,8):
        nr = random.choice(a)
        wyn_los.append(nr)
        a.remove(nr)
    return wyn_los


def los_kosz1():
    a = [1,2,3,4,5,6,7,8]
    for i in range(0,8):
        nr = random.choice(a)
        GRUPY[i].append((sheet[f'A{nr}'].value,sheet[f'B{nr}'].value))
        a.remove(nr)


def los_kosz2():
    wyniki = losuj()
    prawid_los = True
    for i in range(0, 8):
        if str(sheet[f'B{10 + (wyniki[i])}'].value) == str(GRUPY[i][0][1]):
            prawid_los = False
            break
        else:
            pass
    if prawid_los == True:
        for i in range(0,8):
            GRUPY[i].append((sheet[f'A{10 + (wyniki[i])}'].value, sheet[f'B{10 + (wyniki[i])}'].value))
    else:
        los_kosz2()


def los_kosz3():
    wyniki = losuj()
    prawid_los = True
    for i in range(0, 8):
        if str(sheet[f'B{20 + (wyniki[i])}'].value) == str(GRUPY[i][0][1]) or str(sheet[f'B{20 + (wyniki[i])}'].value) == str(GRUPY[i][1][1]):
            prawid_los = False
            break
        else:
            pass
    if prawid_los == True:
        for i in range(0,8):
            GRUPY[i].append((sheet[f'A{20 + (wyniki[i])}'].value, sheet[f'B{20 + (wyniki[i])}'].value))
    else:
        los_kosz3()


def los_kosz4():
    wyniki = losuj()
    prawid_los = True
    for i in range(0, 8):
        if str(sheet[f'B{30 + (wyniki[i])}'].value) == str(GRUPY[i][0][1]) or str(sheet[f'B{30 + (wyniki[i])}'].value) == str(GRUPY[i][1][1]) or str(sheet[f'B{30 + (wyniki[i])}'].value) == str(GRUPY[i][2][1]):
            prawid_los = False
            break
        else:
            pass
    if prawid_los == True:
        for i in range(0, 8):
            GRUPY[i].append((sheet[f'A{30 + (wyniki[i])}'].value, sheet[f'B{30 + (wyniki[i])}'].value))
    else:
        los_kosz4()


los_kosz1()
los_kosz2()
los_kosz3()
los_kosz4()

for i in range(0,8):
    print(f'\nGrupa {chr(65+i)}:\n{GRUPY[i][0][0]} ({GRUPY[i][0][1]})\n{GRUPY[i][1][0]} ({GRUPY[i][1][1]})\n{GRUPY[i][2][0]} ({GRUPY[i][2][1]})\n{GRUPY[i][3][0]} ({GRUPY[i][3][1]})')