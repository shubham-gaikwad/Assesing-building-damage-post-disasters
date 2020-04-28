import os
import shutil
import random

images_dir = '/home/abhirag/ONLY_PORTUGAL/images/'
labels_dir = '/home/abhirag/ONLY_PORTUGAL/labels/'

val_dir = '/home/abhirag/ONLY_PORTUGAL/validation/'

#######################################################################################################################

if os.path.exists(val_dir):
	shutil.rmtree(val_dir)
	print('DELETED EXISTING VAL DIR')
	os.mkdir(val_dir)
	print('CREATED VAL DIR')
else:
	os.mkdir(val_dir)
	print('CREATED VAL DIR')

################

# TEMPLATES 
# /home/abhirag/ONLY_PORTUGAL/labels/portugal-wildfire_00000000_post_disaster.json
# /home/abhirag/ONLY_PORTUGAL/images/portugal-wildfire_00000000_post_disaster.png

###############

files = [images_dir + i for i in os.listdir(images_dir)]

nums = set([i.split('/')[-1].split('_')[1] for i in files])

nums_to_transfer = random.sample(nums, 369)

for x in nums_to_transfer:
	a = '/home/abhirag/ONLY_PORTUGAL/labels/portugal-wildfire_' + x +'_post_disaster.json'
	b = '/home/abhirag/ONLY_PORTUGAL/labels/portugal-wildfire_' + x +'_pre_disaster.json'
	c = '/home/abhirag/ONLY_PORTUGAL/images/portugal-wildfire_' + x +'_post_disaster.png'
	d = '/home/abhirag/ONLY_PORTUGAL/images/portugal-wildfire_' + x +'_pre_disaster.png'

	# shutil.copy(a, val_dir)
	# shutil.copy(b, val_dir)
	# shutil.copy(c, val_dir)
	# shutil.copy(d, val_dir)

	shutil.move(a, val_dir)
	shutil.move(b, val_dir)
	shutil.move(c, val_dir)
	shutil.move(d, val_dir)

#######################################################################################################################

