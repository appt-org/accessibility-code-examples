# A11YService - iOS implementation
## Xamarin

You can find the iOS implementation of A11YService below:

```csharp
// TODO: Add required imports
[assembly: Dependency(typeof(A11YService))]
namespace Project.iOS.Services
{
    public class A11YService : IA11YService
    {
        public void ChangeA11YFocus(VisualElement visualElement)
        {
            if (!UIAccessibility.IsVoiceOverRunning || visualElement == null)
                return;
            
            var nativeView = visualElement.GetViewForAccessibility();
            if (nativeView != null)
                UIAccessibility.PostNotification(UIAccessibilityPostNotification.LayoutChanged, nativeView);

        }

        public bool IsInVoiceOverMode()
        {
            return UIAccessibility.IsVoiceOverRunning;
        }

        public void NotifyForNewPage()
        {
            if (UIAccessibility.IsVoiceOverRunning)
            {
                UIKit.UIAccessibility.PostNotification(UIKit.UIAccessibilityPostNotification.ScreenChanged, null);
            }
        }

        public async Task Speak(string text, int pauseInMs = 0)
        {
            if (UIAccessibility.IsVoiceOverRunning && !string.IsNullOrEmpty(text))
            {
                if (pauseInMs > 0)
                    await Task.Delay(pauseInMs);

                UIAccessibility.PostNotification(UIAccessibilityPostNotification.Announcement, Foundation.NSObject.FromObject(text.StripHtml()));
            }
        }
    }
}

The above code depends on the `GetViewForAccessibility()` iOS extension on `Xamarin.Forms.VisualElement`:

```csharp
using UIKit;
using Xamarin.Forms;
using Xamarin.Forms.Platform.iOS;

namespace Project.iOS.Extensions
{
    public static class Extensions
    {
        public static UIView GetViewForAccessibility(this VisualElement visualElement)
        {
            return Platform.GetRenderer(visualElement)?.NativeView ?? Platform.CreateRenderer(visualElement)?.NativeView;
        }
    }
}
```

See also [AutomationProperties](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties)
