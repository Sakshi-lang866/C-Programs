# C-Programs
Basic C programs for beginners
# PCB Tester using Raspberry Pi (GPIO Based)

## 📖 Project Description
This project is a simple PCB testing system using Raspberry Pi GPIO pins.  
It measures:
- Voltage
- Current
- Temperature  

and checks whether the PCB is working properly (PASS/FAIL).

## 🛠️ Technologies Used
- Python
- Raspberry Pi
- GPIO Library

## ⚙️ Hardware Required
- Raspberry Pi
- Sensors (Voltage, Current, Temperature)
- ADC (e.g., ADS1115)

## 🚀 How It Works
1. Sensors read voltage, current, and temperature.
2. Values are processed in Python.
3. System checks:
   - Voltage in range (3V – 12V)
   - Current in range (0.1A – 5A)
   - Temperature < 70°C
4. Displays PCB Status → PASS / FAIL

## ▶️ How to Run
```bash
python pcb_tester.py
# Wireless E-Notice Board

## Description
This project demonstrates a wireless electronic notice board using NodeMCU and embedded systems.

## Features
- Wireless message transmission
- Real-time display on LCD
- Simple user input system

## Hardware Used
- NodeMCU (ESP8266)
- LCD Display
- Wi-Fi Communication

## Technologies Used
- Embedded C / Arduino
- IoT Concepts

## Output
Displays messages on the electronic notice board in real-time

## Note
This is a basic simulation of the actual hardware implementation.
