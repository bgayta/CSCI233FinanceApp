import csv
import os
import glob

#Enter folder that contains all downloaded financial files
directory = input("Enter input folder name: ")
#Enter folder where you want to put transposed files
output = input("Enter input folder name: ")
in_files = os.path.join(directory, '*.csv')

for in_file in glob.glob(in_files):
    with open(in_file) as input_file:
        reader = csv.reader(input_file)
        cols = []
        for row in reader:
            cols.append(row)

    # "outdent" this code so it only needs to run once for each in_file
    filename = os.path.splitext(os.path.basename(in_file))[0] + '.csv'

    # Indent this to the same level as the rest of the "for in_file" loop!
    with open (os.path.join(output, filename), 'w') as output_file:
        writer = csv.writer(output_file)
        for i in range(len(max(cols, key=len))):
            writer.writerow ([(c[i] if i<len(c) else '') for c in cols])
