# Predictive-Maintenance-Of-Airlines :airplane:

<img src="https://github.com/smartinternz02/SI-GuidedProject-4669-1626958329/blob/main/Dataset/demo.gif" >

[`Demo Video Link`] : [`https://drive.google.com/drive/folders/1WUa9eRHjRuhR25ubqFBmioQG82jMBXHk?usp=sharing`](https://drive.google.com/drive/folders/1WUa9eRHjRuhR25ubqFBmioQG82jMBXHk?usp=sharing)

[`Feedback Video Link`] : [`https://drive.google.com/file/d/1AEoOTgceC6uzu3oKp2tYd0CfnSfl5FBB/view?usp=sharing`](https://drive.google.com/file/d/1AEoOTgceC6uzu3oKp2tYd0CfnSfl5FBB/view?usp=sharing)
_______________________________________________________________________________________________

## Introduction
Aircraft maintenance is an integral part of ensuring an aircraft is safe for operations. Poor
maintenance planning can lead to devastating financial results for air carriers and keep
aircraft grounded, passengers waiting and can even lead to flight cancellations.
Additionally, an inaccurate overview of maintenance causes overstocking of surplus aircraft
parts, resulting in air carriers losing vast sums of money.
To increase operational reliability and cost saving measures, aircraft operators follow
aircraft maintenance programs. There are three well-known types of maintenance:
reactive, preventive and predictive. Reactive maintenance refers to a timeline in which a
particular part of an aircraft is used to its limits and repairs are only performed after a
failure. This method is usually costly and dangerous for operational safety. Therefore,
many aircraft operators use preventive aircraft maintenance (PM), also known as planned
maintenance, which refers to a determined timeline of checks on certain airplane
components.
The obvious challenge for carriers is a focused execution, which produces tangible and
demonstrable improvements in cost and reliability. For OEMs accelerating adoption and
profitably monetizing investments in predictive maintenance will be a significant challenge.
Another primary concern is data security. Due to the enormous amount of data that needs
to be processed, it is critical to guarantee that equipment performance data cannot be
accessed by outside parties, and that outside parties are not able to control predictive
maintenance systems

___________________________________________________________________________________________________

## Problem Statement 

The airport is currently carrying scale increases year by year, the traditional method of
airport resource allocation has been unable to adapt to the requirements of the operation
of the airport. Dynamic allocation and scheduling of airport terminal passenger service
resources are one of the most effective ways to improve passenger service levels and
operational efficiency within the terminal, while the relatively accurate passenger traffic
forecasting is the prerequisite for dynamic allocation and scheduling.

_____________________________________________________________________________________________________

## Solution

In this project, we have developed a model to predict the number of international airline
passengers in units of 1000, given a year and a month.
The data ranges from January 1949 to December 1960, or 12 years, with 144 observations.
Prediction for next months is computed based on current year and month traffic.
Dataset link: [`https://www.kaggle.com/chirag19/air-passengers`](https://www.kaggle.com/chirag19/air-passengers)
RNN and LSTM have been used in the development of the model and we have used Flask
to deploy the model as a web application.

______________________________________________________________________________________________________

## Experimental Investigations

[`(1.)`] Data Collection
- Collect the dataset or create the dataset.

[`(2.)`] Data Preprocessing
- Import the libraries
- Reading the dataset
- Handling missing values
- Data Visualization
- Split the data into train and test
- Normalize the data
- Reshape the train and test data

[`(3.)`] Model Building
- Import the model building Libraries
- Initializing the model
- Adding LSTM Layer
- Adding Output Layer
- Configure the Learning Process
- Training and testing the model
- Optimize the Model
- Save the Model

[`(4.)`] Application Building
- Build HTML page.
- Build Python code.

__________________________________________________________________________________________

## Flowchart

<img src="https://github.com/smartinternz02/SI-GuidedProject-4669-1626958329/blob/main/Dataset/flowchart.PNG" >

__________________________________________________________________________________________

## Conclusion

In this project, we presented an effective RNN based predictive maintenance solution for
predictive maintenance of airlines. The model uses LSTM for predicting the number of
passengers in the near future. The model created is shown to have very low loss rate and
high overall accuracy.

__________________________________________________________________________________________

## Future Scope

As part of the future work, we would investigate additional data sources, and expand our
model to predict a large number of different parameters so that airlines can remain wellmaintained.

