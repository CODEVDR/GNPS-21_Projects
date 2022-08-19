one_kg_in_tonnes = 0.001
one_kg_in_pound = 2.20462

def  kgtotonne( x ):
    "Return value in tonne from kilogram"
    return x * one_kg_in_tonnes

def tonnetokg( x ) :
    "Return value in kilogram from tonnes"
    return x / one_kg_in_tonnes
def  kgtopound ( x ):
    "Return value pound from kilogram"
    return x * one_kg_in_pound

def  poundtokg( x ) :
    "Return value kilogram from pound"
    return x / one_kg_in_pound