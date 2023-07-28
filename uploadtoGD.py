import os
from googleapiclient.discovery import build 
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload

# Google Drive API認證設定
SCOPES = ['https://www.googleapis.com/auth/drive']  
CREDENTIALS_FILE = 'credentials.json'

upt_folder = r'C:\Users\cn\Desktop\Cloud-AutoUpload\upt'  
drive_folder = '197VyoiyRjW39qmI63-Tc7XL52T7qDKeS'

flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
creds = flow.run_local_server(port=0)

drive_service = build('drive', 'v3', credentials=creds)

# 上傳文件  
for filename in os.listdir(upt_folder):
  if filename.endswith('.png'):
    file_metadata = {
      'name': filename,
      'parents': [drive_folder]
    }
    media = MediaFileUpload(os.path.join(upt_folder, filename), resumable=True)
    drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

print('Upload complete')