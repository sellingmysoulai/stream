import pandas as pd
import random
import os

def generate_dataframes_based_on_template(template_path):
    number_of_files = random.randint(1, 100)
    print(f"Number of DataFrames to generate: {number_of_files}")

    # Read the template CSV file to get the DateTime values
    template_df = pd.read_csv(template_path)

    dataframes = {}  # Using a dictionary to store DataFrames with their identifiers

    for file_number in range(1, number_of_files + 1):
        movie_list = ['BowOne', 'BowTwo', 'BowFour', 'BowSix', 'BowNine', 'BowTwelve']
        loclist = ['Studio', 'EG', 'Roffa', 'deStreetzzz', 'Ho Chi Minh-stad']

        # pick a random element from a list of strings
        movie = random.choice(movie_list)
        loc = random.choice(loclist)

        maximum_occupancy = {'BowOne': 1, 'BowTwo': 2, 'BowFour': 4, 'BowSix': 6, 'BowNine': 6, 'BowTwelve': 8}.get(movie, 0)

        # Construct DataFrame identifier
        df_identifier = f'Netherlands#Almelo#{loc}#{movie}-{file_number}'

        # Initialize DataFrame with the 'received_at' column from the template
        new_df = template_df[['DateTime']].copy()
        new_df.rename(columns={'DateTime': 'received_at'}, inplace=True)

        # Generate new 'people_counter_all' values with weighted randomness
        weights = [10] + [1] * maximum_occupancy  # This gives a much higher weight to 0
        new_df['people_counter_all'] = [random.choices(range(0, maximum_occupancy + 1), weights=weights, k=1)[0] for _ in range(len(new_df))]

        # Store the new DataFrame in the dictionary
        dataframes[df_identifier] = new_df

    return dataframes