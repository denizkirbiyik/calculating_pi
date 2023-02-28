import math
import decimal

iter = int(input("How many iterations of the convergent series do you want to compute? : "));
decimal.getcontext().prec = 1+(int(input("How many digits would you like to display? : ")));
i = 1; pi = 0;

while (i<iter):
    pi = pi + 1/decimal.Decimal(i**2);
    i = i + 1;

pi = decimal.Decimal(pi*6).sqrt();
print(pi);