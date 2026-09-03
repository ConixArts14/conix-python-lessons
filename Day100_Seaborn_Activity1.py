import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_heatmap():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade FROM exams", conn)

    # Pivot table for heatmap
    pivot = df.pivot_table(index="subject", columns="grade", aggfunc=len, fill_value=0)

    sns.set(style="whitegrid")
    plt.figure(figsize=(8,6))
    sns.heatmap(pivot, cmap="YlGnBu", annot=True, fmt="d")

    plt.title("Heatmap of Grade Distribution (Day100)")
    plt.xlabel("Grades")
    plt.ylabel("Subjects")
    plt.tight_layout()
    plt.show()

    conn.close()

seaborn_heatmap()

import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_swarmplot():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade FROM exams", conn)

    sns.set(style="whitegrid")
    plt.figure(figsize=(8,6))
    sns.swarmplot(x="subject", y="grade", data=df, palette="Set2")

    plt.title("Swarmplot of Grades per Subject (Day100)")
    plt.show()
    conn.close()

seaborn_swarmplot()

import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_pairplot():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade FROM exams", conn)

    sns.set(style="whitegrid")
    pairplot = sns.pairplot(df, hue="subject", palette="Set1")

    pairplot.fig.suptitle("Pairplot of Grades per Subject (Day100)", y=1.02)
    plt.show()
    conn.close()

seaborn_pairplot()

import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_heatmap():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade FROM exams", conn)

    pivot = df.pivot_table(index="subject", columns="grade", aggfunc=len, fill_value=0)

    sns.set(style="whitegrid")
    plt.figure(figsize=(8,6))
    sns.heatmap(pivot, cmap="YlGnBu", annot=True, fmt="d")

    plt.title("Heatmap of Grade Distribution (Day100)")
    plt.xlabel("Grades")
    plt.ylabel("Subjects")
    plt.tight_layout()
    plt.show()
    conn.close()

seaborn_heatmap()
