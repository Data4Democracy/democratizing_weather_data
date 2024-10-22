# Streaming Weather Data

This folder was created by a team of University of Washington Professional and Continuing Education night school students for a final project, for class Big Data 230B Emerging Technologies in Big Data 8/23/2017.

## Overview
The main components of the project are:
- A set of python scripts that use Apache Kafka and Web API's to gather weather and traffic data from Washington State Dept of Transportation (WSDOT) and Yahoo Query Language (YQL), and save to disk as JSON files.
- A Jupyter Notebook that aggregates the JSON files into data frames, and does some mapping and graphing.


|File of Interest | Description |
|----------------:|:------------|
| BigData_Su17_Proposal.pdf | Proposal for the original UW class project. |
| BigData_Su17_Outbrief.pdf | Final UW class presentation | 
| APIs/API_index.csv | Table of Web API's, including url syntax and links to API documentation. |
| APIs/\*.json       | Sample Web API outputs. |
| prototypes/wsdot_weather/\*.py | Kafka producers which call Web API's; consumers which store outputs as json. |
| prototypes/UW_PCE_BIGDATA_230B.ipynb | Jupyter Notebook which opens multiple json files, combines them into data frames, then does mapping and visualization.|

Open_Weather/\*.py contains Kafka scripts that call openweathermap.org, but the  resulting json has issues.

_Cool-looking tables, huh?  I learned how to do it from [adam-p's markdown cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)_

## Running the Python Kafka Scripts
[TODO] Describe the Bitnami, etc.

## Setting up the Jupyter Environment & Notebook
[TODO] Describe Conda, etc.

## Alternatives to Kafka
In theory, you could have a python script that simply runs on one machine, making web API calls and saving results to json. The use of Kafka was a class project requirement, that may or may not fit your particular use case.  

## Future Work
- Add instructions for setting up Bitnami Kafka server & scripts.
- Add instructions for setting up the conda environment for Jupyter.
- Finalize comprehensive data frames, export to csv, upload to data.world.
  - Assemble a data dictionary for data.world.
