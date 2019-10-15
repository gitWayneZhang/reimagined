class cobbDataset(utils.Dataset):
    def load_cobb(self, dataset_dir):
        """Load a subset of the CObb dataset.
           Load a subset of the Cobb dataset from the given dataset_dir.
        """
        # Add classes
        self.add_class("cobb", 1, "building")
        #loading images
        self._image_dir = os.path.join(dataset_dir, "images1/")
        self._mask_dir = os.path.join(dataset_dir, "labels/")
        i=0
        for f in glob.glob(os.path.join(self._image_dir, "*.tif")):
            filename = os.path.split(f)[1]
            self.add_image("cobb", image_id=i, path=f,
                          width=config.IMAGE_SHAPE[0], height=config.IMAGE_SHAPE[1], filename=filename)
            i += 1
            if i>3800:
                break
         
    def load_mask(self, image_id):
        """Load instance masks for the given image.

        Different datasets use different ways to store masks. This
        function converts the different mask format to one format
        in the form of a bitmap [height, width, instances].

        Returns:
        masks: A bool array of shape [height, width, instance count] with
            one mask per instance.
        class_ids: a 1D array of class IDs of the instance masks.
        """
        # If not a COCO image, delegate to parent class.
        """Read instance masks for an image.
        Returns:
        masks: A bool array of shape [height, width, instance count] with one mask per instance.
        class_ids: a 1D array of class IDs of the instance masks.
        """
#        self._mask_dir = os.path.join(dataset_dir, "labels")
        info = self.image_info[image_id]
        fname = info["filename"]
        masks = []
        class_ids = []
        mask_src = skimage.io.imread(os.path.join(self._mask_dir, "1", fname))
        instance_ids = np.unique(mask_src)
#       print (instance_ids)
        for i in instance_ids:
            if i > 0:
                m = np.zeros(mask_src.shape)
                m[mask_src==i] = i
#               print(i)
                if np.any(m==i):
                    masks.append(m)
#                        class_ids.append(class_id)
        try:
            masks = np.stack(masks, axis=-1)        
        except:
            print("no mask found.", info)
            
        return masks.astype(np.bool), np.ones([masks.shape[-1]], dtype=np.int32)
