# iOS
Hieronder de iOS implementatie van bovenstaand interface:

``` csharp
// de benodigde "using"s weggelaten
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

```

Hierboven wordt gebruik gemaakt van 

``` csharp
    var nativeView = visualElement.GetViewForAccessibility();
```

dit is Extension op Xamarin.Forms.VisualElement, hieronder de code:

``` csharp
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