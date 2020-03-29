#FUNCTIONS FOR BITWISE MONTGOMERY MODULAR EXPONENTIATION
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def bit_val(a, n):
    if (a & (1<<n)):
        return 1
    else:
        return 0

#multiplication the Montgomery way
#---------------------------------

def montgomery_product(x, y, modulus, bitlength):
    product = 0
    for i in range(0, bitlength):
        if bit_val(x, i):
            product = product + y
        if bit_val(product, 0):
            product = product + modulus
        product = product >> 1
    if product >= modulus:
        product = product - modulus
    return product

#modular exponentiation in Montgomery form
#-----------------------------------------

def modular_exponentiation(one, base, exponent, modulus, bitlength):
    exponential = one
    for i in range(bitlength-1, -1, -1):
        exponential = montgomery_product(exponential, exponential, modulus, bitlength)
        if bit_val(exponent, i):
            exponential = montgomery_product(base, exponential, modulus, bitlength)
    return exponential

#modular exponentiation input - pick random numbers!
#---------------------------------------------------

base = 54 #610178765
exponent = 19 #865194045
modulus = 97 #16859994528005452387
#modulus = 11745174699710101459

print("expected:\n",base ** exponent % modulus)  #uncomment for smaller numbers only

#CONVERT INPUT TO MONTGOMERY DOMAIN -- do not convert the exponent!
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

bitlength = 8 #4096
domain = 2**bitlength

#conversion with plain mathematics
#---------------------------------

#one = 1 * domain % modulus
#base = base * domain % modulus

#conversion of big numbers into Montgomery domain by Montgomery product
#----------------------------------------------------------------------

domain_square = domain ** 2 % modulus
one = montgomery_product(1, domain_square, modulus, bitlength)
base = montgomery_product(base, domain_square, modulus, bitlength)

#calculate modular exponential
#-----------------------------
result = modular_exponentiation(one, base, exponent, modulus, bitlength)

#REVERSE MONTGOMERY CONVERSION
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#with plain mathematics:
#-----------------------

#eulers_totient = modulus - 1 #because (modulus) is prime
#domain_to_minus_one = domain ** (eulers_totient - 1) % modulus
#result = result * domain_to_minus_one % modulus

#reverse convert big numbers with Montgomery product
#---------------------------------------------------
result = montgomery_product(result, 1, modulus, bitlength)

print("modular exponentiation with montgomery multiplication:\n", result)

