import matplotlib as mpl
import matplotlib.pyplot as plt

def get_counter_plot(counter, plot_name):
    mpl.rcParams['figure.figsize'] = (6, 6)

    sorted_x, sorted_y = zip(*counter.most_common(15))

    plt.bar(range(len(sorted_x)), sorted_y, width=0.75, align='center')
    plt.xticks(range(len(sorted_x)), sorted_x, rotation=90)
    plt.axis('tight')
    plt.tight_layout()
    plt.savefig(plot_name)
    plt.show()
