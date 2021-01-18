#You are in charge of the cake for a child's birthday. 
# You have decided the cake will have one candle for each year of their total age. 
# They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

def birthdayCakeCandles(candles):               # this is why I love Python " pass the array"
    return candles.count(max(candles))          # use the built in function to go from the inside out. first get the max and then use the count function to get the number of max elements

candles_in_the_bag_for_the_party = [1,2,2,3,4,2,4] # make the candle list
print(birthdayCakeCandles(candles_in_the_bag_for_the_party)) # pass the list to the function. 