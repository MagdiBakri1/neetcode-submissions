class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack=[]
        cars=[]
        for i in range(0,len(position)):
            cars.append([position[i],speed[i]])
            
        cars.sort(key=lambda position: position[0], reverse=True)

        for i in range(0,len(cars)) :
                if not stack:
                    stack.append(cars[i])
                else:
                    T=(target-cars[i][0])/cars[i][1]
                    T2=(target-stack[-1][0])/stack[-1][1]
                    if T>T2:
                        stack.append(cars[i])
                    else:
                        continue

        return int(len(stack))

