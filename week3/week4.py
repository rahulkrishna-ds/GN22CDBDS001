import re
def processing(ans):
    answer = []
    for ele in ans:
        answer.append(ele[1:-1])
    return answer

def voweland3letters(s):
    s = '|'+'||'.join(s.split(' '))+'|'
    pattern = '\|[aeiouAEIOU][a-z][a-z][a-z]\|'


    ans = re.findall(pattern,s)
    return processing(ans)

def currency(s):
    return re.findall(r"[\$\u20AC\u00A3\u20B9]{1}[0-9]+",s,re.UNICODE)

def orders(s):
    s = '|'+'||'.join(s.split(' '))+'|'
    pattern = '(\|1st\||\|2nd\||\|3rd\||\|[0-9]+[t][h]\||\|[a-zA-Z]*[t][h]\|)'
    return processing(re.findall(pattern, s))

def datefind(s):
    s = '|'+'||'.join(s.split(' '))+'|'
    dmy = '\|[0-3][0-9]/[0-1][0-9]/[1-2][0-9][0-9][0-9]\|'
    mdy = '\|[0-1][0-9]/[0-3][0-9]/[1-2][0-9][0-9][0-9]\|'
    dmy2 = '\|[0-3][0-9]/[0-1][0-9]/[0-9][0-9]\|'
    mdy2 = '\|[0-1][0-9]/[0-3][0-9]/[0-9][0-9]\|'
    pattern = dmy+'|'+mdy+'|'+dmy2+'|'+mdy2
    return processing(re.findall(pattern,s))


filename = input('Enter file name')
fp = open(filename, 'r')
text = ''
for line in fp:
    text += line[:-1]+' '
text = text.replace(',',' ')
text = text.replace('.',' ')
print(text)
print('word of length 4 and starts with a vowel :',*voweland3letters(text))
print('currencies :' ,*currency(text))
print('orders :',*orders(text))
print('dates',*datefind(text))
