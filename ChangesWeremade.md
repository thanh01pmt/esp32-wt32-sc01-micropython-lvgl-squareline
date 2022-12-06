In folder: **lv_micropython/ports/esp32/modules**

Update 3 files before compile the firmware for ESP32:
* ft6x36.py (driver for touch)
* ili9XXX.py (add subclass st7796(ili9XXX), driver for display)
* squarelineHelper.py (optional, used by Squareline exported code)

=> All needed files are in this gist
