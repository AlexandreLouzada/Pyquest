__author__ = 'วรรณพงษ์'
#pytemperature
def c2f(arg):
    f = ((arg/5)*9)+32
    return round(f, 2)
def f2c(arg):
    c = ((arg-32)/9)*5
    return round(c, 2)
def c2k(arg):
    return arg+273.15
def k2c(arg):
    return arg-273.15
def k2f(arg):
    f = (arg*1.8)-459.69
    return round(f,2)
def f2k(arg):
    k = (arg+459.67)/1.8
    return round(k,2)
def r2c(arg):
    return arg*1.25
def c2r(arg):
    return round(arg*0.8, 2)
def r2k(arg):
    return c2k(r2c(arg))