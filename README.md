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
    * [Hyperparameter Tuning](#tuning)
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

The image that will be used for training is a polygon image that has been extracted from a complete satellite image. After do some extraction process, then we generate a csv file with polygon ID and it's corresponding damage labels. We will use this csv later to input data into the model using flow_from_dataframe. We will apply multiple augmentations to our training data for all polygon images such as ; horizontal flip, vertical flip, rotation, width and height shift. We resize our input images to 128x128, this number is not too small to cause loss of necessary information, but not too large to cause our CNN performance slowed down.

<h2 id="datamodel">Data Modeling</h2>
asdfasdsadf

<h3 id="architecture">Architecture</h3>

<h3 id="tuning">Hyperparameter Tuning</h3>

<h2 id="result">Result</h2>

