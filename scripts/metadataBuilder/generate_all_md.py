import os
import subprocess
import glob
import threading
import itertools
import sys
import time

def spinner(msg, stop_event):
    for c in itertools.cycle('⠷⠯⠟⠻⠽⠾'):
        if stop_event.is_set():
            break
        sys.stdout.write(f'\r{msg} {c}')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * (len(msg) + 2) + '\r')

# Step 1: Run fetchMeta.py and wait for it to finish
stop_event = threading.Event()
spin_thread = threading.Thread(target=spinner, args=('', stop_event))
spin_thread.start()
subprocess.run(['python3', 'fetchMeta.py'], check=True)
stop_event.set()
spin_thread.join()
print('Fetching... done.')

# Step 2: Find all JSON files in metaJSON
meta_json_dir = os.path.join(os.path.dirname(__file__), 'metaJSON')
json_files = glob.glob(os.path.join(meta_json_dir, '*.json'))

# Step 3: For each JSON file, run json_to_md.py with spinner
for json_file in json_files:
    stop_event = threading.Event()
    spin_thread = threading.Thread(target=spinner, args=(f'Converting {os.path.basename(json_file)}', stop_event))
    spin_thread.start()
    subprocess.run(['python3', 'json_to_md.py', json_file], check=True)
    stop_event.set()
    spin_thread.join()
    # print(f'Converted {os.path.basename(json_file)}')

print('All markdown files generated into ./toMD')