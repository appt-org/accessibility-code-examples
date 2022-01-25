Onderstaand interface maakt het mogelijk om generiek, platform specifiek code uit te voeren:

Voorbeeld:

``` csharp
    if (DependencyService.Get<IA11YService>().IsInVoiceOverMode())
        DependencyService.Get<IA11YService>().Speak("tekst", 500);
```


``` csharp
using System.Threading.Tasks;
using Xamarin.Forms;

namespace Project.Common.Services
{
    public interface IA11YServicee
    {
        // Staat VoiceOver(iOS) of Talkback (Android) aan
        bool IsInVoiceOverMode();
        // Meegegeven 'text' wordt uitgesproken na de meegegeven pauze ('pauseInMs')
        Task Speak(string text, int pauseInMs = 0);
        // Het systeem op de hoogte stellen dat er een nieuwe pagina getoond wordt
        void NotifyForNewPage();
        // Probeer de focus op meegegeven 'visualElement' te zetten
        void ChangeA11YFocus(VisualElement visualElement);
    }
}
```

Runtime wordt dan de platformspecifieke code aangeroepen:

# Android
Zie [Android implementatie](./A11YService_Android.md)

# iOS
Zie [iOS implementatie](./A11YService_iOS.md)