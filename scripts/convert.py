import sys

if len(sys.argv) != 4:
    print "Usage:", sys.argv[0], "stock_sypbol, source_csv_file, dest_txt_file"
    exit(1)

file csv  = open(sys.argv[2], "r")
file dest = open(sys.argv[3], "w")

stock_sypbol = sys.argv[1]

for line in csv.readlines():
    if "Date" in line:
        continue

    # Sample data in csv:
    # 2015-12-11,27.00,27.75,26.50,26.75,74803500,26.75
    # Want to convert to:
    # stock,symbol=000917 open=27,high=27.75,low=26.5,close=26.75,volume=74803500,adj_close=26.75 1449817200

    values = line.split(',')
    print "Original line:", line








