from asyncore import read
import csv

import time
# To read the csv file into the dictionary

start = time.time()

converter={} 

with open('french_dictionary.csv', newline='') as csvfile:
    fieldnames = ['english', 'french']
    reader = csv.DictReader(csvfile,fieldnames)
    for row in reader:
       converter.setdefault(row['english'],row['french'])


print(converter)
words_freq = []

converted_file = open("t8.shakespeare.translated.txt", "w+")

with open('t8.shakespeare.txt','r') as inputfile:   
    for line in inputfile:
        converted_line = ''
        for word in line.split():
            if word in converter:
                if len(words_freq) == 0:
                    new_dict = {'english': word, 'french': converter[word], 'count': 1}
                    words_freq.append(new_dict)
                else:
                    exist_dic = [x for x in words_freq if x['english'] == word]
                    if len(exist_dic) == 0:
                        new_dict = {'english': word, 'french': converter[word], 'count': 1}
                        words_freq.append(new_dict)
                    else:
                        exist_dic[0]['count'] += 1
                converted_line += ' ' + converter[word]
            else:
                converted_line += ' ' + word

        converted_file.write(converted_line)
        converted_file.write('\n')

converted_file.close()

for w in words_freq:
    print(w['english'] + ',' + w['french'] + ',' + str(w['count']))

end = time.time()

print("The time", end-start)