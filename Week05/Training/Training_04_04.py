from enum import Enum
from Training_04-03 import FixedQueue

Menu = Enum('Menu', ['Enqueue', 'Dequeue', 'Peek', 'Clear', 'Find', 'Count', 'Dump', 'Exit'])


def selectMenu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]

    while True:
        print(*s, sep='  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)


queue = FixedQueue(64)

while True:
    menu = selectMenu()

    if menu == Menu.Enqueue:
        value = int(input('큐에 집어넣을 데이터를 입력하세요 : '))
        queue.enqueue(value)

    elif menu == Menu.Dequeue:
        value = queue.dequeue()
        print('큐에 꺼낸 데이터는 {}입니다'.format(value))

    elif menu == Menu.Peek:
        value = queue.peek()
        print('큐에 가장 앞 데이터는 {}입니다'.format(value))

    elif menu == Menu.Clear:
        queue.clear()
        print('큐를 비웠습니다')

    elif menu == Menu.Find:
        value = int(input('큐에서 찾을 데이터를 입력하세요 : '))
        result = queue.find(value)

        if result == -1:
            print('큐에 찾는 데이터가 없습니다')
        else:
            print('큐에 찾는 데이터는 {}번 인덱스에 있습니다'.format(result))

    elif menu == Menu.Count:
        value = int(input('큐에서 개수를 셀 데이터를 입력하세요 : '))
        result = queue.count(value)

        if result == 0:
            print('큐에 {}은 없습니다'.format(value))
        else:
            print('큐에 있는 {}은 {}개입니다'.format(value, result))

    elif menu == Menu.Dump:
        print('큐에 있는 모든 데이터를 출력합니다')
        queue.dump()

    elif menu == Menu.Exit:
        break