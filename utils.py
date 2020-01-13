from pathlib import Path
import sys
import os
import datetime
import re


def cls(argument):
    r"""
Очищает содержимое экрана

CLS

"""
    if len(argument) == 0:
        os.system('cls')
    else:
        print('cls' + argument, """ не является внутренней или внешней
командой, исполняемой программой или пакетным файлом utils.""")
        return 'wrong_argument'

    
def help(cli):
    r"""
Для получения сведений об определенной команде наберите HELP <имя команды>
ASSOC          Вывод либо изменение сопоставлений по расширениям имен файлов.
ATTRIB         Отображение и изменение атрибутов файлов.
BREAK        Включение и выключение режима обработки комбинации клавиш CTRL+C.
BCDEDIT        Задает свойства в базе данных загрузки для управления начальной
               загрузкой.
CACLS          Отображение и редактирование списков управления доступом (ACL)
               к файлам.
CALL           Вызов одного пакетного файла из другого.
CD             Вывод имени либо смена текущей папки.
CHCP           Вывод либо установка активной кодовой страницы.
CHDIR          Вывод имени либо смена текущей папки.
CHKDSK         Проверка диска и вывод статистики.
CHKNTFS        Отображение или изменение выполнения проверки диска во время
               загрузки.
CLS            Очистка экрана.
CMD            Запуск еще одного интерпретатора командных строк Windows.
COLOR       Установка цветов переднего плана и фона, используемых по умолчанию.
COMP           Сравнение содержимого двух файлов или двух наборов файлов.
COMPACT        Отображение и изменение сжатия файлов в разделах NTFS.
CONVERT        Преобразование дисковых томов FAT в NTFS. Нельзя выполнить
               преобразование текущего активного диска.
COPY           Копирование одного или нескольких файлов в другое место.
DATE           Вывод либо установка текущей даты.
DEL            Удаление одного или нескольких файлов.
DIR            Вывод списка файлов и подпапок из указанной папки.
DISKCOMP       Сравнение содержимого двух гибких дисков.
DISKCOPY       Копирование содержимого одного гибкого диска на другой.
DISKPART       Отображение и настройка свойств раздела диска.
DOSKEY         Редактирование и повторный вызов командных строк; создание
               макросов.
DRIVERQUERY    Отображение текущего состояния и свойств драйвера устройства.
ECHO           Вывод сообщений и переключение режима отображения команд на
               экране.
ENDLOCAL       Конец локальных изменений среды для пакетного файла.
ERASE          Удаление одного или нескольких файлов.
EXIT           Завершение работы программы CMD.EXE (интерпретатора командных
               строк).
FC             Сравнение двух файлов или двух наборов файлов и вывод различий
               между ними.
FIND           Поиск текстовой строки в одном или нескольких файлах.
FINDSTR        Поиск строк в файлах.
FOR            Запуск указанной команды для каждого из файлов в наборе.
FORMAT         Форматирование диска для работы с Windows.
FSUTIL         Отображение и настройка свойств файловой системы.
FTYPE          Вывод либо изменение типов файлов, используемых при
               сопоставлении по расширениям имен файлов.
GOTO           Передача управления в отмеченную строку пакетного файла.
GPRESULT       Отображение информации о групповой политике для компьютера или
               пользователя.
GRAFTABL       Позволяет Windows отображать расширенный набор символов в
               графическом режиме.
HELP           Выводит справочную информацию о командах Windows.
ICACLS         Отображение, изменение, архивация или восстановление
               списков ACL для файлов и каталогов.
IF             Оператор условного выполнения команд в пакетном файле.
LABEL          Создание, изменение и удаление меток тома для дисков.
MD             Создание папки.
MKDIR          Создание папки.
MKLINK         Cоздание символических и жестких ссылок
MODE           Конфигурирование системных устройств.
MORE           Последовательный вывод данных по частям размером в один экран.
MOVE           Перемещение одного или нескольких файлов из одной папки
               в другую.
OPENFILES      Отображение файлов, открытых на общей папке удаленным
               пользователем.
PATH           Отображает или устанавливает путь поиска исполняемых файлов.
PAUSE          Приостанавливает выполнение пакетного файла и выводит сообщение.
POPD           Восстанавливает предыдущее значение активной папки,
               сохраненное с помощью команды PUSHD.
PRINT          Выводит на печать содержимое текстового файла.
PROMPT         Изменяет приглашение в командной строке Windows.
PUSHD          Сохраняет значение активной папки и переходит к другой папке.
RD             Удаляет папку.
RECOVER        Восстанавливает данные, которые можно прочитать, с плохого или
               поврежденного диска.
REM            Помещает комментарии в пакетные файлы и файл CONFIG.SYS.
REN            Переименовывает файлы или папки.
RENAME         Переименовывает файлы или папки.
REPLACE        Замещает файлы.
RMDIR          Удаление папки.
ROBOCOPY       Улучшенное средство копирования файлов и деревьев каталогов
SET            Показывает, устанавливает и удаляет переменные среды Windows.
SETLOCAL       Начинает локализацию изменений среды в пакетном файле.
SC             Отображает и настраивает службы (фоновые процессы).
SCHTASKS       Выполняет команды и запускает программы по расписанию.
SHIFT          Изменение положения (сдвиг) подставляемых параметров для
пакетного файла.
SHUTDOWN       Локальное или удаленное выключение компьютера.
SORT           Сортировка ввода.
START          Выполнение программы или команды в отдельном окне.
SUBST          Назначение заданному пути имени диска.
SYSTEMINFO     Вывод сведений о системе и конфигурации компьютера.
TASKLIST       Отображение всех выполняемых задач, включая службы.
TASKKILL       Прекращение или остановка процесса или приложения.
TIME           Вывод и установка системного времени.
TITLE          Назначение заголовка окна для текущего сеанса интерпретатора
               командных строк CMD.EXE.
TREE           Графическое отображение структуры каталогов диска или папки.

TYPE           Вывод на экран содержимого текстовых файлов.
VER            Вывод сведений о версии Windows.
VERIFY         Установка режима проверки правильности записи файлов на диск.

VOL            Вывод метки и серийного номера тома для диска.
XCOPY          Копирование файлов и деревьев каталогов.
WMIC           Вывод сведений WMI в интерактивной среде.

Дополнительные сведения о программах приведены в описании программ командной строки в справке.
    """
    print(help.__doc__)


