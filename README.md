Overview
This project provides multiple neural network models based on DenseNet121 as the backbone. The models experiment with different configurations, integrating components like Global Average Pooling (GAP), Dropout, and Dense layers to evaluate their performance on a classification task.

Models Summary
Model 1: GAP + Dropout + Dense Layers
Model 2: GAP
Model 3: GAP + Dropout
Model 4: GAP + Dense Layer
Model 5: Dropout + Dense Layer
Model 6: Dropout
Model 7: Dense Layers
Base Model
All models use DenseNet121 without the top layer and with ImageNet weights as the feature extractor:

python
Copy code
def base_model():
    return DenseNet121(include_top=False, input_shape=INPUT_SHAPE, weights="imagenet")
Training and Evaluation
Each model is compiled with:

Optimizer: Adam
Loss: Categorical Crossentropy
Metric: Accuracy
Access the models via the models dictionary:

python
Copy code
models = {
    "M1": create_model_1(),
    "M2": create_model_2(),
    "M3": create_model_3(),
    "M4": create_model_4(),
    "M5": create_model_5(),
    "M6": create_model_6(),
    "M7": create_model_7()
}
Example Usage
python
Copy code
history = models["M1"].fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))
test_loss, test_acc = models["M1"].evaluate(X_test, y_test)
print(f"Test Accuracy: {test_acc}")
