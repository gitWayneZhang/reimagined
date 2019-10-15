def generate_dataset(image_csv, imageKey, labelkey,trainset_count=0):

    data_path_df=pd.read_csv(image_csv)
    image_path_arr = np.array(data_path_df[imageKey].values)
    label_path_arr= np.array(data_path_df[labelkey].values)
    x_trains=[]
    y_trains=[]

    if (trainset_count==0):
        trainset_count=image_path_arr.shape[0]
    for i in range(trainset_count):
        x_train = gdal.Open(image_path_arr[i])
        x_train = np.array(x_train.ReadAsArray())
        x_train = np.rollaxis(x_train,0,3)
        x_trains.append(x_train)
        y_train = gdal.Open(label_path_arr[i])
        y_train = np.array(y_train.GetRasterBand(1).ReadAsArray())
        #try just two categories 0,1
        y_train[y_train==2]=1
        y_train= y_train.reshape(*y_train.shape,-1)  
        y_trains.append(y_train)
      # if need image augmentation uncomment
      #  x_train_aug, y_train_aug=data_aug(x_train,y_train,angel=5)
      #  x_train_flip=np.fliplr(x_train)
      #  y_train_flip=np.fliplr(y_train)
      #  x_train_rotate=np.rot90(x_train)
      #  y_train_rotate=np.rot90(y_train)
        
      #  x_trains.append(x_train_flip)
      #  y_trains.append(y_train_flip)
      #  x_trains.append(x_train_rotate)
      #  y_trains.append(y_train_rotate)

    x_trains=np.array(x_trains)
    y_trains=np.array(y_trains)
    
    print ('x_trains shape: ',  x_trains.shape)
    print ('y_trains shape: ',  y_trains.shape)
    return x_trains, y_trains
