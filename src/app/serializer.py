import json
from .avlc import AvlcMedia


def serialize_library(media_list, file_path):
    """
    Serializa la lista de medios y la guarda en un archivo JSON.

    :param media_list: Lista de objetos de medios a serializar
    :param file_path: Ruta del archivo JSON donde guardar los datos
    """
    with open(file_path, "w") as file:
        file.truncate(0)  # Limpiar el contenido del archivo
        # Convertir la lista de medios en diccionarios
        media_list = [media.get_meta_as_dict() for media in media_list]
        # Guardar los datos en formato JSON
        json.dump({"library": media_list}, file, indent=2)


def deserialize_library(file_path, vlc_instance):
    """
    Deserializa un archivo JSON para cargar la lista de medios.

    :param file_path: Ruta del archivo JSON con la biblioteca serializada
    :param vlc_instance: Instancia de VLC para crear objetos AvlcMedia
    :return: Lista de objetos AvlcMedia
    """
    result = []
    # Verificar si el archivo de biblioteca existe antes de intentar cargarlo
    if not exists(file_path):
        return result

    with open(file_path, "r") as file:
        # Cargar los datos del archivo JSON
        library = json.load(file)["library"]
        for track in library:
            # Crear instancias de AvlcMedia usando los datos deserializados
            media = AvlcMedia(None, None, vlc_instance,
                              track["location"],
                              track["type"],
                              track["filename"],
                              track["duration"],
                              track["title"],
                              track["artist"],
                              track["album"],
                              track["art"],
                              track["genre"],
                              track["channel"],
                              track["category"],
                              track["date"]
                              )
            result.append(media)
    return result