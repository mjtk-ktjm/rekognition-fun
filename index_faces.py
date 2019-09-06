import sys
import os
import re
import boto3 

bucket_name = "BUCKETNAME"
collection_id = "COLLECTIONNAME"
p = re.compile("0007.jpg")

dir_path = os.path.dirname(os.path.realpath(__file__))
all_objects = os.listdir(dir_path)

#

rek_client=boto3.client('rekognition')

for file_name in all_objects:
    if p.search(file_name):
        name_only, _ = file_name.split(".")
        name_only = name_only[:-1]
        for i in range(1,8):
            this_name = name_only + str(i) + ".jpg"
            print(this_name)
            response=rek_client.index_faces(CollectionId=collection_id,
                                Image={'S3Object':{'Bucket':bucket_name,'Name':this_name}},
                                ExternalImageId=this_name,
                                MaxFaces=1,
                                QualityFilter="AUTO",
                                DetectionAttributes=['ALL'])
            print(response)
