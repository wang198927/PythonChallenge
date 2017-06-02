import base64
import wave

text = open("music.txt","r").read()

indianMusic = open("indian.wav","wb")

decodeText = base64.b64decode(text)

indianMusic.write(decodeText)
indianMusic.close()

indianMusic = wave.open("indian.wav","rb")
indianMusicMap = wave.open('indian_map.wav','wb')
indianMusicMap.setparams(indianMusic.getparams())
for i in range(indianMusic.getnframes()):
    indianMusicMap.writeframes(indianMusic.readframes(1)[::-1])
indianMusic.close()
indianMusicMap.close()