Het is mogelijk om bijvoorbeeld door middel van Effects bestaande elementent "uit te breiden".

Hieronder een voorbeeld van een effect die gebruikt wordt om A11Y elementen die ontbreken in standaard Xamarin Forms elementen toe te voegen.

### <a id="A11YEffect"></a> A11YEffect
```c#
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

### <a id="A11YControlTypes"></a> A11YControlTypes
```c#
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

Een voorbeeld voor een groepsnaam:

```c#
        public const string A11YEffectGroupName = "Project.A11Y.Effect";
```

In de platform specifieke projecten (iOS en Android) worden bovenstaand effect verder uitgewerkt:

Android: [implementatie in Android](./A11yEffect_Android.md)

iOS: [implementatie in iOS](./A11yEffect_iOS.md)
