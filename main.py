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

print(len(picture[0]))

for i in range(len(picture)):
  for j in range(len(picture[i])):
    if picture[i][j] == 0:
      print(' ', end=' ')
    elif picture[i][j] == 1:
      print('*', end=' ')
  print()


