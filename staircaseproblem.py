def staircase(n):
    for i in range(1, n+1): # start with one until n inclusive. inclusive meaning sources: https://stackoverflow.com/questions/39010041/what-is-the-meaning-of-exclusive-and-inclusive-when-describing-number-ranges#:~:text=In%20simple%20terms%2C%20inclusive%20means,and%20without%20the%20number%20n%20.
        stair = "#" * i
        print(stair.rjust(n)) # little python awesomeness justified right 


staircase(7)

"""
      #
     ##        
    ###        
   ####        
  #####        
 ######        
#######        
"""
            