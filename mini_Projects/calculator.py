HISTORY_FILE = "mini_Projects/history.txt"

def show_history():
    file = open(HISTORY_FILE,'r')
    Lines = file.readlines()

    if len(Lines) == 0:
        print(" no history found")
    else:
        for line in reversed(Lines):
            print(line.strip())

    file.close()

def clear_file():
    file = open(HISTORY_FILE,'w')
    file.close()

    print("history cleared")


def save_to_history(equation, result):
    file = open(HISTORY_FILE,'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()

    if(len(parts) != 3):
        print("Invalid input")
        return
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])
    result = 0
    
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2

    elif op == "*":
        result = num1 * num2
    
    elif op == "/":
        if num2 == 0:
            print("denominator can't be  zero (0)")
            return
        result = num1 / num2
    else:

        print("invalid operators use only (+,-,*,/)")

    print(f"result is : {result}")
    save_to_history(user_input,result)

def main():
    print("-------SIMPLE CALCULATOR WITH HISTORY------(type history , clear, or exit )")
    
    while True:
       
        user_input = input("enter operations (+,-,*,/) or command (clear,exit,history)")
        if user_input == "exit":
           print("ok....Bye")
           break
        elif user_input == "clear":
           clear_file()
        elif user_input == "history":
           show_history()
        else:
           calculate(user_input)
            
main()