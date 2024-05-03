from fastapi import FastAPI, Response, Depends
from setup import set_queue

app = FastAPI()

@app.on_event("startup")
def startup():
    channel = set_queue()
    return channel


@app.post("/send-message")
def send_message(response: Response,
                 message: str,
                 channel=Depends(startup)):
    try:
        channel.basic_publish(exchange='exchange',
                              routing_key='tasks',
                              body=message)
        return {'ok': True}
    except Exception as e:
        response.status_code = 400
        return {'ok': False, 'message': str(e)}
