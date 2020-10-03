import csv

def merge_csv(csvlist,output):
    fieldnames=[]
    for file in csvlist:
        with open(file,'r') as in_file:
            fn = csv.DictReader(in_file).fieldnames
            fieldnames.extend(x for x in fn if x not in fieldnames)
    with open(output,'w') as out_file:
        wn = csv.DictWriter(out_file, fieldnames)
        wn.writeheader()
        for file in csvlist:
            with open(file,'r') as in_file:
                fn = csv.DictReader(in_file)
                for row in fn:
                    wn.writerow(row)
            
merge_csv(['Book1.csv','Book2.csv'],'Book3.csv')
