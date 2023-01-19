# Audio description

Videos should include audio description when important visual details are shown which you cannot hear. Audio description is an additional sound track which describes these important visual details. This allows people who are blind or have difficulty processing visual information to understand the content.

## WCAG

Relates to 1.2.3, 1.2.5

## Android

As of Android 4.1, the [`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer) has support for multiple audio tracks. Use the [`selectTrack`](https://developer.android.com/reference/android/media/MediaPlayer#selectTrack(int)) method to select the correct audio track.

The code example belows shows a basic implementation of selecting an audio description track embedded inside a video.

```kotlin
val player = MediaPlayer.create(this, R.raw.video)
try {
    player.trackInfo.forEachIndexed { index, trackInfo ->
        if (trackInfo.trackType == TrackInfo.MEDIA_TRACK_TYPE_AUDIO) {
            player.selectTrack(index)
            return@forEachIndexed
        }
    }
    player.start()
} catch (e: Exception) {
    e.printStackTrace()
}
```

## iOS

On iOS, [`AVPlayer`](https://developer.apple.com/documentation/avfoundation/avplayer) has support to [add audio description](https://developer.apple.com/documentation/avfoundation/media_playback_and_selection/adding_subtitles_and_alternative_audio_tracks). Users can [enable audio description automatically](https://support.apple.com/en-us/HT205796) through System Preferences. Turning on audio description works automatically if you add the [`public.accessibility.describes-video`](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/1389809-describesvideoforaccessibility) property to the audio description track.

The code example below shows a basic implementation of enabling audio description embedded inside a video.

```swift
let videoComposition = AVMutableComposition()

// Add video track
guard let videoTrack = videoComposition.addMutableTrack(
    withMediaType: .video, 
    preferredTrackID: kCMPersistentTrackID_Invalid
) else { 
    return 
}
guard let videoUrl = Bundle.main.url(
    forResource: "Appt", 
    withExtension: "mp4"
) else { 
    return 
}
let videoAsset = AVURLAsset.init(url: videoUrl)
try? videoTrack.insertTimeRange(
    CMTimeRangeMake(start: .zero, duration: videoAsset.duration),
    of: videoAsset.tracks(withMediaType: .video)[0],
    at: .zero
)

// Find & add audio description track
for track in videoAsset.tracks {
    if track.hasMediaCharacteristic(.describesVideoForAccessibility) {
        guard let audioTrack = videoComposition.addMutableTrack(
            withMediaType: track.mediaType, 
            preferredTrackID: kCMPersistentTrackID_Invalid
        ) else { 
            return 
        }
        try? audioTrack.insertTimeRange(
            CMTimeRange(start: .zero, duration: videoAsset.duration), 
            of: track, 
            at: .zero
        )
        break
    }
}
```

## Flutter

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

## React Native

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

## Xamarin

On Xamarin, you can use [`MediaElement`](https://docs.microsoft.com/en-us/xamarin/community-toolkit/views/mediaelement) to embed videos. Unfortunately, there is no built-in support to switch to an audio description track.

```xml
Not available, contribute!
```
