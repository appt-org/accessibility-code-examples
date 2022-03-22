# A11YEffect - Xamarin implementation

Met Effects is het mogelijk om bestaande elementen "uit te breiden". Hieronder zie je een voorbeeld van een effect dat wordt gebruikt om toegankelijkheidsfuncties (A11Y) toe te voegen aan Xamarin Forms.

```csharp
using Project.Common.Constants;
using System.Linq;
using Xamarin.Forms;

namespace Project.Common.Effects
{
    public class A11YEffect : RoutingEffect
    {
        public static readonly BindableProperty ControlTypeProperty = BindableProperty.CreateAttached("ControlType", typeof(A11YControlTypes), typeof(A11YEffect), A11YControlTypes.None, propertyChanged: ControlTypePropertyChanged);

        private static void ControlTypePropertyChanged(BindableObject bindable, object oldValue, object newValue)
        {
            if (!(bindable is View view))
                return;

            var oldControlType = (A11YControlTypes)oldValue;
            var newControlType = (A11YControlTypes)newValue;

            if (oldControlType != newControlType)
            {
                if (newControlType != A11YControlTypes.None)
                {
                    view.Effects.Add(new A11YEffect());
                }
                else
                {
                    var toRemove = view.Effects.FirstOrDefault(e => e is A11YEffect && GetControlType(view) == oldControlType);
                    if (toRemove != null)
                        view.Effects.Remove(toRemove);
                }
            }
        }

        public static A11YControlTypes GetControlType(BindableObject view) => (A11YControlTypes)view?.GetValue(ControlTypeProperty);
        public static void SetControlType(BindableObject view, A11YControlTypes value) => view?.SetValue(ControlTypeProperty, value);

        public A11YEffect() : base($"{AppConfigConstants.A11YEffectGroupName}.{nameof(A11YEffect)}")
        {
        }
    }
}
```

Daarnaast moet er een enum worden gedefinieerd met de A11YControlTypes:

```csharp
using System;
namespace Project.Common.Effects
{
    [Flags]
    public enum A11YControlTypes
    {
        None = 0,
        Button = 1,
        Toggle = 2,
        Link = 4,
        Header = 8,
        LiveUpdate = 16,
        MenuItem = 32
    }
}
```

Example of a group name:

```csharp
public const string A11YEffectGroupName = "Project.A11Y.Effect";
```

In the platform specific files you can find the Android and iOS implementation:

* [A11YEffect on Android](./A11YEffect_Android.md)
* [A11YEffect on iOS](./A11YEffect_iOS.md)
