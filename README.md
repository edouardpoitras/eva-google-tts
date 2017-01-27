Google Text-to-Speech
=====================

A text-to-speech plugin that uses the gTTS python library to generate speech for Eva.

Sounds better than the [Default Text-to-Speech](https://github.com/edouardpoitras/eva-default-tts.git) plugin but requires an active internet connection and sends your Eva responses to a third-party.

## Installation

Can be easily installed through the Web UI by using [Web UI Plugins](https://github.com/edouardpoitras/eva-web-ui-plugins).

Alternatively, add `google_tts` to your `eva.conf` file in the `enabled_plugins` option list and restart Eva.

## Usage

Once enabled, Eva will start adding audio data from the third-party service to every response. This can be used by the clients to playback an appropriate audio response from Eva.

#### Audio Data

The clients should expect data with the following structure:

    data {
        'output_text': <text response here>,
        'output_audio': {
            'content_type': 'audio/wav', 'audio/mpeg', etc,
            'audio': <raw audio data>
        }
    }

## Configuration

None
