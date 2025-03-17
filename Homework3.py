# Zhdanovich Valery
# Date: 17/03/2024
# Description: Homework 3
# Grodno IT Academy Python 3.9.6

def pairs(numbers_string):
    #Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
    #Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
    #Входные данные - строка из чисел, разделенная пробелами.
    #Выходные данные - количество пар.
    #Важно: `1 1 1` - это 3 пары, `1 1 1 1` - это 6 пар.
    numbers = list(map(int, numbers_string.split())) # Преобразуем строку с числами в список целых чисел
    pairs = 0 # Инициализируем счетчик пар
    nums_pairs = {} # Словарь для хранения количества вхождений каждого числа

    for num in numbers:
        if num in nums_pairs: # Проверяем, есть ли число уже в словаре
            pairs += nums_pairs[num] # Если есть, добавляем к количеству пар количество текущих вхождений числа
            nums_pairs[num] += 1
        else:
            nums_pairs[num] = 1 # Если числа нет в словаре, добавляем его с количеством 1
    return pairs


def uniques(array):
    #Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
    #Элементы нужно выводить в том порядке, в котором они встречаются в списке.
    counts = {}  # Словарь для подсчета вхождений каждого элемента
    uniques = []  # Список для хранения уникальных элементов в нужном порядке
    for element in array:
        if element in counts:
            counts[element] += 1 # Если элемент уже в словаре, увеличиваем его счетчик
        else:
            counts[element] = 1 # Если новый элемент, добавляем его в словарь с счетчиком 1

    for element in array:
        if counts[element] == 1: 
            uniques.append(element) # Если элемент встречается только один раз, добавляем его в список уникальных
    return uniques


def ordered_list(array):
    # Дан список целых чисел. Требуется переместить все ненулевые элементы в левую часть списка,
    # не меняя их порядок, а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя,
    # дополнительный список использовать нельзя, задачу нужно выполнить за один проход по списку.
    # Верните полученный список.
    nonzero_index = 0  # Индекс для отслеживания позиции для следующего ненулевого элемента

    for i in range(len(array)):
        if array[i] != 0:
            # Если текущий элемент ненулевой, перемещаем его в начало списка (в позицию nonzero_index)
            array[i], array[nonzero_index] = array[nonzero_index], array[i]
            nonzero_index += 1  # Увеличиваем индекс для следующего ненулевого элемента
    return array


def tuple_to_list(in_tuple):
    #Возмите кортеж `('a', 'b', 'c')`, И сделайте из него список.
    lst = list(in_tuple) # Преобразуем кортеж в список
    return lst

def euclid(a,b):
    #Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи алгоритма Евклида (мы не знаем функции и рекурсию). can't call itself
    while b != 0:
        a, b = b, a % b  # Обновляем a и b
    return a  # Когда b станет равным 0, a содержит НОД

#Dictionaries
def cities(input_string):
    #Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.
    #Учтите, что бывают ситуации когда город с таким называнием бывает в разных странах (Брест есть в Беларуси и Франции).
    #Входные данные
    #Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается с названия страны, затем идут названия городов этой страны.
    #В следующей строке записано число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.
    #Выходные данные
    #Для каждого из запроса выведите название страны, в котором находится данный город.
    #Пример данных:
    #Входные данные
    #2
    #Russia Moscow Petersburg Novgorod Kaluga
    #Ukraine Kiev Lvov Odessa
    #3
    #Odessa
    #Moscow
    #Novgorod
    #Выходные данные
    #Ukraine
    #Russia
    #Russia
    #input_string = "2\nRussia Moscow Petersburg Novgorod Kaluga\nUkraine Kiev Lvov Odessa\n3\nOdessa\nMoscow\nNovgorod"
    #output_string = 'Ukraine\nRussia\nRussia'
    #country_map={}
    lines = input_string.split('\n') # Разбиваем входное значение на строки

    N = int(lines[0]) # Считываем количество стран

    country_map = {}  # Словарь для хранения стран и городов

    for i in range(1, N + 1): # Обрабатываем информацию о странах и городах
        data = lines[i].split()
        country = data[0]
        cities = data[1:]

        for city in cities:
            if city not in country_map:
                country_map[city] = []  
            country_map[city].append(country)

    M = int(lines[N + 1]) # Считываем количество запросов

    input_string = [] # Результат для каждого запроса

    for j in range(N + 2, N + 2 + M): # Обрабатываем запросы
        city_query = lines[j].strip()
        if city_query in country_map:
            input_string.append(' '.join(country_map[city_query]))  # Используем пробел для объединения стран
        else:
            input_string.append("Unknown")  # На случай, если город не найден
    return '\n'.join(input_string)

