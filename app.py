from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

from extract_resume import extract_text_from_pdf
from matcher import match_resume_to_jd  # updated function name

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the uploaded resume file
        file = request.files["resume"]

        # Get the job description entered by the user
        job_desc = request.form["job_description"]

        if file and job_desc:
            # Save the uploaded file
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)

            # Extract text from the resume
            resume_text = extract_text_from_pdf(filepath)

            # Compare the resume text with job description
            score = match_resume_to_jd(resume_text, job_desc)

            # Show the result on the next page
            return render_template("results.html", score=score)

    # If it's a GET request, just show the form
    return render_template("index.html")

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True)
