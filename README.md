## CNN Classifier Project with proper folder structure and AIOPS

- **Step 01:** Create the 'template.py' to automatically create the folder structure.
  - The Path library is used to avoid the notation conflict of paths in Windows and Linux.
    1.  **Windows path:** F:\Machine_Learning\full_stack_data_science-ineuron\Computer Vision\CNNProjectStructure>
    2.  **Linux path:** /home/ubuntu/full_stack_data_science-ineuron/Computer Vision/CNNProjectStructure>
        > from pathlib import Path  
        > print(Path('x/y/z.txt'))
    3.  **Output:** x\y\z.txt  
        Since, we are using Windows machine. It will become x/y/z.txt if we were using a linux machine. Path library adjusts the path according to the OS.
