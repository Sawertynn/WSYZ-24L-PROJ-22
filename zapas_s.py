import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import re

order = ['buraki', 'kapusta', 'marchew', 'ziemniaki']

def transform(veg):
    with open(f'{veg}_zapas.txt', 'r') as file:
        data = file.read()
    data = re.sub(r'\s+', ';', data)
    words = data.split(';')
    words = [word if (i+1) % 11 != 0 else word + ';\n' for i, word in enumerate(words)]
    data = ';'.join(words)
    with open(f'{veg}_zapas_modified.txt', 'w') as file:
        file.write(data)

# for veg in order:
#     transform(veg)

store_palette = sns.color_palette('husl', 10)
stores = {f'S{i}':store_palette[i-1] for i in range(1, 11)}
buraki = pd.read_csv("buraki_zapas_modified.txt", sep=';').dropna(axis=1)
kapusta = pd.read_csv("kapusta_zapas_modified.txt", sep=';').dropna(axis=1)
marchew = pd.read_csv("marchew_zapas_modified.txt", sep=';').dropna(axis=1)
ziemniaki = pd.read_csv("ziemniaki_zapas_modified.txt", sep=';').dropna(axis=1)

y_lim = (0, 9)
fig, ax = plt.subplots(4, figsize=(15, 5))
for j, veg in enumerate([buraki, kapusta, marchew, ziemniaki]):
    df_melt = veg.melt(id_vars='w', var_name='column', value_name='value')
    sns.lineplot(x='w', y='value', data=df_melt, ax=ax[j], hue='column', palette=store_palette, legend=False)
    ax[j].set_xlabel('')
    ax[j].set_ylabel('')
    ax[j].set_ylim(y_lim)
    ax[j].set_xticks([])
ax[0].set_ylabel('Buraki')
ax[1].set_ylabel('Kapusta')
ax[2].set_ylabel('Marchew')
ax[3].set_ylabel('Ziemniaki')
ax[3].set_xlabel('Tydzień')
# create legend
for i, (store, color) in enumerate(stores.items()):
    ax[0].plot([], [], color=color, label=store)
ax[0].legend(loc='upper right', bbox_to_anchor=(1.1, 1))
plt.tight_layout()
plt.show()