import os
import signal
#TODO:assign this to a thread so it can run in background
class processesObserver:
    @staticmethod
    def get_process_data()->list[dict]:
        process_list = []
        try:
            for pid in os.listdir('/proc'):
                if pid.isdigit():
                    with open(os.path.join('/proc', pid, 'status'), 'r') as f:
                        status_info = f.readlines()
                    mem_usage = 0
                    for line in status_info:
                        if line.startswith('VmRSS:'):
                            process_name = status_info[0].split()[1]
                            mem_usage = int(line.split()[1]) * 1024
                            break
                    process_list.append({'pid': int(pid),'name':process_name,'memory_usage':mem_usage})
        except Exception as e:
            print(f"Error while fetching process data: {e}, maybe was dead already?")
        return process_list






#TODO: assign this to a thread so it can run in background
class MemoryManagment:

    @staticmethod
    def peak_memory_usage() -> int:
        return 512 * 1024 * 1024  # 512 MB



    @staticmethod
    def limit_resources(pid: int, max_bytes:int, max_cpu_seconds: int = 10):
        try:
            os.system(
                f"prlimit --pid {pid} --as={max_bytes} --cpu={max_cpu_seconds}"
            )
            print(f"Limited resources for process {pid}.")
        except Exception as e:
            print(f"Failed to limit resources for process {pid}: {e}, RUNNING OUT OF OPTIONS")



    #TODO: change to a real parent instead of environment parent
    @staticmethod
    def parent_killer(pid: int):
        try:
            print(f"Attempting to kill parent of process {pid} due to high memory usage.")
            sender = os.getpgid(pid=pid)
            os.kill(sender, signal.SIGKILL)
        except Exception as e:
            print(f"Failed to kill parent of process {pid}: {e}, trying to limitate the usage of memory and cpu instead")
            MemoryManagment.limit_resources(pid,MemoryManagment.peak_memory_usage(), 10)



    @staticmethod
    def sleep_process(pid: int):
        try:
            print(f"Process {pid} trying to sleep due to high memory usage.")
            os.killpg(pid, signal.SIGSTOP)
        except Exception as e:
            print(f"Failed to put process {pid} to sleep: {e}, trying to kill the parent instead.")
    
    @staticmethod
    def killproccess(pid: int):
        try:
            os.kill(pid, signal.SIGKILL)
            print(f"Process {pid} has been killed due to high memory usage.")

        except Exception as e:
            print(f"Failed to kill process {pid}: {e}, trying to sleep instead.")
            MemoryManagment.sleep_process(pid)

