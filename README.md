# FitnessPose

## TODO
We need to decide on the following specs:
- Which network for pose estimation? What outputs does it produce?
- Which network for classification on skeleton data? What input does it produce? Is it easily finetunable? Or do we need to train from scratch?
- What exactly do we want to predict? Good/Bad overall or per joint? gold standard deviation? Classes of common errors? 
- What and How Much data should we collect?
- Which augmentations do we want to make?
- Framework setup and visualization

## Ideas
- ViTPose: https://paperswithcode.com/paper/vitpose-vision-transformer-foundation-model
- RTMW: https://paperswithcode.com/paper/rtmw-real-time-multi-person-2d-and-3d-whole
- (2D skeleton seq -> Action recognition): https://paperswithcode.com/paper/revisiting-skeleton-based-action-recognition
