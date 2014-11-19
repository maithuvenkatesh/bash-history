import os

class Bash_History(object):
    def __init__(self):
        self.cmds = list()

    def add_commands(self, commands):
        self.cmds.append(commands)

class Command(object):
    def __init__(self, line_args):
        self.cmd = line_args[0]
        self.params = line_args[1:]

def read_data():
    bash_histories = list()
    root_filepath = "./data/"
    for r, d, f in os.walk(root_filepath):
        files = f
        for f in files:
            with open(root_filepath + f, 'r') as bhf:
                bh = Bash_History()
                cmds = [Command(l.strip().split(' ')) for l in bhf]
                bh.add_commands(cmds)
                bash_histories.append(bh)

def main():
    cmds_list =   read_data()

if __name__ == '__main__':
  main()