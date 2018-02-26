import scipy.io
import torch
import os
import numpy as np
# from cv2 import imshow
# import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def rank_save(img_dir):
    base = 'D:\Lab\dataset\Market-1501-v15.09.15'
    gallery_dir = os.path.join(base, 'bounding_box_test')
    query_dir = os.path.join(base, 'query')
    result = scipy.io.loadmat('D:\Lab\Person_reID_baseline_pytorch-master/pytorch_result.mat')
    query_feature = result['query_f']
    gallery_feature = result['gallery_f']
    # test_img='1483_c3s3_061578_00.jpg'
    # img_dir = input("Input the dir of your image:")
    print(os.path.join(query_dir, img_dir))
    if os.path.exists(os.path.join(query_dir, img_dir)):
        pos = os.listdir(query_dir).index(img_dir)
        # print("position"+ pos)
        score = np.dot(gallery_feature, query_feature[pos])
        index = np.argsort(score)
        index = index[::-1]
        best_index = []
        gallery_imgs = os.listdir(gallery_dir)
        for i in range(10):
            best_index.append(os.path.join(gallery_dir, gallery_imgs[index[i + 1]]))
        f = open("matching_info.txt", 'w')
        for i in range(10):
            f.write(best_index[i] + '\n')
        f.close()
    else:
        print("Dir does not exist")

    # 0080_c6s1_012251_00.jpg
    # img_source = cv2.imread(os.path.join(query_dir,img_dir),0)
    # imshow('source',img_source)
    # img_match = cv2.imread(best_index, 0)
    # imshow('best_matching', img_match)
    # cv2.waitKey(0)