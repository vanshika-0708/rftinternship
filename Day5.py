import csv
def read_csv_to_dicts(filename):
    records=[]
    with open(filename,'r')as f:
        reader=csv.DictReader(f)
        for row in reader:
            record={}
            for key,value in row.items():
                key=key.strip()
                value=value.strip()if value else None
                #convert numeric fields,handle missing values
                if key in('AGE','MARKS'):
                    try:
                        record[key]=int(value)if value else None
                    except ValueError:
                        record[key]=None
                else:
                    record[key]=value if value else None
            records.append(record)
        return records
    

def calculate_average_marks(records):
    marks=[r['MARKS'] for r in records if r.get ('MARKS')is not None]
    if not marks:
        return None
    return sum(marks)/len(marks)

#create simple csv
with open('students.csv','w')as f:
    f.write("NAME,AGE,MARKS\n")
    f.write("AMIT,25,85\n")
    f.write("RIYA,21,90\n")
    f.write("JOHN,,78\n")
#run
data=read_csv_to_dicts('students.csv')
print("Parsed Data:")
print("[")
for record in data:
    print(f"{record},")
print("]")

avg = calculate_average_marks(data)
print(f"Average Marks(ignoring missing):{avg:2f}"if avg else"No marks data.")
missing=[r['NAME']for r in data if r.get('MARKS')is None or r.get('AGE')is None]
if missing:
    print(f"Students with missing values:{missing}")



                    

        
