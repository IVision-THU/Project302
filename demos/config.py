'''
All configurations are set here  
'''
# detector mtcnn model
detector_mtcnn = '../models/mtcnn/';

# detector rfcn  model
detctor_rfcn = '../models/detection/detector_rfcn_1_0_0';

# tracker Goturn model
tracker_goturn = '../models/tracker/Goturn_1_0_0';

GPU_MODE = False;

GPU_DEVICE = 0;

CAMERA_INDEX = 0;

# parameters for detection

detect_w = 320; # width of input image

detect_h = 240; # height of input image

detect_minsize = 30 # minsize of image pyramid

detect_threshold = [0.8, 0.9, 0.8] # thresholds for P-Net, R-Net and O-Net6
detect_factor = 0.609 # resizing factor of image pyramid

# parameters for tracking

track_minsize = 20 # minsize of image pyramid

track_threshold = [0.6, 0.7, 0.7] # thresholds for P-Net, R-Net and O-Net

track_factor = 0.4 # resizing factor of image pyramid



if '__name__' == '_main__':
	print('This is configuration files \n');


