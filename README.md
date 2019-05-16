# whiteFrame

Skript to batch process iamges for instagram surrounding them with a white frame keeping the aspect ratio of the input image and resulting in a squared output image.

![example](https://user-images.githubusercontent.com/6838540/57885100-85303780-782a-11e9-9246-2f9c200f4f5a.png)

Current directory as input and output directory surrounding all images in the input directory with a border of 30 pixels on the larger side of the image. The output images will be renamed.

```python whiteFrame.py -i ./ -o ./ -b 30```

Shorthand for the command above with the same default values:

```python whiteFrame.py ```
