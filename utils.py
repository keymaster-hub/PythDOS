from pathlib import Path
import sys
import os
import datetime
import re
import shutil


def dos_help(cli):
    r"""
Для получения сведений об определенной команде наберите HELP <имя команды>
CALL           Вызов одного пакетного файла из другого.
CD             Вывод имени либо смена текущей папки.
CHDIR          Вывод имени либо смена текущей папки.
CLS            Очистка экрана.
COPY           Копирование одного или нескольких файлов в другое место.
DEL            Удаление одного или нескольких файлов.
DIR            Вывод списка файлов и подпапок из указанной папки.
ERASE          Удаление одного или нескольких файлов.
EXIT           Завершение работы программы.
HELP           Выводит справочную информацию о командах Windows.
MD             Создание папки.
MKDIR          Создание папки.
MOVE           Перемещение одного или нескольких файлов из одной папки в другую.
POPD           Восстанавливает предыдущее значение активной папки,
               сохраненное с помощью команды PUSHD.
PRINT          Выводит на печать содержимое текстового файла.
PROMPT         Изменяет приглашение в командной строке Windows.
PUSHD          Сохраняет значение активной папки и переходит к другой папке.
RD             Удаляет папку.
REN            Переименовывает файлы или папки.
RENAME         Переименовывает файлы или папки.
RMDIR          Удаление папки.
TREE           Графическое отображение структуры каталогов диска или папки.
TYPE           Вывод на экран содержимого текстовых файлов.

Дополнительные сведения о программах приведены в описании программ командной строки в справке.
    """
    print(dos_help.__doc__)


def dos_copy(argument):
    r"""
Копирование файлов и каталогов в другое место.

COPY  источник результат
"""
    if len(argument.split()) == 2:
        source_dest = argument.split()
        source = source_dest[0]
        dest = source_dest[1]
        try:
            if os.path.isfile(source):
                shutil.copy(source, dest)
            elif os.path.isdir(source):
                os.mkdir(os.path.join(dest, source))
                dest = os.path.join(dest, source)
                for item in os.listdir(source):
                    s = os.path.join(source, item)
                    d = os.path.join(dest, item)
                    if os.path.isdir(s):
                        shutil.copytree(s, d)
                    else:
                        shutil.copy2(s, d)
            print("%s copyed to %s successfully." % (source, dest))
        # If source or dest not found
        except FileNotFoundError as error:
            print(error)

        # For other errors
        except OSError as error:
            print(error)
    else:
        return            
            

def dos_move(argument):
    r"""
Перемещение одного или более файлов:

MOVE [диск:][путь]имя_файла назначение

"""
    if len(argument.split()) == 2:
        source_dest = argument.split()
        source = source_dest[0]
        dest = source_dest[1]
        try:
            shutil.move(source, dest)
            print("%s moved to %s successfully." % (source, dest))
            
        # If source or dest not found    
        except FileNotFoundError as error:
            print(error)
            
        # For other errors
        except OSError as error:
            print(error)
    else:
        return
            

def dos_rename(argument):
    r"""
    Переименование директорий и файлов.

RENAME [диск:][путь]имя_файла1 имя_файла2.
REN [диск:][путь]имя_файла1 имя_файла2.
    """
    if len(argument.split()) == 2:
        source_dest = argument.split()
        source = source_dest[0]
        dest = source_dest[1]
        try:
            os.rename(source, dest)
            print("%s renamed to %s successfully." % (source, dest))

        # If Source is a file
        # but destination is a directory
        except IsADirectoryError:
            print("Source is a file but destination is a directory.")

        # If source is a directory
        # but destination is a file
        except NotADirectoryError:
            print("Source is a directory but destination is a file.")

        # For permission related errors
        except PermissionError:
            print("Operation not permitted.")

        # For other errors
        except OSError as error:
            print(error)
    else:
        return


def dos_mkdir(path):
    r"""
    Создание каталога.

MKDIR [диск:]путь
MD [диск:]путь

Изменение команды MKDIR при включении расширенной обработки команд:

Команда MKDIR создает при необходимости все промежуточные каталоги в пути.
Например, если \a не существует, то:

    mkdir \a\b\c\d

приводит к тому же результату, что и:

    mkdir \a
    chdir \a
    mkdir b
    chdir b
    mkdir c
    chdir c
    mkdir d

При отключении расширенной обработки команд используется только второй вариант.
    """
    try:
        os.mkdir(path)
        print("Directory '%s' created" % path)
    except OSError as error:
        print(error)


