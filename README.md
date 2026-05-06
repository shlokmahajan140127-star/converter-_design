This project involves developing Python code to automate the design calculations of the circuit, reducing manual effort and improving accuracy. The computed results are then validated using LTspice simulations to ensure correctness and practical reliability. This approach combines analytical design with simulation-based verification for efficient and accurate circuit development.

<img width="1905" height="844" alt="Screenshot 2026-05-06 235909" src="https://github.com/user-attachments/assets/b6a922de-f829-48af-96c2-4bf9eee6fe04" />

All component details — BSC035N04LS MOSFET, RB228T-60NZ Schottky diode, 76.83µH inductor, 4×100µF output caps
Operating parameters — 12V in, ~21.5V out, 42.5% duty cycle, 25kHz switching
Design equations — duty cycle, ideal Vout (20.87V theoretical vs 21.5V simulated), ripple voltage
Simulation results — startup overshoot (~28V peak), ~35ms settling time, steady-state behavior
PWM signal breakdown — PULSE parameters explained in table form
Improvement suggestions — closed-loop control, soft-start, snubber, EMI filter




<img width="1905" height="844" alt="Screenshot 2026-05-06 235909" src="https://github.com/user-attachments/assets/b5544394-c19e-40eb-b1e4-f5ff19f048eb" />
BSC042N03LS (30V, 4.2mΩ) MOSFET + 1N5819 Schottky diode + 12.15µH inductor + 4.7µF cap
400 kHz switching at 40% duty cycle → theoretical 4.8V, simulated ~4.7V (the ~100mV drop is explained by diode Vf losses)
No-load behavior explained — the slow exponential rise in V(n008) is because there's no load resistor to discharge, making it charge like an RC circuit
Inductor ripple current: ~0.593A and output ripple: ~39.5mV calculated
Buck vs Boost comparison table — since you've designed both, it neatly contrasts both designs side by side
