from asyncio import threads
import os
import re
import time
import pickle
import zipfile
import threading
from threading import Lock, Semaphore, Thread


#GLOBAL SHARED RESOURCES

INTELLIGENCE_VAULT = []
vault_lock = Lock()   #lock for syncherisation
agent_semaphore = Semaphore(3)

SECRET_FOLDER ="secret_files"
OUTPUT_FOLDER ="extracted_reports"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


#REGEX PATTERNS

EMAIL_PATTERN = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
DATE_PATTERN = r"\b\d{2}-\d{2}-\d{4}\b"
CODE_PATTERN = r"\b[A-Z]{2}-\d{2}-[A-Z]+\b"
KEYWORD_PATTERN = r"\b(TOP-SECRET|URGENT|CONFIDENTIAL)\B"


# FILE PROCESSIN FUNCTION
def analyze_file(filename, agent_name):
    with agent_semaphore:
        print(f"[{agent_name}]) Started analyzing {filename}")
        time.sleep(1)
        
        file_path = os.path.join(SECRET_FOLDER, filename)
        
        #FILE HANDLING
        with open(file_path, "r") as file:
            content = file.read()
            
        
        with open(file_path, "r")as file:
            file.seek(0)
            first_20_chars = file.read(20)
            
        # REGEX EXTRACTION    
        extracted_data = {
            "agent": agent_name,
            "file": filename,
            "emails": re.findall(EMAIL_PATTERN, content),
            "dates":re.findall(DATE_PATTERN, content),
            "codes": re.findall(CODE_PATTERN, content),
            "keywords":re.findall(CODE_PATTERN, content),
            "preview": first_20_chars
        }  
        
        #THREAD SYNCHRONIZATION(LOCK)
        with vault_lock:
            INTELLIGENCE_VAULT.append(extracted_data)
        
        #SAVE THE REPORTS
        report_file = os.path.join(OUTPUT_FOLDER, f"report_{filename}")
        with open(report_file, "w") as report:
            for key, value in extracted_data.items():
                report.write(f"{key}: {value}\n")
                
        print(f"[{agent_name}])Finished {filename}")

#MAIN FUNCTION
def main():
    print("\n HGA Mission Stsrted")
    thread = []
    
    for idx, file in enumerate(os.listdir(SECRET_FOLDER)):
        agent_name = f"agent-{idx+1}"
        t= Thread(target=analyze_file, args=(file, agent_name))
        thread.append(t)
        t.start()
        
    #THREAD JOIN
    for t in thread:
        t.join()
        
    print("\n Saving intelegence using pickle")
    
    #PICKLE DATA
    with open("intel.pkl","wb") as pkl_file:
        pickle.dump(INTELLIGENCE_VAULT, pkl_file)
        
    print("Zipping the mission report")
        
        
    #ZIP FILES
    with zipfile.ZipFile("mission_report.zip", "w") as zipf:
        zipf.write("intel.pkl")
        for file in os.listdir(OUTPUT_FOLDER):
            zipf.write(os.path.join(OUTPUT_FOLDER, file))
            
    print("\n Mission Complete Successfully")
    
    

#ENTRY POINT
if __name__ =="__main__":
      main()      


























