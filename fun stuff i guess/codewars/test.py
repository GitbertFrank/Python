def to_camel_case(text):
    string = ''
    i = 0
    while i < len(text)- 1:
        if text[i] == '-' or text[i] == '_':
            i += 1
            string += text[i].upper() 
            i += 1
        else:string += text[i]
    return string

print(to_camel_case("the_black_killer"))