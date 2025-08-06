from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.responses import StreamingResponse
import cv2
import numpy as np
import io

app = FastAPI()
@app.post("/object_detection")
async def object_detection(input_file: UploadFile = File(None)):
    if not input_file.content_type.startswith("image/"):
        raise HTTPException(status_code=415, detail="unsupported file type")
    contents = await input_file.read()
    np_array = np.frombuffer(contents, dtype=np.uint8)
    image_rgb = cv2.imdecode(np_array, cv2.IMREAD_UNCHANGED)
    #image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)

    catface_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface.xml")
    faces = catface_detector.detectMultiScale(image_rgb)

    for cat_face in faces:
        x, y, w, h = cat_face
        cv2.rectangle(image_rgb, [x, y], [x+w, y+h], (100, 200, 100), 5)

    _, encoded_image = cv2.imencode(".jpg", image_rgb)
    image_bytes = encoded_image.tobytes()
    return StreamingResponse(io.BytesIO(image_bytes), media_type="image/jpeg" )