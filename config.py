class Config:
    # Model parameters
    MODEL_PATH = 'models/'
    INPUT_SIZE = (416, 416)  # Standard YOLO input size
    
    # Dataset parameters
    TRAIN_PATH = 'data/train/'
    TEST_PATH = 'data/test/'
    VAL_PATH = 'data/val/'
    
    # Training parameters
    BATCH_SIZE = 32
    EPOCHS = 100
    LEARNING_RATE = 0.001 