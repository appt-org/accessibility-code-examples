# Audio description - Flutter

With Flutter, you can use [`better_player`](https://pub.dev/packages/better_player) to let users select different audio tracks.

The code example belows shows a basic implementation of changing audio tracks.

```dart
BetterPlayerController controller = BetterPlayerController(
    const BetterPlayerConfiguration(
      controlsConfiguration: BetterPlayerControlsConfiguration(
        enableAudioTracks: true,
      ),
    ),
    betterPlayerDataSource: BetterPlayerDataSource.file(
      'assets/appt.mp4',
      useAsmsSubtitles: true,
    ),
  );

void changeAudioTrack(int track) {
  if (controller.betterPlayerAsmsAudioTracks?[track] != null) {
    controller.setAudioTrack(controller.betterPlayerAsmsAudioTracks![track]);
  }
}

@override
Widget build(BuildContext context) {
  return BetterPlayer(controller: controller);
}
```
