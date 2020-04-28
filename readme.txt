#### project members - Abhirag Nagpure (anagpure@iu.edu), Pranav Gujarati (pgujarat@iu.edu), Shubham Gaikwad (shgaikwa@iu.edu)


## Data download - The data can be doanloaded from website https://xview2.org/

## To run the baseline model - follow the steps from https://github.com/DIUx-xView/xview2-baseline to recreate the baseline model.

## Subset of data ie. Portugal wildfire data has been uploaded to box. link - https://iu.box.com/s/7xx75303xjr1o6g5i50nfbxzq36eozpo

## The trained models, required csv files etc are also uploaded in the link - https://iu.box.com/s/64wg8r9498rvb8dqb1jot5lgdq4xwpt8

## description of ipynb
classification.ipynb - This notebook covers the part of vgg19 feature extraction and then classification on the dot product of vectors
resnet_bottleneck.ipynb - This covers resnet feature extraction and euclidean and manhatten distace
siamese_experiments.ipynb - This cover the siamese training part
siamese_res_on_test_data.ipynb - Siamese testing part
view_polygons - to visualize output

All python notebooks are baseline model related files

## the ipynb files uploaded in the zip uses the files from above link and assumes to be in the same folder.

## THE TRAINING COMMAND FOR SPACENET

python3 /home/abhirag/experiments_on_portugal/spacenet/src/models/train_model.py /home/abhirag/experiments_on_portugal/spacenet_gt/dataSet /home/abhirag/experiments_on_portugal/spacenet_gt/images /home/abhirag/experiments_on_portugal/spacenet_gt/labels -e 50

## THE INFERENCE COMMAND FOR SPACENET - THIS PRODUCES A OUTPUT_JSON.JSON

python3 /home/abhirag/experiments_on_portugal/spacenet/src/models/inference.py --input /home/abhirag/ONLY_PORTUGAL/images/portugal-wildfire_00000029_pre_disaster.png --weights /home/abhirag/experiments_on_portugal/spacenet/models/logs/model_iter_711 --mean /home/abhirag/experiments_on_portugal/spacenet_gt/dataSet/mean.npy --output /home/abhirag/experiments_on_portugal/output_json.json

## GET OUTPUT IMAGE FROM JSON

python3 /home/abhirag/experiments_on_portugal/inference_image_output.py --input /home/abhirag/experiments_on_portugal/output_json.json --output output_image.png


