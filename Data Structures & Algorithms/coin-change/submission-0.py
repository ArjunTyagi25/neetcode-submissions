class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque()
        q.append(0)
        visited_sums = set()

        coin_count = 0
        while q:
            for i in range(len(q)):
                curr_sum = q.popleft()

                if curr_sum == amount:
                    return coin_count

                for coin in coins:
                    next_sum = curr_sum + coin

                    if next_sum > amount or next_sum in visited_sums:
                        continue
                    
                    visited_sums.add(next_sum)
                    q.append(next_sum)
            
            coin_count += 1

        return -1

    

        