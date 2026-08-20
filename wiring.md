# Prototype Wiring

## OLED SSD1306 I2C

Typical ESP8266 NodeMCU wiring:

| OLED | NodeMCU |
|---|---|
| VCC | 3.3V |
| GND | GND |
| SCL | D1 / GPIO5 |
| SDA | D2 / GPIO4 |

## Microphone

The example firmware assumes an analog microphone output connected to `A0`.

**Important:** verify the microphone module's output voltage range before connecting it to the ESP8266 ADC.

## Health Sensors

Health sensors are intentionally left modular. Add the exact sensor and pin mapping after selecting the sensor (for example, heart-rate/SpO2 or temperature).
