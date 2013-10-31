U-report National Pulse
=======================

========
Overview
========

The National Pulse on Ureport is a public web interface on ureport that displays Geo-tagged text messages from u-reporters mapped against their respective locations.

The messages are initially categorized into seven categories that each have a static color assigned to it(These categories and colors have been chosen by the U-report Management, they are not to be questioned). On the Geochart(Map), political region is colored with the most dominant category color.

For example:

    "Uganda is divided into 112 political regions referred to as districts. From each text received from each district and a text analytics system classifies text into one of the seven categories, for each district, texts per category are counted and the category that has the most texts gets to color that region on the map.
    
    A clear example on this can be seen here at the `Uganda National Pulse <http://ureport.ug/national-pulse>`_ "

The National Pulse is further categorized into periodic groups which include;

    - The Daily National Pulse:
        - This one displays the geo-tagged conversation on U-report in the previous 24 hours from the moment you check it out
    - The Monthly National Pulse:
        - This one displays the geo-tagged conversation on U-report with in the previous 30 days from the moment you check it out.
    - The Annual National Pulse:
        - This one displays the geo-tagged conversation on U-report within the previous 365 days


============
How it works
============
The Map
^^^^^^^
This chart maps the most dominant category in a specific location. When a location is selected on the chart. A link will appear on the top of the chart that will let one select to load a word cloud of the selected region. This word cloud is of the messages that have been texted in by U-reporters from the selected region.

The Pie Chart
^^^^^^^^^^^^^
This shows distribution of message categories in a selected region. If no region in selected, the pie chart show distribution of these categories national wide. When you select on a specific category in the pie chart. A link will appear above it that you can optionally click on to see a word cloud of messages that fall within that category. Real counts of the messages also is shown when a specific category on the chart is hovered over.


===============
The Ingredients
===============

National Pulse is basically a visualisation of text data mapped against the location from which this data is from.
This data is calculated within the core U-report application and fed into the National Pulse using two separate JSON files;

(i) A geojson file that includes all region locations including the gor-coordinates of the specific region.
(ii) The data file that includes the text counts, categories and the locations from which the texts are from.


================
How it's created
================

The visualisation of the data is basically drawn using the `Dimensional Charting Javascript Library(dc.js) <http://nickqizhu.github.io/dc.js/>`_ and `Data-Driven Documents(d3.js) <http://d3js.org/>`_


The Map
^^^^^^^
This is drawn using the `Geo Choropleth Chart <https://github.com/NickQiZhu/dc.js/blob/master/web/docs/api-1.6.0.md#geo-choropleth-chart>`_. You can follow the link to check out the documentation.
This takes both the geojson and data files, using a KeyAccessor(`Checkout Documentation <https://github.com/NickQiZhu/dc.js/blob/master/web/docs/api-1.6.0.md#geo-choropleth-chart>`_). We give the chart the most dominant category as the keyAccessor which is used to determine the color of the region on the chart.

The Pie Chart
^^^^^^^^^^^^^
This is drawn using the `Pie Chart <https://github.com/NickQiZhu/dc.js/blob/master/web/docs/api-1.6.0.md#pie-chart>`_ with same data source as the map. With the dc.js api, this makes the Pie Chart responsive to events triggered on the map. Hence making it change variables when specific regions are selected on the map.

The Word Cloud
^^^^^^^^^^^^^^
The word cloud is generated and displayed using core U-report tools. This is drawn from a list of words that appear most frequently in the text messages of the region or category selected to display a word cloud for.

Relevant Links
^^^^^^^^^^^^^^
`Sample Pulse JSON Data <http://ureport.ug/pulse/>`_

`GeoJson for Uganda Districts <http://ureport.ug/static/ureport/data/districts.json>`_

