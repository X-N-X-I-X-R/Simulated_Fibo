# Simulated Market Movement with Fibonacci Levels

This Python script creates a real-time dynamic simulation of market price movements while calculating and displaying Fibonacci levels. It uses `matplotlib` for visualization and `random` for generating random price movements, resulting in realistic price fluctuations. The Fibonacci levels are calculated for each update, and both the current price and Fibonacci levels are updated live on the graph.

## Key Features

- **Randomized Market Movements**: Simulates price movements using random fluctuations, periodic cycles, and occasional sharp jumps to mimic real market behavior.
- **Real-Time Price Display**: The current price is displayed on the graph in real-time, updating with every price change.
- **Fibonacci Levels**: Calculates Fibonacci retracement levels dynamically, showing them on the chart with color-coded horizontal lines.
- **Interactive Graph**: The graph updates dynamically, with the price movements and Fibonacci levels adjusting continuously in response to the simulated market behavior.

## How It Works

1. **Price Simulation**: The `simulate_market_movement()` function generates price movements using a combination of random variations and cyclic patterns. Occasionally, it adds sharp price jumps for more realistic behavior.
2. **Fibonacci Level Calculation**: Fibonacci levels are calculated based on the current maximum and minimum prices, using standard Fibonacci retracement percentages.
3. **Real-Time Updates**: The graph updates continuously, displaying both the current price and the Fibonacci levels dynamically.
4. **Graph Rendering**: The code uses `matplotlib`'s interactive mode (`plt.ion()`) to continuously update the graph with new price data and Fibonacci levels, ensuring smooth transitions during the simulation.

## Dependencies

- `matplotlib`: Used for creating the dynamic, interactive graph.
- `numpy`: Utilized for numerical operations.
- `random`: Used to generate the randomized price movements.
- `time`: Controls the timing between updates to simulate a real-time market.

## Usage

1. **Install the necessary dependencies**:
    ```bash
    pip install matplotlib numpy
    ```

2. **Run the script**:
    ```bash
    python fibonacci.py
    ```

The dynamic graph will start with a simulated market and real-time Fibonacci level calculations.

This script is perfect for those looking to visualize market price movements and learn how Fibonacci levels adjust with price changes. It can be used for educational purposes, finance-related projects, or as a basis for more advanced simulations of financial markets.