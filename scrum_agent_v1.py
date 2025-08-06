import streamlit as st
import google.generativeai as genai
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
import re
import os
from dataclasses import dataclass
from typing import List, Dict, Optional
import time

# Configure page
st.set_page_config(
    page_title="AI Scrum Master Agent",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #667eea;
    }
    
    .task-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid #28a745;
    }
    
    .impediment-card {
        background: #fff3cd;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid #ffc107;
    }
    
    .risk-card {
        background: #f8d7da;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid #dc3545;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

@dataclass
class SprintData:
    sprint_number: int
    start_date: datetime
    end_date: datetime
    total_story_points: int
    completed_story_points: int
    team_members: List[str]
    impediments: List[str]
    risks: List[str]

class ScrumMasterAgent:
    def __init__(self):
        api_key = os.getenv('GEMINI_API_KEY')
        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
            self.api_configured = True
        else:
            self.model = None
            self.api_configured = False
    
    def generate_daily_standup_questions(self, team_member: str, previous_work: str) -> str:
        if not self.api_configured:
            return "❌ Gemini API key not found. Please set the GEMINI_API_KEY environment variable."
        
        prompt = f"""
        As an AI Scrum Master, generate personalized daily standup questions for {team_member}.
        
        Previous work context: {previous_work}
        
        Generate 3-4 thoughtful questions that will help uncover:
        1. Progress updates
        2. Potential blockers
        3. Plans for today
        4. Any support needed
        
        Make the questions conversational and team-member specific.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating questions: {str(e)}"
    
    def analyze_sprint_health(self, sprint_data: SprintData) -> str:
        if not self.api_configured:
            return "❌ Gemini API key not found. Please set the GEMINI_API_KEY environment variable."
        
        completion_rate = (sprint_data.completed_story_points / sprint_data.total_story_points) * 100
        days_remaining = (sprint_data.end_date - datetime.now()).days
        
        prompt = f"""
        As an AI Scrum Master, analyze the current sprint health:
        
        Sprint {sprint_data.sprint_number} Details:
        - Completion Rate: {completion_rate:.1f}%
        - Days Remaining: {days_remaining}
        - Total Story Points: {sprint_data.total_story_points}
        - Completed Story Points: {sprint_data.completed_story_points}
        - Team Size: {len(sprint_data.team_members)}
        - Active Impediments: {len(sprint_data.impediments)}
        - Identified Risks: {len(sprint_data.risks)}
        
        Provide:
        1. Sprint health assessment (Red/Yellow/Green)
        2. Key concerns and recommendations
        3. Actions for the Scrum Master to take
        4. Team motivation suggestions
        
        Be concise but actionable.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error analyzing sprint: {str(e)}"
    
    def generate_retrospective_insights(self, feedback_data: List[str]) -> str:
        if not self.api_configured:
            return "❌ Gemini API key not found. Please set the GEMINI_API_KEY environment variable."
        
        prompt = f"""
        As an AI Scrum Master, analyze this retrospective feedback and generate insights:
        
        Team Feedback:
        {chr(10).join([f"- {feedback}" for feedback in feedback_data])}
        
        Provide:
        1. Key themes and patterns
        2. Top 3 improvement opportunities
        3. Specific action items with owners
        4. Team strengths to celebrate
        5. Suggested retrospective activities for next time
        
        Focus on actionable insights that drive continuous improvement.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating insights: {str(e)}"
    
    def suggest_impediment_resolution(self, impediment: str, context: str) -> str:
        if not self.api_configured:
            return "❌ Gemini API key not found. Please set the GEMINI_API_KEY environment variable."
        
        prompt = f"""
        As an AI Scrum Master, suggest resolution strategies for this impediment:
        
        Impediment: {impediment}
        Context: {context}
        
        Provide:
        1. Root cause analysis
        2. 2-3 specific resolution strategies
        3. Who should be involved in resolution
        4. Timeline for resolution
        5. How to prevent similar issues
        
        Be practical and consider typical organizational constraints.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating suggestions: {str(e)}"

    def generate_scrum_master_recommendations(self, context: str) -> str:
        if not self.api_configured:
            return "❌ Gemini API key not found. Please set the GEMINI_API_KEY environment variable."
        
        prompt = f"""
        As an AI Scrum Master, analyze the following data and provide recommendations:

        {context}

        Based on the provided data, please provide recommendations on:
        1. What to focus on in the next daily standup.
        2. What to discuss with the product owner.
        3. What to bring up in the next sprint planning.
        4. Any potential risks to the sprint.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating recommendations: {str(e)}"

def initialize_session_state():
    if 'sprint_data' not in st.session_state:
        st.session_state.sprint_data = SprintData(
            sprint_number=1,
            start_date=datetime.now() - timedelta(days=7),
            end_date=datetime.now() + timedelta(days=7),
            total_story_points=50,
            completed_story_points=30,
            team_members=["Alice", "Bob", "Charlie", "Diana", "Eve"],
            impediments=["API dependency blocking feature", "Test environment unavailable"],
            risks=["Key developer on vacation next week", "Unclear requirements for user story #23"]
        )
    
    if 'daily_updates' not in st.session_state:
        st.session_state.daily_updates = []

    if 'team_updates' not in st.session_state:
        st.session_state.team_updates = pd.DataFrame({
            "Team Member": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
            "Update": ["Working on feature #123", "Fixing bug #456", "Refactoring the auth module", "Blocked by API dependency", "Writing documentation for new endpoint"]
        })

    if 'current_implementations' not in st.session_state:
        st.session_state.current_implementations = pd.DataFrame({
            "Task ID": ["FEAT-123", "BUG-456", "REFC-789", "DOC-101"],
            "Description": ["Implement new user profile page", "Fix login button alignment", "Refactor database connection logic", "Document the new API endpoints"],
            "Status": ["In Progress", "In Progress", "In Review", "Done"]
        })

    if 'product_backlog' not in st.session_state:
        st.session_state.product_backlog = pd.DataFrame({
            "Story ID": ["ST-101", "ST-102", "ST-103", "ST-104"],
            "Description": ["As a user, I want to be able to reset my password", "As an admin, I want to be able to view all users", "As a user, I want to be able to upload a profile picture", "As a user, I want to receive an email notification when my order is shipped"],
            "Priority": ["High", "Medium", "Low", "High"],
            "Story Points": [5, 3, 2, 5]
        })
    
    if 'retrospective_feedback' not in st.session_state:
        st.session_state.retrospective_feedback = []

def create_burndown_chart(sprint_data: SprintData):
    # Sample burndown data
    days = list(range(15))  # 2-week sprint
    ideal_burndown = [sprint_data.total_story_points - (i * sprint_data.total_story_points / 14) for i in days]
    actual_burndown = [50, 48, 45, 42, 38, 35, 32, 30, 30, 28, 25, 22, 20, 18, 15]  # Sample data
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=days, 
        y=ideal_burndown,
        mode='lines',
        name='Ideal Burndown',
        line=dict(color='#28a745', width=3, dash='dash')
    ))
    
    fig.add_trace(go.Scatter(
        x=days[:len(actual_burndown)], 
        y=actual_burndown,
        mode='lines+markers',
        name='Actual Burndown',
        line=dict(color='#dc3545', width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title="Sprint Burndown Chart",
        xaxis_title="Days",
        yaxis_title="Story Points Remaining",
        template="plotly_white",
        height=400
    )
    
    return fig

def create_velocity_chart():
    # Sample velocity data
    sprints = ['Sprint 1', 'Sprint 2', 'Sprint 3', 'Sprint 4', 'Sprint 5']
    planned = [45, 50, 48, 52, 50]
    completed = [42, 47, 45, 50, 48]
    
    fig = go.Figure(data=[
        go.Bar(name='Planned', x=sprints, y=planned, marker_color='#667eea'),
        go.Bar(name='Completed', x=sprints, y=completed, marker_color='#28a745')
    ])
    
    fig.update_layout(
        title="Team Velocity Trend",
        xaxis_title="Sprint",
        yaxis_title="Story Points",
        template="plotly_white",
        height=400,
        barmode='group'
    )
    
    return fig

def create_team_workload_chart(team_members: List[str]):
    # Sample workload data
    workload = [8, 6, 9, 7, 5]  # Hours per day
    colors = ['#ff6b6b' if w > 8 else '#4ecdc4' if w < 6 else '#45b7d1' for w in workload]
    
    fig = go.Figure(data=[
        go.Bar(x=team_members, y=workload, marker_color=colors)
    ])
    
    fig.update_layout(
        title="Team Workload Distribution",
        xaxis_title="Team Members",
        yaxis_title="Hours/Day",
        template="plotly_white",
        height=300
    )
    
    return fig

def main():
    initialize_session_state()
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🚀 AI Scrum Master Agent</h1>
        <p>Automating Scrum processes with Intelligent Insights</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Check if API key is configured
        agent = ScrumMasterAgent()
        if agent.api_configured:
            st.success("✅ Gemini API Key loaded from environment")
        else:
            st.error("❌ GEMINI_API_KEY environment variable not found")
            st.info("💡 Set your API key: `export GEMINI_API_KEY=your_key_here`")
        
        st.header("📋 Sprint Settings")
        sprint_num = st.number_input("Sprint Number", value=1, min_value=1)
        total_points = st.number_input("Total Story Points", value=50, min_value=1)
        completed_points = st.slider("Completed Story Points", 0, total_points, 30)
        
        # Update sprint data
        st.session_state.sprint_data.sprint_number = sprint_num
        st.session_state.sprint_data.total_story_points = total_points
        st.session_state.sprint_data.completed_story_points = completed_points
    
    # Main dashboard
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        completion_rate = (completed_points / total_points) * 100
        st.metric("Sprint Progress", f"{completion_rate:.1f}%", f"{completed_points}/{total_points} SP")
    
    with col2:
        days_remaining = (st.session_state.sprint_data.end_date - datetime.now()).days
        st.metric("Days Remaining", days_remaining, "days")
    
    with col3:
        st.metric("Team Size", len(st.session_state.sprint_data.team_members), "members")
    
    with col4:
        st.metric("Active Impediments", len(st.session_state.sprint_data.impediments), "blockers")
    
    # Charts section
    st.header("📊 Sprint Analytics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(create_burndown_chart(st.session_state.sprint_data), use_container_width=True)
    
    with col2:
        st.plotly_chart(create_velocity_chart(), use_container_width=True)
    
    st.plotly_chart(create_team_workload_chart(st.session_state.sprint_data.team_members), use_container_width=True)
    
    # Tabs for different features
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🤖 AI Sprint Analysis", "📝 Daily Standup", "🔄 Retrospective", "⚠️ Impediments", "📈 Reports", "📊 Tracker"])
    
    with tab1:
        st.subheader("AI-Powered Sprint Health Analysis")
        
        if st.button("🔍 Analyze Current Sprint", type="primary"):
            with st.spinner("Analyzing sprint health..."):
                analysis = agent.analyze_sprint_health(st.session_state.sprint_data)
                st.markdown("### Analysis Results")
                st.write(analysis)
    
    with tab2:
        st.subheader("Daily Standup Assistant")
        
        col1, col2 = st.columns(2)
        
        with col1:
            selected_member = st.selectbox("Select Team Member", st.session_state.sprint_data.team_members)
            previous_work = st.selectbox("Previous Work Context", ["Finished feature X", "Working on bug Y", "Starting new task Z"])
            
            if st.button("Generate Standup Questions"):
                with st.spinner("Generating personalized questions..."):
                    questions = agent.generate_daily_standup_questions(selected_member, previous_work)
                    st.markdown("### Suggested Questions")
                    st.write(questions)
        
        with col2:
            st.markdown("### Today's Updates")
            new_update = st.selectbox("Add daily update", ["Making good progress", "Blocked by an issue", "Need help with a task"])
            if st.button("Add Update"):
                if new_update:
                    st.session_state.daily_updates.append({
                        'timestamp': datetime.now(),
                        'member': selected_member,
                        'update': new_update
                    })
                    st.success("Update added!")
            
            for update in st.session_state.daily_updates[-5:]:  # Show last 5 updates
                st.markdown(f"""
                <div class="task-card">
                    <strong>{update['member']}</strong> - {update['timestamp'].strftime('%H:%M')}
                    <br>{update['update']}
                </div>
                """, unsafe_allow_html=True)
    
    with tab3:
        st.subheader("Retrospective Insights")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Add Feedback")
            feedback_text = st.selectbox("Team Feedback", ["The daily standups are effective", "We need to improve our code review process", "The sprint planning was accurate"])
            if st.button("Add Feedback"):
                if feedback_text:
                    st.session_state.retrospective_feedback.append(feedback_text)
                    st.success("Feedback added!")
            
            if st.session_state.retrospective_feedback:
                st.markdown("### Current Feedback")
                for i, feedback in enumerate(st.session_state.retrospective_feedback):
                    st.write(f"{i+1}. {feedback}")
        
        with col2:
            if st.session_state.retrospective_feedback and st.button("🧠 Generate AI Insights"):
                with st.spinner("Analyzing retrospective feedback..."):
                    insights = agent.generate_retrospective_insights(st.session_state.retrospective_feedback)
                    st.markdown("### AI-Generated Insights")
                    st.write(insights)
    
    with tab4:
        st.subheader("Impediment Management")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Current Impediments")
            for i, impediment in enumerate(st.session_state.sprint_data.impediments):
                st.markdown(f"""
                <div class="impediment-card">
                    <strong>Impediment {i+1}:</strong> {impediment}
                </div>
                """, unsafe_allow_html=True)
            
            new_impediment = st.selectbox("Add New Impediment", ["Technical debt is slowing us down", "The staging environment is unstable", "We have a new dependency on another team"])
            if st.button("Add Impediment"):
                if new_impediment:
                    st.session_state.sprint_data.impediments.append(new_impediment)
                    st.success("Impediment added!")
                    st.rerun()
        
        with col2:
            st.markdown("### AI Resolution Suggestions")
            if st.session_state.sprint_data.impediments:
                selected_impediment = st.selectbox("Select Impediment", st.session_state.sprint_data.impediments)
                context = st.selectbox("Additional Context", ["This is a high priority issue", "This is blocking multiple team members", "We need a decision from the product owner"])
                
                if st.button("🔧 Get Resolution Suggestions"):
                    with st.spinner("Generating resolution strategies..."):
                        suggestions = agent.suggest_impediment_resolution(selected_impediment, context)
                        st.write(suggestions)
    
    with tab5:
        st.subheader("Sprint Reports")
        
        # Sprint summary
        st.markdown("### Sprint Summary")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            fig = go.Figure(data=go.Pie(
                labels=['Completed', 'Remaining'],
                values=[completed_points, total_points - completed_points],
                hole=0.3
            ))
            fig.update_layout(title="Story Points Progress", height=300)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Risk assessment chart
            risk_levels = ['Low', 'Medium', 'High']
            risk_counts = [3, 2, 1]  # Sample data
            fig = go.Figure(data=[go.Bar(x=risk_levels, y=risk_counts, marker_color=['#28a745', '#ffc107', '#dc3545'])])
            fig.update_layout(title="Risk Assessment", height=300)
            st.plotly_chart(fig, use_container_width=True)
        
        with col3:
            # Team satisfaction (sample data)
            satisfaction = ['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied']
            counts = [2, 2, 1, 0]
            fig = go.Figure(data=[go.Bar(x=satisfaction, y=counts, marker_color='#667eea')])
            fig.update_layout(title="Team Satisfaction", height=300)
            st.plotly_chart(fig, use_container_width=True)
        
        # Download report
        if st.button("📥 Generate Sprint Report"):
            report_data = {
                'sprint_number': st.session_state.sprint_data.sprint_number,
                'completion_rate': f"{completion_rate:.1f}%",
                'total_points': total_points,
                'completed_points': completed_points,
                'impediments': len(st.session_state.sprint_data.impediments),
                'team_size': len(st.session_state.sprint_data.team_members),
                'days_remaining': days_remaining
            }
            
            st.json(report_data)
            st.success("Report generated! You can copy the JSON data above.")

    with tab6:
        st.subheader("Team Updates")
        st.dataframe(st.session_state.team_updates, use_container_width=True)

        st.subheader("Current Implementations")
        st.dataframe(st.session_state.current_implementations, use_container_width=True)

        st.subheader("Product Backlog")
        st.dataframe(st.session_state.product_backlog, use_container_width=True)

        st.subheader("AI Scrum Master Recommendations")
        if st.button("🤖 Generate Recommendations"):
            with st.spinner("Generating recommendations..."):
                # Combine all data into a single context string
                context = f"""
                Team Updates:
                {st.session_state.team_updates.to_string()}

                Current Implementations:
                {st.session_state.current_implementations.to_string()}

                Product Backlog:
                {st.session_state.product_backlog.to_string()}

                Sprint Data:
                {st.session_state.sprint_data}
                """
                # Create a new method in the agent to handle this
                recommendations = agent.generate_scrum_master_recommendations(context)
                st.markdown(recommendations)

if __name__ == "__main__":
    main()