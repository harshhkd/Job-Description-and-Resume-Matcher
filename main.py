# from flask import Flask, request, render_template
# import os
# import docx2txt
# import PyPDF2
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
#
# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads/'
#
# def extract_text_from_pdf(file_path):
#     text = ""
#     with open(file_path, 'rb') as file:
#         reader = PyPDF2.PdfReader(file)
#         for page in reader.pages:
#             text += page.extract_text()
#     return text
#
# def extract_text_from_docx(file_path):
#     return docx2txt.process(file_path)
#
# def extract_text_from_txt(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         return file.read()
#
# def extract_text(file_path):
#     if file_path.endswith('.pdf'):
#         return extract_text_from_pdf(file_path)
#     elif file_path.endswith('.docx'):
#         return extract_text_from_docx(file_path)
#     elif file_path.endswith('.txt'):
#         return extract_text_from_txt(file_path)
#     else:
#         return ""
#
# @app.route("/")
# def index():
#     return render_template('index.html')
#
# @app.route('/matcher', methods=['POST'])
# def matcher():
#     if request.method == 'POST':
#         job_description = request.form['job_description']
#         resume_files = request.files.getlist('resumes')
#
#         resumes = []
#         for resume_file in resume_files:
#             filename = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
#             resume_file.save(filename)
#             resumes.append(extract_text(filename))
#
#         if not resumes or not job_description:
#             return render_template('index.html', message="Please upload resumes and enter a job description.")
#
#         # Vectorize job description and resumes
#         vectorizer = TfidfVectorizer().fit_transform([job_description] + resumes)
#         vectors = vectorizer.toarray()
#
#         # Calculate cosine similarities
#         job_vector = vectors[0]
#         resume_vectors = vectors[1:]
#         similarities = cosine_similarity([job_vector], resume_vectors)[0]
#
#         # Get top 3 resumes and their similarity scores
#         top_indices = similarities.argsort()[-5:][::-1]
#         top_resumes = [resume_files[i].filename for i in top_indices]
#         # similarity_scores = [round(similarities[i], 2) for i in top_indices]
#         similarity_scores = [round(similarities[i] * 100, 2) for i in top_indices]
#
#         return render_template('index.html', message="Top matching resumes:", top_resumes=top_resumes, similarity_scores=similarity_scores)
#
#     return render_template('matchresume.html')
#
# if __name__ == '__main__':
#     if not os.path.exists(app.config['UPLOAD_FOLDER']):
#         os.makedirs(app.config['UPLOAD_FOLDER'])
#     app.run(debug=True)


