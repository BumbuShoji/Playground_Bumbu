import numpy as np
import numpy.random as random
import scipy as sp
import pandas as pd
import sys
sys.path.append('/Users/ryusukekimura/Desktop/GCI/week5')

from pandas import Series, DataFrame

#可視化ライブラリ
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns


#機械学習ライブラリ
import sklearn

#データの読み込み
import requests, zipfile
import io

#自動車の価格データを取得
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'
res = requests.get(url).content

#zipファイルを解凍
auto = pd.read_csv(io.StringIO(res.decode('utf-8')), header=None)

#カラム名を設定
auto.columns =['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration', 'num-of-doors',
                            'body-style', 'drive-wheels', 'engine-location', 'wheel-base', 'length', 'width', 'height',
                            'curb-weight', 'engine-type', 'num-of-cylinders', 'engine-size', 'fuel-system', 'bore',
                            'stroke', 'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']
 




