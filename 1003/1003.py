# coding:utf-8
import re


def match(string):
    # only P、A、T
    if not onlyPAT(string):
        # print "not only PAT"
        return False

    # xPATx is currect
    if xPATx(string):
        return True
    else:
        # print "original string is not xPATx"
        return subRecur(string)

def onlyPAT(string):
    m = re.match(r'^[PAT]+$', string)
    if m:
        return True
    else:
        return False

def xPATx(string):
    m = re.match(r'^A*PATA*$', string)
    if m:
        left, right = re.search('PAT', string).span(0)
        if string[:left] == string[right:]:
            return True
        else:
            # print "not xPATx"
            return False
    else:
        # print "not xPATx"
        return False

def subRecur(string):
    m = re.match(r'^A*PA+TA*$', string)
    if not m: return False

    left, right = re.search(r'PA+T', string).span(0)
    newStr = string[:right - 2] + string[right - 1:len(string) - left]
    if xPATx(newStr):
        return True
    else:
        # print "new recur..."
        return subRecur(newStr)

# print "please enter the number of strings: "
count = input()
resultList = []
for x in range(0,count):
    # print "enter string you want to check: "
    string = raw_input()
    resultList.insert(0, match(string))

while resultList:
    if resultList.pop():
        print "YES"
    else:
        print "NO"