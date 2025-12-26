# Day 4: 30 Days of python programming

print('Thirty ' + 'Days ' + 'Of ' + 'Python')
print('Coding ' + 'For ' + 'All')

company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[:6])
print(company.index('Coding'))
print(company.find('Coding'))

print(company.replace('Coding', 'Python'))

python = 'Python For Everyone'
print(python.replace('Everyone', 'All'))

print(company.split())

mnc = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(mnc.split(','))

print(company[0])
print(company[-1])
print(company[9])

python1 = python.split()
print(python1[0][0].upper() + python1[1][0].upper() + python1[2][0].upper())

company1 = company.split()
print(company1[0][0].upper() + company1[1][0].upper() + company1[2][0].upper())

print(company.index('C'))
print(company.index('F'))
print(company.rfind('l'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print(sentence.rfind('because'))
print(sentence[31:54])

print(company.startswith('Coding'))
print(company.endswith('coding'))

stripping = '   Coding For All      '
print(stripping.strip())

checker1 = '30DaysOfPython'
checker2 = 'thirty_days_of_python'
print(checker1.isidentifier())
print(checker2.isidentifier())

frameworks = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#'.join(frameworks))

newliner = 'I am enjoying this challenge.\nI just wonder what is next.'
print(newliner)

tabliner = 'Name\tAge\tCountry\tCity\nSarvesh\t100\tIndia\tJaunpur'
print(tabliner)

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 ** 6 = {8 ** 6}")