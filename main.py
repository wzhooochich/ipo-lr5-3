# открывает файл text.txt , читает его и обозначает как file
with open('text.txt', 'r') as file:
    # переменная info , хранит содержимое file
    info = file.read()  
    # переменная ворд хранит данные переменной info, в которой split убирает пробелы
    words = info.split() 
    #возвращение длины строки
    print("Слов в файле : " + str(len(words)))
