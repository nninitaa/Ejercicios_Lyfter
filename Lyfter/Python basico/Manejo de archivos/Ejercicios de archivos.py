def arrange_songs(origin_archive, destination_archive):
    with open(origin_archive, 'r', encoding='utf-8') as file:
        songs = [line.strip() for line in file.readlines() if line.strip()]
    songs.sort()

    with open(destination_archive, 'w', encoding='utf-8') as file:
        for song in songs:
            file.write(song + '\n')

print("Canciones ordenadas correctamente.")

arrange_songs('canciones.txt', 'canciones_ordenadas.txt')