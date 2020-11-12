## Installing the PubSubClient Library
The [PubSubClient](https://github.com/knolleary/pubsubclient) library provides a client for doing simple publish/subscribe messaging with a server that supports MQTT (basically allows your ESP32 to talk with Node-RED).

    1. [Click here to download the PubSubClient library.](https://github.com/knolleary/pubsubclient/archive/master.zip) You should have a .zip folder in your Downloads folder
    2. Unzip the .zip folder and you should get ~~pubsubclient-master~~ folder
    3. Rename your folder from pubsubclient-master to pubsubclient
    4. Move the pubsubclient folder to your Arduino IDE installation libraries folder
    5. Then, re-open your Arduino IDE
The library comes with a number of example sketches. See **File** >**Examples** > **PubSubClient** within the Arduino IDE software.

**Important:** PubSubClient is not fully compatible with the ESP32, but the example provided in this tutorial is working very reliably during our tests.