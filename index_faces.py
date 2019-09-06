import sys
import os
import re
import boto3 

bucket_name = "BUCKETNAME"
collection_id = "COLLECTIONID"
p = re.compile("0007.jpg")

dir_path = os.path.dirname(os.path.realpath(__file__))
all_objects = os.listdir(dir_path)

#

rek_client=boto3.client('rekognition')

for file_name in all_objects[100:]:
    if p.search(file_name):
        name_only, _ = file_name.split(".")
        name_only = name_only[:-1]
        for i in range(1,8):
            external_image_id = name_only + str(i)
            this_name = "faces/" + external_image_id + ".jpg"
            print("Indexing face ".format(external_image_id, this_name))
            response=rek_client.index_faces(CollectionId=collection_id,
                                Image={'S3Object':{'Bucket':bucket_name,'Name':this_name}},
                                ExternalImageId=external_image_id,
                                DetectionAttributes=["ALL"],
                                MaxFaces=1,
                                QualityFilter="AUTO",
                                )
            print(response)
