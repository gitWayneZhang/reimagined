class ParallerModelCheckPoint(Callback):
    def __init__(self, single_model):
        self.mode_to_save = single_model
        
    def on_epoch_end(self, epoch, logs={}):
        print(r'save model:" modelpath\DeepLabV3+-Weights-%02d.hdf5'%(epoch+1))
        self.mode_to_save.save_weights(modelpath\DeepLabV3+-Weights-%02d.hdf5'%(epoch+1))
        
# xception, mobilenetv2
basemodel = Deeplabv3(input_shape=(512, 512, 3), classes=1, backbone='mobilenetv2')
model_file = 'checkpoints/DeepLabV3+-Weights-40.hdf5'
if os.path.exists(model_file):
    print('loading model:', model_file)
    basemodel.load_weights(model_file, by_name=True)

parallermodel = create_model(basemodel)
sgd=SGD(lr=0.0001,momentum=0.9)

parallermodel.compile(loss="binary_crossentropy", optimizer=sgd, metrics=["accuracy",mean_iou,"binary_crossentropy",dice_coef])   
#tensorboard = TensorBoard('tflog', write_graph=True)

earlystopper = EarlyStopping(patience = 5, verbose = 1)
checkpointer = ModelCheckpoint(modelpath\model_epochs_deeplabv3_512.h5', verbose = 1, save_best_only = True)
results      = parallermodel.fit(read_X, read_y, validation_split = 0.15, batch_size = 10, epochs = 8,   
                         callbacks = [earlystopper, checkpointer])
