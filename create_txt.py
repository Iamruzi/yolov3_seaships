import os
import random

txt_file = open('data\\'+'train_seaship_ore.txt', 'w')
training_file = os.listdir("Seaships\\JPEGImages_ore")
count = 0
for i in training_file:
    txt_file.write('D:/python_files/yolov3/Seaships/JPEGImages/' + i)
    txt_file.write('\n')
    count = count + 1

txt_file.close()
print(count)