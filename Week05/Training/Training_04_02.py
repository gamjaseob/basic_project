from enum import Enum
from Training_04_01 import FixedStack

Menu = Enum('Menu', ['Push', 'Pop', 'Peek', 'Clear', 'Find', 'Count', 'Dump', 'Exit'])

def selectMenu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]

    while True:
        print(*s, sep='  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)


stack = FixedStack(64)

while True:
    menu = selectMenu()
    if menu == Menu.Push:
        value = int(input('스택에 집어넣을 데이터를 입력하세요 : '))
        stack.push(value)

    elif menu == Menu.Pop:
        value = stack.pop()
        print('스택에 꺼낸 데이터는 {}입니다'.format(value))

    elif menu == Menu.Peek:
        value = stack.peek()
        print('스택에 가장 위 데이터는 {}입니다'.format(value))

    elif menu == Menu.Clear:
        stack.clear()
        print('스택을 비웠습니다')

    elif menu == Menu.Find:
        value = int(input('스택에 찾을 데이터를 입력하세요 : '))
        result = stack.find(value)

        if result == -1:
            print('스택에 찾는 데이터가 없습니다')
        else:
            print('스택에 찾는 데이터는 {}번 인덱스에 있습니다'.format(result))

    elif menu == Menu.Count:
        value = int(input('스택에 개수를 셀 데이터를 입력하세요 : '))
        result = stack.count(value)

        if result == 0:
            print('스택에 {}은 없습니다'.format(value))
        else:
            print('스택에 있는 {}은 {}개입니다'.format(value, result))

    elif menu == Menu.Dump:
        print('스택에 있는 모든 데이터를 출력합니다')
        stack.dump()

    elif menu == Menu.Exit:
        break

    else:
        print('잘못된 입력입니다')