import os

class Bash_History(object):
  def __init__(self):
    self.cmds = list()

  def add_commands(self, commands):
    self.cmds.append(commands)

class Command(object):
  def __init__(self, line):
    self.full_command = line
    self.cmd = self.full_command.split(' ')[0]
    self.params = self.full_command.split(' ')[1:]

# TODO
# Add support for parsing multiple commands in a line. 
# Important information if commands all listed in one line?
def get_bash_histories():
  bash_histories = list()
  root_filepath = "./data/"
  for r, d, f in os.walk(root_filepath):
  files = f 
    for f in files:
      with open(root_filepath + f, 'r') as bhf:
        bh = Bash_History()
        for l.strip() in bhf:
        # Check for multiple commands per line
          if ';' in l:
            cmds = l.split(';')
            for cmd in cmds:
              c = Command(l)
                bh.add_commands(c)
          else:
            c = Command(l)
            bh.add_commands(c)
        bash_histories.append(bh)
  return bash_histories

def main():
  bash_histories = get_bash_histories()

if __name__ == '__main__':
main()