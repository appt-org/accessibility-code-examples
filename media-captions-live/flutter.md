# Live captions - Flutter

On Flutter, the [video_player](https://pub.dev/packages/video_player) package does not have support for captions in live videos. [Issue #50595](https://github.com/flutter/flutter/issues/50595) has been opened to request support.

Other packages, like [better_player](https://pub.dev/packages/better_player), do have support for using captions on live video. The [better_player documentation](https://jhomlala.github.io/betterplayer/#/README) contains detailed information on how to do so.

```dart
BetterPlayerController controller = BetterPlayerController(
    const BetterPlayerConfiguration(
        controlsConfiguration: BetterPlayerControlsConfiguration(
        enableAudioTracks: true,
        enableSubtitles: true,
        ),
    ),
    betterPlayerDataSource: BetterPlayerDataSource.network(
        'https://appt.org/live-video', 
        liveStream: true,
        useAsmsSubtitles: true,
    ),
);

@override
Widget build(BuildContext context) {
  return BetterPlayer(controller: controller);
}
```
