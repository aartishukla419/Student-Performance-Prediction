import streamlit as st
import joblib
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Student Performance Prediction", page_icon="🎓", layout="wide"
)

# ==================================================
# LOAD MODEL
# ==================================================

model = joblib.load("student_performance_model.pkl")

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    """
<style>

[data-testid="stAppViewContainer"]{
background: linear-gradient(
135deg,
#0f172a,
#111827,
#1e293b
);
}

section[data-testid="stSidebar"]{
background:#111827;
}

.main-title{
font-size:4rem;
font-weight:900;
background:linear-gradient(
90deg,
#38bdf8,
#818cf8,
#ec4899
);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.glass{
background:rgba(255,255,255,0.08);
backdrop-filter:blur(12px);
padding:25px;
border-radius:20px;
border:1px solid rgba(255,255,255,0.1);
}

.footer{
text-align:center;
color:#d1d5db;
padding-top:20px;
font-size:14px;
}

</style>
""",
    unsafe_allow_html=True,
)

# ==================================================
# HEADER
# ==================================================

st.markdown(
    """
<div class='glass'>

<h1 class='main-title'>
🎓 Student Performance Prediction
</h1>

<h3>
AI Powered Academic Analytics Dashboard
</h3>

<p>
Predict student performance using machine learning-based academic analytics.
</p>

</div>
""",
    unsafe_allow_html=True,
)

st.write("")

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.header("📋 Student Information")

study_hours = st.sidebar.slider(
    "Weekly Self Study Hours", min_value=0, max_value=50, value=10
)

attendance = st.sidebar.slider(
    "Attendance Percentage", min_value=0, max_value=100, value=75
)

participation = st.sidebar.slider(
    "Class Participation", min_value=0, max_value=100, value=50
)

grade = st.sidebar.selectbox("Grade", ["A", "B", "C", "D", "F"])

# ==================================================
# GRADE ENCODING
# ==================================================

grade_mapping = {"A": 0, "B": 1, "C": 2, "D": 3, "F": 4}

grade_encoded = grade_mapping[grade]

# ==================================================
# KPI CARDS
# ==================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📚 Study Hours", study_hours)

with col2:
    st.metric("📅 Attendance", f"{attendance}%")

with col3:
    st.metric("🙋 Participation", participation)

with col4:
    st.metric("🏆 Grade", grade)

st.divider()

# ==================================================
# PREDICT BUTTON
# ==================================================

if st.button("🚀 Predict Total Score", use_container_width=True):
    input_df = pd.DataFrame(
        {
            "weekly_self_study_hours": [study_hours],
            "attendance_percentage": [attendance],
            "class_participation": [participation],
            "grade": [grade_encoded],
        }
    )

    prediction = model.predict(input_df)[0]

    # ==============================================
    # RESULT CARD
    # ==============================================

    st.success(f"Predicted Total Score : {prediction:.2f}")

    # ==============================================
    # GAUGE CHART
    # ==============================================

    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=prediction,
            title={"text": "Predicted Score"},
            gauge={"axis": {"range": [0, 100]}},
        )
    )

    st.plotly_chart(gauge, use_container_width=True)

    # ==============================================
    # PROFILE CHART
    # ==============================================

    chart_df = pd.DataFrame(
        {
            "Feature": ["Study Hours", "Attendance", "Participation"],
            "Value": [study_hours, attendance, participation],
        }
    )

    fig = px.bar(chart_df, x="Feature", y="Value", title="Student Academic Profile")

    st.plotly_chart(fig, use_container_width=True)

    # ==============================================
    # PROGRESS BAR
    # ==============================================

    progress_score = max(0, min(int(prediction), 100))

    st.progress(progress_score)

    # ==============================================
    # PERFORMANCE CATEGORY
    # ==============================================

    if prediction >= 85:
        st.balloons()

        st.success("🏆 Excellent Performance")

    elif prediction >= 70:
        st.info("🎯 Good Performance")

    elif prediction >= 50:
        st.warning("📘 Average Performance")

    else:
        st.error("⚠ Needs Improvement")

    # ==============================================
    # INSIGHT SECTION
    # ==============================================

    st.subheader("📊 Performance Insight")

    st.write(
        f"""
        Based on the provided academic indicators,
        the student is expected to achieve a total score
        of **{prediction:.2f}**.

        The prediction is influenced by:

        • Weekly Self Study Hours

        • Attendance Percentage

        • Classroom Participation

        • Academic Grade
        """
    )

# ==================================================
# FOOTER
# ==================================================

st.divider()

st.markdown(
    """
    <div class="footer">
    Developed using Machine Learning, Scikit-Learn, Plotly and Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)
