"""
MIT License

Copyright (c) 2022 Konrad

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from colorama import Fore

class FilesManagerException(Exception):
    def __init__(self,error_name=None, string=None):
        string = string or "Exception triggered"
        print(Fore.RED + error_name + ': ' + string)

# errors
class SourceConvertError(FilesManagerException): 
    def __init__(self, msg): 
        super().__init__(self.__class__.__name__, msg)

class DownloadError(FilesManagerException): 
    def __init__(self, msg): 
        super().__init__(self.__class__.__name__, msg)