def isPal(x):
    """ Assumes x is a list
        Returns True if the list is a panlindrome"""
    temp = x[:]
    temp.reverse()
    if temp == x:
        return True
    else:
        return False

def silly(n):
    """ Assumes n is an int > 0
        Gets n inputs from user
        Prints 'Yes' if the sequence of input forms a palindrome;
            'No' otherwise"""
    result =[]
    for i in range(n):
        elem = raw_input('Enter element: ')
        result.append(elem)
    if isPal(result):
        print 'Yes'
    else:
        print 'No'
