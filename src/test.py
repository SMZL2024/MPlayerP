import time

from app.avlc import AudioPlayer

a = AudioPlayer()
a.add_local_media(r" /Users/samuelgonzalez/Documents/MUSICA/02\ -\ Avicii\ -\ Heaven.flac ")
a.play()
print(a.vlcPlayer.get_state())
time.sleep(10)
a.pause()
print(a.vlcPlayer.get_state())
a.wait()
