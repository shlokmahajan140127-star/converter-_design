# P=100
P =float(input ("enter the power :- "))
# fs =25000
fs=float(input("enter the frequency:- "))
# Vs= 12
Vs=float(input("neter the input voltage:- "))
# VD=20
VD=float(input( "enter the output voltage:- "))
# delta_IL=0.3
delta_IL=float(input ("enter the ripple current:- "))
# delta_VC=0.01
delta_VC=float(input ("enter the ripple voltage:- "))

def Duty_cycle(Vs,VD,n):
    return ((1-(Vs/VD)))
duty_cycle=Duty_cycle(Vs,VD,n)

print ( "duty_cycle :- ",(duty_cycle))
print("\n")


def IL(P,Vs):
    return (P/Vs)
Il=IL(P,Vs)
print( "IL :-", Il)
print('\n')


def inductance(Vs,duty_cycle,fs,Il,delta_IL):
    return ((Vs * (duty_cycle))/(fs * delta_IL *Il))
L=inductance(Vs,duty_cycle,fs,Il,delta_IL)
print("inductance :- ", L)
print("\n")    


def ID_max(P,VD):
    return (P/VD)
ID= ID_max(P,VD)
print("max current :- ",ID)
print('\n')


def Capacitance(ID,duty_cycle,fs,delta_VC ,VD):
    return (ID*(duty_cycle))/(fs * delta_VC * VD )
C=Capacitance(ID,duty_cycle,fs,delta_VC ,VD)
print("Capacitance :- " ,C)
print("\n")


def load_of_rated_power(VD ,P):
    return (VD*VD)/P
power=load_of_rated_power(VD ,P)
print( 'load at rated resistor in ohms  ',power)
print('\n')
