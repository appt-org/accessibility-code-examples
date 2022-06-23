# A11YService - Xamarin implementation
## Xamarin

This interface makes it possible to execute methods of platform specific accessibility services.

```csharp
using System.Threading.Tasks;
using Xamarin.Forms;

namespace Project.Common.Services
{
    public interface IA11YService
    {
        // Check if VoiceOver (iOS) or TalkBack (Android) is on
        bool IsInVoiceOverMode();
        // Announces the given text after the given delay in milliseconds
        Task Speak(string text, int pauseInMs = 0);
        // Notifies the system that a new page is displayed
        void NotifyForNewPage();
        // Attempts to move the focus to the given visual element
        void ChangeA11YFocus(VisualElement visualElement);
    }
}
```

Example of detecting screen reader and announcing text:

```csharp
if (DependencyService.Get<IA11YService>().IsInVoiceOverMode())
    DependencyService.Get<IA11YService>().Speak("Appt", 500);
```

In the platform specific files you can find the Android and iOS implementation:

* [A11YService on Android](./A11YService_Android.md)
* [A11YService on iOS](./A11YService_iOS.md)
