message = '\nВведите топпинг, который хотите добавить'
message +=  '\nНапишите "Выйти", когда закончите: '
while True:
    topping = input(message)
    
    if topping == 'Выйти':
        break
    else:
        print(f"\t\n{topping.title()} - хороший выбор!")