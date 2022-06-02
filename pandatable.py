from turtle import pd


import panda as pd
df = pd.read_html('https://en.wikipedia.org/wiki/Poverty')
df[1]