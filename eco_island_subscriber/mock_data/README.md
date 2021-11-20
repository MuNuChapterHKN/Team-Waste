# Mock data for data analytics

## Content of the dataset
This mock data contains 5 islands, 23 bins and 69 sensors.

Most of the islands have one bin for each type, no island has more than one bin for each type. Each island has 3 sensors, one for each type.


## Assumptions on sensor measurements
All volume and load sensors are measured once every minute, 24/7, and infrared sensor has one line every time trash is thrown in the bin.

### Volume sensor
The value column is a percentage

### Load sensor
The value column is a number from 0 to 100 (If it was a flaot it could be a net weight)

### Infrared sensor
value=1