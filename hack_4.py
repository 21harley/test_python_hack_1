"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    pos=len(result)-1
    result=result[:pos]+result[pos].upper()
    return result