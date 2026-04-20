from fastapi import FastAPI
from google.cloud import firestore

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "OK"}

@app.post("/nowy_dokument")
def create_document():
    # Application Default credentials are automatically created.
    db = firestore.Client()
    cities = db.collection("cities")

    sf_landmarks = cities.document("SF").collection("landmarks")
    sf_landmarks.document().set({"name": "Golden Gate Bridge", "type": "bridge"})
    sf_landmarks.document().set({"name": "Legion of Honor", "type": "museum"})
    la_landmarks = cities.document("LA").collection("landmarks")
    la_landmarks.document().set({"name": "Griffith Park", "type": "park"})
    la_landmarks.document().set({"name": "The Getty", "type": "museum"})
    dc_landmarks = cities.document("DC").collection("landmarks")
    dc_landmarks.document().set({"name": "Lincoln Memorial", "type": "memorial"})
    dc_landmarks.document().set(
        {"name": "National Air and Space Museum", "type": "museum"}
    )
    tok_landmarks = cities.document("TOK").collection("landmarks")
    tok_landmarks.document().set({"name": "Ueno Park", "type": "park"})
    tok_landmarks.document().set(
        {"name": "National Museum of Nature and Science", "type": "museum"}
    )
    bj_landmarks = cities.document("BJ").collection("landmarks")
    bj_landmarks.document().set({"name": "Jingshan Park", "type": "park"})
    bj_landmarks.document().set(
        {"name": "Beijing Ancient Observatory", "type": "museum"}
    )

    return {"message": "Document created"}


@app.post(
    "/wypushuj-do-kolejki"
)
def push_to_queue():
    import os
    from google.cloud import pubsub_v1

    publisher = pubsub_v1.PublisherClient()
    topic_name = 'projects/{project_id}/topics/{topic}'.format(
        project_id="project-f917d675-ded5-498e-a47",
        topic='pierwsza-kolejka',  # Set this to something appropriate.
    )
    future = publisher.publish(topic_name, b'My first message!', spam='eggs')
    future.result()
    return {"message": "Pushed to queue"}