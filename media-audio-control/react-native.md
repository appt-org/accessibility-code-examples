# Audio control - React Native

In React Native apps you should always be able to control audio. A popular option for media is the [`react-native-video`](https://github.com/react-native-video/react-native-video/) package. You can use the [`audioOnly`](https://github.com/react-native-video/react-native-video/blob/master/API.md#audioonly) property to play audio files. The `react-native-video` package offers native controls for playing and pausing by default.

```jsx
<Video 
    audioOnly
    post={require('appt.png')} 
    source={require('appt.mp3')} />
```
