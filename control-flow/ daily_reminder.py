user_task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        pass
    case "medium":
        pass
    case "low":
        pass
    

if time_bound == "yes":
    print(f"\'{user_task}\' is a {priority} priority task that requires immediate attention today!")
elif time_bound == "no":
    print(f"\'{user_task}\' is a {priority} priority task. Consider completing it when you have free time.")

