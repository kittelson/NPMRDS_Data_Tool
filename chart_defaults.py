"""
Contains default values and utility methods for the matplotlib based charts
"""

SPEED_BIN_DEFAULTS = ['#d62728', '#ff7f0e', '#dbdb8d', '#98df8a', '#2ca02c']
TT_BLUE = '#6e97c8'  # '#4f81bd'
TT_RED = '#da9694'  # '#c0504d'
TT_BLUE_BEFORE = '#032548'  # '#08519c'
TT_ORANGE_BEFORE = '#d95f0e'
TT_RED_BEFORE = '#c00000'
SB_BLUE = '#B0C4DE'
SB_RED = '#cd5c5c'
BEFORE_LW = 1.0
CHART1_TYPES = ['Peak Period Travel Time Trends (Line)',
                'Peak Period Travel Time Trends (Bar)',
                'Speed Heatmap - Time of Day',
                'Peak Period Speed Heatmap - Facility',
                'Congestion Stack - Day',
                'Congestion Stack - Facility']


def generate_color_button_style(color_str):
    style_str = 'QPushButton { border: 2px solid #8f8f91; border-radius: 1px; background-color:'
    style_str = style_str + color_str + ';'
    style_str = style_str +'min-width: 80px; border-width: 5px; border-color:white; }\n'
    style_str = style_str + 'QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0  #dadbde, stop: 1 '
    style_str = style_str + color_str + '); }'
    return style_str

def make_colormap(seq):
    """Return a LinearSegmentedColormap
    seq: a sequence of floats and RGB-tuples. The floats should be increasing
    and in the interval (0,1).
    """
    import matplotlib.colors as mcolors
    seq = [(None,) * 3, 0.0] + list(seq) + [1.0, (None,) * 3]
    cdict = {'red': [], 'green': [], 'blue': []}
    for i, item in enumerate(seq):
        if isinstance(item, float):
            r1, g1, b1 = seq[i - 1]
            r2, g2, b2 = seq[i + 1]
            cdict['red'].append([item, r1, r2])
            cdict['green'].append([item, g1, g2])
            cdict['blue'].append([item, b1, b2])
    return mcolors.LinearSegmentedColormap('CustomMap', cdict)


def create_dq_cmap():
    import matplotlib.colors as mcolors
    c = mcolors.ColorConverter().to_rgb
    # rvb1 = make_colormap(
    #     [c('indigo'), c('red'), 0.5, c('red'), c('orange'), 0.6, c('orange'), c('yellow'), 0.7, c('yellow'), c('lightgreen'), 0.8, c('lightgreen'),
    #      c('green'), 0.9, c('green')])
    custom_cmap = make_colormap(
        [c('indigo'), c('indigo'), 0.25, c('indigo'), c('red'), 0.5, c('red'), c('orange'), 0.6, c('orange'), c('yellow'), 0.7, c('yellow'),
         c('lightgreen'), 0.8, c('lightgreen'), c('green'), 0.9, c('green')])
    return custom_cmap


class ChartOptions:
    def __init__(self, **kwargs):
        self.MAX_ROWS = 2
        self.MAX_COLS = 2
        self.num_rows = 2
        self.num_cols = 2
        self.num_speed_bins = 5
        self.speed_bin_colors = SPEED_BIN_DEFAULTS
        self.speed_bins = [0, 25, 35, 45, 55]

        if kwargs is not None:
            if 'rows' in kwargs:
                self.num_rows = kwargs['rows']
            if 'cols' in kwargs:
                self.num_cols = kwargs['cols']
            if 'num_speed_bins' in kwargs:
                self.num_speed_bins = kwargs['num_speed_bins']
            if 'speed_bin_colors' in kwargs:
                self.speed_bin_colors = kwargs['speed_bin_colors']
            if 'speed_bins_vals' in kwargs:
                self.speed_bins = kwargs['speed_bins_vals']

        self.has_chart = [[False for j in range(self.MAX_COLS)] for i in range(self.MAX_ROWS)]
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.has_chart[i][j] = True
        # self.chart_type = [[(i * self.num_cols) + j for j in range(self.MAX_COLS)] for i in range(self.MAX_ROWS)]
        self.chart_type = [[0, 4], [1, 5]]
        # self.layout = compute_layout()


class AnalysisOptions:
    def __init__(self, speed_band=True, extra_time=True, tt_cdf=True, speed_freq=True, tt_trend=False, congestion_stack=False, **kwargs):
        self.speed_band = speed_band
        self.extra_time = extra_time
        self.tt_cdf = tt_cdf
        self.speed_frequency = speed_freq
        self.tt_trend = tt_trend
        self.congestion_stack = congestion_stack



def generate_vega_lite(data_frame, f_name=None):
    import json
    # Creating data dictionary
    data = []
    for index, row in data_frame.iterrows():
        data.append({'Time of Day': str(index), 'Travel Time': str(row['travel_time_minutes'])})
    # Creating JSON dictionary
    vis = dict()
    vis['description'] = 'TMC Travel Time by Hour of Day'
    vis['data'] = {'values': data}
    vis['mark'] = 'bar'
    f1 = {'field': 'Time of Day', 'type': 'quantitative'}
    f2 = {'field': 'Travel Time', 'type': 'quantitative'}
    vis['encoding'] = {'x': f1, 'y': f2}

    return json.dumps(vis, ensure_ascii=False)
