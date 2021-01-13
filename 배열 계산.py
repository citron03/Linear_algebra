# -*- coding: utf-8 -*-
#내장 함수 참조 : https://wikidocs.net/22216
# 참조 https://blogbugmaker.tistory.com/205, https://covenant.tistory.com/28
# 3개의 행렬을 각각 입력받기. 그리고 행렬의 계산.

# aA + (bB + cC), aA*(bB*cC), aA*(bB + cC), (bB + cC)*aA, aA+bB*cC


# 함수
def plus(list1, list2):
    Q = [[0 for columns in range (len(list1[0]))] for rows in range(len(list1))]
    #답을 리턴하기 위한 행렬 만들기
    for i in range(0,len(list1)):
        for j in range(0,len(list1[0])):
            Q[i][j] = list1[i][j] + list2[i][j]
    return Q

def minus(list1, list2):
    Q = [[0 for columns in range (len(list1[0]))] for rows in range(len(list1))]
    #답을 리턴하기 위한 행렬 만들기
    for i in range(0,len(list1)):
        for j in range(0,len(list1[0])):
            Q[i][j] = list1[i][j] - list2[i][j]
    return Q

def mul(list1, list2):
    Q = [[0 for columns in range (len(list2[0]))] for rows in range(len(list1))]
    #답을 리턴하기 위한 행렬 만들기
    for i in range(0,len(list1)):
        for j in range(0,len(list2[0])):
            for k in range(0,len(list1[0])):
                Q[i][j] += list1[i][k]*list2[k][j]
    return Q

def sca(list1,num):
    for i in range(0,len(list1)):
        for j in range(0,len(list1[0])):
            list1[i][j] *= num
    return list1


#본문 시작

