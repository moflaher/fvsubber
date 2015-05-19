import sys
import shutil
import os
from datetime import datetime,timedelta


def build_name(runvalues,looplist,dates,date):
    changes=[]
    name_changes=[]
    for i,key in enumerate(runvalues):
        if len(runvalues[key])>1:
            changes+=[i]
            name_changes+=[key]

    mystr=''
    for val in changes:
        mystr+='_'+str(looplist[val])
    foldername=date+'_'+dates[date]+mystr

    return foldername,name_changes


def copy_create(runvalues,looplist,dates,date,copypath,outpath):
    
    #add slashes to path if they were not included
    if copypath[-1]!='/':
        copypath+='/'
    if outpath[-1]!='/':
        outpath+='/'


    foldername,name_changes=build_name(runvalues,looplist,dates,date)
    shutil.copytree(copypath+runvalues['CASE_TITLE'], outpath+foldername )

    #remove 3days for spin up
    startdate_num=datetime.strptime(date,"%Y-%m-%d")-timedelta(days=3)
    startdate=datetime.strftime(startdate_num,"%Y-%m-%d")


    top = '''
     !================================================================!
       _______  _     _  _______  _______  _______  ______     _____
      (_______)(_)   (_)(_______)(_______)(_______)(_____ \   (_____)
       _____    _     _  _        _     _  _  _  _  _____) )  _  __ _
      |  ___)  | |   | || |      | |   | || ||_|| |(_____ (  | |/ /| |
      | |       \ \ / / | |_____ | |___| || |   | | _____) )_|   /_| |
      |_|        \___/   \______) \_____/ |_|   |_|(______/(_)\_____/
      -- Beta Release
     !                                                                !
     !========DOMAIN DECOMPOSITION USING: METIS 4.0.1 ================!
     !======Copyright 1998, Regents of University of Minnesota========!
     !                                                                !


     &NML_CASE
     CASE_TITLE      = '{}'
     TIMEZONE        = '{}',
     DATE_FORMAT     = '{}'
     START_DATE      = '{} 00:00:00'
     END_DATE        = '{} 00:00:00'
     /
     
     &NML_STARTUP
     STARTUP_TYPE      = '{}'
     STARTUP_FILE      = '{}'
     STARTUP_UV_TYPE   = '{}'
     STARTUP_TURB_TYPE = '{}'
     STARTUP_TS_TYPE   = '{}'
     STARTUP_T_VALS    = {}
     STARTUP_S_VALS    = {}
     STARTUP_DMAX      = {}
     /

     &NML_IO
     INPUT_DIR       =  './input/'
     OUTPUT_DIR      =  './output'
     IREPORT         = {},
     VISIT_ALL_VARS  = {},
     WAIT_FOR_VISIT  = {},
     USE_MPI_IO_MODE = {}
     /

     &NML_INTEGRATION
     EXTSTEP_SECONDS =  {},
     ISPLIT          =  {}
     IRAMP           =  {}
     MIN_DEPTH       =  {}
     STATIC_SSH_ADJ  =  {}
     /

     &NML_RESTART
     RST_ON  = {},
     RST_FIRST_OUT      = '{} 00:00:00'
     RST_OUT_INTERVAL   = '{}'
     RST_OUTPUT_STACK   = {}
     /

     &NML_NETCDF
     NC_ON           = {},
     NC_FIRST_OUT    = '{}  00:00:00',
     NC_OUT_INTERVAL = '{}',
     NC_OUTPUT_STACK = {},
     NC_GRID_METRICS = {},
     NC_VELOCITY     = {},
     NC_SALT_TEMP    = {},
     NC_TURBULENCE   = {},
     NC_AVERAGE_VEL  = {},
     NC_VERTICAL_VEL = {},
     NC_WIND_VEL     = {},
     NC_WIND_STRESS  = {},
     NC_EVAP_PRECIP  = {},
     NC_SURFACE_HEAT = {},
     NC_GROUNDWATER  = F
     /

     &NML_NETCDF_AV
     NCAV_ON                 = {},
     NCAV_FIRST_OUT          = '{}'
     NCAV_OUT_INTERVAL       = {},
     NCAV_OUTPUT_STACK       = {},
     NCAV_GRID_METRICS       = {},
     NCAV_FILE_DATE          = {},
     NCAV_VELOCITY           = {},
     NCAV_SALT_TEMP          = {},
     NCAV_TURBULENCE         = {},
     NCAV_AVERAGE_VEL        = {},
     NCAV_VERTICAL_VEL       = {},
     NCAV_WIND_VEL           = {},
     NCAV_WIND_STRESS        = {},
     NCAV_EVAP_PRECIP        = {},
     NCAV_SURFACE_HEAT       = {},
     NCAV_GROUNDWATER        = {},
     NCAV_BIO                = {},
     NCAV_WQM                = {},
     NCAV_VORTICITY          = {}
    /

     &NML_SURFACE_FORCING
     WIND_ON             = {},
     HEATING_ON          = {},
     PRECIPITATION_ON    = {},
     /

     &NML_PHYSICS
     HORIZONTAL_MIXING_TYPE          = '{}'
     HORIZONTAL_MIXING_KIND          = '{}'
     HORIZONTAL_MIXING_COEFFICIENT   = {}
     HORIZONTAL_PRANDTL_NUMBER       = {}
     VERTICAL_MIXING_TYPE            = '{}'
     VERTICAL_MIXING_COEFFICIENT     = {},
     VERTICAL_PRANDTL_NUMBER         = {}
     BOTTOM_ROUGHNESS_MINIMUM        = {} 
     BOTTOM_ROUGHNESS_LENGTHSCALE    = {}
     BOTTOM_ROUGHNESS_KIND           = '{}'
     BOTTOM_ROUGHNESS_TYPE           = '{}'
     CONVECTIVE_OVERTURNING          = {},
     SCALAR_POSITIVITY_CONTROL       = {},
     BAROTROPIC                      = {},
     BAROCLINIC_PRESSURE_GRADIENT    = '{}'
     SEA_WATER_DENSITY_FUNCTION      = '{}'
     RECALCULATE_RHO_MEAN            = {}
     INTERVAL_RHO_MEAN               = '{}'
     TEMPERATURE_ACTIVE              = {},
     SALINITY_ACTIVE                 = {},
     SURFACE_WAVE_MIXING             = {},
     WETTING_DRYING_ON               = {}
     /

     &NML_RIVER_TYPE
     RIVER_NUMBER   = {},
     /

     &NML_OPEN_BOUNDARY_CONTROL
     OBC_ON                      = {},
     OBC_NODE_LIST_FILE          = '{}'
     OBC_ELEVATION_FORCING_ON    = {},
     OBC_ELEVATION_FILE          = '{}'
     OBC_TS_TYPE                 = {}
     OBC_TEMP_NUDGING            = {},
     OBC_TEMP_FILE               = '{}'
     OBC_TEMP_NUDGING_TIMESCALE  = {},
     OBC_SALT_NUDGING            = {},
     OBC_SALT_FILE               = '{}'
     OBC_SALT_NUDGING_TIMESCALE  = {},
     OBC_MEANFLOW                = {},
    /

     &NML_GRID_COORDINATES
     GRID_FILE              = '{}'
     GRID_FILE_UNITS        = '{}'
     PROJECTION_REFERENCE   = '{}'
     SIGMA_LEVELS_FILE      = '{}'
     DEPTH_FILE             = '{}'
     CORIOLIS_FILE          = '{}'
     SPONGE_FILE            = '{}'
     BFRIC_FILE             = '{}'
     VVCOE_FILE             = '{}'
    /

     &NML_GROUNDWATER
     GROUNDWATER_ON         = {},
     GROUNDWATER_FLOW       = {},
     GROUNDWATER_FILE       = '{}'
     /

     &NML_LAG
     LAG_PARTICLES_ON = {},
     LAG_START_FILE   = '{}'
     LAG_OUT_FILE     = '{}'
     LAG_RESTART_FILE = '{}'
     LAG_OUT_INTERVAL = {},
     LAG_SCAL_CHOICE  = '{}'
     /

     &NML_ADDITIONAL_MODELS
     DATA_ASSIMILATION       = {},
     BIOLOGICAL_MODEL        = {},
     SEDIMENT_MODEL          = {},
     SEDIMENT_PARAMETER_TYPE = '{}'
     SEDIMENT_MODEL_FILE     = '{}'
     ICING_MODEL             = {},
     ICE_MODEL               = {},
     /

    &NML_PROBES
    PROBES_ON     = {},
    PROBES_NUMBER = {},
    PROBES_FILE   = '{}',
    /

    &NML_TURBINE
    TURBINE_ON   = {},
    TURBINE_FILE = '{}'
    /

    &NML_NESTING
    NESTING_ON = {}
    /

    &NML_NCNEST
    NCNEST_ON = {}
    /

    &NML_BOUNDSCHK
    BOUNDSCHK_ON  = {}
    /

    &NML_STATION_TIMESERIES
    OUT_STATION_TIMESERIES_ON   = {},
    STATION_FILE                = '{}'
    LOCATION_TYPE               = '{}'
    OUT_ELEVATION               = {},
    OUT_VELOCITY_3D             = {},
    OUT_VELOCITY_2D             = {},
    OUT_SALT_TEMP               = {},
    OUT_WIND_VELOCITY           = {},
    OUT_INTERVAL                = '{}',
    OUT_START_DATE              = '{}'
     /

    '''.format(looplist[0:3],startdate,dates[date],looplist[3:23],date,looplist[23:],date)
    #change format to add all values

    top = top.split('\n')

    #save run folder
    outputFile = outpath+foldername+"/{0}_run.nml".format(gridName)
    print outputFile
    with open(outputFile, 'w') as f:
        for t in top:
            print >> {}, t

    #save file with variables changed
    outputFile2 = outpath+foldername+"/variables_changed"
    print outputFile
    with open(outputFile2, 'w') as f:
        for item in name_changes:
            print >> {}, item

    return foldername


