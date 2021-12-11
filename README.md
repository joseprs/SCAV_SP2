# SCAV_SP2

## Exercise 1
We have created a class called Exercise1, that has a unique argument that is the name of the video we want to convert and apply the compression. Then, we can call the convert function and the way that we want to do it (VP8, VP9, h265, AV1).

## Exercise 2
This is a simple function with a single command, that we use to display the resulting two videos from above.

## Exercise 3 & 4
We have acheved, with FFMPEG, to create the streaming video to udp://127.0.0.1 using the port 44100 (normally used for local purposes) using the command that we can see on the script (function "streaming"). Furthermore, it also applies a MPEG4 codification.
Due to this codification and other compression and VLC settings, the video is not really good and desn't has a good quality when we open it from VLC (as we can see in the following picture).

<img width="1280" alt="Captura de pantalla 2021-12-11 a las 18 51 01" src="https://user-images.githubusercontent.com/59847264/145687775-57620162-9fd9-4fa7-9bab-a20044963543.png">
If we observe the result, we can think that this poor quality is because of the motion compensation (predicted frames) from the MPEG encoding.
 
But if we open it with the terminal, with this command "ffplay udp://127.0.0.1:23000", we can see it with a very good quality (as in the following image):

<img width="721" alt="Captura de pantalla 2021-12-11 a las 18 52 13" src="https://user-images.githubusercontent.com/59847264/145687812-4d30e867-2267-42a8-a45d-fd60b91227b8.png">

The function that does the streaming also has the option to decide which ip and port to use.
