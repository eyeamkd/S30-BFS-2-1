"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        importanceMap = {}

        for emp in employees:
            importanceMap[emp.id]= (emp.importance, emp.subordinates)
        
        visited = set()

        queue = deque()
        res = importanceMap[id][0]

        for sub in importanceMap[id][1]:
            queue.append(sub)

        while queue:
            sub = queue.popleft()
            if sub not in visited:
                visited.add(sub)
                res+=importanceMap[sub][0]
                for child in importanceMap[sub][1]:
                    queue.append(child)
        
        return res
               