#Sets
def languages(input_string):
    #Задачи для домашней работы
    #Языки
    #Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
    #Входные данные
    #Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й школьник.
    #Пример входных данных:
    #3 # N количество школьников
    #2 # M1 количество языков первого школьника
    #Russian # языки первого школьника
    #English
    #3 # M2 количество языков второго школьника
    #Russian
    #Belarusian
    #English
    #3
    #Russian
    #Italian
    #French
    #Выходные данные
    #В первой строке выведите количество языков, которые знают все школьники. Начиная со второй строки - список таких языков.
    #Затем - количество языков, которые знает хотя бы один школьник, на следующих строках - список таких языков.
    #input_string = "3\n2\nRussian\nEnglish\n3\nRussian\nBelarusian\nEnglish\n3\nRussian\nItalian\nFrench"
    #output_string = '1\nRussian\n5\nRussian\nFrench\nItalian\nEnglish\nBelarusian'
    data = input_string.strip().split('\n')
    
    N = int(data[0])  # Количество школьников
    index = 1
    all_languages = set()  # Языки, которые знает хотя бы один школьник
    common_languages = None  # Языки, которые знают все школьники

    for _ in range(N):
        Mi = int(data[index])  # Количество языков i-го школьника
        index += 1
        
        current_languages = set() # Множество языков текущего школьника
        
        for _ in range(Mi):
            language = data[index].strip()
            current_languages.add(language)
            index += 1
            
        # Обновляем множества
        all_languages.update(current_languages)  # Языки, которые знает хотя бы один школьник
        
        if common_languages is None:
            common_languages = current_languages  # Инициализируем, если это первый школьник
        else:
            common_languages.intersection_update(current_languages)  # Пересекаем с языками текущего школьника

    # Преобразуем множества в отсортированные списки
    common_languages_list = sorted(common_languages)  # Языки, которые знают все
    all_languages_list = sorted(all_languages)  # Языки, которые знает хотя бы один

    # Формируем результат
    input_string = []
    input_string.append(str(len(common_languages_list)))  # Количество языков, которые знают все
    input_string.extend(common_languages_list)  # Языки, которые знают все
    
    input_string.append(str(len(all_languages_list)))  # Количество языков, которые знает хотя бы один
    input_string.extend(all_languages_list)  # Языки, которые знает хотя бы один

    return '\n'.join(input_string)

#Generators
def list_gen(arr1, arr2):
    #Генераторы списков
    #Используйте генератор списков чтобы получить следующий: ['xy', 'xz', 'xv', 'yy', 'yz', 'yv']. из ['x','y'] & ['y','z','v']
    #пример:
    result = [a + b for a in arr1 for b in arr2] # Генераторы списков для создания списка пар
    return result


#Генераторы словарей
def dict_gen(N):
    #Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до N, а значениями кубы этих чисел.
    result = {i: i**3 for i in range(1, N+1)} # Генератор словарей
    return result

#Кортежи
def multiplication_table(N):
    #Создайте генератор, который возвращает строки таблицы умножения от 0 до заданного числа.
    # Генератор для создания таблицы умножения от 0 до N
    for i in range(N + 1): # Генератор для создания таблицы умножения
        yield ' '.join(str(i * j) for j in range(N + 1))
    table = N
    return table