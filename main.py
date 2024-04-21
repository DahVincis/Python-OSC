from pythonosc.udp_client import SimpleUDPClient
import time

client = SimpleUDPClient('192.168.1.5', 10023)  # Example IP and port

# Low: 118 to 292 | Low Mid: 313 to 1090 | High Mid: 1170 to 5000 | High: 5360 to 18660
dataRTA = {
    20: [-90.0, -90.0, -90.0, -90.0, -90.0, -90.0, -90.0, -90.0, -90.0, -90.0], 
    21: [-90.0, -90.0, -90.0, -90.0, -90.0, -90.0, -90.0, -90.0, -90.0, -90.0], 
    22: [-90.0, -90.0, -90.0, -90.0, -90.0, -90.0, -90.0, -90.0, -90.0, -90.0], 
    24: [-90.0, -90.0, -90.0, -90.0, -90.0, -90.0, -90.0, -90.0, -90.0, -90.0], 
    26: [-90.0, -89.7734375, -90.0, -90.0, -90.0, -90.0, -90.0, -90.0, -90.0, -90.0], 
    28: [-90.0, -88.3046875, -90.0, -90.0, -90.0, -90.0, -90.0, -88.8359375, -90.0, -90.0], 
    30: [-90.0, -87.1875, -89.6640625, -90.0, -90.0, -90.0, -89.9453125, -87.5859375, -89.171875, -90.0], 
    32: [-90.0, -85.6328125, -88.4296875, -90.0, -90.0, -90.0, -89.1796875, -86.2265625, -87.953125, -90.0], 
    34: [-90.0, -84.40625, -86.8046875, -89.359375, -90.0, -90.0, -87.84375, -84.921875, -86.4296875, -90.0], 
    36: [-90.0, -83.1015625, -86.109375, -88.328125, -90.0, -89.4609375, -86.46875, -83.3984375, -84.96875, -88.8671875], 
    39: [-90.0, -81.875, -83.875, -86.9453125, -90.0, -88.1171875, -84.9453125, -82.0703125, -83.171875, -87.6640625], 
    42: [-90.0, -79.921875, -82.484375, -85.171875, -90.0, -86.921875, -83.1171875, -80.8046875, -82.3984375, -86.5234375], 
    45: [-90.0, -77.8125, -81.1171875, -83.7578125, -90.0, -85.2421875, -82.390625, -79.2265625, -80.53125, -85.0546875], 
    48: [-90.0, -76.3984375, -79.046875, -82.2578125, -90.0, -82.78125, -79.59375, -77.796875, -78.3359375, -83.7734375], 
    52: [-90.0, -75.5078125, -73.9609375, -81.0625, -90.0, -81.546875, -78.8828125, -76.2890625, -77.21875, -81.6875], 
    55: [-90.0, -71.734375, -72.6015625, -79.625, -90.0, -79.7109375, -75.953125, -74.515625, -74.90625, -79.375], 
    59: [-90.0, -70.046875, -69.8125, -77.9609375, -90.0, -77.6953125, -74.078125, -73.09375, -72.53125, -77.9140625], 
    63: [-90.0, -69.6171875, -66.984375, -77.65625, -90.0, -75.9140625, -70.21875, -71.234375, -70.359375, -76.015625], 
    68: [-90.0, -65.8359375, -64.109375, -76.1328125, -90.0, -74.234375, -66.2421875, -68.9375, -68.40625, -73.7578125], 
    73: [-90.0, -62.59375, -61.4765625, -70.3984375, -89.3515625, -71.0234375, -61.515625, -66.6484375, -65.046875, -71.6015625], 
    78: [-90.0, -60.359375, -61.0234375, -72.4921875, -90.0, -76.265625, -58.1015625, -73.15625, -66.1171875, -74.4453125], 
    84: [-88.5703125, -54.828125, -58.3046875, -70.6484375, -89.6796875, -73.8984375, -54.7890625, -71.59375, -59.8984375, -73.5546875], 
    90: [-90.0, -51.359375, -55.2578125, -60.75, -79.7890625, -70.3125, -52.234375, -72.140625, -53.3671875, -62.9296875], 
    96: [-88.1015625, -47.15625, -51.4609375, -57.7734375, -76.8046875, -69.9765625, -49.8046875, -67.8125, -47.4765625, -66.4296875], 
    103: [-83.765625, -44.9921875, -46.1796875, -62.28125, -78.7265625, -69.296875, -45.375, -65.28125, -42.4375, -57.9453125], 
    110: [-82.0859375, -43.578125, -44.0078125, -58.484375, -77.5234375, -60.6875, -41.5859375, -61.4921875, -38.2734375, -51.6953125], 
    118: [-77.3203125, -40.15625, -43.7421875, -57.609375, -74.9609375, -59.578125, -38.9765625, -55.3671875, -35.046875, -46.609375], 
    127: [-72.8984375, -34.484375, -38.7578125, -48.75, -67.78125, -56.5859375, -36.984375, -48.8515625, -33.1796875, -44.3203125], 
    136: [-69.1171875, -28.859375, -34.625, -42.7265625, -61.7578125, -48.6328125, -36.7734375, -48.3515625, -32.0546875, -46.4375], 
    146: [-69.1015625, -25.21875, -32.8515625, -40.4453125, -59.4765625, -44.2734375, -33.875, -42.6484375, -31.4453125, -34.8203125], 
    156: [-58.2109375, -24.6015625, -28.1171875, -23.984375, -43.015625, -37.453125, -25.46875, -36.84375, -32.1796875, -28.1640625], 
    167: [-61.6640625, -27.640625, -24.0, -23.921875, -42.953125, -24.3046875, -22.2109375, -30.203125, -23.7890625, -26.515625], 
    179: [-54.1953125, -26.734375, -19.2109375, -22.1328125, -41.1640625, -22.3046875, -17.796875, -26.328125, -23.1015625, -22.4609375], 
    192: [-53.0703125, -18.359375, -18.5703125, -17.6484375, -36.6875, -21.2578125, -27.1328125, -35.71875, -25.375, -18.765625], 
    206: [-51.2265625, -19.0390625, -16.3515625, -21.0859375, -40.1171875, -20.03125, -26.5703125, -32.0625, -25.0078125, -38.265625], 
    221: [-47.578125, -22.3828125, -23.734375, -38.40625, -57.4375, -18.765625, -36.2890625, -34.96875, -29.5703125, -48.5234375], 
    237: [-46.28125, -30.046875, -32.3125, -45.5625, -64.59375, -41.7421875, -43.34375, -42.4609375, -38.8828125, -43.7265625], 
    254: [-44.203125, -26.78125, -35.3671875, -48.8828125, -67.9140625, -45.78125, -43.09375, -43.984375, -40.0, -42.953125], 
    272: [-54.1875, -28.4609375, -36.9296875, -43.5859375, -62.6171875, -51.0625, -39.84375, -45.890625, -42.296875, -37.2265625], 
    292: [-65.3125, -25.96875, -34.4140625, -35.296875, -54.328125, -48.7734375, -36.1796875, -39.1875, -42.1875, -24.4296875], 
    313: [-61.4765625, -26.7890625, -33.453125, -24.1328125, -43.171875, -36.2734375, -17.3671875, -31.71875, -34.34375, -15.625], 
    335: [-57.6875, -30.546875, -22.3046875, -17.2421875, -36.2734375, -18.3125, -20.15625, -27.8359375, -24.15625, -12.9375], 
    359: [-48.6640625, -18.8203125, -16.5703125, -13.6328125, -32.6640625, -17.796875, -12.171875, -27.7109375, -14.8671875, -8.3203125], 
    385: [-44.953125, -9.7578125, -15.140625, -3.1796875, -22.2109375, -19.84375, -16.078125, -33.53125, -12.3046875, -5.453125], 
    412: [-46.3125, -6.1015625, -2.6015625, -7.203125, -26.234375, -16.7421875, -14.9140625, -29.359375, -9.2890625, -28.2421875], 
    442: [-48.2109375, -14.6796875, -13.859375, -32.6484375, -51.6875, -16.5703125, -22.375, -28.296875, -13.96875, -32.921875], 
    474: [-46.15625, -22.859375, -31.0, -24.1640625, -43.1953125, -35.0546875, -30.75, -25.859375, -28.4609375, -32.953125], 
    508: [-48.265625, -34.5703125, -13.015625, -22.65625, -41.6953125, -20.4140625, -24.453125, -29.125, -19.53125, -34.0546875], 
    544: [-54.9453125, -21.1171875, -9.0078125, -21.78125, -40.8125, -18.234375, -21.65625, -40.6328125, -21.3515625, -31.3984375], 
    583: [-57.46875, -13.5703125, -3.0234375, -21.5, -40.53125, -17.140625, -19.890625, -39.328125, -25.1953125, -26.5859375], 
    625: [-61.125, -3.796875, -11.1015625, -26.0390625, -45.078125, -13.7734375, -11.625, -31.5390625, -14.3125, -33.265625], 
    670: [-53.359375, -14.546875, -7.3125, -22.0625, -41.1015625, -15.5390625, -27.5546875, -32.734375, -7.8671875, -26.8203125], 
    718: [-51.375, -14.2890625, -6.1640625, -20.90625, -39.9375, -24.3125, -22.8125, -40.5546875, -4.65625, -20.3671875], 
    769: [-54.8203125, -11.25, -11.390625, -20.8828125, -39.921875, -22.828125, -15.0, -34.90625, -20.7109375, -26.5234375], 
    825: [-54.765625, -9.28125, -19.9453125, -26.53125, -45.5625, -21.96875, -16.640625, -36.546875, -8.3671875, -27.3203125], 
    884: [-50.5234375, -11.8359375, -19.671875, -23.1328125, -42.1640625, -22.3671875, -33.765625, -36.0234375, -6.0546875, -25.0078125], 
    947: [-54.2421875, -14.8125, -18.40625, -21.484375, -40.515625, -17.984375, -21.1484375, -40.984375, -14.2578125, -30.3671875], 
    1020: [-54.0546875, -11.6953125, -13.890625, -23.09375, -42.125, -26.75, -15.3203125, -35.2265625, -9.5546875, -28.5078125], 
    1090: [-52.015625, -12.09375, -18.2890625, -24.2265625, -43.265625, -22.9140625, -18.640625, -38.5546875, -7.5, -25.5], 
    1170: [-49.859375, -12.5234375, -6.0703125, -14.2734375, -33.3046875, -23.8984375, -21.625, -35.7265625, -11.6328125, -20.171875], 
    1250: [-44.8984375, -6.296875, -11.8984375, -18.3046875, -37.34375, -14.8046875, -32.7578125, -32.7421875, -7.796875, -26.6953125], 
    1340: [-50.34375, -19.0, -9.6328125, -24.8046875, -43.8359375, -12.6328125, -28.625, -33.0859375, -22.7421875, -21.59375], 
    1440: [-56.4140625, -17.15625, -8.453125, -14.640625, -33.671875, -15.21875, -26.734375, -33.2109375, -16.6171875, -25.0625], 
    1540: [-44.671875, -18.4375, -19.3046875, -30.265625, -49.296875, -17.7734375, -16.4296875, -33.9453125, -32.7109375, -27.796875], 
    1650: [-47.296875, -11.2578125, -20.3984375, -19.4375, -38.46875, -21.609375, -19.875, -31.84375, -27.8203125, -25.8515625], 
    1770: [-42.984375, -19.296875, -22.2890625, -15.234375, -34.2734375, -23.9453125, -18.6953125, -38.6015625, -29.1640625, -25.53125], 
    1890: [-41.4375, -19.2109375, -20.5078125, -21.5625, -40.59375, -20.6640625, -15.2421875, -30.6015625, -26.8515625, -22.28125], 
    2030: [-49.03125, -19.59375, -18.84375, -15.265625, -34.3046875, -24.609375, -22.5546875, -29.7734375, -29.2421875, -25.375], 
    2180: [-51.7109375, -21.265625, -20.140625, -21.546875, -40.578125, -21.9296875, -21.8046875, -32.3359375, -28.1484375, -27.9921875], 
    2330: [-46.671875, -19.453125, -21.828125, -17.1015625, -36.1328125, -16.3203125, -21.515625, -33.984375, -20.8984375, -29.140625], 
    2500: [-43.28125, -23.5703125, -21.8984375, -19.1328125, -37.4375, -23.40625, -20.3828125, -39.0703125, -22.1875, -33.9609375], 
    2680: [-49.4609375, -21.7421875, -28.171875, -17.375, -33.6015625, -30.859375, -24.1484375, -39.78125, -22.328125, -37.859375], 
    2870: [-54.703125, -24.7578125, -31.921875, -19.7578125, -38.796875, -33.234375, -31.5, -39.484375, -31.6953125, -38.5078125], 
    3080: [-51.9765625, -26.296875, -32.9765625, -21.46875, -40.5078125, -30.78125, -32.90625, -39.4296875, -34.40625, -35.8046875], 
    3300: [-54.4609375, -16.5625, -30.53125, -15.7265625, -34.765625, -27.3359375, -36.0859375, -43.1640625, -32.359375, -30.609375], 
    3540: [-47.2890625, -18.5625, -32.5390625, -18.5703125, -37.6015625, -24.5, -29.40625, -34.9765625, -31.5859375, -23.4453125], 
    3790: [-48.4296875, -17.0859375, -34.7578125, -19.5390625, -38.5703125, -27.6171875, -34.65625, -40.140625, -31.109375, -27.96875], 
    4060: [-49.203125, -18.75, -29.7421875, -18.125, -37.1640625, -28.625, -30.7421875, -39.703125, -27.90625, -27.2421875], 
    4350: [-46.84375, -21.359375, -30.703125, -16.2265625, -35.265625, -29.734375, -28.4140625, -37.6640625, -25.0234375, -25.2421875], 
    4670: [-43.9609375, -18.4140625, -28.4609375, -17.3515625, -36.3828125, -29.6015625, -27.2734375, -39.4140625, -20.8828125, -28.90625], 
    5000: [-40.296875, -16.6171875, -25.3046875, -16.9765625, -36.015625, -27.390625, -25.9921875, -35.96875, -19.625, -26.375], 5360: [-47.9765625, -13.671875, -21.6953125, -13.0546875, -32.09375, -29.375, -25.671875, -40.71875, -21.7421875, -25.3203125], 5740: [-49.515625, -16.671875, -26.78125, -19.53125, -38.5703125, -28.515625, -27.546875, -43.7265625, -31.3671875, -27.34375], 6160: [-50.65625, -21.625, -23.8515625, -16.1875, -35.2265625, -28.15625, -30.2734375, -39.953125, -27.0234375, -28.40625], 6600: [-52.6484375, -16.703125, -26.5546875, -17.8515625, -36.8125, -28.9453125, -28.984375, -36.53125, -22.640625, -26.8984375], 7070: [-51.6953125, -14.953125, -22.703125, -19.2421875, -38.203125, -28.3515625, -27.03125, -42.109375, -27.7578125, -29.53125], 7580: [-48.046875, -24.5390625, -19.609375, -22.03125, -40.9921875, -30.5390625, -24.4921875, -43.5859375, -25.484375, -24.2109375], 8120: [-45.7265625, -21.984375, -18.3984375, -23.84375, -42.8046875, -30.1796875, -24.2578125, -43.3046875, -24.1484375, -24.0390625], 8710: [-49.28125, -24.390625, -17.578125, -20.671875, -39.6328125, -34.3046875, -25.90625, -41.1953125, -21.6796875, -23.875], 9330: [-50.515625, -21.6953125, -17.5390625, -22.171875, -41.1328125, -31.59375, -22.7734375, -42.6875, -29.265625, -26.7109375], 10000: [-50.578125, -19.4140625, -24.2578125, -22.5859375, -41.5546875, -30.59375, -29.265625, -46.3125, -30.3828125, -26.6875], 10720: [-52.8125, -25.2890625, -26.5546875, -24.6328125, -43.6015625, -30.8984375, -33.203125, -49.7265625, -35.140625, -31.5390625], 11490: [-61.6171875, -37.828125, -32.078125, -33.3828125, -52.3515625, -34.65625, -40.421875, -49.5, -40.484375, -40.0], 12310: [-66.3984375, -35.3203125, -36.34375, -31.2421875, -50.2109375, -36.0390625, -41.9921875, -49.7578125, -46.5, -43.703125], 13200: [-72.0625, -44.5234375, -44.125, -40.453125, -59.4296875, -45.546875, -46.7578125, -54.25, -51.109375, -50.4140625], 14140: [-76.921875, -49.765625, -53.28125, -45.703125, -64.671875, -49.09375, -55.953125, -55.5, -60.265625, -57.5], 15160: [-72.859375, -52.984375, -49.7265625, -51.6796875, -70.6484375, -53.0625, -61.578125, -66.296875, -61.703125, -65.1640625], 16250: [-75.46875, -62.765625, -60.8359375, -61.578125, -77.3984375, -58.9765625, -68.9296875, -65.8359375, -65.75, -67.9296875], 17410: [-76.25, -65.1015625, -63.1875, -63.484375, -77.734375, -65.671875, -69.296875, -64.0703125, -66.921875, -68.9609375], 18660: [-75.3203125, -63.9609375, -65.953125, -66.7265625, -76.453125, -67.3125, -70.6328125, -64.1796875, -67.1328125, -71.2734375]}

