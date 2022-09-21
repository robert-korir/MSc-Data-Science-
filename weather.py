Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@robert-korir 
planet-os
/
demos
Public
Code
Issues
Pull requests
Actions
Projects
Security
Insights
demos/scripts/python/energy_calculator.py /
@dobrych
dobrych set wind/power graph bottom to zero
Latest commit 5aeea61 on Feb 21, 2017
 History
 1 contributor
248 lines (189 sloc)  8.62 KB

"""
Use PlanetOS Datahub API to model wind energy production by location and supported wind turbine type
Usage:
  energy_calculator.py  <longitude> <latitude>
                        [--rotor=<meters>] [--hub_height=<meters>]
                        [--turbine=<TURBINE_NAME_STRING>]
                        [--days=<number>]
                        [--roughness=<number>]
                        [--apikey=<APIKEY>]
Options:
  --turbine=<MODEL_NAME>        Turbine name [default: VESTAS V 90 3000]
                                List of supported turbines
                                https://github.com/wind-python/windpowerlib/blob/dev/windpowerlib/data/cp_values.csv
  --rotor=<diameter>            Turbine rotor diameter in meters [default: 90]
  --hub_height=<height>         Turbine hub height in meters [default: 70]
  --days=<number>               Number of GFS forecast days [default: 5]
  --roughness=<number>          Roughness length [default: 0.0002]
                                Other applicable values
                                https://en.wikipedia.org/wiki/Roughness_length#Application
  --apikey=<APIKEY>             Set PLANETOS_APIKEY environment variable to skip that option
Examples:
  energy_calculator.py 4.418889 52.606111 --rotor=90 --hub_height=70 --turbine='VESTAS V 90 3000'
  # Example parameters are for the OWEZ wind park (NL)
  # https://en.wikipedia.org/wiki/OWEZ
"""

try:

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
   
except ImportError:
    print('Some required Python modules are missing.\nPlease run `pip install slumber docopt pandas matplotlib seaborn windpowerlib`\nOr use PIP requirements file: https://github.com/planet-os/demos/tree/master/scripts/python/requirements.txt')
    exit()


import os
from datetime import datetime, timedelta

from pandas.io.json import json_normalize
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib import dates


if 'PLANETOS_APIKEY' in os.environ:
    APIKEY = os.environ['PLANETOS_APIKEY']

PAGESIZE = 500

DATASET_ID = 'noaa_gfs_pgrb2_global_forecast_recompute_0.25degree'

DATASET_VARIABLES = (
    # height index : list of variables
    (0, ('pres',)),
    (1, ('tmp_m',)),
    (1, ('ugrd_m', 'vgrd_m',)),
)

HEIGHT_SETTINGS = {
    'pressure': 80,
    'temp_air': 80,
    'v_wind': 80,
    'z0': 0
}


def fetch_metadata(ds_id):
    return API.datasets(ds_id).get(apikey=APIKEY)


def fetch_batch(ds_id, lat, lon, z, var_list, page=0, max_page=None, start_time=None, end_time=None):
    while True:
        print ("fetching %s -> %s\t\tpage: %s" % (ds_id, ', '.join(var_list), page))

        kwargs = dict()

        if start_time is not None:
            kwargs.update({'start': start_time.isoformat()})
        if end_time is not None:
            kwargs.update({'end': end_time.isoformat()})

        try:
            res = API.datasets(ds_id).area().get(
                apikey=APIKEY,
                lat=lat,
                lon=lon,
                count=PAGESIZE,
                var=','.join(var_list),
                z=z,  # z level index, 80m height in case of GFS
                offset=PAGESIZE * page,
                **kwargs
            )
        except HttpClientError as er:
            print("API query is failed: %s\nError: %s" % (er.response.url, er.response.content))
            return

        yield res

        # check if maximum limit of pages set and stop if it reached
        if max_page is not None and page > max_page:
            return
        # continue to "paginate" while nextOffset is present
        if 'stats' in res and 'nextOffset' in res['stats']:
            page += 1
        else:  # stop "pagination"
            return

