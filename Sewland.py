import random

print("Добро пожаловать в город SEWLAND, но чтобы попасть в крепость ты должен пройти начальное испытание")
class Hero:
    def __init__(self,name: str,health = 100,experience = 0):
        self.name = name
        self.health = health
        self.experience = experience 
name = input("Введите имя героя:")
hero = Hero(name)
print(f"\033[90mСоздан герой {hero.name}, с здоровьем {hero.health}, у которого пока что {hero.experience} опыта\033[0m")

class Evil:
    def __init__(self,name,health):
        self.name = name
        self.health = health


def war(enemy):
    print("\033[31mБой начался⚔\033[0m")
    print(f"Твой противник '{enemy.name}' с здоровьем ({enemy.health})\n")
    round_num = 1
    while hero.health > 0 and enemy.health > 0:
        print(f"\n\033[43m==Раунд {round_num}==\033[0m")
        print("1. Атаковать")
        print("2. Защищаться")

        choice = input("Сделай свой выбор:")
        if choice =="1":
           damage_for_enemy = random.randint(15,30)
           enemy.health = max(0, enemy.health - damage_for_enemy)

           damage_for_hero = random.randint(10,25)
           hero.health = max(0, hero.health - damage_for_hero)

           print(f"\n\033[35mВы нанесли {damage_for_enemy} урона, а {chosen_name} вам нанес {damage_for_hero}\033[0m")
        elif choice == "2":
            damageforhero = random.randint(10,20)
            hero.health = max(0, hero.health - damageforhero)

            damageforenemy = random.randint(10,15)
            enemy.health = max(0, enemy.health - damageforenemy) #Функция max выбирает максимальное из двух чисел: 0 и результата вычитания.Если результат вычитания положительный (например, 20), то max(0, 20) = 20.Если результат отрицательный (например, -10), то max(0, -10) = 0, потому что 0 больше -10.

            print(f"\n\033[36mПосле защиты у вас осталось {hero.health} HP, а у {chosen_name} осталось {enemy.health} HP\033[0m")
        else:
            print("\033[91mНеверный выбор, ты пропускаешь ход!\033[0m")
            damage_to_hero = random.randint(10,20)
            hero.health -= damage_to_hero
            print(f"{chosen_name} наносит вам {damage_to_hero}")

        round_num += 1

    print("\n\033[37m=== Бой окончен ===\033[1m")
    if hero.health <= 0 and enemy.health <= 0:
        print("Ничья! Оба пали в бою.")
        hero.experience += 5
        print(f"За ничью ты получил 5 опыта")
        print(f"Всего у тебя {hero.experience} опыта")

    elif hero.health <= 0:
        print(f"Ты проиграл... {enemy.name} победил.")
        hero.experience = max(0, hero.experience - 10)
        print(f"За проигрыш у тебя осталось {hero.experience} опыта")
        
    else:
        print(f"Победа! Ты одолел '{enemy.name}'.")
        hero.experience += 15 
        print(f"За победу ты получил 15 опыта")
        print(f"Всего у тебя {hero.experience} опыта")

def lvl2():
    print(f"{hero.name} ты отлично справился с начальным истыпаем 🥳 и поэтому ты поподаешь в город SEWLAND")
    while True:
        print("✨" * 30)
        print("✨"," "*15,"Основное меню"," "*24,"✨")
        print("✨" * 30)
        break

print("Пора в бой чтобы получить опыт, а потом ПРИСТИЖ")
while True:
    print("\n \033[96mМеню\033[0m ")
    num = (input("1. Пойти в бой\n""2. Восстановить здоровье.""\n""3. Чтобы выйти:"))
    
    if hero.experience >= 75:
        lvl2()
        hero.experience = 0 
        print("Продолжение следует...")
        break
        
    if num == "1":
        names = ["Скелет", "Зомби"]    

        chosen_name = random.choice(names)

        health = random.randint(55, 100)

        enemy = Evil(chosen_name, health)
        war(enemy)
    elif num =="3":
        print(f"До встречи {hero.name}✋!")
        break

    elif num =="2":
        
        if hero.health == 100:
            print("\033[1;32mУ тебя 100 HP!\033[0m")
        elif hero.health <= 0:
            hero.health += 100
            print("С 0 hp ваше здоровье пополнилось до 100 HP")
        elif hero.health <= 99 and hero.health >= 1:
            hero.health += random.randint(45,65)
            print(f"Твоё здоровье пополнилось до {hero.health} HP")
            if hero.health >=101:
                hero.health = min(100,hero.health)
                print(f"\033[1;32mУ тебя {hero.health} HP\033[0m")

    else:
        print("Попробуй нажать 1")
