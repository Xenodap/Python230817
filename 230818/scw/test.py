L=open("./230818/scw/Lyrics.txt",'r',encoding='UTF8')

L_lyric=L.readlines()
L.close()

print(L_lyric)

contents=""
for line in L_lyric:
    contents=contents+line.strip()+"\n"
    #contents에 1라인씩넣으면서 반복 줄바꿈시 나눈다

Num_of_me=contents.count("내")
print(Num_of_me)
print(f"'내' 가 나온 횟수:{Num_of_me}")