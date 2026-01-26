def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('User')

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

input3 = -1

while input != int:
    input3 = input("Input third integer")
    if input3.isalpha():
        print("Please enter a number")
    if str.isdigit(input3):
        break

if input1 > input2 and input1 > input3:
    print({"input 1 is the largest of 3", input1})
if input2 > input3 and input2 > input1:
    print({"input 2 is the largest of 3", input2})
if input3 > input1 and input3 > input2:
    print({"input 3 is the largest of 3", input3})
if input3 > input1 and input3 == input2:
    print({"input 3 and input 2 are the largest of 3", input3})
if input3 > input2 and input3 == input1:
    print({"input 3 and input 1 are the largest of 3", input3})
if input3 == input1 and input3 == input2:
    print({"input 3 and input 2 and input 1 are the largest of 3", input3})
if input1 == input2 and input1 > input3:
    print({"input 1 and input 2 are the largest of 3", input3})
