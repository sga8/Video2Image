import argparse
import os
import cv2
import time
from datetime import date
import glob

parser = argparse.ArgumentParser()
parser.add_argument('--input_path', type=str, default='', help='input video file\'s path')
parser.add_argument('--output_path', type=str, default='', help='output video file\'s path')
parser.add_argument('--video_type', type=str, default='avi,mp4,mpg,mpeg,mov', help='available video\'s type')
parser.add_argument('--fps', type=int, default=1, help='extract frame per second from video')

args = parser.parse_args()


def extract_frame(file_path):
    file_name_ext = os.path.basename(file_path)
    file_name = file_name_ext.split('.')[0]
    output_path = os.path.join(file_path.replace('/' + file_name_ext, ""), 'result/')
    if not os.path.exists(output_path):
        print('% % % % % % % % %  make result directory  % % % % % % % % %')
        os.mkdir(output_path)

    video = cv2.VideoCapture(file_path)
    video_fps = int(video.get(cv2.CAP_PROP_FPS))
    video_length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    video_length_one = int(video_length / 100)
    video_save_fps = int(video_fps / args.fps)

    extract_today = date.today().strftime('%m%d')
    start = time.time()
    success = True
    count = 1
    save_count = 1
    while success:
        success, image = video.read()
        if success:
            if count % video_save_fps == 0:
                cv2.imwrite(os.path.join(output_path, ('%s_%s_frame%05d.jpg'
                                                       % (extract_today, file_name, save_count))), image)
                save_count += 1
            if count % video_length_one == 0:
                print('########## progress ------ %s (fps: %d) ------ %7.2f%%  (%6d/%6d) ------------------ ##########'
                      % (file_name_ext, video_fps, count / video_length * 100, count, video_length), end='\r')
            count += 1
        else:
                print('########## progress ------ %s (fps: %d) ------ %7.2f%%  (%6d/%6d) ------------------ ##########'
                      % (file_name_ext, video_fps, (count - 1) / video_length * 100, count - 1, video_length), end='\r')
    print('@@@@@@@@@@ complete ------ %s (fps: %d, frames: %6d) -->> image\'s count: %6d ------ %0.2f sec @@@@@@@@@@'
          % (file_name, video_fps, video_length, save_count, time.time() - start), end='\r')
    print()


if __name__ == '__main__':
    video_type_list = args.video_type.split(',')

    if os.path.isfile(args.input_path):
        extract_frame(args.input_path)
    elif os.path.isdir(args.input_path):
        input_path = sorted(glob.glob(os.path.join(args.input_path, '*.*')))
        for f in input_path:
            if f.split('.')[-1] in video_type_list:
                extract_frame(f)

    else:
        print('% % % % % % % % % no file or directory % % % % % % % % %')


