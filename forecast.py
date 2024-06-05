import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_sine_with_noise(num_samples=52, noise_level=0.1, shift=0):
    x = np.linspace(0, 2 * np.pi, num_samples)
    
    cos_wave = np.cos(x)
    cos_wave = np.roll(cos_wave, shift)
    
    noise = np.random.normal(0, noise_level, num_samples)
    cos_with_noise = cos_wave + noise
    _min = 0
    _max = 1.4
    old_min = np.min(cos_with_noise)
    old_max = np.max(cos_with_noise)
    scaled_cos = _min + (cos_with_noise - old_min) * (_max - _min) / (old_max - old_min)
    scaled_cos = np.round(scaled_cos, 2)
    
    return scaled_cos

# Optionally, plot the results to visualize
warzywa = ['Ziemniaki', 'Marchew', 'Kapusta', 'Buraki']
shifts = [12, 25, 38, 51]
sklepy = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10']
noises = [0.1, 0.15, 0.2, 0.25, 0.05, 0.75, 0.1, 0.1, 0.15, 0.175]
for v,s in zip(warzywa, shifts):
    samples = []
    for skl in sklepy:
        samples.append(generate_sine_with_noise(52, 0.1, s))
    print(samples)
    fig, ax = plt.subplots()
    for i, sample in enumerate(samples):
        ax.plot(sample, label=sklepy[i], alpha=0.5)
    ax.legend()
    ax.set_title(f'Zapotrzebowanie na {v}')
    plt.show()
    # save the plot
    fig.savefig(f'Zapotrzebowanie na {v}.png')
    plt.close()
    df = pd.DataFrame(columns=sklepy)
    for i, sample in enumerate(samples):
        df[sklepy[i]] = sample
    df.index = range(1,53)
    df.to_csv(f'Zapotrzebowanie na {v}.csv', sep='\t')


