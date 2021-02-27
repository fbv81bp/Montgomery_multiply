# Based on Handbook of Applied Cryptography
# by A. Menezes, P. van Oorschot, and S. Vanstone
# CRC Press, 1996. 
# Chapter 14., 14.36 Algorithm Montgomery multiplication, page 603.


# working parameters of the algorithm
x  = 1294321 # multiplier
y  = 6553456 # multiplicand
# m = 65537 # 17 bits
# m = 12578413 # 24 bits
m = 279231519537917 # 48 bits
#m = 211 * 157 # 16 bit composite number of two primes
bit_width = 11  # any arbitrary length

print('Expected result:',x * y % m)

# preparations
num_sys_base = 2**bit_width #number system base (hexadecimal)

mod_bit_len = 0
modulus = m
length = 0
while modulus != 0:
    length += 1
    modulus >>= 1
if length % bit_width != 0:
    mod_bit_len = length // bit_width + 1
else:
    mod_bit_len = length // bit_width

print('Modulus length in bit width steps:', mod_bit_len)

R = num_sys_base**mod_bit_len

# Uncomment to see inner result if x and y are both converted too in line 41 and 42
# result = x * y % m
# converted = result * R % m
# print('Expexted in Montgomery domain:', converted)

#x = x * R % m # skip converting x or y to get normal domain result after multiplication
y = y * R % m  # skip converting x or y to get normal domain result after multiplication
phi_base = 2 ** (bit_width - 1)  # for powers of 2
m_neginv = num_sys_base - (m % num_sys_base) ** (phi_base - 1) % num_sys_base
#                           ^^^ ENABLES THE USE OF A LOOKUP TABLE TO BE USED FOR SMALLER BIT WIDTHS !!!

# multiplication
accu = 0
for i in range(mod_bit_len):
    u = (accu % num_sys_base + (x % num_sys_base) * (y % num_sys_base)) * m_neginv % num_sys_base  # modulo num_sys_base gives the last digit
    accu = (accu + (x % num_sys_base) * y + u * m) // num_sys_base
    x = x >> bit_width  # shiftig x so that modulo num_sys_base we get th elast digit in the next round
if accu > m:
    accu -= m

print('Result in Montgomery domain:  ',accu)

# inverse conversion: comment for larger modulus!
#phi_m = m - 1  # for prime numbers only!
# phi_m = (211 - 1) * (157 - 1) # for the composite number set in line 11
# R_inv = R ** (phi_m - 1) % m
# accu  = accu * R_inv % m

# print('Final result with Montgomery: ',accu)
