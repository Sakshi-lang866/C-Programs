import RPi.GPIO as GPIO
import time
import random

# GPIO setup
GPIO.setmode(GPIO.BCM)

# Define pins (example)
VOLTAGE_PIN = 17
CURRENT_PIN = 27
TEMP_PIN = 22

GPIO.setup(VOLTAGE_PIN, GPIO.IN)
GPIO.setup(CURRENT_PIN, GPIO.IN)
GPIO.setup(TEMP_PIN, GPIO.IN)

# Simulated sensor reading functions
def read_voltage():
    # In real case: ADC (ADS1115)
    return round(random.uniform(3, 12), 2)

def read_current():
    return round(random.uniform(0.1, 5), 2)

def read_temperature():
    return round(random.uniform(25, 75), 2)

def check_status(v, c, t):
    if (3 <= v <= 12) and (0.1 <= c <= 5) and (t < 70):
        return "PASS"
    else:
        return "FAIL"

try:
    print("---- PCB TESTER (GPIO BASED) ----")

    voltage = read_voltage()
    current = read_current()
    temp = read_temperature()

    print(f"Voltage: {voltage} V")
    print(f"Current: {current} A")
    print(f"Temperature: {temp} °C")

    status = check_status(voltage, current, temp)
    print("PCB Status:", status)

    time.sleep(2)

except KeyboardInterrupt:
    print("Program stopped")

finally:
    GPIO.cleanup()
