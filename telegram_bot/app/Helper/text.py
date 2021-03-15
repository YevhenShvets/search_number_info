

def number_with_character(text):
    result = ""
    for val in text:
        if val in "+()-_|\\/';:=":
            result += '\\' + val
        else:
            result += val
    return result
