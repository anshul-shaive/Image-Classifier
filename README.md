# Image-Classifier

API: https://dog-classifier-app-as.herokuapp.com/get_prediction

Send a POST request(from postman,etc) there and in request body inside form-data, pass base64 encoded image value in the 'image' key.
(First request can take some time as the app is hosted in a free dyno on heroku).

Example:

POST: https://dog-classifier-app-as.herokuapp.com/get_prediction
Body:form-data:

{
'image': /9j/4AAQSkZJRgABAQEASABIAAD/2wBDAAYEBQYFBAYGBQYHBwYIChAKCgkJC......
}

Response:
{
    "breed": "golden_retriever",
    "score": "0.99999034"
}
