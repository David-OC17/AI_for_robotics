# Write a function 'kalman_filter' that implements a multi-
# dimensional Kalman Filter for the example given

from math import *
import matrix

########################################

# Implement the filter function below

def kalman_filter(x, P):
    for n in range(len(measurements)):
        
        # measurement update
        # y = z - H*x
        # S = H*P*Ht + R
        # K = P*Ht*S^-1
        # x1 = x + (K*y)
        # P1 = (I - K*H) * P
        Ht = H.transpose()
        z = matrix.matrix([[measurements[n]]])
        y = z - (H * x)
        S = (H * P * Ht) + R
        Sinv = S.inverse()
        K = P * Ht * Sinv
        x = x + (K * y)
        P = (I - K * H) * P

        # prediction
        # x1 = F*x + u
        # P1 = F * P * Ft
        x = F * x + u
        P = F * P * F.transpose()
        
    return x,P

############################################
### use the code below to test your filter!
############################################

measurements = [1, 2, 3]

x = matrix.matrix([[0.], [0.]]) # initial state (location and velocity)
P = matrix.matrix([[1000., 1.], [0., 1000.]]) # initial uncertainty
u = matrix.matrix([[0.], [0.]]) # external motion
F = matrix.matrix([[1., 1.], [0, 1.]]) # next state function
H = matrix.matrix([[1., 0.]]) # measurement function
R = matrix.matrix([[1.]]) # measurement uncertainty
I = matrix.matrix([[1., 0.], [0., 1.]]) # identity matrix

print(kalman_filter(x, P))
# output should be:
# x: [[3.9996664447958645], [0.9999998335552873]]
# P: [[2.3318904241194827, 0.9991676099921091], [0.9991676099921067, 0.49950058263974184]]
                                                            