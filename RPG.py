import random

PR_atack = [5, 7, 8, 10]
DR_atack = 10
heal = 10
PR_HP = 50
DR_HP = 50
select = 1
heal_count = 0

def menu():
        print("1. 攻撃")
        
        if heal_count == 0:
            print("2. 回復(0/2)")
        elif heal_count == 1:
            print("2. 回復(1/2)")
        else:
            print("2. 回復(使用不可)")
        
        print("3. 逃げる")

def HP_print():
    print(f"""
あなたのHP： {PR_HP}
ドラゴンのHP ： {DR_HP}
---------------------------
    """)


print("=== RPG ===")
print("ドラゴンが現れた！🐉")

while PR_HP > 0 and DR_HP > 0:
    HP_print()
    menu()
    select = int(input("何をしますか？： "))

    if select == 1:
        damage = random.choice(PR_atack)
        print(str(damage) + "ダメージを与えた")
        DR_HP -= damage
        print("ドラゴンの残りHPは" + str(DR_HP))
        if DR_HP <= 0:
            print("""
ドラゴンのHPは0になった！
あなたの勝利です。
-----------------------
経験値を100手に入れた
""")
        else:
            print("""
ドラゴンが攻撃してきた！！
10ダメージ受けた
""")
            PR_HP -= DR_atack
            if PR_HP <= 0:
                 print("""
HPが0になった。
目の前が真っ暗になり気絶した...
""")
    elif select == 2:
        if heal_count >= 2:
            print("もう回復は使えないよ")
        else:
            PR_HP += heal
            heal_count += 1
            print("あなたは回復してHPが" + str(PR_HP) + "になった")