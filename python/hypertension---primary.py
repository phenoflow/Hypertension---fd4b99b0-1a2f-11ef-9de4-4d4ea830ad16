# Kethryn E Mansfield, Dorothea Nitsch, Liam Smeeth, Krishnan Bhaskaram, Laurie A Tomlinson, 2024.

import sys, csv, re

codes = [{"code":"14A2.00","system":"readv2"},{"code":"67H8.00","system":"readv2"},{"code":"G203.00","system":"readv2"},{"code":"G202.00","system":"readv2"},{"code":"246M.00","system":"readv2"},{"code":"662H.00","system":"readv2"},{"code":"G20z.11","system":"readv2"},{"code":"7Q01.00","system":"readv2"},{"code":"G20..11","system":"readv2"},{"code":"1JD..00","system":"readv2"},{"code":"G20..12","system":"readv2"},{"code":"6624","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hypertension-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hypertension---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hypertension---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hypertension---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
