class CoffeeMachine:
    def __init__(self):
        self.cappuccino = 10 # объем капучино в литрах

    def pour_coffee(self):
        if self.cappuccino >= 0.25: # проверяем, достаточно ли капучино
            self.cappuccino -= 0.25 # вычитаем порцию капучино
            return True # возвращаем True, если кофе налит
        else:
            return False # возвращаем False, если кофе не налит

machine = CoffeeMachine()
petya = 0 # количество выпитого кофе Петей
vasya = 0 # количество выпитого кофе Васей

while machine.pour_coffee(): # пока есть капучино, наливаем кофе
    if petya <= vasya: # Петя пьет первым, если количество кофе одинаковое или меньше
        petya += 0.2
    else:
        vasya += 0.25

if petya > vasya:
    print("Петя победил! Он выпил", petya, "литров кофе.")
elif vasya > petya:
    print("Вася победил! Он выпил", vasya, "литров кофе.")
else:
    print("Ничья! Оба выпили по", petya, "литров кофе.")