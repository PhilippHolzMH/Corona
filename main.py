from createjson import catch_cases
from creates3 import create_bucket
from creates3 import upload_json
 
create_bucket("bucket-fmv-446", "eu-central-1")
catch_cases("austria") 
upload_json("bucket-fmv-446","rawdata.json")

