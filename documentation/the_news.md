# newsapi-python

A Python client for the [News API](https://newsapi.org/docs/).

## License


```
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## General

This is a Python client library for [News API V2](https://newsapi.org/).
The functions and methods for this library should mirror the
endpoints specified by the News API [documentation](https://newsapi.org/docs/endpoints).

## Installation

Installation for the package can be done via `pip`:

```bash
pip install newsapi-python
```

## Usage

After installation, import the client class into your project:

```python
from newsapi import NewsApiClient
```

Initialize the client with your API key:

```python
api = NewsApiClient(api_key='XXXXXXXXXXXXXXXXXXXXXXX')
```

### Endpoints

An instance of `NewsApiClient` has three instance methods corresponding to three News API endpoints.

#### Top Headlines

Use `.get_top_headlines()` to pull from the [`/top-headlines`](https://newsapi.org/docs/endpoints/top-headlines) endpoint:

```python
api.get_top_headlines(sources='bbc-news')
```

#### Everything

Use `.get_everything()` to pull from the [`/everything`](https://newsapi.org/docs/endpoints/everything) endpoint:

```python
api.get_everything(q='bitcoin')
```

#### Sources

Use `.get_sources()` to pull from the [`/sources`](https://newsapi.org/docs/endpoints/sources) endpoint:

```python
api.get_sources()
```

