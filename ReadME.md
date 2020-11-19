# Python Flask Introduction

This is a quick tutorial which highlihgts the basics of using flask which is a web framework designed for python


# Details

This assignment revolves around creating a book archive API and when the appropriate URL is caled a HTTP request will occur

This Tutorial is based from the following website:

* [Programming Historian](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask) - This link holds the tutorial and important information regarding the use of API's and how to create a python+flask application


___

# Running Application

Before you use this appliaction, the following must be installed in your device:

**Prerequisites**
* Python >= 3 
* Pip >= 18
* Integrated Development Environment (I reccommend __Visual Studio Code__)

**These two components are esstential to have before you can run this application. once both components are installed you can follow this process to use the application**

## Cloning

The first step is to clone this repository to a folder on your device to do so you can copy the following link

<p align="center">
<img src="Images\image1.PNG" width="500">
<p>

In visual studio code if you type in "CTRL+SHIFT+P" you will get a list of commands that can be entered search for **"Git:Clone"** and click on this once it's been found

You will them be prompted to enter the link to clone the repository 

<p align="center">
<img src="Images\image2.PNG" width="500">
<p>

Paste the link here and click **"Clone from Github"**

The project will be then be cloned to the loctaion specified on the device and you can continue onto the next step

____


## Dependencies

This application requires flask to be installed before the application can be fully functional.

Once you have cloned the project open the terminal on Visual studio or command line and change directory using the command **"cd"** followed by the path to the following folder


<p align="center">
<img src="Images\image3.PNG" width="500">
<p>

**Introduction was spelt wrong i know loooool**

Once you have gotten to this folder run the following command **"pip install flask"**
This will take a few minutes to install flask

The application has now ben configured and you can run it

___

## Application In Use

This application is as basic as it gets and functions off passing URL's to create read updae and delete objects

The application uses what's known as **"query parameters"** for some of the URL's this allows users to pass in values that will be sent to the flask server and used appropriately 

URL's

* **localhost:5000/api/books** - Retrives all books
* **localhost:5000/api/getid?id='value'** - Retrives book by id
* **localhost:5000/api/updateid?id='value'&author='value'** - Gets a book by id and updates the author name 
* **localhost:5000/api/removeid?id='value'** - Removes a book by id 
* **localhost:5000/api/create?id='value'&author='value'&title='value'** - Creates a new book with an id author name and title
