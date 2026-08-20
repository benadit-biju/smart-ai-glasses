# Architecture

## Main data flow

1. The microphone captures voice activity.
2. ESP8266 NodeMCU detects/processes the input.
3. Wi-Fi sends a request to the AI backend.
4. The AI backend processes the request.
5. The response is returned to the NodeMCU.
6. OLED displays the result to the user.
7. Health sensors can periodically provide wearable health data.

## AI Layer

The repository uses a replaceable AI interface rather than hard-coding a specific provider. This allows the project to use a cloud model or a local model later.

## IoT Layer

ESP8266 provides Wi-Fi connectivity and can be extended with MQTT, Firebase, REST APIs, or another IoT platform.