while int(input("행렬을 입력하시겠습니까? 계속 하시겠다면 1 종료하시겠다면 0")) == 1:
    #일단 행렬을 입력 받는다.
    #첫번째 행렬
    Xa, Ya = map(int,input("A 행렬의 rows와 columns의 개수를 입력하세요").split())
    AA = [[0 for columns in range (Ya)] for rows in range(Xa)]
    for i in range(0,Xa):
        AA[i] = list(map(int,input("%d row의 숫자를 입력하세요" %(i)).split()))
    Aname = input("A행렬의 이름을 정해주세요")


    #두번째 행렬
    Xb, Yb = map(int, input("B 행렬의 rows와 columns의 개수를 입력하세요").split())
    BB = [[0 for columns in range(Yb)] for rows in range(Xb)]
    for i in range(0,Xb):
        BB[i] = list(map(int,input("%d row의 숫자를 입력하세요" %(i)).split()))
    Bname = input("B행렬의 이름을 정해주세요")

    #세번째 행렬
    Xc, Yc = map(int,input("C 행렬의 rows와 columns의 개수를 입력하세요").split())
    CC = [[0 for columns in range(Yc)] for rows in range(Xc)]
    for i in range(0,Xc):
        CC[i] = list(map(int,input("%d row의 숫자를 입력하세요" %(i)).split()))
    Cname = input("C행렬의 이름을 정해주세요")

    print("입력된 %s,%s,%s 세 행렬입니다." %(Aname, Bname, Cname))
    for rows in AA:
        print(rows)
    print("\n")
    for rows in BB:
        print(rows)
    print("\n")
    for rows in CC:
        print (rows)

    #연산문 입력    
    while int(input("연산을 입력하시겠습니까? 계속 하시겠다면 1 종료하시겠다면 0")) == 1:
        #연산을 입력받는다
        print("입력된 세행렬의 계산식은 간소화를 위해 각각 %s는 A, %s는 B, %s는 C로 지칭합니다. 괄호와 +와 -와 *기호를 사용할 수 있습니다" %(Aname, Bname, Cname))
        Calculation = input("확인할 계산식을 입력하세요")

        #각각 행렬과 똑같은 리스트를 만들어서
        A = [[0 for columns in range (Ya)] for rows in range(Xa)]
        B = [[0 for columns in range (Yb)] for rows in range(Xb)]
        C = [[0 for columns in range (Yc)] for rows in range(Xc)]
        #여러번 계산을 위해서 초기의 값을 보존해놓는다.
        for i in range(0,Xa):
            for j in range(0,Ya):
                A[i][j] = AA[i][j]
        for i in range(0,Xb):
            for j in range(0,Yb):
                B[i][j] = BB[i][j]
        for i in range(0,Xc):
            for j in range(0,Yc):
                C[i][j] = CC[i][j]

        #문자열 처리
        
        # scalar 곱셈 ####################################################################

        #숫자
        number = {'0','1','2','3','4','5','6','7','8','9'}
        #초기화
        scalar = 0
        #숫자를 발견시
        i = 0
        while(i != len(Calculation)):
            if(Calculation[i] in number):
                if(scalar == 0):
                    scalar = int(Calculation[i])
                else :
                    scalar *= 10
                    scalar += int(Calculation[i])
                Calculation = Calculation[:i] + Calculation[i+1:]
                i -= 1
            else:
                #숫자가 아닌 것을 만났을때 만약 축적된 scalar가 있으면 이를 만난 문자, 행렬에 곱해준다.
                if(scalar != 0):
                    if(Calculation[i] == 'A'):
                        sca(A,scalar)
                    elif(Calculation[i] == 'B'):
                        sca(B,scalar)
                    elif(Calculation[i] == 'C'):
                        sca(C,scalar)
                    #그리고 다시 scalar를 초기화 시켜준다
                    scalar = 0
            i += 1

        #()를 처리하고 곱셈 덧셈을 한다.

        #()처리#######################################################################################3

        if '(' in Calculation:
            if(Calculation[Calculation.index('(')-1] == '+' or Calculation[Calculation.index('(')-1] == '-'):
                Calculation = Calculation.replace('(','')
                Calculation = Calculation.replace(')','')
                # ( 의 왼쪽이 + 라면 그냥 ()둘다 지운다.
            elif(Calculation[Calculation.index('(')-1] == '*' and Calculation[Calculation.index(')')-2] == '*'):
                Calculation = Calculation.replace('(','')
                Calculation = Calculation.replace(')','')
                # ( 의 왼쪽이 곱셈일때, 오른쪽이 곱셉이면 그냥 ()둘다 지운다
            elif((Calculation.index('(') == 0 ) and ( (Calculation[Calculation.index(')')+1]) == '+' or  (Calculation[Calculation.index(')')+1]) == '-' )):
                Calculation = Calculation.replace('(','')
                Calculation = Calculation.replace(')','')
                # ( 의 왼쪽이 없고, )의 오른쪽이 덧셈이면 그냥 ()둘다 지운다. (A+B)+C
            elif(Calculation.index('(') == 0 and Calculation[Calculation.index(')')+1] == '*' and Calculation[Calculation.index('(')+2]) == '*':
                Calculation = Calculation.replace('(','')
                Calculation = Calculation.replace(')','')
                # (A*B)*C 일경우 그냥 순서대로 계산
            elif(Calculation.index('(') == 0 and Calculation[Calculation.index(')')+1] == '*' and ( Calculation[Calculation.index('(')+2] == '+' or Calculation[Calculation.index('(')+2] == '-' )) :
                Calculation = Calculation[:2] + '*' + Calculation[Calculation.index('*') + 1] + Calculation[2:]
                Calculation = Calculation.replace('(','')
                Calculation = Calculation.replace(')','')
                # (A+B)*C
                # ( 의 왼쪽이 없고, )의 오른쪽이 곱셈이라면 분배해야 한다.
            elif(( Calculation[Calculation.index('(')+2] == '+' or Calculation[Calculation.index('(')+2] == '-'  ) and Calculation[Calculation.index('(') - 1] == '*'):
                Calculation = Calculation[:5] + Calculation[Calculation.index('*') - 1] + '*' + Calculation[5:]
                Calculation = Calculation.replace('(','')
                Calculation = Calculation.replace(')','')
                # ( 의 왼쪽이 곱셈이고, 오른쪽이 +라면 곱셈을 분배해야 한다. 
                # A*(B+C)

        # 곱셉하기 #########################################################################################################

        #마지막 덧셈을 위해서 곱셈의 결과는 두 행렬중 하나에 할당한 후 그 행렬을 X*Y 대신 문자열에서 치환한다
        #곱셈이 없어질때까지 반복


        #만약 곱셈에서 불가능한 경우가 나왔다면 덧셈을 건너뛰기 위한 장치로 변수를 만듦
        conti = 1

        while '*' in Calculation:
            #왼쪽 X
            #정리된 식을 확인하기
            if(Calculation[Calculation.index('*') - 1] == 'A'):
                X = A[:]
                if(Calculation.count('A') > 1):
                    change = 'B'
                else:
                    change = 'A'                
                Calculation = Calculation[: Calculation.index('*') -1] + Calculation[Calculation.index('*') :]
                #곱해지는 왼쪽 행렬이 X, 오른쪽 행렬이 Y가 되도록 한다.
            elif(Calculation[Calculation.index('*') - 1] == 'B'):
                X = B[:]
                if( Calculation.count('B') > 1):
                    change = 'C'
                else:
                    change = 'B'                
                Calculation = Calculation[: Calculation.index('*') -1] + Calculation[Calculation.index('*') :]
                #왼쪽의 행렬이 무엇인지 알았으니까 곧바로 식을 지워준다.
            elif(Calculation[Calculation.index('*') - 1] == 'C'):
                X = C[:]
                if( Calculation.count('C') > 1):
                    change = 'A'
                else:
                    change = 'C'                
                Calculation = Calculation[: Calculation.index('*') -1] + Calculation[Calculation.index('*') :]
                #계산후 치환되는 값은 왼쪽의 변수로 한다.

            #오른쪽 Y역시 왼쪽처럼 반복. 그러나 치환을 위한 저장은 하지 않는다.
            if(Calculation[Calculation.index('*') + 1] == 'A'):
                Y = A[:]
                Calculation = Calculation[: Calculation.index('*') + 1] + Calculation[Calculation.index('*') + 2 :]
            elif(Calculation[Calculation.index('*') + 1] == 'B'):
                Y = B[:]
                Calculation = Calculation[: Calculation.index('*') + 1] + Calculation[Calculation.index('*') + 2 :]
            elif(Calculation[Calculation.index('*') + 1] == 'C'):
                Y = C[:]
                Calculation = Calculation[: Calculation.index('*') + 1] + Calculation[Calculation.index('*') + 2 :]
                    
            # Xa = len(A), Ya = len(A[0]), Xb = len(B), Yb = len(B[0]), Xc = len(C), Yc = len(C[0])
            # 곱셈이 불가능한 경우의 수
            if(len(X[0]) != len(Y)):
                print("곱셈을 하려는 두 행렬은 왼쪽행렬의 columns와 오른쪽 행렬의 rows가 일치하지 않습니다")
                conti = 0
                break
                
            #계산값을 저장
            if(change == 'A'):
                A = mul(X,Y)
            elif(change == 'B'):
                B = mul(X,Y)
            elif(change == 'C'):
                C = mul(X,Y)

            #마지막으로 곱하기 기호를 Change의 행렬로 바꿔준다.
            Calculation = Calculation.replace('*',change,1)

        # 빼기 계산하기 #####################################################################################################

        while '-' in Calculation:
            # 왼쪽
            if(Calculation[Calculation.index('-') -1] == 'A'):
                left = A[:]
                MinusChange = 'A' # 계산 후 왼쪽것으로 치환
                Calculation = Calculation[: Calculation.index('-') -1] + Calculation[Calculation.index('-') :]
            elif(Calculation[Calculation.index('-') -1] == 'B'):
                left = B[:]
                MinusChange = 'B'
                Calculation = Calculation[: Calculation.index('-') -1] + Calculation[Calculation.index('-') :]
            elif(Calculation[Calculation.index('-') -1] == 'C'):
                left = C[:]
                MinusChange = 'C'
                Calculation = Calculation[: Calculation.index('-') -1] + Calculation[Calculation.index('-') :]
            # 오른쪽
            if(Calculation[Calculation.index('-') +1] == 'A'):
                right = A[:]
                Calculation = Calculation[: Calculation.index('-') + 1] + Calculation[Calculation.index('-') + 2 :]
            elif(Calculation[Calculation.index('-') +1] == 'B'):
                right = B[:]
                Calculation = Calculation[: Calculation.index('-') + 1] + Calculation[Calculation.index('-') + 2 :]
            elif(Calculation[Calculation.index('-') +1] == 'C'):
                right = C[:]
                Calculation = Calculation[: Calculation.index('-') + 1] + Calculation[Calculation.index('-') + 2 :]
            
            if(len(right) != len(left) and len(right[0]) != len(left[0]) ):
                print("뺄셈을 하려는 두 행렬은 왼쪽행렬의 columns와 오른쪽 행렬의 rows가 일치하지 않습니다")
                conti = 0
                break

            # 계산값을 처리

            if(MinusChange == 'A'):
                A = minus(left,right)
            elif(MinusChange == 'B'):
                B = minus(left,right)
            elif(MinusChange == 'C'):
                C = minus(left,right)

            #마지막에 -를 치환할 행렬로 변환
            Calculation = Calculation.replace('-',MinusChange,1)



        #정리된 식을 확인하기
        #print(Calculation)

        #마지막으로 남은 행렬들의 덧셈 #####################################################################################
        # 단순 세 행렬의 덧셈 
        if conti == 0:
            print("오류가 발생, 다른 연산식을 입력하세요\n")
        #곱셈에서 오류가 발생했을때
        elif Calculation == "A+B+C" or Calculation == "A+C+B" or Calculation == "B+A+C"  or Calculation == "B+C+A" or Calculation == "C+A+B" or Calculation == "C+B+A":
            if (len(B) != len(C)) or (len(B[0]) != len(C[0])) or (len(B) != len(A)) or (len(B[0]) != len(A[0])) or (len(C) != len(A)) or (len(C[0]) != len(A[0])):
               print ("ERROR 세 행렬은 같은 수의 rows, columns을 갖지 않습니다")
            else :          
               Q = plus(plus(A,B),C)
               #함수로 더해진 행렬을 받는다
               for rows in Q :
                    print (rows)

        #입력된 연산이 가능한지 체크한다. 
        # 단순 두 행렬의 덧셈 
        elif Calculation == "A+B" or Calculation == "B+A":
            if (len(A) != len(B)) or (len(A[0]) != len(B[0])):
                print ("ERROR 두 행렬은 같은 수의 rows, columns을 갖지 않습니다")
            else :          
                Q = plus(A,B)
                #함수로 더해진 행렬을 받는다
                for rows in Q :
                    print (rows)
        # Xa = len(A), Ya = len(A[0]), Xb = len(B), Yb = len(B[0]), Xc = len(C), Yc = len(C[0])

        # 단순 두 행렬의 덧셈 
        elif Calculation == "A+C" or Calculation == "C+A":
            if (len(A) != len(C)) or (len(A[0]) != len(C[0])):
                print ("ERROR 두 행렬은 같은 수의 rows, columns을 갖지 않습니다")
            else :          
                Q = plus(A,C)
                #함수로 더해진 행렬을 받는다
                for rows in Q :
                    print (rows)
                    
        # 단순 두 행렬의 덧셈 
        elif Calculation == "B+C" or Calculation == "C+B":
            if (len(B) != len(C)) or (len(B[0]) != len(C[0])):
                print ("ERROR 두 행렬은 같은 수의 rows, columns을 갖지 않습니다")
            else :          
                Q = plus(B,C)
                #함수로 더해진 행렬을 받는다
                for rows in Q :
                    print (rows)

        #덧셈이 없어 마지막에 하나의 행렬만 남았을 경우
        elif Calculation == 'A':
            for rows in A:
                print(rows)
        elif Calculation == 'B':
            for rows in B:
                print(rows)
        elif Calculation == 'C':
            for rows in C:
                print (rows)
