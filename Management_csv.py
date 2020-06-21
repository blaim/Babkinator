# 2019029029 황근민
# csv 파일 관리 프로그램
import pandas as pd


class Management_csv():

    def __init__(self):
        self.foodcode_df = pd
        self.restarurant_df = pd
        self.food_code = ""
        self.food_name = ""
        self.code_list = []
        self.rs_name = ""
        self.rs_address = ""
        self.rs_phone = ""
        self.rs_menu = ""
        self.rs_payment = ""
        self.rs_web = ""
        self.rs_lat = 0
        self.rs_long = 0

    # 식당 정보 csv 파일 읽기
    def open_restaurnat_csv(self):
        self.restarurant_df = pd.read_csv('./res_data.csv', encoding='utf-8-sig')

    # 음식 코드 csv 파일 읽기
    def open_foodcode_csv(self):
        self.foodcode_df = pd.read_csv('./food_code.csv', encoding='utf-8-sig')

    # 질문을 출력하고 답변을 누적하는 함수
    def babkinator(self):
        q0 = ["고기(해산물포함)는 어떻습니까?"]
        q1 = ["익혀 먹는 음식은 어떻습니까?", "매운 음식은 어떻습니까?"]
        q2 = ["매운 음식은 어떻습니까?", "해산물이 들어가는 음식은 어떻습니까?", "면이 들어가는 음식은 어떻습니까?"]
        q3 = ["해산물이 들어가는 음식은 어떻습니까?", "밥이 들어가거나 밥과 함께 먹는 음식은 어떻습니까?", "차가운 음식은 어떻습니까?"]
        q4 = ["탕 또는 찌개 또는 전골은 어떻습니까?", "닭이 들어가는 음식은 어떻습니까?"]
        q5 = ["찜요리는 어떻습니까?", "돼지고기가 들어가는 음식 어떻습니까?", "튀겨 먹는 음식은 어떻습니까?"]
        q6 = ["볶음요리는 어떻습니까?", "구이 어떻습니까?"]
        q7 = ["전골 또는 찌개는 어떻습니까?", "튀겨 먹는 음식은 어떻습니까?", "탕 또는 전골는 어떻습니까?"]
        q8 = ["국밥 또는 탕은 어떻습니까?"]

        # 0단계 질문
        if len(self.food_code) == 0:
            # 고기입니까?
            self.food_code = input(q0[0])

        while self.food_code != "":

            # 1단계 질문
            if len(self.food_code) == 1:

                # 고기o
                if self.food_code == "y":
                    # 익힌 음식입니까?
                    self.food_code += input(q1[0])

                # 고기x
                elif self.food_code == "n":
                    # 매운 음식입니까?
                    self.food_code += input(q1[1])

            # 2단계 질문
            elif len(self.food_code) == 2:

                # 고기o, 익힘o
                if self.food_code == "yy":
                    # 매운 음식입니까?
                    self.food_code += input(q2[0])

                # 고기o, 익힘x
                elif self.food_code == "yn":
                    # 해산물이 들어가는 음식입니까?
                    self.food_code += input(q2[1])

                # 고기x, 매움o 또는 고기x, 매움x
                elif (self.food_code == "ny") or (self.food_code == "nn"):
                    # 면이 들어가는 음식입니까?
                    self.food_code += input(q2[2])

            # 3단계 질문
            elif len(self.food_code) == 3:

                # 고기o, 익힘o, 매움o 또는 고기o, 익힘o, 매움x
                if (self.food_code == "yyy") or (self.food_code == "yyn"):
                    # 해산물이 들어가는 음식입니까?
                    self.food_code += input(q3[0])

                # 고기o, 익힘x, 해산물o 또는 고기x, 매움o, 면x 또는 고기x, 매움x, 면x
                elif (self.food_code == "yny") or (self.food_code == "nyn") or (self.food_code == "nnn"):
                    # 쌀이 들어가거나 밥과 함께 먹는 음식입니까?
                    self.food_code += input(q3[1])

                # 고기o, 익힘x, 해산물x
                elif self.food_code == "ynn":
                    return self.food_code

                # 고기x, 매움o, 면o 또는 고기x, 매움x, 면o
                elif (self.food_code == "nyy") or (self.food_code == "nny"):
                    self.food_code += input(q3[2])
            # 4단계 질문
            elif len(self.food_code) == 4:

                # 고기o, 익힘o, 매움o, 해산물o 또는 고기o, 익힘o, 매움x, 해산물o
                if (self.food_code == "yyyy") or (self.food_code == "yyny"):
                    self.food_code += input(q4[0])

                # 고기o, 매움x, 해산물o, 밥o 또는 고기o, 매움x, 해산물o, 밥x
                # 고기x, 매움o, 면x, 쌀o 또는 고기x, 매움o, 면x, 쌀x 또는
                # 고기x, 매움x, 면x, 쌀o 또는 고기x, 매움x, 면x, 쌀x 또는
                # 고기x, 매움o, 면o, 차가움o 또는  고기x, 매움o, 면o, 차가움x
                # 고기x, 매움x, 면o, 차가움o 또는 고기x, 매움x, 면o, 차가움x
                elif (self.food_code == "ynyy") or (self.food_code == "ynyn") or \
                     (self.food_code == "nyny") or (self.food_code == "nynn") or \
                     (self.food_code == "nnny") or (self.food_code == "nnnn") or \
                     (self.food_code == "nnyy") or (self.food_code == "nnyn"):
                    return self.food_code

                # 고기o, 익힘o, 매움o, 해산물x 또는 고기o, 익힘o, 매움x, 해산물x
                elif (self.food_code == "yyyn") or (self.food_code == "yynn"):
                    # 닭이 들어가는 음식입니까?
                    self.food_code += input(q4[1])

            # 5단계 질문
            elif len(self.food_code) == 5:

                """
                    고기o, 익힘o, 매움o, 해산물o, 탕,찌개,전골o 또는 고기o, 익힘o, 매움x, 해산물o, 탕,찌개,전골o
                    고기o, 익힘o, 매움o, 해산물x, 닭o
                """
                if (self.food_code == "yyyyy") or (self.food_code == "yynyy") or \
                   (self.food_code == "yyyny"):
                    return self.food_code

                # 고기o, 익힘o, 매움o, 해산물o, 탕,찌개,전골x 또는 고기o, 익힘o, 매움x, 해산물o, 탕,찌개,전골x
                elif self.food_code == "yynnn" or self.food_code == "yynyn":
                    # 찜요리는 어떻습니까?
                    self.food_code += input(q5[0])

                # 고기o, 익힘o, 매움o, 해산물x, 닭x 또는 고기o, 익힘o, 매움x, 해산물x, 닭x
                elif(food_code == "yyynn") or (food_code == "yynnn") :
                    self.food_code += input(q5[1])

                # 고기o, 익힘o, 매움x, 해산물x, 닭o
                elif food_code == "yynny":
                    self.food_code += input(q5[2])

            # 6단계 질문
            elif len(self.food_code) == 6:

                """
                    고기o, 익힘o, 매움o, 해산물o, 탕,찌개,전골x, 찜o 또는 고기o, 익힘o, 매움x, 해산물o, 탕,찌개,전골x, 찜o 또는
                    고기o, 익힘o, 매움o, 해산물x, 닭x, 돼지x 또는
                    고기o, 익힘o, 매움x, 해산물x, 닭o, 튀김o 또는 고기o, 익힘o, 매움x, 해산물x, 닭o, 튀김x
                """
                if (self.food_code == "yyyyny") or (self.food_code == "yynyny") or \
                   (self.food_code == "yyynnn") or \
                   (self.food_code == "yynnyy") or (self.food_code == "yynnyn"):
                    return self.food_code

                # 고기o, 익힘o, 매움o, 해산물o, 탕,찌개,전골x, 찜x 또는 고기o, 익힘o, 매움o, 해산물x, 닭x, 돼지o
                elif (self.food_code == "yynnnn") or (self.food_code == "yyynny"):
                    self.food_code += input(q6[0])

                # 고기o, 익힘o, 매움x, 해산물o, 탕,찌개,전골x, 찜x 또는
                # 고기o, 익힘o, 매움x, 해산물x, 닭x, 돼지고기o, 또는 고기o, 익힘o, 매움x, 해산물x, 닭x, 돼지고기x
                elif (self.food_code == "yynynn") or (self.food_code == "yynnny") or (self.food_code == "yynnnn"):
                    self.food_code += input(q6[1])

            # 7단계
            elif len(self.food_code) == 7:
                """ 
                    고기o, 익힘o, 매움o, 해산물o, 탕, 찌개, 전골x, 찜x, 볶음o 또는 고기o, 익힘o, 매움o, 해산물o, 탕, 찌개, 전골x, 찜x, 볶음x 또는
                    고기o, 익힘o, 매움o, 해산물x, 닭x, 돼지o, 볶음o 또는
                    고기o, 익힘o, 매움x, 해산물o, 탕, 찌개, 전골x, 찜x, 구이o 또는 고기o, 익힘o, 매움x, 해산물o, 탕, 찌개, 전골x, 찜x, 구이x 또는
                    고기o, 익힘o, 매움x, 해산물x, 닭x, 돼지고기o, 구이o 또는 고기o, 익힘o, 매움x, 해산물x, 닭x, 돼지고기x, 구이o
                """
                if (self.food_code == "yyyynny") or (self.food_code == "yyyynnn") or\
                   (self.food_code == "yyynnyy") or\
                   (self.food_code == "yynynny") or (self.food_code == "yynynnn") or\
                   (self.food_code == "yynnnyy") or (self.food_code == "yynnnny"):
                    return self.food_code

                # 고기o, 익힘o, 매움o, 해산물x, 닭x, 돼지o, 볶음x
                elif self.food_code == "yyynnyn":
                    self.food_code += input(q7[0])

                # 고기o, 익힘o, 매움x, 해산물x, 닭x, 돼지고기o, 구이x
                elif self.food_code == "yynnnyn":
                    self.food_code += input(q7[1])

                # 고기o, 익힘o, 매움x, 해산물x, 닭x, 돼지고기x, 구이x
                elif self.food_code == "yynnnnn":
                    self.food_code += input(q7[2])

            # 8단계
            elif len(self.food_code) == 8:

                """
                    고기o, 익힘o, 매움o, 해산물x, 닭x, 돼지o, 볶음x, 전골,찌개o 또는 고기o, 익힘o, 매움o, 해산물x, 닭x, 돼지o, 볶음x, 전골,찌개x 또는
                    고기o, 익힘o, 매움x, 해산물x, 닭x, 돼지고기o, 구이x, 튀김o 또는
                    고기o, 익힘o, 매움x, 해산물x, 닭x, 돼지고기x, 구이x, 탕,전골o 또는 고기o, 익힘o, 매움x, 해산물x, 닭x, 돼지고기x, 구이x, 탕,전골x
                """
                if (self.food_code == "yyynnyny") or (self.food_code == "yyynnynn") or\
                   (self.food_code == "yynnnyny") or\
                   (self.food_code == "yynnnnny") or (food_code == "yynnnnnn"):
                    return self.food_code

                # 고기o, 익힘o, 매움x, 해산물x, 닭x, 돼지고기o, 구이x, 튀김x 또는 고기o, 익힘o, 매움x, 해산물x, 닭x, 돼지고기x, 구이x, 튀김x
                elif self.food_code == "yynnnynn":
                    self.food_code += input(q8[0])

            # 9단계
            elif len(self.food_code) == 9:
                # 고기o, 익힘o, 매움x, 해산물x, 닭x, 돼지고기o, 구이x, 튀김x, 탕, 전골o 또는 고기o, 익힘o, 매움x, 해산물x, 닭x, 돼지고기o, 구이x, 튀김x, 탕, 전골o
                if (self.food_code == "yynnnynny") or (self.food_code == "yynnnynnn"):
                    return self.food_code

    # 음식 코드 csv 파일에서 메뉴에 대한 코드를 수정하는 함수
    def modfiy_foodcode(self, code_list):

        self.foodcode_df.loc[code_list[0], '메뉴'] = code_list[1]
        self.foodcode_df.loc[code_list[0], '코드'] = code_list[2]

        self.foodcode_df.to_csv('food_code.csv',  encoding='utf-8-sig', mode='w', index=False)

    # 음식 코드 csv 파일에 메뉴와 코드를 추가하는 함수
    def add_foodcode(self, food_name, code):
        index = len(self.foodcode_df.index) + 1

        self.foodcode_df.loc[index, '메뉴'] = food_name
        self.foodcode_df.loc[index, '코드'] = code

        self.foodcode_df.to_csv('food_code.csv', encoding='utf-8-sig', mode='w', index=False)

    # 수정할 음식을 검색하는 함수
    def search_foodcode(self):
        self.food_name = input("수정할 음식을 입력하세요:")

        for i in range(0, len(self.foodcode_df.index), 1):
            if self.foodcode_df.loc[i, '메뉴'] == self.food_name:
                self.code_list = [i, self.foodcode_df.loc[i, '메뉴'], self.foodcode_df.loc[i, '코드']]
                print(self.code_list)
                break

        return self.code_list

    # 식당 정보 수정하는 함수
    def modify_res(self, res_menu):

        if res_menu == 6:
            self.restarurant_df.to_csv('res_data.csv',  encoding='utf-8-sig', mode='w', index=False)

        else:
            self.rs_name = input("정보를 수정할 식당의 이름을 입력하세요:")
            self.rs_address = input("정보를 수정할 식당의 주소를 입력하세요:")

            for i in range(0, len(self.restarurant_df.index), 1):
                if (self.restarurant_df.loc[i, '업소명'] == self.rs_name) and (self.restarurant_df.loc[i, '주소']):

                    # 주소 변경
                    if res_menu == 1:
                        self.rs_address = input("새로운 주소를 입력하세요:")
                        self.rs_lat = input("새로운 위도를 입력하세요:")
                        self.rs_long = input("새로운 경도를 입력하세요:")
                        self.restarurant_df.loc[i, '주소'] = self.rs_address
                        self.restarurant_df.loc[i, '위도'] = self.rs_lat
                        self.restarurant_df.loc[i, '경도'] = self.rs_long

                    # 전화번호 변경
                    elif res_menu == 2:
                        self.rs_phone = input("새로운 전화번호를 입력하세요:")
                        self.restarurant_df.loc[i, '전화번호'] = self.rs_phone

                    # 웹페이지 변경
                    elif res_menu == 3:
                        self.rs_web = input("새로운 웹페이지를 입력하세요:")
                        self.restarurant_df.loc[i, '웹페이지'] = self.rs_web

                    # 가격대 변경
                    elif res_menu == 4:
                        self.rs_payment = input("새로운 가격대를 입력하세요:")
                        self.restarurant_df.loc[i, '웹페이지'] = self.rs_payment

                    # 메뉴 변경
                    elif res_menu == 5:
                        self.rs_menu = input("새로운 메뉴를 입력하세요:")
                        self.restarurant_df.loc[i, '메뉴'] = self.rs_menu

    # 식당 추가하는 함수
    def add_res(self):

        index = len(self.restarurant_df.index) + 1

        self.restarurant_df.loc[index, '업종명'] = "일반음식점"
        self.restarurant_df.loc[index, '업소명'] = input("새로 추가할 식당 이름을 입력하세요:")
        self.restarurant_df.loc[index, '주소'] = input("새로 추가할 식당의 주소를 입력하세요:")
        self.restarurant_df.loc[index, '전화번호'] = input("새로 추가할 식당의 전화번호를 입력하세요:")
        self.restarurant_df.loc[index, '위도'] = input("새로 추가할 식당의 위도를 입력하세요:")
        self.restarurant_df.loc[index, '경도'] = input("새로 추가할 식당의 경도를 입력하세요:")
        self.restarurant_df.loc[index, '웹피이지'] = input("새로 추가할 식당의 웹페이지를 입력하세요:")
        self.restarurant_df.loc[index, '가격대'] = input("새로 추가할 식당의 가격대를 입력하세요:")
        self.restarurant_df.loc[index, '메뉴'] = input("새로 추가할 식당의 메뉴를 입력하세요:")

        self.restarurant_df.to_csv('res_data.csv', encoding='utf-8-sig', mode='w', index=False)


