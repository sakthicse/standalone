import boto3
from botocore.client import Config
import io
# import pdftotext
from six.moves.urllib.request import urlopen
from PyPDF2 import PdfFileReader
from io import BytesIO

ACCESS_KEY_ID = 'AKIA3PEUNMSCYNBM5NJQ'
ACCESS_SECRET_KEY = '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'



# S3 Connect
s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)

# s3 = boto3.resource('s3')
bucket = s3.Bucket('liscp-data')

# get to get the whole body.
for obj in bucket.objects.all():
    key = obj.key
    file_extension = key.split('/')
    file_type = file_extension[len(file_extension)-1].split('.')
    image_ext = ['png','jpeg']
    if file_type:
	    if file_type[1] == 'pdf':
	    	body = obj.get()['Body'].read()
	    	# # pdfFileObj = obj.get()['Body'].read()
	    	# pdfFileObj = open(body, 'rb')
	    	# # creating a pdf reader object
	    	# pdfReader = PyPDF2.PdfFileReader(body)
	    	# # printing number of pages in pdf file
	    	# print(pdfReader.numPages)
	    	# # creating a page object
	    	# pageObj = pdfReader.getPage(0)
	    	# # extracting text from page
	    	# print(pageObj.extractText())
	    	# # closing the pdf file object
	    	# pdfFileObj.close()
	    	# print(body)
	    	
	    	
	    	fs = obj.get()['Body'].read()
	    	pdfFile = PdfFileReader(BytesIO(fs))
	    	info = pdfFile.getDocumentInfo()
	    	# print(info)
	    	# get the first page
	    	page = pdfFile.getPage(1)
	    	print(page)
	    	# print('Page type: {}'.format(str(type(page))))
	    	text = page.extractText()
	    	print("==============================================================")
	    	print(text)

	    	# pdfReader = PdfFileReader(BytesIO(body))

	    	# remote_file = obj.get()['Body'].read()
	    	# memory_file = io.BytesIO(remote_file)
	    	# pdf = pdftotext.PDF(memory_file)
	    	# total_contant = "".join(pdf)
	    	print(pdfFile)

	    	# print(pdfReader)
	    	# print(pdfReader.numPages)
	    	# pageObj = pdfReader.getPage(0)
	    	# print(pageObj)
	    	# print(pageObj.extractText())
	    	# pdfFileObj.close()
	    	print("In ...")
	    elif file_type[1] == 'csv' or file_type[1] == 'txt':
	    	body = obj.get()['Body'].read()
	    	# print(body)
	    elif file_type[1] in image_ext:
	    	pass
    print("*************")
    print(key)