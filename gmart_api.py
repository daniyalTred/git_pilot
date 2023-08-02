import requests
import json
res=requests.get('https://globalmart-api.onrender.com/mentorskool/v1/sales',
             headers={'accept':'application/json','access_token':'fe66583bfe5185048c66571293e0d358'}
             )
print(f"the response is: {json.loads(res.text)}")