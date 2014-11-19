from collections import Counter

import matplotlib.pyplot as plt
import data_reader

def plot_bash_history(bh):
  cmds = list()
  for c in bh.cmds:
    cmds.append(c.full_cmd)

  plt.plot(cmds.values())
  plt.xlabel('Distinct Commands')
  plt.ylabel('Counts of Distinct Commands')
  plt.show()

def main():
  bash_histories = data_reader.get_bash_histories()
  plot_bash_history(bash_histories[0])

if __name__ == '__main__':
  main()