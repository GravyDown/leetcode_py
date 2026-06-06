class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        i=0
        while i <len(asteroids):
            if i==len(asteroids)-1 and mass>=asteroids[i]:
                return True
            if mass>=asteroids[i]:
                mass+=asteroids[i]
                i+=1
            else:
                return False
        
