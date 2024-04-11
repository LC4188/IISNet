python train.py \
 -batch 50 \
 -dataset cub_crop \
 -gpu 0 \
 -extra_dir your_run \
 -lamb 1.5 \
 -shot 5 \
 -milestones 40 50 \
 -max_epoch 60