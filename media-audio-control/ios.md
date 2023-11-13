# Audio control - iOS

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
