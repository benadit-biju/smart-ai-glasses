# Smart AI Glasses

A smart wearable prototype that combines **AI, IoT, voice interaction, OLED feedback, and health monitoring** using an ESP8266 NodeMCU.

## Features

- Voice-input interface using a microphone
- OLED display for notifications, AI responses, and device status
- Wi-Fi connectivity through ESP8266 NodeMCU
- AI-assisted processing through a configurable API/backend
- Health-data interface for future sensors such as pulse/SpO2/temperature sensors
- Modular architecture so the wearable can be extended with additional sensors
- Lightweight design suitable for an academic prototype

## System Architecture

```text
Microphone ───────┐
                  │
Health Sensors ───┼──> ESP8266 NodeMCU ──Wi-Fi──> AI/API Backend
                  │             │                    │
                  │             └──> OLED Display <──┘
                  │
             User / Wearable
```

## Hardware

- ESP8266 NodeMCU
- 0.96" SSD1306 OLED (I2C)
- Microphone module
- Health sensor(s), optional depending on implementation
- Li-ion/battery power system
- Glasses frame / wearable enclosure

## Software

- Arduino IDE
- ESP8266 Arduino Core
- Adafruit GFX
- Adafruit SSD1306
- WiFi / HTTP client libraries
- Optional Python backend for AI processing

## Repository Structure

```text
smart-ai-glasses/
├── firmware/
│   └── smart_ai_glasses.ino
├── backend/
│   ├── app.py
│   └── requirements.txt
├── docs/
│   ├── architecture.md
│   └── wiring.md
├── assets/
│   └── project-image-placeholder.txt
├── .gitignore
└── README.md
```

## Getting Started

1. Install Arduino IDE.
2. Add ESP8266 board support.
3. Install `Adafruit GFX Library` and `Adafruit SSD1306`.
4. Open `firmware/smart_ai_glasses.ino`.
5. Enter your Wi-Fi credentials and backend URL.
6. Upload the firmware to NodeMCU.
7. Start the optional backend with:

```bash
cd backend
pip install -r requirements.txt
python app.py
```

> The AI backend is intentionally modular. Replace the demo response function with your preferred AI model/API.

## Future Enhancements

- Offline/on-device speech recognition
- Text-to-speech output
- GPS navigation assistance
- Object detection
- Fall detection
- Heart-rate and SpO2 monitoring
- Emergency alert to a cloud service
- Firebase/Firestore integration
- Mobile companion application
