import random
hand = ["グー", "チョキ", "パー"]
CP_hand = int(random.randint(0, 2))
PR_hand = 1
print("===じゃんけんゲームへようこそ===")
print("------------------------------------")
print("最初はグー！じゃんけん・・！")

PR_hand = int(input("何を出しますか？数字で答えてください：グー=0, チョキ=1, パー=2 ："))

while CP_hand == PR_hand:
    print("相手は同じ手を出してあいこでした")
    print(("------------------------------------"))
    CP_hand = int(random.randint(0, 2))
    PR_hand = int(input("あいこでしょ！！："))

if CP_hand == 0 and PR_hand == 1:
    print("相手は" + hand[CP_hand] + "を出しました。あなたの負けです")
elif CP_hand == 1 and PR_hand == 2:
    print("相手は" + hand[CP_hand] + "を出しました。あなたの負けです")
elif CP_hand == 2 and PR_hand == 0:
    print("相手は" + hand[CP_hand] + "を出しました。あなたの負けです")
elif CP_hand == 2 and PR_hand == 1:
    print("相手は" + hand[CP_hand] + "を出しました。あなたの勝ちです")
elif CP_hand == 1 and PR_hand == 0:
    print("相手は" + hand[CP_hand] + "を出しました。あなたの勝ちです")
elif CP_hand == 0 and PR_hand == 2:
    print("相手は" + hand[CP_hand] + "を出しました。あなたの勝ちです")