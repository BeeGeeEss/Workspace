"""Option one for library"""

from kerykeion import AstrologicalSubject, KerykeionChartSVG, Report

# # Create an instance of the AstrologicalSubject class.
# # Arguments: Name, year, month, day, hour, minutes, city, nation
subject = AstrologicalSubject(
     name="Brando",
     year=1991,
     month=2,
     day=8,
     hour=8,
     minute=30,
     lat=-34.206907,
     lng=142.136694,
     tz_str="Australia/Melbourne",
     city="Mildura, Australia")

# # Retrieve information about the Sun:
subject.sun
# > {'name': 'Sun', 'quality': 'Mutable', 'element': 'Air', 'sign': 'Gem', 'sign_num': 2, ...}

# # Retrieve information about the first house:
subject.first_house
# # > {'name': 'First_House', 'quality': 'Cardinal', 'element': 'Water', 'sign': 'Can', ...}

# # Retrieve the element of the Moon sign:
subject.moon.element
# # > 'Water'

print(subject.moon)



John = AstrologicalSubject()
birth_chart_svg = KerykeionChartSVG(John, new_output_directory="/home/beegeeess/GitHome/Workspace/App-Project/generated_SVGs")
birth_chart_svg.makeSVG()


John = AstrologicalSubject(John)
report = Report(John)
report.print_report()



"""Option 2 for libraries"""

from natal import Data, Chart, Stats 
from natal_report import Report

# create chart data object
mimi = Data(
    name="MiMi",
    utc_dt="1980-04-20 06:30",
    lat=25.0531,
    lon=121.526,
)

# return natal chart in SVG string
Chart(mimi, width=600).svg

# create transit data object
transit = Data(
    name="Transit",
    utc_dt="2024-01-01 05:30",
    lat=25.0531,
    lon=121.526,
)

# create a transit chart
transit_chart = Chart(
    data1=mimi, 
    data2=transit, 
    width=600
)

# view the composite chart in jupyter notebook
# from IPython.display import HTML

# HTML(transit_chart.svg)

report = Report(data1=mimi, data2=transit)
html = report.full_report
bytes_io = report.create_pdf(html)

with open("demo_report_mono.pdf", "wb") as f:
    f.write(bytes_io.getbuffer())