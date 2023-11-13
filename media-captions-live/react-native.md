# Live captions - React Native

React Native does not have any out-of-the box packages which enable you to provide real-time captions for live audio or video streams.

You can however embed a YouTube stream in your app and enable [Live Stream Captioning](https://support.google.com/youtube/thread/129769858/updates-to-captions-and-audio-features-on-youtube?hl=en).

```jsx
import YoutubePlayer from "react-native-youtube-iframe";
  
<YoutubePlayer
    height={300}
    play={playing}
    videoId="dQw4w9WgXcQ"
    onChangeState={onStateChange}
/>
```
