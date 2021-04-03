try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import re


def proc_newlines(instr):
    instr = instr.replace('-\n', '')
    instr = re.sub(r"(?<!\n)\n(?!\n)", " ", instr)
    return instr    

def get_text(fname):
    intext = pytesseract.image_to_string(Image.open(fname), lang='deu')
    intext = proc_newlines(intext)
    return intext

def main():
    print("proc pic")
    output = get_text(fname)
    print(output)
    # print(repr(output))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Hisorical data:')
    parser.add_argument('-f','--file', type=str, default='t2', help="Name of file ") 
    args = parser.parse_args()
    fname = vars(args)["file"]
    main()