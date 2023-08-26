import subprocess

def main():
    print("This program converts mp4 to mp3.\n ")
def converter(inputfile,outputfile):
    ffcommand = ["ffmpeg", "-i", inputfile, "-vn", outputfile]

    try:
        subprocess.run(ffcommand, check = True)
        print("File converted succsessfully!")

    except subprocess.CalledProcessError as e:
        print(e)
        print("File did not convert!")

# converter("video1.mp4", "audio8.mp3")