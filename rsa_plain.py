p = 97  # prime 1
q = 101  # prime 2
m = p * q  # modulus
e = 19  # encrypting exponent

for x in range(50):
    # prolly wrong, but lucky
    phi = (p - 1) * (q - 1)  # Euler's totient
    d1 = e ** (phi - 1) % phi  # decrypting exponent
    print(d1)
    y = x ** e % m  # cipher text
    print(x == y ** d1 % m)

    # more likely to be correct
    phi = (p - 1) * (q - 1)  # Euler's totient --> 9600 in this case
    phi_of_phi = 2560 # Euler's totient again (of 9600) --> http://www.javascripter.net/math/calculators/eulertotientfunction.htm
    d2 = e ** (phi_of_phi - 1) % phi  # decrypting exponent
    print(d2)
    y = x ** e % m  # cipher text
    print(x == y ** d1 % m)