import collections


def make_rundict(grid):

    rv=collections.OrderedDict()

    #&NML_CASE
    rv['CASE_TITLE']                     =   [grid]
    rv['TIMEZONE']                       =   ['UTC']
    rv['DATE_FORMAT']                    =   ['YMD']
    #no start and end dates because they interfer with product have to be passed manually... 
    #rv['START_DATE']                     =   ['2000-01-01 00:00:00']
    #rv['END_DATE']                       =   ['2000-01-01 00:00:00']

    #&NML_STARTUP
    rv['STARTUP_TYPE']                   =   ['coldstart']
    rv['STARTUP_FILE']                   =   ['none']
    rv['STARTUP_UV_TYPE']                =   ['default']
    rv['STARTUP_TURB_TYPE']              =   ['default']
    rv['STARTUP_TS_TYPE']                =   ['constant']
    rv['STARTUP_T_VALS']                 =   [18]
    rv['STARTUP_S_VALS']                 =   [35.0]
    rv['STARTUP_DMAX']                   =   [-10.0]

    #&NML_IO
    rv['INPUT_DIR']                      =   ['./input/']
    rv['OUTPUT_DIR']                     =   ['./output/']
    rv['IREPORT']                        =   [1000]
    rv['VISIT_ALL_VARS']                 =   ['F']
    rv['WAIT_FOR_VISIT']                 =   ['F']
    rv['USE_MPI_IO_MODE']                =   ['F']

    #&NML_INTEGRATION
    rv['EXTSTEP_SECONDS']                =   [0.01]
    rv['ISPLIT']                         =   [1]
    rv['IRAMP']                          =   [34560]
    rv['MIN_DEPTH']                      =   [0.5]
    rv['STATIC_SSH_ADJ']                 =   [0.0]

    #&NML_RESTART
    rv['RST_ON']                         =   ['T']
    #no date stuff will be handled in makeRun code
    #rv['RST_FIRST_OUT']                  =   ['2000-01-01 00:00:00']
    rv['RST_OUT_INTERVAL']               =   ['days=5.0']
    rv['RST_OUTPUT_STACK']               =   [0]

    #&NML_NETCDF
    rv['NC_ON']                          =   ['T']
    #no date stuff will be handled in makeRun code
    #rv['NC_FIRST_OUT']                   =   ['2000-01-01 00:00:00']
    rv['NC_OUT_INTERVAL']                =   ['seconds=600.0']
    rv['NC_OUTPUT_STACK']                =   [0]
    rv['NC_GRID_METRICS']                =   ['T']
    rv['NC_VELOCITY']                    =   ['F']
    rv['NC_SALT_TEMP']                   =   ['F']
    rv['NC_TURBULENCE']                  =   ['F']
    rv['NC_AVERAGE_VEL']                 =   ['T']
    rv['NC_VERTICAL_VEL']                =   ['F']
    rv['NC_WIND_VEL']                    =   ['F']
    rv['NC_WIND_STRESS']                 =   ['F']
    rv['NC_EVAP_PRECIP']                 =   ['F']
    rv['NC_SURFACE_HEAT']                =   ['F']
    rv['NC_GROUNDWATER']                 =   ['F']

    #&NML_NETCDF_AV
    rv['NCAV_ON']                        =   ['F']
    rv['NCAV_FIRST_OUT']                 =   ['none']
    rv['NCAV_OUT_INTERVAL']              =   [0.0]
    rv['NCAV_OUTPUT_STACK']              =   [0]
    rv['NCAV_GRID_METRICS']              =   ['F']
    rv['NCAV_FILE_DATE']                 =   ['F']
    rv['NCAV_VELOCITY']                  =   ['F']
    rv['NCAV_SALT_TEMP']                 =   ['F']
    rv['NCAV_TURBULENCE']                =   ['F']
    rv['NCAV_AVERAGE_VEL']               =   ['F']
    rv['NCAV_VERTICAL_VEL']              =   ['F']
    rv['NCAV_WIND_VEL']                  =   ['F']
    rv['NCAV_WIND_STRESS']               =   ['F']
    rv['NCAV_EVAP_PRECIP']               =   ['F']
    rv['NCAV_SURFACE_HEAT']              =   ['F']
    rv['NCAV_GROUNDWATER']               =   ['F']
    rv['NCAV_BIO']                       =   ['F']
    rv['NCAV_WQM']                       =   ['F']
    rv['NCAV_VORTICITY']                 =   ['F']

    #&NML_SURFACE_FORCING
    rv['WIND_ON']                        =   ['F']
    rv['HEATING_ON']                     =   ['F']
    rv['PRECIPITATION_ON']               =   ['F']

    #&NML_PHYSICS
    rv['HORIZONTAL_MIXING_TYPE']         =   ['closure']
    rv['HORIZONTAL_MIXING_KIND']         =   ['constant']
    rv['HORIZONTAL_MIXING_COEFFICIENT']  =   [0.3]
    rv['HORIZONTAL_PRANDTL_NUMBER']      =   [1.0]
    rv['VERTICAL_MIXING_TYPE']           =   ['closure']
    rv['VERTICAL_MIXING_COEFFICIENT']    =   [1.0E-3]
    rv['VERTICAL_PRANDTL_NUMBER']        =   [1.0]
    rv['BOTTOM_ROUGHNESS_MINIMUM']       =   [0.0025]
    rv['BOTTOM_ROUGHNESS_LENGTHSCALE']   =   [0.001]
    rv['BOTTOM_ROUGHNESS_KIND']          =   ['constant']
    rv['BOTTOM_ROUGHNESS_TYPE']          =   ['orig']
    rv['CONVECTIVE_OVERTURNING']         =   ['F']
    rv['SCALAR_POSITIVITY_CONTROL']      =   ['T']
    rv['BAROTROPIC']                     =   ['T']
    rv['BAROCLINIC_PRESSURE_GRADIENT']   =   ['sigma levels']
    rv['SEA_WATER_DENSITY_FUNCTION']     =   ['dens2']
    rv['RECALCULATE_RHO_MEAN']           =   ['F']
    rv['INTERVAL_RHO_MEAN']              =   ['seconds=1800.']
    rv['TEMPERATURE_ACTIVE']             =   ['F']
    rv['SALINITY_ACTIVE']                =   ['F']
    rv['SURFACE_WAVE_MIXING']            =   ['F']
    rv['WETTING_DRYING_ON']              =   ['T']

    #&NML_RIVER_TYPE
    rv['RIVER_NUMBER']                   =   [0]

    #&NML_OPEN_BOUNDARY_CONTROL
    rv['OBC_ON']                         =   ['T']
    rv['OBC_NODE_LIST_FILE']             =   [grid+'_obc.dat']
    rv['OBC_ELEVATION_FORCING_ON']       =   ['T']
    rv['OBC_ELEVATION_FILE']             =   [grid+'_el_obc.nc']
    rv['OBC_TS_TYPE']                    =   [3]
    rv['OBC_TEMP_NUDGING']               =   ['F']
    rv['OBC_TEMP_FILE']                  =   ['none']
    rv['OBC_TEMP_NUDGING_TIMESCALE']     =   [0.0000000E+00]
    rv['OBC_SALT_NUDGING']               =   ['F']
    rv['OBC_SALT_FILE']                  =   ['none']
    rv['OBC_SALT_NUDGING_TIMESCALE']     =   [0.0000000E+00]
    rv['OBC_MEANFLOW']                   =   ['F']

    #&NML_GRID_COORDINATES
    rv['GRID_FILE']                      =   [grid+'_grd.dat']
    rv['GRID_FILE_UNITS']                =   ['meters']
    rv['PROJECTION_REFERENCE']           =   ['']
    rv['SIGMA_LEVELS_FILE']              =   ['sigma.dat']
    rv['DEPTH_FILE']                     =   [grid+'_dep.dat']
    rv['CORIOLIS_FILE']                  =   [grid+'_cor.dat']
    rv['SPONGE_FILE']                    =   [grid+'_spg.dat']
    rv['BFRIC_FILE']                     =   [grid+'_bfric.dat']
    rv['VVCOE_FILE']                     =   [grid+'_vvcoe.dat']

    #&NML_GROUNDWATER
    rv['GROUNDWATER_ON']                 =   ['F']
    rv['GROUNDWATER_FLOW']               =   [0.0]
    rv['GROUNDWATER_FILE']               =   ['none']

    #&NML_LAG
    rv['LAG_PARTICLES_ON']               =   ['F']
    rv['LAG_START_FILE']                 =   ['none']
    rv['LAG_OUT_FILE']                   =   ['none']
    rv['LAG_RESTART_FILE']               =   ['none']
    rv['LAG_OUT_INTERVAL']               =   [0.00E+000]
    rv['LAG_SCAL_CHOICE']                =   ['none']

    #&NML_ADDITIONAL_MODELS
    rv['DATA_ASSIMILATION']              =   ['F']
    rv['BIOLOGICAL_MODEL']               =   ['F']
    rv['SEDIMENT_MODEL']                 =   ['F']
    rv['SEDIMENT_PARAMETER_TYPE']        =   ['constant']
    rv['SEDIMENT_MODEL_FILE']            =   ['generic_sediment.inp']
    rv['ICING_MODEL']                    =   ['F']
    rv['ICE_MODEL']                      =   ['F']

    #&NML_PROBES
    rv['PROBES_ON']                      =   ['F']
    rv['PROBES_NUMBER']                  =   [75]
    rv['PROBES_FILE']                    =   ['none']

    #&NML_TURBINE
    rv['TURBINE_ON']                     =   ['F']
    rv['TURBINE_FILE']                   =   ['none']

    #&NML_NESTING
    rv['NESTING_ON']                     =   ['F']

    #&NML_NCNEST
    rv['NCNEST_ON']                      =   ['F']

    #&NML_BOUNDSCHK
    rv['BOUNDSCHK_ON']                   =   ['F']

    #&NML_STATION_TIMESERIES
    rv['OUT_STATION_TIMESERIES_ON']      =   ['T']
    rv['STATION_FILE']                   =   [grid+'_stations.dat']
    rv['LOCATION_TYPE']                  =   ['cell']
    rv['OUT_ELEVATION']                  =   ['T']
    rv['OUT_VELOCITY_3D']                =   ['F']
    rv['OUT_VELOCITY_2D']                =   ['T']
    rv['OUT_SALT_TEMP']                  =   ['F']
    rv['OUT_WIND_VELOCITY']              =   ['F']
    rv['OUT_INTERVAL']                   =   ['seconds=10.0']
    #no date stuff will be handled in makeRun code
    #rv['OUT_START_DATE']                 =   ['2000-01-01 00:00:00']


    if grid=='smallcape_force':
        rv['PROJECTION_REFERENCE']           =   ['proj=lcc +lon_0=-64.55880 +lat_0=41.84493 +lat_1=39.72147 +lat_2=43.96838']
        rv['EXTSTEP_SECONDS']                =   [0.5]



    return                               rv

