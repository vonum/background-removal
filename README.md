# background-removal
Service responsible for removing background from images and uploading them to gcloud.

## Setup
1. git clone git@github.com:vonum/background-removal.git
2. docker build -t background-removal .

This create an image with all available models installed:
1. U2net
2. U2netp
3. BASNet
4. XCEPTION
5. MOBILENET

## Running the container
```bash
docker run -p 8000:8000 \
  --mount type=bind,source=SRC_PATH,target=TARGET_PATH \
  background-removal:latest
```

## Request parameters
1. `url`: Image url
2. `model`: ["u2net", "u2netp", "basnet", "xception_model", "mobile_net_model"]
3. `preprocessing`: ["bdd-fastrcnn", "bbmd-maskrcnn", "None"]
4. `postprocessing`: ["rtb-bnb", "rtb-bnb2", "No"]

## Examples
### Payload
```json
{
  "model": "u2net",
  "url": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Donkey_in_Clovelly%2C_North_Devon%2C_England.jpg"
}
```

### Request
```bash
curl -X POST \
     -H "Content-type: application/json" \
     -d @scripts/image_request.json \
     0.0.0.0:8000/remove_background
```
