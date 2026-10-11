class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        currTime = 0
        totalWaitingTime = 0

        for arrivalTime, prepTime in customers:
            if arrivalTime > currTime:
                currTime = arrivalTime + prepTime
            else:
                currTime += prepTime

            customerWaitingTime = currTime - arrivalTime
            totalWaitingTime += customerWaitingTime

        return totalWaitingTime/len(customers)

