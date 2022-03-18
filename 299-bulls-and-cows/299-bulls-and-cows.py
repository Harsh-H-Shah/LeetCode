class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret, guess = list(secret), list(guess)

        l = len(secret)
        a = 0

        for i in range(0, l):
            if secret[i]==guess[i]:
                secret[i]="#"
                guess[i]="#"
                a+=1
        b = 0

        secret = collections.Counter(secret)

        for i in range(0, l):
            if guess[i]!="#":
                if guess[i] in secret and secret[guess[i]]>0:
                    secret[guess[i]]-=1
                    b+=1

        return str(a)+"A"+str(b)+"B"
        