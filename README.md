# MumbleRap_song_generator

ABOUT:

Do you always listen to few mumble rap songs and you think you cant really hear the lyrics or they just go over your head?.This is python program auto-generates a lyrics from the most popular mumble rap artists  music using Markov graph and superimposes it over a random generic rap beat instrumental. Here a female voice is used instead of a male voice to add more flavour.

Instructions to run the program:

1.Download the zip file and unzip the file , and further unzip '.rar' files which contain the sample tracks which are a part of the program(they are bigger than 25mb hence they are compressed).

2.You can use the 'Genius_lyrics_finder' to add your favourite artists lyrics into the program as well.You will require a Genius access token for this which you can generate at "https://genius.com/api-clients" which is completely optional for the functioning of the program.

3.You should then open  the program  "Mumblerapgen.py" .It is recommended to set the directory of these files to a virtual environment because you  will need to install  the following modules:
a.pydub   b.gtts   c.re   d.string   e.lyricsgenius(if you followed step 2).

4.After this is done you can finally run the "Mumblerapgen.py" program and you will be prompted to select the artist from whom you want the Markov graph and finally the lyrics generated from.Make sure to enter pre-existing artists name(you can add more using step 2).

5.You will see finally see the script of the rap song in the terminal which you can choose if you want to listen or not.

6.Then finally the composed 'mumblerap' song is played.

