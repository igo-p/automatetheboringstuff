import re
def imitate_strip(str,chars=' '):
    if chars == ' ':
        pattern = r'^\s+|\s+$'
        return re.sub(pattern,'',str)
    else:
        return re.sub(chars,'',str)
print(imitate_strip('      m      on','o'))