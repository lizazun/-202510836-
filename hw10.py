import os
import pickle

def input_scores():
    scores = []
    i = 1
    print("[점수 입력]")
    while True:
        score = int(input(f"#{i}? "))
        if score < 0:
            break
        scores.append(score)
        i += 1
    return scores

def show_scores(scores):
    print("[점수 출력]")
    print("개인점수:", end=' ')
    for s in scores:
        print(s, end=' ')
    print()

def get_average(scores):
    return sum(scores) / len(scores)

def save_scores(scores):
    with open("score.bin", "wb") as f:
        pickle.dump(scores, f)

def load_scores():
    with open("score.bin", "rb") as f:
        return pickle.load(f)

if os.path.exists("score.bin"):
    print("[파일 읽기]")
    scores = load_scores()
else:
    scores = input_scores()
    save_scores(scores)

show_scores(scores)
print(f"평균: {get_average(scores):.1f}")
