def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Bobby')

# define variable
input1 = -1

# get input integer from user and check to make sure only numbers else keep prompting user till enter a integer
while input != int:
    input1 = input("Input first integer")
    if input1.isalpha():
        print("Please enter a number")
    if str.isdigit(input1):
        break

input2 = -1

while input != int:
    input2 = input("Input second integer")
    if input2.isalpha():
        print("Please enter a number")
    if str.isdigit(input2):
        break

# define variable that stores and adds two different integers that were input from user
sum_two_ints = int(input1) + int(input2)

# print result of sum of two input integers from user
print(f"The sum of two integers is {sum_two_ints}")
