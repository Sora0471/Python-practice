ToDo_list = []
def menu():
        print("""
    ------------------------------
    1. 追加
    2. 一覧
    3. 削除
    4. 終了
    ------------------------------
    """)

print("=== ToDoリスト ===")

select = ""

while select != 4:
    menu()
    select = int(input("選んで数字を入力してください: "))
    if select == 1:
        add = input("追加する内容: ")
        ToDo_list.append(add)
        print(add + "を追加しました")
    elif select == 2:
        print(ToDo_list)
    elif select == 3:
        print(ToDo_list)
        delete = input("削除するものを選んで入力してください: ")
        ToDo_list.remove(delete)
        print(delete + "を削除しました")