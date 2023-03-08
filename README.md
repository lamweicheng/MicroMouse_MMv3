# MicroMouse_MMv3
MMv3 is the 3rd generation robot platform used to teach the IEEE Micromouse DeCal at UC Berkeley. It was designed with usability, manufacturability, size, and cost in mind.


MMv3 is the 3rd generation robot platform used to teach the IEEE Micromouse DeCal at UC Berkeley. It was designed with usability, manufacturability, size, and cost in mind.

## Setup

1. Follow the assembly instructions in [lab1](docs/lab1.md) using the latest **BOM**.
2. Plug mouse into your computer and upload the latest **firmware.uf2** (see [releases](https://circuitpython.org/board/raspberry_pi_pico/)) by dragging the file into the `RPI-RP2` folder that shows up. It should disappear and reappear as a `CIRCUITPY` folder.
    * If you've uploaded firmware before, you'll need to hold the `BOOTSEL` button on the Pi Pico while plugging in.
3. Download the latest CircuitPython [libraries](https://circuitpython.org/libraries) (Bundle for Version 7.x) and upload the following ones to the lib/ folder on your mouse.
    * adafruit_motor/
    * adafruit_onewire/
    * neopixel.mpy

## Labs

Skeleton lab code, lab documents, and solutions are stored in [labs/](labs/), [docs/](docs/), and [solutions/](solutions/), respectively. To get started with a lab, simply copy the contents of the folder over to the CircuitPython drive and edit files from there.

* [sanity](docs/sanity.md) - Hardware Check
* [lab1](docs/lab1.md) - Assembly
* [lab2](docs/lab2.md) - CircuitPython Basics
* [lab3](docs/lab3.md) - Encoders
* [lab4](docs/lab4.md) - IR Sensors
* [lab5](docs/lab5.md) - Odometry and Motor Control
* [lab6](docs/lab6.md) - Intro to PID
* [lab7](docs/lab7.md) - More PID
* [lab8](docs/lab8.md) - Maze Solving Primitives **(WIP)**
