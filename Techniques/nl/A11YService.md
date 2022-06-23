# A11YService - Xamarin implementation
## Xamarin

Deze interface maakt het mogelijk om methoden van platformspecifieke toegankelijkheidsservices uit te voeren.

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

Voorbeeld van detecteren van schermlezer en aankondigingstekst:

```csharp
if (DependencyService.Get<IA11YService>().IsInVoiceOverMode())
    DependencyService.Get<IA11YService>().Speak("Appt", 500);
```

In de platformspecifieke bestanden vind je de implementatie voor Android en iOS:

* [A11YService op Android](./A11YService_Android.md)
* [A11YService op iOS](./A11YService_iOS.md)
