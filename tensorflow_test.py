import tensorflow as tf
from tflite_model_maker import model_spec, object_detector

assert tf.__version__.startswith("2")

tf.get_logger().setLevel("ERROR")
from absl import logging

logging.set_verbosity(logging.ERROR)

spec = model_spec.get("efficientdet_lite0")
train_data, validation_data, test_data = object_detector.DataLoader.from_csv(
    "gs://cloud-ml-data/img/openimage/csv/salads_ml_use.csv"
)

model = object_detector.create(
    train_data,
    model_spec=spec,
    batch_size=8,
    train_whole_model=True,
    validation_data=validation_data,
)

model.evaluate(test_data)
model.export(export_dir="./tf_model")
model.evaluate_tflite("model.tflite", test_data)