# Define band ranges
band_ranges = { # band_name: [(freq_id, freq), ...]
#    'LowCut': [(0.2600, 120.5)],
    'Low': [(0.2650, 124.7),        # 124.7 to 306.2
        (0.2700, 129.1),
        (0.2750, 133.7),
        (0.2800, 138.4),
        (0.2850, 143.2),
        (0.2900, 148.3),
        (0.2950, 153.5),
        (0.3000, 158.9),
        (0.3050, 164.4),
        (0.3100, 170.2),
        (0.3150, 176.2),
        (0.3200, 182.4),
        (0.3250, 188.8),
        (0.3300, 195.4),
        (0.3350, 202.3),
        (0.3400, 209.4),
        (0.3450, 216.8),
        (0.3500, 224.4),
        (0.3550, 232.3),
        (0.3600, 240.5),
        (0.3650, 248.9),
        (0.3700, 257.6),
        (0.3750, 266.7),
        (0.3800, 276.1),
        (0.3850, 285.8),
        (0.3900, 295.8),
        (0.3950, 306.2)],
    'Low Mid': [(0.4000, 317.0),    # 317.0 to 1055.0
        (0.4050, 328.1),
        (0.4100, 339.6),
        (0.4150, 351.6),
        (0.4200, 363.9),
        (0.4250, 376.7),
        (0.4300, 390.0),
        (0.4350, 403.7),
        (0.4400, 417.9),
        (0.4450, 432.5),
        (0.4500, 447.7),
        (0.4550, 463.5),
        (0.4600, 479.8),
        (0.4650, 496.6),
        (0.4700, 514.1),
        (0.4750, 532.1),
        (0.4800, 550.8),
        (0.4850, 570.2),
        (0.4900, 590.2),
        (0.4950, 611.0),
        (0.5000, 632.5),
        (0.5050, 654.7),
        (0.5100, 677.7),
        (0.5150, 701.5),
        (0.5200, 726.2),
        (0.5250, 751.7),
        (0.5300, 778.1),
        (0.5350, 805.4),
        (0.5400, 833.7),
        (0.5450, 863.0),
        (0.5500, 893.4),
        (0.5550, 924.8),
        (0.5600, 957.3),
        (0.5650, 990.9),
        (0.5700, 1002.0),
        (0.5750, 1006.0),
        (0.5800, 1009.0),
        (0.5850, 1013.0),
        (0.5900, 1017.0),
        (0.5950, 1021.0),
        (0.6000, 1026.0),
        (0.6050, 1030.0),
        (0.6100, 1035.0),
        (0.6150, 1039.0),
        (0.6200, 1044.0),
        (0.6250, 1049.0),
        (0.6300, 1055.0)],
    'High Mid': [(0.6350, 1600),    # 1600 to 5020
        (0.6400, 1660),
        (0.6450, 1720),
        (0.6500, 1780),
        (0.6550, 1840),
        (0.6600, 1910),
        (0.6650, 1970),
        (0.6700, 2040),
        (0.6750, 2110),
        (0.6800, 2190),
        (0.6850, 2270),
        (0.6900, 2340),
        (0.6950, 2430),
        (0.7000, 2510),
        (0.7050, 2600),
        (0.7100, 2690),
        (0.7150, 2790),
        (0.7200, 2890),
        (0.7250, 2990),
        (0.7300, 3090),
        (0.7350, 3200),
        (0.7400, 3310),
        (0.7450, 3430),
        (0.7500, 3550),
        (0.7550, 3680),
        (0.7600, 3810),
        (0.7650, 3940),
        (0.7700, 4080),
        (0.7750, 4220),
        (0.7800, 4370),
        (0.7850, 4520),
        (0.7900, 4680),
        (0.7950, 4850),
        (0.8000, 5020)],
    'High': [(0.8050, 5200),        # 5200 to 20000
        (0.8100, 5380),
        (0.8150, 5570),
        (0.8200, 5760),
        (0.8250, 5970),
        (0.8300, 6180),
        (0.8350, 6390),
        (0.8400, 6620),
        (0.8450, 6850),
        (0.8500, 7090),
        (0.8550, 7340),
        (0.8600, 7600),
        (0.8650, 7870),
        (0.8700, 8140),
        (0.8750, 8430),
        (0.8800, 8730),
        (0.8850, 9030),
        (0.8900, 9350),
        (0.8950, 9680),
        (0.9000, 10020),
        (0.9050, 10370),
        (0.9100, 10740),
        (0.9150, 11110),
        (0.9200, 11500),
        (0.9250, 11890),
        (0.9300, 12330),
        (0.9350, 12760),
        (0.9400, 13210),
        (0.9450, 13670),
        (0.9500, 14150),
        (0.9550, 14650),
        (0.9600, 15170),
        (0.9650, 15700),
        (0.9700, 16250),
        (0.9750, 16820),
        (0.9800, 17410),
        (0.9850, 18030),
        (0.9900, 18660),
        (0.9950, 19320),
        (1.0000, 20000)]
}

