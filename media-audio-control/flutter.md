# Audio control - Flutter

In Flutter apps you should always be able to control audio. Two popular options for playing media are [`video_player`](https://pub.dev/packages/video_player) and [`just_audio`](https://pub.dev/packages/just_audio). Both packages have options for controlling audio through `play()` and `pause()` methods.

```dart
final player = AudioPlayer();                   
final duration = await player.setUrl('https://appt.org/audio.mp3');

IconButton(
  icon: Icon(Icons.play_arrow),
  iconSize: 64.0,
  onPressed: await player.play(),
);

IconButton(
  icon: Icon(Icons.pause),
  iconSize: 64.0,
  onPressed: await player.pause(),
);
```
