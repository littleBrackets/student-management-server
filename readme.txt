myenv\Scripts\activate
uvicorn app.main:app --reload

dependencies

py -m venv myenv
python -m venv myenv

pip install fastapi "uvicorn[standard]" "python-jose[cryptography]" "passlib[bcrypt]" sqlalchemy psycopg2 python-multipart

pip install fastapi
pip install "uvicorn[standard]"
pip install "python-jose[cryptography]"
pip install "passlib[bcrypt]"
pip install sqlalchemy
pip install psycopg2
pip install python-multipart

pip install weasyprint
pip install pdfkit

uvicorn app.main:app --host 0.0.0.0 --port 8021
