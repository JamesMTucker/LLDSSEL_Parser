import sys
import os
import argparse
from lldssel import get_source
# import pandas as pd

def main(args):
    """

    """

    parser = argparse.ArgumentParser()
    parser.add_argument("siglum", help="Specify a siglum")
    
    args = parser.parse_args()
    
    if not os.path.exists('plates/' + str(args.siglum)):
        os.mkdir('plates/' + str(args.siglum))
    
    get_source(args.siglum)

if __name__ == '__main__':
    main(sys.argv[:1])