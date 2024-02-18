# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
postion_list = [int(digit) for digit in position]

# this does what ^ this does in a more simple way
# test = input("Give me numebr")
# num1 = int(test[0])
# num2 = int(test[1])
# print(num1)
# print(num2)

num1 = postion_list[0]
num2 = postion_list[1]

map[num2 - 1][num1 - 1] = 'X'



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")