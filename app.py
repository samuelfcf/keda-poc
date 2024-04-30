from fastapi import FastAPI, Response
from setup import set_channel_and_queue

app = FastAPI()


@app.post("/send-message")
async def send_message(response: Response,
                       message: str):
    channel = set_channel_and_queue()

    try:
        channel.basic_publish(exchange='test_q',
                              routing_key='test_q',
                              body=message)
        return {'ok': True}
    except Exception as e:
        response.status_code = 400
        return {'ok': False, 'message': str(e)}
