# Camouflaged Dataset Generator
> **Developers:** 
> [Kaney Nguyen](https://github.com/MagicKey23/) &
> [Martin Navarrete](https://github.com/mnavarrete12) 

## Introduction

- In the ever-evolving landscape of computer vision and machine learning, one constant remains: the need for high-quality labeled data. Introducing the Camouflaged Image Generator, a powerful tool designed to revolutionize the image labeling and data generation process for researchers, developers, and AI enthusiasts.
- Labeling images for object segmentation is a time-consuming task that often demands meticulous attention to detail. Our Camouflaged Image Generator steps in as your trusty ally, streamlining and expediting the labeling process with unparalleled efficiency. By harnessing advanced algorithms, this tool empowers researchers to effortlessly generate images embedded with target segmentation.
- Our mission is to empower researchers and developers with tools that amplify their capabilities. The Camouflaged Image Generator epitomizes this ethos by providing a seamless solution to a persistent challenge. Whether you're an AI researcher exploring the boundaries of object detection or a developer seeking to train robust machine learning models, our generator equips you with the means to achieve your goals more efficiently.

## Key Features:
- **Swift Segmentation Generation**: Say goodbye to laborious manual segmentation. Our generator swiftly incorporates target segmentation into images, significantly reducing the time investment required for data labeling.
- **Negative Image Synthesis**: Enhance your training dataset with ease. The Camouflaged Image Generator doesn't stop at positive examples – it creates negative images as well. This ingenious feature bolsters the diversity of your dataset and simplifies the training process.
- **Unleash Innovation**: With the burden of repetitive data generation lifted, you're free to channel your energy into innovation. Propel your research forward, experiment with cutting-edge techniques, and unlock new possibilities in the realm of computer vision.

## Video Demo.


https://github.com/MagicKey23/camo_dataset_generator/assets/22732906/7909b70f-3347-423b-a8f8-e39e1161e703



## Use Case
- Generate Camouflaged Dataset
- Save time from labeling dataset

## Tested OS
- MacOS(M1/M2 Chipset)
- Window


## Installation


``` shell

REQUIRED:
BLENDER 2.79a or 2.79b other version won't work

# clone the git hub
git clone https://github.com/MagicKey23/camo_dataset_generator
# go to code folder
cd camo_dataset_generator
# apt install required packages
pip install -r requirements
```


## Help

``` shell
python main.py --help
  -h, --help                   show this help message and exit
  --width WIDTH                Width of the image (Minimum value: 0)
  --height HEIGHT              Height of the image (Minim value: 0)
  --polygon_size POLYGON_SIZE  Minimum perimeter of a polygon (Minimum value: 0)
  --color_bleed COLOR_BLEED    Bleeding of the colors, i.e. number of neighbouring polygons with the same color
  --colors COLORS              List of all the colors.
  --max_depth MAX_DEPTH        Maximum depth for creating the polygon
  --num_spot NUM_SPOT          Number of spots (Minimum value: 0)
  --radius RADIUS              Dictionary with the min and max radius
  --spot_var SPOT_VAR          Variation for the sampling, i.e. how far it goes looking for the color for the spot.
  --pixel_scale PIXEL_SCALE    Percentage of pixelization (Between 0 and 1)
  --pixel_var PIXEL_VAR        Variation for the sampling, i.e. how far it goes looking for the color for the spot.
  --density DENSITY            Density of the pixels, i.e. inverse of the size of the pixels.

```


## How to use camogen 

Refer to : http://www.happyponyland.net/camogen.php to get a preview
Make sure to have background and foreground folder
``` shell
python main.py

Taking config input...

Option:
1. Camo Generator
2. Image Generator

=>1

Enter background folder number, ex: 1 for background1 or 2 for background2
#This save file to background1 to add more folder simply add background3 or background4 so on
=>1
How many image?
=> 100
Example Output:
./background//background_blots_1.jpg
./foreground1/foreground_blots_1.jpg
./background//background_blots_1.jpg
./foreground1/foreground_blots_2.jpg
./background//background_blots_1.jpg
./foreground1/foreground_blots_3.jpg
./background//background_blots_1.jpg
./foreground1/foreground_blots_4.jpg
./background//background_blots_1.jpg
./foreground1/foreground_blots_5.jpg
./background//background_blots_1.jpg
./foreground1/foreground_blots_6.jpg
./background//background_blots_1.jpg
./foreground1/foreground_blots_7.jpg
```


## How to use image generator

Check List:

- [ ] .Obj file in foregroundObjects folder
- [ ] camo image in background and foreground folders
- [ ] Blender 2.79 install

``` shell
python main.py
Taking config input...

Option:
1. Camo Generator
2. Image Generator
=> 2
Input Valid!
run option 2
Try Program Files path
AL lib: (EE) UpdateDeviceParams: Failed to set 44100hz, got 48000hz instead
found bundled python: C:\Program Files\Blender Foundation\Blender\2.79\python
Enter Resolution X: 
=> 800
Enter Resolution Y:
=> 600
Negative Enable ? Y/N: 
=> y
Enter amount of images to generate: 
-> 100
which index to start from (images will be overwritten if starting at an already existing index) :
=>1
Enter Generate Image
1

:\Users\Kaney\Downloads\ImageGen-20230627T103115Z-001\ImageGen/outputFiles/img1
Fra:1 Mem:17.87M (0.00M, Peak 17.87M) | Time:00:00.00 | Preparing Scene data
Fra:1 Mem:18.31M (0.00M, Peak 18.32M) | Time:00:00.00 | Preparing Scene data
Fra:1 Mem:18.31M (0.00M, Peak 18.32M) | Time:00:00.00 | Creating Shadowbuffers
Fra:1 Mem:18.31M (0.00M, Peak 18.32M) | Time:00:00.00 | Raytree.. preparing
Fra:1 Mem:18.31M (0.00M, Peak 18.32M) | Time:00:00.00 | Raytree.. building
Fra:1 Mem:18.33M (0.00M, Peak 18.35M) | Time:00:00.00 | Raytree finished
Fra:1 Mem:18.33M (0.00M, Peak 18.35M) | Time:00:00.00 | Creating Environment maps
Fra:1 Mem:18.33M (0.00M, Peak 18.35M) | Time:00:00.00 | Caching Point Densities
Fra:1 Mem:18.33M (0.00M, Peak 18.35M) | Time:00:00.00 | Sce: Scene Ve:12 Fa:7 La:2
Fra:1 Mem:18.33M (0.00M, Peak 18.35M) | Time:00:00.00 | Loading voxel datasets
Fra:1 Mem:18.33M (0.00M, Peak 18.35M) | Time:00:00.00 | Sce: Scene Ve:12 Fa:7 La:2
Fra:1 Mem:18.33M (0.00M, Peak 18.35M) | Time:00:00.00 | Sce: Scene Ve:12 Fa:7 La:2
Fra:1 Mem:18.33M (0.00M, Peak 18.35M) | Time:00:00.00 | Volume preprocessing
Fra:1 Mem:18.33M (0.00M, Peak 18.35M) | Time:00:00.00 | Sce: Scene Ve:12 Fa:7 La:2
Fra:1 Mem:18.33M (0.00M, Peak 18.35M) | Time:00:00.00 | Sce: Scene Ve:12 Fa:7 La:2
Fra:1 Mem:31.09M (0.00M, Peak 36.46M) | Time:00:00.03 | Scene, Part 24-130
Fra:1 Mem:27.96M (0.00M, Peak 36.46M) | Time:00:00.03 | Scene, Part 3-130
Fra:1 Mem:30.70M (0.00M, Peak 36.46M) | Time:00:00.04 | Scene, Part 2-130
Fra:1 Mem:32.03M (0.00M, Peak 36.46M) | Time:00:00.04 | Scene, Part 4-130
Fra:1 Mem:32.52M (0.00M, Peak 36.46M) | Time:00:00.04 | Scene, Part 10-130
Fra:1 Mem:33.95M (0.00M, Peak 36.46M) | Time:00:00.04 | Sc
```
## Citation

```
@Software{Camouflaged Generator,
    author    = {Kaney Nguyen, Martin Navarrete},
    title     = {PFNet_Ease},
    webpage = {[https://github.com/MagicKey23/PFNet_Ease/](https://github.com/MagicKey23/camo_dataset_generator)},
    month     = {April},
    year      = {2023}
}

```


## Acknowledgements

<details><summary> <b>Expand</b> </summary>

* [https://github.com/glederrey/camogen](https://github.com/glederrey/camogen)
* [http://www.happyponyland.net/camogen.php](http://www.happyponyland.net/camogen.php)
</details>

## License

PFNET_Ease is available under two different licenses:
- **MIT License**: Refer to License.txt 
- The source code is free for research and education use only. Any commercial usage should get formal permission first.


