import cv2
import os
import sys
import argparse
import numpy as np

def main():
    parser = argparse.ArgumentParser(
                usage="Movie Converte Test",
                add_help = False
            )
    parser.add_argument("-i", "--i_file", type = str, default = "test.avi")
    parser.add_argument("-d", "--dir", type = str, default = "test")
    parser.add_argument("-o", "--out", type = str, default = "test")
    parser.add_argument("-f", "--flag", type = int, default = 0)
    args = parser.parse_args()

    cap = cv2.VideoCapture(args.i_file)
    if not cap.isOpened():
        print("Input File Error!")
        sys.exit()
    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))
    max_cnt = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cnt_fps = np.floor(cv2.CAP_PROP_FPS / 2).astype(np.int32)
    print(cnt_fps)
    o_dir = os.path.join(os.getcwd(), args.dir)
    if not os.path.isdir(o_dir):
        print("Output Dir Error!")
        sys.exit()
    o_file = args.out + "_"
    flag = args.flag
    if flag == 0:
        flag_txt = ""
    else:
        flag_txt = "_mask"
    n = 0
    while True:
        is_image, frame_img = cap.read()
        if is_image and n % cnt_fps == 0:
            if flag > 0:
                ret, frame_img = cv2.threshold(frame_img, 100, 1, cv2.TRRESH_BINARY)
            cv2.imwrite(os.path.join(o_dir, o_file + str(n) + flag_txt + ".png"), frame_img)
        elif n < max_cnt:
            n += 1
            continue
        else:
            break
        n += 1
    print(n)

if __name__ == "__main__":
    main()
