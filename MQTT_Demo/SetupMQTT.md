# Setup and run a MQTT server on your PC (UBUNTU & WINDOWS)

Requirements for windows:
- Windows 10
- Windows Subsistem for Linux (WSL): https://docs.microsoft.com/en-us/windows/wsl/install-win10
- Ubuntu installed on WSL

If on Windows open the WSL folder and type, otherwise simply open a Linux terminal:
```
sudo apt-get update
```

after the repos have been updated install the mosquitto MQTT broker
```
sudo apt-get install mosquitto
```

run mosquitto with:
```
mosquitto
```

More infos on how to configure mosquitto here: https://mosquitto.org/man/mosquitto-conf-5.html

If you are on linux the mosquitto broker is up and running, execute the 2 python scripts in this folder in 2 different terminals in the following order:
- mqtt_subscriber.py
- mqtt_publisher.py

If you are on Windows it is necessary to open a port on the firewall in order to send and receive traffic

## Open a port on the firewall (Necessary only on Windows)
- Go to Windows Firewall with Advanced Security
- Click on Inbound Rules and then on the right: Add a new Rule
- Set rule type as Port
- Enter a specific local port in which the server is running; in this case: 1883 (default port for MQTT)
- Set TCP Port
- In the following tab select: Allow the connection
- Set wheter this rule applies (for simplicity check all)
- Name the rule as you like and click Finish