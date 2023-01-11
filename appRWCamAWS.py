from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
import cv2
from cvlib.object_detection import draw_bbox
# in dos command is cd C:\Users\USER\PycharmProjects\pythonProject\pythonProject\smartParkingv2\apptry1
# then uvicorn appRWCamAWS:app --reload


app = FastAPI()


@app.get("/")
def first():
    return{"System is ready: capture or show"}

@app.get("/capture/")
def home():
    cap = cv2.VideoCapture(0)
    noOfframe = 10
    for x in range(noOfframe):
        ret, frame = cap.read()

    filename = 'savedImage.png'
    cv2.imwrite(filename, frame)
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return {'image captured'}

@app.get("/show/")
async def read_random_file():
    filename = 'savedImage.png'
    return FileResponse(filename)


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)