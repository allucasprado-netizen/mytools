import math
PI_INT = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
E_INT = "2.71828182845904523536028747135266249775724709369995957496696762772407663035354759457138217852516642742"
def pi_real(n):
    if(n > 0 and n < 100):
        n+=2
        return PI_INT[0:n]
    else:
        return "numero invalido"
def e_real(n):
    if(n > 0 and n < 100):
        n+=2
        return E_INT[0:n]
    else:
        return "numero invalido"
