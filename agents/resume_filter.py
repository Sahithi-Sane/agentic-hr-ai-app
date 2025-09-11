from langchain.vectorstores import FAISS

def build_resume_index(embedding, resume_texts):
    return FAISS.from_texts(resume_texts, embedding)

def shortlist_candidates(index, job_description, top_k=3):
    results = index.similarity_search(job_description, k=top_k)
    return [res.page_content for res in results]
