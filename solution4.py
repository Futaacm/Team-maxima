def factorial(n):
        newfact = n
        for i in range(1,n):
            newfact *= i
        return newfact
testcase= raw_input('>> ')
testcase=testcase.split(' ')
for name in testcase:
    length= len(name)
    permutation= factorial(length)
    print permutation
