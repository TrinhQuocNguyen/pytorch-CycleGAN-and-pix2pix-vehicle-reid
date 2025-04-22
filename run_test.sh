#!./scripts/test_cyclegan.sh
# python test.py --dataroot /old/home/ccvn/Workspace/trinh/data/reid/VeRi2VehicleID/VeRi_styled --name veri2vehicleid_cyclegan --model cycle_gan --phase test --no_dropout

# Vehicleid to Veri
python test.py --dataroot /old/home/ccvn/Workspace/trinh/data/reid/VeRi2VehicleID/VeRi_styled --name veri2vehicleid_small_cyclegan --model cycle_gan --phase test --no_dropout

# Veri to Vehicle
# python test.py --dataroot /old/home/ccvn/Workspace/trinh/data/reid/VeRi2VehicleID/VeRi_styled \
#         --name veri2vehicleid_small_cyclegan --model cycle_gan --phase test --no_dropout --direction BtoA
