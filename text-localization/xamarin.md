# Localization - Xamarin

With Xamarin, you can use [`CultureInfo`](https://docs.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo?view=net-6.0) to set a language. For more information, see [String and Image localization in Xamarin Forms](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/localization/text?pivots=windows).

```csharp
using System.Globalization;
using System.Threading;

CultureInfo ci = CultureInfo.GetCultureInfo(DependencyService.Get<IGeneralPreferences>().Language);

CultureInfo.DefaultThreadCurrentCulture = ci;
CultureInfo.DefaultThreadCurrentUICulture = ci;
AppResources.Culture = ci;
CultureInfo.CurrentUICulture = ci;
Thread.CurrentThread.CurrentUICulture = ci;
Thread.CurrentThread.CurrentCulture = ci;
```
