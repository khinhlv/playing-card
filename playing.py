import sys
import re

input_suites = []
input_ranks = []
same_suites = []
same_ranks = []

find_all = lambda s, lst: (i for i,e in enumerate(lst) if e == s)

# parse parameter into arrays input_suites, input_ranks
def parse_params(input_string):
	
  for s in input_string:
    if s == '1':
      c = s	 
    if s == '0':
      s = c + s

    if s in ['S', 'H', 'D', 'C']:
      input_suites.append(s)
    elif s in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
      input_ranks.append(s)

# find max ranks
def find_same_ranks_suites(input_suites, input_ranks):
	
  for rank in input_ranks:
    r = list(find_all(rank, input_ranks))
    same_ranks.append(len(r))
	
  for suite in input_suites:
    s = list(find_all(suite, input_suites))
    same_suites.append(len(s))	

# playing card function
def playing_card(input_suites, input_ranks):
  output = ''
  find_same_ranks_suites(input_suites, input_ranks)
  same_max = max(same_ranks)
	
  if same_max == 4:
    output = '4C'
  elif same_max == 3:
    one_pair = list(find_all(same_max - 1, same_ranks))
    if len(one_pair) == 2:
      output = 'FH'
    else:
      output = '3C'
  elif same_max == 2:
    two_pairs = list(find_all(same_max, same_ranks))
    if len(two_pairs) == 4:
      output = '2P'
    else:
      output = '1C'
  else:
    output = '--'

  return output

def main(argv):
  # validate argument
  if len(sys.argv) != 2:
    print 'Please call function with 1 argument, Ex: python playing.py D4C4C8D8S4'
    sys.exit()
	
  input_string = sys.argv[1]
  # validate input string
  pattern = '^(([S H D C])([2-9]|10|([J Q K A]))){5}$'
  pattern = re.compile(pattern)
  match = re.search(pattern, input_string)
  if not match:
    print 'Argument len 10 ~ 15 characters with format {suite}{rank}, Ex: D4C4C8D8S4'
    sys.exit()

  # parse input params to array
  parse_params(input_string)
  # main process
  print playing_card(input_suites, input_ranks)

if __name__ == "__main__":
  main(sys.argv[1:])
