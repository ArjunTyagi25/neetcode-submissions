class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]

        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_to_account = {}  # email -> index of account
        
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in email_to_account:
                    uf.union(i, email_to_account[e])  # This email was seen before in a different account so we union them together
                else:
                    email_to_account[e] = i  # Add a new email to that account's index

        emailGroup = defaultdict(list)      # index of account -> list of emails
        for e, i in email_to_account.items():
            account = uf.find(i)    # Find the root account for the email
            emailGroup[account].append(e)   # For the root account, append the email

        res = []
        for accIndex, emails in emailGroup.items():
            name = accounts[accIndex][0]
            res.append([name] + sorted(emails))

        return res
