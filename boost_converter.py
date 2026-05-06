#VS =12 #input voltage
VS =float(input("enter the input voltage :- "))
VD =float(input(" enter the output voltage :- "))
#VD =5 #output voltage
switching_frequency=int(input("enter the frequency :- ")) # Frequency
#switching_frequency=400000
max_output_current=int(input("enter the max out put current:- "))
#max_output_current=2 #7A

def Duty_cycle(VS, VD):
    return ((VD)/(VS))
duty_cycle=Duty_cycle(VS, VD)
print("duty_cycle :- " ,duty_cycle)
print("\n")


def current_ripple(max_output_current):
    return (0.3*max_output_current ) #choose between 20% to 40%
ripple_current=current_ripple(max_output_current)
print("Inducter Ripple:- ",ripple_current)
print("\n")


def Inductor_val(VS,VD ,Inducter_ripple_current ,switching_frequency,duty_cycle):
    return ((VD*(1 - duty_cycle))/(Inducter_ripple_current * switching_frequency))
Inductor=Inductor_val(VS,VD ,ripple_current ,switching_frequency ,duty_cycle)
print("Inductor val :- ",Inductor)
print("\n")


def Voltage_ripple(VD):
    return 0.01 * VD ## choose between 1% to 5%
ripple_voltage=Voltage_ripple(VD)
print("ripple voltage :- ",ripple_voltage)
print("\n")


def Capacitance(ripple_current , ripple_voltage , switching_frequency):
    return ((ripple_current)/(8 * switching_frequency* ripple_voltage))
capacitance =Capacitance(ripple_current , ripple_voltage , switching_frequency)
print('capacitance is :- ',capacitance)
print("\n")


def Diode_current(duty_cycle , max_output_current):
    return max_output_current*(1 - duty_cycle)
diode_current=Diode_current(duty_cycle , max_output_current)
print('Diode current :- ',diode_current)
print("\n")