# hardcoded frequencies based on /meters/15 data
frequencies = [
    20, 21, 22, 24, 26, 28, 30, 32, 34, 36,
    39, 42, 45, 48, 52, 55, 59, 63, 68, 73,
    78, 84, 90, 96, 103, 110, 118, 127, 136, 146,
    156, 167, 179, 192, 206, 221, 237, 254, 272, 292,
    313, 335, 359, 385, 412, 442, 474, 508, 544, 583,
    625, 670, 718, 769, 825, 884, 947, 1020, 1090, 1170,
    1250, 1340, 1440, 1540, 1650, 1770, 1890, 2030, 2180, 2330,
    2500, 2680, 2870, 3080, 3300, 3540, 3790, 4060, 4350, 4670,
    5000, 5360, 5740, 6160, 6600, 7070, 7580, 8120, 8710, 9330,
    10000, 10720, 11490, 12310, 13200, 14140, 15160, 16250, 17410, 18660
]

q_values = {        # q_value:q_id      6.4 to 1.0
    6.4: 0.1268, 
    6.1: 0.1408, 
    5.8: 0.1549, 
    5.5: 0.1690,
    5.3: 0.1831,
    5.0: 0.1972,
    4.8: 0.2113,
    4.5: 0.2254,
    4.3: 0.2394,
    4.1: 0.2535,
    3.9: 0.2676,
    3.7: 0.2817,
    3.5: 0.2958,
    3.4: 0.3099,
    3.2: 0.3239,
    3.1: 0.3380,
    2.9: 0.3521,
    2.8: 0.3662,
    2.6: 0.3803,
    2.5: 0.3944,
    2.4: 0.4085,
    2.3: 0.4225,
    2.2: 0.4366,
    2.1: 0.4507,
    2.0: 0.4648,
    1.9: 0.4789,
    1.8: 0.4930,
    1.7: 0.5070,
    1.6: 0.5211,
    1.5: 0.5352,
    1.4: 0.5634,
    1.3: 0.5775,
    1.2: 0.6056,
    1.1: 0.6338,
    1.0: 0.6479
}

