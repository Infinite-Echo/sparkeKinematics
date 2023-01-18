% L1 = 0.055
% L2 = 0.125
% L3 = 0.135
% W = 0.055
% L = 0.101
% thetaB = 0
% theta1 = 0
% theta2 = 0
% theta3 = 0
thetaB = 
Tb0 = [cos(thetaB) -sin(thetaB) 0 W; 
    sin(thetaB) cos(thetaB) 0 -L; 
    0 0 1 0;
    0 0 0 1]
T01 = [cos(theta1) 0 -sin(theta1) L1;
    0 1 0 0;
    sin(theta1) 0 cos(theta1) 0;
    0 0 0 1]
T12 = [1 0 0 0;
    0 cos(theta2) -sin(theta2) -L2*cos(theta2+(pi/4));
    0 sin(theta2) cos(theta2) -L2*sin(theta2+(pi/4));
    0 0 0 1]
T23 = [1 0 0 0;
    0 cos(theta3) -sin(theta3) -L3*cos(theta3+(pi/4));
    0 sin(theta3) cos(theta3) -L3*sin(theta3+(pi/4));
    0 0 0 1]
Tb0
p0 = Tb0*T01
p1 = p0*T12
p2 = p1*T23