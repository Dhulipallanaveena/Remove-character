from sys import stdin


def removeAllOccurrencesOfChar(string, ch) :
    counts=string.count(ch)
    string=list(string)
    while counts:
        string.remove(ch)
        counts=counts-1
    string="".join(string)
    return string
   
    
    
	# Your code goes here




























	

#main
string = stdin.readline().strip()
ch = stdin.readline().strip()[0]

ans = removeAllOccurrencesOfChar(string, ch)

print(ans)
