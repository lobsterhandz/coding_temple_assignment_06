# just for fun:
def standard():
    print("Standard Countdown:")
    for i in range(5, 2, -1):
        print(i)

def anotherway():
    print("Lambda Countdown:")
    countdown = map(lambda x: print(x), range(5, 2, -1))
    list(countdown)
standard()
user_choice = input("See another way? (yes/no): ").lower()

if user_choice == "yes":
    anotherway()