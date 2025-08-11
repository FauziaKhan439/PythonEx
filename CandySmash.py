def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.

     to_smash(91)
    1
    """
    if total_candies < 2:
        # print("Splitting", total_candies, "candy")
        print("Splitting 1 candy")
        return total_candies % 3
    else:
        print("Splitting", total_candies, "candies")
        return total_candies % 3


to_smash(91)
to_smash(1)

#when called with print, returned value will be shown as well
print ("calling in print")
print(to_smash(91))
print(to_smash(5))


#git remote set-url origin https://github.com/YourUsername/NewRepo.git   change remote repo ur local git project is connected to
#git remote set-url origin https://github.com/YourUsername/NewRepo.git
#  check current remote git remote -v

