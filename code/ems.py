import requests
from code.key import thai_post_token

class ems(object):
    def __init__(self, barcode):
        self.status_Ems_number = ""
        self.Response_message = ""
        self.barcode = barcode
        
        self.GET_item() #start

    def GET_token(self): #create token for api
        Token = thai_post_token

        url = "https://trackapi.thailandpost.co.th/post/api/v1/authenticate/token"
        Authorization = "Token {}".format(Token)

        headers = {
                'Content-Type':'application/json',
                'Authorization':Authorization
            }

        r = requests.post(url, headers=headers, verify=True)

        self.token = r.json()["token"]
    
    def GET_item(self):
        
        self.GET_token()
        url = "https://trackapi.thailandpost.co.th/post/api/v1/track"

        Authorization = "Token {}".format(self.token)
        headers = {
                'Content-Type':'application/json',
                'Authorization':Authorization
            }
        data = {
            "status": "all",
            "language": "TH",
            "barcode": [
                "{}".format(self.barcode)
            ]    
        }

        r = requests.post(url, headers=headers, json=data, verify=True)
        #* รีเซ็ตตัวเเปล
        self.status_Ems_number = ""
        self.Response_message = ""
        number = 0
        id = ""
        status = ""
        location = ""

        #* ถ้าเลขเเทรคผิด
        if(r.json()["response"]["items"][self.barcode] == []): 
            self.status_Ems_number = False
            self.Response_message = "ไม่พบหมายเลขพัสดุ กรุณาตรวจสอบใหม่อีกครั้งนะคะ"
        
        else:
            number = len(r.json()["response"]["items"][self.barcode])
            id = r.json()["response"]["items"][self.barcode][number - 1]["barcode"]
            status = r.json()["response"]["items"][self.barcode][number - 1]["status_description"]
            location = r.json()["response"]["items"][self.barcode][number - 1]["location"]
            self.status_Ems_number = True
            self.Response_message = "{}\nStatus: {}\nLocation: {}".format(id, status, location)
