# Project:
   **Zillow Clustering**

## Goal:
  **Discover the drivers of the log error.**


## Data Dictionary:

**bathroomcnt:** number of bathrooms

**bedroomcnt:** number of bedrooms

**culatedfinishedsquarefeet:** SqFt of total living area

**finishedsquarefeet12:** SqFt of finished living area

**latitude:** latitude of the middle of the property

**longitude:** longitude of the middle of the property

**lotsizesquarefeet:** SqFt of the lot

**yearbuilt:** Year home was built

**structuretaxvaluedollarcnt:** Assessed value of the home

**structuretaxvaluedollarcnt:** Assessed home value

**taxamount:** tax amount of the home

**logerror:** logarithmic error of housing price predictions

**transactiondate:** date sold

## Phases:
### Plan:
- Outline the steps to take for the project
- Create the necessary repositories
- Brainstorm different approaches
- Think of different hypothesis to test on

### Data Acquisition:
-	Data is acquired from the CodeUp Database 
-	Credentials are required in order to access the database
-	Necessary function required to acquire the data can be found in **acquire.py** module.

### Data Preparation:
-	Use propertyusetypeid to filter the dataset to only get the single unit properties
-	Run summary statistics
-	Check and remove null values
-	Check and remove outliers
-	Drop repeated/redundant columns
-	Replace null values
-	Split data into train, test, and validate 
-	All of the necessary functions to reproduce the work in this phase can be found in **wrangle_zillow.py** module.

### Data Exploration
- Explore relationship between various features and the target variable
- Notedown key discoveries
- Cluster to aid exploration
- Perform statistical tests
#### Hypothesis to test:
- Is there a statistically significant difference in the log error of properties with different number of bathrooms
- Is there a statistically significant difference in the log error of properties with different number of bedrooms
- Is there a statistically significant difference in the log error between the clusters created using location features
- Is there a statistically significant difference in the log error between the clusters created using different features of the property
### Modeling & Evaluation
- Create a baseline model
- Decide whether to use clusters as features
- Use Linear Regression algorith to create model
- Train model, caluclate RMSE, and compare with baseline RMSE
- Validate top performing models
- Test with the best perfroming model

### Conclusion
- Summarize the process
- Note down the findings
- Whats next?

## How to reproduce?
- Once credentials are provided
- Download acquire, wrangle_zillow, explore module

