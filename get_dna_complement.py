import string
def get_2_before(x):
    abcs = string.ascii_lowercase
    new_sent = ""
    for letter in x:

        if letter in abcs and letter not in ('y','z'):
            new_sent += abcs[abcs.index(letter)+2]
        elif letter == 'y':
            new_sent += 'a'
        elif letter == 'z':
            new_sent += 'b'
        else:
            new_sent += letter
            
    return new_sent

x = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print(get_2_before("pc/def/map.html"))