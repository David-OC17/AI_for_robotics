#probabilities of overshooting or undershooting 
#the intended destination.

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    range_ = range(len(p))
    for i in range_:
        #Exact
        prob = p[(i-U)%len(p)]*pExact
        #Behind undershot
        prob += p[(i-U+1)%len(p)]*pUndershoot
        #In front overshot
        prob += p[(i-U-1)%len(p)]*pOvershoot
        
        q.append(prob)
        
    
    return q
    

print(move(p, 1))#Move once
print(move(move(p, 1), 1)) #Move two times, accumulate prob

#Given the list motions=[1,1] which means the robot 
#moves right and then right again, compute the posterior 
#distribution if the robot first senses red, then moves 
#right one, then senses green, then moves right again, 
#starting with a uniform prior distribution.
p = [2, 2, 2, 2, 2]
p = move(sense(move(sense(p, measurements[0]), 1), measurements[1]), 1)
