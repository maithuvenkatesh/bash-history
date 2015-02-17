import os

class Bash_History(object):
  def __init__(self, name):
    self.name = name
    self.cmds = list()

  def add_commands(self, commands):
    self.cmds.append(commands)

  def split_command(self):
    self.cmd = self.full_cmd.split(' ')[0]
    self.params = self.full_cmd.split(' ')[1:]

# Important information if commands all listed in one line?
def get_bash_histories():
  bash_histories = list()
  root_filepath = "./data/"
  for r, d, files in os.walk(root_filepath):
    for f in files:
      with open(root_filepath + f, 'r') as bhf:
        bh = Bash_History(f)
        for l in bhf:
          l = l.strip()
          # Check for multiple commands per line
          if ';' in l:
            cmds = l.split(';')
            for cmd in cmds:
              bh.add_commands(cmd)
          else:
            bh.add_commands(l)
        bash_histories.append(bh)
  return bash_histories

def main():
  bash_histories = get_bash_histories()

if __name__ == '__main__':
  main()