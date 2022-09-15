
def main():
    problem_one = "5*10"
    print(problem_one)
    user_input = input()
    response_one = ("Correct!")
    def new_func():
        print(response_one)
    if user_input == "50":
        new_func()
    if user_input != "50":
        print("Incorrect, press enter to try again.")
        input()
        main()
main()    