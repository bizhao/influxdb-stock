import sys
import time

if len(sys.argv) != 4:
    print 'Usage:', sys.argv[0], 'stock_symbol, source_csv_file, dest_txt_file'
    exit(1)

csv  = open(sys.argv[2], 'r')
dest = open(sys.argv[3], 'w')

prefix = 'stock,symbol=' + sys.argv[1]

for line in csv.readlines():
    if 'Date' in line:
        continue

    # Sample data in csv:
    # 2015-12-11,27.00,27.75,26.50,26.75,74803500,26.75
    # Want to convert to:
    # stock,symbol=000917 open=27.00,high=27.75,low=26.50,close=26.75,volume=74803500,adj_close=26.75 1449817200

    values = line.split(',')
    # print 'Original line:', line
    timestamp = int(time.mktime(time.strptime(values[0], '%Y-%m-%d')))
    newline = prefix + ' open=' + values[1] + ',high=' + values[2] + ',low=' + values[3]
    newline += ',close=' + values[4] + ',volume=' + values[5] + ',adj_close=' + values[6]
    newline = newline.strip('\n') + ' ' + str(timestamp) + '\n'
    # print 'New line:', newline
    dest.write(newline)

dest.close()
csv.close()






