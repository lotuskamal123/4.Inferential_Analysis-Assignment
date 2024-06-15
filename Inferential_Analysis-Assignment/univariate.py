import pandas as pd
import numpy as np
dataset=pd.read_csv("Placement.csv")
dataset
class univar():
    def QuanQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            #print(columnName)
            if(dataset[columnName].dtype=='object'):
                #print("qual")
                qual.append(columnName)
            else:
                quan.append(columnName)
        return quan,qual
        
    def Central_tendency(dataset,quan):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%","IQR","1.5rule",
                                        "Lesser","Greater","Minimum","Maximum"],columns=quan)
        for columnName in quan:
            descriptive[columnName]['Mean']=dataset[columnName].mean()
            descriptive[columnName]['Median']=dataset[columnName].median()
            descriptive[columnName]['Mode']=dataset[columnName].mode()[0]
            descriptive[columnName]['Q1:25%']=np.percentile(dataset[columnName],25)
            descriptive[columnName]['Q2:50%']=np.percentile(dataset[columnName],50)
            descriptive[columnName]['Q3:75%']=np.percentile(dataset[columnName],75)
            descriptive[columnName]['99%']=np.percentile(dataset[columnName],99)
            descriptive[columnName]['Q4:100%']=np.percentile(dataset[columnName],100)
            descriptive[columnName]['IQR']=descriptive[columnName]['Q3:75%']- descriptive[columnName]['Q1:25%']
            descriptive[columnName]['1.5rule']=1.5* descriptive[columnName]['IQR']
            descriptive[columnName]['Lesser']=descriptive[columnName]['Q1:25%']-descriptive[columnName]['1.5rule']
            descriptive[columnName]['Greater']=descriptive[columnName]['Q3:75%']+descriptive[columnName]['1.5rule']
            descriptive[columnName]['Minimum']=dataset[columnName].min()
            descriptive[columnName]['Maximum']=dataset[columnName].max()
        return descriptive
    
    def find_outlier(Lesser,Greater):
        Lesser=[]
        Greater=[]

        for columnName in quan:
            if(descriptive[columnName]['Minimum']<descriptive[columnName]['Lesser']):
                Lesser.append(columnName)
            if(descriptive[columnName]['Maximum']>descriptive[columnName]['Greater']):
                Greater.append(columnName)
        return Lesser,Greater
    
   