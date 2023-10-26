# Area of triangle is 1/2 * base * height


base = int(input("base num? "))
height = int(input("height num? "))

area_of_triable = 1 / 2 * base * height
print(area_of_triable)





n = 9
prime = 0
for i in range(2, n):
    if n % i == 0:
       break
    if i == n-1:
        print(i)

