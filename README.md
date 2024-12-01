# **Resume Matcher Application**  
An intelligent resume matcher application built using **Flask**, **Python**, and **Machine Learning** to find the best matches for job descriptions based on resumes uploaded by users.

![resume matcher](https://github.com/user-attachments/assets/38599867-8829-427b-81e9-9e51f75d1d03)

---

## **Overview**

The **Resume Matcher Application** uses advanced text-processing techniques and machine learning algorithms to compare resumes with job descriptions and rank them based on their relevance. It helps recruiters shortlist candidates faster and more effectively.

---

## **Features**

- Upload multiple resumes in PDF, DOCX, or TXT formats.  
- Input a job description to find the best matching resumes.  
- Remove personal information (like names, addresses, etc.) using Named Entity Recognition (NER).  
- Rank resumes using **TF-IDF Vectorization** and **Cosine Similarity**.  
- Responsive and visually appealing interface.

---

## **Tech Stack**

- **Backend**: Python, Flask  
- **Frontend**: HTML, CSS  
- **Libraries**: 
  - [Spacy](https://spacy.io/) (for Named Entity Recognition)  
  - [Scikit-learn](https://scikit-learn.org/) (for TF-IDF and similarity calculations)  
  - [PyPDF2](https://pypi.org/project/PyPDF2/) and [docx2txt](https://pypi.org/project/docx2txt/) (for text extraction from files)

---

## **How It Works**

1. **Upload Resumes**: Users upload multiple resumes in supported formats.  
2. **Input Job Description**: The user provides the job description in plain text.  
3. **Text Extraction**: The application extracts text from resumes and removes personal information using NER.  
4. **Matching Algorithm**: 
   - Converts job description and resumes into TF-IDF vectors.  
   - Computes similarity using Cosine Similarity.  
   - Ranks resumes based on their similarity scores.  
5. **Results**: Displays the top 5 matching resumes along with their scores.

---

## **Usage**
1. Navigate to the homepage.
2. Upload one or more resumes.
3. Enter the job description.
4. Click Match to see the top 5 resumes ranked by relevance.
