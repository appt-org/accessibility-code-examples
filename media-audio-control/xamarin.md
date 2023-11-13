# Audio control - Xamarin

In Xamarin apps you should always be able to control audio. You can use [`MediaElement`](https://docs.microsoft.com/en-us/xamarin/community-toolkit/views/mediaelement) to embed media. The `ShowsPlaybackControls` needs to be set to `True` to show controls for playing and pausing. The value is `False` by default.

```xml
<MediaElement Source="https://appt.org/video.mp4"
              ShowsPlaybackControls="True" />
```
