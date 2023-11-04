
gbl_num = 100  #Global variable that can be used in any function below. 

def base_fctn(a, b):
    int_2 = a   #int_2, int_3, and total can be called in this  
    int_3 = b   #function and any functions that are nested within it .
    total = int_2 + int_3

    def inner_fctn_2():
        int_4 = total
        double = int_4 * 2
        print ("Total =", total)
        print("Double total =", double)
        
        def inner_fctn_3():
            print("Here is the global number: ", gbl_num)
        inner_fctn_3()
    
    inner_fctn_2()

def base_fctn_2():
    print("In this fucntion, only the global variable is available to be called.")
    print("Global number times two is: ", (2*gbl_num))
  
base_fctn(45, 20)
base_fctn_2()
