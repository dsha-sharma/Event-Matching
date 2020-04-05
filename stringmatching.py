import jellyfish as jf
from fuzzywuzzy import fuzz

def string_match(x,y):
    
    # converts the string into unicode
    x = x.decode('utf-8')
    y = y.decode('utf-8')

    # makes the metaphones of the words
    xp = jf.metaphone(x)
    yp = jf.metaphone(y)
    
    # compares the metaphones of the words
    if xp == yp:
        return True
    
    return False

def metaphone(x):

    x = x.decode('utf-8')

    xp = jf.metaphone(x)

    return xp

def make_fuzz_match(x,y):

    tsr = fuzz.token_sort_ratio(x,y)
    tsetr = fuzz.token_set_ratio(x,y)
    pr = fuzz.partial_ratio(x,y)

    ans = float(tsr+tsetr+pr)/3.0
    return ans


