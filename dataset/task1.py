from data import make_data
import plotly
import plotly.graph_objs as go

file=open('FRvideos.csv','r', encoding="utf8")
dataset=make_data(file)
print(dataset)
#вивести стовпчикову діаграму з кілкістю відео за кожну дату
new_dict=dict()
for category_id in dataset:
    for date in dataset[category_id]:
        if date in new_dict:
            new_dict[date]+=len(dataset[category_id][date].values())
        else:
            new_dict[date] = len(dataset[category_id][date].values())

diagram = go.Bar(
    x=list(new_dict.keys()),
    y=list(new_dict.values())
)
fig = go.Figure(data=[diagram])
plotly.offline.plot(fig, filename='graph1.html')

#вивести кругову діаграму з кількістю відео в кожній категорії
new_new_dict=dict()
for category_id in dataset:
    for date in dataset[category_id]:
        if category_id in new_new_dict:
            new_new_dict[category_id]+=len(dataset[category_id][date].values())
        else:
            new_new_dict[category_id] = len(dataset[category_id][date].values())

diagram = go.Pie(labels=list(new_new_dict.keys()), values=list(new_new_dict.values()))

plotly.offline.plot([diagram], filename='graph2.html')