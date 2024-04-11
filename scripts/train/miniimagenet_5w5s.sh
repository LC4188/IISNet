python train.py \
 -batch 128 \
 -dataset miniimagenet \
 -gpu 0 \
 -extra_dir your_run \
 -lamb 0.53 \
 -shot 5 \
 -milestones 40 50 \
 -max_epoch 60
