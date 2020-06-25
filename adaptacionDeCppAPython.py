# float rumb_a_wp, diferAbs_rumbRef_magVar, errorAbs, error, penellGlobal, diferAbs_wp_v,
# difer_wp_v, rumbRef, wpop, vent_op, diferAbs_wpop_v, difer_wpop_v, magVar, difer_magVar_vop, diferAbs_magVar_vop;

# unsigned long temps;


import math


def funcioPenell():
    return 90


def courseTo(lat1, long1, lat2, long2):
    dlong = math.radians(long2 - long1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    a1 = math.sin(dlong) * math.cos(lat2)
    a2 = math.sin(lat1) * math.cos(lat2) * math.cos(dlong)
    a2 = math.cos(lat1) * math.sin(lat2) - a2
    a2 = math.atan2(a1, a2)
    if (a2 < 0.0):
        a2 += (math.pi * 2)

    return math.degrees(a2)


currentLat = 10000000000.0
currentLong = 10000000000.0

penellGlobal = 90

rumb_a_wp = courseTo(currentLat,currentLong,10000000.0,100000000000.0)

# calculo de differ_wp_v

# Magnitud de difer_wp_v
diferAbs_wp_v = abs(rumb_a_wp - penellGlobal)

if (diferAbs_wp_v < 180):
    diferAbs_wp_v = diferAbs_wp_v
else:
    diferAbs_wp_v = 360 - diferAbs_wp_v
# Signo de difer_wp_v
if (rumb_a_wp >= 180):
    if ((rumb_a_wp - 180) < penellGlobal) and (penellGlobal < rumb_a_wp):
        difer_wp_v = diferAbs_wp_v
    else:
        difer_wp_v = - diferAbs_wp_v
else:
    if ((rumb_a_wp + 180) > penellGlobal) and (penellGlobal > rumb_a_wp):
        difer_wp_v = - diferAbs_wp_v
    else:
        difer_wp_v = diferAbs_wp_v

# Cálculo de valores opuestos para cálculos posteriores
if (rumb_a_wp < 180):
    wpop = rumb_a_wp + 180
else:
    wpop = rumb_a_wp - 180

if (penellGlobal < 180):
    vent_op = penellGlobal + 180
else:
    vent_op = penellGlobal - 180

# Calculo de difer_wpop_v
# Magnitud de difer_wpop_v
diferAbs_wpop_v = abs(wpop - penellGlobal)

if (diferAbs_wpop_v < 180):
    diferAbs_wpop_v = diferAbs_wpop_v
else:
    diferAbs_wpop_v = 360 - diferAbs_wpop_v

# Signo de difer_wpop_v
if (wpop >= 180):
    if ((wpop - 180) < penellGlobal) and (penellGlobal < wpop):
        diferAbs_wpop_v = diferAbs_wpop_v
    else:
        diferAbs_wpop_v = - diferAbs_wpop_v
else:
    if ((wpop + 180) > penellGlobal) and (penellGlobal > wpop):
        diferAbs_wpop_v = - diferAbs_wpop_v
    else:
        diferAbs_wpop_v = diferAbs_wpop_v

# Eleccion del rumb referencia
if (difer_wp_v > 0) and (difer_wp_v < 45):
    rumbRef = penellGlobal + 45
elif ((difer_wp_v <= 0) and (difer_wp_v > -45)):
    rumbRef = penellGlobal - 45
else:
    if ((difer_wpop_v > 0) and (difer_wpop_v < 20)):
        rumbRef += 20
    elif ((difer_wpop_v <= 0) and (difer_wpop_v > -20)):
        rumbRef += -20
    else:
        rumbRef = rumb_a_wp

if (rumbRef >= 360):
    rumbRef = rumbRef - 360
elif (rumbRef < 0):
    rumbRef = 360 + rumbRef

# Calculo del error
# Magnitud del error
diferAbs_rumbRef_magVar = abs(rumbRef - magVar);
if (diferAbs_rumbRef_magVar < 180):
    errorAbs = diferAbs_rumbRef_magVar
else:
    errorAbs = 360 - diferAbs_rumbRef_magVar
# Signo del error
if (rumbRef >= 180):
    if ((rumbRef - 180 < magVar) and (magVar < rumbRef)):
        error = errorAbs
    else:
        error = - errorAbs

else:
    if ((rumbRef + 180 > magVar) and (magVar > rumbRef)):
        error = - errorAbs
    else:
        error = errorAbs

# Càlcul de difer_magVar_vop

# (Magnitud de difer_magVar_vop)
diferAbs_magVar_vop = abs(magVar - vent_op);
if (diferAbs_magVar_vop < 180):
    diferAbs_magVar_vop = diferAbs_magVar_vop
else:
    diferAbs_magVar_vop = 360 - diferAbs_magVar_vop

# (Signe de difer_magVar_vop)
if (magVar >= 180):
    if ((magVar - 180 < vent_op) and (vent_op < magVar)):
        difer_magVar_vop = diferAbs_magVar_vop
    else:
        difer_magVar_vop = - diferAbs_magVar_vop
else:
    if ((magVar + 180 > vent_op) and (vent_op > magVar)):
        difer_magVar_vop = - diferAbs_magVar_vop
    else:
        difer_magVar_vop = diferAbs_magVar_vop

thetaB, thetaE = 0
# A) Situació on el gir cap al waypoint NO implica una virada per popa (cas desitjat)
if (errorAbs < diferAbs_magVar_vop):
    if (errorAbs > 45):
        thetaE = 101 + 45
        thetaB = 105 + 45
    elif (error < -45):
        thetaE = 101 - 45
        thetaE = 105 - 45
    else:
        thetaE = 101 + error
        thetaB = 105 + error

    case = 'A'

# B) Situació on el gir cap al waypoint SÍ que implica una virada per popa (cas no desitjat)
else:
    if (error < 0):
        thetaE = 101 - 45
        thetaB = 105 - 45
    else:
        thetaE = 101 + 45
        thetaB = 105 + 45
    case = 'B'

if (funcioPenell() >= 0) and (funcioPenell() < 180):
    thetaVela = 86 + 35
elif (funcioPenell() >= 180) and (funcioPenell() < 360):
    thetaVela = 86 - 35

