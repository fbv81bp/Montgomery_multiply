# Based on
# Wikipedia's Karatsuba pseudo code
# and
# Handbook of Applied Cryptography
# by A. Menezes, P. van Oorschot, and S. Vanstone
# CRC Press, 1996. 
# Chapter 14., 14.36 Algorithm Montgomery multiplication, page 603.


# working parameters of the algorithm
m = 16381  # modulus
bit_width = 4  # bit_width of calculation (hexadecimal)
#bit_width = 8  # bytewise calculation
base = 2 ** bit_width #number system base (hexadecimal)
length = 4  # in hexadecimal
#length = 2  # bytes
R = base ** length
x  = 0x16A0  # 5792 in decimal
y  = 0x04CD  # 1229 in decimal

print('Expected result:',x * y % m)

# preparations with plain maths
def convert_to_Montgomery_plain(x, R, m):
    x = x * R % m
    return x

def neg_inv(m, bit_width, base):
    phi_base = 2 ** (bit_width - 1)  # for powers of 2
    m_neginv = base - m ** (phi_base - 1) % base
    return m_neginv

# multiplications
def Karatsuba_multiplication(x_large, y, min_len):  # asymmetric: only one operand is extremely large, th eother fits in a hardware multilier
    x = x_large
    if (x.bit_length() < min_len):
        return x * y
        
    size = x.bit_length()
    s2 = size // 2 
   
    high_x = x >> s2
    low_x = x % 2 ** s2
    low_y = y
    
    z0 = Karatsuba_multiplication(low_x, low_y, min_len)
    z1 = Karatsuba_multiplication((low_x + high_x), low_y, min_len)
    
    return ((z1 - z0) << s2) + z0

def Montgomery_multiplication_with_Karatsuba(x, y, base, m, m_neginv, length):
    accu = 0
    for i in range(length):
        u = accu % base + (x % base) * (y % base)  # easyto compute
        v = u * m_neginv % base  # easy to compute

        #accu = (accu + (x % base) * y + v * m) // base  # needs 2 Karatsuba multiplications
        accu = (accu + Karatsuba_multiplication(y, (x % base), bit_width) + Karatsuba_multiplication(m, v, bit_width)) // base  # needs 2 Karatsuba multiplications
        
        x = x >> bit_width
    if accu > m:
        accu -= m
    return accu

# inverse conversion with plain maths
def reverse_from_Montgomery_plain(accu, R, m):
    phi_m = m - 1  # for prime numbers
    R_inv = R ** (phi_m - 1) % m
    accu  = accu * R_inv % m
    return accu

x = convert_to_Montgomery_plain(x, R, m)
y = convert_to_Montgomery_plain(y, R, m)
m_neginv = neg_inv(m, bit_width, base)
accu = Montgomery_multiplication_with_Karatsuba(x, y, base, m, m_neginv, length)
accu = reverse_from_Montgomery_plain(accu, R, m)

print('Result with Montgomery:',accu)
