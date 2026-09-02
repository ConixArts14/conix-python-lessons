import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_kdeplot():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade FROM exams", conn)

    sns.set(style="whitegrid")
    plt.figure(figsize=(7,5))

    # KDE plot for each subject
    for subject in df['subject'].unique():
        sns.kdeplot(
            data=df[df['subject'] == subject],
            x="grade",
            label=subject,
            fill=True
        )

    plt.title("KDE Plot of Grades per Subject (Day98)")
    plt.xlabel("Grades")
    plt.ylabel("Density")
    plt.legend(title="Subjects")
    plt.tight_layout()
    plt.show()

    conn.close()

seaborn_kdeplot()

import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_pairplot():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade FROM exams", conn)

    sns.set(style="whitegrid")

    # Pairplot to show relationships
    pairplot = sns.pairplot(df, hue="subject", palette="Set2")

    pairplot.fig.suptitle("Pairplot of Grades per Subject (Day98)", y=1.02)
    plt.show()

    conn.close()

seaborn_pairplot()

import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_catplot():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade FROM exams", conn)

    sns.set(style="whitegrid")

    # Catplot for grades per subject
    catplot = sns.catplot(
        x="subject",
        y="grade",
        kind="box",
        data=df,
        palette="Set3",
        height=5,
        aspect=1.2
    )

    catplot.fig.suptitle("Catplot of Grades per Subject (Day98)", y=1.02)
    plt.show()

    conn.close()

seaborn_catplot()