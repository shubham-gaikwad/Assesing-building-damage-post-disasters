import os
import shutil
import random

val_split = 0.2

base = '/home/abhirag/experiments_on_portugal/'

ds = '/home/abhirag/ONLY_PORTUGAL/'

if os.path.exists(os.path.join(base, 'spacenet_gt')):
	shutil.rmtree(os.path.join(base, 'spacenet_gt'))


os.mkdir(os.path.join(base, 'spacenet_gt'))

os.mkdir(os.path.join(base, 'spacenet_gt', 'images'))
os.mkdir(os.path.join(base, 'spacenet_gt', 'labels'))
os.mkdir(os.path.join(base, 'spacenet_gt', 'dataSet'))

for i in [os.path.join(ds, 'masks', j) for j in os.listdir(os.path.join(ds, 'masks'))]:
	shutil.copy(i, os.path.join(base, 'spacenet_gt', 'labels'))
	shutil.copy('/home/abhirag/ONLY_PORTUGAL/images/portugal-wildfire_' + i.split('/')[-1].split('_')[1] + '_pre_disaster.png', os.path.join(base, 'spacenet_gt', 'images'))
	

x = os.listdir(os.path.join(base, 'spacenet_gt', 'labels'))

random.shuffle(x)

with open(os.path.join(base, 'spacenet_gt', 'dataSet', 'train.txt'), 'w') as fp:
	for f in x[:int((1-val_split)*len(x))]:
		fp.write('%s\n' %f)

with open(os.path.join(base, 'spacenet_gt', 'dataSet', 'val.txt'), 'w') as fp:
	for f in x[int((1-val_split)*len(x)):]:
		fp.write('%s\n' %f)

os.system('python3 compute_mean.py /home/abhirag/experiments_on_portugal/spacenet_gt/dataSet/train.txt --root /home/abhirag/experiments_on_portugal/spacenet_gt/images --output /home/abhirag/experiments_on_portugal/spacenet_gt/dataSet/mean.npy')


