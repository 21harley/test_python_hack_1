"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    cont=5
    while cont!=-1:
        result.append(cont)
        cont-=1
    return  result
