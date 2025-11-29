# Dataframe means 2D
import pandas as pd

data = {
    "name" : ["Vansh", "Amit", "Anup"],
    "age" : [18, 19, 11] 
}

df = pd.DataFrame(data)
print(df)