# Audio description - Android

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
