# Live captions

Captions should be provided in real-time to enable users to understand what is being said in live videos. The challenge with live captions is both organizational and technical. A captioner must be present who can provide live captions for the video by using suitable software.

## WCAG

Relates to 1.2.4

## Android

On Android, we recommend using a library such as [`ExoPlayer`](https://github.com/google/ExoPlayer) to support live captions. ExoPlayer is developed by Google and is an open-source alternative to Android's [`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer) for audio and video playback. Many code examples can be found in the [ExoPlayer documentation](https://exoplayer.dev/). You can use [`DefaultTrackSelector`](https://exoplayer.dev/doc/reference/index.html?com/google/android/exoplayer2/trackselection/DefaultTrackSelector.html) in combination with [`DefaultHttpDataSourceFactory`](https://exoplayer.dev/doc/reference/com/google/android/exoplayer2/upstream/DefaultHttpDataSource.html) to show subtitles.

```kotlin
val trackSelector = DefaultTrackSelector(baseContext)
trackSelector.setParameters(
    trackSelector.buildUponParameters().setPreferredTextLanguage("nl")
)
val exoPlayer = SimpleExoPlayer.Builder(baseContext)
                    .setTrackSelector(trackSelector)
                    .build()
val dataSourceFactory: DataSource.Factory = DefaultHttpDataSourceFactory(
    Util.getUserAgent(baseContext, "Appt"),
    null,
    DefaultHttpDataSource.DEFAULT_CONNECT_TIMEOUT_MILLIS,
    1800000,
    true
)
val mediaUri = Uri.parse("https://appt.org/live-video")
val mediaSource = HlsMediaSource.Factory(dataSourceFactory).createMediaSource(mediaUri)
exoPlayer.prepare(mediaSource)
```

## iOS

On iOS, [`AVPlayer`](https://developer.apple.com/documentation/avfoundation/avplayer) has built-in support for [live video](https://developer.apple.com/documentation/avfoundation/media_playback_and_selection/using_avfoundation_to_play_and_persist_http_live_streams) with [captions](https://developer.apple.com/documentation/avfoundation/media_playback_and_selection/adding_subtitles_and_alternative_audio_tracks). Users can [automatically turn on captions](https://support.apple.com/guide/iphone/subtitles-and-captions-iph3e2e23d1/ios) via System Preferences. The easiest way to stream a live video is through [`AVPlayerViewController`](https://developer.apple.com/documentation/avkit/avplayerviewcontroller).

```swift
guard let url = URL(string: "https://appt.org/live-video") else { 
    return 
}
let player = AVPlayer(url: url)

let playerViewController = AVPlayerViewController()
playerViewController.player = player

present(playerViewController, animated: true) {
    player.play()
}
```

## Flutter

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

## React Native

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

## Xamarin

On Xamarin, you can use [`MediaElement`](https://docs.microsoft.com/en-us/xamarin/community-toolkit/views/mediaelement) to embed videos. Unfortunately, there is no built-in support for live captions.

```xml
Not available, contribute!
```
