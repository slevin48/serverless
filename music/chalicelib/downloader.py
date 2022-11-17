from pytube import YouTube, exceptions
from abc import ABC, abstractmethod
import os


class VideoDownloader(ABC):
    @abstractmethod
    def download(self, url: str, path: str):
        pass


class YoutubeDownloader(VideoDownloader):
    def __init__(self):
        self.out_file = None

    def download(self, url: str, path: str = "./downloads"):
        if url is None:
            raise ValueError("URL is None")
        try:
            video = YouTube(url).streams.filter(only_audio=True).first()
            self.out_file = video.download(output_path=path)
            self.convert_to_mp3()
        except exceptions.RegexMatchError:
            raise ValueError("Invalid URL")
        except exceptions.VideoUnavailable:
            raise ValueError("Video is unavailable")
        return video.title

    def convert_to_mp3(self):
        base, ext = os.path.splitext(self.out_file)
        new_file = base + '.mp3'
        if not os.path.exists(new_file):
            os.rename(self.out_file, new_file)