# more accurate
#
# from flask import Flask, request, render_template
# import os
# import docx2txt
# import PyPDF2
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import spacy
#
# # Load Spacy model for Named Entity Recognition
# nlp = spacy.load('en_core_web_sm')
#
# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads/'
#
# def extract_text_from_pdf(file_path):
#     text = ""
#     with open(file_path, 'rb') as file:
#         reader = PyPDF2.PdfReader(file)
#         for page in reader.pages:
#             text += page.extract_text()
#     return text
#
# def extract_text_from_docx(file_path):
#     return docx2txt.process(file_path)
#
# def extract_text_from_txt(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         return file.read()
#
# def extract_text(file_path):
#     if file_path.endswith('.pdf'):
#         return extract_text_from_pdf(file_path)
#     elif file_path.endswith('.docx'):
#         return extract_text_from_docx(file_path)
#     elif file_path.endswith('.txt'):
#         return extract_text_from_txt(file_path)
#     else:
#         return ""
#
# def remove_personal_info(text):
#     """
#     Use Named Entity Recognition to remove personal information.
#     """
#     doc = nlp(text)
#     filtered_text = []
#     for token in doc:
#         # Exclude entities related to personal information
#         if token.ent_type_ not in ['PERSON', 'GPE', 'DATE', 'AGE', 'ORG', 'LOC']:
#             filtered_text.append(token.text)
#     return " ".join(filtered_text)
#
# @app.route("/")
# def index():
#     return render_template('index.html')
#
# @app.route('/matcher', methods=['POST'])
# def matcher():
#     if request.method == 'POST':
#         job_description = request.form['job_description']
#         resume_files = request.files.getlist('resumes')
#
#         resumes = []
#         for resume_file in resume_files:
#             filename = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
#             resume_file.save(filename)
#             text = extract_text(filename)
#             # Remove personal information from resume
#             filtered_text = remove_personal_info(text)
#             resumes.append(filtered_text)
#
#         if not resumes or not job_description:
#             return render_template('index.html', message="Please upload resumes and enter a job description.")
#
#         # Remove personal information from job description
#         filtered_job_description = remove_personal_info(job_description)
#
#         # Vectorize job description and resumes
#         vectorizer = TfidfVectorizer().fit_transform([filtered_job_description] + resumes)
#         vectors = vectorizer.toarray()
#
#         # Calculate cosine similarities
#         job_vector = vectors[0]
#         resume_vectors = vectors[1:]
#         similarities = cosine_similarity([job_vector], resume_vectors)[0]
#
#         # Get top 3 resumes and their similarity scores
#         top_indices = similarities.argsort()[-5:][::-1]
#         top_resumes = [resume_files[i].filename for i in top_indices]
#         similarity_scores = [round(similarities[i] * 100, 2) for i in top_indices]
#
#         return render_template('index.html', message="Top matching resumes:", top_resumes=top_resumes, similarity_scores=similarity_scores)
#
#     return render_template('matchresume.html')
#
# if __name__ == '__main__':
#     if not os.path.exists(app.config['UPLOAD_FOLDER']):
#         os.makedirs(app.config['UPLOAD_FOLDER'])
#     app.run(debug=True)
#


# with file name

from flask import Flask, request, render_template
import os
import docx2txt
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy

# Load Spacy model for Named Entity Recognition
nlp = spacy.load('en_core_web_sm')

app = Flask(__name__,static_folder='static')
app.config['UPLOAD_FOLDER'] = 'uploads/'


def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_text_from_docx(file_path):
    return docx2txt.process(file_path)

def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_text(file_path):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    elif file_path.endswith('.txt'):
        return extract_text_from_txt(file_path)
    else:
        return ""

def remove_personal_info(text):
    """
    Use Named Entity Recognition to remove personal information.
    """
    doc = nlp(text)
    filtered_text = []
    for token in doc:
        # Exclude entities related to personal information
        if token.ent_type_ not in ['PERSON', 'GPE', 'DATE', 'AGE', 'ORG', 'LOC']:
            filtered_text.append(token.text)
    return " ".join(filtered_text)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/matcher', methods=['POST'])
def matcher():
    if request.method == 'POST':
        job_description = request.form['job_description']
        resume_files = request.files.getlist('resumes')

        resumes = []
        uploaded_filenames = []  # Store uploaded filenames
        for resume_file in resume_files:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
            resume_file.save(filename)
            uploaded_filenames.append(resume_file.filename)  # Add filename to the list
            text = extract_text(filename)
            # Remove personal information from resume
            filtered_text = remove_personal_info(text)
            resumes.append(filtered_text)

        if not resumes or not job_description:
            return render_template('index.html', message="Please upload resumes and enter a job description.")

        # Remove personal information from job description
        filtered_job_description = remove_personal_info(job_description)

        # Vectorize job description and resumes
        vectorizer = TfidfVectorizer().fit_transform([filtered_job_description] + resumes)
        vectors = vectorizer.toarray()

        # Calculate cosine similarities
        job_vector = vectors[0]
        resume_vectors = vectors[1:]
        similarities = cosine_similarity([job_vector], resume_vectors)[0]

        # Get top 5 resumes and their similarity scores
        top_indices = similarities.argsort()[-5:][::-1]
        top_resumes = [uploaded_filenames[i] for i in top_indices]
        similarity_scores = [round(similarities[i] * 100, 2) for i in top_indices]

        return render_template(
            'index.html',
            message="Top matching resumes:",
            top_resumes=top_resumes,
            similarity_scores=similarity_scores,
            uploaded_filenames=uploaded_filenames  # Pass filenames to the template
        )

    return render_template('matchresume.html')

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)