#https://wikidocs.net/26 참조
#https://dojang.io/mod/page/view.php?id=2293 이차원 배열 참조

#RREF로의 변환
def Run(M):
    #맨처음 정렬
    RowsNumberMinusZeroRows = len(M)

    #zero row는 맨 밑으로
    for i in range (0,RowsNumberMinusZeroRows - 1):
        cnt = 0
        #0의 개수 세기
        for j in range (0,len(M[i])):
            if(M[i][j] == 0):
                cnt += 1
        #만약 zero row면 맨 밑으로 보내고 열의 숫자를 하나 줄인다.
        if(cnt == len(M[i]) and i != RowsNumberMinusZeroRows - 1):
            Ch(M, i,RowsNumberMinusZeroRows - 1)
            RowsNumberMinusZeroRows -= 1
        #맨 마지막 줄이 이미 제로 row일 경우를 고려
        elif(cnt == len(M[i]) and i == RowsNumberMinusZeroRows - 1) :
            #만약 zero row면 고려할 column의 개수를 하나 줄인다.
            RowsNumberMinusZeroRows -= 1


                



    for i in range(0, RowsNumberMinusZeroRows - 1):
        Messup(M,i)

    for i in range(0, RowsNumberMinusZeroRows):
        #Pivot을 찾는다
        while True:
            Pivotj = None
            for j in range(i, len(M[i])):
                if(M[i][j] != 0):
                    Pivotj = j
                    break
            if(Pivotj == None):
                #zero row는 맨 밑으로
                for i in range (0,RowsNumberMinusZeroRows - 1):
                    cnt = 0
                    #0의 개수 세기
                    for j in range (0,len(M[i])):
                        if(M[i][j] == 0):
                            cnt += 1
                    #만약 zero row면 맨 밑으로 보내고 열의 숫자를 하나 줄인다.
                    if(cnt == len(M[i]) and i != RowsNumberMinusZeroRows - 1):
                        Ch(M, i,RowsNumberMinusZeroRows - 1)
                        RowsNumberMinusZeroRows -= 1
                    #맨 마지막 줄이 이미 제로 row일 경우를 고려
                    elif(cnt == len(M[i]) and i == RowsNumberMinusZeroRows - 1) :
                        #만약 zero row면 고려할 column의 개수를 하나 줄인다.
                        RowsNumberMinusZeroRows -= 1
            #Pivot을 1로 만든다.
            elif(M[i][Pivotj] != 1 and M[i][Pivotj] != 0):
                mulNum = 1/M[i][Pivotj]

                #마지막 줄의 Pivot이 음수가 될 경우를 고려해야 한다
                if(M[i][Pivotj] < 0):
                    mulNum *= -1
                mul(M, i, mulNum)

                #계산 후 Pivot이 음수면 바꿔준다.
                if(M[i][Pivotj] == -1):
                    mul(M, i, -1)
            else:
                break
                

            #pivot의 row를 더하면 0이 된다.

        #현재 row의 pivot의 밑의 값을 전부 0으로 만든다. 
        for k in range(i+1, RowsNumberMinusZeroRows):
            if(M[k][Pivotj] != 0):
                zeroNum = -M[k][Pivotj]
                MpM(M,i,k,zeroNum)        
        #zero row는 맨 밑으로
        for i in range (0,RowsNumberMinusZeroRows - 1):
            cnt = 0
            #0의 개수 세기
            for j in range (0,len(M[i])):
                if(M[i][j] == 0):
                    cnt += 1
            #만약 zero row면 맨 밑으로 보내고 열의 숫자를 하나 줄인다.
            if(cnt == len(M[i]) and i != RowsNumberMinusZeroRows - 1):
                Ch(M, i,RowsNumberMinusZeroRows - 1)
                RowsNumberMinusZeroRows -= 1
            #맨 마지막 줄이 이미 제로 row일 경우를 고려
            elif(cnt == len(M[i]) and i == RowsNumberMinusZeroRows - 1) :
                #만약 zero row면 고려할 column의 개수를 하나 줄인다.
                RowsNumberMinusZeroRows -= 1
    print("REF가 되었다. \n")
        ############### 여기까지 REF ############ 이 다음으로 RREF 만들기


    ## Pivot을 찾는다. 두번째 row부터.
    # row반복
    for i in range(1, RowsNumberMinusZeroRows):
        while True:
            # Pivot의 column 값 초기화
            RREFpivot = None
            #column 반복
            for j in range(0, len(M[i])):
                if(M[i][j] != 0): # 앞서 pivot을 모두 1로 만들어 놓았다
                    RREFpivot = j; #column찾음 현재 row는 고정된 상태
                    break
            if (RREFpivot == None):
                #zero row는 맨 밑으로
                for i in range (0,RowsNumberMinusZeroRows - 1):
                    cnt = 0
                    #0의 개수 세기
                    for j in range (0,len(M[i])):
                        if(M[i][j] == 0):
                            cnt += 1
                    #만약 zero row면 맨 밑으로 보내고 열의 숫자를 하나 줄인다.
                    if(cnt == len(M[i]) and i != RowsNumberMinusZeroRows - 1):
                        Ch(M, i,RowsNumberMinusZeroRows - 1)
                        RowsNumberMinusZeroRows -= 1
                    #맨 마지막 줄이 이미 제로 row일 경우를 고려
                    elif(cnt == len(M[i]) and i == RowsNumberMinusZeroRows - 1) :
                        #만약 zero row면 고려할 column의 개수를 하나 줄인다.
                        RowsNumberMinusZeroRows -= 1
            else:
                break
            #Pivot값을 찾았을때만 반복문 벗어남.



        ####찾은 pivot의 위를 모두 0으로 만든다.
        for k in range(0, i): # row를 다시 반복
            #pivot과 같은 column이며 그 위의 row element
            if(M[k][RREFpivot] != 0):
                ### pivot이 1이기에 그대로 곱해서 부호만 반대로
                RREFmul = M[k][RREFpivot]
                RREFmul *= -1
                #-1이 된 pivot의 열로 다음 열 제거
                MpM(M ,i ,k ,RREFmul)




