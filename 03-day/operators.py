# Day 3: 30 Days of python programming

age = int()
height = float()
complex_num = complex()

base = float(input("Enter Base: "))
height = float(input("Enter Height: "))
area_of_triangle = 0.5 * base * height
print("Area of triangle: ", area_of_triangle)

side_a = int(input("Enter Side a: "))
side_b = int(input("Enter Side b: "))
side_c = int(input("Enter Side c: "))
perimeter_of_triangle = side_a + side_b + side_c
print("The perimeter of the triangle: ", perimeter_of_triangle)

length_rect = int(input("Enter rectangle length: "))
width_rect = int(input("Enter rectangle width: "))
area_of_rectangle = length_rect * width_rect
perimeter_of_rectangle = 2 * (length_rect + width_rect)
print(f"Area of rectangle: {area_of_rectangle}, Perimeter of rectangle: {perimeter_of_rectangle}")

x = int(input("Enter x - intercept for the slope: "))
y = 2 * x - 2
print("Slope 1: ", y)

x1, x2, y1, y2 = 2, 6, 2, 10
m = (y2 - y1) / (x2 - x1)
print("Slope 2: ", m)

print("Comparing Slope1: ", y, " with " , "Slope 2: ", m)

x = int(input("Enter the value for x: "))
y = x ** 2 + 6 * x + 9
# Putting -3 will gives us 0 in this equation.
print("The equation gives: ", y)

checky1 = len('python') != len('dragon')
print(checky1)

checky2 = 'on' in 'python' and 'on' in 'dragon'
print(checky2)

sentence = 'I hope this course is not full of jargon'
checky3 = 'jargon' in sentence
print(checky3)

checky4 = 'on' not in 'python' and 'on' not in 'dragon'
print(checky4)

text = 'python'
print(str(float(len(text))))

even_numbers = int(input("Put a number: "))
print("The number is even? -> ", even_numbers % 2 == 0)

fd =  (7 // 3) == int(2.7)
print(fd)

print(type('10') == type(10))

print(int(9.8) == 10)

hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_hour
print("Your weekly earning is ", weekly_earning)

years_lived = int(input("Enter number of years you have lived: "))
seconds_lived = years_lived * 365.25 * 24 * 60 * 60
print(f"You have lived for {seconds_lived} seconds.")

print("1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125")