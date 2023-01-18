# Audio control

Users should be able to control audio whenever it plays automatically. This includes being able to reduce the volume to zero. It's difficult to hear speech output of the screen reader users when other audio is playing at the same time.

## WCAG

Relates to 1.4.2

## Android

In Android apps, you should always be able to control audio. When using [`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer), you should implement buttons to call the [`start`](https://developer.android.com/reference/android/media/MediaPlayer#start()), [`pause`](https://developer.android.com/reference/android/media/MediaPlayer#pause()) and [`stop`](https://developer.android.com/reference/android/media/MediaPlayer#stop()) methods.

It is a best practice to play audio through the correct channel. Android has introduced [`AudioAttributes`](https://developer.android.com/reference/android/media/AudioAttributes) as a replacement of the `STREAM` types defined in [AudioManager](https://developer.android.com/reference/android/media/AudioManager).

`AudioAttributes` defines the following content types:

- [`CONTENT_TYPE_MOVIE`](https://developer.android.com/reference/android/media/AudioAttributes#CONTENT_TYPE_MOVIE): used for soundtracks, typically in movies
- [`CONTENT_TYPE_MUSIC`](https://developer.android.com/reference/android/media/AudioAttributes#CONTENT_TYPE_MUSIC): used for music
- [`CONTENT_TYPE_SONIFICATION`](https://developer.android.com/reference/android/media/AudioAttributes#CONTENT_TYPE_SONIFICATION): used for accompanying sounds, such as beeps
- [`CONTENT_TYPE_SPEECH`](https://developer.android.com/reference/android/media/AudioAttributes#CONTENT_TYPE_SPEECH): used for speech
- [`CONTENT_TYPE_UNKNOWN`](https://developer.android.com/reference/android/media/AudioAttributes#CONTENT_TYPE_UNKNOWN): used when the content type is unknown, or other than the available options

`AudioAttributes` defines the following usages:

- [`USAGE_ALARM`](https://developer.android.com/reference/android/media/AudioAttributes#USAGE_ALARM): used for alarms
- [`USAGE_ASSISTANCE_ACCESSIBILITY`](https://developer.android.com/reference/android/media/AudioAttributes#USAGE_ASSISTANCE_ACCESSIBILITY): used for accessibility, e.g. for screen reader users
- [`USAGE_ASSISTANCE_NAVIGATION_GUIDANCE`](https://developer.android.com/reference/android/media/AudioAttributes#USAGE_ASSISTANCE_NAVIGATION_GUIDANCE): used for navigation directions, e.g. while driving
- [`USAGE_ASSISTANCE_SONIFICATION`](https://developer.android.com/reference/android/media/AudioAttributes#USAGE_ASSISTANCE_SONIFICATION): used for user interface sounds
- [`USAGE_ASSISTANT`](https://developer.android.com/reference/android/media/AudioAttributes#USAGE_ASSISTANT): used for user queries, audio instructions or help utterances.
- [`USAGE_GAME`](https://developer.android.com/reference/android/media/AudioAttributes#USAGE_GAME): used for audio inside games
- [`USAGE_MEDIA`](https://developer.android.com/reference/android/media/AudioAttributes#USAGE_MEDIA): used for audio in media, such as movies
- [`USAGE_NOTIFICATION`](https://developer.android.com/reference/android/media/AudioAttributes#USAGE_NOTIFICATION): used for notification sounds
- [`USAGE_NOTIFICATION_EVENT`](https://developer.android.com/reference/android/media/AudioAttributes#USAGE_NOTIFICATION_EVENT): used to attract the user's attention, such as a reminder or low battery warning.
- [`USAGE_NOTIFICATION_RINGTONE`](https://developer.android.com/reference/android/media/AudioAttributes#USAGE_NOTIFICATION_RINGTONE): used for telephony ringtones
- [`USAGE_UNKNOWN`](https://developer.android.com/reference/android/media/AudioAttributes#USAGE_UNKNOWN): used when the usage is unknown, or not defined
- [`USAGE_VOICE_COMMUNICATION`](https://developer.android.com/reference/android/media/AudioAttributes#USAGE_VOICE_COMMUNICATION): used for voice communication, such as telephony or VoIP
- [`USAGE_VOICE_COMMUNICATION_SIGNALLING`](https://developer.android.com/reference/android/media/AudioAttributes#USAGE_VOICE_COMMUNICATION_SIGNALLING): used for in-call signalling, such as with a "busy" beep, or `DTMF` tones.

`AudioManager` defines the following legacy channels:

- [`STREAM_ACCESSIBILITY`](https://developer.android.com/reference/android/media/AudioManager#STREAM_ACCESSIBILITY): channel for accessibility, such as assistive technologies
- [`STREAM_ALARM`](https://developer.android.com/reference/android/media/AudioManager#STREAM_ALARM): channel for alarms
- [`STREAM_DMTF`](https://developer.android.com/reference/android/media/AudioManager#STREAM_DTMF): channel for dual-tone multi-frequency signaling, such as phone dialing tones
- [`STREAM_MUSIC`](https://developer.android.com/reference/android/media/AudioManager#STREAM_MUSIC): channel for music
- [`STREAM_NOTIFICATION`](https://developer.android.com/reference/android/media/AudioManager#STREAM_NOTIFICATION): channel for notifications
- [`STREAM_RING`](https://developer.android.com/reference/android/media/AudioManager#STREAM_RING): channel for incoming phone calls
- [`STREAM_SYSTEM`](https://developer.android.com/reference/android/media/AudioManager#STREAM_SYSTEM): channel for system sounds
- [`STREAM_VOICE_CALL`](https://developer.android.com/reference/android/media/AudioManager#STREAM_VOICE_CALL): channel for voice calls

```kotlin
// Set audio attributes
val player = MediaPlayer()
player.setAudioAttributes(
    AudioAttributes.Builder()
        .setUsage(AudioAttributes.USAGE_ASSISTANCE_ACCESSIBILITY)
        .setContentType(AudioAttributes.CONTENT_TYPE_SPEECH)
        .setLegacyStreamType(AudioManager.STREAM_ACCESSIBILITY)
        .build()
)

// Provide media controls
button.setOnClickListener {
    if (player.isPlaying()) {
        player.pause()
    } else {
        player.start()
    }
}
```

## iOS

In iOS apps you should always provide a pause or stop button for media. When using [`AVPlayer`](https://developer.apple.com/documentation/avfoundation/avplayer), you should use [`play`](https://developer.apple.com/documentation/avfoundation/avplayer/1386726-play) and [`pause`](https://developer.apple.com/documentation/avfoundation/avplayer/1387895-pause) methods.

You should also make sure that audio is played through the correct channel. Use [`AVAudioSession`](https://developer.apple.com/documentation/avfaudio/avaudiosession) in combination with [`AVAudioSessionCategory`](https://developer.apple.com/documentation/avfaudio/avaudiosessioncategory) to achieve this.

The following channels are available:

- [`AVAudioSessionCategoryAmbient`](https://developer.apple.com/documentation/avfaudio/avaudiosessioncategoryambient): use this channel if the sound is not important for the functioning of the app
- [`AVAudioSessionCategoryMultiRoute`](https://developer.apple.com/documentation/avfaudio/avaudiosessioncategorymultiroute): use this channel if you are sending the sound to multiple output devices at the same time
- [`AVAudioSessionCategoryPlayAndRecord`](https://developer.apple.com/documentation/avfaudio/avaudiosessioncategoryplayandrecord): use this channel for sound recording and playback
- [`AVAudioSessionCategoryPlayback`](https://developer.apple.com/documentation/avfaudio/avaudiosessioncategoryplayback): use this channel to play recorded music and other sounds that are important for the app's functioning
- [`AVAudioSessionCategoryRecord`](https://developer.apple.com/documentation/avfaudio/avaudiosessioncategoryrecord): use this channel for sound recording; other sound is muted
- [`AVAudioSessionCategorySoloAmbient`](https://developer.apple.com/documentation/avfaudio/avaudiosessioncategorysoloambient): the default channel to play sound

```swift
// Set audio channel
try AVAudioSession.sharedInstance().setCategory(
    .playback, 
    mode: .default, 
    options: []
)

// Provide media controls
@objc private func click(_ sender: UIButton) {
    if player.timeControlStatus == .playing {
        player.pause()
    } else {
        player.play()
    }
}
```

## Flutter

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

## React Native

In React Native apps you should always be able to control audio. A popular option for media is the [`react-native-video`](https://github.com/react-native-video/react-native-video/) package. You can use the [`audioOnly`](https://github.com/react-native-video/react-native-video/blob/master/API.md#audioonly) property to play audio files. The `react-native-video` package offers native controls for playing and pausing by default.

```jsx
<Video 
    audioOnly
    post={require('appt.png')} 
    source={require('appt.mp3')} />
```

## Xamarin

In Xamarin apps you should always be able to control audio. You can use [`MediaElement`](https://docs.microsoft.com/en-us/xamarin/community-toolkit/views/mediaelement) to embed media. The `ShowsPlaybackControls` needs to be set to `True` to show controls for playing and pausing. The value is `False` by default.

```xml
<MediaElement Source="https://appt.org/video.mp4"
              ShowsPlaybackControls="True" />
```
