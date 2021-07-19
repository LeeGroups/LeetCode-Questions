from collections import defaultdict

def accountsMerge(accounts):
    stuff = {}
    for i in range(len(accounts)):
        name = accounts[i][0]
        if name not in stuff:
            stuff[name] = defaultdict(set)
        for k in range(1,len(accounts[i])):
            set1 = set(accounts[i][1:k]) | set(accounts[i][k+1:])
            stuff[name][accounts[i][k]].update(set1)
            for email in set1:
                stuff[name][email].add(accounts[i][k])

    output = []
    for name in stuff:  
        done = defaultdict()
        for email in stuff[name]:       
            stack = {}
            if email not in done:
                email_list = []
                stack = stuff[name][email]
                email_list.append(email)
                done[email] = True
                while stack:
                    node = stack.pop()
                    if node not in done:
                        stack.update(stuff[name][node])
                        email_list.append(node)
                        done[node] = True
                email_list.sort()
                output.append([name] + email_list)
    return output







# sample inputs:

# Expect True
print(accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]) == [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])

# Expect True
print(accountsMerge([["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]])==[["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]])