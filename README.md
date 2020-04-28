# EECE4280
Senior Design Repo for Software portion

Using OpenPose https://github.com/CMU-Perceptual-Computing-Lab/openpose

Examples of output
```
command line execution:

// Run from OpenPose root directory
bin\OpenPoseDemo.exe --video media\examples\input.avi --write_video media\examples\output.avi --write_json media\examples\output_json

// --video: Input will be a video file
// --write_video: Process input and output masked video
// --write_json: Create per-frame json files of data, creates directory for output
```

Raw OpenPose Output

```
File:  COCO_val2014_000000000589_keypoints.json
type: JSON (JavaScript Object Notation)
----------------------------------------

Raw Output:

{'people': [{'face_keypoints_2d': [],
             'face_keypoints_3d': [],
             'hand_left_keypoints_2d': [],
             'hand_left_keypoints_3d': [],
             'hand_right_keypoints_2d': [],
             'hand_right_keypoints_3d': [],
             'person_id': [-1],
             'pose_keypoints_2d': [435.174,
                                   211.901,
                                   0.888144,
                                   444.284,
                                   . . .
                                  ],
             'pose_keypoints_3d': []}],
 'version': 1.3}

```

Data after parsing

```

// Parsed Data: (OpenPose Keypoint Map)

OrderedDict([('Nose', x: 435.174	y: 211.901	 confidence:88.8%),
             ('Neck', x: 444.284	y: 219.757	 confidence:88.9%),
             ('RShoulder', x: 432.449	y: 223.646	 confidence:89.7%),
             ('RElbow', x: 463.876	y: 241.978	 confidence:90.0%),
             ('RWrist', x: 484.743	y: 232.818	 confidence:78.9%),
             ('LShoulder', x: 461.196	y: 214.539	 confidence:84.1%),
             ('LElbow', x: 487.358	y: 213.208	 confidence:69.6%),
             ('LWrist', x: 482.086	y: 213.235	 confidence:76.3%),
             ('MidHip', x: 432.506	y: 286.336	 confidence:88.3%),
             ('RHip', x: 420.727	y: 286.33	 confidence:83.1%),
             ('RKnee', x: 392.118	y: 322.872	 confidence:85.0%),
             ('RAnkle', x: 369.905	y: 350.263	 confidence:93.2%),
             ('LHip', x: 444.264	y: 286.333	 confidence:84.0%),
             ('LKnee', x: 471.691	y: 315.039	 confidence:80.6%),
             ('LAnkle', x: 450.749	y: 350.265	 confidence:88.1%),
             ('REye', x: 433.816	y: 205.401	 confidence:94.2%),
             ('LEye', x: 442.9	y: 205.393	 confidence:92.4%),
             ('REar', x: 0	y: 0	 confidence:0%),
             ('LEar', x: 453.323	y: 204.17	 confidence:91.3%),
             ('LBigToe', x: 466.451	y: 360.769	 confidence:73.5%),
             ('LSmallToe', x: 465.17	y: 359.423	 confidence:71.6%),
             ('LHeel', x: 442.945	y: 351.585	 confidence:84.2%),
             ('RBigToe', x: 352.894	y: 358.112	 confidence:81.8%),
             ('RSmallToe', x: 350.35	y: 351.576	 confidence:86.8%),
             ('RHeel', x: 371.137	y: 354.228	 confidence:79.6%)])
```
