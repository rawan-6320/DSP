import numpy as np
import matplotlib.pyplot as plt
import os


# ========= Read Files =========

def read_files(folder_path):

    signals = {}
    files = os.listdir(folder_path)

    for file_name in files:

        if file_name.endswith(".txt"):

            file_path = os.path.join(folder_path, file_name)

            indices = []
            samples = []

            with open(file_path, "r") as file:

                file.readline()
                file.readline()

                num_samples = int(file.readline().strip())

                for i in range(num_samples):

                    line = file.readline().strip()
                    parts = line.split()

                    index = int(parts[0])
                    sample = float(parts[1])

                    indices.append(index)
                    samples.append(sample)

            signal_name = os.path.splitext(file_name)[0]

            signals[signal_name] = {
                "indices": indices,
                "samples": samples
            }

    return signals


# =========== Display Signals ===========

def display_continuous(signal, signal_name):

    indices = signal['indices']
    values = signal['samples']

    plt.figure(figsize=(10, 6))
    plt.plot(indices, values)

    plt.xlabel("Index")
    plt.ylabel("Signal Value")
    plt.title(f"Continuous {signal_name}")

    plt.show()


def display_discrete(signal, signal_name):

    indices = signal['indices']
    samples = signal['samples']

    plt.figure(figsize=(10, 6))
    plt.stem(indices, samples)

    plt.xlabel("Index")
    plt.ylabel("Signal Value")
    plt.title(f"Discrete {signal_name}")

    plt.grid(True, alpha=0.3)

    plt.show()


# ============= Math Operations =============

def add_signals(signals, signal_names):

    result_indices = signals[signal_names[0]]['indices'].copy()
    result_samples = [0] * len(result_indices)

    for name in signal_names:

        samples = signals[name]['samples']

        for i in range(len(result_indices)):
            result_samples[i] += samples[i]

    return result_indices, result_samples


def mul_const(const, signals, signal_name):

    indices = signals[signal_name]['indices'].copy()
    samples = signals[signal_name]['samples'].copy()

    samples = [sample * const for sample in samples]

    return indices, samples