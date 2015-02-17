from collections import Counter

import matplotlib.pyplot as plt
import data_reader

def avg_cmds(bash_histories):
  cmd_count = 0
  bh_count = len(bash_histories)
  for bh in bash_histories:
    cmd_count += len(bh.cmds)
  print cmd_count
  return float(cmd_count)/bh_count

def avg_cmds_distinct(bash_histories):
  cmd_count = 0
  bh_count = len(bash_histories)
  for bh in bash_histories:
    cmd_count += len(Counter(bh.cmds).keys())
  print cmd_count
  return float(cmd_count)/bh_count

def plot_bash_history(bh):
  cmds = list()
  for c in bh.cmds:
    cmds.append(c.full_cmd)

  cmds_counter = Counter(cmds)
  for c in cmds_counter:
    cmds_counter[c] /= float(len(cmds))

  plt.bar(range(0, len(cmds_counter.keys())), cmds_counter.values())
  plt.xlabel('Distinct Command')
  plt.ylabel('Normalised Counts of Distinct Command')
  plt.show()

def main():
  bash_histories = data_reader.get_bash_histories()
  print "No. of bash histories: " + str(len(bash_histories))
  print "Average no. of commands per bash history: " + str(avg_cmds(bash_histories))
  print "Average no. of distinct commands per bash history: " + str(avg_cmds_distinct(bash_histories))
  #for bh in bash_histories:
    #plot_bash_history(bh)

if __name__ == '__main__':
  main()