from flask import Flask, redirect, render_template, request
from pytube import YouTube, Playlist, Channel
import os
import zipfile
appyoutube= Flask(__name__, template_folder="Plantillas", static_folder="Archivos")
base=os.getcwd()
descarga_carpeta=os.path.join(base, "Archivos", "Descargas")
carpeta_zip=os.path.join(base, "Archivos", "Descargas", "Playlist")
channel_carpeta=os.path.join(base, "Archivos", "Descargas", "Channels")
archivo2=""
archivos2=""
archivorarDL3=""

@appyoutube.errorhandler(404)
def error404(error):
    mensaje= "Ah Ocurrido Un Error 404. Pagina no encontrada. Por Favor regresa al sitio de inicio e intenta de nuevo"
    return render_template("Error.html", message1=mensaje) #Pagina no Encontrada

@appyoutube.errorhandler(405)
def error405(error):
    mensaje= "Error 405. Metodo no encontrado"
    return render_template("Error.html", message1=mensaje)

@appyoutube.errorhandler(500)
def error500(error):
    mensaje= "Error Interno 500. Error ocurrido en el programa"
    return render_template("Error.html", message1=mensaje)

@appyoutube.route("/", methods=["GET", "POST"])
def inicio():
    global archivo2
    global enlace
    if request.method=="POST":
        sitio1=request.form["link"]
        sitio2=sitio1.split("=")[-1]
        enlace=request.form["link"]
        if enlace!="":
            video= YouTube(enlace)
            calidad=request.form["res"]
            if calidad=="audio":
                video=video.streams.get_audio_only()
                mensaje="Audio Descargado"
                archivo=video.download(descarga_carpeta)
                archivo1=archivo.split("\A")[-1]
                archivo2=archivo
                return redirect("/"+sitio2)
            elif calidad=="alta":
                video= video.streams.get_highest_resolution()
                mensaje= "Video Descargado"
                archivo=video.download(descarga_carpeta)
                archivo1=archivo.split("\A")[-1]
                archivo2="A"+archivo1
                return redirect("/"+sitio2)
            elif calidad=="baja":
                video= video.streams.get_lowest_resolution()
                mensaje= "Video Descargado"
                archivo=video.download(descarga_carpeta)
                archivo1=archivo.split("\A")[-1]
                archivo2="A"+archivo1
                return redirect("/"+sitio2)
            else:
                video= video.streams.get_by_resolution(calidad)
                mensaje= "Video Descargado"
                archivo=video.download(descarga_carpeta)
                archivo1=archivo.split("\A")[-1]
                archivo2="A"+archivo1
                return redirect("/"+sitio2)
        else:
            mensaje= "El campo esta vacio o no has seleccionado una calidad de video"
            return render_template("Inicio.html", message=mensaje)
    else:
        return render_template("Inicio.html")

