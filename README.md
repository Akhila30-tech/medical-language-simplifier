## 🩺 Medical Language Simplifier  

This tool rewrites complicated medical sentences into simple, understandable English. It’s meant for patients, families, or anyone without a medical background who wants to understand what’s written in a report.  

## 🔍 What It Does  

You input a sentence like:

> "Patient has hepatosplenomegaly and dyspnea."

It returns:

> "The patient has an enlarged liver and spleen, and difficulty breathing."

It identifies medical terms and replaces them with simpler language.  

## 🧠 How It Works

- Uses spaCy for natural language processing
- A custom dictionary maps medical terms to plain-English equivalents
- You can expand the dictionary anytime to cover more terms

## 🧪 Example Inputs

Try sentences like these:

- "CT scan shows pulmonary edema and pleural effusion."
- "The patient exhibits bradycardia and cyanosis."
- "Findings suggest cardiomegaly with pericardial effusion."
- "Diagnosis: nephrolithiasis and hematuria."

The tool will translate those into everyday language.  

## 💡 Future Plans

- Add a Streamlit UI for easy input/output
- Use scispaCy for advanced medical term detection
- Allow uploading a full report and simplify it in bulk
- Add multilingual support for Hindi or Spanish output

## 👩‍💻 Created by

**Akhila Patlolla**  
Making machine learning more useful, one real-life tool at a time.  
🔗 [LinkedIn](https://www.linkedin.com/in/akhila-patlolla-02b8891b1/)

## ⭐️ Like it?

Star the repo if it helped you. Feel free to fork or contribute!