# main routine
if __name__ == '__main__':
    arguments = docopt(__doc__, help=True)

    APIKEY = arguments['--apikey']
    lon = arguments['<longitude>']
    lat = arguments['<latitude>']

    days = float(arguments['--days']) or 5

    start_time = datetime.utcnow()
    end_time = start_time + timedelta(days=days)

    turbine_model = arguments['--turbine']

    roughness = float(arguments['--roughness'])

    full_data_frame = pd.DataFrame()

    sample_wind_turbine = {
        'h_hub': int(arguments['--hub_height']),
        'd_rotor': int(arguments['--rotor']),
        'wind_conv_type': turbine_model
    }

    # init turbine model
    wind_turbine = basicmodel.SimpleWindTurbine(**sample_wind_turbine)

    # iterate over a list of required variables, fetch them and combine in a single dataframe
    for z_index, var_list in DATASET_VARIABLES:
        paged_frame = pd.DataFrame()
        # paginated fetch (usually fits into single page)
        for frame in fetch_batch(ds_id=DATASET_ID, lat=lat, lon=lon, z=z_index, var_list=var_list, start_time=start_time, end_time=end_time):
            data_page = json_normalize(frame['entries'])
            paged_frame = paged_frame.append(data_page)

        # convert to time
        paged_frame['axes.time'] = paged_frame['axes.time'].apply(pd.to_datetime)
        paged_frame.set_index('axes.time', inplace=True)

        # merge with full frame
        full_data_frame = full_data_frame.merge(
            paged_frame, how='outer',
            right_index=True, left_index=True
        )

    # ensure we have same height for all variables
    assert len(np.unique(full_data_frame['axes.z'])) == 1
    print(u"Closest data grid coordinates found: %s, %s" % (
        np.unique(full_data_frame['axes.longitude']),
        np.unique(full_data_frame['axes.latitude'])
    ))
    grid_coords = (
        np.unique(full_data_frame['axes.longitude'])[0],
        np.unique(full_data_frame['axes.latitude'])[0]
    )

    # ensure we use single forecast run (optional)
    reftimes = np.unique(full_data_frame.filter(items=['axes.reftime', 'axes.reftime_y', 'axes.reftime_x']))
    reftime = reftimes[0] # default

    if len(reftimes) > 1:
        print(u"Two forecast runs detected in the output, picking first one (fuller) - %s" % reftimes)
        # filter rows that belong to a single reftime
        full_data_frame = full_data_frame[
            (full_data_frame['axes.reftime'] == reftime) &
            (full_data_frame['axes.reftime_x'] == reftime) &
            (full_data_frame['axes.reftime_y'] == reftime)
        ]

    full_data_frame['z0'] = roughness
    full_data_frame['wind_speed'] = np.sqrt(np.power(full_data_frame['data.ugrd_m'],2) + np.power(full_data_frame['data.vgrd_m'],2))

    full_data_frame.rename(columns={
        'data.pres': 'pressure',
        'data.tmp_m': 'temp_air',
        'wind_speed': 'v_wind'
    }, inplace=True)

    wind_turbine_forecast = wind_turbine.turbine_power_output(
        weather=full_data_frame,
        data_height=HEIGHT_SETTINGS
    )

    # merged_wind_energy = wind_turbine_forecast.to_frame('wind_energy').merge(full_data_frame['v_wind'].to_frame('wind_speed'), right_index=True, left_index=True)

    # PLOTTING
    plt.style.use('seaborn-paper')

    fig, host = plt.subplots()
    fig.set_size_inches([13, 7.5])
    fig.subplots_adjust(left=0.08, right=0.92)

    par1 = host.twinx()

    p1, = host.plot(wind_turbine_forecast.index, (wind_turbine_forecast.values / 1000000), color='C3', label="Energy (MW)")
    p2, = par1.plot(full_data_frame.index, full_data_frame['v_wind'], color='C5', linestyle='--', label="Wind speed (m/s)")

    host.set_xlabel("Time")
    ax = host.get_xaxis()
    ax.set_minor_locator(dates.HourLocator(byhour=(6,12,18)))
    ax.set_minor_formatter(dates.DateFormatter('%H'))
    ax.set_major_locator(dates.DayLocator())
    ax.set_major_formatter(dates.DateFormatter('%-d %b'))
    ax.grid(True, which='both')

    host.set_ylabel("Energy (MW)")
    par1.set_ylabel("Wind speed (m/s)")
    host.set_ylim(ymin=0)
    par1.set_ylim(ymin=0)

    host.set_title(u"%s energy production forecast for location Lon: %s, Lat: %s\n(based on GFS weather forecast (reftime: %s) acquired from the Planet OS Datahub API)" % (turbine_model, grid_coords[0], grid_coords[1], reftime))

    # host.yaxis.label.set_color(p1.get_color())
    # par1.yaxis.label.set_color(p2.get_color())

    tkw = dict(length=8, width=1.2)
    host.tick_params(axis='y', colors=p1.get_color(), **tkw)
    par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
    host.tick_params(axis='x', **tkw)
    host.tick_params(axis='x', which='minor', length=2)

    lines = [p1, p2]

    host.legend(lines, [l.get_label() for l in lines])

    plt.savefig(u"%s %s - wind speed - energy.png" % (turbine_model, DATASET_ID))
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
You have no unread notifications