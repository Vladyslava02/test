def search_owner (car_num):
    db = {
        "AA3049BT": "Іван Мельник",
        "BB3689CB": "Володимр Сорока",
        "CB6830AI": "Микола Михайленко"
    }
    return db.get(car_num)
car_num = input('Enter car num')
print(search_owner(car_num))
