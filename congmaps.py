import argparse
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.feature import ShapelyFeature
from cartopy.io.shapereader import Reader
import matplotlib.pyplot as plt


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--shapefile', type=str, help='Path to shapefile')
    parser.add_argument('--outfile', type=str, help='Path to output file')
    parser.add_argument('--scale', type=int, default=600, help='Scale of output (bigger is more pixels)')
    return parser.parse_args()

def make_fig(shapefile: str, outfile: str, scale: int):
    _, ax = plt.subplots(subplot_kw=dict(projection=ccrs.PlateCarree()), dpi=scale)

    # Coordinates are bounding box of US48 (sorry Alaksa + Hawaii)
    ax.set_extent([-125, -66, 24, 49])

    # Remove the borders
    ax.axis('off')

    # Draw the coastlines
    ax.coastlines(color='black', linewidth=0.3, resolution='10m')
    ax.add_feature(cfeature.BORDERS.with_scale('10m'),
                linestyle='-', alpha=.5, linewidth=0.3)

    border_feature = ShapelyFeature(Reader(shapefile).geometries(),
                                crs=ccrs.PlateCarree(), edgecolor='b')
    ax.add_feature(border_feature, facecolor='none', edgecolor='r', linewidth=0.1)
    plt.savefig(outfile, format=outfile.split('.')[1])

def main():
    args = parse_args()
    make_fig(args.shapefile, args.outfile, args.scale)

if __name__ == '__main__':
    main()