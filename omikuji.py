import random

kuji = ("大吉", "吉", "中吉", "小吉", "末吉", "凶", "大凶")
answer = ""
print("=== 今日のおみくじ ===")
while answer != "はい":
    answer = input("引く? ：引く場合は'はい'と入力してください。")

    if answer == "はい":
        result = random.choice(kuji)
        print("今日の運勢は" + result + "です")