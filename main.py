import streamlit as st
from streamlit.column_config import CheckboxColumn
import random

st.title("計算問題")


#計算の種類を保存
Calculation_types = {"+": False, "-": False, "×": False, "÷": False}

# セッション状態の初期化
if 'disabled_state' not in st.session_state:
    st.session_state.disabled_state = False


#計算の種類を選択するチェックボックス
if st.checkbox('足し算', key="sum", disabled=st.session_state.disabled_state):
    Calculation_types["+"] = True
if st.checkbox('引き算', key="sub", disabled=st.session_state.disabled_state):
    Calculation_types["-"] = True
if st.checkbox('掛け算', key="mul", disabled=st.session_state.disabled_state):
    Calculation_types["X"] = True
if st.checkbox('割り算', key="div", disabled=st.session_state.disabled_state):
    Calculation_types["÷"] = True


#項の数を選択
term = st.selectbox("項の数", list(range(2, 10)), disabled=st.session_state.disabled_state)

#問題数を選択
question_number = st.selectbox("問題数", [5, 10, 15, 20, 30, 50], disabled=st.session_state.disabled_state)

#桁数
digit = st.selectbox("桁数", [1, 2, 3], disabled=st.session_state.disabled_state)



def create_question(Calculation_list, term, digit):
    #問題の作成
        Equation = []
        print(f"項の数{term}")
        print(f"桁数{digit}")

        
        
        #項を作成
        for i in range(term):
            #指定した桁数の乱数を生成
            min_value = 10**(digit-1)
            max_value = 10**digit - 1
            num = random.randint(min_value, max_value)

            #項をリストに追加
            Equation.append(num)

            #計算の種類をランダムに選択
            Calculation = random.choice(Calculation_list)
            Equation.append(Calculation)

        #最後の計算記号を削除
        Equation.pop()
        

        #直接計算できる形に変換
        result_equation = []
        for i in Equation:
            if type(i) == int:
                result_equation.append(str(i))
            if i == "+" or i == "-":
                result_equation.append(i)
            if i == "X":
                result_equation.append("*")
            if i == "÷":
                result_equation.append("/")

        #リストを文字列に変換
        print(result_equation)
        result_equation_str = "".join(result_equation)
        result = eval(result_equation_str)
        print(f"答え{result}")

        #リスト化された式を文字列に変換
        Equation_str = "".join(map(str, Equation))
        print(Equation_str)
        return Equation_str, result



run = st.button("開始")

if run:
    print("開始ボタンが押されました")
    #st.session_state.disabled_state = True


    for t in range(1, question_number+1): #問題数分繰り返す
        st.write(f"問題{t}")

        #計算の種類をリスト化
        Calculation_list = [k for k,v in Calculation_types.items() if v == True]
        
        #問題作成関数呼び出し(計算の種類、項の数、桁数)
        Equation, result = create_question(Calculation_list, term, digit)
        print(Equation)
        st.write(f"## {Equation}")
        st.write(f"# {result}")
        
        




    
