from random import random

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_scatter(data: pd.DataFrame, x: str, y: str, hue: str):
    plt.figure(figsize=(12, 6))
    ax = sns.scatterplot(data, x=x, y=y, hue=hue)
    ax.set_title(f"scatter {x} vs {y}")
    plt.savefig(f"../../reports/scatter_{x}_vs_{y}.png")
    plt.show()

def plot_hist(data: pd.DataFrame, bins: int):
    plt.figure(figsize=(12, 6))
    ax = sns.histplot(data, bins=bins)
    ax.set_title(f"histogram_{random()}")
    plt.savefig(f"../../reports/hist_{random()}.png")
    plt.show()

def plot_bar(data: pd.DataFrame, x: str, y: str, hue: str=""):
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(data, x=x, y=y, hue=hue)
    ax.set_title(f"bar {x} vs {y}")
    plt.savefig(f"../../reports/bar_{x}_vs_{y}.png")
    plt.show()

def plot_corr_matrix(data: pd.DataFrame):
    plt.figure(figsize=(12, 6))
    ax = sns.heatmap(data.corr(), annot=True)
    ax.set_title(f"correlation_matrix_{random()}")
    plt.savefig(f"../../reports/correlation_matrix_{random()}.png")
    plt.show()

def plot_count_values(data: pd.DataFrame, target: str):
    plt.figure(figsize=(12, 6))
    data[target].value_counts().plot(kind="bar")
    plt.title=f"count_values_{target}"
    plt.savefig(f"../../reports/count_values_{target}.png")
    plt.show()







