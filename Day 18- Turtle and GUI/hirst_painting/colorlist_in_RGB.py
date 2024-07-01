rgb_values = [
    "Rgb(r=245, g=243, b=238)", "Rgb(r=246, g=242, b=244)", "Rgb(r=202, g=164, b=110)",
    "Rgb(r=240, g=245, b=241)", "Rgb(r=236, g=239, b=243)", "Rgb(r=149, g=75, b=50)",
    "Rgb(r=222, g=201, b=136)", "Rgb(r=53, g=93, b=123)", "Rgb(r=170, g=154, b=41)",
    "Rgb(r=138, g=31, b=20)", "Rgb(r=134, g=163, b=184)", "Rgb(r=197, g=92, b=73)",
    "Rgb(r=47, g=121, b=86)", "Rgb(r=73, g=43, b=35)", "Rgb(r=145, g=178, b=149)",
    "Rgb(r=14, g=98, b=70)", "Rgb(r=232, g=176, b=165)", "Rgb(r=160, g=142, b=158)",
    "Rgb(r=54, g=45, b=50)", "Rgb(r=101, g=75, b=77)", "Rgb(r=183, g=205, b=171)",
    "Rgb(r=36, g=60, b=74)", "Rgb(r=19, g=86, b=89)", "Rgb(r=82, g=148, b=129)",
    "Rgb(r=147, g=17, b=19)", "Rgb(r=27, g=68, b=102)", "Rgb(r=12, g=70, b=64)",
    "Rgb(r=107, g=127, b=153)", "Rgb(r=176, g=192, b=208)", "Rgb(r=168, g=99, b=102)"
]

# Convert the RGB strings to tuples and store in the 'color' list
color = []
for rgb_string in rgb_values:
    # Extract the numeric values for r, g, b using regular expressions
    import re
    r, g, b = map(int, re.findall(r'\d+', rgb_string))
    color.append((r, g, b))
