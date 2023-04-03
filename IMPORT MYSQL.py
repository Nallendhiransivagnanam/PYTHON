import pymysql as p

db=p.connect(host='localhost', user='root', password='nallu99',db='nallu1')

mycursor=db.cursor()
q1 = ["INSERT INTO eee2016 ('REGNO', 'NAME', 'HSC', 'SSLC', 'AGE', 'UG') VALUES ('2', 'ajith', '1000', '400', '18', '89');, select * from eee2016"]
output = []
for query in q1:  
    mycursor.execute(query) 
    d = mycursor.fetchall()
    output.append(d)
db.close()

for x in output:
    print(x)
