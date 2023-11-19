import pandas as pd

d = {'age': pd.Series([25,30,35,45,50], index=['i','j','k','l','m']),
     'experiance':pd.Series([5,10,15,20,25], index=['i','j','k','l','m'])
     }
df = pd.DataFrame(d)

print(df)
