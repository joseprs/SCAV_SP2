import os


def stream(input_video, ip, port):
    command = 'ffmpeg -i ' + input_video + ' -v 0 -vcodec mpeg4 -f mpegts udp://' + ip + ':' + port
    os.system(command)


stream('BBB720.mp4', '127.0.0.1', '44100')
