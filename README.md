# SmartTable-IDs-Converter
Fast and lightweight windows x86 gui app that converts in place a file with identifiers derived from metacyc/biocyc/plantcyc into a 1-column txt file 

## Dependencies

1. Windows 11 or 10 version 16215.0 or higher(type `winver` on the search button and click `winver` to find your OS version)
2. [Windows Subsystem for linux(wsl1)](INSTALL.md)
3. the file in the `bin` folder

if you want a windows only software look up the `nowsl` branch

if you want instead to run it via docker go to the `docker` branch

## Usage

![](img/1.png)

1. Go to metacyc/plantcyc/biocyc etc and select an organism and a pathway
2. create a SmartTable by clicking `Add to SmartTable` and selecting `New SmartTable`
3. in the `Add Transform column` select `Genes of pathway`
4. Click the 1st row and select delete, then click `Export -> to Spreadsheet File`
5. Open `SmartTable IDs Converter.exe` and click `Browse` to select an input file
6. Click `Run program` to convert the file in place

Example input/output files can be found in the `data/` folder
Input data were derived from TomatoCyc v4.0  
**Note: Input file can either contain *Genes of pathway* in the 1st row or if the ids are derived from SmartTable enrichment analysis, it should contain only the identifiers**