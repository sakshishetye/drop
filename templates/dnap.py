# Python program to read
# json file


import json
from types import SimpleNamespace
import pdfkit 
from jinja2 import Template

tm = Template("Hello {{ name }}")


# JSON file
f = open ('try.json', "r")


# Reading from file
data = json.loads(f.read())
# config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin')


body = """
   <html>
    <head>
        <title> DNAP </title>
        <style>
            body {
                height: 1000px;
                width: 850px;
                margin-left: auto;
                margin-right: auto;
            }
            </style>
    </head>

    <body topmargin="50px" bottommargin="50px" leftmargin="50px" rightmargin="50px">

        <h1 style="text-align: center;"> TATA INSTITUTE OF FUNDAMENTAL RESEARCH </h1>
        <h2 style="text-align: center;"> <FONT COLOR="RED">Department of Nuclear Atomic Physics</FONT> </h2>
        <h1 style="text-align: center;"><FONT COLOR="BLUE"> SEMINAR</FONT> </h1>
        
        <P style="margin-left: 20px;">
        <table>
            <tr>
                <td style="width: 200px;"> 
                    <h3> Speaker</h3> 
                </td>
                <td style="width: 40px; text-align: center;"> 
                    <h3> : </h3> 
                </td>
                <td> 
                    <h3> MAIN_SPEAKER </h3> 
                </td>
            </tr>
            <tr>
                <td style="width: 200px;"> 
                    <h3>Title</h3> 
                </td>
                <td style="width: 40px; text-align: center;"> 
                    <h3> : </h3> 
                </td>
                <td>  
                    <h3> MAIN_TITLE</h3> 
                </td>
            </tr>
            <tr>
                <td style="width: 200px;"> 
                    <h3>  Date </h3> 
                </td>
                <td style="width: 40px; text-align: center;"> 
                    <h3> : </h3> 
                </td>
                <td> 
                    <h3> MAIN_DATE </h3>
                </td>
            </tr>
            <tr>
                <td style="width: 200px;"> 
                    <h3> Time </h3> 
                </td>
                <td style="width: 40px; text-align: center;"> 
                    <h3> : </h3> 
                </td>
                <td> 
                    <h3> MAIN_TIME </h3>
                </td>
            </tr>
            <tr>
                <td style="width: 200px;"> 
                    <h3> Venue</h3> 
                </td>
                <td style="width: 40px; text-align: center;"> 
                    <h3> : </h3> 
                </td>
                <td> 
                    <h3> MAIN_VENUE </h3>
                </td>
            </tr>
        </table>
        </p>

        <h2 > <I>Abstract</I> </h2>
        <p style="text-align: justify"> MAIN_DESCRIPTION </p>
        
        <h3 style="text-align: right; margin-top: 100px"> MAIN_ORGANIZER <br>  DNAP Office</h3>
    </body>
</html>    
"""


body=body.replace('MAIN_TITLE',data['results'][0]['title'])
body=body.replace('MAIN_DESCRIPTION',data['results'][0]['description'])
body=body.replace('MAIN_START_DATE_DATE',data['results'][0]['startDate']['date'])
body=body.replace('MAIN_START_DATE_TIME',data['results'][0]['startDate']['time'])
body=body.replace('MAIN_END_DATE_DATE',data['results'][0]['endDate']['date'])
body=body.replace('MAIN_END_DATE_TIME',data['results'][0]['endDate']['time'])
body=body.replace('MAIN_LOCATION',data['results'][0]['location'])
body=body.replace('MAIN_ORGANIZER',data['results'][0]['organizer'])
body=body.replace('MAIN_CREATION_DATE_DATE',data['results'][0]['creationDate']['date'])
body=body.replace('MAIN_CREATION_DATE_TIME',data['results'][0]['creationDate']['time'])
body=body.replace('MAIN_URL',data['url'])


pdfkit.from_string(body, 'dnap.pdf') #with --page-size=Legal and --orientation=Landscape
 
   
# Closing file
f.close()