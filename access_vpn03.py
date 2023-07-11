from pathlib import Path
import xarray
import cartopy.crs as ccrs
import cartopy  
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 


datadir = Path.home() / "Downloads" # Path.home() makes the code work for different users  


def read_vnp03(filename03):     
    # Open the file & make it a dataset
    open_ds = xarray.open_dataset(datadir / filename03, group = "geolocation_data",) 
    list(open_ds) 

    # Access the relavant variables 
    height_ds = open_ds['height']  
    lwm_ds = open_ds['land_water_mask']   
    lat_ds = open_ds['latitude']   
    lon_ds = open_ds['longitude']  
    senazi_ds = open_ds['sensor_azimuth']  
    senzen_ds = open_ds['sensor_zenith']   
    solazi_ds = open_ds['solar_azimuth']   
    solzen_ds = open_ds['solar_zenith']    

    # The variables should not need to be scaled/offset because xarray 
    # does that automatically. 
    
    # Extra: Read the long_names
    height_long = height_ds.attrs['long_name']
    lwm_long = lwm_ds.attrs['long_name']
    lat_long = lat_ds.attrs['long_name']
    lon_long = lon_ds.attrs['long_name'] 
    senazi_long = senazi_ds.attrs['long_name']
    senzen_long = senzen_ds.attrs['long_name']
    solazi_long = solazi_ds.attrs['long_name']
    solzen_long = solzen_ds.attrs['long_name']     


def map_vnp03(variable_ds03, variable03_long, lon_ds, lat_ds): 
    ax = plt.axes(projection = ccrs.PlateCarree())
    pc = ax.pcolormesh(lon_ds, lat_ds, variable03_ds) 
    # Pass the longname as the title
    ax.set_title(variable03_long)
    # Colorbar and lables  
    cb = plt.colorbar(pc, shrink=0.5)  
    plt.show()