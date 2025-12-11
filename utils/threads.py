import threading

class ThreadManager:
    def __init__(self):
         self.threads_on_live = []

    def create_thread(self,target, args):
        threads_instance = threading.Thread(target=target, args=args)
        threads_instance.start()
        self.threads_on_live.append(threads_instance)
        while True:
            if threads_instance.is_alive():
                continue
            else:
                break
        return threads_instance
    