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
        <title>TIFR</title>
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
    <h1 style="text-align: center;"style="text-align: center;">TATA INSTITUTE OF FUNDAMENTAL RESEARCH</h1>
    <b><h3 style="text-align: center;">Homi Bhaba Road,Mumbai-400 005</h3></b>
    <h3 style="text-align:right;"><b>June 9,2022</b></h3>
    <h2 style="text-align: center;"><p style="background-color:blue;color:white">Department Of Theoretical Physics</p></h2>
    <h3 style="text-align: center;"><p style="color:red;">ASET Colloquium</p></h3>
    <p style="margin-left: 20px;">

      <table> 
            <tr>
                <td style="width: 100px;",colspan="2"> 
                <h3 style="color:blue;">Title</h3>
                </td>
                <td style="width: 40px; text-align: center;"> 
                    <h3 style="color:blue;">:</h3> 
                </td>
                <td> 
                    <h3><p style="color:blue;">MAIN_TITLE</p> </i> </h3> </td>
            </tr>
            <tr>
                <td style="width: 60px;",colspan="2"> 
                    <h3 ><p style="color:blue;">Link</p></h3> 
                </td>
                <td style="width: 20px; text-align: center;"> 
                    <h3><p style="color:blue;">:</p></h3> 
                </td>
                <td> 
                    <h3><p style="color:blue;">MAIN_ADDRESS</p></h3>
                </td>
            </tr>
          
            <tr>
                <td style="width: 100px;",colspan="2"> 
                    <h3><p style="color:blue;">Start Date</p></h3> 
                </td>
                <td style="width: 40px; text-align: center;"> 
                    <h3><p style="color:blue;">:</p></h3> 
                </td>
                <td> 
                    <h3><p style="color:blue;">MAIN_START_DATE<p style="color:blue;"></h3>
                </td>
            </tr>
            <tr>
                <td style="width: 100px;",colspan="2"> 
                    <h3><p style="color:blue;">End Date</p></h3> 
                </td>
                <td style="width: 40px; text-align: center;"> 
                    <h3><p style="color:blue;">:</p> </h3> 
                </td>
                <td> 
                    <h3><p style="color:blue;">MAIN_END_DATE</p></h3>
                </td>
            </tr>
            <tr>
                <td style="width: 100px;",colspan="2"> 
                    <h3><p style="color:blue;">Location</p></h3> 
                </td>
                <td style="width: 40px; text-align: center;"> 
                    <h3><p style="color:blue;">:</p></h3> 
                </td>
                <td> 
                    <h3><p style="color:blue;">MAIN_LOCATION</p></h3>
                </td>
            </tr>
        </table>
        </p>

            <tr>
                <td >   
                </td>
                <td >
                </td>
                <td> 
                 <h2 style="text-align:left;"><p style="color:brown;"><i>Abstract</i></p></h2> 
                 <h3><p style="color:brown;">MAIN_DESCRIPTION</p></h3>
                </td>
            </tr>
              <tr>
                <td style="width:60px;"> 
                    <h3 style="color:red;"> </h3> 
                </td>
                <td> 
                    <h3 style="color:brown;"> </h3>
                </td>
                <td> 
                    <h3 style="text-align:right"><p style="color:brown;">Organizer</p></h3> 
                    <h3 style="text-align:right"><p style="color:brown;">MAIN_ORGANIZER</p></h3>
                </td>
            </tr>
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

pdfkit.from_string(body, 'DTP.pdf') #with --page-size=Legal and --orientation=Landscape
   
# Closing file
f.close()