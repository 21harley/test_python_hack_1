"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    i=1
    j=0
    while i<4:
     result.insert(i+j, '@')
     i+=1
     j+=1
    return result  
