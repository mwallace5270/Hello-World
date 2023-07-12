from pathlib import Path
import xarray
import cartopy.crs as ccrs
import cartopy  
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 


datadir = Path.home() / "Downloads" # Path.home() makes the code work for different users   


def read_vnp02(filename02): 
    # Open the dataset
    open_ds02 = xarray.open_dataset(datadir / filename02, group = "observation_data",) 
    list(open_ds02) 

    # Access the relavant variables 
    M03_ds = open_ds02['M03']  # blue light
    M04_ds = open_ds02['M04']  # green light  
    M05_ds = open_ds02['M05']  # red light
    M09_ds = open_ds02['M09']  # wavelength that water absorbs light
    M14_ds = open_ds02['M14']  # thermal infared wave length
    M14_BTL_ds = open_ds02['M14_brightness_temperature_lut']   
    M15_ds = open_ds02['M15'] # thermal infared wave length   
    M15_BTL_ds = open_ds02['M15_brightness_temperature_lut'] 
    M16_ds = open_ds02['M16'] # thermal infared wave length  
    M16_BTL_ds = open_ds02['M16_brightness_temperature_lut']   

    # Scale the relavent variables 
    M03_scaled = M03_ds * M03_ds.attrs['scale_factor'] + M03_ds.attrs['add_offset'] 
    M04_scaled = M04_ds * M04_ds.attrs['scale_factor'] + M04_ds.attrs['add_offset']  
    M05_scaled = M05_ds * M05_ds.attrs['scale_factor'] + M05_ds.attrs['add_offset']  
    M09_scaled = M09_ds * M09_ds.attrs['scale_factor'] + M09_ds.attrs['add_offset']

    # Divide the reflectances by the cosine of the solar zenith 
    cos_solzen = np.cos(solzen_ds) # degrees
    cos_solzen = np.radians(cos_solzen) # radians  

    # Divide the reflectances by the cosine of the solar zenith angle 
    M03_scaled = M03_scaled / cos_solzen 
    M04_scaled = M04_scaled / cos_solzen 
    M05_scaled = M05_scaled / cos_solzen 
    M09_scaled = M09_scaled / cos_solzen 

    # Convert to brightness temperature in K 
    M14_scaled = open_ds02['M14_brightness_temperature_lut'][open_ds['M14']] 
    M15_scaled = open_ds02['M15_brightness_temperature_lut'][open_ds['M15']] 
    M16_scaled = open_ds02['M16_brightness_temperature_lut'][open_ds['M16']] 

    # Check for the fill value  
    for value in open_ds02: 
        if value == 65535: # this is from the "_FillValue" variable in the dataset
            value = -999 



def map_vnp02(variable02_ds, lon_ds, lat_ds): 
    ax = plt.axes(projection = ccrs.PlateCarree())
    pc = ax.pcolormesh(lon_ds, lat_ds, variable02_ds) 
    ax.coastlines() 
    # Colorbar and lables  
    cb = plt.colorbar(pc, shrink=0.5) 
    pc.set_cmap('jet') # colors: https://matplotlib.org/stable/tutorials/colors/colormaps.html
    plt.show()
