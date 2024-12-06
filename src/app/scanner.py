import time

from PyQt5.QtCore import QRunnable, QObject, pyqtSignal
from os.path import exists
from .avlc import AudioPlayer, MediaEvent
from .util import get_files
from .serializer import deserialize_library


class Signals(QObject):
    scanned = pyqtSignal(object)


class LibraryScanner(QRunnable):
    def __init__(self, player: AudioPlayer, scanPath: str = "/Users/samuelgonzalez/Documents/MUSICA"):
        super(LibraryScanner, self).__init__()
        self.signal = Signals()
        self.scanPath = scanPath  # Ruta por defecto establecida
        self.audioPlayer = player

    def run(self) -> None:
        if not exists("conf/library.json"):
            # Modificar la ruta de escaneo aquí para buscar en la carpeta de música
            for file in get_files(self.scanPath, [".mp3", ".flac", ".wav"]):  # Buscar múltiples tipos de archivos
                self.audioPlayer.add_local_media(file)
            for media in self.audioPlayer.mediaList:
                media.connect_event(MediaEvent.Parsed, lambda med: self.signal.scanned.emit(med))
                media.parse()
        else:
            library = deserialize_library("conf/library.json", self.audioPlayer.vlcInstance)
            for media in library:
                self.audioPlayer.add_avlc_media(media)
                self.signal.scanned.emit(media)