# Screen orientation - Xamarin

When using Xamarin.Forms, [device orientation](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/layouts/device-orientation) is set at the project level.

- For Android: open `MainActivity.cs` and decorate the `MainActivity` class with `[Activity (ScreenOrientation = ScreenOrientation.FullUser)]`.
- For iOS: open `Info.plist` and check all `Device Orientation` checkboxes.

You can listen to orientation changes by using the [`DeviceDisplay`](https://learn.microsoft.com/en-us/xamarin/essentials/device-display?context=xamarin%2Fxamarin-forms&tabs=android) class included in [Xamarin.Essentials](https://learn.microsoft.com/en-us/xamarin/essentials/).

```csharp
public class OrientationChanges
{
    public OrientationChanges()
    {
        // Subscribe to changes of screen metrics
        DeviceDisplay.MainDisplayInfoChanged += OnMainDisplayInfoChanged;
    }

    void OnMainDisplayInfoChanged(object sender, DisplayInfoChangedEventArgs  e)
    {
        // Process changes
        var displayInfo = e.DisplayInfo;
    }
}
```
