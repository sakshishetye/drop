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
        <title> DHEP Notice Layout </title>
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
        
        <h3 style="text-align: center; margin-top: 50px"> High Energy Physics Seminar </h3>
        
        <P style="top-left: 50px;">
        <table>
            <tr>
                <td style="width: 200px;"> 
                    Start Date & Time: 
                </td>
                <td> 
                    MAIN_START_DATE_DATE at MAIN_START_DATE_TIME
                </td>
            </tr>
            <tr>
                <td style="width: 200px;"> 
                    End Date & Time: 
                </td>
                <td> 
                    MAIN_END_DATE_DATE at MAIN_END_DATE_TIME
                </td>
            </tr>
            <tr>
                <td style="width: 200px;"> 
                    url: 
                </td>
                <td>  
                    MAIN_URL
                </td>
            </tr>
            <tr>
                <td style="width: 200px;"> 
                    Location:
                </td>
                <td> 
                    MAIN_LOCATION
                </td>
            </tr>
            <tr>
                <td style="width: 200px;"> 
                    Title: 
                </td>
                <td> 
                    MAIN_TITLE
                </td>
            </tr>
        </table>
        </p>

        <p> <i> Description: </i> </p>
        <p style="text-align: justify;"> MAIN_DESCRIPTION </p>
        
        <h3 style="text-align: right; margin-top: 100px"> MAIN_ORGANIZER <br> (Organizer, DHEP Forum) </h3>
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
body=body.replace('MAIN_URL',data['url'])


pdfkit.from_string(body, 'DHEP.pdf') #with --page-size=Legal and --orientation=Landscape
 
   
# Closing file
f.close()