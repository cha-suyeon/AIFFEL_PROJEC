from tensorflow.python.keras import applications
def get_feature_extractor(input_shape=(None, None, 3)):
    vgg = applications.vgg19.VGG19(
        include_top = False,
        weights = "imagenet",
        input_shape=input_shape
    )
    # 아래 vgg.layers[20]은 vgg 내의 마지막 conv layer입니다.
    return Model(vgg.input, vgg.layers[20].output)