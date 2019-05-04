import random

MAX_MY_LIFE = 20
my_life = 20
my_attack_list = [3, 5, 7, 9, 11, 20, 100]
enemy_life_list = [5, 10, 15, 20]
enemy_attack_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20]
heal_list = [1, 3, 5, 7, 9, 11, 13, 15]
next_text = "1歩進んだ"
walk = 6
while walk > 0 and my_life > 0:
    walk -= 1
    print("出口まで{0}歩".format(walk))
    print("HP{0}".format(my_life))
    print(next_text)
    event = random.randint(1, 3)
    if event == 1:
        print("敵が現れた！")
        enemy_life = random.choice(enemy_life_list)
        print("敵のHP{0}".format(enemy_life))
        print("自分のHP{0}".format(my_life))
        while enemy_life > 0 and my_life > 0:
            print("コマンドを選択")
            print("1:たたかう 2:にげる")
            command = input()
            if command == "1":
                print("プレイヤーの攻撃！")
                my_attack = random.choice(my_attack_list)
                print("{0}のダメージ".format(my_attack))
                enemy_life = enemy_life - my_attack
                if enemy_life <= 0:
                    print("敵を倒した")
                    break
                print("敵の攻撃！")
                enemy_attack = random.choice(enemy_attack_list)
                my_life = my_life - enemy_attack
                print("{0}のダメージ".format(enemy_attack))
                if my_life <= 0:
                    print("倒されてしまった")
                    break
                print("敵のHP{0}".format(enemy_life))
                print("自分のHP{0}".format(my_life))
            if command == "2":
                escape = random.randint(0, 1)
                if escape == 0:
                    print("回り込まれた！")
                    print("敵の攻撃！")
                    enemy_attack = random.choice(enemy_attack_list)
                    my_life = my_life - enemy_attack
                    print("{0}のダメージ".format(enemy_attack))
                print("敵のHP{0}".format(enemy_life))
                print("自分のHP{0}".format(my_life))
                if escape == 1:
                    print("うまく逃げ切れた")
                    break
    if event == 2:
        print("回復します")
        heal_point = random.choice(heal_list)
        my_life = my_life + heal_point
        my_life = min(my_life, MAX_MY_LIFE)
        print("HPを{0}回復！".format(heal_point if my_life < MAX_MY_LIFE else "最大"))
        print("自分のHP{0}".format(my_life))
    if event == 3:
        print("何も起こらなかった")
if my_life > 0:
    print("おめでとう！洞窟を出られました")
