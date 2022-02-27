import numpy as np

def apply_srgan(image):
    image = tf.cast(image[np.newaxis, ...], tf.float32)
    sr = srgan.predict(image)
    sr = tf.clip_by_value(sr, o, 255)
    sr = tf.round(sr)
    sr = tf.cast(sr, tf.unit8)
    return np.array(sr)[0]

train, valid = tfds.load(
    "div2k/bicubic_x4",
    split=["train", "validation"],
    as_supervised=True
)

for i, (lr, hr) in enumerate(valid):
    if i == 6: break

srgan_hr = apply_srgan(lr)