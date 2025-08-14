
from math import radians


outlook = ['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy','Sunny','Overcast','Overcast','Rainy']
temp = ['hot','hot','hot','mild','cool','cool','cool','mild','cool','mild','mild','mild','hot','mild']
humd = ['high','high','high','high','normal','normal','normal','high','normal','normal','normal','high','normal','high']
windy = ['F','T','F','F','F','T','T','F','F','F','T','T','F','T']
pg = ['N','N','Y','Y','Y','N','Y','N','Y','Y','Y','Y','Y','N']

dataset = [outlook, temp, humd, windy, pg]

yesInPg = 0
noInPg = 0

for i in pg:
    if(i == "Y"):
        yesInPg = yesInPg + 1
    else:
        noInPg = noInPg + 1

yesProb = yesInPg / (yesInPg + noInPg)
noProb = noInPg / (yesInPg + noInPg)

parameter = ["Rainy", "hot", "high", "F"]

rainyInOutlookY = 0
rainyInOutlookN = 0

for i in range(0,len(outlook)):
    if(outlook[i] == "Rainy" and pg[i] == 'Y'):
        rainyInOutlookY = rainyInOutlookY + 1
    elif(outlook[i] == "Rainy" and pg[i] == 'N'):
        rainyInOutlookN = rainyInOutlookN + 1
rainyInOutlookY = rainyInOutlookY / yesInPg
rainyInOutlookN = rainyInOutlookN / noInPg

hotInTempY = 0
hotInTempN = 0

for i in range(0,len(temp)):
    if(temp[i] == "hot" and pg[i] == 'Y'):
        hotInTempY = hotInTempY + 1
    elif(temp[i] == "hot" and pg[i] == 'N'):
        hotInTempN = hotInTempN + 1
hotInTempY = hotInTempY / yesInPg
hotInTempN = hotInTempN / noInPg


highInHumdY = 0
highInHumdN = 0

for i in range(0,len(humd)):
    if(humd[i] == "high" and pg[i] == 'Y'):
        highInHumdY = highInHumdY + 1
    elif(humd[i] == "high" and pg[i] == 'N'):
        highInHumdN = highInHumdN + 1
highInHumdY = highInHumdY / yesInPg
highInHumdN = highInHumdN / noInPg


fInWindyY = 0
fInWindyN = 0

for i in range(0,len(windy)):
    if(windy[i] == "F" and pg[i] == 'Y'):
        fInWindyY = fInWindyY + 1
    elif(windy[i] == "F" and pg[i] == 'N'):
        fInWindyN = fInWindyN + 1
fInWindyY = fInWindyY / yesInPg
fInWindyN = fInWindyN / noInPg


finalYesProb = yesProb * rainyInOutlookY * hotInTempY * highInHumdY * fInWindyY
finalNoProb = noProb * rainyInOutlookN * hotInTempN * highInHumdN * fInWindyN 

if(finalYesProb > finalNoProb):
    print("Yes, probablity :- ",finalYesProb)
else:
    print("No, probablity :- ",finalNoProb)