@appyoutube.route("/playlist", methods=["GET", "POST"])
def inicio2():
    global enlace2
    global archivos2
    global archivorarDL3
    if request.method=="POST":
        sitio1=request.form["link"]
        sitio3=sitio1.split("=")[-1]
        enlace2=request.form["link"]
        if enlace2!="":
            ListaVideos= Playlist(enlace2)
            calidad=request.form["res"]
            if calidad=="audio":
                for video in ListaVideos.videos:
                    video.streams.get_audio_only().download(carpeta_zip)
                    yt = YouTube(ListaVideos.video_urls[0]).thumbnail_url
                    archivos2=yt
                    nombrezip= ListaVideos.title+".zip"
                    ruta=carpeta_zip+"/"+nombrezip
                    archivorar= zipfile.ZipFile(ruta, "w")
                for folder, subfolders, files in os.walk(carpeta_zip):
                    for file in files:
                        if file.endswith(".mp4"):
                            archivorar.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), carpeta_zip), compress_type=zipfile.ZIP_DEFLATED)
                            archivorarDL=archivorar.filename
                            archivorarDL2=archivorarDL.split("\Ar")[-1]
                            archivorarDL3="Ar"+archivorarDL2
                archivorar.close()
                for folder, subfolders, files in os.walk(carpeta_zip):
                    for file in files:
                        if file.endswith(".mp4"):
                            os.remove(folder+"/"+file)
                return redirect("/playlist"+sitio3)
            elif calidad=="alta":
                for video in ListaVideos.videos:
                    video.streams.get_highest_resolution().download(carpeta_zip)
                    yt = YouTube(ListaVideos.video_urls[0]).thumbnail_url
                    archivos2=yt
                    nombrezip= ListaVideos.title+".zip"
                    ruta=carpeta_zip+"/"+nombrezip
                    archivorar= zipfile.ZipFile(ruta, "w")
                for folder, subfolders, files in os.walk(carpeta_zip):
                    for file in files:
                        if file.endswith(".mp4"):
                            archivorar.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), carpeta_zip), compress_type=zipfile.ZIP_DEFLATED)
                            archivorarDL=archivorar.filename
                            archivorarDL2=archivorarDL.split("\Ar")[-1]
                            archivorarDL3="Ar"+archivorarDL2
                archivorar.close()
                for folder, subfolders, files in os.walk(carpeta_zip):
                    for file in files:
                        if file.endswith(".mp4"):
                            os.remove(folder+"/"+file)
                return redirect("/playlist"+sitio3)
            elif calidad=="baja":
                for video in ListaVideos.videos:
                    video.streams.get_lowest_resolution().download(carpeta_zip)
                    yt = YouTube(ListaVideos.video_urls[0]).thumbnail_url
                    archivos2=yt
                    nombrezip= ListaVideos.title+".zip"
                    ruta=carpeta_zip+"/"+nombrezip
                    archivorar= zipfile.ZipFile(ruta, "w")
                for folder, subfolders, files in os.walk(carpeta_zip):
                    for file in files:
                        if file.endswith(".mp4"):
                            archivorar.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), carpeta_zip), compress_type=zipfile.ZIP_DEFLATED)
                            archivorarDL=archivorar.filename
                            archivorarDL2=archivorarDL.split("\Ar")[-1]
                            archivorarDL3="Ar"+archivorarDL2
                archivorar.close()
                for folder, subfolders, files in os.walk(carpeta_zip):
                    for file in files:
                        if file.endswith(".mp4"):
                            os.remove(folder+"/"+file)
                return redirect("/playlist"+sitio3)
            else:
                for video in ListaVideos.videos:
                    video.streams.get_by_resolution(calidad).download(carpeta_zip)
                    yt = YouTube(ListaVideos.video_urls[0]).thumbnail_url
                    archivos2=yt
                    nombrezip= ListaVideos.title+".zip"
                    ruta=carpeta_zip+"/"+nombrezip
                    archivorar= zipfile.ZipFile(ruta, "w")
                for folder, subfolders, files in os.walk(carpeta_zip):
                    for file in files:
                        if file.endswith(".mp4"):
                            archivorar.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), carpeta_zip), compress_type=zipfile.ZIP_DEFLATED)
                            archivorarDL=archivorar.filename
                            archivorarDL2=archivorarDL.split("\Ar")[-1]
                            archivorarDL3="Ar"+archivorarDL2
                archivorar.close()
                for folder, subfolders, files in os.walk(carpeta_zip):
                    for file in files:
                        if file.endswith(".mp4"):
                            os.remove(folder+"/"+file)
                return redirect("/playlist"+sitio3)
        else:
            mensaje= "La Playlist es incorrecta o el campo esta vacio"
            return render_template("Inicio2.html", message=mensaje)
    else:
        return render_template("Inicio2.html")

