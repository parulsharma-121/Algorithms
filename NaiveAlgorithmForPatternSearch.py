'''
Naive Search Algorithm For Pattern Searching.
'''
def naiveSearch(pattern, text):
    m = len(pattern)
    n = len(text)
    for i in range(n-m+1):
        j = 0
        while(j<m):
            if(text[i+j]!=pattern[j]):
                break
            j += 1

        if(j==m):
            print("Pattern found at index ", i)
text = "AABAACAADAABAAABAA"
pattern = "AABA"
naiveSearch(pattern, text)
