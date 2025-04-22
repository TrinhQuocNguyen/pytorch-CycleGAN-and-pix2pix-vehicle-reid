




# Training the domain-awareness model with CycleGAN for Vehicle ReID in CORE-ReID V2

More information:
- [CORE-ReID](https://trinhquocnguyen.github.io/core-reid-homepage/): Comprehensive Optimization and Refinement through Ensemble fusion in Domain Adaptation for person re-identification ![new](https://img.alicdn.com/imgextra/i4/O1CN01kUiDtl1HVxN6G56vN_!!6000000000764-2-tps-43-19.png)

- [CORE-ReID V2](https://trinhquocnguyen.github.io/core-reid-v2-homepage/): Advancing the Domain Adaptation for Object Re-Identification with Optimized Training and Ensemble Fusion ![new](https://img.alicdn.com/imgextra/i4/O1CN01kUiDtl1HVxN6G56vN_!!6000000000764-2-tps-43-19.png)


## 1. Preparation

#### Requirements and installation: 

1. Installation: https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix

2. Config your data path in **"run_train.sh"** and **"run_test.sh"** files.
  
## 2. Train models
  - Change **"--dataroot"** parameter to your path.
  - Example: 
  ```Shell
  python train.py --dataroot /old/home/ccvn/Workspace/trinh/data/reid/VeRi2VehicleID --name veri2vehicleid_cyclegan --model cycle_gan \
                --display_id 0 --gpu_ids '2,3' --batch_size 32 --num_threads 16 --continue_train --epoch_count 100
  ```

## 3. Test models/ generate images
  - Change **"--dataroot"** parameter to your path.
  - Example: 
  ```Shell
  python test.py --dataroot /old/home/ccvn/Workspace/trinh/data/reid/VeRi2VehicleID/VeRi_styled --name veri2vehicleid_small_cyclegan --model cycle_gan --phase test --no_dropout
  ```

## 4. Citations
Please cite our paper if you find it useful.
```
@article{,
  author    = {Nguyen TQ, Prima ODA, Hotta K},
  title     = {CORE-ReID: Comprehensive Optimization and Refinement through Ensemble Fusion in Domain Adaptation for Person Re-Identification.},
  journal   = {Software},
  doi       = {https://doi.org/10.3390/software3020012},
  volume    = {3},
  pages     = {227-249},
  year      = {2024},
}
```

## Awareness
Thanks for the authors of this repo: [[CycleGAN and pix2pix in PyTorch]](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)
