import tflite_runtime.interpreter as tflite
import numpy as np
import cv2

'''PATH'''

#content_path = 'C:/Users/user/PycharmProjects/AC_Innovative_Drawing_Board/resource/tflite/bin.jpg'
#style_path = 'C:/Users/user/PycharmProjects/AC_Innovative_Drawing_Board/resource/tflite/style1.jpg'
style_predict_path = 'C:/Users/user/PycharmProjects/AC_Innovative_Drawing_Board/resource/tflite/prediction.tflite'
style_transform_path = 'C:/Users/user/PycharmProjects/AC_Innovative_Drawing_Board/resource/tflite/transfer.tflite'

class ArtisticStyle:

    def __init__(self):
        print('ArtisticStyple: init')
        print(self.__doc__)

    def run_style_predict(self, preprocessed_style_image):
      # Load the model.
      interpreter = tflite.Interpreter(model_path=style_predict_path)

      # Set model input.
      interpreter.allocate_tensors()
      input_details = interpreter.get_input_details()
      interpreter.set_tensor(input_details[0]["index"], preprocessed_style_image)

      # Calculate style bottleneck.
      interpreter.invoke()
      style_bottleneck = interpreter.tensor(
          interpreter.get_output_details()[0]["index"]
          )()

      return style_bottleneck


    def run_style_transform(self, style_bottleneck, preprocessed_content_image):
      # Load the model.
      interpreter = tflite.Interpreter(model_path=style_transform_path)

      # Set model input.
      input_details = interpreter.get_input_details()
      interpreter.allocate_tensors()

      # Set model inputs.
      interpreter.set_tensor(input_details[0]["index"], preprocessed_content_image)
      interpreter.set_tensor(input_details[1]["index"], style_bottleneck)
      interpreter.invoke()

      # Transform content image.
      stylized_image = interpreter.tensor(interpreter.get_output_details()[0]["index"])()

      return stylized_image

    def preprocess_image(self, image, target_dim):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        center = [image.shape[0] / 2 , image.shape[1] / 2]
        h = image.shape[0]
        w = image.shape[1]
        short_dim = min(h, w)
        scale = target_dim / short_dim
        new_h = scale * h
        new_w = scale * w
        x = center[1]*scale - target_dim / 2
        y = center[0]*scale - target_dim / 2

        image = cv2.resize(image, (int(new_w), int(new_h)), interpolation=cv2.INTER_CUBIC)
        crop_img = image[int(y):int(y + target_dim), int(x):int(x + target_dim)]
        return crop_img

    def get_stylized_image(self, content_img, style_img):

        content_img = self.preprocess_image(content_img, 384)
        style_img = self.preprocess_image(style_img, 256)

        content_img = content_img.astype(np.float32)
        style_img = style_img.astype(np.float32)
        content_img = content_img / 255.0
        style_img = style_img / 255.0
        preprocessed_content_image = np.expand_dims(content_img, axis=0)
        preprocessed_style_image = np.expand_dims(style_img, axis=0)

        style_bottleneck = self.run_style_predict(preprocessed_style_image)
        stylized_image = self.run_style_transform(style_bottleneck, preprocessed_content_image)
        stylized_image = np.squeeze(stylized_image, axis=0)
        stylized_image = np.multiply(stylized_image, 255).astype(np.uint8)
        stylized_image = cv2.cvtColor(stylized_image, cv2.COLOR_RGB2BGR)
        cv2.imwrite("C:/Users/user/PycharmProjects/AC_Innovative_Drawing_Board/resource/tflite/stylized_image_yong.jpg",stylized_image)

        return stylized_image
        #cv2.imshow("stylized_image",stylized_image)
        #cv2.waitKey(0)