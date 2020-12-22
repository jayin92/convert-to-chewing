path = input("Text file path >")

with open(path, "r") as file:
    data = file.read()

alpha   = "1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik,9ol.0p;/-"
chewing = "ㄅㄆㄇㄈㄉㄊㄋㄌˇㄍㄎㄏˋㄐㄑㄒㄓㄔㄕㄖˊㄗㄘㄙ˙ㄧㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦ"

for idx in range(len(alpha)):
    data = data.replace(alpha[idx], chewing[idx])

with open("output.txt", "w") as file:
    file.write(data)

