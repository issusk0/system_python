
from utils.threads import ThreadManager
from utils.observer import MemoryManagment, processesObserver
from pprint import pprint

def observe_processes():
    process_data = processesObserver.get_process_data()
    return pprint(process_data)


def auto_managment_memory():
    process_data = processesObserver.get_process_data()
    for process in process_data:
        name = process['name']
        pid = process['pid']
        memory_usage = process['memory_usage']
        if memory_usage > MemoryManagment.peak_memory_usage():
            print(f"Process {pid} ({name}) is using {memory_usage} bytes, exceeding the peak limit. Killing it.")
            MemoryManagment.killproccess(pid)

if __name__ == "__main__":
    manager = ThreadManager()
    manager.create_thread(target=auto_managment_memory, args=())
    manager.create_thread(target=observe_processes, args=())