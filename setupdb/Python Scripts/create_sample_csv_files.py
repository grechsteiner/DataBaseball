import pandas as pd
import os
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Filter CSV files based on conditions and save to new directory.')
    parser.add_argument('input_directory', type=str, help='Path to the input directory containing the original CSV files')
    parser.add_argument('output_directory', type=str, help='Path to the output directory to save the filtered CSV files')
    return parser.parse_args()


# Define the conditions for selecting rows
# Example: conditions = { 'file1.csv': [{'column_name': 'value1'}, {'column_name': 'value2'}], ... }
conditions = {
    'AllstarFull.csv': [
        {'playerID': 'guerrvl02', 'yearID': '2022', 'gameNum': '0'},
        {'playerID': 'guerrvl02', 'yearID': '2023', 'gameNum': '0'},
        {'playerID': 'bettsmo01', 'yearID': '2022', 'gameNum': '0'},
        {'playerID': 'bettsmo01', 'yearID': '2023', 'gameNum': '0'},
        {'playerID': 'kershcl01', 'yearID': '2022', 'gameNum': '0'},
        {'playerID': 'kershcl01', 'yearID': '2023', 'gameNum': '0'},
        {'playerID': 'greggha01', 'yearID': '1945', 'gameNum': '0'},
        {'playerID': 'galanau01', 'yearID': '1944', 'gameNum': '0'}
    ], 
    'Appearances.csv': [
        {'playerID': 'guerrvl02', 'yearID': '2022', 'teamID': 'TOR'},
        {'playerID': 'guerrvl02', 'yearID': '2023', 'teamID': 'TOR'},
        {'playerID': 'biggica01', 'yearID': '2022', 'teamID': 'TOR'},
        {'playerID': 'biggica01', 'yearID': '2023', 'teamID': 'TOR'},
        {'playerID': 'bettsmo01', 'yearID': '2022', 'teamID': 'LAN'},
        {'playerID': 'bettsmo01', 'yearID': '2023', 'teamID': 'LAN'},
        {'playerID': 'kershcl01', 'yearID': '2022', 'teamID': 'LAN'},
        {'playerID': 'kershcl01', 'yearID': '2023', 'teamID': 'LAN'},
        {'playerID': 'buehlwa01', 'yearID': '2022', 'teamID': 'LAN'},
        {'playerID': 'bordafr01', 'yearID': '1944', 'teamID': 'BRO'},
        {'playerID': 'bordafr01', 'yearID': '1945', 'teamID': 'BRO'},
        {'playerID': 'greggha01', 'yearID': '1944', 'teamID': 'BRO'},
        {'playerID': 'greggha01', 'yearID': '1945', 'teamID': 'BRO'},
        {'playerID': 'webbele01', 'yearID': '1944', 'teamID': 'BRO'},
        {'playerID': 'webbele01', 'yearID': '1945', 'teamID': 'BRO'},
        {'playerID': 'galanau01', 'yearID': '1944', 'teamID': 'BRO'},
        {'playerID': 'galanau01', 'yearID': '1945', 'teamID': 'BRO'},
        {'playerID': 'quinnjo02', 'yearID': '1890', 'teamID': 'BSP'},
        {'playerID': 'broutda01', 'yearID': '1890', 'teamID': 'BSP'},
        {'playerID': 'broutda01', 'yearID': '1891', 'teamID': 'BS2'},
        {'playerID': 'daleybi01', 'yearID': '1890', 'teamID': 'BSP'},
        {'playerID': 'daleybi01', 'yearID': '1891', 'teamID': 'BS2'},
    ],
    'AwardsPlayers.csv': [
        {'playerID': 'guerrvl02', 'awardID': 'Gold Glove', 'yearID': '2022', 'lgID': 'AL'},
        {'playerID': 'bettsmo01', 'awardID': 'TSN All-Star', 'yearID': '2022', 'lgID': 'NL'},
        {'playerID': 'bettsmo01', 'awardID': 'TSN All-Star', 'yearID': '2023', 'lgID': 'NL'},
        {'playerID': 'bettsmo01', 'awardID': 'Silver Slugger', 'yearID': '2022', 'lgID': 'NL'},
        {'playerID': 'bettsmo01', 'awardID': 'Silver Slugger', 'yearID': '2023', 'lgID': 'NL'},
        {'playerID': 'bettsmo01', 'awardID': 'Gold Glove', 'yearID': '2022', 'lgID': 'NL'},
    ],
    'Batting.csv': [
        {'playerID': 'guerrvl02', 'yearID': '2022', 'stint': '1'},
        {'playerID': 'guerrvl02', 'yearID': '2023', 'stint': '1'},
        {'playerID': 'biggica01', 'yearID': '2022', 'stint': '1'},
        {'playerID': 'biggica01', 'yearID': '2023', 'stint': '1'},
        {'playerID': 'bettsmo01', 'yearID': '2022', 'stint': '1'},
        {'playerID': 'bettsmo01', 'yearID': '2023', 'stint': '1'},
        {'playerID': 'bordafr01', 'yearID': '1944', 'stint': '1'},
        {'playerID': 'bordafr01', 'yearID': '1945', 'stint': '1'},
        {'playerID': 'greggha01', 'yearID': '1944', 'stint': '1'},
        {'playerID': 'greggha01', 'yearID': '1945', 'stint': '1'},
        {'playerID': 'webbele01', 'yearID': '1944', 'stint': '1'},
        {'playerID': 'webbele01', 'yearID': '1945', 'stint': '1'},
        {'playerID': 'galanau01', 'yearID': '1944', 'stint': '1'},
        {'playerID': 'galanau01', 'yearID': '1945', 'stint': '1'},
        {'playerID': 'quinnjo02', 'yearID': '1890', 'stint': '1'},
        {'playerID': 'broutda01', 'yearID': '1890', 'stint': '1'},
        {'playerID': 'broutda01', 'yearID': '1891', 'stint': '1'},
        {'playerID': 'daleybi01', 'yearID': '1890', 'stint': '1'},
        {'playerID': 'daleybi01', 'yearID': '1891', 'stint': '1'},
    ],    
    'Fielding.csv': [
        {'playerID': 'guerrvl02', 'yearID': '2022', 'stint': '1', 'POS': '1B'},
        {'playerID': 'guerrvl02', 'yearID': '2022', 'stint': '1', 'POS': '3B'},
        {'playerID': 'guerrvl02', 'yearID': '2023', 'stint': '1', 'POS': '1B'},

        {'playerID': 'biggica01', 'yearID': '2022', 'stint': '1', 'POS': '1B'},
        {'playerID': 'biggica01', 'yearID': '2022', 'stint': '1', 'POS': '2B'},
        {'playerID': 'biggica01', 'yearID': '2022', 'stint': '1', 'POS': '3B'},
        {'playerID': 'biggica01', 'yearID': '2022', 'stint': '1', 'POS': 'OF'},
        {'playerID': 'biggica01', 'yearID': '2023', 'stint': '1', 'POS': '1B'},
        {'playerID': 'biggica01', 'yearID': '2023', 'stint': '1', 'POS': '2B'},
        {'playerID': 'biggica01', 'yearID': '2023', 'stint': '1', 'POS': '3B'},
        {'playerID': 'biggica01', 'yearID': '2023', 'stint': '1', 'POS': 'SS'},
        {'playerID': 'biggica01', 'yearID': '2023', 'stint': '1', 'POS': 'OF'},

        {'playerID': 'kikucyu01', 'yearID': '2022', 'stint': '1', 'POS': 'P'},
        {'playerID': 'kikucyu01', 'yearID': '2023', 'stint': '1', 'POS': 'P'},

        {'playerID': 'bettsmo01', 'yearID': '2022', 'stint': '1', 'POS': '2B'},
        {'playerID': 'bettsmo01', 'yearID': '2022', 'stint': '1', 'POS': 'OF'},
        {'playerID': 'bettsmo01', 'yearID': '2023', 'stint': '1', 'POS': '2B'},
        {'playerID': 'bettsmo01', 'yearID': '2023', 'stint': '1', 'POS': 'SS'},
        {'playerID': 'bettsmo01', 'yearID': '2023', 'stint': '1', 'POS': 'OF'},

        {'playerID': 'kershcl01', 'yearID': '2022', 'stint': '1', 'POS': 'P'},
        {'playerID': 'kershcl01', 'yearID': '2023', 'stint': '1', 'POS': 'P'},

        {'playerID': 'buehlwa01', 'yearID': '2022', 'stint': '1', 'POS': 'P'},

        {'playerID': 'bordafr01', 'yearID': '1944', 'stint': '1', 'POS': '3B'},
        {'playerID': 'bordafr01', 'yearID': '1944', 'stint': '1', 'POS': 'OF'},
        {'playerID': 'bordafr01', 'yearID': '1945', 'stint': '1', 'POS': '3B'},

        {'playerID': 'greggha01', 'yearID': '1944', 'stint': '1', 'POS': 'P'},
        {'playerID': 'greggha01', 'yearID': '1945', 'stint': '1', 'POS': 'P'},

        {'playerID': 'webbele01', 'yearID': '1944', 'stint': '1', 'POS': 'P'},
        {'playerID': 'webbele01', 'yearID': '1945', 'stint': '1', 'POS': 'P'},

        {'playerID': 'galanau01', 'yearID': '1944', 'stint': '1', 'POS': '2B'},
        {'playerID': 'galanau01', 'yearID': '1944', 'stint': '1', 'POS': 'OF'},
        {'playerID': 'galanau01', 'yearID': '1945', 'stint': '1', 'POS': '1B'},
        {'playerID': 'galanau01', 'yearID': '1945', 'stint': '1', 'POS': '3B'},
        {'playerID': 'galanau01', 'yearID': '1945', 'stint': '1', 'POS': 'OF'},

        {'playerID': 'quinnjo02', 'yearID': '1890', 'stint': '1', 'POS': '2B'},

        {'playerID': 'broutda01', 'yearID': '1890', 'stint': '1', 'POS': '1B'},
        {'playerID': 'broutda01', 'yearID': '1891', 'stint': '1', 'POS': '1B'},

        {'playerID': 'daleybi01', 'yearID': '1890', 'stint': '1', 'POS': 'OF'},
        {'playerID': 'daleybi01', 'yearID': '1890', 'stint': '1', 'POS': 'P'},
        {'playerID': 'daleybi01', 'yearID': '1891', 'stint': '1', 'POS': 'OF'},
        {'playerID': 'daleybi01', 'yearID': '1891', 'stint': '1', 'POS': 'P'}
    ],
    'FieldingOFsplit.csv': [
        {'playerID': 'biggica01', 'yearID': '2022', 'stint': '1', 'POS': 'LF'},
        {'playerID': 'biggica01', 'yearID': '2022', 'stint': '1', 'POS': 'RF'},
        {'playerID': 'biggica01', 'yearID': '2023', 'stint': '1', 'POS': 'RF'},
        {'playerID': 'bettsmo01', 'yearID': '2022', 'stint': '1', 'POS': 'RF'},
        {'playerID': 'bettsmo01', 'yearID': '2023', 'stint': '1', 'POS': 'RF'},

    ],
    'HallOfFame.csv': [
        {'yearid': '1936', 'playerID': 'broutda01'},
        {'yearid': '1945', 'playerID': 'broutda01'}
    ],
    'HomeGames.csv': [
        {'yearkey': '1944', 'teamkey': 'BRO', 'parkkey': 'NYC15'},
        {'yearkey': '1945', 'teamkey': 'BRO', 'parkkey': 'NYC15'},
        {'yearkey': '2022', 'teamkey': 'LAN', 'parkkey': 'LOS03'},
        {'yearkey': '2023', 'teamkey': 'LAN', 'parkkey': 'LOS03'},
        {'yearkey': '2022', 'teamkey': 'TOR', 'parkkey': 'TOR02'},
        {'yearkey': '2023', 'teamkey': 'TOR', 'parkkey': 'TOR02'},
        {'yearkey': '1890', 'teamkey': 'BSP', 'parkkey': 'BOS04'},
        {'yearkey': '1891', 'teamkey': 'BS2', 'parkkey': 'BOS04'},
    ],
    'Parks.csv': [
        {'parkkey': 'NYC15'},
        {'parkkey': 'LOS03'},
        {'parkkey': 'TOR02'},
        {'parkkey': 'BOS04'}
    ],
    'Pitching.csv': [
        {'playerID': 'kikucyu01', 'yearID': '2022', 'stint': '1'},
        {'playerID': 'kikucyu01', 'yearID': '2023', 'stint': '1'},
        {'playerID': 'kershcl01', 'yearID': '2022', 'stint': '1'},
        {'playerID': 'kershcl01', 'yearID': '2023', 'stint': '1'},
        {'playerID': 'buehlwa01', 'yearID': '2022', 'stint': '1'},
        {'playerID': 'greggha01', 'yearID': '1944', 'stint': '1'},
        {'playerID': 'greggha01', 'yearID': '1945', 'stint': '1'},
        {'playerID': 'webbele01', 'yearID': '1944', 'stint': '1'},
        {'playerID': 'webbele01', 'yearID': '1945', 'stint': '1'},
        {'playerID': 'daleybi01', 'yearID': '1890', 'stint': '1'},
        {'playerID': 'daleybi01', 'yearID': '1891', 'stint': '1'},
    ],
    'People.csv': [
        {'playerID': 'guerrvl02'},
        {'playerID': 'biggica01'},
        {'playerID': 'kikucyu01'},
        {'playerID': 'bettsmo01'},
        {'playerID': 'kershcl01'},
        {'playerID': 'buehlwa01'},
        {'playerID': 'bordafr01'},
        {'playerID': 'greggha01'},
        {'playerID': 'webbele01'},
        {'playerID': 'galanau01'},
        {'playerID': 'quinnjo02'},
        {'playerID': 'broutda01'},
        {'playerID': 'daleybi01'}
    ],
    'Teams.csv': [
        {'yearID': '1944', 'teamID': 'BRO'},
        {'yearID': '1945', 'teamID': 'BRO'},
        {'yearID': '2022', 'teamID': 'LAN'},
        {'yearID': '2023', 'teamID': 'LAN'},
        {'yearID': '2022', 'teamID': 'TOR'},
        {'yearID': '2023', 'teamID': 'TOR'},
        {'yearID': '1890', 'teamID': 'BSP'},
        {'yearID': '1891', 'teamID': 'BS2'},
    ],
    'TeamsFranchises.csv': [
        {'franchID': 'TOR'},
        {'franchID': 'LAD'},
        {'franchID': 'BRS'},
    ]
}

