class DisplayUnitType(Enum, IComparable, IFormattable, IConvertible):
    """
    The units and display format used to format numbers as strings.  Also used for unit conversions.
    
    enum DisplayUnitType, values: DUT_1_RATIO (182), DUT_ACRES (7), DUT_AMPERES (69), DUT_ATMOSPHERES (54), DUT_BARS (55), DUT_BRITISH_THERMAL_UNIT_PER_FAHRENHEIT (186), DUT_BRITISH_THERMAL_UNITS (31), DUT_BRITISH_THERMAL_UNITS_PER_HOUR (42), DUT_BRITISH_THERMAL_UNITS_PER_HOUR_CUBIC_FOOT (167), DUT_BRITISH_THERMAL_UNITS_PER_HOUR_FOOT_FAHRENHEIT (231), DUT_BRITISH_THERMAL_UNITS_PER_HOUR_SQUARE_FOOT (166), DUT_BRITISH_THERMAL_UNITS_PER_HOUR_SQUARE_FOOT_FAHRENHEIT (155), DUT_BRITISH_THERMAL_UNITS_PER_POUND (233), DUT_BRITISH_THERMAL_UNITS_PER_POUND_FAHRENHEIT (232), DUT_BRITISH_THERMAL_UNITS_PER_SECOND (41), DUT_CALORIES (32), DUT_CALORIES_PER_SECOND (43), DUT_CANDELAS (81), DUT_CANDELAS_PER_SQUARE_METER (80), DUT_CANDLEPOWER (82), DUT_CELSIUS (57), DUT_CELSIUS_DIFFERENCE (244), DUT_CENTIMETERS (1), DUT_CENTIMETERS_PER_MINUTE (62), DUT_CENTIMETERS_TO_THE_FOURTH_POWER (200), DUT_CENTIMETERS_TO_THE_SIXTH_POWER (205), DUT_CENTIPOISES (131), DUT_CUBIC_CENTIMETERS (24), DUT_CUBIC_FEET (13), DUT_CUBIC_FEET_PER_KIP (124), DUT_CUBIC_FEET_PER_MINUTE (63), DUT_CUBIC_FEET_PER_MINUTE_CUBIC_FOOT (169), DUT_CUBIC_FEET_PER_MINUTE_SQUARE_FOOT (156), DUT_CUBIC_FEET_PER_MINUTE_TON_OF_REFRIGERATION (171), DUT_CUBIC_INCHES (23), DUT_CUBIC_METERS (14), DUT_CUBIC_METERS_PER_HOUR (66), DUT_CUBIC_METERS_PER_KILONEWTON (123), DUT_CUBIC_METERS_PER_SECOND (65), DUT_CUBIC_MILLIMETERS (25), DUT_CUBIC_YARDS (10), DUT_CURRENCY (175), DUT_CUSTOM (-1), DUT_CYCLES_PER_SECOND (76), DUT_DECANEWTON_METERS (112), DUT_DECANEWTON_METERS_PER_METER (140), DUT_DECANEWTONS (88), DUT_DECANEWTONS_PER_METER (96), DUT_DECANEWTONS_PER_SQUARE_METER (104), DUT_DECIMAL_DEGREES (15), DUT_DECIMAL_FEET (3), DUT_DECIMAL_INCHES (6), DUT_DECIMETERS (236), DUT_DEGREES_AND_MINUTES (16), DUT_FAHRENHEIT (56), DUT_FAHRENHEIT_DIFFERENCE (243), DUT_FEET_FRACTIONAL_INCHES (4), DUT_FEET_OF_WATER (128), DUT_FEET_OF_WATER_PER_100FT (127), DUT_FEET_PER_KIP (120), DUT_FEET_PER_MINUTE (60), DUT_FEET_PER_SECOND (132), DUT_FEET_PER_SECOND_SQUARED (195), DUT_FEET_TO_THE_FOURTH_POWER (197), DUT_FEET_TO_THE_SIXTH_POWER (202), DUT_FIXED (18), DUT_FOOTCANDLES (78), DUT_FOOTLAMBERTS (79), DUT_FRACTIONAL_INCHES (5), DUT_GALLONS_US (27), DUT_GALLONS_US_PER_HOUR (68), DUT_GALLONS_US_PER_MINUTE (67), DUT_GENERAL (17), DUT_GRADS (215), DUT_GRAINS_PER_HOUR_SQUARE_FOOT_INCH_MERCURY (234), DUT_HECTARES (8), DUT_HERTZ (75), DUT_HORSEPOWER (86), DUT_HOUR_SQUARE_FOOT_FAHRENHEIT_PER_BRITISH_THERMAL_UNIT (184), DUT_HOURS (220), DUT_INCHES_OF_MERCURY (52), DUT_INCHES_OF_WATER (47), DUT_INCHES_OF_WATER_PER_100FT (37), DUT_INCHES_PER_SECOND_SQUARED (194), DUT_INCHES_TO_THE_FOURTH_POWER (198), DUT_INCHES_TO_THE_SIXTH_POWER (203), DUT_INV_CELSIUS (138), DUT_INV_FAHRENHEIT (137), DUT_INV_KILONEWTONS (125), DUT_INV_KIPS (126), DUT_JOULES (34), DUT_JOULES_PER_GRAM (228), DUT_JOULES_PER_GRAM_CELSIUS (227), DUT_JOULES_PER_KELVIN (187), DUT_JOULES_PER_KILOGRAM_CELSIUS (237), DUT_KELVIN (58), DUT_KELVIN_DIFFERENCE (245), DUT_KILOAMPERES (70), DUT_KILOCALORIES (33), DUT_KILOCALORIES_PER_SECOND (44), DUT_KILOGRAM_FORCE_METERS (116), DUT_KILOGRAM_FORCE_METERS_PER_METER (144), DUT_KILOGRAMS_FORCE (92), DUT_KILOGRAMS_FORCE_PER_METER (100), DUT_KILOGRAMS_FORCE_PER_SQUARE_METER (108), DUT_KILOGRAMS_MASS (189), DUT_KILOGRAMS_MASS_PER_METER (212), DUT_KILOGRAMS_MASS_PER_SQUARE_METER (224), DUT_KILOGRAMS_PER_CUBIC_METER (28), DUT_KILOJOULES (223), DUT_KILOJOULES_PER_KELVIN (188), DUT_KILOMETERS_PER_HOUR (221), DUT_KILOMETERS_PER_SECOND_SQUARED (193), DUT_KILONEWTON_METERS (113), DUT_KILONEWTON_METERS_PER_DEGREE (151), DUT_KILONEWTON_METERS_PER_DEGREE_PER_METER (153), DUT_KILONEWTON_METERS_PER_METER (141), DUT_KILONEWTONS (89), DUT_KILONEWTONS_PER_CUBIC_METER (134), DUT_KILONEWTONS_PER_METER (97), DUT_KILONEWTONS_PER_SQUARE_CENTIMETER (178), DUT_KILONEWTONS_PER_SQUARE_METER (105), DUT_KILONEWTONS_PER_SQUARE_MILLIMETER (180), DUT_KILOPASCALS (49), DUT_KILOVOLT_AMPERES (85), DUT_KILOVOLTS (73), DUT_KILOWATT_HOURS (35), DUT_KILOWATTS (40), DUT_KIP_FEET (115), DUT_KIP_FEET_PER_DEGREE (150), DUT_KIP_FEET_PER_DEGREE_PER_FOOT (152), DUT_KIP_FEET_PER_FOOT (143), DUT_KIPS (91), DUT_KIPS_PER_CUBIC_FOOT (149), DUT_KIPS_PER_CUBIC_INCH (136), DUT_KIPS_PER_FOOT (99), DUT_KIPS_PER_INCH (148), DUT_KIPS_PER_SQUARE_FOOT (107), DUT_KIPS_PER_SQUARE_INCH (133), DUT_LITERS (26), DUT_LITERS_PER_MINUTE (242), DUT_LITERS_PER_SECOND (64), DUT_LITERS_PER_SECOND_CUBIC_METER (170), DUT_LITERS_PER_SECOND_KILOWATTS (172), DUT_LITERS_PER_SECOND_SQUARE_METER (157), DUT_LUMENS (83), DUT_LUMENS_PER_WATT (176), DUT_LUX (77), DUT_MEGANEWTON_METERS (114), DUT_MEGANEWTON_METERS_PER_METER (142), DUT_MEGANEWTONS (90), DUT_MEGANEWTONS_PER_METER (98), DUT_MEGANEWTONS_PER_SQUARE_METER (106), DUT_MEGAPASCALS (50), DUT_METERS (0), DUT_METERS_CENTIMETERS (9), DUT_METERS_PER_KILONEWTON (119), DUT_METERS_PER_SECOND (61), DUT_METERS_PER_SECOND_SQUARED (192), DUT_METERS_TO_THE_FOURTH_POWER (201), DUT_METERS_TO_THE_SIXTH_POWER (206), DUT_MICROINCHES_PER_INCH_FAHRENHEIT (239), DUT_MICROMETERS_PER_METER_CELSIUS (238), DUT_MILES_PER_HOUR (222), DUT_MILES_PER_SECOND_SQUARED (196), DUT_MILISECONDS (217), DUT_MILLIAMPERES (71), DUT_MILLIMETERS (2), DUT_MILLIMETERS_OF_MERCURY (53), DUT_MILLIMETERS_TO_THE_FOURTH_POWER (199), DUT_MILLIMETERS_TO_THE_SIXTH_POWER (204), DUT_MILLIVOLTS (74), DUT_MINUTES (219), DUT_NANOGRAMS_PER_PASCAL_SECOND_SQUARE_METER (229), DUT_NEWTON_METERS (111), DUT_NEWTON_METERS_PER_METER (139), DUT_NEWTONS (87), DUT_NEWTONS_PER_METER (95), DUT_NEWTONS_PER_SQUARE_METER (103), DUT_NEWTONS_PER_SQUARE_MILLIMETER (179), DUT_OHM_METERS (230), DUT_PASCAL_SECONDS (129), DUT_PASCALS (48), DUT_PASCALS_PER_METER (38), DUT_PER_MILLE (235), DUT_PERCENTAGE (19), DUT_POUND_FORCE_FEET (118), DUT_POUND_FORCE_FEET_PER_FOOT (146), DUT_POUNDS_FORCE (94), DUT_POUNDS_FORCE_PER_CUBIC_FOOT (135), DUT_POUNDS_FORCE_PER_FOOT (102), DUT_POUNDS_FORCE_PER_SQUARE_FOOT (110), DUT_POUNDS_FORCE_PER_SQUARE_INCH (51), DUT_POUNDS_MASS (191), DUT_POUNDS_MASS_PER_CUBIC_FOOT (29), DUT_POUNDS_MASS_PER_CUBIC_INCH (30), DUT_POUNDS_MASS_PER_FOOT (213), DUT_POUNDS_MASS_PER_FOOT_HOUR (147), DUT_POUNDS_MASS_PER_FOOT_SECOND (130), DUT_POUNDS_MASS_PER_SQUARE_FOOT (225), DUT_RADIANS (214), DUT_RADIANS_PER_SECOND (216), DUT_RANKINE (59), DUT_RANKINE_DIFFERENCE (246), DUT_RATIO_10 (158), DUT_RATIO_12 (159), DUT_RISE_OVER_10_FEET (183), DUT_RISE_OVER_120_INCHES (181), DUT_RISE_OVER_FOOT (162), DUT_RISE_OVER_INCHES (161), DUT_RISE_OVER_MMS (163), DUT_SECONDS (218), DUT_SLOPE_DEGREES (160), DUT_SQUARE_CENTIMETERS (21), DUT_SQUARE_CENTIMETERS_PER_METER (210), DUT_SQUARE_FEET (11), DUT_SQUARE_FEET_PER_FOOT (207), DUT_SQUARE_FEET_PER_KIP (122), DUT_SQUARE_FEET_PER_THOUSAND_BRITISH_THERMAL_UNITS_PER_HOUR (177), DUT_SQUARE_FEET_PER_TON_OF_REFRIGERATION (173), DUT_SQUARE_INCHES (20), DUT_SQUARE_INCHES_PER_FOOT (208), DUT_SQUARE_METER_KELVIN_PER_WATT (185), DUT_SQUARE_METERS (12), DUT_SQUARE_METERS_PER_KILONEWTON (121), DUT_SQUARE_METERS_PER_KILOWATTS (174), DUT_SQUARE_METERS_PER_METER (211), DUT_SQUARE_MILLIMETERS (22), DUT_SQUARE_MILLIMETERS_PER_METER (209), DUT_THERMS (36), DUT_TON_OF_REFRIGERATION (168), DUT_TONNE_FORCE_METERS (117), DUT_TONNE_FORCE_METERS_PER_METER (145), DUT_TONNES_FORCE (93), DUT_TONNES_FORCE_PER_METER (101), DUT_TONNES_FORCE_PER_SQUARE_METER (109), DUT_TONNES_MASS (190), DUT_UNDEFINED (-2), DUT_USTONNES_FORCE (241), DUT_USTONNES_MASS (240), DUT_VOLT_AMPERES (84), DUT_VOLTS (72), DUT_WATTS (39), DUT_WATTS_PER_CUBIC_FOOT (164), DUT_WATTS_PER_CUBIC_METER (165), DUT_WATTS_PER_METER_KELVIN (226), DUT_WATTS_PER_SQUARE_FOOT (45), DUT_WATTS_PER_SQUARE_METER (46), DUT_WATTS_PER_SQUARE_METER_KELVIN (154)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DUT_1_RATIO = None
    DUT_ACRES = None
    DUT_AMPERES = None
    DUT_ATMOSPHERES = None
    DUT_BARS = None
    DUT_BRITISH_THERMAL_UNITS = None
    DUT_BRITISH_THERMAL_UNITS_PER_HOUR = None
    DUT_BRITISH_THERMAL_UNITS_PER_HOUR_CUBIC_FOOT = None
    DUT_BRITISH_THERMAL_UNITS_PER_HOUR_FOOT_FAHRENHEIT = None
    DUT_BRITISH_THERMAL_UNITS_PER_HOUR_SQUARE_FOOT = None
    DUT_BRITISH_THERMAL_UNITS_PER_HOUR_SQUARE_FOOT_FAHRENHEIT = None
    DUT_BRITISH_THERMAL_UNITS_PER_POUND = None
    DUT_BRITISH_THERMAL_UNITS_PER_POUND_FAHRENHEIT = None
    DUT_BRITISH_THERMAL_UNITS_PER_SECOND = None
    DUT_BRITISH_THERMAL_UNIT_PER_FAHRENHEIT = None
    DUT_CALORIES = None
    DUT_CALORIES_PER_SECOND = None
    DUT_CANDELAS = None
    DUT_CANDELAS_PER_SQUARE_METER = None
    DUT_CANDLEPOWER = None
    DUT_CELSIUS = None
    DUT_CELSIUS_DIFFERENCE = None
    DUT_CENTIMETERS = None
    DUT_CENTIMETERS_PER_MINUTE = None
    DUT_CENTIMETERS_TO_THE_FOURTH_POWER = None
    DUT_CENTIMETERS_TO_THE_SIXTH_POWER = None
    DUT_CENTIPOISES = None
    DUT_CUBIC_CENTIMETERS = None
    DUT_CUBIC_FEET = None
    DUT_CUBIC_FEET_PER_KIP = None
    DUT_CUBIC_FEET_PER_MINUTE = None
    DUT_CUBIC_FEET_PER_MINUTE_CUBIC_FOOT = None
    DUT_CUBIC_FEET_PER_MINUTE_SQUARE_FOOT = None
    DUT_CUBIC_FEET_PER_MINUTE_TON_OF_REFRIGERATION = None
    DUT_CUBIC_INCHES = None
    DUT_CUBIC_METERS = None
    DUT_CUBIC_METERS_PER_HOUR = None
    DUT_CUBIC_METERS_PER_KILONEWTON = None
    DUT_CUBIC_METERS_PER_SECOND = None
    DUT_CUBIC_MILLIMETERS = None
    DUT_CUBIC_YARDS = None
    DUT_CURRENCY = None
    DUT_CUSTOM = None
    DUT_CYCLES_PER_SECOND = None
    DUT_DECANEWTONS = None
    DUT_DECANEWTONS_PER_METER = None
    DUT_DECANEWTONS_PER_SQUARE_METER = None
    DUT_DECANEWTON_METERS = None
    DUT_DECANEWTON_METERS_PER_METER = None
    DUT_DECIMAL_DEGREES = None
    DUT_DECIMAL_FEET = None
    DUT_DECIMAL_INCHES = None
    DUT_DECIMETERS = None
    DUT_DEGREES_AND_MINUTES = None
    DUT_FAHRENHEIT = None
    DUT_FAHRENHEIT_DIFFERENCE = None
    DUT_FEET_FRACTIONAL_INCHES = None
    DUT_FEET_OF_WATER = None
    DUT_FEET_OF_WATER_PER_100FT = None
    DUT_FEET_PER_KIP = None
    DUT_FEET_PER_MINUTE = None
    DUT_FEET_PER_SECOND = None
    DUT_FEET_PER_SECOND_SQUARED = None
    DUT_FEET_TO_THE_FOURTH_POWER = None
    DUT_FEET_TO_THE_SIXTH_POWER = None
    DUT_FIXED = None
    DUT_FOOTCANDLES = None
    DUT_FOOTLAMBERTS = None
    DUT_FRACTIONAL_INCHES = None
    DUT_GALLONS_US = None
    DUT_GALLONS_US_PER_HOUR = None
    DUT_GALLONS_US_PER_MINUTE = None
    DUT_GENERAL = None
    DUT_GRADS = None
    DUT_GRAINS_PER_HOUR_SQUARE_FOOT_INCH_MERCURY = None
    DUT_HECTARES = None
    DUT_HERTZ = None
    DUT_HORSEPOWER = None
    DUT_HOURS = None
    DUT_HOUR_SQUARE_FOOT_FAHRENHEIT_PER_BRITISH_THERMAL_UNIT = None
    DUT_INCHES_OF_MERCURY = None
    DUT_INCHES_OF_WATER = None
    DUT_INCHES_OF_WATER_PER_100FT = None
    DUT_INCHES_PER_SECOND_SQUARED = None
    DUT_INCHES_TO_THE_FOURTH_POWER = None
    DUT_INCHES_TO_THE_SIXTH_POWER = None
    DUT_INV_CELSIUS = None
    DUT_INV_FAHRENHEIT = None
    DUT_INV_KILONEWTONS = None
    DUT_INV_KIPS = None
    DUT_JOULES = None
    DUT_JOULES_PER_GRAM = None
    DUT_JOULES_PER_GRAM_CELSIUS = None
    DUT_JOULES_PER_KELVIN = None
    DUT_JOULES_PER_KILOGRAM_CELSIUS = None
    DUT_KELVIN = None
    DUT_KELVIN_DIFFERENCE = None
    DUT_KILOAMPERES = None
    DUT_KILOCALORIES = None
    DUT_KILOCALORIES_PER_SECOND = None
    DUT_KILOGRAMS_FORCE = None
    DUT_KILOGRAMS_FORCE_PER_METER = None
    DUT_KILOGRAMS_FORCE_PER_SQUARE_METER = None
    DUT_KILOGRAMS_MASS = None
    DUT_KILOGRAMS_MASS_PER_METER = None
    DUT_KILOGRAMS_MASS_PER_SQUARE_METER = None
    DUT_KILOGRAMS_PER_CUBIC_METER = None
    DUT_KILOGRAM_FORCE_METERS = None
    DUT_KILOGRAM_FORCE_METERS_PER_METER = None
    DUT_KILOJOULES = None
    DUT_KILOJOULES_PER_KELVIN = None
    DUT_KILOMETERS_PER_HOUR = None
    DUT_KILOMETERS_PER_SECOND_SQUARED = None
    DUT_KILONEWTONS = None
    DUT_KILONEWTONS_PER_CUBIC_METER = None
    DUT_KILONEWTONS_PER_METER = None
    DUT_KILONEWTONS_PER_SQUARE_CENTIMETER = None
    DUT_KILONEWTONS_PER_SQUARE_METER = None
    DUT_KILONEWTONS_PER_SQUARE_MILLIMETER = None
    DUT_KILONEWTON_METERS = None
    DUT_KILONEWTON_METERS_PER_DEGREE = None
    DUT_KILONEWTON_METERS_PER_DEGREE_PER_METER = None
    DUT_KILONEWTON_METERS_PER_METER = None
    DUT_KILOPASCALS = None
    DUT_KILOVOLTS = None
    DUT_KILOVOLT_AMPERES = None
    DUT_KILOWATTS = None
    DUT_KILOWATT_HOURS = None
    DUT_KIPS = None
    DUT_KIPS_PER_CUBIC_FOOT = None
    DUT_KIPS_PER_CUBIC_INCH = None
    DUT_KIPS_PER_FOOT = None
    DUT_KIPS_PER_INCH = None
    DUT_KIPS_PER_SQUARE_FOOT = None
    DUT_KIPS_PER_SQUARE_INCH = None
    DUT_KIP_FEET = None
    DUT_KIP_FEET_PER_DEGREE = None
    DUT_KIP_FEET_PER_DEGREE_PER_FOOT = None
    DUT_KIP_FEET_PER_FOOT = None
    DUT_LITERS = None
    DUT_LITERS_PER_MINUTE = None
    DUT_LITERS_PER_SECOND = None
    DUT_LITERS_PER_SECOND_CUBIC_METER = None
    DUT_LITERS_PER_SECOND_KILOWATTS = None
    DUT_LITERS_PER_SECOND_SQUARE_METER = None
    DUT_LUMENS = None
    DUT_LUMENS_PER_WATT = None
    DUT_LUX = None
    DUT_MEGANEWTONS = None
    DUT_MEGANEWTONS_PER_METER = None
    DUT_MEGANEWTONS_PER_SQUARE_METER = None
    DUT_MEGANEWTON_METERS = None
    DUT_MEGANEWTON_METERS_PER_METER = None
    DUT_MEGAPASCALS = None
    DUT_METERS = None
    DUT_METERS_CENTIMETERS = None
    DUT_METERS_PER_KILONEWTON = None
    DUT_METERS_PER_SECOND = None
    DUT_METERS_PER_SECOND_SQUARED = None
    DUT_METERS_TO_THE_FOURTH_POWER = None
    DUT_METERS_TO_THE_SIXTH_POWER = None
    DUT_MICROINCHES_PER_INCH_FAHRENHEIT = None
    DUT_MICROMETERS_PER_METER_CELSIUS = None
    DUT_MILES_PER_HOUR = None
    DUT_MILES_PER_SECOND_SQUARED = None
    DUT_MILISECONDS = None
    DUT_MILLIAMPERES = None
    DUT_MILLIMETERS = None
    DUT_MILLIMETERS_OF_MERCURY = None
    DUT_MILLIMETERS_TO_THE_FOURTH_POWER = None
    DUT_MILLIMETERS_TO_THE_SIXTH_POWER = None
    DUT_MILLIVOLTS = None
    DUT_MINUTES = None
    DUT_NANOGRAMS_PER_PASCAL_SECOND_SQUARE_METER = None
    DUT_NEWTONS = None
    DUT_NEWTONS_PER_METER = None
    DUT_NEWTONS_PER_SQUARE_METER = None
    DUT_NEWTONS_PER_SQUARE_MILLIMETER = None
    DUT_NEWTON_METERS = None
    DUT_NEWTON_METERS_PER_METER = None
    DUT_OHM_METERS = None
    DUT_PASCALS = None
    DUT_PASCALS_PER_METER = None
    DUT_PASCAL_SECONDS = None
    DUT_PERCENTAGE = None
    DUT_PER_MILLE = None
    DUT_POUNDS_FORCE = None
    DUT_POUNDS_FORCE_PER_CUBIC_FOOT = None
    DUT_POUNDS_FORCE_PER_FOOT = None
    DUT_POUNDS_FORCE_PER_SQUARE_FOOT = None
    DUT_POUNDS_FORCE_PER_SQUARE_INCH = None
    DUT_POUNDS_MASS = None
    DUT_POUNDS_MASS_PER_CUBIC_FOOT = None
    DUT_POUNDS_MASS_PER_CUBIC_INCH = None
    DUT_POUNDS_MASS_PER_FOOT = None
    DUT_POUNDS_MASS_PER_FOOT_HOUR = None
    DUT_POUNDS_MASS_PER_FOOT_SECOND = None
    DUT_POUNDS_MASS_PER_SQUARE_FOOT = None
    DUT_POUND_FORCE_FEET = None
    DUT_POUND_FORCE_FEET_PER_FOOT = None
    DUT_RADIANS = None
    DUT_RADIANS_PER_SECOND = None
    DUT_RANKINE = None
    DUT_RANKINE_DIFFERENCE = None
    DUT_RATIO_10 = None
    DUT_RATIO_12 = None
    DUT_RISE_OVER_10_FEET = None
    DUT_RISE_OVER_120_INCHES = None
    DUT_RISE_OVER_FOOT = None
    DUT_RISE_OVER_INCHES = None
    DUT_RISE_OVER_MMS = None
    DUT_SECONDS = None
    DUT_SLOPE_DEGREES = None
    DUT_SQUARE_CENTIMETERS = None
    DUT_SQUARE_CENTIMETERS_PER_METER = None
    DUT_SQUARE_FEET = None
    DUT_SQUARE_FEET_PER_FOOT = None
    DUT_SQUARE_FEET_PER_KIP = None
    DUT_SQUARE_FEET_PER_THOUSAND_BRITISH_THERMAL_UNITS_PER_HOUR = None
    DUT_SQUARE_FEET_PER_TON_OF_REFRIGERATION = None
    DUT_SQUARE_INCHES = None
    DUT_SQUARE_INCHES_PER_FOOT = None
    DUT_SQUARE_METERS = None
    DUT_SQUARE_METERS_PER_KILONEWTON = None
    DUT_SQUARE_METERS_PER_KILOWATTS = None
    DUT_SQUARE_METERS_PER_METER = None
    DUT_SQUARE_METER_KELVIN_PER_WATT = None
    DUT_SQUARE_MILLIMETERS = None
    DUT_SQUARE_MILLIMETERS_PER_METER = None
    DUT_THERMS = None
    DUT_TONNES_FORCE = None
    DUT_TONNES_FORCE_PER_METER = None
    DUT_TONNES_FORCE_PER_SQUARE_METER = None
    DUT_TONNES_MASS = None
    DUT_TONNE_FORCE_METERS = None
    DUT_TONNE_FORCE_METERS_PER_METER = None
    DUT_TON_OF_REFRIGERATION = None
    DUT_UNDEFINED = None
    DUT_USTONNES_FORCE = None
    DUT_USTONNES_MASS = None
    DUT_VOLTS = None
    DUT_VOLT_AMPERES = None
    DUT_WATTS = None
    DUT_WATTS_PER_CUBIC_FOOT = None
    DUT_WATTS_PER_CUBIC_METER = None
    DUT_WATTS_PER_METER_KELVIN = None
    DUT_WATTS_PER_SQUARE_FOOT = None
    DUT_WATTS_PER_SQUARE_METER = None
    DUT_WATTS_PER_SQUARE_METER_KELVIN = None
    value__ = None
