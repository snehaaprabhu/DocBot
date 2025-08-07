import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def format_context(chunks):
    return "\n".join(chunks)

def answer_query(query, vectordb):
    context_chunks = vectordb.query(query)
    context = format_context(context_chunks)

    prompt = f"""
    You are an AI assistant. Use the following document context to answer the user's question:

    Context:
    {context}

    Question: {query}
    Answer:
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()
