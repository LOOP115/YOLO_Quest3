import matplotlib.pyplot as plt

# Data from the table
models = ['cubic100-v8n', 'cubic100-v8s', 'cubic100-v8m', 'cubic100-v8l', 'cubic100-v8x']
map_values = [92.7, 93.7, 94.4, 94.3, 91.9]
params = [3.2, 11.2, 25.9, 43.7, 68.2]
preprocess_time = [1.6, 1.8, 1.6, 2.2, 2.3]
inference_time = [10.1, 11.3, 14.4, 16.9, 19.4]
postprocess_time = [3.3, 3.2, 3.2, 3.5, 3.1]

# Calculate total time
total_time = [preprocess_time[i] + inference_time[i] + postprocess_time[i] for i in range(len(models))]

# Plot 1: mAP vs Params
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(params, map_values, 'o-', label=r'$\underset{50-95}{\text{mAP}}^{\text{val}}$ vs Params')
for i, model in enumerate(models):
    plt.text(params[i], map_values[i], model, fontsize=12, ha='right')
plt.xlabel('Parameters (M)', fontsize=16)
plt.ylabel(r'$\underset{50-95}{\text{mAP}}^{\text{val}}$', fontsize=16)
# plt.title(r'$\underset{50-95}{\text{mAP}}^{\text{val}}$ vs Parameters')
# plt.legend()
plt.grid(True)

# Plot 2: mAP vs Total Time
plt.subplot(1, 2, 2)
plt.plot(total_time, map_values, 'o-', label=r'$\underset{50-95}{\text{mAP}}^{\text{val}}$ vs Time')
for i, model in enumerate(models):
    plt.text(total_time[i], map_values[i], model, fontsize=12, ha='right')
plt.xlabel('Latency RTX 4090 (ms/img)', fontsize=16)
plt.ylabel(r'$\underset{50-95}{\text{mAP}}^{\text{val}}$', fontsize=16)
# plt.title(r'$\underset{50-95}{\text{mAP}}^{\text{val}}$ vs Total Time')
# plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
