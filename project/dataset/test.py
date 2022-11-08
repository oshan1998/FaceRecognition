import argparse
import  cv2 as cv
import numpy as np
def volumeOfCylinder(h,r):
    return (np.pi*r**2*h)
parser = argparse.ArgumentParser(description="finding volume of a cylider.",prog="Cylidro",)
parser.add_argument('height',type=int,help="type the height of the cylider")
parser.add_argument('radius',type=int,help="type the radius of the cylider")
args = parser.parse_args()
if __name__=="__main__":

    print(volumeOfCylinder(args.height,args,radius))