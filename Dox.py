import webbrowser

def display_ascii_art():
    print("""
 $$$$$$\  $$\             $$$$$$$\                      $$\                     
$$  __$$\ $$ |            $$  __$$\                     \__|                    
$$ /  \__|$$ |            $$ |  $$ | $$$$$$\  $$\   $$\ $$\ $$$$$$$\   $$$$$$\  
$$ |      $$ |            $$ |  $$ |$$  __$$\ \$$\ $$  |$$ |$$  __$$\ $$  __$$\ 
$$ |      $$ |            $$ |  $$ |$$ /  $$ | \$$$$  / $$ |$$ |  $$ |$$ /  $$ |
$$ |  $$\ $$ |            $$ |  $$ |$$ |  $$ | $$  $$<  $$ |$$ |  $$ |$$ |  $$ |
\$$$$$$  |$$$$$$$$\       $$$$$$$  |\$$$$$$  |$$  /\$$\ $$ |$$ |  $$ |\$$$$$$$ |
 \______/ \________|      \_______/  \______/ \__/  \__|\__|\__|  \__| \____$$ |
                                                                      $$\   $$ |
                                                                      \$$$$$$  |
                                                                       \______/ 
""")

def confirm_action():
    print("Вы выбрали ДоXинг по Тg.")
    print("Подтвердите действие (Y/N):")
    confirm_choice = input().strip().upper()
    if confirm_choice == "Y":
        print("Подтверждено. Открываем ссылку...")
        webbrowser.open("https://ua.xxxi.porn/video/15409")
    elif confirm_choice == "N":
        print("Действие отменено.")
    else:
        print("Неверный выбор. Попробуйте снова.")
        confirm_action()

def main_menu():
    print("Выберите действие:")
    print("1. ДоXинг по Тg")
    print("2. Dоксинг по номеру")
    choice = input().strip()
    if choice == "1":
        confirm_action()
    elif choice == "2":
        print("Вы выбрали Dоксинг по номеру.")
    else:
        print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    display_ascii_art()
    main_menu()
