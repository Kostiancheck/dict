import re

def chek(line, i):
    category_id=line[i]
    if bool(re.match(r"^\d*$", category_id)) == False:
        category_id=chek(line, i + 1)
    return category_id

def make_data(file):
    dataset = dict()
    header = file.readline().split(',')[0:5]
    print('header', header)
    for line in file:
        line=line.split(',')
        video_id=line[0]
        trending_date=line[1]
        title=line[2]
        channel_title=line[3]
        category_id = chek(line,4)
        add_in_dataset(dataset, category_id, trending_date, video_id, channel_title, title)
    return dataset
    file.close()





def add_in_dataset(dataset, category_id, trending_date, video_id, channel_title, title):
    temporary_data={'video_id':video_id, 'channel_title':channel_title, 'title':title}
    #   Якщо ця вікова категорія є в dataset
    if category_id in dataset:
        if trending_date in dataset[category_id]:
            #Оскільки video_id є унікальним, то воно не може зустрітися декілька разів, тому ми не перевіряємо його наявність
            dataset[category_id][trending_date][video_id]=temporary_data
        else:
            dataset[category_id][trending_date] = {video_id: temporary_data}

    else:
        dataset[category_id] = {trending_date: {video_id: temporary_data}}

