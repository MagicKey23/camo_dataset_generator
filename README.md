# Camouflaged Dataset Generator
> **Developers:** 
> [Kaney Nguyen](https://github.com/MagicKey23/) &
> [Martin Navarrete](https://github.com/mnavarrete12) 
<div align="center">
<figure>
    <a href="./">
        <img src="./img/img22.png" width="79%"/>
    </a>
    <div class = "text-align:center">
    <figcaption>Figure 1 - Camouflaged with a pyramid</figcaption>
    </div>
</figure>

</div>


<div align="center">
<figure>
    <a href="./">
        <img src="./img/img22_GT.png" width="79%"/>
    </a>
    <div class = "text-align:center">
    <figcaption>Figure 2 - Ground Truth</figcaption>
    </div>
</figure>

</div>

## Introduction
- Updating Soon


## Video Demo.

...


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


## How to use


``` shell

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

</details>

## License

PFNET_Ease is available under two different licenses:
- **MIT License**: Refer to License.txt 
- The source code is free for research and education use only. Any commercial usage should get formal permission first.


