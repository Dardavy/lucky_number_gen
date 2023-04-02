# called in a function for this script
# customised the function with yuor name
# programmed your script to collect your user imput
# the application should populate the result of your username, user input, and manchine number(win or loose)


import random
 
 

  # This is used in calling in my function
def dardanells_lott_gen():

    #  # initialise an empty list that will be used to store the lucky number!
    lottery_numbers = []
    for i in range(0,1):
       nunber = random.randint(0, 50)
    while number in lottery_numbers:
        number =random.randint(0, 50)

    #     # now we have a unique number, let's append it to our list.
    #     lottery_numbers.append(number)
    #  # sort the list in ascending order
    #  lottery_numbers.sort()

    user_number = []
    for i in range(0,1):
         user_name = input(">>> Please Enter Your Name: ")
         number = int(input(">>> Please Enter Your Number: "))
         while (number in user_number or number>50):
             print("Invalid number, Please try again.")
             number = int(input(">>> Please Enter Your Number: "))
         user_number.append(number) 
         

            


 # here to Generate a user's name and input number
 #     user_name = input(">>> Please Enter Your Name: ")
  #     user_number = int(input(">>> Please Enter Your Number: ")) 
 #    print(user_name)
 #     system_winning_num = 30
 # # Here to generate the lottery random number
 # for i in range(0, 1):
 #     rand_num = random.randint(0, 50)
 #     #check if this number has already been picked and
 #      # print(rand_num)
     
 #     # for x in (0, 50):
 #     #     print(x)
 #     #     if user_number == rand_num:
 #     #      print("Congratulation,You win the lottery", user_name)


dardanells_lott_gen()    