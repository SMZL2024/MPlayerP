import glob
import re
import os


def get_files(path: str, filetypes: list):
    """
    Scan a directory for files with specific file types.

    :param path: [str] path to directory that you want to scan
    :param filetypes: [list] the file types that you want to get from the specific directory
    :return: [list] list of path to the files
    """
    # Asegura que la ruta esté en el formato correcto
    path = re.split(r"[\\|/]", path)
    path[0] = path[0] + os.path.sep
    files = []

    # Buscar los archivos con las extensiones indicadas
    for filetype in filetypes:
        files.extend(glob.glob(os.path.join(*path, f"**/*{filetype}"), recursive=True))

    return files


# Directorio y extensiones de música
music_directory = "/Users/samuelgonzalez/Documents/MUSICA"  # Ruta donde se encuentran los archivos de música
file_types = [".flac", ".mp3", ".wav"]  # Puedes agregar más extensiones de música si es necesario

# Obtener archivos de música
music_files = get_files(music_directory, file_types)

# Imprimir archivos encontrados
print(f"Se encontraron {len(music_files)} archivos de música:")
for music_file in music_files:
    print(music_file)