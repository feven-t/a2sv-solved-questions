class Solution:
    def reverseParentheses(self, s: str) -> str:
        ans=""
        st =[]
        for i in s:
            if i!=")" :
                st.append(i)
            else:
                ans=""
                while st[-1] != "(":
                    ans+=st.pop()
                st.pop()
                for k in ans:
                    st.append(k)
        return ''.join(st)
