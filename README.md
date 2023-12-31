# SEU Testing Of ECON-D

Logs from radiation tests of ECON-D-P1 at Northwestern Medicine Proton Therapy Center in Warrenville; August 5, 2023

## Run Information

| Run   | Time     |Current [nA]	| Calib [p/cm2/MU] |Time [s] | MU | Energy [MeV] | Flux [1/cm2/s] |Fluence [1/cm2]	| Tot Fluence [1/cm2] | Notes |
| ----------- | ----------- |  ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| 1	| 10:00 am | 2	 | 1.70E+07 | 52  | 779	   | 217 | 2.55E+08 | 1.32E+10 | 1.32E+10 |  |
| 2	| 10:17 am | 5	 | 1.70E+07 | 100 | 4413   | 217 | 7.50E+08 | 7.50E+10 | 8.83E+10 |  |
| 3	| 10:30 am | 10	 | 1.70E+07 | 159 | 15674  | 217 | 1.68E+09 | 2.66E+11 | 3.55E+11 |  |
| 4	| 10:45 am | 25	 | 1.74E+07 | 158 | 40000  | 217 | 4.41E+09 | 6.96E+11 | 1.05E+12 |  |
| 5	| 10:51 am | 50	 | 1.79E+07 | 117 | 56200  | 217 | 8.60E+09 | 1.01E+12 | 2.06E+12 | hex48 error abort (i2c issue) |
| 6	| 11:25 am | 100 | 1.90E+07 | 126 | 105814 | 217 | 1.60E+10 | 2.01E+12 | 4.07E+12 | hex44 RO - no JSON |
| 7	| 12:04 pm | 25	 | 1.74E+07 | 30  | 7891   | 217 | 4.58E+09 | 1.37E+11 | 4.20E+12 |  |
| 8	| 12:11 pm | 100 | 1.90E+07 | 56  | 49987  | 217 | 1.70E+10 | 9.50E+11 | 5.15E+12 |  |
| 9	| 12:19 pm | 100 | 1.90E+07 | 180 | 150933 | 217 | 1.59E+10 | 2.87E+12 | 8.02E+12 | beam abort, hex44 RO - JSON saved|
| 10	|  1:16 pm | 100 | 1.90E+07 | 60  | 50520  | 217 | 1.60E+10 | 9.60E+11 | 8.98E+12 |  |
| 11	|  1:20 pm | 100 | 1.90E+07 | 609 | 506749 | 217 | 1.58E+10 | 9.63E+12 | 1.86E+13 |  |
| 12	|  1:39 pm | 100 | 1.90E+07 | 635 | 550490 | 217 | 1.65E+10 | 1.05E+13 | 2.91E+13 |  |
| 13	|  1:57 pm | 100 | 1.90E+07 | 194 | 166333 | 217 | 1.63E+10 | 3.16E+12 | 3.22E+13 | beam abort |
| 14	|  2:00 pm | 100 | 1.90E+07 | 543 | 470286 | 217 | 1.65E+10 | 8.94E+12 | 4.12E+13 |  |
| 15	|  2:25 pm | 100 | 1.90E+07 | 354 | 305957 | 217 | 1.64E+10 | 5.81E+12 | 4.70E+13 |  |
| 16	|  2:53 pm | 100 | 1.90E+07 | 59  | 50820  | 217 | 1.64E+10 | 9.66E+11 | 4.79E+13 | all 1s and 0s |
| 17	|  2:59 pm | 100 | 1.90E+07 | 58  | 50150  | 217 | 1.64E+10 | 9.53E+11 | 4.89E+13 | all 0s and 1s |
| 18	|  3:23 pm | 100 | 1.90E+07 | 59  | 50767  | 217 | 1.63E+10 | 9.65E+11 | 4.99E+13 | CLKA turned off |

## Setup information

Photos of the setup can be found [here](https://photos.app.goo.gl/F5yrbbC9boyt8ciVA).

Two chips were irradiated:
 - Chip 4, connected to hexacontroller 48, on the side of g-10 card closest to the beam aperture
 - Chip 1, connected to hexacontroller 44, on the side of the g-10 card further from the bream aperture