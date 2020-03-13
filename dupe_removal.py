import glob
import time,datetime,os
etl_time = datetime.datetime.now().strftime('%Y%m%d%H%M')


start = time.time()
print(f'Script Executing at {start}.')

#globbed_files = glob.glob(r'G:\\cmb_fast_inbound\\*')  # creates a list of all csv files
globbed_files = glob.glob(r'G:\\inbound\\*')  # creates a list of all csv files

i = 0
for in_file in globbed_files:
    fname = os.path.basename(in_file)
    out_file = open(f'G:\\outbound\\test_{fname}_{etl_time}.txt','w') 
    i += 1
    seen = set() # set for fast O(1) amortized lookup
    with open(in_file) as f:
        for line in f:
            if line in seen: continue # skip duplicate
            seen.add(line)
            out_file.write(line)
        out_file.close()
    print(f"Writing Output dupes file #{i} at {datetime.datetime.now()}")

quit = input('Press the X button to exit. Script complete.')