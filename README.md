### Context

Author: Christine Van Kirk & Alice Chen

Date: Summer 2021

Location: Auburn University, funding through National Science Foundation & Department of Defense


### Explore this repository to see code for this project!

this repository is organized as follows:
 - `template_matching` folder holds images and code (Python) for determining the ground speed between two aerial images
 - `feature_matching` folder holds images and code (Python) for determining whether two images are taken at the same location
 - `dead_reckoning` folder holds code for path determination in GPS-denied environments through mathematical methods


### Abstract:
UAV navigation within GPS-denied environments has become increasingly critical in recent years due to modern heavy reliance on GPS and the rise of UAV use within GPS-denied and GPS-unstable zones. GPS reliance marks on the of the largest weaknesses of most autonomous UAV systems, and the loss of GPS signal often renders many autonomous UAVs as completely coordinately-impaired. To confront this issue, we present the implementation of a navigational system based on terrain imaging and dead reckoning for home-oriented navigation, which is viable even in foreign environments. We explore the possibility of various forms of image processing, such as feature matching and optical flow via template matching, in order to replicate similar data (ground speed, initial and ending orientation comparison) that would have otherwise been produced by GPS outputs. We use traditional dead reckoning methods as a path basis for the initial UAV navigation, and we utilize both physical implementation and formal methods to study the general applicability of this solution.

### Links to Related Work (Computer Vision):
 - https://www.sciencedirect.com/science/article/pii/S1077314207001555
 - https://www.researchgate.net/publication/44198726_BRIEF_Binary_Robust_Independent_Elementary_Features
 - https://arxiv.org/pdf/1710.02726.pdf
 - http://margaritachli.com/papers/ICCV2011paper.pdf
 - https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf
 - https://pubmed.ncbi.nlm.nih.gov/28397758/
 - https://www.researchgate.net/publication/314285930_Comparison_of_Feature_Detection_and_Matching_Approaches_SIFT_and_SURF
 - https://arxiv.org/pdf/1905.01658.pdf


### Research Groups Working on Similar Topics:
 - (TBD)
