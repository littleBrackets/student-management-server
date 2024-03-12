myenv\Scripts\activate
uvicorn app.main:app --reload


dependencies

pip install fastapi
pip install "uvicorn[standard]"
pip install "python-jose[cryptography]"
pip install "passlib[bcrypt]"
pip install sqlalchemy
pip install psycopg2
pip install python-multipart


