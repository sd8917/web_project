dict={}
while True:
    print("----- Birthday App -------")
    print("1.Show Birthday")
    print("2.Add to Birtday List ")
    print("3.Exit")
    choice = int(input("Enter the choice "))

    if choice == 1:
        '''cheching whether dictionary contain any value or not '''
        if len(dict.keys()) == 0:
            print("Nothing to Show ")

            '''if there is any keys-value pair then check for birthday by entering the name '''
        else:
            name = input("Enter name to look for birthday ")
            birthday =dict.get(name,"No Data found ")
            print(birthday)

            '''now adding the birthday to dict in keys and values pair by entering the name &
            birtday by using input() function '''

    elif choice == 2:
        name = input("Enter Friend's birthday ")
        date=input("Enter  Birthdate : ")
        dict[name]=date
        print("Birthday Added")

        '''since it is inifinte loop it need to stop the loop 
        by using the suitable condition here we give the choice 3 to {break}'''
    elif choice == 3:
        break
    else:
        print("Choose a Valid Option")

