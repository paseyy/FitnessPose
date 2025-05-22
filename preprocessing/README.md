# Preprocessing Pipeline
After obtaining the pose data from ViTPose as `json` files, we need to process them before training

## 1. Conversion to `.pkl` dataset
For each of the three labels `correct`, `elbows_error` and `knees_error`, we run `data_transformations` in order to convert them into a `pkl` file, which is what PoseConv3D expects for training.
This does several things:
1. **Discard superfluous keypoints**: Since PoseConv3D expects only the 17 keypoints that COCO uses, we can discard most of the keypoints detected by ViTPose, that also includes hands and face keypoints.
2. **Identify the main subject**: In case ViTPose detects multiple people in the video, we identify the person that is doing the exercise. <code style="color : red">(TODO: HOW? Biggest bounding box? Longest time in frame? Most stable bounding box?)</code>
3. **Clean invalid keypoints**: In case we have `inf` or `NaN` values, we discard the frame keypoints.
3. **Split** the data into train, test and validation set.
4. **Save the data** to a `.pkl` file that corresponds to the format expected by PoseConv3D.

## 2. Combining the `.pkl` files
We run `combine_pickle.py` in order to combine the `.pkl` files into one, since that is the format expected by PoseConv3D.

## 3. Correcting the frame counts
We run `correct_frame_count.py` in order to correct invalid frame counts in the videos.
Since we discard frames that do not include the main subject, the number of keypoints might not match the number of frames in the video.

## 4. Relabeling the data
We run `relabel_pickle.py` in order to relabel the dataset.
We noticed that unlike how we processed our data, the authors of Fitness-AQA trained a model for each error separately.
Therefore, we also split our dataset into two, one to detect knees-error and the other to detect elbows-error.