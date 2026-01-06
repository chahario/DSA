# Maximize the confusion of an Exam.


class solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        start = 0
        best = 0
        fcount = 0
        tcount = 0
        for end in range(len(answerKey)):
            if answerKey[end] == 'T':
                tcount +=1
            else:
                fcount +=1
            while min(fcount,tcount) > k:
                if answerKey[start] == 'T':
                    tcount-=1
                else:
                    fcount-=1
                start +=1
            best = max(best, end-start+1)
        return best


