import random
list=["shahrukh khan","salman khan","hritik roshan","amir khan","ajay devagan"]
random_choice = random.randint(0,len(list))
name =  input("Enter your name : ")
print(name ,"looks like " ,list[random_choice])