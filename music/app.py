import os
from chalice import Chalice
from chalicelib.downloader import YoutubeDownloader
# from chalicelib.aws_helper import S3
import boto3

app = Chalice(app_name='music')

@app.route('/convert', methods=['POST'])
def convert():
    if app.current_request.query_params is not None:
        if 'v' not in app.current_request.query_params:
            return {'error': 'Parameter v is missing'}
        else:
            url_extension = app.current_request.query_params.get('v')
            url = "https://www.youtube.com/watch?v={url_part}".format(url_part=url_extension)
            yt = YoutubeDownloader()
            title = yt.download(url)
            # S3("music48").upload_file(file_path="/tmp/"+title+".mp3",
            #                                     s3_path="/downloads/{url_part}.mp3".format(url_part=title))
            print(title)
            s3_client = boto3.client('s3')
            file_name = "downloads/"+title+".mp3"
            object_name = file_name
            s3_bucket = "music48"
            s3_client.upload_file(file_name, s3_bucket, object_name)
            os.remove("downloads/"+title+".mp3")
            os.remove("downloads/"+title+".mp4")
            return {'success': 'Video downloaded'}
    else:
        return {'error': 'No video URL provided'}