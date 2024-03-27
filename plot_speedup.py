from parse_file import parse_file

def calculate_speedup(data_dict):
    speedup_dict = {}
    for size, thread_times in data_dict.items():
        baseline_time = thread_times[0][1]
        speedups = [
          (thread, baseline_time / time) for thread, time in thread_times
        ]
        speedup_dict[size] = speedups
    return speedup_dict

def plot_speedup(speedup_dict):
    import matplotlib.pyplot as plt
    plt.style.use('classic')
    plt.figure(figsize=(12, 8))
    for size, speedup_data in speedup_dict.items():
        threads = [data[0] for data in speedup_data]
        speedups = [data[1] for data in speedup_data]
        plt.plot(threads, speedups, label=f"Size {size}", marker='o', linestyle='-', linewidth=2, markersize=8)
    plt.title('Speedup vs. Number of Threads', fontsize=16)
    plt.xlabel('Number of Threads', fontsize=14)
    plt.ylabel('Speedup', fontsize=14)
    plt.legend(title='Data Size', title_fontsize='13', fontsize='11', loc='best')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='grey')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.savefig("speedup.png")

data_dict = parse_file("profile.dat")
speedup_dict = calculate_speedup(data_dict)
plot_speedup(speedup_dict)
