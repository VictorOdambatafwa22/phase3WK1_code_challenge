def two_positive_numbers(a,b,c):
    if a>0 and b>0 and c<0:
       return True
    elif a<0 and b>0 and c>0:
       return True
    elif a>0 and b<0 and c>0:
       return True
    else:
       return False


two_positive_numbers(-5,4,-3)

