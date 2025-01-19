import sys
import pandas as pd
import numpy as np

def validate_inputs(args):
    if len(args) != 5:
        raise ValueError("Incorrect number of parameters. Expected: 4 arguments (inputFileName, Weights, Impacts, resultFileName).")

    input_file = args[1]
    weights = args[2].split(',')
    impacts = args[3].split(',')
    output_file = args[4]

    try:
        weights = [float(w) for w in weights]
    except ValueError:
        raise ValueError("Weights must be numeric values separated by commas.")

    if not all(impact in ['+', '-'] for impact in impacts):
        raise ValueError("Impacts must be either '+' or '-'.")

    return input_file, weights, impacts, output_file

def read_input_file(input_file):
    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{input_file}' not found.")
    
    if data.shape[1] < 3:
        raise ValueError("Input file must contain at least three columns.")

    if not np.issubdtype(data.iloc[:, 1:].dtypes[0], np.number):
        raise ValueError("From 2nd to last columns, all values must be numeric.")

    return data

def topsis(data, weights, impacts):
    # Normalize the data
    matrix = data.iloc[:, 1:].values.astype(float)
    norm_matrix = matrix / np.sqrt((matrix**2).sum(axis=0))

    # Apply weights
    weighted_matrix = norm_matrix * weights

    # Determine ideal best and worst
    ideal_best = []
    ideal_worst = []
    for i, impact in enumerate(impacts):
        if impact == '+':
            ideal_best.append(np.max(weighted_matrix[:, i]))
            ideal_worst.append(np.min(weighted_matrix[:, i]))
        else:
            ideal_best.append(np.min(weighted_matrix[:, i]))
            ideal_worst.append(np.max(weighted_matrix[:, i]))

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # Calculate distances to ideal best and worst
    dist_to_best = np.sqrt(((weighted_matrix - ideal_best)**2).sum(axis=1))
    dist_to_worst = np.sqrt(((weighted_matrix - ideal_worst)**2).sum(axis=1))

    # Calculate TOPSIS scores
    scores = dist_to_worst / (dist_to_best + dist_to_worst)
    ranks = scores.argsort()[::-1] + 1

    return scores, ranks

def write_output_file(data, scores, ranks, output_file):
    data['Topsis Score'] = scores
    data['Rank'] = ranks
    data.to_csv(output_file, index=False)
    print(f"Results written to '{output_file}'.")

def main():
    try:
        args = sys.argv
        input_file, weights, impacts, output_file = validate_inputs(args)
        data = read_input_file(input_file)

        if len(weights) != data.shape[1] - 1 or len(impacts) != data.shape[1] - 1:
            raise ValueError("Number of weights and impacts must match the number of columns from 2nd to last in the input file.")

        scores, ranks = topsis(data, weights, impacts)
        write_output_file(data, scores, ranks, output_file)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
