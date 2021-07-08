# Git repository containing all code used to TCC project

## Files present and not present in this GIT repository
- All codes in-development and necessaries to project
- NWPU VHR-10 and SAR ship detection dataset (SSDD) data sets are not present here, because of their size. However, they can be respectively found at: https://drive.google.com/open?id=1--foZ3dV5OCsqXQXT84UeKtrAqc5CkAE and https://drive.google.com/file/d/1grDw3zbGjQKYPjOxv9-h4WSUctoUvu1O/view?usp=sharing

## Bibliography (In articles folder)
- Fast R-CNN
- Feature Pyramid Networks for Object Detection
- Faster R-CNN
- DyHead 

## TODO steps list:
  Legend:

  :repeat: = On going

  :no_entry_sign: = Aborted

  :white_check_mark: = Done
- :repeat: Create a good bibliography set
- :no_entry_sign: Well understand CNN 
- :no_entry_sign: Create CNN, train it and test it
- :no_entry_sign: Apply CNN with fully-connected NNs to finally detect objects
- :repeat: Read articles to see what's being made nowadays
- :repeat: Read the DyHead (it's the better NN today)

## Important points to follow
- Perform ablation study (turn off some parts and verify what happens, if it really is what it should be)
- Spend at least 10% of the project trying to reject it, with ablation

## Evolution of methods https://paperswithcode.com/sota/object-detection-on-coco
- R-CNN
- Fast R-CNN https://github.com/rbgirshick/fast-rcnn
- Faster R-CNN https://github.com/rbgirshick/py-faster-rcnn
- Detectron https://github.com/facebookresearch/Detectron
- Detectron 2 https://github.com/facebookresearch/detectron2
- DyHead 

## DyHead conclusion
- Usually we have 2 parts in a NN (backbone and heads)
- Backbone: feature extraction
- Heads: use the features to classify
- A good head is capable of scale, spacial and task awareness, it used to be separeted
