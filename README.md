# llm_doc_chat_GCP
Document based chat application on Google Cloud  Platform (GCP). <br>
#### *Input file format:* excel (.xlsx) - this can be easily customised for other file formats such as csv, txt, docx formats.


## Technology stack:

- Large Language Model (LLM): Gemini-1.5 (pro/flash) using GCP Vertex-AI
- UI: python Streamlit
- Deployment: GCP Cloud Run (for containerized deployment)


## How to Build the application?

### Prerequisites: 
- You have a GCP account and essential services enabled (vertex AI, cloud storage, cloud build, cloud run)
- Google cloud SDK installed on you system and configured your project. (to setup your account run ```gcloud init```)
- To check config run ```gcloud config configurations list```

### Clone Repository:
```
git clone https://github.com/shashank3110/llm_doc_chat_GCP.git

cd llm_doc_chat_GCP

```

In ```app.py``` replace ```PROJECT_ID``` value with your GCP project ID.


### Build Image and deploy contirnerized application:

```
gcloud builds submit --tag gcr.io/<your-project-id>/<your-docker-image-name>
gcloud run deploy --image gcr.io/<your-project-id>/<your-docker-image-name> --platform managed --allow-unauthenticated
```

After successfully run the deployment command we will receive a url to our streamlit application running on GCP.


### My Learnings from this project:
- LLM Results are sensitive to document formats.
- Results sensitive to data preprocessing.
- Even the most sophisticated LLMs are not yet good at basic arithmetic (as of September 2024)
- Deploying streamlit applications as containerized apps via GCP Cloud Run works quite well.




