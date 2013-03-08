import sys

sum=0
n=0

# Sum input values
for num in open('data.txt'):
  sum += float(num)
  n+=1

# this is a comment.
print sum/n
