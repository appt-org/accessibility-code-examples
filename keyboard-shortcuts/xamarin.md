# Keyboard shortcuts - Xamarin

Xamarin does not have support for hardware keyboard events. However, you can intercept key events inside the Android and iOS application.

- Android: hook into [`onKeyUp`](https://learn.microsoft.com/en-us/dotnet/api/android.app.activity.onkeyup?view=xamarin-android-sdk-12) inside `MainActivity.cs`
- iOS: hook into [`KeyCommands`](https://learn.microsoft.com/en-us/dotnet/api/uikit.uiresponder.keycommands?view=xamarin-ios-sdk-12) using a [custom renderer](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/custom-renderer/contentpage).

The code example below shows a sample implementation for iOS.

```csharp
[assembly: ExportRenderer(typeof(ContentPage), typeof(KeyboardPageRenderer))]
namespace KeyCommandsInXamarinForms.iOS
{
    public class KeyboardPageRenderer : PageRenderer
    {
        protected override void OnElementChanged(VisualElementChangedEventArgs e)
        {
            base.OnElementChanged(e);

            if (e.OldElement != null || Element == null)
            {
                return;
            }

            // Create key command for Command + F
            UIKeyCommand command1 = UIKeyCommand.Create(
                new NSString("F"), 
                UIKeyModifierFlags.Command, 
                new ObjCRuntime.Selector("OnKeyPressed:")
            );

            this.AddKeyCommand(command1);
        }

        [Export("OnKeyPressed:")]
        private void Excute(UIKeyCommand keyCommand)
        {
            // Find
        }

        public override bool CanBecomeFirstResponder
        {
            get
            {
                return true; // Key commands require first responder
            }
        }
    }
}
```

The code example below shows a sample implementation for Android.

```csharp
public override bool OnKeyUp([GeneratedEnum] Keycode keyCode, KeyEvent e)
{
    if (keyCode == Keycode.KEYCODE_F && e.isCtrlPressed)
    {
        // Search
        return true
    }

    return base.OnKeyUp(keyCode, e);
}
```
