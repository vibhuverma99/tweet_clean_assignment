'''
tweet_clean.py - script to clean tweets
Author - Vibhu Verma
'''
import re
str = '@Rohan,I\'m lesving BITS today !! :] #freedom myNameIsRohan'
emojies = [':‑)', ':)', ':-]', ':]', ':-3', ':3', ':->', ':>', '8-)', '8)', ':-}', ':}', ':o)', ':c)', ':^)', ':‑D', ':D', '8‑D', '8D', 'x‑D', 'xD', 'X‑D',
           'XD', ':-))', ':‑(', ':(', ':‑c', ':c', ':‑<', ':<', ':‑[', ':[', ':-||', '>:[', ':‑O', ':O', ':‑o', ':o', ':-0', '8‑0', ':×', ';‑)', ';)', ';]', ';D', ':‑P', ':P', 'X‑P', 'XP', 'x‑p', 'xp', ':‑p']  # source : wikipedia.org


class tweet:

    def __init__(self, twt):
        self.original = twt
        self.copy = twt

    def replaceMentions(self):
        pattern = re.compile(r'@\w+')  # defining patterns of type @John
        matches = pattern.finditer(self.copy)
        for match in matches:
            substr = match.group(0)[1:]  # removing '@' from @John
            sub_pattern = re.compile(substr)
            self.copy = re.sub(sub_pattern, '__NAME__', self.copy)  # substitute the name John everywhere in sentence

        self.copy = re.sub(pattern, '__NAME__', self.copy)  # substitute @John mentions

    def removeHastags(self):
        pattern = re.compile(r'#\w*')
        matches = pattern.finditer(self.copy)
        for match in matches:
            substr = match.group(0)[1:]  # removing '#' from findings
            sub_pattern = re.compile(match.group(0))
            self.copy = re.sub(sub_pattern, substr, self.copy)  # substitute #ABC to ABC

    def removeEmoji(self):
        type1 = re.compile(r'[:8x;%][-o][\)\(\[\}\]DCc<0]')  # emojies of type <eyes><nose><mouth> eg :-)
        type2 = re.compile(r'[:8x;=%][\)\(\[\}\]DCc<0P]')  # emojies of type <eyes><mouth> eg :)
        self.copy = re.sub(type1, '', self.copy)
        self.copy = re.sub(type2, '', self.copy)

    def separateWords(self):
        pattern = re.compile(r'[a-z][A-Z]')  # find occourance of camel case eg: myNameIs
        matches = pattern.finditer(self.copy)
        for match in matches:
            substr = match.group(0)
            substr = substr[0] + ' ' + substr[1]
            sub_pattern = re.compile(match.group(0))
            self.copy = re.sub(sub_pattern, substr, self.copy)


fin = open('jan9-2012.txt', 'r')        # <edit here> the name of input files with tweets
fout = open('output.txt', 'w')          # <edit here> the name of output files with tweets
for line in fin:
    tweet1 = tweet(line)
    tweet1.separateWords()
    tweet1.replaceMentions()
    tweet1.removeHastags()
    tweet1.removeEmoji()
    fout.write(tweet1.copy)
'''
tweet1 = tweet(str)
tweet1.separateWords()
tweet1.replaceMentions()
tweet1.removeHastags()
tweet1.removeEmoji()
fout.write(tweet1.copy)
'''
fin.close()
fout.close()
