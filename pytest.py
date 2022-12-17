# Nov 22, 2022 practice exercise

#print words that only start with a S
st = 'Sam Print only the words that start with s in the sentence'

for word in st.split():
    if word[0].lower() == 's':
        print(word)

#print a list with a step count of 2
l1 = list(range(0, 11, 2))
print(l1)

#print number with step 2 using for loop
for item in range(0, 11, 2):
    print(item)

#list comprehension to list number between 1 and 50 that are divisibe by 3
comp = [x for x in range(1,51) if x%3 == 0]
print(comp)

#in given string print word if length is even
s1 = 'Print every word in this sentence that has an even number of letters'
for z in s1.split():
    if len(z)%2 == 0:
        print(z)



#print numbers from 1 to 100. print "Fizz" if muliple of 3
#print "Buzz" if multiple of 5.
#print "FizzBuzz" if multiple of both 3 & 5

for num in range(1, 101):
    if num%3 == 0 and num%5 == 0:
        print('FizzBuzz')
    elif num%3 == 0:
        print('Fizz')
    elif num%5 == 0:
        print('Buzz')
    else:
        print(num)


#list comprehension to create a list of first letter in the string
q = 'Create a list of the first letters of every word in this string'
lcom = [word[0] for word in q.split()]
print(lcom)