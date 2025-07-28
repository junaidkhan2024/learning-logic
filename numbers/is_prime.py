#Check if a number is prime.

def isPrime(n):
   if n <= 1:
    print(f"{n} is not a prime number")
    return
   for i in range(2,n):
     if n % i == 0:
      print(f"{n} is defiantely not a prime")
      return
   else:
    print(f"{n} is PRIME number") 

a = 5
isPrime(a)
print("__________________________________________________")
#square root method

def squareroot_Isprime(n):
  if n <= 1:
    print(f"{n} is not a prime number") # 1 is not a prime number
    return
  for i in range(2,int((n**0.5)+1)):
    if n % i == 0:
      print(f"{n} is surely not a prime number")
      return
  else:
      print(f"{n} is PRIME NUMBER.")

a = 4546565
squareroot_Isprime(a)
