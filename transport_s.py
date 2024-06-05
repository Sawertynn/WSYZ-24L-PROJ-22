import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import re

# with open('m1_transport.txt', 'r') as file:
#     data = file.read()
# data = re.sub(r'\s+', ';', data)
# words = data.split(';')
# words = [word if (i+1) % 11 != 0 else word + ';\n' for i, word in enumerate(words)]
# data = ';'.join(words)
# with open('m1_transport_modified.txt', 'w') as file:
#     file.write(data)

# with open('m2_transport.txt', 'r') as file:
#     data = file.read()
# data = re.sub(r'\s+', ';', data)
# words = data.split(';')
# words = [word if (i+1) % 11 != 0 else word + ';\n' for i, word in enumerate(words)]
# data = ';'.join(words)
# with open('m2_transport_modified.txt', 'w') as file:
#     file.write(data)

# with open('m3_transport.txt', 'r') as file:
#     data = file.read()
# data = re.sub(r'\s+', ';', data)
# words = data.split(';')
# words = [word if (i+1) % 11 != 0 else word + ';\n' for i, word in enumerate(words)]
# data = ';'.join(words)
# with open('m3_transport_modified.txt', 'w') as file:
#     file.write(data)

order = ['buraki', 'kapusta', 'marchew', 'ziemniaki']
store_palette = sns.color_palette('husl', 10)
stores = {f'S{i}':store_palette[i-1] for i in range(1, 11)}
m1 = pd.read_csv("m1_transport_modified.txt", sep=';').dropna(axis=1)
m2 = pd.read_csv("m2_transport_modified.txt", sep=';').dropna(axis=1)
m3 = pd.read_csv("m3_transport_modified.txt", sep=';').dropna(axis=1)
y_lim = (0, 8)

fig, ax = plt.subplots(4, 3, figsize=(15, 5))
for i, m in enumerate([m1, m2, m3]):
    buraki = m.iloc[:52, :]
    kapusta = m.iloc[52:104, :]
    marchew = m.iloc[104:156, :]
    ziemniaki = m.iloc[156:, :]
    x = range(1, 53)
    for j, veg in enumerate([buraki, kapusta, marchew, ziemniaki]):
        df_melt = veg.melt(id_vars='w', var_name='column', value_name='value')
        sns.lineplot(x='w', y='value', data=df_melt, ax=ax[j, i], hue='column', palette=store_palette, legend=False)
        ax[j, i].set_ylim(y_lim)
        ax[j, i].set_xlabel('')
        ax[j, i].set_ylabel('')
        ax[j, i].set_xticks([])
ax[0, 0].set_title('M1')
ax[0, 1].set_title('M2')
ax[0, 2].set_title('M3')
ax[0, 0].set_ylabel('Buraki')
ax[1, 0].set_ylabel('Kapusta')
ax[2, 0].set_ylabel('Marchew')
ax[3, 0].set_ylabel('Ziemniaki')
# create legend
for i, (store, color) in enumerate(stores.items()):
    ax[0, 2].plot([], [], color=color, label=store)
ax[0, 2].legend(loc='upper right', bbox_to_anchor=(1.3, 1))
plt.tight_layout()
plt.show()

