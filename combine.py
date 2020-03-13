import datetime
#date_object = datetime.datetime.strptime(str, '%m/%d/%y')
import glob
# Combines multiple input files in. Added a counter for how many files were inputted/concatenated.
# Primary Practical use has been data analyis across multiple sources with an identical layout (example being multiple clientids, but identical source layout) 
filenames = glob.glob ("G:/inbound/*")

try:                       #['foo1.txt', 'foo2.txt',   'r']
    with open('G:/outbound/cmb_outbound.txt', 'w') as outfile: # 'BPS_cmb_non_W.txt'
        i = 0
        for fname in filenames:
            i += 1
            with open(fname) as infile:
                print(f"Writing Input file {i} at {datetime.datetime.now()}")
                #print("the TMS DF cols are %s" %df_p2.columns)
                for line in infile:
                    outfile.write(line)
except IOError: 
    print("IO Error!")
outfile.close()
quit = input("Press the X button to exit. Script complete.")