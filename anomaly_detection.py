import numpy as np
import matplotlib.pyplot as plt


# Function to simulate a data stream
def data_stream(n=1000):
    if n <= 0:  # Check for valid input
        raise ValueError("Number of data points must be greater than zero.")
    x = np.linspace(0, 10 * np.pi, n)  # X values from 0 to 10*pi
    y = np.sin(x) + np.random.normal(0, 0.1, n)  # Regular pattern (sine wave) with random noise
    return y


# Function to detect anomalies using Z-score
def detect_anomalies(data, threshold=2.0):
    if len(data) == 0:  # Check if data is empty
        raise ValueError("Data array is empty.")

    mean = np.mean(data)  # Calculate mean of the data
    std_dev = np.std(data)  # Calculate standard deviation of the data
    anomalies = []  # List to hold indices of anomalies
    for i in range(len(data)):
        z_score = (data[i] - mean) / std_dev  # Calculate Z-score for each point
        if abs(z_score) > threshold:  # Check if Z-score exceeds threshold
            anomalies.append(i)  # Record index of anomaly
    return anomalies



# Visualization function
def visualize_data(data, anomalies):
    plt.figure(figsize=(10, 6))
    plt.plot(data, label='Data Stream', color='blue')
    plt.scatter(anomalies, data[anomalies], color='red', label='Anomalies')  # Mark anomalies in red
    plt.title('Data Stream and Anomalies')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.show()


# Main function
def main():
    # Simulate data stream
    data = data_stream()

    # Detect anomalies
    anomalies = detect_anomalies(data)

    # Visualize simulated data and anomalies
    visualize_data(data, anomalies)


if __name__ == "__main__":
    main()
