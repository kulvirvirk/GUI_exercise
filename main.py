#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


for i in range(len(picture)):
  for j in range(len(picture[i])):
    if picture[i][j] == 0:
      print(' ', end='')
    elif picture[i][j] == 1:
      print('*', end='')
  print()
print('\n\n\n')


# some Gotcha notes: 
# 1. you would need nested for loop to iterate through list of lists
# 2. for the inner loop make sure you use len() with funciton with inner list's length. 
#    use len(picture[i])
#    not len(picture)    //this way you only iterage 6 times in above example
# 3. use print() with end=' ' to print in same row
#    e.g. 
#    for i in range(10):
#    print(i, end="<separator>") # <separator> = \n, <space> etc.

# instructor's code 
for row in picture:
  for pixel in row:
    if (pixel == 1):
      print('*', end='')
    else: 
      print(' ', end='')
  print('')