import os


class Exercise1:

    def __init__(self, video):
        self.video = video
        pass

    def convert(self, output, compression):
        print(self.video)
        if compression == 'VP8':
            os.system('ffmpeg - i ' + self.video + ' - c: v libvpx - b: v 1 M - c: a libvorbis ' + output)
        elif compression == 'VP9':
            os.system('ffmpeg -i ' + self.video + ' -c:v libvpx-vp9 -b:v 2M' + output)
        elif compression == 'h265':
            os.system('ffmpeg -i ' + self.video + ' -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k ' + output)
        elif compression == 'AV1':
            os.system('ffmpeg -i ' + self.video + ' -c:v libaom-av1 -crf 30 -b:v 0 ' + output)
        return True


def comparison(video1, video2):
    command = 'ffplay -v warning -f rawvideo -video_size 800x400 -video-size /dev/zero -vf movie=' + video1 + ',scale=400x400 [mv2] ; movie=' + video2 + ',scale=400x400 [mv1]; [in][mv1] overlay=0:0 [tmp]; [tmp][mv2] overlay=400:0'
    os.system(command)


a = Exercise1('BBB720.mp4')
a.convert('output1.mp4', 'VP8')
a.convert('output2.mp4', 'VP9')

comparison('output1.mp4', 'output2.mp4')
