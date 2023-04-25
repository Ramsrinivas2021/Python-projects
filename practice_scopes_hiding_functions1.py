# Here my requirement is to make add() as private and is not intended to be called from outside the practice_scopes_hiding_functions1.py module
def _add():
    v1 = 10
    v2 = 20
    v3 =  v1 + v2
    print(v3)
    return v3
def sub():
    v4 = 10
    v5 = 15
    v6 = v5 - v4
    print(v6)
    return v6
def mult():
    v7 = 10
    v8 = 50
    v9 = v7*v8
    print(v9)
    return v9

