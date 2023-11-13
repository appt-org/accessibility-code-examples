# Live captions - Android

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
