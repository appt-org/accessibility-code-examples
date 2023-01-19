# Captions

Captions should be provided to enable users to understand what is being said in videos. Captions are a text based alternative for media, such as videos. The spoken dialogue and sound effects are displayed on screen as the video plays. Captions mostly benefit people who are deaf, hard of hearing, or deafblind. But captions are also useful to anyone who is temporarily unable to perceive sound, for example inside a library.

## WCAG

Relates to 1.2.2

## Android

On Android, captions can be added by using [`TimedText`](https://developer.android.com/reference/android/media/TimedText) inside a [`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer). The code example below shows a basic example.

```kotlin
val player = MediaPlayer.create(this, R.raw.video)
try {
    player.addTimedTextSource("/assets/appt.srt", MediaPlayer.MEDIA_MIMETYPE_TEXT_SUBRIP)
    player.trackInfo.forEachIndexed { index, trackInfo ->
        if (trackInfo.trackType == TrackInfo.MEDIA_TRACK_TYPE_TIMEDTEXT) {
            player.selectTrack(index)
            return@forEachIndexed
        }
    }
    player.setOnTimedTextListener(this)
    player.start()
} catch (e: Exception) {
    e.printStackTrace()
}
```

## iOS

On iOS, [`AVPlayer`](https://developer.apple.com/documentation/avfoundation/avplayer) offers support to [add captions](https://developer.apple.com/documentation/avfoundation/media_playback_and_selection/adding_subtitles_and_alternative_audio_tracks). Users can [automatically turn on subtitles](https://support.apple.com/nl-nl/guide/iphone/iph3e2e23d1/ios) via System Preferences.

The code example below shows a basic implementation of adding captions.

```swift
// Add video track
guard let videoTrack = videoComposition.addMutableTrack(
    withMediaType: .video, 
    preferredTrackID: kCMPersistentTrackID_Invalid
) else { 
    return 
}

guard let videoUrl = Bundle.main.url(forResource: "Appt", withExtension: "mp4") else { 
    return 
}

let videoAsset = AVURLAsset.init(url: videoUrl)
try? videoTrack.insertTimeRange(
    CMTimeRangeMake(start: .zero, duration: videoAsset.duration),
    of: videoAsset.tracks(withMediaType: .video)[0],
    at: .zero
)

// Add captions track
guard let captionsUrl = Bundle.main.url(
    forResource: "Appt", 
    withExtension: ".vtt"
) else { 
    return 
}
guard let captionsTrack = videoComposition.addMutableTrack(
    withMediaType: .text, 
    preferredTrackID: kCMPersistentTrackID_Invalid
) else { 
    return 
}

let captionsAsset = AVURLAsset(url: captionsUrl)
try? captionsTrack.insertTimeRange(
    CMTimeRangeMake(start: .zero, duration: videoAsset.duration),
    of: subtitleAsset.tracks(withMediaType: .text)[0],
    at: .zero
)
```

## Flutter

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

## React Native

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

## Xamarin

On Xamarin, you can use [`MediaElement`](https://docs.microsoft.com/en-us/xamarin/community-toolkit/views/mediaelement) to embed videos. Unfortunately, there is no built-in support to add captions.

```csharp
Not available, contribute!
```
