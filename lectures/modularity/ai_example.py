"""
Gemini 2.5 prompt: 
make me a function that samples from a normal distribution 
and plots the data in a histogram and prints a dataframe 
of the mean and standard deviation
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def sample_and_analyze_normal(num_samples: int, mu: float, sigma: float):
    """
    Generates random samples from a normal distribution, plots a histogram,
    and prints a DataFrame with the sample's mean and standard deviation.

    Args:
        num_samples (int): The number of samples to generate.
        mu (float): The mean of the normal distribution.
        sigma (float): The standard deviation of the normal distribution.
    """
    # 1. Generate the samples from a normal distribution
    # We use numpy's random.normal function for this.
    sampled_data = np.random.normal(mu, sigma, num_samples)

    # 2. Plot the data in a histogram
    # We create a figure and axes for the plot.
    plt.figure(figsize=(10, 6))
    plt.hist(sampled_data, bins=30, density=True, alpha=0.6, color='skyblue', edgecolor='black')

    # Add a title and labels for clarity
    plt.title(f'Histogram of Normal Distribution (μ={mu}, σ={sigma})')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Show the plot
    plt.show()

    # 3. Create a DataFrame for the mean and standard deviation
    # We calculate the mean and standard deviation of our sampled data.
    calculated_mean = np.mean(sampled_data)
    calculated_std = np.std(sampled_data)

    # Now, we create a pandas DataFrame to hold these values.
    # The dictionary keys become the column headers.
    stats_data = {
        'Statistic': ['Mean', 'Standard Deviation'],
        'Value': [calculated_mean, calculated_std]
    }
    stats_df = pd.DataFrame(stats_data)

    # 4. Print the DataFrame
    print("--- Sample Statistics ---")
    print(stats_df.to_string(index=False))


if __name__ == "__main__":
    # Example usage:
    # We'll sample 10,000 data points from a normal distribution
    # with a mean of 0 and a standard deviation of 1.
    sample_and_analyze_normal(num_samples=10000, mu=0, sigma=1)

    print("\n" + "="*50 + "\n")

    # Another example with different parameters:
    # 5,000 data points with a mean of 50 and a standard deviation of 10.
    sample_and_analyze_normal(num_samples=5000, mu=50, sigma=10)
