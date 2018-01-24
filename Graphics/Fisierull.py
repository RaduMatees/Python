import csv
file_cpulog = open('cpulog.csv')
cpu_log = []
for line in file_cpulog:
    data_line = line.rstrip().split('\t')
    cpu_log.append(data_line)
for line in cpu_log:
        print(line)
for line in cpu_log:
    print(line[0]," ",line[0][11:13])
hour=0
suma=0
contor=0
for line in cpu_log:
   if(hour==int(line[0][11:13])):
    suma=suma+float(line[2])
    contor=contor+1

   else:
       if(contor==0):
           print("La ora ",hour," media este 0")
       else:
            media=suma/contor
            print("La ora ",hour," media este",media)
            suma=float(line[2])
            hour=hour+1
            contor=0
media=suma/contor
print("La ora ",hour," media este",media)
file_cpulog = open('cpulog.csv')
