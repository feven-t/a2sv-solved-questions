class Solution():
    def sortSentence(self, s:str) -> str:
        
        k = s.split(" ")
        s2 = [0] * len(k)
        s3 = []
        for i in range(0, len(k), 1):
            l = int(k[i][-1]) - 1
            s2[l] = k[i]
        for i in range(0, len(s2)):
            s3.append(s2[i].replace(s2[i][-1], ""))
        s4 = ' '.join(s3)
        return (s4)
