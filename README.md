# SmartTable-IDs-Converter

x86-64 docker container that converts in place a file with identifiers derived from metacyc/biocyc/plantcyc into a 1-column txt file 

# Installation
1. Install Docker
2. Download the following container on your machine:

```shell
docker pull olgatsiouri/python-pandas:latest
```
3. Download `smarttable_ids_converter.py` from `src/`

## Usage

1. Go to metacyc/plantcyc/biocyc etc and select an organism and a pathway
2. create a SmartTable by clicking `Add to SmartTable` and selecting `New SmartTable`
3. in the `Add Transform column` select `Genes of pathway`
4. Click the 1st row and select delete, then click `Export -> to Spreadsheet File`

5. run docker:

on linux/mac os x64-86:

```bash
docker run --rm -it -v /path/to/folder:/data olgatsiouri/python-pandas /data/smarttable_ids_converter.py <input_txt> 
```
on mac silicon:

```shell
docker run --platform=linux/amd64 --rm -it -v /path/to/folder:/data olgatsiouri/python-pandas /data/smarttable_ids_converter.py <input_txt> 
```
or on windows:

```Powershell
docker run --rm -it -v C:\path\to\folder:/data olgatsiouri/python-pandas /data/smarttable_ids_converter.py <input_txt> 
```
example:
```bash
docker run --rm -it -v /home/linuxubuntu2004/Desktop:/data olgatsiouri/python-pandas /data/smarttable_ids_converter.py c4_pepck_ids.txt
```

Example input/output files can be found in the `data/` folder
Input data were derived from TomatoCyc v4.0
