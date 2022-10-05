
# ceil()

# Import math library
import math

#  Round a number upward to its nearest integer
print(math.ceil(1.4)) ;print(math.ceil(-5.3)) ;print(math.ceil(10.0)) # 2,5,10

# Round numbers down to the nearest integer
print(math.floor(1.4)) ;print(math.floor(-5.3)) ;print(math.floor(10.0)) # 1,-6,10

# Get the number of ways to choose  k items from n items without  repetition and without order
n = 5; k = 3 #  Ncr and Nck probability formulae
nCk = math.comb(n, k); # - 5*4*3*2*1/2(3*2*1) https://www.cuemath.com/ncr-formula/
print(nCk) # 10

#Return the value of the first parameter and the sign of the second parameter
print(math.copysign(4, -1)) # -4.0

#Convert angles from radians to degrees:
print (math.degrees(8.90)) # 509.9324376664327

# Calculate Euclidean distance/  = √[ (x2– x1)2 + (y2 – y1)2] draw graphs and get distance
p = [3, 3]; q = [0, 0]
print (math.dist(p, q)) # 4.242640687119286 ->d

#The math.exp() method returns E raised to the power of x (Ex). 'E' is the base of the natural system of logarithms (approximately 2.718282) and x is the number passed to it.
print(math.exp(65)) # 1.6948892444103338e+28

#Remove - sign of given number
print(math.fabs(-66.43)) # 66.43

# Return the remainder of x/y
print(math.fmod(20, 4)); print(math.fmod(20, 3)) # 0.0, 2.0

# Print the sum of all items lists, tuples and sets
print(math.fsum([1, 2])); print(math.fsum({1,3}));print(math.fsum((1,3))); #print(math.fsum((1,4))

#find the  the greatest common divisor of the two integers
print (math.gcd(3, 6)) # 3

#compare the closeness of two values // It uses the following formula to compare the values: abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
print(math.isclose(1.233, 1.4566)) # flase

# Check whether the values are finite or not// its numer of no
print(math.isfinite(2000)); print(math.isfinite(float("-inf"))) # true , flase

# Check whether the values are infinite or not
print(math.isinf(56)) # false

# The math.isnan() method checks whether a value is NaN (Not a Number), or not
print (math.isnan (56));print (math.isnan (0)) # false false


# Print the number of ways to choose k items from n items
n = 7; k = 5
print (math.perm(n, k)) # Ncr 2520

#Return the value of 9 raised to the power of 3
print(math.pow(2, 3)) # = 2^3 = 8

# Print the square root of different numbers
print (math.sqrt(10))
















