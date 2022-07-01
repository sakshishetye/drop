# Python program to read
# json file


import json
from types import SimpleNamespace
import pdfkit


# JSON file
f = open ('try.json', "r")


# Reading from file
data = json.loads(f.read())
# config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin')


body = """
   <html>
    <head>
        <title> tifr</title>
        <style>
        h2{
            background-color:grey;
            color:black;

        }
            body {
                height: 1000px;
                width: 850px;
                margin-left: auto;
                margin-right: auto;
                }
            </style>
    </head>

    <body topmargin="50px" bottommargin="50px" leftmargin="50px" rightmargin="50px">
   <center> <h1><b><u>TATA INSTITUTE OF FUNDAMENTAL RESEARCH</b></u></h1> </center>
   <center><h2><big>Chemical Sciences Seminar</big></h2></center>
   
        <P style="margin-left: 20px;">
        <table>
            <tr>
                <td style="width: 200px;"> 
                    <h3> Title </h3> 
                </td>
                <td style="width: 40px; text-align: center;"> 
                    <h3> : </h3> 
                </td>
                <td> 
                    <h3> MAIN_TITLE </h3> 
                </td>
            </tr>
            <tr>
                <td style="width: 200px;"> 
                    <h3> url </h3> 
                </td>
                <td style="width: 40px; text-align: center;"> 
                    <h3> : </h3> 
                </td>
                <td>  
                    <h3> MAIN_URL </h3> 
                </td>
            </tr>
            <tr>
                <td style="width: 200px;"> 
                    <h3> Start Date & Time </h3> 
                </td>
                <td style="width: 40px; text-align: center;"> 
                    <h3> : </h3> 
                </td>
                <td> 
                    <h3> MAIN_START_DATE_DATE at MAIN_START_DATE_TIME </h3>
                </td>
            </tr>
            <tr>
                <td style="width: 200px;"> 
                    <h3> End Date & Time </h3> 
                </td>
                <td style="width: 40px; text-align: center;"> 
                    <h3> : </h3> 
                </td>
                <td> 
                    <h3> MAIN_END_DATE_DATE at MAIN_END_DATE_TIME </h3>
                </td>
            </tr>
            <tr>
                <td style="width: 200px;"> 
                    <h3> Location </h3> 
                </td>
                <td style="width: 40px; text-align: center;"> 
                    <h3> : </h3> 
                </td>
                <td> 
                    <h3> MAIN_LOCATION </h3>
                </td>
            </tr>
        </table>
        </p>

        <h3> <u> Abstract: </u> </h3>
        <h3 style="text-align: justify"> MAIN_DESCRIPTION </h3>
        
        <h3 style="text-align: right; margin-top: 100px"> MAIN_ORGANIZER <br> (Organizer, ASET Forum) </h3>
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


pdfkit.from_string(body, 'DCS.pdf') #with --page-size=Legal and --orientation=Landscape
 
   
# Closing file
f.close()