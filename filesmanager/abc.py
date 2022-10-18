"""
MIT License

Copyright (c) 2022 Konrad

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from dataclasses import dataclass
import typing as t

@dataclass
class DownloadSource:
    """
    Represents a download source.

    Attributes
    ----------
    url: :class:`str`
        A url of the source
    uri: :class:`str`
        URI of the source (contains http or https and url)
    https: :class:`bool`
        Tells if the source is protected by the https protocol or not
    children: :class:`list[str] | None`
        If they exist the so-called "children" are multiple filenames whose parent is the url (eg. children are ["file1","file2"] the program will download `url/child` for every child given)
    """
    url: str
    uri: str
    https: bool
    children: t.Optional[t.List[str]]