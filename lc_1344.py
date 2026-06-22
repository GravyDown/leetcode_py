class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        a=30*hour
        b=5.5*minutes
    
        angle=abs(a-b)

        if angle>180:
            return 360-angle
        
        return angle
