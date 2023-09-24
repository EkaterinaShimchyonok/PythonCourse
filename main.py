import random
import pandas as pd


def task_menu():
    print("1 задание")
    print("2 задание")
    print("3 задание")
    print("4 задание")
    print("5 задание")
    print("6 задание")
    print("7 закончить работу")
    ch = input("Сделайте выбор: ")
    return ch


def task1():
    print("-" * 100)
    print("Вывести все делители числа")
    print("-" * 100)

    num = int(input("Введите целое число: "))
    divisors = {1, num}
    for i in range(2, abs(num)):
        if num % i == 0:
            divisors.add(i)
    if num < 0:
        divisors = divisors.union({-div for div in divisors})
    print("Делители числа: ", divisors)


def task2():
    print("-" * 100)
    print("Подсчитать количество слов в строке и вывести самое длинное слово")
    print("-" * 100)

    my_str = input("Введите строку: ")
    words = my_str.split(sep=" ")
    max_word = ""
    for word in words:
        if len(word) > len(max_word):
            max_word = word
    print("Количество слов в строке: ", len(words))
    print("Самое длинное слово: " + max_word)


def task3():
    print("-" * 100)
    print("Создать из указанных чисел список (длиной не меньше 2), состоящий из сумм соседних чисел")
    print("-" * 100)

    num_list = []
    n = int(input("Введите количество чисел не меньше 2: "))
    if n >= 2:
        for i in range(n):
            number = int(input("Введите целое число: "))
            num_list.append(2 * number)
        print("Полученный список: ", num_list)
    else:
        task3()


def task4():
    print("-" * 100)
    print("Отсортировать словарь по ключу в порядке возрастания и убывания. Вывести на экран элемент с максимальным "
          "значением.")
    print("-" * 100)

    i_list = []
    for i in range(10):
        i_list.append(random.randint(1, 100))

    cubes = {i: i ** 3 for i in i_list}
    print("Не отсортирован", cubes)
    print("Отсортирован в порядке возрастания", dict(sorted(cubes.items())))
    print("Отсортирован в порядке убывания", (dict(sorted(cubes.items(), reverse=True))))
    max_el = {k: v for k, v in cubes.items() if v == max(cubes.values())}
    print("Максимальное значение в словаре", max_el)


goods = {"Даниш с клубникой": ["Сливочная слойка с ягодами клубники, заварным кремом Патисьер и желе", "3.46", "120"],
         "Слойка с изюмом": ["Французская сливочная слойка с изюмом и заварным кремом", "4.5", "75"],
         "Торт Лоуре": [
             "Миндальный бисквит, фисташковый мусс, хрустящий слой из белого шоколада, кокосовой стружки и цельной "
             "вишни, украшен малиновыми макаронами",
             "4.5", "920"],
         "Торт Ализи средний": ["Миндальный бисквит, мусс из малины, фисташковый крем, макарон", "5.59", "490"],
         "Французский рулет с творожным кремом": ["Нежный бисквит, творожный сливочный крем", "3.78", "315"],
         "Торт Медовый": ["Медовый бисквит, крем шантильи с натуральным медом", "2.52", "750"],
         "Макарон с черной смородиной": [
             "Воздушное пирожное из французской миндальной муки с начинкой из черной смородины", "18.1", "20"],
         "Чиабатта с Чиа": [
             "Традиционный итальянский хлеб на яблочной закваске с оливковым маслом, семенами чиа и подсолнечника",
             "1.38", "325"],
         "Булочка Венская ржаная": ["Пресная ржано-пшеничная булочка с семенами льна, подсолнечника, кунжута", "1.09",
                                    "55"],
         "Пирожное Версаль": ["Шоколадный бисквит, мусс из темного шоколада, лимонный крем, шоколад велюр", "6.1",
                              "100"],
         "Круассан с лососем": ["Сливочный круассан, ломтики слабосоленого лосося, мягкий сливочный сыр, зелень", "6.7",
                                "100"]}


def task5_menu():
    print("1-просмотреть описание")
    print("2-просмотреть цены")
    print("3-просмотреть количество")
    print("4-просмотреть всю информацию")
    print("5-совершить покупку")
    print("6-до свидания")
    ch = input("Cделайте выбор: ")
    return ch


def show_goods(mode):
    for good in goods:
        print("-" * 100)
        print(good)
        if mode == "1":
            print(goods[good][0])
        if mode == "2":
            print(goods[good][1], "р. за 100г")
        if mode == "3":
            print(goods[good][2], "г")
        if mode == "4":
            print(goods[good][0], goods[good][1], "р. за 100г", goods[good][2], "г")


def task55(mode='5'):
    result = 0
    check = pd.DataFrame(columns=["name", "amount", "cost"])
    while mode != '1':
        purchase = input("Введите название товара: ")
        if purchase in goods:
            amount = int(input("Укажите количество шт: "))
            cost = amount * float(goods[purchase][1]) * int(goods[purchase][2]) / 100
            result += cost
            check.loc[len(check.index)] = [purchase, amount, round(cost, 2)]
            print("Закончить покупки и оплатить заказ - 1: ")
            mode = input()
        else:
            print("У нас ещё не появилось данного товара :(")
    print("Чек")
    print(check)
    print(f"Итого: {round(result, 2)} р. ")


def task5():
    ch = task5_menu()
    if ch == '6':
        print("До свидания!")
        return
    show_goods(ch)
    if ch == '5':
        task55()
    task5()


def task6():
    print("-" * 100)
    print("Дан кортеж целых чисел. Отсортировать его в порядке убывания. Вывести первый и последний элемент кортежа.")
    print("-" * 100)

    numbers = (3, 21, 239, 0, -9)

    print("Не отсортирован", numbers)
    numbers = tuple(sorted(numbers, reverse=True))
    print("Отсортирован в порядке убывания", numbers)
    print("Максимальный и минимальный элемент картежа", numbers[0], numbers[-1])


while True:
    choice = task_menu()
    if choice == '1':
        task1()
    if choice == '2':
        task2()
    if choice == '3':
        task3()
    if choice == '4':
        task4()
    if choice == '5':
        task5()
    if choice == '6':
        task6()
    if choice == '7':
        break
