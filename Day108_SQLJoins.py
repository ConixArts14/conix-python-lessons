import sqlite3
import pandas as pd

def sql_joins_demo():
    conn = sqlite3.connect("student_records.db")
    query = """
    SELECT s.name, s.section, e.subject, e.grade, e.exam_type
    FROM student_report s
    INNER JOIN exams e ON s.id = e.id
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    print(df)

sql_joins_demo()

# Day108_Activity2_Violinplot.py
import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def sql_violinplot_demo():
    conn = sqlite3.connect("student_records.db")
    query = """
    SELECT s.name, s.section, e.subject, e.grade, e.exam_type
    FROM student_report s
    INNER JOIN exams e ON s.id = e.id
    """
    df = pd.read_sql_query(query, conn)
    conn.close()

    # Create violinplot
    sns.violinplot(x="subject", y="grade", data=df)
    plt.title("Grade Distribution by Subject")
    plt.show()

sql_violinplot_demo()
