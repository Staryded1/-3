from watchdog.events import FileSystemEventHandler
numbers = ['0','1','2','3','4','5','6','7','8','9']

def on_create(path: str):
    global my_file
    my_file = open(path, "w+")

def main():
    import_file: str = input("Введите имя файла: ")
    if len(import_file) < 3:
        print('"Введите строку с кол-вом символов больше 3')
        main()
    for a in import_file:
        if a in numbers:
            print ("Введите строку без чисел")
            main()
        else:         
            on_create("files/" + import_file + ".txt")
                
main()
