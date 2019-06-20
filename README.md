# Video2Image
Convert Video to image files Python

# Parameters
+ **--input_path**
  * you should use directory path (contains video files) or video file path
  * 비디오 파일이 있는 디렉토리의 경로나 비디오 파일의 경로를 입력해야 합니다.
  * after my code check input path, extract video files
  * 코드에서 `input_path`를 확인한 후, 비디오 파일들을 이미지로 전환합니다.

+ **--video_type**
  * You can set the possible extensions for the files in the directory or the video files.
  * 디렉토리 내 파일이나 비디오 파일에 대해 가능한 확장자를 설정할 수 있습니다.
  * `default='avi,mp4,mpg,mpeg,mov'`

+ **--fps**
  * this parameter means frame per second from video files.
  * 해당 파라미터는 비디오 파일로부터 초당 몇 프레임을 추출할 것인지를 의미합니다.
  * example1) parameter fps = 1, video file(fps 30)
  *          every 1s -> save 1 image
  * example2) parameter fps = 3, video file(fps 30)
  *          every 1s -> save 3 image
  * `default=1`

## Using Directory Path


## Using File's Path
