# remember to fork this and push to github

# f = open("test.txt","r")
# print(f.readlines())
# f.close()

# with open('test.txt','r') as f:
#   f_contents = f.readlines()
#   print(f_contents, end='')

# employee_file = open("employees.txt",'r')
# for employee in employee_file.readlines():
#   print(employee)
# employee_file.close()

# employee_file = open("employees.txt",'a')
# employee_file.write("\nKelly- Customer Service")
# employee_file.close()

# with open('readme.txt','w') as f:
#   f.write('readme')

# # this overwrites the original content
# with open('readme.txt','w') as f:
#   f.write('I dont care')

# # this appends to the original content
# with open('readme.txt','a') as f:
#   f.write('I dont care I dont care I dont care I dont care')

user = input("Say something: ")
with open('userinput.txt',"a") as f:
  f.write(user)
