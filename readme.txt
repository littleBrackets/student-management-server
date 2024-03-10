myenv\Scripts\activate

pip install fastapi

pip install "uvicorn[standard]"

pip install "python-jose[cryptography]"

pip install "passlib[bcrypt]"

pip install sqlalchemy

pip install psycopg2

uvicorn app.main:app --reload


test dependencies

pip install python-multipart