################################################### 함수들

# 출력
def PRINT(M):
    
    for i in range(0, len(M)):
        for j in range(0, len(M[i])):
            ######소수점 둘째자리 반올림. 둘째자리까지만 출력
            M[i][j] = round(M[i][j],2)
    for i in M:
        print(i)
    


#행렬 row1 + N행렬 row2 = 행렬 row1     
def MpM(M,i,j,N):
    for k in range(0, len(M[i])):
        M[j][k] += N*M[i][k]
    print("\n")
    for l in M:
        print(l)
    print("R" , j+1 , "+ " , N , "R" , i+1 , "= R" ,j+1)
            

#0인 행렬이 밑으로 가도록 정렬
def Messup(M, i): 
    for j in range(i + 1,len(M)):
        for k in range(i, len(M[0])):
            if(M[i][k] == 0 and M[j][k] != 0):
                Ch(M,i,j)
                break
            


#rows의 곱셈
def mul(M ,Mi ,N):
    for i in range(0,len(M[Mi])):
        if(M[Mi][i] != 0):
            M[Mi][i] = N*M[Mi][i]
            '''
            #오류 수정
            if(M[Mi][i] == 0.9999999999999999):
                M[Mi][i] = 1
            '''
    #변경 후 출력
    print("\n")
    for i in M:
        print(i)
    print("R",Mi+1,"* ",N,"= R",Mi+1)

#rows의 위치 바꾸기
def Ch(M, M1, M2):
    tmp = M[M1]
    M[M1] = M[M2]
    M[M2] = tmp
    #변경 후 출력
    print("\n")
    for i in M:
        print(i)
    print("R",M1+1," <-> R",M2+1)


################################################ 프로그램 본문 시작

while True :
    FileName = input("꺼내올 파일의 이름을 입력하세요.(파일 확장자를 포함한 이름) 프로그램 중지를 원한다면 Q>>>")

    if(FileName == 'Q'):
        break

    f = open(FileName,'r')
    
    #파일의 마지막 까지 계속 반복
    while True:
        A = []
        #첫 번째 줄의 행렬 이름을 분리
        Mname = f.readline()
        #행렬의 이름을 분리해내고 그 다음부터 행렬을 받는다.
        
        while True:
            #row를 저장할 임시 배열
            Q = []
            rows = f.readline()

            #행렬 사이의 엔터 또는 파일 마지막의 엔터
            if rows == '\n' :
                break
            #행렬 사이의 간격
            elif not rows: 
                break
            #EOF시 중단

            Q = list(map(int,rows.split()))
            #배열에 리스트를 저장
            A.append(Q)

        print(FileName,"에서 추출한 행렬인 ",Mname)
        for i in A:
            print(i)
        #변환 시작    
        Run(A)        
        
        print("\n변환된 RREF는 다음과 같다.")
        PRINT(A)
        '''
        for i in A:
            print(i)
        '''
        print("--------------------------------------------")

        if not rows: 
            break
        #EOF시 중단
        
    print("모든 파일의 내용을 읽었습니다.")
    #파일 닫기
    f.close()

    
