import streamlit as st
import math

st.set_page_config(
    page_title="Goal Grade Calculation", 
    )

t1 = st.number_input('Input your Test 1 grade', format='%g', step=0.1)

t2 = st.number_input('Input your Test 2 grade', format='%g', step=0.1)

t3 = st.number_input('Input your Test 3 grade', format='%g', step=0.1)

t4 = st.number_input('Input your Test 4 grade', format='%g', step=0.1)

q = st.number_input('Input your Quizzes total', format='%g', step=0.1)

cp = st.number_input('Input your Class Performance grade', format='%g', step=0.1)

goal_letter = st.selectbox(
    'Choose your GOAL course grade',
    ('A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D'))

goal_number = {'A': 92.5,
               'A-': 89.5,
               'B+': 86.5,
               'B': 82.5,
               'B-': 79.5,
               'C+': 76.5,
               'C': 72.5,
               'C-': 69.5,
               'D': 59.5}

goal = goal_number[goal_letter]

exam_1 = (goal - 0.1*cp - 0.15*q - 0.15*t1 - 0.15*t2 - 0.15*t3 - 0.15*t4) / 0.15

exam_1 = math.ceil(exam_1)

test_sum_drop_lowest = t1 + t2 + t3 + t4 - min(t1, t2, t3, t4)

exam_2 = (goal - 0.1*cp - 0.15*q - 0.15*test_sum_drop_lowest) / 0.3

exam_2 = math.ceil(exam_2)

exam = min(exam_1, exam_2)

if exam > 100:
    st.error(f'The course grade {goal_letter} is unattainable. Please select a lower GOAL course grade.')
elif exam < 0:
    st.warning(f'You would have a course grade of {goal_letter} even if you did not take the final exam.')
else:
    st.info(f'You need to make {exam} on the final exam in order to earn {goal_letter} for the course.')
