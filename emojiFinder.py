import json
import os
import subprocess, sys

def convert_unicode_readable(emoji):
    return chr(int(emoji[2:], 16))

def split_unicode_list(unicode_list):
    return unicode_list.split(' ')

def getEmojis(concept_list):
    unicode_set = set()
    with open('./dataset/emojis.json') as json_data:
        data = json.load(json_data)
        for i in range(len(concept_list)):
            for j in range(len(data)):
                for k in range(len(data[j]['keywords'])):
                    # print("%d %d %d" % (len(concept_list), len(data), len(data[i]['keywords'])))
                    # print("%d %d %d" % (i, j, k))
                    # concept_list[i]
                    # data[j]['keywords'][k]

                    if(concept_list[i] == data[j]['keywords'][k]):
                        # print(data[j]['unicode'])
                        # f.write(data[j]['unicode'])
                        # emoji = chr(int(data[j]['unicode']))
                        # f.write(emoji)
                        unicode_list = split_unicode_list(data[j]['unicode'])
                        for l in range(len(unicode_list)):
                            unicode_set.add(convert_unicode_readable(unicode_list[l]))
                        break
    return unicode_set

        

# def open_file(filename):
#     if sys.platform == "win32":
#         os.startfile(filename)
#     else:
#         opener ="open" if sys.platform == "darwin" else "xdg-open"
#         subprocess.call([opener, filename])


# with open('../emojiTest.html','w',encoding='utf-8-sig') as f:
#     for emoji in unicode_set:
#         f.write(emoji)

# open_file('../emojiTest.html')