def print_menu():
    print("1. 식당 csv 파일 관리\n")
    print("2. 음식 code csv 파일 관리\n")
    print("0. 종료\n")
    menu = int(input("메뉴를 선택하세요:"))
    return menu


def small_menu():
    print("1. 정보 수정\n")
    print("2. 정보 추가\n")
    print("0. 종료\n")
    menu = int(input("메뉴를 선택하세요:"))
    return menu


def modify_res_menu():
    print("1. 주소 변경\n")
    print("2. 전화번호 변경\n")
    print("3. 웹페이지 변경\n")
    print("4. 가격대 변경\n")
    print("5. 메뉴 변경\n")
    print("6. 수정 정보 저장\n")
    print("0. 종료\n")
    menu = int(input("메뉴를 선택하세요:"))
    return menu


Manage_csv = Management_csv()
code_list = []

# 메뉴 출력
Menu = print_menu()

while Menu != 0:
    code = ""

    # 식당 csv 파일 관리
    if Menu == 1:
        Manage_csv.open_restaurnat_csv()

        Small_menu = small_menu()

        while Small_menu != 0:

            if Small_menu == 1:
                modify_menu = modify_res_menu()

                while modify_menu != 0:
                    Manage_csv.modify_res(modify_menu)
                    modify_menu = modify_res_menu()

                Small_menu = small_menu()

            elif Small_menu == 2:
                Manage_csv.add_res()

                Small_menu = small_menu()

        Menu = print_menu()

    # 음식 code csv 파일 관리
    elif Menu == 2:
        Manage_csv.open_foodcode_csv()

        Small_menu = small_menu()

        while Small_menu != 0:
            if Small_menu == 1:
                # 수정할 음식 메뉴 검색
                code_list = Manage_csv.search_foodcode()

                # 밥키네이터 통해서 code 입력
                code_list[2] = Manage_csv.babkinator()

                # 수정할 음식과 토드 확인
                print(code_list)

                # 수정한 음식 메뉴와 해당 코드 csv 파일에 저장
                Manage_csv.modfiy_foodcode(code_list)

                Small_menu = small_menu()

            elif Small_menu == 2:

                # 추가할 음식 입력
                Food_Name = input("추가할 음식을 입력하세요:")

                # 밥키네이터 통해서 code 입력
                Code = Manage_csv.babkinator()

                # 추가할 음식과 코드 확인
                print(Food_Name, Code)

                # 음식메뉴와 해당 코드 csv 파일에 저장
                Manage_csv.add_foodcode(Food_Name, Code)

                Small_menu = small_menu()

        Menu = print_menu()


