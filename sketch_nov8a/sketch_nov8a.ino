const int trigPin = 9;
const int echoPin = 10;

void setup() {
    Serial.begin(9600); // Initialize serial communication at 9600 baud
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
}

void loop() {
    long duration;
    int distance;

    // Send a pulse to trigger the ultrasonic sensor
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    // Read the echo time
    duration = pulseIn(echoPin, HIGH);

    // Calculate the distance (in cm)
    distance = duration * 0.034 / 2;

    // Print the distance to the serial monitor
    Serial.println(distance);

    delay(1000); // Wait for a second before taking another reading
}
