def oxford_comma(items):
    l = len(items)
    if l == 1:
        return items[0]
    elif l == 2:
        return items[0] + ' and ' + items[1]
    else:
        phrase = ''
        for x in range(l - 1):
            phrase += items[x] + ', '
        phrase += 'and ' + items[l-1]
        return phrase
    
