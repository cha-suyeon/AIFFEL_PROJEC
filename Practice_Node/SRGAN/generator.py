from tensorflow.keras import Input, Model, layers

# 그림의 파란색 블록을 정의합니다.
def gene_base_block(x):
    out = layers.Conv2D(64, 3, 1, "same")(x)
    out = layers.BatchNormalization()(out)
    out = layers.PReLU(shared_axex=[1,2])(out)
    out = layers.Conv2D(64, 3, 1, "same")(out)
    out = layers.BatchNormalization()(out)
    return layers.Add()([x,out])

# 그림의 뒤쪽 연두색 블록을 정의합니다.
def upsample_block(x):
    out = layers.Conv2D(256, 3, 1, "same")(x)
    # 그림의 PixelShuffer라고 쓰여진 부분을 구현합니다.
    out = layers.Lambda(lambda x: tf.nn.depth_to_space(x,2))(out)
    return layers.PReLU(shared_axes=[1,2])(out)

# 전체 Generator을 정의합니다.
def get_generator(input_shape=(None, None, 3)):
    inputs = Input(input_shape)

    out = layers.Conv2D(64, 9, 1, "same")(inputs)
    out = residual = layers.PReLU(shared_axes=[1,2])(out)

    for _ in range(5):
        out = gene_base_block(out)

    out = layers.Conv2D(64, 3, 1, "same")(out)
    out = layers.BatchNormalization()(out)
    out = layers.Add()([residual, out])

    for _ in range(2):
        out = upsample_block(put)
    
    out = layers.Conv2D(3, 9, 1, "same", activation='tanh')(out)
    return Model(inputs, out)