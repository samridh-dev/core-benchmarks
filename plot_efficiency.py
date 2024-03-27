from parse_file import parse_file

def calculate_efficiency(data_dict):
    efficiency_dict = {}
    for size, thread_times in data_dict.items():
        baseline_time = thread_times[0][1]
        efficiencies = [
            (thread, (baseline_time / (thread * time))) 
            for thread, time in thread_times
        ]
        efficiency_dict[size] = efficiencies
    return efficiency_dict

def plot_efficiency(efficiency_dict):
    import matplotlib.pyplot as plt
    plt.style.use('classic')
    plt.figure(figsize=(12, 8))
    plt.figure(figsize=(12, 8))
    for size, efficiency_data in efficiency_dict.items():
        threads = [data[0] for data in efficiency_data]
        efficiencies = [data[1] for data in efficiency_data]
        plt.plot(threads, efficiencies, label=f"Size {size}", marker='o', linestyle='-', linewidth=2, markersize=8)

    
    plt.title('Efficiency vs. Number of Threads for Different Sizes')
    plt.xlabel('Number of Threads', fontsize=14)
    plt.ylabel('Speedup', fontsize=14)
    plt.legend(title='Data Size', title_fontsize='13', fontsize='11', loc='best')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='grey')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.savefig("efficiency.png")


data_dict = parse_file("profile.dat")
efficiency_dict = calculate_efficiency(data_dict)
plot_efficiency(efficiency_dict)

