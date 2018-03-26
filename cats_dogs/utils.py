# Required libraries
import numpy as np
import glob
import random

#set random seed
np.random.seed(72)

def build_dataset(dataset_sz, valid_split_ratio):
  '''
    Build train and validation dataset
  '''

  tr_files = glob.glob("input/train/*.*")
  cats = [fname for fname in tr_files if "cat" in fname]
  dogs = [fname for fname in tr_files if "dog" in fname]
  
  if dataset_sz == -1:
    #select all images
    sel_cats = cats
    sel_dogs = dogs
  else:
    idx_cats, idx_dogs = np.arange(0, len(cats)), np.arange(0, len(dogs))
    sel_cats = [cats[i] for i in idx_cats[0:dataset_sz//2]]
    sel_dogs = [dogs[i] for i in idx_dogs[0:dataset_sz//2]]

  x = sel_dogs + sel_cats
  y = [0] * len(sel_dogs) + [1] * len(sel_cats)
  data = list(zip(x, y))
  idx = np.arange(0, len(data), 1)
  np.random.shuffle(idx)

  valid_sz = int( valid_split_ratio * len(idx) )
  train_idx, validation_idx = idx[0:-valid_sz], idx[-valid_sz::]
  print("Set size Training: {} | Validation: {}".format(len(train_idx), len(validation_idx)))

  #Build train dataset and validation dataset
  train_data = [ data[i] for i in train_idx  ]
  validation_data = [ data[i] for i in validation_idx ]

  return train_data, validation_data