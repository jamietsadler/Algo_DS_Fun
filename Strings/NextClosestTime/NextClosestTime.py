
class Solution:
    def nextClosestTime(self, time: str) -> str:
        hour, minute = time.split(":")
        
        # Generate all possible 2 digit values
        # There are at most 16 sorted values here
        nums = sorted(set(hour + minute))
        combos = [a + b for a in nums for b in nums]
        
        idx = combos.index(minute)
        if idx + 1 < len(combos) and int(combos[idx+1]) < 60:
            return hour + ":" + combos[idx+1]
        idx = combos.index(hour)
        if idx + 1 < len(combos) and int(combos[idx+1]) < 24:
            return combos[idx+1] + ":" + combos[0]
        else:
            return combos[0] + ":" + combos[0]