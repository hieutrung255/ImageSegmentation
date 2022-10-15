from lib import *

#http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar
data_dir = "./data"
if not os.path.exists(data_dir):
    os.mkdir(data_dir)

url = 'http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar'
target = os.path.join(data_dir, 'VOC.tar')

if not os.path.exists(target):
    #os.mkdir(target)
    urllib.request.urlretrieve(url, target)
    tar = tarfile.TarFile(target)
    tar.extractall(data_dir)
    tar.close()