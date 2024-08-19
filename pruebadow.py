
import yt_dlp



def obtener_formatos(video_url):
    formatos_dict = {
        '144p': False,
        '240p': False,
        '360p': False,
        '480p': False,
        '720p': False,
        '1080p': False,
        'Otros': False
    }
   
    with yt_dlp.YoutubeDL() as ydl:
        # Obtener información del video
        info_dict = ydl.extract_info(video_url, download=False)
        
        # Listar formatos disponibles y verificar su disponibilidad
        formatos = info_dict.get('formats', [])
        for formato in formatos:
            height = formato.get('height', None)  # Resolución
            
            # Clasificar según la resolución
            if height in formatos_dict:
                formatos_dict[height] = True
            else:
                formatos_dict['Otros'] = True
    print(formatos_dict)
    return formatos_dict
video_url= 'https://youtu.be/kdiDXBQwQwk?si=Ct43YVWYLqwh1e-Q'
formatos_disponibles = obtener_formatos(video_url)
print(formatos_disponibles)