# None is the return value of of functions without a return value
# None is an Object, a constant and a singleton. 
# Singleton is a creational design pattern, which ensures that only one object of its kind exists and provides a single point of access to it for any other code. 
# Singleton has almost the same pros and cons as global variables. 
# Although they're super-handy, they break the modularity of your code.
# THIS IS VERY IMPORTANT All variables with a None value point to the same instance of the None, CHECK for None with is instead of ==. AGAIN!!! READ THIS LAST ONE AND EMBRACE IT!! 


value = "testing for value"
print(value)
value = None

if value is not None:
    print(value)# this is not going to execute becuase the value is set to None and we are testing to see if there is something 
                # if the value is not the object None then print the value, it is not going to going to print becuase right now the value is pointing to None

if value is None: # here it prints becuase the value is pointing to None.
    print(value)