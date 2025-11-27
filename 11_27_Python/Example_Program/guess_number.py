import random

secret_number =random.randint(1,20)
print("1에서 부터 20까지 숫자중 생각하고 있습니다.")

#6번 사용자에게 물어본다.
for guessesTaken in range(1,7):
    print("예측해보아라")
    guess = int(input())

    if guess < secret_number:
        print("너가 예측한 숫자보다 큰 수입니다")
    elif guess > secret_number:
        print("너가 예측한 숫자보다 작은 수입니다")
    else:
        break 

if guess == secret_number:
    print("잘하셨습니다. 당신은 제가 생각한 숫자" + str(secret_number)+ " 를 " +str(guessesTaken)+  "번만에 맞췄습니다.")
else:
    print("틀렸습니다. 당신은 제가 생각한 숫자 " + str(secret_number)+ " 를 " +str(guessesTaken)+  "번 동안 맞추지 못했습니다")
