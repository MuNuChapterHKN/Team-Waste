# Mock data for data analytics

## Content of the dataset
This mock data contains 2 islands, 9 bins and 27 sensors.

Most of the islands have one bin for each type, no island has more than one bin for each type. Each island has 3 sensors, one for each type.


## Assumptions on sensor measurements
Volume and load sensors are measured at random times and have random values, and there's entries for infrared sensor at random times.

### Volume sensor
The value column is a percentage.

### Load sensor
The value column is the net weight, from 0 to 8kg (an arbitrary number).

### Infrared sensor
value=1