# Function to check if a row matches any condition
def row_matches_conditions(row, conditions):
    for condition in conditions:
        if all(row.get(key) == str(value) for key, value in condition.items()):
            return True
    return False


def main():
    args = parse_arguments()

    input_directory = args.input_directory
    output_directory = args.output_directory

    # Define the paths to your original CSV files
    csv_files = [
        'AllstarFull.csv',
        'Appearances.csv',
        'AwardsPlayers.csv',
        'Batting.csv',
        'Fielding.csv',
        'FieldingOFsplit.csv',
        'HallOfFame.csv',
        'HomeGames.csv',
        'Parks.csv',
        'Pitching.csv',
        'People.csv',
        'Teams.csv',
        'TeamsFranchises.csv'
    ]

    # Create the directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Create a sub CSV for each CSV file based on conditions
    for csv_file in csv_files:
        if csv_file in conditions:
            file_path = os.path.join(input_directory, csv_file)
            df = pd.read_csv(file_path, encoding='ISO-8859-1')

            # Check if the required columns are in the dataframe
            required_columns = list(conditions[csv_file][0].keys())
            if not set(required_columns).issubset(df.columns):
                print(f"Missing columns in {csv_file}: {set(required_columns) - set(df.columns)}")
                continue

            # Convert required columns to string for consistency
            df[required_columns] = df[required_columns].astype(str)

            filtered_df = df[df.apply(lambda row: row_matches_conditions(row, conditions[csv_file]), axis=1)]

            output_file = os.path.join(output_directory, f"Sample{csv_file}")
            filtered_df.to_csv(output_file, index=False)
            print(f"Created {output_file} with {len(filtered_df)} matching rows.")

if __name__ == '__main__':
    main()
