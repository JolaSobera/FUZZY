def T_minimum(a, b):
    """
    Funckja oblicza wartość T-normy minimum liczb a i b

    WE:
    a - liczba z przedziału [0;1]
    b - liczba z przedziału [0;1]

    WY:
    liczba z przedziału [0;1]
    """
    if a <= b:
        return a
    else:
        return b

def T_Hamachera(a,b):
    """
    Funckja oblicza wartość iloczynu Hamachera liczb a i b

    WE:
    a - liczba z przedziału [0;1]
    b - liczba z przedziału [0;1]

    WY:
    liczba z przedziału [0;1]
    """

    if a==0 and b==0:
        return 0
    else:
        return (a*b)/(a+b-a*b)

def T_produktowa(a,b):
    """
    Funckja oblicza wartość T-normy produktowej liczb a i b

    WE:
    a - liczba z przedziału [0;1]
    b - liczba z przedziału [0;1]

    WY:
    liczba z przedziału [0;1]
    """

    return a*b

def T_Lukasiewicza(a,b):
    """
    Funckja oblicza wartość T-normy Łukasiewicza liczb a i b

    WE:
    a - liczba z przedziału [0;1]
    b - liczba z przedziału [0;1]

    WY:
    liczba z przedziału [0;1]
    """
    if a+b - 1 > 0:
        return a+b - 1
    else:
        return 0

def T_drastyczna(a, b):
    """
    Funckja oblicza wartość T-normy drastycznej liczb a i b

    WE:
    a - liczba z przedziału [0;1]
    b - liczba z przedziału [0;1]

    WY:
    liczba z przedziału [0;1]
    """
    if a == 1:
        return b
    elif b == 1:
        return a
    else:
        return 0

def T_minimum_nilpotentne(a,b):
    """
    Funckja oblicza wartość T-normy minimum nilpotentne liczb a i b

    WE:
    a - liczba z przedziału [0;1]
    b - liczba z przedziału [0;1]

    WY:
    liczba z przedziału [0;1]
    """
    if a+b <= 1:
        return 0
    elif a < b:
        return a
    else:
        return b

def S_maksimum(a, b):
    """
    Funckja oblicza wartość S-normy maksimum liczb a i b

    WE:
    a - liczba z przedziału [0;1]
    b - liczba z przedziału [0;1]

    WY:
    liczba z przedziału [0;1]
    """
    if a >= b:
        return a
    else:
        return b

def S_hamachera(a,b):
    """
    Funckja oblicza wartość sumy Hamachera liczb a i b

    WE:
    a - liczba z przedziału [0;1]
    b - liczba z przedziału [0;1]

    WY:
    liczba z przedziału [0;1]
    """
    if a==1 and b==1:
        return 1
    else:
        return (a+b-2*a*b)/(1-a*b)

def S_dualna_produktowa(a,b):
    """
    Funckja oblicza wartość S-normy dualnej do T-normy produktowej liczb a i b

    WE:
    a - liczba z przedziału [0;1]
    b - liczba z przedziału [0;1]

    WY:
    liczba z przedziału [0;1]
    """
    return a+b-a*b

def S_lukasiewicza(a,b):
    """
    Funckja oblicza wartość S-normy Łukasiewicza liczb a i b

    WE:
    a - liczba z przedziału [0;1]
    b - liczba z przedziału [0;1]

    WY:
    liczba z przedziału [0;1]
    """
    if a+b < 1:
        return a+b
    else:
        return 1

def S_drastyczna(a, b):
    """
    Funckja oblicza wartość S-normy drastycznej liczb a i b

    WE:
    a - liczba z przedziału [0;1]
    b - liczba z przedziału [0;1]

    WY:
    liczba z przedziału [0;1]
    """
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return 1

def S_maksimum_nilpotentne(a,b):
    """
    Funckja oblicza wartość S-normy maksimum nilpotentne liczb a i b

    WE:
    a - liczba z przedziału [0;1]
    b - liczba z przedziału [0;1]

    WY:
    liczba z przedziału [0;1]
    """
    if a + b >= 1:
        return 1
    elif a > b:
        return a
    else:
        return b

def I_Lukasiewicza(a,b):
    """
    Funckja oblicza wartość implikacji Łukasiewicza liczb a i b

    WE:
    a - liczba z przedziału [0;1]
    b - liczba z przedziału [0;1]

    WY:
    liczba z przedziału [0;1]
    """
    if 1 - a + b < 1:
        return 1 - a+b
    else:
        return 1

def I_Godel(a,b):
    """
    Funckja oblicza wartość implikacji Godela liczb a i b

    WE:
    a - liczba z przedziału [0;1]
    b - liczba z przedziału [0;1]

    WY:
    liczba z przedziału [0;1]
    """
    if a <= b:
        return 1
    else:
        return b

def I_Reichenbach(a,b):
    """
    Funckja oblicza wartość implikacji Reichenbacha liczb a i b

    WE:
    a - liczba z przedziału [0;1]
    b - liczba z przedziału [0;1]

    WY:
    liczba z przedziału [0;1]
    """
    return 1 - a + a*b

def I_Kleene_Dienes(a,b):
    """
    Funckja oblicza wartość implikacji Kleene-Dienesa liczb a i b

    WE:
    a - liczba z przedziału [0;1]
    b - liczba z przedziału [0;1]

    WY:
    liczba z przedziału [0;1]
    """
    if 1 - a > b:
        return 1 - a
    else:
        return b

def I_Goguen(a,b):
    """
    Funckja oblicza wartość implikacji Goguena liczb a i b

    WE:
    a - liczba z przedziału [0;1]
    b - liczba z przedziału [0;1]

    WY:
    liczba z przedziału [0;1]
    """
    if a <= b:
        return 1
    else:
        return b / a

def I_Rescher(a,b):
    """
    Funckja oblicza wartość implikacji Reschera liczb a i b

    WE:
    a - liczba z przedziału [0;1]
    b - liczba z przedziału [0;1]

    WY:
    liczba z przedziału [0;1]
    """
    if a <= b:
        return 1
    else:
        return 0

def I_Yager(a,b):
    """
    Funckja oblicza wartość implikacji Yagera liczb a i b

    WE:
    a - liczba z przedziału [0;1]
    b - liczba z przedziału [0;1]

    WY:
    liczba z przedziału [0;1]
    """
    if a == 0 and b == 0:
        return 1
    else:
        return b ** a

def I_Weber(a,b):
    """
    Funckja oblicza wartość implikacji Webera liczb a i b

    WE:
    a - liczba z przedziału [0;1]
    b - liczba z przedziału [0;1]

    WY:
    liczba z przedziału [0;1]
    """
    if a < 1:
        return 1
    else:
        return b

def I_Fodor(a,b):
    """
    Funckja oblicza wartość implikacji Fodora liczb a i b

    WE:
    a - liczba z przedziału [0;1]
    b - liczba z przedziału [0;1]

    WY:
    liczba z przedziału [0;1]
    """
    if a <= b:
        return 1
    elif 1-a > b:
        return 1-a
    else:
        return b