import random

print("数当てゲームへようこそ！")
answer = random.randint(1, 100)
guess = 0

while answer != guess:
    guess = int(input("予想する数を入力してください"))
    if guess == answer:
        print("おめでとう！！答えは" + str(answer) + "であたりだよ！！")
    elif guess < answer:
        print("答えよりその数は小さいよ！")
    elif guess > answer:
        print("答えよりその数は大きいよ！")