#!/usr/bin/env python3

import os
import sys
import webbrowser
import subprocess
import time

__version__ = 2.0 # added ability to open/play file searched

top_path = '/media/3TB Hard Drive'
print(top_path)

def change(top_path):

        other_dir = input('Input full path\n')
        if os.path.exists(other_dir):
            top_path = other_dir
            return other_dir
        else:
            change(top_path)

print('1) Continue')
print('2) Change directory')
changedir = input('Search another directory?\n')
if changedir == '2':
    top_path = change(top_path)
    print('Directory changed to', top_path)


def search(top_path):
    filename = input('Enter part/full name of the file you are searching : ')
    if filename == 'q' or filename == '':
        return False
    alter = []
    found = []
    if filename not in alter:
        alter.append(filename)
    if filename.upper() not in alter:
        alter.append(filename.upper())
    if filename.capitalize() not in alter:
        alter.append(filename.capitalize())
    if filename.lower() not in alter:
        alter.append(filename.lower())
    if filename.title() not in alter:
        alter.append(filename.title())

    if ' ' in filename:
        dotted = filename.replace(' ', '.')
        alter.append(dotted)
        alter.append(dotted.title())
        '''
        alter.append(dotted.upper())
        alter.append(dotted.capitalize())
        alter.append(dotted.lower())'''

    file_name = []
    counter = 0
    mydict = {}
    print('Searching for',alter,'\nPlease Wait...')
    for (path, dirs, files) in os.walk(top_path):
        for num, filename in enumerate(files):
            for index in alter:
                if index in filename:
                    if index not in found:
                        found.append(path)
                        counter += 1
                    mydict[str(counter)] = path + os.sep + filename
                    print('found', filename, '\nin', path)

                    #print('found', filename, '\nin', path)
                    print(counter, ': To open/play')
                    print('---')
        for all in dirs:
            for index in alter:
                if index in all:
                    if index not in found:
                        pass
                        #found.append(index)
                    #print('found dir', all, '\nin', path)
                    #print('---')

    if found == []: #if found none
            print('Could not find', alter)
    print()
    while True:
        choice = input('Choose file to open, [q to quit]: ')
        if choice == 'q':
            break
        else:
            try:
                webbrowser.open(mydict[choice])
                time.sleep(2)
            except KeyError:
                print('Value does not exist')
            continue
    #print(mydict)
    
    
while True: 
    val = search(top_path)
    if val is False:
        break
    







