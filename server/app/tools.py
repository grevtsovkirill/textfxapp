try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def get_text(fname):
    intext = pytesseract.image_to_string(Image.open(fname), lang='deu')
    return intext

def main():
    print("proc pic")
    print(get_text(fname))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Hisorical data:')
    parser.add_argument('-f','--file', type=str, default='t2', help="Name of file ") 
    args = parser.parse_args()
    fname = vars(args)["file"]
    main()