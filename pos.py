import panda as pd
data = {
    "column1" : [1,2,3,4,5,6,7],
    "column2" : ['a','b','c','d','e','f','g'],
    "column3" : [10.5,20.3,30,6,34,45,56]
    
}   
df = pd.Dataframe(data)
print(df)

# Display basic info

print("\n shape of dataframe (rows,column):",df.shape)
print("Column names : ",df.columns)
print("First 3 rows :\n",df['column'])
# access rows with the help of index
print("Access rows wth index 2 : \n",df.iloc[2])



# 7 different employees including employ name employ id employ department and employee review


import sklearn 
from sklearn.preprocessing import OneHotEncoder

empdata = {
    "emp_10" : [10,20,15,25,30],    "gender" : ['m','f','f','m','f'],
    "remarks" : ["good","best","nice","great"]
    
    
}

edf = pd.DataFrame(empdata)
print(f"orifinal employee data : \n ",edf)
df_pandas_encoded = pd.get_dumies(edf,columns=["gender","remarks"],drop_first = True)
print(f"One-hot encoded data using pandas : \n[df_pandas_encoded]\n")

df = pd.DataFrame(data)
# pandas one hot 

print(f"Original employee data \n(df) ")