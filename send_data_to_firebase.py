import firebase_admin
from firebase_admin import credentials, db
import serial
import time

# Initialize Firebase
cred = credentials.Certificate('/Users/keshav/Desktop/cc api da/ultrasonic sensor/firebase_credentials.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ultrasonicsensordata-default-rtdb.firebaseio.com/'  # replace with your actual Firebase URL
})

# Initialize Serial Communication
ser = serial.Serial('/dev/cu.usbmodem1201', 9600)  # Replace with your Arduino's serial port
time.sleep(2)  # Allow time for the serial connection to initialize

while True:
    if ser.in_waiting > 0:
        distance = ser.readline().decode('utf-8').strip()
        print(f"Distance: {distance} cm")

        # Send data to Firebase
        db.reference('/ultrasonic_data').push({
            'distance': distance,
            'timestamp': time.time()
        })
        time.sleep(1)
