#!./scripts/train_cyclegan.sh
# python train.py --dataroot /old/home/ccvn/Workspace/trinh/data/reid/VeRi2VehicleID --name veri2vehicleid_cyclegan --model cycle_gan --display_id 0
# python train.py --dataroot ./datasets/veri2vehicleid --name veri2vehicleid_tmp_cyclegan --model cycle_gan --display_id 0 --gpu_ids '2,3' --batch_size 16 --num_threads 16
python train.py --dataroot /old/home/ccvn/Workspace/trinh/data/reid/VeRi2VehicleID --name veri2vehicleid_cyclegan --model cycle_gan \
                --display_id 0 --gpu_ids '2,3' --batch_size 32 --num_threads 16 --continue_train --epoch_count 100

