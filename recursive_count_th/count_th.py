'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

 # Start with the base
 # If the word only has 1 letter, it cannot contain "th"
  if len(word) <= 1:
        return 0
 # Looking for occurrences of "th" within a given word.
 # Must start with t so we check everything following our initial index[0]
 # Utilize recursion. Cannot use ANY loops. 
  if word[0] == "t" and word[1] == "h":
        return 1 + count_th(word[1:])
  else:
        return count_th(word[1:])

  # count of occurences of ***"th"*** occur within `word`:
  # ""   = count 0
  # "t"   = count 0
  #  "rath"= count 1
  # "rathrsth" = count 2
  # "rathrathdfrth" = count 3
  # and so on

    
