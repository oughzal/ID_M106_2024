import numpy
a = map(int, input().split())
b = numpy.array([input().split() for i in range(a[0])], int)
print (numpy.mean(b, axis = 1))
print (numpy.var(b, axis = 0))
print (numpy.std(b, axis = None))