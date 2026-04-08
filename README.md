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
