# Audio control - Android

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
