import pandas as pa
import numpy as nu
import plotly.express as pe


data = pa.read_csv("project.csv")

ts = data["TOEFL Score"].tolist()
coa = data["Chance of Admit "].tolist()

fig = pe.scatter(x= ts , y = coa)

fig.show()

#---------------using hit and trial-------------

m, c = 1,0
y = []

for x in ts:
    y2 = m*x + c
    y.append(y2)

fig = pe.scatter(x=ts, y= coa)
fig.update_layout(
    shapes=[
        dict(
            x0 = min(ts),
            x1 = max(ts),
            y0 = min(y),
            y1 = max(y),
            type = "line",
        )
       
    ]
)
# fig.show()

# ----------------------------------- 2nd attempt ------------------------------
m, c = 0.018, -1.27
y = []

for x in ts:
    y2 = m*x + c
    y.append(y2)

fig = pe.scatter(x=ts, y= coa)
fig.update_layout(
    shapes=[
        dict(
            x0 = min(ts),
            x1 = max(ts),
            y0 = min(y),
            y1 = max(y),
            type = "line",
        )
       
    ]
)
# fig.show()

x = 250
y = m * x + c
print("Chances of admit if the TOEFL score 250 using hit and trial :-", y)


#--------------------using algo-------------

tsArray = nu.array(ts)
coaArray = nu.array(coa)

m,c = nu.polyfit(tsArray,coaArray,1)

y = []

for x in ts:
    y2 = m*x + c
    y.append(y2)

fig = pe.scatter(x=ts, y= coa)
fig.update_layout(
    shapes=[
        dict(
            x0 = min(ts),
            x1 = max(ts),
            y0 = min(y),
            y1 = max(y),
            type = "line",
        )
       
    ]
)
fig.show()

x = 250
y = m * x + c
print("Chances of admit if the TOEFL score 250 using algo :-", y)














