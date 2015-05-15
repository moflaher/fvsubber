import sys
import shutil
import os

arguments = sys.argv

gridName = arguments[1]
timenum = int(arguments[2])
drag= int(arguments[3])

filepath="/home/moflaher/scratch/minaspassage/smallcape_force/"
start_dates=['2013-08-17', '2011-10-30','2011-08-12', '2010-07-11', '2009-01-28', '2008-08-17','2008-04-29', '2012-08-25','2012-06-03']
end_dates  =['2013-10-24', '2011-12-11','2011-11-03', '2010-08-22', '2009-03-02', '2008-09-24','2008-07-10', '2012-10-23','2012-08-29']

start_dates=['2011-10-30','2011-08-12']
end_dates  =['2011-12-11','2011-11-03']

drag_list=['0.0025']

shutil.copytree(filepath+"smallcape_force_2d_clean", filepath+("%s"%start_dates[timenum])+"_"+ ("%s"%end_dates[timenum]) )


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
 CASE_TITLE      = '{0}'
 TIMEZONE        = 'UTC',
 DATE_FORMAT     = 'YMD'
 START_DATE      = '{1} 00:00:00'
 END_DATE        = '{2} 00:00:00'
 /
 
 &NML_STARTUP
 STARTUP_TYPE      = 'coldstart'
 STARTUP_FILE      = 'none'
 STARTUP_UV_TYPE   = 'default'
 STARTUP_TURB_TYPE = 'default'
 STARTUP_TS_TYPE   = 'constant'
 STARTUP_T_VALS    = 18
 STARTUP_S_VALS    = 35.0
 STARTUP_DMAX      =  -10.0
 /

 &NML_IO
 INPUT_DIR       =  './input/'
 OUTPUT_DIR      =  './output'
 IREPORT         =  720,
 VISIT_ALL_VARS  = F,
 WAIT_FOR_VISIT  = F,
 USE_MPI_IO_MODE = F
 /

 &NML_INTEGRATION
 EXTSTEP_SECONDS =  0.5,
 ISPLIT          =  1
 IRAMP           =  34560
 MIN_DEPTH       =  0.5
 STATIC_SSH_ADJ  =  0.0
 /

 &NML_RESTART
 RST_ON  = T,
 RST_FIRST_OUT      = '{1} 00:00:00'
 RST_OUT_INTERVAL   = 'days = 1.0'
 RST_OUTPUT_STACK   =           0
 /

 &NML_NETCDF
 NC_ON   = T,
 NC_FIRST_OUT    = '{1} 00:00:00',
 NC_OUT_INTERVAL =  'seconds=600.0',
 NC_OUTPUT_STACK =  0,
 NC_GRID_METRICS = T,
 NC_VELOCITY     = F,
 NC_SALT_TEMP    = F,
 NC_TURBULENCE   = F,
 NC_AVERAGE_VEL  = T,
 NC_VERTICAL_VEL = F,
 NC_WIND_VEL     = F,
 NC_WIND_STRESS  = F,
 NC_EVAP_PRECIP  = F,
 NC_SURFACE_HEAT = F,
 NC_GROUNDWATER = F
 /

 &NML_NETCDF_AV
 NCAV_ON = F,
 NCAV_FIRST_OUT  = 'none'
 NCAV_OUT_INTERVAL       =  0.0,
 NCAV_OUTPUT_STACK       =           0,
 NCAV_GRID_METRICS       = F,
 NCAV_FILE_DATE  = F,
 NCAV_VELOCITY   = F,
 NCAV_SALT_TEMP  = F,
 NCAV_TURBULENCE = F,
 NCAV_AVERAGE_VEL        = F,
 NCAV_VERTICAL_VEL       = F,
 NCAV_WIND_VEL   = F,
 NCAV_WIND_STRESS        = F,
 NCAV_EVAP_PRECIP        = F,
 NCAV_SURFACE_HEAT       = F,
 NCAV_GROUNDWATER        = F,
 NCAV_BIO        = F,
 NCAV_WQM        = F,
 NCAV_VORTICITY  = F
