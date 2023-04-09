from tkinter import *
from tkinter.filedialog import *

## 함수 선언 부분 ##
def file_open():
    filename = askopenfilename(parent = window, filetypes = (("PNG 파일", "*.png"), ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo

def exit():
    window.quit()
    window.destroy()


## 메인 코드 부분 ##
window = Tk()
window.geometry("400x400")

window.title("이미지 뷰어")

photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand = 1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
filemenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = filemenu)
filemenu.add_command(label = "파일 열기", command = file_open)
filemenu.add_separator()
filemenu.add_command(label = "프로그램 종료", command = exit)

window.mainloop()