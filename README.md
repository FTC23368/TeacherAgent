#Sequence of Steps:

1. Create a repo in GitHub

2. Clone it in Cursor

3. Check Python version  
   python3 --version

4. Create Virtual Environment  
   python3 -m venv venv  
   source venv/bin/activate  # (macOS/Linux)  
   venv\Scripts\activate     # (Windows)

5. Create .gitignore file and add .streamlit/secrets.toml

6. Create .streamlit folder and add secrets.toml

7. Add API keys to secrets.toml

8. Create requirements.txt and add relevant libraries

9. Create create_llm_message.py 

10. Create prompt_store.py

11. Create sub-agents i.e., math_agent.py, reading_agent.py, writing_agent.py

12. Create graph.py

13. Create teacherapp.py

14. Commit code in GitHub

15. Run and Test teacherapp.py