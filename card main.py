import card_f

while True:
    card_f.card_menu()
    action = input("请选择你希望执行的操作：")
    print("你选择的操作是%s" %action)

    if action in ["1", "2", "3"]:
        if action == "1":
            card_f.new_card()

        elif action == "2":
            card_f.show_card()

        elif action == "3":
                    card_f.search_card()
        elif action == "0":
         print("欢迎再次使用名片系统")

    else:
         print("您的输入有误，请重新输入")


