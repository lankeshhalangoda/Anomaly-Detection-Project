# Anomaly Detection in Data Streams

## Overview
This project implements an anomaly detection algorithm for continuous data streams using Python. The algorithm detects unusual patterns in a simulated data stream, which can represent various metrics such as financial transactions or system metrics.

## Table of Contents
- Installation
- Usage
- How It Works
- Visualizations
- License

## Installation
To run this project, you will need Python 3.x installed on your machine. You can install the necessary dependencies using pip. Follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/lankeshhalangoda/anomaly-detection-project.git
   cd anomaly-detection-project
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt

## Usage
To run the anomaly detection script, execute the following command:
python anomaly_detection.py
This will simulate a data stream and visualize the detected anomalies.

## How It Works
The project consists of the following components:
- Data Stream Simulation: The `data_stream()` function generates a simulated data stream that follows a sine wave pattern with added random noise.
- Anomaly Detection: The `detect_anomalies()` function identifies anomalies using the Z-score method, flagging points that deviate significantly from the mean.
- Visualization: The `visualize_data()` function plots the data stream and marks detected anomalies in red for easy identification.

## Visualizations
The script generates a plot displaying the data stream with highlighted anomalies. The blue line represents the data stream, while the red dots indicate detected anomalies.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
