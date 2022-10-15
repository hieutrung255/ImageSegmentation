import os.path as osp

def make_datapath_list(root):
    ori_imgpath_template = osp.join(root, 'JPEGImages', '%s.jpg')
    anno_imgpath_template = osp.join(root, 'SegmentationClass', '%s.png')

    #train, val
    train_ids = osp.join(root, 'ImageSets/Segmentation/train.txt')
    val_ids = osp.join(root, 'ImageSets/Segmentation/val.txt')

    train_img_list = list()
    train_anno_list = list()

    for line in open(train_ids):
        img_id = line.strip()
        img_path = (ori_imgpath_template % img_id)
        anno_path = (anno_imgpath_template % img_id)

        train_img_list.append(img_path)
        train_anno_list.append(anno_path)

    val_img_list = list()
    val_anno_list = list()

    for line in open(val_ids):
        img_id = line.strip()
        img_path = (ori_imgpath_template % img_id)
        anno_path = (anno_imgpath_template % img_id)

        val_img_list.append(img_path)
        val_anno_list.append(anno_path)

    return train_img_list, train_anno_list, val_img_list, val_anno_list

if __name__ == '__main__':
    root = './data/VOCdevkit/VOC2012'

    train_img_list, train_anno_list, val_img_list, val_anno_list = make_datapath_list(root)

    print(len(train_img_list))
    print(len(train_anno_list))
    