@appyoutube.route("/channel", methods=["GET", "POST"])
def inicio3():
    global enlace3
    global miniatura
    global archivozipDL3
    if request.method=="POST":
        sitio1= request.form["link"]
        sitio4= sitio1.split("/")
        sitio4_1= sitio4[4]
        enlace3=request.form["link"]
        if enlace3!="":
            Canal= Channel(enlace3)
            calidad=request.form["res"]
            if calidad=="audio":
                for video in Canal.videos:
                    video.streams.get_audio_only().download(channel_carpeta)
                    ytcanal= YouTube(Canal.video_urls[0]).thumbnail_url
                    miniatura=ytcanal
                    nombrezipfile= Canal.channel_name+".zip"
                    ruta2= channel_carpeta+"/"+nombrezipfile
                    archivozip= zipfile.ZipFile(ruta2, "w")
                for folder, subfolder, files in os.walk(channel_carpeta):
                    for file in files:
                        if file.endswith(".mp4"):
                            archivozip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), channel_carpeta), compress_type=zipfile.ZIP_DEFLATED)
                            archivozipDL=archivozip.filename
                            archivozipDL2=archivozipDL.split("/Ar")[-1]
                            archivozipDL3="Ar"+archivozipDL2
                archivozip.close()
                for folder, subfolder, files in os.walk(channel_carpeta):
                    for file in files:
                        if file.endswith(".mp4"):
                            os.remove(folder+"/"+file)
                return redirect("/channel"+sitio4_1)
            elif calidad=="alta":
                for video in Canal.videos:
                    video.streams.get_highest_resolution().download(channel_carpeta)
                    ytcanal= YouTube(Canal.video_urls[0]).thumbnail_url
                    miniatura=ytcanal
                    nombrezipfile= Canal.channel_name+".zip"
                    ruta2= channel_carpeta+"/"+nombrezipfile
                    archivozip= zipfile.ZipFile(ruta2, "w")
                for folder, subfolder, files in os.walk(channel_carpeta):
                    for file in files:
                        if file.endswith(".mp4"):
                            archivozip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), channel_carpeta), compress_type=zipfile.ZIP_DEFLATED)
                            archivozipDL=archivozip.filename
                            archivozipDL2=archivozipDL.split("/Ar")[-1]
                            archivozipDL3="Ar"+archivozipDL2
                archivozip.close()
                for folder, subfolder, files in os.walk(channel_carpeta):
                    for file in files:
                        if file.endswith(".mp4"):
                            os.remove(folder+"/"+file)
                return redirect("/channel"+sitio4_1)
            elif calidad=="baja":
                for video in Canal.videos:
                    video.streams.get_lowest_resolution().download(channel_carpeta)
                    ytcanal= YouTube(Canal.video_urls[0]).thumbnail_url
                    miniatura=ytcanal
                    nombrezipfile= Canal.channel_name+".zip"
                    ruta2= channel_carpeta+"/"+nombrezipfile
                    archivozip= zipfile.ZipFile(ruta2, "w")
                for folder, subfolder, files in os.walk(channel_carpeta):
                    for file in files:
                        if file.endswith(".mp4"):
                            archivozip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), channel_carpeta), compress_type=zipfile.ZIP_DEFLATED)
                            archivozipDL=archivozip.filename
                            archivozipDL2=archivozipDL.split("/Ar")[-1]
                            archivozipDL3="Ar"+archivozipDL2
                archivozip.close()
                for folder, subfolder, files in os.walk(channel_carpeta):
                    for file in files:
                        if file.endswith(".mp4"):
                            os.remove(folder+"/"+file)
                return redirect("/channel"+sitio4_1)
            else:
                for video in Canal.videos:
                    video.streams.get_by_resolution(calidad).download(channel_carpeta)
                    ytcanal= YouTube(Canal.video_urls[0]).thumbnail_url
                    miniatura=ytcanal
                    nombrezipfile= Canal.channel_name+".zip"
                    ruta2= channel_carpeta+"/"+nombrezipfile
                    archivozip= zipfile.ZipFile(ruta2, "w")
                for folder, subfolder, files in os.walk(channel_carpeta):
                    for file in files:
                        if file.endswith(".mp4"):
                            archivozip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), channel_carpeta), compress_type=zipfile.ZIP_DEFLATED)
                            archivozipDL=archivozip.filename
                            archivozipDL2=archivozipDL.split("/Ar")[-1]
                            archivozipDL3="Ar"+archivozipDL2
                archivozip.close()
                for folder, subfolder, files in os.walk(channel_carpeta):
                    for file in files:
                        if file.endswith(".mp4"):
                            os.remove(folder+"/"+file)
                return redirect("/channel"+sitio4_1)
        else:
            mensaje= "El canal es incorrecto o el campo esta vacio"
            return render_template("Inicio3.html", message=mensaje)
    else:
        return render_template("Inicio3.html")

@appyoutube.route("/<sitio2>", methods=["GET", "POST"])
def Descarga(sitio2=None):
    if request.method == "POST":
        volver=request.form
        return redirect("/")
    else:
        return render_template("Youtube.html", archivo3=archivo2)

@appyoutube.route("/playlist<sitio3>", methods=["GET", "POST"])
def Descarga2(sitio3=None):
    if request.method == "POST":
        volver=request.form
        return redirect("/playlist")
    else:
        return render_template("Youtube2.html", archivosimg=archivos2, archivorar=archivorarDL3)

@appyoutube.route("/channel<sitio4>", methods=["GET", "POST"])
def Descarga3(sitio4=None):
    if request.method == "POST":
        volver=request.form
        return redirect("/channel")
    else:
        return render_template("Youtube3.html", imagen=miniatura, archivozip=archivozipDL3)

if __name__ == "__main__":
    appyoutube.run(debug=False)