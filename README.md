#Sequence of Steps:

1. Create a repo in GitHub

2. Clone it in Cursor

3. Check Python version  
   python3 --version

4. Create Virtual Environment  (Do NOT commit yet)
   python3 -m venv venv  
   source venv/bin/activate  # (macOS/Linux)  
   venv\Scripts\activate     # (Windows)

5. Create .gitignore file and add BOTH .streamlit/secrets.toml and venv/  (Note: Do NOT commit yet)

6. Create .streamlit folder and add secrets.toml

7. Add API keys to secrets.toml

8. Create requirements.txt and add relevant libraries

9. Commit to GitHub

10. Create create_llm_message.py 

11. Create prompt_store.py

12. Create sub-agents i.e., smalltalk_agent.py, clarify_agent.py, math_agent.py, reading_agent.py, writing_agent.py

13. Create graph.py

14. Create app.py

15. Commit code in GitHub

16. Run and Test app.py