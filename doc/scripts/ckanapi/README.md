# ckanapi
A command line interface and Python module for accessing the [CKAN Action API](http://docs.ckan.org/en/latest/api/index.html#action-api-reference)

>[!NOTE]
> `ckanapi`: https://github.com/ckan/ckanapi

## Installation

Installation with pip:
```
pip install ckanapi
```

Installation with conda:
```
conda install -c conda-forge ckanapi
```


## ckanapi CLI

The ckanapi command line interface lets you access local and
remote CKAN instances for bulk operations and simple API actions.


### Actions

Simple actions with string parameters may be called directly. The
response is pretty-printed to STDOUT.

used to adjust these limits.  `CKANAPI_MY_SITES` (comma-delimited list of CKAN urls)
will not have the `PARALLEL_LIMIT` applied.

`dump` and `load` jobs may be resumed from the last completed
record or split across multiple servers by specifying record
start and max values.

#### 🔧 Dump datasets from CKAN into a local file with 4 processes

```
$ ckanapi dump datasets --all -O datasets.jsonl.gz -z -p 4 -r http://localhost
```

#### 🔧 Export datasets including private ones using search

```
$ ckanapi search datasets include_private=true -O datasets.jsonl.gz -z \
          -c /etc/ckan/production.ini

# Remote URL
$ ckanapi search datasets include_private=true -O datasets.jsonl.gz -z \
          -r http://myckan.org/catalog --apikey my_api_key
```

`search` is faster than `dump` because it calls `package_search` to retrieve
many records per call, paginating automatically.

You may add parameters supported by `package_search` to filter the
records returned.


#### 🔧 Load/update datasets from a dataset JSON lines file with 3 processes

```
$ ckanapi load datasets -I datasets.jsonl.gz -z -p 3 -c /etc/ckan/production.ini

# Remote URL
$ ckanapi load datasets -I datasets.jsonl.gz -z -p 3 -r http://myckan.org/catalog --apikey my_api_key
```


### Bulk Delete

Datasets, groups, organizations, users and related items may be deleted in
bulk with the delete command. This command accepts ids or names on the
command line or a number of different formats piped on standard input.


```bash
  ckanapi delete (datasets | groups | organizations | users | related)
          (ID_OR_NAME ... | [-I JSONL_INPUT] [-s START] [-m MAX])
          [-p PROCESSES] [-l LOG_FILE] [-qwz]
          [[-c CONFIG] [-u USER] | -r SITE_URL [-a APIKEY] [--insecure]]
```

#### 🔧 All datasets (JSON list of "id" or "name" values)
```
$ ckanapi action package_list -j | ckanapi delete datasets

$ ckanapi action package_list -j -r http://ckan.source.org/catalog --apikey my_api_key | ckanapi delete datasets -r https://ckan.target.org -u ckan_admin -a target_api_key

```

#### 🔧 Selective delete (JSON object with "results" list containing "id" values)
```
$ ckanapi action package_search q=ponies | ckanapi delete datasets
```

#### 🔧 Processed JSON Lines (JSON objects with "id" or "name" value, one per line)
```
$ ckanapi dump groups --all > groups.jsonl
$ grep ponies groups.jsonl | ckanapi delete groups


# Remote delete datasets
$ ckanapi action package_list -j -r http://ousrce.ckan.org/catalog --apikey my_api_key  > default.jsonl
$ ckanapi delete datasets -I default.jsonl -p 3 -l log.log -u ckan_admin -r http://target.ckan.org/catalog --apikey my_api_key

```

#### 🔧 Text list of "id" or "name" values (one per line)
```
$ cat users_to_remove.txt
fred
bill
larry
$ ckanapi delete users < users_to_remove.txt


## Datasets
ckanapi delete users -r http://myckan.org/catalog --apikey my_api_key < output_pre.txt

```


### Bulk Dataset and Resource Export - datapackage.json format

Datasets may be exported to a simplified
[datapackage.json format](http://dataprotocols.org/data-packages/)
(which includes the actual resources, where available).

If the resource url is not available, the resource will be included
in the datapackage.json file but the actual resource data will not be downloaded.

```
$ ckanapi dump datasets --all --datapackages=./output_directory/ -r http://sourceckan.example.com
```

### Batch Actions

Run a set of actions from a JSON lines file. For local actions this is much faster than running
`ckanapi action ...` in a shell loop because the local start-up time only happens once.

Batch actions can also be run in parallel with multiple processes and errors logged, just like the
dump and load commands.

#### 🔧 Update a dataset field across a number of datasets
```
$ cat update-emails.jsonl
{"action":"package_patch","data":{"id":"dataset-1","maintainer_email":"new@example.com"}}
{"action":"package_patch","data":{"id":"dataset-2","maintainer_email":"new@example.com"}}
{"action":"package_patch","data":{"id":"dataset-3","maintainer_email":"new@example.com"}}
$ ckanapi batch -I update-emails.jsonl
```

#### 🔧 Replace a set of uploaded files
```
$ cat upload-files.jsonl
{"action":"resource_patch","data":{"id":"408e1b1d-d0ca-50ca-9ae6-aedcee37aaa9"},"files":{"upload":"data1.csv"}}
{"action":"resource_patch","data":{"id":"c1eab17f-c2d0-536d-a3f6-41a3dfe6a2c3"},"files":{"upload":"data2.csv"}}
{"action":"resource_patch","data":{"id":"8ed068c2-4d4c-5f20-90db-39d2d596ce1a"},"files":{"upload":"data3.csv"}}
$ ckanapi batch -I upload-files.jsonl --local-files
```

The `"files"` values in the JSON lines file is ignored unless the `--local-files` parameter is passed.
Paths in the JSON lines file reference files on the local filesystems relative to the current working
directory.

### Shell pipelines

Simple shell pipelines are possible with the CLI.

#### 🔧 Copy the name of a dataset to its title with 'jq'
```
$ ckanapi action package_show id=my-dataset \
  | jq '.+{"title":.name}' \
  | ckanapi action package_update -i
```

#### 🔧 Mirror all datasets from one CKAN instance to another
```
$ ckanapi dump datasets --all -q -r http://sourceckan.example.com \
  | ckanapi load datasets
```

* `ValidationError` - field errors listed in `.error_dict`
* `SearchQueryError` - error reported from SOLR index
* `SearchError`
* `CKANAPIError` - incorrect use of ckanapi or unable to parse response
* `ServerIncompatibleError` - the remote API is not a CKAN API

When using an action shortcut or the `call_action` method
failures are raised as exceptions just like when calling `get_action` from a
CKAN plugin:

```python
from ckanapi import RemoteCKAN, NotAuthorized
ua = 'ckanapiexample/1.0 (+http://example.com/my/website)'

demo = RemoteCKAN('https://demo.ckan.org', apikey='phony-key', user_agent=ua)
try:
    pkg = demo.action.package_create(name='my-dataset', title='not going to work')
except NotAuthorized:
    print('denied')
```

When it is possible to `import ckan` all the ckanapi exception classes are
replaced with the CKAN exceptions with the same names.


### File Uploads

File uploads for CKAN 2.2+ are supported by passing file-like objects to action
shortcut methods:

```python
from ckanapi import RemoteCKAN
ua = 'ckanapiexample/1.0 (+http://example.com/my/website)'

mysite = RemoteCKAN('http://myckan.example.com', apikey='real-key', user_agent=ua)
mysite.action.resource_create(
    package_id='my-dataset-with-files',
    url='dummy-value',  # ignored but required by CKAN<2.6
    upload=open('/path/to/file/to/upload.csv', 'rb'))
```

When using `call_action` you must pass file objects separately:

```python
mysite.call_action('resource_create',
    {'package_id': 'my-dataset-with-files'},
    files={'upload': open('/path/to/file/to/upload.csv', 'rb')})
```


### List all private datasets
```py
from ckanapi import RemoteCKAN, ValidationError, SearchQueryError, SearchError, CKANAPIError, ServerIncompatibleError
import requests

ua = 'ckanapiexample/1.0 (+http://example.com/my/website)'

# Configura tu instancia de CKAN y tu API key
ckan_instance = RemoteCKAN('http://myckan.example.com', apikey='api_key', user_agent=ua)

try:
    # Realiza la búsqueda de paquetes
    result = ckan_instance.action.package_search(
        q='*:*',
        include_private=True,
        include_drafts=True
    )
    print(f"Datasets: {result['count']}")
except (ValidationError, SearchQueryError, SearchError, CKANAPIError, ServerIncompatibleError) as e:
    print(f"Error: {e}")
```

### Session Control

As of ckanapi 4.0 RemoteCKAN will keep your HTTP connection open using a
[requests session](http://docs.python-requests.org/en/master/user/advanced/).

For long-running scripts make sure to close your connections by using
RemoteCKAN as a context manager:

```python
from ckanapi import RemoteCKAN
ua = 'ckanapiexample/1.0 (+http://example.com/my/website)'

with RemoteCKAN('https://demo.ckan.org', user_agent=ua) as demo:
    groups = demo.action.group_list(id='data-explorer')
print(groups)
```

Or by explicitly calling `RemoteCKAN.close()`.

### LocalCKAN

A similar class is provided for accessing local CKAN instances from a plugin in
the same way as remote CKAN instances.
Unlike [CKAN's get_action](http://docs.ckan.org/en/latest/extensions/plugins-toolkit.html?highlight=get_action#ckan.plugins.toolkit.get_action)
LocalCKAN prevents data from one action
call leaking into the next which can cause issues that are very hard do debug.

This class defaults to using the site user with full access.

```python
from ckanapi import LocalCKAN, ValidationError

registry = LocalCKAN()
try:
    registry.action.package_create(name='my-dataset', title='this will work fine')
except ValidationError:
    print('unless my-dataset already exists')
```

For extra caution pass a blank username to LocalCKAN and only actions allowed
by anonymous users will be permitted.

```python
from ckanapi import LocalCKAN

anon = LocalCKAN(username='')
print(anon.action.status_show())
```

#### Extra Loggging

To enable extra info logging for the execution of LocalCKAN ckanapi commands, you can enable the config option in your CKAN INI file.

```
ckanapi.log_local = True
```

The output of the log will look like:

```
INFO [ckan.ckanapi] OS User <user> executed LocalCKAN: ckanapi <args>
```

### TestAppCKAN

A class is provided for making action requests to a
[webtest.TestApp](http://webtest.readthedocs.org/en/latest/testapp.html)
instance for use in CKAN tests:

```python
from ckanapi import TestAppCKAN
from webtest import TestApp

test_app = TestApp(...)
demo = TestAppCKAN(test_app, apikey='my-test-key')
groups = demo.action.group_list(id='data-explorer')
```


## Tests

To run the tests:

  python setup.py test

