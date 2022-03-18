class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = 0
        B = 0
        secret = [char for char in secret]
        guess = [char for char in guess]
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                A+=1
                secret[i] = '*'
                guess[i] = '@'
        for i in range(len(guess)):
            if guess[i] in secret:
                B+=1
                for j in range(len(secret)):
                    if guess[i]==secret[j]:
                        secret[j] = '*'
                        break
        print(secret)
        print(guess)
        return(str(A)+"A"+str(B)+"B")
                
        