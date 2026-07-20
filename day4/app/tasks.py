class Tasks:
    task_lst=[]
    def add_task(self,name):
        self.task_lst.append(name)
    def display_tasks(self):
        for i in self.task_lst:
            print(i)

print(__name__)