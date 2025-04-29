try:
    with open("config.json") as f:  
    print(f.read())
except FileNotFoundError:
 print("Файл не найден")
