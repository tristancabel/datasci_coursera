import os
import io
import sys
import codecs
import string
import operator

import pandas  as pd
import numpy   as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split
from sklearn import metrics

from zipfile    import ZipFile, is_zipfile
from contextlib import contextmanager

# Plotting Options
sns.set_style("whitegrid")
sns.despine()

def plot_bar(df, title, filename):
    """
    Helper function for plotting barplots.
    Color selection is made at random from a tuple of seabonrn colorsets
    """
    p = (
        'Set2', 'Paired', 'colorblind', 'husl',
        'Set1', 'coolwarm', 'RdYlGn', 'spectral'
    )
    color = sns.color_palette(np.random.choice(p), len(df))
    bar   = df.plot(kind='barh',
                    title=title,
                    fontsize=8,
                    figsize=(12,8),
                    stacked=False,
                    width=1,
                    color=color,
    )

#    bar.figure.savefig(filename)

    plt.show()

def plot_top_crimes(df, column, title, fname, items=0):
    """
    Helper function for plotting seaborn plots
    """
    lower_case     = operator.methodcaller('lower')
    df.columns     = df.columns.map(lower_case)
    by_col         = df.groupby(column)
    col_freq       = by_col.size()
    col_freq.index = col_freq.index.map(string.capwords)

    #col_freq.sort(ascending=True, inplace=True)

    plot_bar(col_freq[slice(-1, - items, -1)], title, fname)
    
def periodOfDay(date_string):
    date = pd.to_datetime(date_string)
    if date.hour > 5 and date.hour <=9 :
        return 'morning'
    if date.hour > 9 and date.hour <=17 :
        return 'businessHour'
    if date.hour > 17 and date.hour <=23 :
        return 'evening'
    return 'night'
    
   

def setPeriodOfDay(df):
    """
    add a column period of the day containing either : morning ]05,09], businessHour ]09:17], evening ]17,23], night ]23am,05] 
    """
    df['PeriodOfDay'] = df.index.map(periodOfDay)
#    df['PeriodOfDay'] = map(periodOfDay, df['Dates'])


def setHour(df):
    df['Hour'] = df.index.map(lambda date_string : pd.to_datetime(date_string).hour)

def setDayToNumber(df):
    df['WeekDay'] = df.index.map(lambda date_string : pd.to_datetime(date_string).weekday)
    df.drop(['DayOfWeek'],inplace=True,axis=1)

def extract_csv(filepath):
    zp  = ZipFile(filepath)
    csv = [
        f for f in zp.namelist()
            if os.path.splitext(f)[-1] == '.csv'
    ]
    return zp.open(csv[0])

@contextmanager
def zip_csv_opener(filepath):
    """
    Context manager for opening zip files.

    Usage
    -----
    with zip_csv_opener(filepath) as fp:
        raw = fp.read()
    """
    fp = extract_csv(filepath) if is_zipfile(filepath) else open(filepath, 'rb')
    try:
        yield fp
    finally:
        fp.close()

def input_transformer(filepath):
    """
    Read file input and transform it into a pandas DataFrame
    """
    with zip_csv_opener(filepath) as fp:
        raw = fp.read()
        raw = raw.decode('utf-8')

    return pd.read_csv(io.StringIO(raw), parse_dates=True, index_col=0, na_values='NONE')

def main(filepath):
    """
    Script Entry Point
    """
    print 'reading data'
    df = input_transformer(filepath)
    #filter unused data
    print 'filter data'
    df.drop(['Descript', 'PdDistrict', 'Resolution', 'Address'],inplace=True,axis=1)

    #pass columns to numbers
    setHour(df)
    setDayToNumber(df)

#    setPeriodOfDay(df)
    #only focus on drunkenness
    #df_cat = df[df['Category']=='DRUNKENNESS']

    #set train and test
    print 'split data'
    df_x = df[['WeekDay','X','Y','Hour']]
    df_y = df['Category']
    #print df_x.head(2)
    print df_y.head(20)
    x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size = 0.2)

    #learn
    print ' Start learning'
    #knn = SVC()
    knn = KNeighborsClassifier(n_neighbors=20, n_jobs=4)
    knn.fit(x_train, y_train)
    print(knn)

    #give a dayofWeek, X, Y, and PeriodOfDay and predict Category
    print ' start prediction'
    predict = knn.predict(x_test)
    print ' prediction done'
    
    #compare predictions and reality
    nb_equal = np.sum(y_test==predict)
    print "number of equality", nb_equal
    print "number of test elements", y_test.size
    proba = 100*nb_equal/y_test.size
    print "proba correct " , proba

    
    # summarize the fit of the model
    print(metrics.classification_report(y_test, predict))
###    print(metrics.confusion_matrix(y_test, predict))

    
#    plot_top_crimes(df, 'category',   'Top Crime Categories',        'category.png')
#    plot_top_crimes(df, 'resolution', 'Top Crime Resolutions',       'resolution.png')
#    plot_top_crimes(df, 'pddistrict', 'Police Department Activity',  'police.png')
##    plot_top_crimes(df_cat, 'dayofweek',  'Days of the Week',            'weekly.png')
#    plot_top_crimes(df_cat, 'address',    'Top Crime Locations',         'location.png', items=20)
#    plot_top_crimes(df, 'descript',   'Descriptions',                'descript.png', items=20)


if __name__ == '__main__':
#    sys.exit(main('test.csv.zip'))
    sys.exit(main('train.csv'))
