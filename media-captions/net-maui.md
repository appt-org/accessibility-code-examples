# Captions - .NET MAUI

In .NET MAUI, you can use [`MediaElement`](https://docs.microsoft.com/en-us/xamarin/community-toolkit/views/mediaelement) to embed videos. Unfortunately, there is no built-in support to add captions.

```xml
<toolkit:MediaElement
    x:Name="mediaElement"
    WidthRequest="400"
    HeightRequest="300"
    ShouldLoopPlayback="True"
    Source="embed://videos/appt.mp4"/>

<Button  
    x:Name="mediaButton"
    Text="Click me"
    SemanticProperties.Hint="Pauses or resumes the video"
    Clicked="OnMediaButtonClicked"
    HorizontalOptions="Center" />
```

If you name the MediaElement, e.g. `x:Name="mediaElement"`, you can pause and play the video using code.

```csharp
private void OnMediaButtonClicked(object sender, EventArgs e)
{
  if (mediaElement.CurrentState == CommunityToolkit.Maui.Core.Primitives.MediaElementState.Paused)
    mediaElement.Play();
  else
    mediaElement.Pause();
  SetButtonSemantics();
}

private void SetButtonSemantics()
{
  var description = mediaElement.CurrentState == CommunityToolkit.Maui.Core.Primitives.MediaElementState.Paused ? "Resume video" : "Pause video";
  SemanticProperties.SetDescription(mediaButton, description);
  SemanticScreenReader.Announce(description);
}
```
