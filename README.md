## Data Sources

Get [shapefiles from UCLA](https://cdmaps.polisci.ucla.edu/).

I've included the ones from the first congress, which is used in the example. But if you want anymore,
go and get them from the source above.

## Usage

- Setup a Python venv.
- Install the requirements in requirements.txt into it (for example: pip -r requirements.txt)
- Get the shapefiles from the source above, and extract the zip. 
- Run `python congmaps.py --shapefile <path to shapefile> --outfile <path to output file>`
- The output file will be in the same directory as the input file.

## Example

```shell
$ python congmaps.py --shapefile districtShapes/districts001.shp --outfile congress-districts.png
```

Should produce the file in the examples directory, shown here.

![Example](examples/1st_congress.png)



