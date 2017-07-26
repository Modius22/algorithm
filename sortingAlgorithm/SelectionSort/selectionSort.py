def selectionsort (sequence)
  for i in range (len(sequence) -1):
    c = i
    for j in range (i + 1, len(sequence)):
      if sequence[j] < seqcuence[c]:
        c = j
    sequence[i],sequence[c] = sequence[c], sequence[i] 
