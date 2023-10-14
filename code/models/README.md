# Pre-trained Models

## Inputs
Finding input formats for the various pre-trained models we hope to use for
transfer learning.

Review ['Transfer Learning & Fine-Tuning'][1]

The most common incarnation of transfer learning in the context of deep learning is the following workflow:

1. Take layers from a previously trained model.
2. Freeze them, so as to avoid destroying any of the information they contain during future training rounds.
3. Add some new, trainable layers on top of the frozen layers. They will learn to turn the old features into predictions
   on a new dataset.
4. Train the new layers on your dataset.

A last, optional step, is fine-tuning, which consists of unfreezing the entire model you obtained above (or part of it), and re-training it on the new data with a very low learning rate. This can potentially achieve meaningful improvements, by incrementally adapting the pretrained features to the new data.

Potential models:
E.g., Model (Size, params, depth)

### [VGG16][2] (528 MB, 138.4M, 16)

- The default input size for this model is 224 x 224.
- Was trained on Imagenet
- Default is 3 fully connected layers at the top, can disable to define your own layers and then
  re-define *input_shape*
- convert the input images from RGB to BGR, then will zero-center each color channel with respect to the ImageNet
  dataset, without scaling

### [ResNet50V2][3] (98 MB, 25.6M, 103)

- The default input size for this model is 224 x 224.
- Trained on Imagenet
- scale input pixels between -1 and 1

### [InceptionV3][4] (92 MB, 23.9M, 189)

- Trained on Imagenet
- scale input pixels between -1 and 1
- Default input size is 299 x 299 

### [EfficientNetB4][5] (75MB, 19.5M, 258)

- Trained on Imagenet
- EfficientNet models expect their inputs to be float tensors of pixels with values in the [0-255] range
- Input pre-processing is part of the model, as part of a Rescaling layer

Look into ['Build InceptionV3 over a custom input tensor'][6]

[1]: https://keras.io/guides/transfer_learning/
[2]: https://keras.io/api/applications/vgg/#vgg16-function
[3]: https://keras.io/api/applications/resnet/#resnet50v2-function
[4]: https://keras.io/api/applications/inceptionv3/
[5]: https://keras.io/api/applications/efficientnet/#efficientnetb4-function
[6]: https://faroit.com/keras-docs/1.1.1/applications/#build-inceptionv3-over-a-custom-input-tensor