eqGainValues = {    # gain_value:gain_hexa                  -15.0 to 15.0
    -15.00: 'C1700000',
    -14.75: 'C16C0000',
    -14.50: 'C1680000',
    -14.25: 'C1640000',
    -14.00: 'C1600000',
    -13.75: 'C15C0000',
    -13.50: 'C1580000',
    -13.25: 'C1540000',
    -13.00: 'C1500000',
    -12.75: 'C14C0000',
    -12.50: 'C1480000',
    -12.25: 'C1440000',
    -12.00: 'C1400000',
    -11.75: 'C13C0000',
    -11.50: 'C1380000',
    -11.25: 'C1340000',
    -11.00: 'C1300000',
    -10.75: 'C12C0000',
    -10.50: 'C1280000',
    -10.25: 'C1240000',
    -10.00: 'C1200000',
    -9.75: 'C11C0000',
    -9.50: 'C1180000',
    -9.25: 'C1140000',
    -9.00: 'C1100000',
    -8.75: 'C10C0000',
    -8.50: 'C1080000',
    -8.25: 'C1040000',
    -8.00: 'C1000000',
    -7.75: 'C0F80000',
    -7.50: 'C0F00000',
    -7.25: 'C0E80000',
    -7.00: 'C0E00000',
    -6.75: 'C0D80000',
    -6.50: 'C0D00000',
    -6.25: 'C0C80000',
    -6.00: 'C0C00000',
    -5.75: 'C0B80000',
    -5.50: 'C0B00000',
    -5.25: 'C0A80000',
    -5.00: 'C0A00000',
    -4.75: 'C0980000',
    -4.50: 'C0900000',
    -4.25: 'C0880000',
    -4.00: 'C0800000',
    -3.75: 'C0700000',
    -3.50: 'C0600000',
    -3.25: 'C0500000',
    -3.00: 'C0400000',
    -2.75: 'C0300000',
    -2.50: 'C0200000',
    -2.25: 'C0100000',
    -2.00: 'C0000000',
    -1.75: 'BFE00000',
    -1.50: 'BFC00000',
    -1.25: 'BFA00000',
    -1.00: 'BF800000',
    -0.75: 'BF400000',
    -0.50: 'BF000000',
    -0.25: 'BE800000',
    0.00: '00000000',
    0.25: '3E800000',
    0.50: '3F000000',
    0.75: '3F400000',
    1.00: '3F800000',
    1.25: '3FA00000',
    1.50: '3FC00000',
    1.75: '3FE00000',
    2.00: '40000000',
    2.25: '40100000',
    2.50: '40200000',
    2.75: '40300000',
    3.00: '40400000',
    3.25: '40500000',
    3.50: '40600000',
    3.75: '40700000',
    4.00: '40800000',
    4.25: '40880000',
    4.50: '40900000',
    4.75: '40980000',
    5.00: '40A00000',
    5.25: '40A80000',
    5.50: '40B00000',
    5.75: '40B80000',
    6.00: '40C00000',
    6.25: '40C80000',
    6.50: '40D00000',
    6.75: '40D80000',
    7.00: '40E00000',
    7.25: '40E80000',
    7.50: '40F00000',
    7.75: '40F80000',
    8.00: '41000000',
    8.25: '41040000',
    8.50: '41080000',
    8.75: '410C0000',
    9.00: '41100000',
    9.25: '41140000',
    9.50: '41180000',
    9.75: '411C0000',
    10.00: '41200000',
    10.25: '41240000',
    10.50: '41280000',
    10.75: '412C0000',
    11.00: '41300000',
    11.25: '41340000',
    11.50: '41380000',
    11.75: '413C0000',
    12.00: '41400000',
    12.25: '41440000',
    12.50: '41480000',
    12.75: '414C0000',
    13.00: '41500000',
    13.25: '41540000',
    13.50: '41580000',
    13.75: '415C0000',
    14.00: '41600000',
    14.25: '41640000',
    14.50: '41680000',
    14.75: '416C0000',
    15.00: '41700000'
}

