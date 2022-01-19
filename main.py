# this is a program that calculates the total score for a students result
# when line 16 is in line 14 it says "this code is unreachable"
# Line 16 displays before the RETRUN code in line 13, WHY? It is supposed to be the reverse
#Enter first test score
#Enter exam score

test = 30


def total_scores(score_int):
    if score_int >= 40:
        return f"You passed your exams and your total score is {score_int + test}"
    else:
        return "you performed poorly, kindly repeat the exam."


# Check time of video at 1hr 36 mins for inout validation to avoid program crash
def validation_process():
    if entered_score.isdigit():
        score_int = int(entered_score)
        var_scores = total_scores(score_int)
        print(var_scores)
    else:
        print("Invalid input")


entered_score = input("Please enter the students exam score.\n")

validation_process()