from tkinter import *
from time import *

## 전역 변수 선언 부분 ##
fnameList = ["panda (1).png", "panda (2).png", "panda (3).png", "panda (4).png", "panda (5).png",
             "panda (6).png", "panda (7).png", "panda (8).png", "panda (9).png"]
PhotoList = [None] * 9
num = 0

## 함수 선언 부분 ##
def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    photo = PhotoImage(file="./jpg/" + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo


def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    photo = PhotoImage(file="./jpg/" + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo

## 메인 코드 부분 ##
window = Tk()
window.geometry("500x300")
window.title("판~다")

btnPrev = Button(window, text="<< 이전", command=clickPrev)
btnNext = Button(window, text="다음 >>", command=clickNext)

photo = PhotoImage(file="./jpg/" + fnameList[0])
pLabel = Label(window, image=photo)

btnPrev.place(x=250, y=10)
btnNext.place(x=300, y=10)
pLabel.place(x=15, y=50)

window.mainloop()