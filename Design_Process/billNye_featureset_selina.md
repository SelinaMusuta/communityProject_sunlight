DOC: billNye_featureset.md
AUTHOR and PROJECT LEAD:  Selina Musuta
DESCRIPTION: Many organizations have bill tracking pages with static information about legislation they care about. Using the data from Open States and OpenCongress, fellows will develop a bill tracker that provides updated and relevant information about the selected bills such as bill name, number, sponsors, status, and summary.

Feature Set
=============================

Description: In this feature set, we will list out the major sections of this iframe feature.  (iframe will be used to display updated and relevant information concerning bills).

so here it goes....

Design, Develop, Test, Deploy a web app that makes API calls:

Back-End::

(1)Makes API calls to Open Congress and Open States with parameters set by the user
(2)The user receives the results from the API request and slice out/up the data you want to display (backend)

Front-End::
(1) The data from the API request will be displayed on the front-end through an HTML template
(2)	Determine the sizes of the frame (maybe 300 width and 300 height)
(3)	Style the template(s) for the iframe 

Back-End::
(1)	Allows users click through to new "windows"/frames or actions if necessary 