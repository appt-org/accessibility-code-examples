# Captions - Flutter

With Flutter, the [`video_player`](https://pub.dev/packages/video_player) package has support for the [`SubRip`](https://github.com/flutter/plugins/blob/main/packages/video_player/video_player/lib/src/sub_rip.dart) and [`WebVTT`](https://github.com/flutter/plugins/blob/main/packages/video_player/video_player/lib/src/web_vtt.dart) formats for captions. These files will be parsed to a `ClosedCaptionFile` that can be interpreted by the `video_player` package.

One way to implement this would be to load the video file and the captions and add these to the `VideoPlayerController`. The implementation below shows how this is achieved in the `video_player` example implementation. A full implementation can be found in the [GitHub repository of video_player](https://github.com/flutter/plugins/tree/main/packages/video_player/video_player).

```dart
late VideoPlayerController _controller;

Future<ClosedCaptionFile> _loadCaptions() async {
  final String fileContents = await DefaultAssetBundle.of(context)
    .loadString('/assets/appt.vtt');
  return WebVTTCaptionFile(
    fileContents); // For vtt files, use WebVTTCaptionFile
}

@override
void initState() {
  super.initState();
  _controller = VideoPlayerController.asset(
    '/assets/appt.mp4',     
    closedCaptionFile: _loadCaptions(),
  );

  _controller.addListener(() {
    setState(() {});
  });
  _controller.initialize();
}

@override
Widget build(BuildContext context) {
  return Stack(
    alignment: Alignment.bottomCenter,
    children: <Widget>[
      VideoPlayer(_controller),
      ClosedCaption(text: _controller.value.caption.text),
      VideoProgressIndicator(_controller, allowScrubbing: true),
    ],
  );
}
```
