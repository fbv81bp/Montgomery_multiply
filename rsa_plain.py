p = 97  # prime 1
q = 101  # prime 2
m = p * q  # modulus
e = 19  # encrypting exponent

for x in range(50):
    # wrong, but lucky
    phi = (p - 1) * (q - 1)  # Euler's totient
    d1 = e ** (phi - 1) % phi  # decrypting exponent
    print(d1)
    #x = 24  # plain text
    y = x ** e % m  # cipher text
    print(x == y ** d1 % m)

    # more likely to be correct
    phi = (p - 1) * (q - 1)  # Euler's totient
    phi_of_phi = (29-1)*(331-1) # Euler's totient again(!)
    d2 = e ** (phi_of_phi - 1) % phi  # decrypting exponent
    print(d2)
    #x = 24  # plain text
    y = x ** e % m  # cipher text
    print(x == y ** d1 % m)