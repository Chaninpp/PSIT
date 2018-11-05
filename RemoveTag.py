''' RemoveTag '''
def main(cha):
    ''' for
    Ex. <h1>Title</h1><p>This is a          <a href="http://judge.it.kmitl.ac.th">link</a>.<p><br />
        ['Title','This','is','a','link','.']
    Ex. <table cellpadding='3'>       <tr><td>Hello</td><td>World!</td></tr></table><br />
        ['Hello','World!']
    Ex. <hello>       <goodbye>
        []
    Ex. This is plain text.
        ['This', 'is', 'plain', 'text.']
    '''
    cha_2, check, lis = '', '', []
    for i in cha:
        if i == '>':
            check = i
        if i == '<':
            check = i
            if cha_2 != '':
                cha_2 = cha_2.strip()
                cha_2 = cha_2.split()
                if len(cha_2) > 1:
                    for j in range(len(cha_2)):
                        lis.append(cha_2[j])
                elif cha_2 != []:
                    lis.append(*cha_2)
        if check == '>':
            cha_2 += i if i != '>' and i != '<' else ''
        elif check == '<':
            cha_2 = ''
    if '<' not in cha and '>' not in cha:
        lis = cha.split()
    print(lis)

main(input())
