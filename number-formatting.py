# Create a function called FormOut() which takes three parameters
#   1. Number of Integer
#   2. Prefix of String
#   3. AddComma of Boolean
# Assume number is between range 0-999999 inclusive
# If addcomma is true then the number will have seperating the number otherwise no comma will be added

def FormOut(Number: int, Prefix: str, AddComma: bool):
    after = Prefix + str(Number)
    result = after
    if AddComma == True:
        length = len(after)
        n = length - 3
        result = after[0:n] + ',' + after[n:length]
    print(result)


FormOut(100000, "$", True)

