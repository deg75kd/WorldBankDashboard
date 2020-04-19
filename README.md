# [World Bank Data Dashboard](https://deg75kd-wb.herokuapp.com)

## Table of Contents

* [Summary](#summary)
* [File Descriptions](#file-descriptions)
* [Prerequisites](#prerequisites)
* [Running the Code](#running-the-code)
* [Results](#results)
* [Built With](#built-with)
* [License](#license)

## Summary

This project was part of the Udacity Data Science Nanodegree.  It was the final project for the segment on Web Development.  The goal of the project was to first analyze from the World Bank and create three graphs depicting my findings.  Then I was required to build a web page to deliver these findings in a user-friendly manner.

## File Descriptions

* myapp.py - Runs the web page server
* Procfile - Indicates use of gunicorn on Heroku
* requirements.txt - Package requirements to be installed on Heroku
* data/*.csv - CSV files downloaded from the World Bank web site
* myapp/__init__.py - Runs the Flask web application
* myapp/routes.py - Renders the web pages
* myapp/static/img/githublogo.png - GitHub logo
* myapp/static/img/linkedinlogo.png - LinkedIn logo
* myapp/templates/index.html - Web page that displays graphics
* wrangling_scripts/wrangle_data_project.py - Python scripts for creating graphs

## Prerequisites

Flask 1.1.1\
gunicorn 20.0.4\
itsdangerous 1.1.0\
Jinja2 2.10\
MarkupSafe 1.1.1\
numpy 1.18.1\
pandas 0.25.3\
plotly 4.4.1\
python 3.6\
Werkzeug 0.16.0\

## Running the Code

To start the web application, run the following.  *This was developed in a Linux environment and will not work on a Windows machine.*
```
python myapp.py
```

## Results

With Bootstrap I was able to create a web page with a header bar with links, a side bar with images that link to external pages and three graphs in two rows.

I used Plotly to generate three different types of graphs.  The first is a line graph of internet users for several regions over a period of time.  The second is a bar graph of the total population of those regions in 2014.  The third is a double bar graph comparing the female youth illiteracy rate to the female lower secondary enrollment rate.

## Built With

* [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/#starter-template) - CSS framework
* [Plotly](https://cdn.plot.ly/plotly-latest.min.js) - API for generating graphs
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Python-based Web framework
* [Heroku](https://www.heroku.com/) - Web hosting service

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)
