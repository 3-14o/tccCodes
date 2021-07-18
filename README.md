# Git repository containing all code used to TCC project

## Files present and not present in this GIT repository
- All codes in-development and necessaries to project
- NWPU VHR-10 and SAR ship detection dataset (SSDD) data sets are not present here, because of their size. However, they can be respectively found at: https://drive.google.com/open?id=1--foZ3dV5OCsqXQXT84UeKtrAqc5CkAE and https://drive.google.com/file/d/1grDw3zbGjQKYPjOxv9-h4WSUctoUvu1O/view?usp=sharing

## Latex to write about this work
- https://www.overleaf.com/read/fpfbkkjrmbnb

## Bibliography (In articles folder)
Books:
  - Deep Learning by Goodfellow
Articles:
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

## Youtube videos
- https://www.youtube.com/watch?v=dichIcUZfOw&t=2s&ab_channel=Hedu-MathofIntelligence
- https://www.youtube.com/watch?v=TQQlZhbC5ps&t=1s&ab_channel=CodeEmporium
- https://www.youtube.com/watch?v=m8pOnJxOcqY&ab_channel=CodeEmporium
- https://www.youtube.com/watch?v=W2rWgXJBZhU&ab_channel=CodeEmporium

## DyHead conclusion
- Usually we have 2 parts in a NN (backbone and heads)
- Backbone: feature extraction
- Heads: use the features to classify
- A good head is capable of scale, spacial and task awareness, it used to be separeted

## Convolutive Neural Networks (CNNs)
Several filters, pass them through image and will have the response to this filters. First layers is understandable, e.g.: [1 1 0; 1 0 0; 0 0 0] is searching for curves.
However, going more deeply it becomes unnatural to our brian. It extracts harsh features. Convolution has a property of interpretion 


## Transform method

### Attention heads (as seen in DyHead)
