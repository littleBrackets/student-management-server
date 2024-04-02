from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
import pdfkit
import tempfile
import os

from app.routers import router
from app.config import API_PREFIX, ORIGINS

app = FastAPI()

origins = ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix=API_PREFIX)


@app.get("/educatu-server")
async def root():
    return {"message": "Hello and Welcome to educatu server."}

@app.get("/educatu-server/test/pdf")
async def root():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Generated PDF</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>This PDF was generated on the server side using pdfkit.</p>
    </body>
    </html>
    """
    wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # Update this path
    pdfkit_config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
    pdf = pdfkit.from_string(html_content, False, configuration=pdfkit_config)
    response = Response(content=pdf, media_type="application/pdf")
    response.headers["Content-Disposition"] = "attachment; filename=output.pdf"
    return response


@app.get("/educatu-server/test2/pdf")
async def root():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    html_file_path = os.path.join(current_dir, "pdftemplates", "test1", "myhtml.html")
    css_file_path = os.path.join(current_dir, "pdftemplates", "test1", "mystyle.css")
    if not os.path.exists(html_file_path):
        raise HTTPException(status_code=404, detail="HTML file not found")
    with open(html_file_path, "r") as html_file:
        html_content = html_file.read()
    wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # Update this path
    pdfkit_config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
    pdf = pdfkit.from_string(html_content, False, configuration=pdfkit_config, css=css_file_path)
    response = Response(content=pdf, media_type="application/pdf")
    response.headers["Content-Disposition"] = "attachment; filename=output.pdf"
    return response