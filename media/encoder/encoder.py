
from streamer.controller_node import ControllerNode



controller = ControllerNode()

def encode():
    controller.start(
        output_location= '../encoded_files',
        input_config_dict= {
            'inputs': [
                dict(name='../ocean.mkv', media_type='video'),
                dict(name='../countryroad.mp4', media_type='audio'),
            ]
            },
        pipeline_config_dict= {
            'streaming_mode': 'vod',
            'resolutions': ['1080p', '720p', '480p'],
            'channel_layouts': ['stereo'],
            'video_codecs': ['h264'],
            'audio_codecs': ['aac'] ,
            'manifest_format': ['dash', 'hls'],
            'segment_size': 10,
            'segment_per_file': True,
            'segment_folder': 'segments',
            'dash_output': 'this_is_dash.mpd',
            'hls_output': 'this_is_hls.m3u8',
        },
     use_hermetic= True,   
    )


encode()
