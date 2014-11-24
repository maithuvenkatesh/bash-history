from collections import Counter

import matplotlib.pyplot as plt
import data_reader

def get_ngrams(cmds_list, n):
  return zip(*[cmds_list[i:] for i in range(n)])

def plot_ngram_cmds(bh):
  cmd_ngrams = get_ngrams(bh.cmds)
  ngram_counter = Counter(cmd_ngrams)
  for s in ngram_counter:
    ngram_counter[c] /= float(len(bh.cmds))

  plt.bar(range(0, len(ngram_counter.keys())), ngram_counter.values())
  plt.xlabel('Distinct Command Sequences')
  plt.ylabel('Normalised Counts of Distinct Command Sequences')
  plt.show()


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
  print len(bash_histories)
  for bh in bash_histories:
    plot_bash_history(bh)

if __name__ == '__main__':
  main()