def cd(argument):
    r""""Вывод имени либо смена текущего каталога.

CHDIR [/D] [диск:][путь]
CHDIR [..]
CD [/D] [диск:][путь]
CD [..]

  ..  обозначает переход в родительский каталог.

Команда CD диск: отображает имя текущего каталога указанного диска.
Команда CD без параметров отображает имена текущих диска и каталога.

Параметр /D используется для одновременной смены
текущих диска и каталога.

Изменение команды CHDIR при включении расширенной обработки команд:

Имя текущего каталога в строке вызова преобразуется к тому же регистру
символов, что и для существующих имен на диске.  Так, команда CD C:\TEMP
на самом деле сделает текущим каталог C:\Temp, если он существует на диске.

Команда CHDIR перестает рассматривать пробелы как разделители, что позволяет
перейти в подкаталог, имя которого содержит пробелы, не заключая все имя
каталога в кавычки.  Например:

    cd \winnt\profiles\username\programs\start menu

приводит к тому же результату, что и:

    cd "\winnt\profiles\username\programs\start menu"

При отключении расширенной обработки команд используется только второй вариант.


"""
    if len(argument) > 0:
        command = re.split(r'[ ]', argument, maxsplit=1)
        if len(command) > 1 and command[0] == '/d':
                path = command[1]
        else:
            path = argument
        if not os.path.isdir(path):
            print('Системе не удается найти указанный путь.')
        else:
            accert: os.path.isdir(path)
            os.chdir(path)
    elif argument == '':
            print(os.getcwd())

