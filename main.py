#import classes
import base64
import urllib
import json

#image path of picture
base_path_image = "/Users/thomasmeichtry/Desktop/Application based Object-oriented Programming/" \
                  "OOPBallers/Pictures/Karotten.jpg"

def send_request():
    """ sends a request to the Google Vision API """

    base_url = "https://vision.googleapis.com/v1/images:annotate?key="
    api_key = "AIzaSyDfKIKpRF7OBu5Q3Q6Zh1zxFOsulyTZ2IE"
    url = base_url + api_key

    json_request = {
                      "requests":[
                        {
                          "image":{
                            #encoded_image
                          },
                          "features":[
                            {
                              "type":"LABEL_DETECTION",
                              "maxResults":1
                            }
                          ]
                        }
                      ]
                    }

def encode_image_as_base64(image_path):
    """ Loads an image from path and returns it as base64 encoded string """

    print("Encoding image: "+ image_path)

    encoded_string = ""
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    return encoded_string


#the main function is the first function to be executed when starting a programm.
if __name__ == "__main__":
    print(encode_image_as_base64(base_path_image))