def has_sufficient_data(freq):
    """Check if there are at least 10 dB values for the frequency."""
    return len(dataRTA.get(freq, [])) >= 10

def find_highest_db_frequency_in_band(dataRTA, low, high):
    highest_db = float('-inf')
    highest_freq = None
    for freq, db_values in dataRTA.items():
        if low <= freq <= high:
            latest_db = max(db_values)
            if latest_db > highest_db:
                highest_db = latest_db
                highest_freq = freq
    return highest_freq, highest_db

def find_closest_frequency_in_band_ranges(band_ranges, target_freq):
    """Find the closest frequency in band_ranges to a given target frequency."""
    closest_freq = None
    closest_id = None
    min_diff = float('inf')
    for band, freqs in band_ranges.items():
        for freq_id, freq in freqs:
            diff = abs(float(freq) - float(target_freq))
            if diff < min_diff:
                min_diff = diff
                closest_freq = freq
                closest_id = freq_id
    return closest_id, closest_freq

def calculate_gain(db_value, band, vocal_type):
    """Calculate the gain for a given dB value, band, and vocal type."""
    freq_flat = -45  # Target dB level for flat response
    distance = db_value - freq_flat
    gain_multipliers = {
        'Low Pitch': {'Low': 1.0, 'Low Mid': 0.8, 'High Mid': 1.2, 'High': 1.2},
        'High Pitch': {'Low': 0.8, 'Low Mid': 0.7, 'High Mid': 0.6, 'High': 0.7},
        'Mid Pitch': {'Low': 0.9, 'Low Mid': 0.85, 'High Mid': 1.1, 'High': 0.9}
    }
    band_multiplier = gain_multipliers[vocal_type][band]
    gain = (distance / 10) * band_multiplier
    return round(gain, 2)

