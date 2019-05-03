import random
mylife = 20
myattacklist = [3,5,7,9,11,20,100]
enemylifelist = [5,10,15,20]
enemyattacklist = [1,2,3,4,5,6,7,8,9,10,15,20]
heallist = [1,3,5,7,9,11,13,15]
next = "1歩進んだ"
walk = 6
while walk >= 2 :
    if(walk >= 2):
        walk -= 1
        print("出口まで"+str(walk)+"歩")
        print("HP"+str(mylife))
        print(next)
        actionlist = random.choice(("敵が現れた！", "回復します", "何も起こらなかった"))
        if actionlist == "敵が現れた！":
            print("敵が現れた！")
            enemylife = random.choice(enemylifelist)
            print("敵のHP"+str(enemylife))
            print("自分のHP"+str(mylife))
            while enemylife > 0 and mylife > 0:
                print("コマンドを選択")
                input("1:たたかう 2:にげる")
                command = input()
                if int(command) == 1:
                    print("プレイヤーの攻撃！")
                    myattack = random.choice(myattacklist)
                    print(str(myattack)+"のダメージ")
                    enemylife = enemylife - myattack
                    if enemylife <= 0:
                        print("敵を倒した")
                        break
                    print("敵の攻撃！")
                    enemyattack = random.choice(enemyattacklist)
                    mylife = mylife - enemyattack
                    print(str(enemyattack)+"のダメージ")
                    if mylife <= 0:
                        print("倒されてしまった")
                        break
                    print("敵のHP"+str(enemylife))
                    print("自分のHP"+str(mylife))
                if int(command) == 2:
                    escape = random.choice(("回り込まれた！", "うまく逃げ切れた"))
                    if escape == "回り込まれた！":
                        print("回り込まれた！")
                        print("敵の攻撃！")
                        enemyattack = random.choice(enemyattacklist)
                        mylife = mylife - enemyattack
                        print(str(enemyattack)+"のダメージ")
                    print("敵のHP"+str(enemylife))
                    print("自分のHP"+str(mylife))
                    if escape == "うまく逃げ切れた":
                        print("うまく逃げ切れた")
                        break
        if actionlist == "回復します":
            print("回復します")
            healpoint = random.choice(heallist)
            mylife = mylife + healpoint
            if mylife > 20:
                mylife = 20
            print("HPを"+str(healpoint)+"回復！")
            print("自分のHP"+str(mylife))
        if actionlist == "何も起こらなかった":
            print("何も起こらなかった")
    if(walk == 1):
        print("出口まで"+str(walk)+"歩")
        print(next)
        print("おめでとう！洞窟を出られました")
