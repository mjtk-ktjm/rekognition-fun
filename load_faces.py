import sys
import os
import re
import boto3 
import time 

bucket_name = "BUCKETNAME"
p = re.compile("0007.jpg")

dir_path = os.path.dirname(os.path.realpath(__file__))
all_objects = os.listdir(dir_path)

s3_resource = boto3.resource("s3")

for file_name in all_objects:
    if p.search(file_name):
        name_only, _ = file_name.split(".")
        name_only = name_only[:-1]
        for i in range(1,8):
            this_name = name_only + str(i) + ".jpg"
            full_file_path = dir_path + "/" + this_name
            target_file_name = "faces/" + this_name
            print("Sending {} from {} to {}  now...".format(this_name, full_file_path, target_file_name))
            s3_resource.meta.client.upload_file(
                                    full_file_path,
                                    bucket_name,
                                    target_file_name
                                    )