def dos_rmdir(path):
    r"""
    Удаление каталога.

RMDIR [/S] [/Q] [диск:]путь
RD [/S] [/Q] [диск:]путь

    /S      Удаление дерева каталогов, т. е. не только указанного каталога,
            но и всех содержащихся в нем файлов и подкаталогов.

    /Q      Отключение запроса подтверждения при удалении дерева каталогов
            с помощью ключа /S.
    """
    try:
        os.removedirs(path)
        print("Directory removed successfully")

        # If path is not a directory
    except NotADirectoryError:
        print("Specified path is not a directory.")

        # If permission related errors
    except PermissionError:
        print("Permission denied.")

        # for other errors
    except OSError as error:
        print(error)
        print("Directory can not be removed")


def dos_del(path):
    r"""
    Удаление одного или нескольких файлов.

DEL [/P] [/F] [/S] [/Q] [/A[[:]атрибуты]] имена
ERASE [/P] [/F] [/S] [/Q] [/A[[:]атрибуты]] имена

  имена         Список из одного или нескольких файлов или каталогов.
                Для удаления группы файлов можно использовать подстановочные
                знаки. Если указан каталог, будут удалены все файлы в этом
                каталоге.

  /P            Запрос подтверждения перед удалением каждого файла.
  /F            Принудительное удаление файлов, доступных только для чтения.
  /S            Удаление указанных файлов из всех подкаталогов.
  /Q            Отключение запроса на подтверждение при удалении файлов.
  /A            Отбор файлов для удаления по атрибутам.
  атрибуты      R  Файлы, доступные только для чтения.
                S  Системные файлы.
                H  Скрытые файлы.
                A  Файлы, готовые для архивирования.
                I  Файлы с неиндексированным содержимым.
                L  Точки повторной обработки.
                -  Префикс "-" имеет значение НЕ.

Изменение команд DEL и ERASE при включении расширенной обработки команд:

Результаты вывода для ключа /S принимают обратный характер, то есть выводятся
только имена удаленных файлов, а не файлов, которые не удалось найти.
    """

    try:
        os.remove(path)
        print("% s removed successfully" % path)
    except OSError as error:
        print(error)
        print("File path can not be removed")


def dos_type(argument):
    r"""
Вывод содержимого одного или нескольких текстовых файлов.

TYPE [диск:][путь]имя_файла
"""
    try:
        if os.path.isfile(argument):
            with open(argument, 'r') as file:
                for line in file:
                    print(line.strip())
        elif argument == '':
            print('Ошибка в синтаксисе команды')
        else:
            print('Не удается найти указанный файл.')
    except OSError as error:
        print(error)


def dos_cls(argument):
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


def dos_cd(argument):
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


def dos_dir(path):
    r"""
Вывод списка файлов и подкаталогов в указанном каталоге.

DIR [диск:][путь][имя файла]

    """
    try:    
        path = os.path.join(os.getcwd(), path)
        print('Содержимое папки', path)
        dir_count = 0
        files_counter = 0
        file_size = 0
        summ_files_size = 0
        for item in os.listdir(path):
            if Path(os.path.join(path, item)).is_dir():
                file_size = ''
                dir_or_file = '   <DIR>   '
                dir_count += 1
                filetime = os.path.getmtime(os.path.join(path, item))
                x = datetime.datetime.fromtimestamp(filetime)
                print(x.strftime('%m.%d.%Y  %H:%M'), dir_or_file, '{:>10}'.format(file_size), item)
        for item in os.listdir(path):
            if Path(os.path.join(path, item)).is_file():
                dir_or_file = '           '
                file_size = os.stat(os.path.join(path, item)).st_size
                summ_files_size += file_size
                files_counter += 1
                filetime = os.path.getmtime(os.path.join(path, item))
                x = datetime.datetime.fromtimestamp(filetime)
                print(x.strftime('%m.%d.%Y  %H:%M'), dir_or_file, '{:>10}'.format(file_size), item)
        print('{:>13}'.format(files_counter), 'файлов', summ_files_size, 'байт')
    except OSError as error:
        print(error)    


def dos_quit(cli):
    r"""
quit & exit commands
    """
    sys.exit()



def tree(path='.', head='', tail=''):
    r"""
Графическое представление структуры папок или пути.

TREE [диск:][путь]

    """
    path = Path(path)

    if path.is_dir():
        print(head + path.name)
        entries = sorted(filter(Path.is_dir, path.iterdir()))

        for i, entry in enumerate(entries):
            if i < len(entries) - 1:
                tree(entry, tail + '|--', tail + '|  ')
            else:
                tree(entry, tail + '|__', tail + '   ')
