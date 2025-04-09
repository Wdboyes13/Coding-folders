from gtts import gTTS
import os
tts = gTTS(text='À propos de moi!', lang='fr')
tts.save("aboutme.mp3")
os.system("mpg123 aboutme.mp3")

tts = gTTS(text='Je m\'appelle william.', lang='fr')
tts.save("name.mp3")
os.system("mpg123 name.mp3")

tts = gTTS(text='Je suis canadien.', lang='fr')
tts.save("country.mp3")
os.system("mpg123 country.mp3")

tts = gTTS(text='Je parlais anglais.', lang='fr')
tts.save("english.mp3")
os.system("mpg123 english.mp3")

tts = gTTS(text='J\'adore envoyer des textes et écouter de la musique.', lang='fr')
tts.save("love.mp3")
os.system("mpg123 love.mp3")

tts = gTTS(text='J\'aime jouer à des jeux-vidéo et cuisiner.', lang='fr')
tts.save("like.mp3")
os.system("mpg123 like.mp3")

tts = gTTS(text='Je n\'aime pas faire du sport.', lang='fr')
tts.save("dislike.mp3")
os.system("mpg123 dislike.mp3")

tts = gTTS(text='Je déteste faire la fête.', lang='fr')
tts.save("hate.mp3")
os.system("mpg123 hate.mp3")

tts = gTTS(text='Au revoir! Bonne journée!', lang='fr')
tts.save("bye.mp3")
os.system("mpg123 bye.mp3")

