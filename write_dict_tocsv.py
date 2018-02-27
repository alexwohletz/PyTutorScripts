with open('dict.csv','w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Colname1","Colname2"])
    for key,value in {item[0]:item[1] for item in zip(l1,l2)}.items():

        writer.writerow([key,value])