def calculate_q_value(band, freq):
    """Calculate the Q value based on adjacent frequencies, ensuring the highest dB frequency is considered."""
    if freq not in dataRTA:
        print(f"Frequency {freq} not found in dataRTA for band {band}")
        return None  # Early exit if the frequency data is not available

    frequencies = [f for _, f in band_ranges[band]]
    if freq not in frequencies:
        print(f"Selected frequency {freq} not found in {band} band range.")
        return None  # Return None if frequency is not in band ranges

    freq_index = frequencies.index(freq)
    # Ensure to check the existence of frequency in dataRTA and take the latest dB value
    freq_db_values = [dataRTA[f][-1] for f in frequencies if f in dataRTA]
    selected_db = dataRTA[freq][-1]
    min_q_value = 6.4
    max_q_value = 1.0
    band_size = len(freq_db_values)

    # Calculate adjacent values within 20 dB range of the highest dB value
    adjacent_values_count = sum(1 for db in freq_db_values[max(0, freq_index - 1): min(freq_index + 2, band_size)]
                                if selected_db - 20 <= db <= selected_db + 20)

    # Calculate the Q value, adjust based on the count of adjacent frequencies within 20 dB range
    q_value = min_q_value - (adjacent_values_count * ((min_q_value - max_q_value) / max(band_size, 1)))
    return q_value

