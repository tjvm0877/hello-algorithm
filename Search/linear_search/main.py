from sequence_ssearch_for import seq_search


t = (4, 7, 5.6, 2, 3.14, 1)
s = "string"
a = ["DST", "AAC", "FLAC"]

print(f"{t}에서 5.6의 인덱스는 {seq_search(t, 5.6)}입니다.")
print(f'{s}에서 "n"의 인덱스는 {seq_search(s, "n")}입니다.')
print(f'{a}에서 "DTS"의 인덱스는 {seq_search(a, "DST")}입니다.')
