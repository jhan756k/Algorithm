numprac = int(input())

for _ in range(numprac):
  std, brown = map(int, input().split())
  print("Practice #" + str(_+1) + ": " + str(std) + " " + str(brown))
  group = int(input())
  for g in range(group):
    nums = int(input())
    while (brown - nums <= 0):
      brown *= 2
    brown -= nums
    print(nums, brown)
  print()