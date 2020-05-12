import embedding as ed
import extraction as ex
import argparse
def main():

    print("This is program about steganography")
    print("The program is builed by Team 2 of L02 from KMA-HaNoi")
    print("How to use?")
    print("Put your images u wanto use to folder named input")
    print("This program have 02 mode are: Embeding and Extraction")
    print("With Embeding use form command like this (below):")
    print("python main.py -i [PATH_HOST_IMAGE] -w [PATH_WATERMARK_IMAGE] -m 0")
    print("With extraction use form command like this (below):")
    print("python main.py -i [PATH_HOST_IMAGE] -w [PATH_WATERMARK_IMAGE] -m 1")
    print("Output will be in folder named output")
    print("=    =   =         =        ==")
    print("=   =    =  =    = =       =  =")
    print("= =      =    ==   =      =    =")
    print("= =      =         =     = = = ==")
    print("=   =    =         =    =        =")
    print("=    =   =         =   =          =")
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=False,
                    help="Host imgae")
    ap.add_argument("-w", "--watermark", required=False,
                    help="Watermark image")
    ap.add_argument("-m", "--mode", required=True,
                    help="Mode to use")

    args = vars(ap.parse_args())
    print(args["mode"])
    if args["mode"] == '0':
        print("Start Embeding")
        ed.embedding(pathhostimge=args["image"], pathwatermarkimage=args["watermark"])
        print("have been done")
    elif args["mode"] == '1':
        ex.extraction()

if __name__ == "__main__":
    main()
