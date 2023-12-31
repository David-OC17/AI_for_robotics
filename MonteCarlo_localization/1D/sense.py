#Modify the code below so that the function sense, which 
#takes p and Z as inputs, will output the normalized 
#probability distribution, q, after multiplying the entries 
#in p by pHit or pMiss according to the color in the 
#corresponding cell in world.


p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q = [0] * len(p)
    for i in range(len(p)):
        if world[i] == Z:
            q[i] = p[i] * pHit
        else:
            q[i] = p[i] * pMiss
    
    total = sum(q)
    q = [x / total for x in q]
    
    return q
    
print(sense(p,Z))


'''
p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    total = sum(q)
    q = [x / total for x in q]
    return q
print sense(p,Z)

'''