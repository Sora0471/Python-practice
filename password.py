import random
import string

num = string.digits
moji = string.ascii_lowercase
word_list = num + moji

print("パスワードを生成します")

keta = int(input("パスワードの桁数を入力してください :"))
password = ""

while len(password) != keta:
    random_word = random.choice(word_list)
    password += random_word

print("パスワードは" + password + "です")