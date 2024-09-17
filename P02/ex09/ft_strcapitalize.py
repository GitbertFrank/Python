def ft_strcapitalize(str):
    iscapital = False
    newstr = ''
    for i in str:
        if ('A' <= i <= 'Z' or '0' <= i <= '9') and iscapital == False:
            iscapital = True
            newstr += i
        elif 'a' <= i <= 'z' and iscapital == False:
            i = chr(ord(i) - 32)
            newstr += i
            iscapital = True
        elif 'A' <= i <= 'Z' and iscapital == True:
            i = chr(ord(i) + 32)
            newstr += i
        elif i.isspace() or not ('A' <= i <= 'Z' or '0' <= i <= '9' or 'a' <= i <= 'z'):
            iscapital = False
            newstr += i
        else:
            newstr += i
    return newstr

print(ft_strcapitalize("helllooo Niger niger JAWDUAWDUIhi 42Mooawedoawod"))

# Salut, Comment Tu Vas ? 42mots Quarante-Deux; Cinquante+Et+Un