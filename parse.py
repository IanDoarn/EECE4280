import json
from os import path
from collections import OrderedDict
import pprint

KEY_POINT_MAP = [
                "Nose",
                "Neck",
                "RShoulder",
                "RElbow",
                "RWrist",
                "LShoulder",
                "LElbow",
                "LWrist",
                "MidHip",
                "RHip",
                "RKnee",
                "RAnkle",
                "LHip",
                "LKnee",
                "LAnkle",
                "REye",
                "LEye",
                "REar",
                "LEar",
                "LBigToe",
                "LSmallToe",
                "LHeel",
                "RBigToe",
                "RSmallToe",
                "RHeel",
                "Background"
                ]

class Point:
    x, y, c = 0, 0, 0

    def __init__(self, values: list):
        self.x, self.y, self.c = values

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "x: {}\ty: {}\t confidence:{:.4}%".format(
                str(self.x), str(self.y), str(self.c * 100)
            )


class KeyPoints:
    
    def __init__(self, file):
        self.file = path.split(file)[-1]
        self.points = self.__parse(file)

    def __parse(self, file):
        with open(file, 'r') as jf:
            data = json.load(jf)

        key_points = data['people'][0]['pose_keypoints_2d']

        values = []
        mapped = OrderedDict()

        for x, i in enumerate(range(0, len(key_points), 3)):
            values.append(key_points[0 + i : 3 + i])


        for x in zip(KEY_POINT_MAP, values):
            mapped[x[0]] = Point(x[1])

        return mapped


if __name__ == '__main__':
    file = "COCO_val2014_000000000589_keypoints.json"

    print("File: ", file)
    print("type: JSON (JavaScript Object Notation)")
    print('-'*40)
    print('\nRaw Output:\n')

    with open(file, 'r') as jf:
        data = json.load(jf)

    pprint.pprint(data)

    print('\n')

    keypoints = KeyPoints(file)

    print('-'*40)
    print('\nParsed Data: (OpenPose Keypoint Map)\n')

    pprint.pprint(keypoints.points)