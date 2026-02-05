def retrieve_data():
    conn = sqlite3.connect("samsung.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM phones")
    data = cur.fetchall()
    conn.close()
    return data

def review_agent(data):
    return (
        f"{data[0][0]} has better camera and battery than {data[1][0]}. "
        "Display quality is similar. Recommended for photography."
    )

from fastapi import FastAPI

app = FastAPI()

@app.post("/ask")
def ask(q: dict):
    data = retrieve_data()
    answer = review_agent(data)
    return {"answer": answer}
