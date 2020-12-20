import pandas as pd 

'''Example data frame of people of a certain community'''

df = pd.DataFrame(
    {
        'Name': ['Sir Titus Mahwenda', 'Madam Jan Doe', 'Mrs Kate Don'],
        'Age': [26, 35, 71],
        'Sex': ['male', 'female', 'female']
    }
)

print(df)