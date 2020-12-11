pol2ipa = {
    "t\^s\'": ["t͡ɕ",1],
    "d\^z\'": ["d͡ʑ",1],
    "t\^s":  ["t͡s",1],
    "d\^z":  ["d͡z",1],
    "t\^S":  ["t͡ʃ",1],
    "d\^Z":  ["d͡ʒ",1],
    "s\'":   ["ɕ",1],
    "z\'":   ["ʑ",1],
    "n\'":   ["ɲ",1],
    "w~":   ["w̃",1],
    "j~":   ["j̃",1],
    "N":    ["ŋ",1],
    "l":    ["l",1],
    "r":    ["r",1],
    "w":    ["w",1],
    "j":    ["j",1],
    "m":    ["m",1],
    "n":    ["n",1],
    "p":    ["p",1],
    "b":    ["b",1],
    "t":    ["t",1],
    "d":    ["d",1],
    "k":    ["k",1],
    "g":    ["g",1],
    "h":    ["x",1],
    "c":    ["c",1],
    "J":    ["ɟ",1],
    "f":    ["f",1],
    "v":    ["v",1],
    "s":    ["s",1],
    "z":    ["z",1],
    "S":    ["ʃ",1],
    "Z":    ["ʒ",1],
    "Z,":   ["ʒ",1],
    "x":    ["x",1],
    "e~j~": ["εj̃",0],
    "o~j~": ["ɔj̃",0],
    "o~w~": ["ɔw̃",0],
    "e~w~": ["ew̃",0],
    "i~w~": ["iw̃",0],
    "a~w~": ["ɑw̃",0],
    "y~w~": ["ɨw̃",0],
    "u~w~": ["uw̃",0],
    "i":    ["i",0],
    "y":    ["ɨ",0],
    "e":    ["ε",0],
    "a":    ["a",0],
    "o":    ["ɔ",0],
    "u":    ["u",0],
    " ":    [" ",0]
    
}
dic = {
    'abażur': 'a b a Z u r',
    'abażura': 'a b a Z u r a',
    'abażurach': 'a b a Z u r a h',
    'abażurami': 'a b a Z u r a m i',
    'abażurek': 'a b a Z u r e k',
    'abażurem': 'a b a Z u r e m',
    'abażurka': 'a b a Z u r k a',
    'abażurkach': 'a b a Z u r k a h',
    'abażurkami': 'a b a Z u r k a m i',
    'abażurki': 'a b a Z u r k i',
    'abażurkiem': 'a b a Z u r k j e m',
    'abażurkom': 'a b a Z u r k o m',
    'abażurkowi': 'a b a Z u r k o v i',
    'abażurków': 'a b a Z u r k u f',
    'abażurku': 'a b a Z u r k u',
    'abażurom': 'a b a Z u r o m',
    'abażurowi': 'a b a Z u r o v i',
    'abażurów': 'a b a Z u r u f',
    'abażuru': 'a b a Z u r u',
    'abażury': 'a b a Z u r y',
    'abażurze': 'a b a Z u Z e'
}

#solution
cons = vows = 0
for key, value in dic.items():
    for x in value:
        print(pol2ipa[x][0],end='')
        if(pol2ipa[x][1] == 1):
            cons += 1
        else:
            vows += 1
    print()
print('In dic, there are', cons, 'consonants and', vows, 'vowels, therefore consonants constitute', 
      str(round((cons/(cons+vows))*100, 2)) + '% of all phonemes in dic.')