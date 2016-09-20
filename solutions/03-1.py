import pandas as pd

def clean_body_type(df):
    mapping = {
        '2 door': 'Coupe',
        'Special Purpose Vehicles/2wd': 'Special Purpose Vehicle 2WD',
        'Special Purpose Vehicles/4wd': 'Special Purpose Vehicle 4WD',
        'Special Purpose Vehicles': 'Special Purpose Vehicle',
        'Standard Pickup Trucks/2wd': 'Standard Pickup Trucks 2WD',
        'Vans Passenger': 'Vans, Passenger Type',
    }
    for old, new in mapping.items():
        df.loc[df.Body_Type == old, 'Body_Type'] = new

    return df


def read_auto_data():
    data = pd.read_excel('data/AutoDB.xlsx', header=(2))
    notnull = data.isnull().sum() < 5
    nonzero = (data == 0).sum() < 5
    selected_columns = data.columns[notnull & nonzero]
    data = data[selected_columns]
    return clean_body_type(data)