/

 &NML_SURFACE_FORCING
 WIND_ON = F,
 HEATING_ON      = F,
 PRECIPITATION_ON        = F,
 /

 &NML_PHYSICS
 HORIZONTAL_MIXING_TYPE          = 'closure'
 HORIZONTAL_MIXING_KIND          = 'constant'
 HORIZONTAL_MIXING_COEFFICIENT   = 0.3
 HORIZONTAL_PRANDTL_NUMBER       = 1.0
 VERTICAL_MIXING_TYPE            = 'closure'
 VERTICAL_MIXING_COEFFICIENT     = 1.0E-3,
 VERTICAL_PRANDTL_NUMBER         = 1.0
 BOTTOM_ROUGHNESS_MINIMUM        =  {3} 
 BOTTOM_ROUGHNESS_LENGTHSCALE    =  0.001
 BOTTOM_ROUGHNESS_KIND           = 'constant'
 BOTTOM_ROUGHNESS_TYPE           = 'orig'
 CONVECTIVE_OVERTURNING          = F,
 SCALAR_POSITIVITY_CONTROL       = T,
 BAROTROPIC                      = T,
 BAROCLINIC_PRESSURE_GRADIENT    = 'sigma levels'
 SEA_WATER_DENSITY_FUNCTION      = 'dens2'
 RECALCULATE_RHO_MEAN           = F
 INTERVAL_RHO_MEAN              = 'seconds=1800.'
 TEMPERATURE_ACTIVE              = F,
 SALINITY_ACTIVE                 = F,
 SURFACE_WAVE_MIXING             = F,
 WETTING_DRYING_ON               = T
 /

 &NML_RIVER_TYPE
 RIVER_NUMBER    =           0,
 /

 &NML_OPEN_BOUNDARY_CONTROL
 OBC_ON                      = T,
 OBC_NODE_LIST_FILE          = '{0}_obc.dat'
 OBC_ELEVATION_FORCING_ON    = T,
 OBC_ELEVATION_FILE          = '{0}_el_obc.nc'
 OBC_TS_TYPE                 = 3
 OBC_TEMP_NUDGING            = F,
 OBC_TEMP_FILE               = 'none'
 OBC_TEMP_NUDGING_TIMESCALE  =  0.0000000E+00,
 OBC_SALT_NUDGING            = F,
 OBC_SALT_FILE               = 'none'
 OBC_SALT_NUDGING_TIMESCALE  =  0.0000000E+00,
 OBC_MEANFLOW                = F,
/

 &NML_GRID_COORDINATES
 GRID_FILE       = '{0}_grd.dat'
 GRID_FILE_UNITS = 'meters'
 PROJECTION_REFERENCE  = 'proj=lcc +lon_0=-64.55880 +lat_0=41.84493 +lat_1=39.72147 +lat_2=43.96838'
 SIGMA_LEVELS_FILE     = 'sigma.dat'
 DEPTH_FILE      = '{0}_dep.dat'
 CORIOLIS_FILE   = '{0}_cor.dat'
 SPONGE_FILE     = '{0}_spg.dat'
 BFRIC_FILE='{0}_bfric.dat'
VVCOE_FILE='{0}_vvcoe.dat'
/

 &NML_GROUNDWATER
 GROUNDWATER_ON             = F,
 GROUNDWATER_FLOW  = 0.0,
 GROUNDWATER_FILE           = 'none'
 /

 &NML_LAG
 LAG_PARTICLES_ON        = F,
 LAG_START_FILE   = 'none'
 LAG_OUT_FILE     = 'none'
 LAG_RESTART_FILE = 'none'
 LAG_OUT_INTERVAL =  0.000000000000000E+000,
 LAG_SCAL_CHOICE  = 'none'
 /

 &NML_ADDITIONAL_MODELS
 DATA_ASSIMILATION       = F,
 BIOLOGICAL_MODEL        = F,
 SEDIMENT_MODEL  = F,
 SEDIMENT_PARAMETER_TYPE = 'constant'
 SEDIMENT_MODEL_FILE     = 'generic_sediment.inp'
 ICING_MODEL     = F,
 ICE_MODEL       = F,
 /

&NML_PROBES
PROBES_ON = F,
PROBES_NUMBER = 75,
PROBES_FILE = 'none',
/

&NML_TURBINE
TURBINE_ON = F,
TURBINE_FILE = 'none'
/

&NML_NESTING
NESTING_ON = F
/

&NML_NCNEST
NCNEST_ON = F
/

&NML_BOUNDSCHK
BOUNDSCHK_ON  = F
/

&NML_STATION_TIMESERIES
OUT_STATION_TIMESERIES_ON       = T,
STATION_FILE='{0}_stations.dat'
LOCATION_TYPE='cell'
OUT_ELEVATION=T,
OUT_VELOCITY_3D=F,
OUT_VELOCITY_2D=T,
OUT_SALT_TEMP =F,
OUT_WIND_VELOCITY=F,
OUT_INTERVAL= 'seconds=10.0',
OUT_START_DATE= '{1} 00:00:00'
 /

'''.format(gridName, start_dates[timenum], end_dates[timenum],drag_list[drag])

top = top.split('\n')

outputFile = filepath+drag_list[drag]+"_"+("%s"%start_dates[timenum])+"_"+ ("%s"%end_dates[timenum])+"/{0}_run.nml".format(gridName)
print outputFile
with open(outputFile, 'w') as f:
    for t in top:
        print >> f, t
