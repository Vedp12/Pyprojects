# n = int(input("Enter the number: "))
# for num in range(2,n+1):
#         is_prime = True
#         for i in range(2,num):
#             if num%i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
            # print(num)

# n = int(input("Enter a number: "))

# for num in range(2, n + 1):
#     is_prime = True

#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(num)

n = int(input("Enter the number: "))
for i,num in enumerate(range(1,n+1)):
    if num%2 == 0:
        print(f"{i+1} is even")
    else:
        print(f"{i+1} is odd")