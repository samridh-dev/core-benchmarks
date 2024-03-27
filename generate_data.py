# --------------------------------------------------------------------------- #

# parameters
thread_arr = range(1, 13)
element_arr = [100000000]
iterations = 10
filename = "profile.dat"
generate_script = "./example/make.sh"
run_script = "./example/run.sh"

# --------------------------------------------------------------------------- #

import subprocess
import os
import time

total_steps = len(element_arr) * len(thread_arr) * iterations
current_step = 0

with open(filename, 'w') as f:
    for elementsize in element_arr:
        for threadsize in thread_arr:
            f.write(f"? {elementsize}")

            measured_times = []

            # Change threadsize
            subprocess.run(
                [generate_script, str(threadsize), str(elementsize)],
                check=True
            )

            for i in range(iterations):
                beg = time.perf_counter()

                # Run desired program
                result = subprocess.run(
                    [run_script], stderr=subprocess.PIPE, text=True)

                end = time.perf_counter()
                measured_times.append(end - beg)

                # Update progress
                current_step += 1
                progress = (current_step / total_steps) * 100
                bar_length = 64
                filled_length = int(bar_length * current_step // total_steps)
                bar = '█' * filled_length + '-' * (bar_length - filled_length)

                print(
                    f"\033[92m\rSize: {elementsize:.1e},"                     + 
                    f" Thread: {threadsize},"                                 +
                    f" Iteration: {i + 1}/{iterations}"                       +
                    f" [{bar}] {progress:.1f}%\033[0m", end='', flush=True
                )

            average_time = sum(measured_times) / len(measured_times)
            f.write(f" - {threadsize} : {average_time:.5f}\n")
print("\n\033[92mGenerated Data. Exiting.\033[0m")