def get_closest_q_osc_value(q_value):
    """Return the closest Q OSC float value from the dictionary based on the provided Q value."""
    if not q_values:  # Check if q_values is empty or undefined
        return None
    closest_q = min(q_values.keys(), key=lambda k: abs(k - q_value))
    return q_values[closest_q]

def get_closest_gain_hex(gain_value):
    """Return the closest gain hexadecimal value from the dictionary based on the provided gain value."""
    if not eqGainValues:  # Check if eqGainValues is empty or undefined
        return None
    closest_gain = min(eqGainValues.keys(), key=lambda k: abs(k - gain_value))
    return eqGainValues[closest_gain]

def get_valid_channel():
    while True:
        channel = input("Enter the channel number from 01 to 32: ")
        if channel.isdigit() and 1 <= int(channel) <= 32:
            return channel.zfill(2)  # Ensures the channel number is formatted with two digits
        else:
            print("Invalid input. Please enter a number from 01 to 32.")

def send_osc_combined_parameters(channel, eq_band, freq_id, gain_value, q_value):
    """Send OSC message with all EQ parameters in one command, using frequency id."""
    gain_hex = get_closest_gain_hex(gain_value)
    q_osc_value = get_closest_q_osc_value(q_value)
    client.send_message(f'/ch/{channel}/eq/{eq_band}', [2, freq_id, gain_hex, q_osc_value])
    print(f"Sent OSC message to /ch/{channel}/eq/{eq_band} with parameters: Type 2, Frequency ID {freq_id}, Gain {gain_hex}, Q {q_osc_value}")

