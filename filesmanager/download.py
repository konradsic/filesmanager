"""
MIT License

Copyright (c) 2022 Konrad

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import typing as t
import requests
from .abc import DownloadSource, ReturnInformation
from .errors import SourceConvertError, DownloadError

class DownloadManager:
    """
    DownloadManager
    ================
    Class allowing to download files from any url provided

    Parameters
    ----------
    source_link: :class:`str`
        A base URL where files will be downloaded from. Can be either a base link to a resource (eg. https://resourceful.com/resources) or a direct link to a file (https://files.org/file/cf540s9d.png). Please note that you shouldn'y visit any of these sites they are just examples
    https: :class:`bool`
        Indicates wherever the source is secure or not. Defaults to True may cause errors when downloading
    chilren: :class:``list[DownloadSource] | []`
        "Children" of the source to be downloaded. If none are provided, the program will download only from uri, chilren can be used to download multiple sources from the root url. If argument is empty it will set chilren to an empty list

    Attributes
    ----------
    source: :class:`DownloadSource`
        Packed source dataclass
    """
    def __init__(
        self, 
        source_link: str,
        https: bool=True,
        children: t.Union[t.List[DownloadSource], t.List]=[]
    ) -> None:
        url = ""
        uri = ""
        # check if source link is an URL or URI
        if source_link.startswith("https://") or source_link.startswith("http://"):
            uri = source_link
            url_strip_len = 8 if https else 7
            url = uri[url_strip_len:]
            if url.endswith("/"):
                url = url[:-1]
            if not uri.endswith("/"):
                uri += "/"

        else:
            url = source_link
            uri = f"{'https' if https else 'http'}://{url}/"

        self.source: DownloadSource = DownloadSource(
            url=url,
            uri=uri,
            https=https,
            children=children
        )

        # other sources
        self.sources = [self.source]

    def add_source(
        self,
        url: str,
        uri: t.Optional[str]=None,
        https: t.Optional[bool]=True,
        children: t.Optional[t.List[DownloadSource]]=[]
    ) -> DownloadSource:
        try:
            uri = f"{'https' if https else 'http'}://{url}{'/' if not url.endswith('/') else ''}"
            
            self.sources.append(DownloadSource(
                url=url,
                uri=uri,
                https=https,
                children=children
            ))
            return self.sources[-1] # freshly added source
        except:
            raise SourceConvertError("Failed to convert data to DownloadSource - invalid parameters were passed")

    def download_sources(self, all_:bool=False):
        """
        Downloads a file or files (only if childrens are passed)

        Parameters
        ----------
        all: :class:`bool`
            Wherever to download all sources or only the first one. Defaults to False
        """
        sources = [self.sources[0]] if all_ else self.sources
        info = ""
        try:
            # iteracte over sources and download them
            for source in sources:
                download_query = [source.uri]
                if source.children:
                    download_query = [f"{source.uri}{child}" for child in source.children]
                for q in download_query:
                    try:
                        req = requests.get(q, stream=True)
                        filename = q[:-1].split("/")[-1]
                        print(filename)
                        with open(filename, "wb") as qfile:
                            qfile.write(req.content)
                    except Exception as e:
                        info += f"Failed to load resource {q} caused by {e.__class__.__name__}:{e}\n"
                        continue
        except Exception as e:
            DownloadError(f"Download failed because of {e.__class__.__name__}: {e}")
        return ReturnInformation("Results for downloading files", info)

    def __str__(self):
        return f"<DownloadManager url={self.source.url} uri={self.source.uri} https={self.source.https} sources={self.sources}>"