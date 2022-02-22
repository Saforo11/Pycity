def get_ruler(kingdom):
  ruler = ''
  vowel_letter = {'a', 'e', 'i', 'o', 'u'}
  x = kingdom[-1]
# It should be either 'Alice', 'Bob' or 'nobody'.
  if x in vowel_letter:
    ruler = 'Alice'
  elif x == 'y':
    ruler = 'nobody'
  else:
    ruler = 'Bob'

  return ruler


def main():
# Get the number of test cases
  T = int(input())
  for t in range(T):
    # Get the kingdom
    kingdom = input()
    print('Case #%d: %s is ruled by %s.' % (t + 1, kingdom, get_ruler(kingdom)))

if __name__ == '__main__':
  main()
