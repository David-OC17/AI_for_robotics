#Function 'kalman_filter' that implements a 
# multi-dimensional Kalman Filter

import matrix as matrix

def kalman_filter(x, P):
    #where x is the initial state (location and velocity)
    #and P is the initial uncertainty
    for n in range(len(measurements)):
        Y = measurements[n] - H * x
        S = H * P * H.transpose() + R
        K = P * H.transpose() * S.inverse()
        # measurement update
        x = x + K * Y

        # prediction
        P = (I - K * H) * P
        
    return x,P

############################################
### use the code below to test your filter!
############################################

measurements = [1, 2, 3]

x = matrix.matrix([[0.], [0.]]) # initial state (location and velocity)
P = matrix.matrix([[1000., 0.], [0., 1000.]]) # initial uncertainty
u = matrix.matrix([[0.], [0.]]) # external motion
F = matrix.matrix([[1., 1.], [0, 1.]]) # next state function
H = matrix.matrix([[1., 0.]]) # measurement function
R = matrix.matrix([[1.]]) # measurement uncertainty
I = matrix.matrix([[1., 0.], [0., 1.]]) # identity matrix

print(kalman_filter(x, P))
# output should be:
# x: [[3.9996664447958645], [0.9999998335552873]]
# P: [[2.3318904241194827, 0.9991676099921091], [0.9991676099921067, 0.49950058263974184]]
