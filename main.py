import time

# DEFAULT BREAK FUNCTION
def default_break():
    minutes = 5

    total_seconds = minutes * 60

    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        print(timer_display, end='\r')
        time.sleep(1)
        total_seconds -= 1

# CUSTOM BREAK FUNCTION
def custom_break(minutes):
    total_seconds = minutes * 60

    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        print(timer_display, end='\r')
        time.sleep(1)
        total_seconds -= 1

# DEFAULT FOCUS TIMER MODE
def default_focus_timer():
    minutes = 25
    total_seconds = minutes * 60

    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        print(timer_display, end='\r')
        time.sleep(1)
        total_seconds -= 1

    if total_seconds <= 0:
        choice = input("Session Completed! Nice work! Would you like to begin your break? y/n \n")
        choice = choice.lower()
        if choice == "y":
            break_type = input("Would you like to take the default break duration of 5 mins? y/n \n")
            if break_type == "y":
                default_break()
                minutes = int(input("How long do you want your break to last? (use whole numbers please!)\n"))
                custom_break(minutes)
            elif break_type == "n":
                default_break()
        elif choice == "n":
            main_menu()
        else: 
            print("Input does not match options given.")
            main_menu()

# CUSTOM FOCUS TIMER MODE
def custom_focus_timer(minutes):
    total_seconds = minutes * 60

    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        print(timer_display, end='\r')
        time.sleep(1)
        total_seconds -= 1

    if total_seconds <= 0:
        choice = input("Session Completed! Nice work! Would you like to begin your break? y/n \n")
        choice = choice.lower()
        if choice == "y":
            break_type = input("Would you like to take the default break duration of 5 mins? y/n \n")
            if break_type == "y":
                default_break()
                minutes = int(input("How long do you want your break to last? (use whole numbers please!)\n"))
                custom_break(minutes)
            elif break_type == "n":
                default_break()
        elif choice == "n":
            main_menu()
        else: 
            print("Input does not match options given.")
            main_menu()

# MAIN MENU OPTIONS / MAIN CONTROL FLOW AND CONDITIONALS
def main_menu():
    main_menu_query = int(input("What will you like to do: \n1. Run Default Focus Session \n2. Run Custom Focus Session \n3. Take a break? \n4. Quit Program\n\n"))

    if main_menu_query == 1:
        default_focus_timer()
    elif main_menu_query == 2:
        minutes = int(input("How long would you like your session to last? (Please use whole numbers) \n"))
        custom_focus_timer(minutes)
    elif main_menu_query == 3:
        minutes = int(input("How long would you like your break to last? (Please use whole numbers) \n"))
        custom_break(minutes)
    else: 
        print("Unprocessable input, returning to main menu. ")
        main_menu()

main_menu()