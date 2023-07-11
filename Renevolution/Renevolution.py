import space
import os
import time
import thankyoumessage

class Renevolution:
    def __init__(self):
        pass

    def start(self,folder,new):
        counter_folders = 0        
        start_process = time.time()
        for file_name in os.listdir(folder_path):
            old_name = folder + file_name
            current_name = new + old_name
            os.rename(old_name,current_name)


        for counter in range(counter_folders): 
            print(os.listdir(folder_path))
        
        
        end_process = time.time()
        space.space()
        enumerate_files = 1
        for file in range(counter_folders):
            print(f'{enumerate_files} File - {folder_path[file]}')
            enumerate_files += 1
        return f'Process finished in {(end_process - start_process):.2f} seconds. \033[1;33m\n{space.space()}\nEnd of Program!'

space.space()
RT = Renevolution()
folder_path = input('Enter the path of folder > ')
new_name = input('What do you wish to insert which name in the folder(s)? >')
print(RT.start(folder_path,new_name))
