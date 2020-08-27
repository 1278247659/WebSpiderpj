card_list = []
def card_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用名片管理系统")

    print("1 新增名片")
    print("2 显示全部")
    print("3 搜索名片")

    print("0 退出系统")
    print("*" * 50)

def new_card():
    print("-" * 50)
    # 1. 提示用户输入名片的详细信息
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入QQ号：")

    # 2. 使用用户输入的信息建立一个名片字典
    card_dict = {"name" : name,
                 "phone" : phone,
                 "qq" : qq}

    # 3. 将名片字典添加到列表中
    card_list.append(card_dict)

    # 4. 提示用户添加成功
    print("名片添加成功")

    print("-" * 50)

def show_card():
    print("姓名     电话     qq")
    print("-" *50)

    for card_dict in card_list:
       print("%s\t\t%s\t\t%s" %(card_dict["name"],
                                card_dict["phone"],
                                card_dict["qq"]))

def search_card():
    names = input("请输入搜索的姓名")
    for card_dict in card_list:

        if card_dict["name"] == names:
            print("姓名        电话        QQ")
            print("=" * 50)
            print("%s  %s   %s   " % (card_dict["name"],
                                         card_dict["phone"],
                                         card_dict["qq"]))
        break
