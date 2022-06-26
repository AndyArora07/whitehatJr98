def switch_file_data():
    name_1= input("Enter file one name: ")
    name_2= input("Enter file two name: ")
    #-------------------------------------
    with open(name_1,"r") as a:
        data_a = a.read()
    with open(name_2,"r") as b:
        data_b = b.read()
    #-------------------------------------
    with open(name_1,"w") as a:
        a.write(data_b)
    with open(name_2,"w") as b:
        b.write(data_a)
    
switch_file_data()
