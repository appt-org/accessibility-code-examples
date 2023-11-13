# Audio description - iOS

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