def dir(cli):
    r"""
Вывод списка файлов и подкаталогов в указанном каталоге.

DIR [диск:][путь][имя файла] [/A[[:]атрибуты]] [/B] [/C] [/D] [/L] [/N]
  [/O[[:]порядок сортировки]] [/P] [/Q] [/R] [/S] [/T[[:]время]] [/W] [/X] [/4]

  [диск:][путь][имя файла]
              Диск, каталог или имена файлов для включения в список.

  /A          Отображение файлов с указанными атрибутами.
  атрибуты     D  Каталоги.            R  Файлы, доступные только для чтения.
               H  Скрытые файлы.       A  Файлы, готовые для архивирования.
               S  Системные файлы.     I  Файлы с неиндексированным содержимым.
               L  Точки повторной обработки.  -  Префикс "-" имеет значение НЕ.
  /B          Вывод только имен файлов.
  /C          Применение разделителя групп разрядов при выводе размеров файлов.
              Используется по умолчанию.  Чтобы отключить применение
              разделителя групп разрядов, задайте ключ /-C.
  /D          Вывод списка в нескольких столбцах с сортировкой по столбцам.
  /L          Использовать нижний регистр для имен файлов.
  /N          Новый формат длинного списка, имена файлов выводятся в крайнем
              правом столбце.
  /O          Сортировка списка отображаемых файлов.
  порядок      N  По имени (по алфавиту)
  сортировки   S  По размеру (начиная с минимального)
               E  По расширению (по алфавиту)
               D  По дате и времени (начиная с самого старого)
               G  Начать список с каталогов.  -  Префикс "-" обращает порядок.
  /P          Пауза после заполнения каждого экрана.
  /Q          Вывод сведений о владельце файла.
  /R          Отображение альтернативных потоков данных этого файла.
  /S          Отображение файлов из указанного каталога и всех его
              подкаталогов.
  /T          Выбор поля времени для сортировки.
  время       C  Создание.
              A  Последнее использование.
              W  Последнее изменение.
  /W          Вывод списка в несколько столбцов.
  /X          Отображение коротких имен для файлов, чьи имена не соответствуют
              стандарту 8.3. Формат аналогичен выводу с ключом /N, но короткие
              имена файлов выводятся слева от длинных. Если короткого имени у
              файла нет, вместо него выводятся пробелы.
  /4          Вывод номера года в четырехзначном формате.

Стандартный набор ключей можно записать в переменную среды DIRCMD.  Для отмены
их действия введите в команде те же ключи с префиксом "-", например: /-W.

    """
    print('Содержимое папки', os.getcwd())
    dir_count = 0
    files_counter = 0
    file_size = 0
    summ_files_size = 0
    for item in os.listdir('.'):
        if Path(item).is_dir():
            file_size = ''
            dir_or_file = '   <DIR>   '
            dir_count += 1
        else:
            dir_or_file = '           '
            file_size = os.stat(item).st_size
            summ_files_size += file_size
            files_counter += 1
        filetime = os.path.getmtime(item)
        x = datetime.datetime.fromtimestamp(filetime)
        print(x.strftime('%m.%d.%Y  %H:%M'), dir_or_file, '{:>10}'.format(file_size), item)
    print('{:>13}'.format(files_counter), 'файлов', summ_files_size, 'байт')


def quit(cli):
    r"""
quit & exit commands
    """
    sys.exit()

    
def __drawtree(path, seen, head='', tail=''):
    """ for tree function """
    
    fork_string   = '├──'
    corner_string = '└──'
    wall_string   = '│  '
    space_string  = '   '
    
    if path.is_dir() and path.resolve() not in seen:
        yield head + path.name
        seen.add(path.resolve()) # на случай зацикленных ссылок
        entries = sorted(filter(Path.is_dir, path.iterdir()))

        for i, entry in enumerate(entries):
            if i < len(entries) - 1:
                yield from __drawtree(entry, seen, tail + fork_string, tail + wall_string)
            else:
                yield from __drawtree(entry, seen, tail + corner_string, tail + space_string)

def tree(arg, my_path='.'):
    r"""
Графическое представление структуры папок или пути.

TREE [диск:][путь] [/F] [/A]

   /F   Вывод имен файлов в каждой папке.
   /A   Использовать символы ASCII вместо символов национальных алфавитов.
    """
    if os.path.isdir(str(arg).strip()):
        my_path = str(arg).strip()
        
    for line in __drawtree(Path(my_path), set()):
        print(line)
