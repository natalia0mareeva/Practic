Перейдём в директорию где расположены файлы и сделаем их исполняемыми (chmod +x file_name).  
Благодоря указаному пути к интерпретатору в начале каждого файла (#!/usr/bin/python3), можно выполнить запуск всей композиции.

Для этого необходимо записать следующий конвейер:  
`./task1.py | ./task2.py 2> error.txt | ./task3.py > output.txt 2> error.txt`

В параметрах этого конвейера предусмотрены обработки потоков вывода:  
поток ошибок перенаправляется в файл error.txt.  
поток вывода перенаправляется в файл output.txt.

**При запуске конвейера заполняется только 1 файл (error.txt или output.txt)**  
**Полный текст выполнения дописывается в файл log.txt**

Далее, подробно о каждом файле:

---
### task1 :

При запуске файла task1.py сначала генерируется случайное целое число от -10 до 10.  
Затем число перенаправляется в стандартный поток вывода.

Направление вывода задаётся с помощью параметра file функции print()

---
### task2 :

При запуске файла task2.py из стандартного потока данных считываются данные и преобразовываются к целому типу.  
При отладке программы были опробованы различные варианты ввода, что привело к добавлению ValueError в код программы (например, ввод строки).  
В программе определяется случайный целый делитель от -10 до 10, если делитель будет равен 0 и будет произведена попытка деления на 0, то возникнет ZeroDivisionError.

Для перенаправления возникших ошибок в стандартный поток ошибок используется явное указание - print(..., file = sys.stderr).

---
### task3 :

При запуске файла task3.py из стандартного потока данных считываются данные и преобразовываются к вещественному типу.  
Программа сравнивает поступившее число с 0, если поступившее число меньше 0, то возникает Exception, что сообщит о попытке взять корень отрицательного числа.  
Если поступает 0 или -0 (т.е. в task1 было случайно выбрано 0, а в task2 не было выполнено деление на 0), то программа возвращает резульат (0) в поток вывода.  
Если в task2 была произведена попытка деления на 0, то task3 не получит данных, тогда в потоке ошибок надо явно указать, что ошибка была произведена на прошлом этапе т.к. в конвейере произойдёт перезапись error.txt.