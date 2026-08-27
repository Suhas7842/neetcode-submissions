class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for num in asteroids:
            while stack and stack[-1] > 0 and num < 0:
                if abs(stack[-1])>abs(num):
                    break
                elif abs(stack[-1])==abs(num):
                    stack.pop()
                    break
                else:
                    stack.pop()
            else:
                stack.append(num)
        return stack