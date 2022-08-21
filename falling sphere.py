# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 20:03:15 2022

@author: MUSTAFA
"""

""" Euler Method will be used in this code."""





"""For baseball"""

# Part a)

import matplotlib.pyplot as plt
import numpy as np
import math

# Defining constants of the motion:
    
m_base= 0.145 # Typical mass of a baseball in kg.
g= 9.8 # Gravitational acceleration in m/s^2.
D= 0.5 # Drag coefficient (unitless).
p= 1.225 # Density of air near sea level in kg/m^3.
R_base= 0.0365 # Typical radius of a baseball in m.
A_base= 2*math.pi*R_base**2 # Frontal surface area of the baseball in m^2.
tau=0.005 # Time step (unitless).

# Initial conditions must be set up:

y_i= 440 # Initial height in m.
v_i= 0 # Initial velocity in m/s.
a_i= g # Initial acceleration in m/s^2.
t_i= 0 # Initial time in s.   


# Declaring lists for the position & velocity of the baseball:

pos_list= [y_i]
vel_list= [v_i]
time_list= [t_i]

# Declaring a list for the flight times for the exact calculations:
    
flight=[]

# Using Euler Method to calculate instantaneous position and velocity:

for n in range (1, 10000001): # Let the total number of steps be n_max= 10000000.
    new_vel=v_i+tau*a_i # New velocity.
    new_pos=y_i-tau*v_i # New position.
    # Filling the lists with new values of velocity and position:
    vel_list.append(v_i) 
    pos_list.append(y_i)
    time_list.append(n*tau)
    # Updating the variables:
    v_i=new_vel
    y_i=new_pos
    a_i= (m_base*g-(1/2)*D*p*A_base*new_vel**2)/m_base # New acceleration in m/s^2.
    if n*tau==4: # For t=4 s (Verification of the Program / Numerical Values):
        print(str(new_pos)+' '+' is the numerical position of BASEBALL at t= 4s.''\n')
        print(str(new_vel)+' '+' is the numerical velocity of BASEBALL at t= 4s.''\n')
    
    if y_i <= 0: # The ball cannot go underground, it must bounce back. Thus, flight time must be computed.
        print(str(n*tau)+'s'+' '+'is the approximate flight time of BASEBALL.''\n')
        flight.append(str(n*tau)) # Saving the flight time to be used in the exact calculation.
        break
    


# Part b)

# Declaring position & time lists again:

pos= []
vel= []

# Declaring a time array up to the flight time found in part a):

time=np.arange(0, float(flight[0])+tau, tau)

# Exact calculation:  

for t in time:
    # Exact position (it is relative to the ground, that is why we substract from 440 meters):
    exact_pos=440- (2*m_base/(D*p*A_base))*math.log(math.cosh(math.sqrt((D*p*A_base*g/(2*m_base)))*t))
    # Exact velocity:
    exact_vel=math.sqrt((2*m_base*g/(D*p*A_base)))*math.tanh(math.sqrt((D*p*A_base*g/(2*m_base)))*t)
    # Filling the lists for velocity and position:
    pos.append(exact_pos)
    vel.append(exact_vel)
    if t==4: # For t=4 s (Verification of the Program / Exact Values):
        print(str(exact_pos)+' '+'is the exact position of BASEBALL at t= 4s.''\n')
        print(str(exact_vel)+' '+'is the exact velocity of BASEBALL at t= 4s.''\n')
    
    

# Plotting the results for baseball:
plt.plot(time_list,vel_list, 'r', label='Numerical Velocity')
plt.plot(time,vel, 'k--', label='Exact Velocity')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')  
plt.title('Exact vs Numerical Velocity (Baseball)') 
plt.legend()
plt.show()



plt.plot(time_list,pos_list, 'r', label='Numerical Position')
plt.plot(time, pos, 'k--', label='Exact Position')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')  
plt.title('Exact vs Numerical Position (Baseball)') 
plt.legend()
plt.show()

    

"""For basketball"""

# Part a)     

# Defining constants of the motion again for the basketball:
    
m_bask= 0.624 # Typical mass of a basketball in kg.    
R_bask= 0.1194 # Typical radius of a basketball in m.
A_bask= 2*math.pi*R_bask**2 # Frontal surface area of the basketball in m^2.

# Initial conditions must be set up again:

y_i= 440 # Initial height in m.
v_i= 0 # Initial velocity in m/s.
a_i= g # Initial acceleration in m/s^2.
t_i= 0 # Initial time in s.   


# Declaring lists for the position & velocity of the basketball:

pos_list1=[y_i]
vel_list1=[v_i]
time_list1=[t_i]

# Using Euler Method to calculate instantaneous position and velocity:

for n in range (1, 10000001): # Let the total number of steps be n_max= 10000000.
    new_vel=v_i+tau*a_i # New velocity.
    new_pos=y_i-tau*v_i # New position.
    # Filling the lists with new values of velocity and position:
    vel_list1.append(v_i) 
    pos_list1.append(y_i)
    time_list1.append(n*tau)
    # Updating the variables:
    v_i=new_vel
    y_i=new_pos
    a_i= (m_bask*g-(1/2)*D*p*A_bask*new_vel**2)/m_bask # New acceleration in m/s^2.
    if n*tau==4: # For t=4 s (Verification of the Program / Numerical Values):
        print(str(new_pos)+' '+' is the numerical position of BASKETBALL at t= 4s.''\n')
        print(str(new_vel)+' '+' is the numerical velocity of BASKETBALL at t= 4s.''\n')
    
    if y_i <= 0: # The ball cannot go underground, it must bounce back. Thus, flight time must be computed.
        print(str(n*tau)+'s'+' '+'is the approximate flight time of BASKETBALL.''\n')
        flight.append(str(n*tau)) # Saving the flight time to be used in the exact calculation.
        break
    

# Part b)

# Declaring position & time lists again:

pos1= []
vel1= []

# Declaring a time array up to the flight time found in part a).

time=np.arange(0, float(flight[1])+tau, tau)

# Exact calculation:  

for t in time:
    # Exact position (it is relative to the ground, that is why we substract from 440 meters):
    exact_pos=440- (2*m_bask/(D*p*A_bask))*math.log(math.cosh(math.sqrt((D*p*A_bask*g/(2*m_bask)))*t))
    # Exact velocity:
    exact_vel=math.sqrt((2*m_bask*g/(D*p*A_bask)))*math.tanh(math.sqrt((D*p*A_bask*g/(2*m_bask)))*t)
    # Filling the lists for velocity and position:
    pos1.append(exact_pos)
    vel1.append(exact_vel)
    if t==4: # For t=4 s (Verification of the Program / Exact Values):
        print(str(exact_pos)+' '+'is the exact position of BASKETBALL at t= 4s.''\n')
        print(str(exact_vel)+' '+'is the exact velocity of BASKETBALL at t= 4s.''\n')
    

# Plotting the results for basketball:
plt.plot(time_list1,vel_list1, 'r', label='Numerical Velocity')
plt.plot(time,vel1, 'k--', label='Exact Velocity')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')  
plt.title('Exact vs Numerical Velocity (Basketball)') 
plt.legend()
plt.show()


plt.plot(time_list1,pos_list1, 'r', label='Numerical Position')
plt.plot(time, pos1, 'k--', label='Exact Position')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')  
plt.title('Exact vs Numerical Position (Basketball)') 
plt.legend()
plt.show()



"""For bowling ball"""

# Part a)   

# Defining constants of the motion again for the bowling ball:
    
m_bow= 5 # Typical mass of a bowling ball in kg.    
R_bow= 0.108 # Typical radius of a bowling ball in m.
A_bow= 2*math.pi*R_bow**2 # Frontal surface area of the bowling ball in m^2.

# Initial conditions must be set up again:

y_i= 440 # Initial height in m.
v_i= 0 # Initial velocity in m/s.
a_i= g # Initial acceleration in m/s^2.
t_i= 0 # Initial time in s.   


# Declaring lists for the position & velocity of the bowling ball:

pos_list2=[y_i]
vel_list2=[v_i]
time_list2=[t_i]

# Using Euler Method to calculate instantaneous position and velocity:

for n in range (1, 10000001): # Let the total number of steps be n_max= 10000000.
    new_vel=v_i+tau*a_i # New velocity.
    new_pos=y_i-tau*v_i # New position.
    # Filling the lists with new values of velocity and position:
    vel_list2.append(v_i) 
    pos_list2.append(y_i)
    time_list2.append(n*tau)
    # Updating the variables:
    v_i=new_vel
    y_i=new_pos
    a_i= (m_bow*g-(1/2)*D*p*A_bow*new_vel**2)/m_bow # New acceleration in m/s^2.
    
    if n*tau==4: # For t=4 s (Verification of the Program / Numerical Values):
        print(str(new_pos)+' '+' is the numerical position of BOWLING BALL at t= 4s.''\n')
        print(str(new_vel)+' '+' is the numerical velocity of BOWLING BALL at t= 4s.''\n')
    if y_i <= 0: # The ball cannot go underground, it must bounce back. Thus, flight time must be computed.
        print(str(n*tau)+'s'+' '+ 'is the approximate flight time of BOWLING BALL.''\n')  
        flight.append(str(n*tau)) # Saving the flight time to be used in the exact calculation.
        break

# Part b)

# Declaring position & time lists again:

pos2= []
vel2= []


# Declaring a time array up to flight time found in part a).
    
time=np.arange(0, float(flight[2])+tau, tau)

# Now we can calculate the exact position & time:
for t in time:   
    # Exact position (it is relative to the ground, that is why we substract from 440 meters):
    exact_pos=440-(2*m_bow/(D*p*A_bow))*math.log(math.cosh(math.sqrt((D*p*A_bow*g/(2*m_bow)))*t))
    # Exact velocity:
    exact_vel=math.sqrt((2*m_bow*g/(D*p*A_bow)))*math.tanh(math.sqrt((D*p*A_bow*g/(2*m_bow)))*t)
    # Filling the lists for velocity and position:
    pos2.append(exact_pos)
    vel2.append(exact_vel)
    if t==4: # For t=4 s (Verification of the Program / Exact Values):
        print(str(exact_pos)+' '+'is the exact position of BOWLING BALL at t= 4s.''\n')
        print(str(exact_vel)+' '+'is the exact velocity of BOWLING BALL at t= 4s.''\n')
    
    
# Plotting the results for bowling ball:
plt.plot(time_list2,vel_list2, 'r', label='Numerical Velocity')
plt.plot(time,vel2, 'k--', label='Exact Velocity')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')  
plt.title('Exact vs Numerical Velocity (Bowling Ball)') 
plt.legend()
plt.show()


plt.plot(time_list2,pos_list2, 'r', label='Numerical Position')
plt.plot(time, pos2, 'k--', label='Exact Position')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')  
plt.title('Exact vs Numerical Position (Bowling Ball)') 
plt.legend()
plt.show()

# Name: Ahmet Mustafa Baraz
# ID: 21702127
# Title of the Program: Vertical motion of a falling sphere.
