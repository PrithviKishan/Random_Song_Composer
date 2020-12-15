
import os
import re
import string
import random
from gtts import gTTS 
from pydub import AudioSegment
from pydub.playback import play
from markov_graph import Graph, Vertex

def get_words_from_text(text_path):
    with open(text_path, 'rb') as file:
        text = file.read().decode("utf-8") 

        # remove [verse 1: artist] and (.....) etc
        text = re.sub(r'\[(.+)\]', ' ', text)
        text = re.sub(r'\((.+)\)', ' ', text)
        text = ' '.join(text.split())
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = words[:4000]
    return words


def make_graph(words):
    g = Graph()
    prev_word = None
    # for each word
    for word in words:
        # check that word is in graph, and if not then add it
        word_vertex = g.get_vertex(word)

        # if there was a previous word, then add an edge if does not exist
        # if exists, increment weight by 1
        if prev_word:  # prev word should be a Vertex
            # check if edge exists from previous word to current word
            prev_word.increment_edge(word_vertex)

        prev_word = word_vertex

    g.generate_probability_mappings()
    
    return g

def compose(g, words, length=200):
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition


def main(artist):
    #words = get_words_from_text('texts/hp_sorcerer_stone.txt')
    f = open("demofile2.txt", 'w')
    
    
    words=[]
    for song in os.listdir('songs/{}'.format(artist)):
         if song == '.DS_Store':
             continue
         words.extend(get_words_from_text('songs/{artist}/{song}'.format(artist=artist, song=song)))
        
    g = make_graph(words)
    composition = compose(g, words, 300)
    print(' '.join(composition))
    f.write(' '.join(composition))
    f.close()
    


if __name__ == '__main__':
    artist=input(' artist name(xxxx_xxxx):')
    print(main(artist)) 

    fh=open("demofile2.txt","r")

    mytext=fh.read().replace("\n"," ")
    language='en'
    output=gTTS(text=mytext, lang=language, slow=False)
    output.save("output.mp3")

    fh.close()

    option='y'
    option=input('Do you want to keep listen to the vocals?(y/n)')  

    if option=='y'  :
        os.system("start output.mp3")
    #files={1:"E:\\Python\\virtualenv1\\rap1.wav" ,2:"E:\\Python\\virtualenv1\\rap2.wav",3:"E:\\Python\\virtualenv1\\rap3.wav"}
    
    files={1:"rap1.wav" ,2:"rap2.wav",3:"rap3.wav"}
    r=random.randint(1,3)
    file_select=files[r]
    src = "output.mp3"
    dst = "output0.wav"
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")
   
    audio1 = AudioSegment.from_file(file_select) #your first audio file
    audio2 = AudioSegment.from_file("output0.wav") #your second audio file


    mixed = audio1.overlay(audio2)          #combine , superimpose audio files

#If you need to save mixed file
    mixed.export("mixed.wav", format='wav') #export mixed  audio file
    play(mixed)                             #play mixed audio file

    