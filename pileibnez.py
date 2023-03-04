import math
import decimal

iter = int(input("How many iterations of the convergent series do you want to compute? : "));
decimal.getcontext().prec = 1+(int(input("How many digits would you like to calculate for each calculation : ")));
i = 1; pi = 0;

while (i<iter):
    if(i%4==3):
        pi = pi - 1/decimal.Decimal(i);
    else:
        pi = pi + 1/decimal.Decimal(i);
    i = i + 2;

pi = pi*4;
print(pi);