def update_all_bands(vocal_type, channel):
    eq_band_numbers = {
        'Low': '1',
        'Low Mid': '2',
        'High Mid': '3',
        'High': '4'
    }

    for band_name, band_data in band_ranges.items():
        # Determine band limits from dataRTA for valid frequencies
        valid_freqs = [freq for freq in dataRTA if has_sufficient_data(freq)]
        band_freqs = [freq for freq in valid_freqs if any(low <= freq <= high for low, high in [(min(freq for _, freq in band_data), max(freq for _, freq in band_data))])]

        if band_freqs:
            # Find the frequency with the highest dB within these limits in dataRTA
            highest_freq, highest_db = max(((freq, max(dataRTA[freq])) for freq in band_freqs), key=lambda x: x[1], default=(None, float('-inf')))
            if highest_freq:
                # Generate sequence for closest frequency ID comparison
                closest_freq_data = [(abs(freq - highest_freq), osc) for osc, freq in band_data if freq in valid_freqs]
                if closest_freq_data:
                    # Find the closest frequency ID in band_ranges for the OSC message
                    _, closest_id = min(closest_freq_data)
                    gain = calculate_gain(highest_db, band_name, vocal_type)
                    q_value = calculate_q_value(band_name, highest_freq)
                    if q_value is not None:
                        gain_hex = get_closest_gain_hex(gain)
                        q_osc_value = get_closest_q_osc_value(q_value)
                        # Send OSC message
                        send_osc_combined_parameters(channel, eq_band_numbers[band_name], closest_id, gain_hex, q_osc_value)
                        print(f"Processed {band_name}: Frequency ID {closest_id}, Gain {gain_hex}, Q Value {q_osc_value}")



if __name__ == "__main__":
    print("Select the vocal type:")
    print("1. Low Pitch")
    print("2. High Pitch")
    print("3. Mid Pitch (Flat)")

    try:
        vocal_type_input = int(input("Enter the number for the desired vocal type: "))
        vocal_types = ['Low Pitch', 'High Pitch', 'Mid Pitch']
        vocal_type = vocal_types[vocal_type_input - 1]  # Adjust index for zero-based
    except (IndexError, ValueError):
        print("Invalid input. Defaulting to 'Mid Pitch (Flat)'.")
        vocal_type = 'Mid Pitch'

    channel = get_valid_channel()  # Get a valid channel number

    while True:
        update_all_bands(vocal_type, channel)
        time.sleep(1)  # Adjustable based on system capabilities and needs