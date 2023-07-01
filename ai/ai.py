import numpy as np

import tensorflow as tf
from tensorflow.python.saved_model import tag_constants
from keras_cv.models.stable_diffusion.clip_tokenizer import SimpleTokenizer


class StableDiffusion():
    def __init__(self):
        self.PADDING_TOKEN = 49407
        self.MAX_PROMPT_LENGTH = 77

    def build_model(self):
        self.tokenizer = SimpleTokenizer()

        saved_model_loaded = tf.saved_model.load(
            "./diffusion_model/1/", tags=[tag_constants.SERVING]
        )
        self.diffusion_predict_fn = saved_model_loaded.signatures["serving_default"]

        saved_model_loaded = tf.saved_model.load(
            "./text_encoder/1/", tags=[tag_constants.SERVING]
        )
        self.text_encoder_predict_fn = saved_model_loaded.signatures["serving_default"]

        saved_model_loaded = tf.saved_model.load("./decoder/1/", tags=[tag_constants.SERVING])
        self.decoder_predict_fn = saved_model_loaded.signatures["serving_default"]

    def predict(self, text: str, batch_size: int = 1, num_steps: int = 25) -> np.ndarray:

        batch_size = tf.constant(batch_size)
        num_steps = tf.constant(num_steps)

        tokens = self.tokenizer.encode(text)
        tokens = tokens + [self.PADDING_TOKEN] * (self.MAX_PROMPT_LENGTH - len(tokens))
        tokens = tf.convert_to_tensor([tokens], dtype=tf.int32)

        encoded_text = self.text_encoder_predict_fn(
            tokens=tokens,
            batch_size=batch_size,
        )

        latents = self.diffusion_predict_fn(
            batch_size=batch_size,
            context=encoded_text["context"],
            num_steps=num_steps,
            unconditional_context=encoded_text["unconditional_context"],
        )

        decoded_images = self.decoder_predict_fn(latent=latents["latent"])
        return decoded_images["generated_images"].numpy()