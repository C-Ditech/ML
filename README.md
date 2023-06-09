<div align="center">
  
  # Chicken Disease Classification with Feces Images
  
  <img src="https://img.shields.io/github/repo-size/C-Ditech/ML?style=for-the-badge&color=darkgoldenrod">
  <img alt="Visitor Badge" src="https://visitor-badge.feriirawann.repl.co?username=C-Ditech&repo=ML&label=VISITOR&style=for-the-badge&color=238636&contentType=svg">
  <img src="https://img.shields.io/github/contributors/C-Ditech/ML?style=for-the-badge&color=blue"></br></br>
  
</div>

<details>
  
  <summary><h2>Table of Content</h2></summary>
  
  * [Overview](#overview)
  * [Dataset](#dataset)
  * [Data Preparation](#dataprep)
  * [Data Modeling](#datamodel)
    * [Architecture](#architecture)
      * [Proprocess Layer](#preprocess)
      * [DenseNet121](#dense)
      * [Top Layer](#top)
      * [Summary](#summary)
  * [Result](#result)
  
</details>

<h2 id="overview">Overview</h2>

C - Ditech is an Android application that aims to detect diseases in chickens through their feces. The application will be able to detect diseases such as Coccidiosis, Healthy, and Salmonella. Information about the disease and how to handle it will be provided in the app. Our team wants to tackle this problem to help farmers detect diseases early and take appropriate measures to prevent further spread and loss.

<h2 id="dataset">Dataset</h2>

We use **Poultry Diseases Detection** dataset in [Kaggle](https://www.kaggle.com/datasets/kausthubkannan/poultry-diseases-detection) by Kausthub Kannan. The dataset consists of 4 directories. Each directory contains images in jpeg format. There are 4 classes 

* Coccidiosis (2103 images)
* Salmonella (2057 images)
* Newcastle diseases (376 images)
* Healthy poultry (2276 images)

The images are feces of the poultries with random image sizes and orientations. The total images in this dataset are 6812 images of feces and have a size of 8.64GB
  
<h2 id="dataprep">Data Preparation</h2>

<div align="center">
  
  ![Sample Images](https://github.com/C-Ditech/ML/blob/main/assets/samples.png)
 
</div>

In data preparation, images will retrieve from each directory with [`tensorflow.keras.utils.image_dataset_from_directory`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/image_dataset_from_directory) function because this function generate a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset) which is can use method [`cache`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#cache) and [`prefetch`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch) function to optimize I/O operations and speed up training process. Considering the dataset above, we have an unbalanced class of Newcastle disease. If we are still practicing with unbalanced data, it'll affect real accuracy such as f1, precision, recall, and support. So we'll downsample all classes except the NCD class. The total images of each class must be the same as the others. For each class, we'll make it as large as the NCD class which is 376 images.

<div align="center">
    
  <img src="https://i1.wp.com/dataaspirant.com/wp-content/uploads/2020/08/17-undersampling.png" width=50% height=50%>
    
</div>

Then we'll apply some augmentations to minimize overfitting the model with our training data like; flip horizontal, flip vertical, random contrast, and random brightness. We make augmentation layers part of our model so it'll run on-device, synchronously with the rest of your layers, and benefit from GPU acceleration. And then, we resize our input images to `224x224`, this number have to defined earlier because we'll use transfer in the next step that required a specific image size. Lastly, we split the dataset into 2 which are the training dataset and the validation dataset with a ratio of 80% : 20%

<h2 id="datamodel">Data Modeling</h2>
In data modeling, we'll do transfer learning to quickly get a good model. If we build a model from scratch it will take a lot of time for training, especially with time-tight projects it is impossible to get a good model. Now, in the transfer learning below, we will use some of the pre-training models provided in the Keras application. The model we chose was one that was less than 50MB in size. 

The model architecture of this model is simply. This is the detail of model:

* Augmentation layer
* Rescaling layer
* Pretrained model (`DenseNet121`)
* Average Pooling
* Dense layer (`128 unit size`, `relu`)
* Dropout (`0.3 rate`)
* Dense layer (`4 unit size`, `softmax`)

<h3 id="architecture">Architecture</h3>

<details>
  
  <summary><h4 id="preprocess">Preprocess Layer</h4></summary>
  
  ![preprocess_image](https://github.com/C-Ditech/ML/blob/main/assets/preprocess.png)

</details>

<details>
  
  <summary><h4 id="dense">DenseNet121</h4></summary>
  
  <img src="https://github.com/C-Ditech/ML/blob/main/assets/densenet121_simple2.png" width=50% height=50%>
  
  <img src="https://github.com/C-Ditech/ML/blob/main/assets/densenet121_simple.png" width=75% height=75%>
 
</details>

<details>
  
  <summary><h4 id="top">Top Layer</h4></summary>
  
  ![preprocess_image](https://github.com/C-Ditech/ML/blob/main/assets/top.png)

</details>

<details>
  
  <summary><h4 id="summary">Summary</h4></summary>
  
  ![preprocess_image](https://github.com/C-Ditech/ML/blob/main/assets/summary.png)

</details> 

<h2 id="result">Result</h2>

<div align="center">
    
  ![chart](https://github.com/C-Ditech/ML/blob/main/assets/chart.png)

  ![accuracy](https://github.com/C-Ditech/ML/blob/main/assets/accuracy.png)

  ![confusion matrix](https://github.com/C-Ditech/ML/blob/main/assets/conf.png)

</div>
