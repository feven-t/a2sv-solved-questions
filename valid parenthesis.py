class Solution:
    def isValid(self, s: str) -> bool:
        temp=[]
        for sym in s:
            if sym in "([{":
                temp.append(sym)
            elif len(temp)>0:
                if sym=="]" and temp[-1] == "[" :
                    temp.pop()
                elif sym=="}" and temp[-1] == "{" :
                    temp.pop()
                elif sym==")" and temp[-1] == "(" :
                    temp.pop()
                else:
                    return False
            else:
                return False
        return True if len(temp)==0 else False
