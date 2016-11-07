import boto
from boto.s3.key import Key
import requests
import os
import urlparse

#setup the bucket configuration variables

AWS_ACCESS_KEY = 'YOUR ACCESS KEY'
AWS_ACCESS_SECRET_KEY = 'YOUR SECRET KEY'
AWS_HOST = 'YOUR REGION LIKE api-southeast-1 for singapore'
AWS_BUCKET = 'YOUR BUCKET NAME'

def extractFileExtension(url):
    path = urlparse.urlparse(url).path
    ext = os.path.splitext(path)[1]
    if ext is None or len(ext) is 0:
        return '.png'
    else:
        return ext 

def upload_to_s3(fileName,fileUrl):
    print "connecting to your bucket"
    try:
        conn = boto.s3.connect_to_region(AWS_HOST, aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_ACCESS_SECRET_KEY)
        bucket = conn.get_bucket(AWS_BUCKET, validate=False)
    except:
        print "an exception is raised in connecting to bucket"
    print "fetching file from URL"
    r = requests.get(fileUrl)
    if r.status_code == 200:
        print "extraction of URL successful now uploading to s3 ..."
        ext = extractFileExtension(fileUrl)
        k = Key(b)
        k.key = "%s%s" % (fileName,ext)
        k.content_type = r.headers['content-type']
        k.set_contents_from_string(r.content)
        print "successfully uploaded."
    else:
        print "cannot fetch the file from URL returning status code %s" % (r.status_code)


#url = 'https://s3-ap-southeast-1.amazonaws.com/oyo-dev-1/uploads/hotel_image/2/hotel.jpeg'
#upload_to_s3('image2',url)
