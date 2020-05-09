# Extract slides from video
Have you ever had a video that you want to extract the image? 
Have you ever had a class recorded but you want to have the slides?

Exctracting slides would allow you to generate your pdf from your video.

## Installation

Instal [python](https://www.python.org/downloads/)

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
    pip install -r requirements.txt 
    pip3 install -r requirements.txt 
```

## Usage
Move you video to the folder `videos`.

From the shell run if you have `python`
```bash
python main.py video_name output_name(opitonal)
```
or if you have `python3`
```bash
python3 main.py video_name output_name(opitonal)
```
The video_name shout be with the format: `exmaple.mp4`

The `output_name` is  optional, 
If there is not `output_name` would be use the `input_name`

## Results
Would generate a pdf in `pdfs/` with the `output_name`


## Settings
There is a file `settings.py` where you can configurate:

`SKIPFRAME` (60): The number of frames the video skip to generate the image. 

`THRESHOLD` (80%): The percentage requirement between two frames to save the image.

`DELETE_IMAGES` (true): Is a boolean to know if you want to keep the images or deleted

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## License
[MIT](https://choosealicense.com/licenses/mit/)
