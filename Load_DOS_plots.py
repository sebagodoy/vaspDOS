import matplotlib.pyplot as plt
from DOSclass import *
import pickle

with open("./Bulk_and_Surfs/Bulk_DOS.fig.pickle", "rb") as plotB:
    fig_bulk = pickle.load(plotB)
with open("./Bulk_and_Surfs/Surf111_DOS.fig.pickle", "rb") as plot111:
    fig_111 = pickle.load(plot111)
with open("./Bulk_and_Surfs/Surf100_DOS.fig.pickle", "rb") as plot100:
    fig_100 = pickle.load(plot100)

plt.show()