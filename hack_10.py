"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = list("fooziman".upper().replace('O', '0').replace('I', '1').replace('A', '@'))
    return result  