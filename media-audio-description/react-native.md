# Audio description - React Native

On React Native, the [React-Native-Video](https://github.com/react-native-video/react-native-video) package has support for [switching audio tracks](https://github.com/react-native-video/react-native-video/blob/master/API.md#selectedaudiotrack). This allows you to offer users a way to switch to an audio description track.

Note: The audio tracks must be encoded in the file, this is not something you add programmatically.

```jsx
import Video from 'react-native-video';

<Video
    selectedAudioTrack={{
        type: "audio-description",
        value: "en"
    }}
/>
```
