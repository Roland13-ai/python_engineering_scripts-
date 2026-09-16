
#Exercise1 controlling 2 LEDs via Bluetooth (HC-05)

## Objective
Control 2 LEDs using commands received via Bluetooth (HC-05 module),
using the "Serial Bluetooth Terminal" app on a smartphone.

## Files
- 1erExo.ino: Arduino source code
- wiring_proteus_arduino_basics.jpg: Wiring diagram created in Proteus 9

## Code Operation
- SoftwareSerial BT(10, 11): Software serial communication with the HC-05

(pin 10 = RX, pin 11 = TX)
- Pin 7 → light1, Pin 8 → light2
- Commands received via Bluetooth:

- 1 → turns on light1

- 2 → turns on light2

- 0 → turns off both lights

## Proteus Simulation
The diagram cablage_proteus_arduino_base.jpg shows the basic setup
built to validate the hardware wiring:
- ATmega328P
- External 16 MHz oscillator (crystal + 2 22pF capacitors)

- Reset circuit (10kΩ pull-up resistor)

- 2 LEDs with current-limiting resistors (220Ω)

*Limitation encountered*: The HC-05 module is not available in the Proteus 9 demo version library, and the AVR microcontroller simulation itself requires a full license (error
"AVR2.DLL failed to authorize"). The circuit was therefore built and visually checked, but could not be run in a real simulation.

## Status
- [x] Code written and compiled without errors (Arduino IDE)
- [x] Generated .hex file
- [x] Wiring diagram built in Proteus
- [ ] Functional simulation (blocked by demo license)
- [ ] Testing with real hardware (Arduino + physical HC-05) — coming soon