# Captions - React Native

In React Native, you can use the [React-Native-Video](https://github.com/react-native-video/react-native-video/blob/master/API.md#texttracks) package to add captions in `.vtt`, `.ttml` and `.srt` formats. It is advised to use `.vtt` as it is supported on both Android and iOS.

```jsx
import { TextTrackType, Video } from 'react-native-video';

<Video
    textTracks={[
        {
            title: "English CC",
            language: "en",
            type: TextTrackType.VTT,
            uri: "https://appt.org/subtitles/en.vtt"
        },
        {
            title: "Spanish Subtitles",
            language: "es",
            type: TextTrackType.SRT,
            uri: require('https://appt.org/subtitles/es.srt')
        }
    ]}
/>
```
