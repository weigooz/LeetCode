#Anagram

def anagram(s1, s2):
    match_anagram = True
    s1 = s1.strip(' ')
    s2 = s2.strip(' ')
    tmp = {}
    
    for s in s1:
        if s in tmp:
            tmp[s] += 1
        else:
            tmp.update({s:0})

    for i in s2:
        if i in tmp:
            tmp[i] -= 1
        else:
            match_anagram = False
            
    return match_anagram
