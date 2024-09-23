# Base model function
def base_model():
    return DenseNet121(include_top=False, input_shape=INPUT_SHAPE, weights="imagenet")

# Model 1: GAP + Dropout + Dense Layers
def create_model_1():
    model = Sequential([
        base_model(),
        GlobalAveragePooling2D(),
        Dropout(0.5),
        Dense(256, activation='relu'),
        Dropout(0.5),
        Dense(n, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Model 2: GAP
def create_model_2():
    model = Sequential([
        base_model(),
        GlobalAveragePooling2D(),
        Dense(n, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Model 3: GAP + Dropout
def create_model_3():
    model = Sequential([
        base_model(),
        GlobalAveragePooling2D(),
        Dropout(0.5),
        Dense(n, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Model 4: GAP + Dense Layer
def create_model_4():
    model = Sequential([
        base_model(),
        GlobalAveragePooling2D(),
        Dense(256, activation='relu'),
        Dense(n, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Model 5: Dropout + Dense Layer
def create_model_5():
    model = Sequential([
        base_model(),
        Dropout(0.5),
        Dense(256, activation='relu'),
        Dense(n, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Model 6: Dropout
def create_model_6():
    model = Sequential([
        base_model(),
        Dropout(0.5),
        Dense(n, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Model 7: Dense Layers
def create_model_7():
    model = Sequential([
        base_model(),
        Dense(256, activation='relu'),
        Dense(n, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Training and evaluating all models
models = {
    "M1": create_model_1(),
    "M2": create_model_2(),
    "M3": create_model_3(),
    "M4": create_model_4(),
    "M5": create_model_5(),
    "M6": create_model_6(),
    "M7": create_model_7()
}
