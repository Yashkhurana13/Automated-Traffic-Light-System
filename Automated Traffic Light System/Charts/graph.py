import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("traffic.csv")  # Example: 'traffic_data.csv'


print("Available columns:", df.columns)


vehicle_column = 'Vehicle_Count'
waiting_time_column = 'Avg_Wait_Time (s)'

# Clean data: remove rows with missing values
df = df.dropna(subset=[vehicle_column, waiting_time_column])

# Plot Vehicle Count vs Waiting Time
plt.figure(figsize=(10, 6))
plt.scatter(df[vehicle_column], df[waiting_time_column], color='green', edgecolor='black')
plt.title('Vehicle Count vs Waiting Time', fontsize=14)
plt.xlabel('Number of Vehicles', fontsize=12)
plt.ylabel('Waiting Time (seconds)', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()


df['Time'] = pd.to_datetime(df['Time'])

df['Rounded_Time'] = df['Time'].dt.floor('15T')


heatmap_data = df.pivot_table(
    index='Lane',
    columns='Rounded_Time',
    values='Vehicle_Count',
    aggfunc='mean',
    fill_value=0
)


plt.figure(figsize=(14, 6))
sns.heatmap(heatmap_data, cmap="YlOrRd", linewidths=0.5, annot=True, fmt=".0f")
plt.title("Heatmap of Lane Congestion Over Time")
plt.xlabel("Time")
plt.ylabel("Lane")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


file_path = "Static vs dynamic.xlsx"
xls = pd.ExcelFile(file_path)
df = pd.read_excel(xls, sheet_name='Sheet2')


simulation_numbers = df.iloc[1:, 0].astype(int).reset_index(drop=True)
static_totals = df.iloc[1:, 5].astype(int).reset_index(drop=True)
dynamic_totals = df.iloc[1:, 14].astype(int).reset_index(drop=True)


plt.figure(figsize=(10, 6))
plt.plot(simulation_numbers, static_totals, label='Static Total', marker='o')
plt.plot(simulation_numbers, dynamic_totals, label='Dynamic Total', marker='o')
plt.title('Static vs Dynamic')
plt.xlabel('Simulation Number')
plt.ylabel('Total')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
