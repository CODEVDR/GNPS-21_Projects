one_mile_in_km = 1.609344
one_feet_in_inche = 12


def miletokm(x):
    "Return value in kilometer from miles "
    return x * one_mile_in_km


def kmtomile(x):
    "Return value in miles from kilometer "
    return x / one_mile_in_km


def feettoinches(x):
    "Return value in inches from feet "
    return x / one_feet_in_inche


def inchestofeet(x):
    "Return value in feet from inches "
    return x * one_feet_in_inche
