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
        <title>TIFR</title>
        <style>
        <body> {
            height: 1000px;
            width: 850px;
            }
            </style>
    </head>
    <body topmargin="30px" bottommargin="30px" leftmargin="50px" rightmargin="50px">
    <h1 style="text-align: center;">TATA INSTITUTE OF FUNDAMENTAL RESEARCH</h1>
    <h2 style="text-align: center;">CONDENSED MATTER PHYSICS AND MATERIALS</h2>
    <h1 style="text-align:center;">Science Seminar</h1>
    <p style="margin-left: 20px;">
          <table>
            <tr>
            <td style="width: 50px;",colspan="2"> 
                <h3 style="color:black;">Title</h3>
                </td>
                <td style="width: 10px; text-align: center;"> 
                    <h3 style="color:black;">:</h3> 
                </td>
                <td> 
                    <h3><p style="color:black;">MAIN_TITLE</p> </i> </h3> </td>
            </tr>
            <tr>
                <td style="width: 100px;",colspan="2"> 
                    <h3><p style="color:black;">Start Date</p></h3> 
                </td>
                <td style="width: 40px; text-align: center;"> 
                    <h3><p style="color:black;">:</p></h3> 
                </td>
                <td> 
                    <h3><p style="color:black;">MAIN_START_DATE</p></h3>
                </td>
            </tr>
            <tr>
                <td style="width: 100px;",colspan="2"> 
                    <h3><p style="color:black;">End Date</p></h3> 
                </td>
                <td style="width: 40px; text-align: center;"> 
                    <h3><p style="color:black;">:</p> </h3> 
                </td>
                <td> 
                    <h3><p style="color:black;">MAIN_END_DATE</p></h3>
                </td>
            </tr>
            <tr>
                <td style="width: 60px;",colspan="2"> 
                    <h3 ><p style="color:black;">Link</p></h3> 
                </td>
                <td style="width: 20px; text-align: center;"> 
                    <h3><p style="color:black;">:</p></h3> 
                </td>
                <td> 
                    <h3><i>MAIN_ADDRESS</i></h3>
                </td>
            </tr>
            <tr>
                <td style="width: 100px;",colspan="2"> 
                    <h3><p style="color:black;">Location</p></h3> 
                </td>
                <td style="width: 40px; text-align: center;"> 
                    <h3><p style="color:black;">:</p></h3> 
                </td>
                <td> 
                    <h3><p style="color:black;">MAIN_LOCATION</p></h3>
                </td>
            </tr>
        </table>
    </p>
    <h2 style="text-align:left;"><i>Abstract</i></h2> 
    <h3><p style="color:brown;">MAIN_DESCRIPTION</p></h3>
    <td>  
    <h3 style="text-align:right">MAIN_ORGANIZER</h3>
    </td>
</body>
</html>    
"""
body=body.replace('MAIN_TITLE',data['results'][0]['title'])
body=body.replace('MAIN_DESCRIPTION',data['results'][0]['description'])
body=body.replace('MAIN_START_DATE',data['results'][0]['startDate']['date'])
body=body.replace('MAIN_END_DATE',data['results'][0]['endDate']['date'])
body=body.replace('MAIN_LOCATION',data['results'][0]['location'])
body=body.replace('MAIN_ADDRESS',data['results'][0]['address'])
body=body.replace('MAIN_ORGANIZER',data['results'][0]['organizer'])

pdfkit.from_string(body, 'DCMP.pdf') #with --page-size=Legal and --orientation=Landscape
   
# Closing file
f.close()