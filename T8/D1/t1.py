import pandas as pd
import random
import numpy as np

# Set a random seed for reproducibility
random.seed(42)

# Number of records in the dataset
num_records = 1000

# Create an empty DataFrame
data = pd.DataFrame(columns=['SalePrice', 'LotArea', 'Bedrooms', 'Bathrooms', 'Neighborhood',
                             'YearBuilt', 'GarageArea', 'OverallQual', 'HeatingType'])

# Generate synthetic data with added noise
for _ in range(num_records):
    # Generate property information with more noise
    sale_price = round(np.random.uniform(40000, 600000), 2)
    lot_area = random.randint(1500, 25000)
    bedrooms = random.randint(1, 6)
    bathrooms = random.uniform(1.0, 5.0)
    neighborhoods = ['SuburbA', 'SuburbB', 'Downtown', 'Rural']
    neighborhood = random.choice(neighborhoods)
    year_built = random.randint(1920, 2025)
    garage_area = random.randint(100, 1000)
    overall_qual = random.randint(1, 10)
    heating_types = ['Gas', 'Electric', 'Oil', 'Wood']
    heating_type = random.choice(heating_types)

    data = data._append({
        
        'SalePrice': sale_price,
        'LotArea': lot_area,
        'Bedrooms': bedrooms,
        'Bathrooms': bathrooms,
        'Neighborhood': neighborhood,
        'YearBuilt': year_built,
        'GarageArea': garage_area,
        'OverallQual': overall_qual,
        'HeatingType': heating_type
    }, ignore_index=True)

# Save the dataset to a CSV file
data.to_csv('housing_price_dataset_noisy.csv', index=False)
