# OrientationExtension

```csharp
using System;
using Project.Common.Enums;
using Xamarin.Essentials;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace Project.Common.Markup
{
    public abstract class OrientationExtension<T> : IMarkupExtension
    {
        // If the properties are optional then the variables of type T have to be nullable.
        public T Landscape { get; set; }
        public T Portrait { get; set; }

        public virtual object ProvideValue(IServiceProvider serviceProvider)
        {
            // Get the service for checking the target object and target property
            var provideValueTarget = serviceProvider.GetService<IProvideValueTarget>();

            if (provideValueTarget.TargetObject is BindableObject targetObject &&
                provideValueTarget.TargetProperty is BindableProperty targetProperty)
            {
                // If the target object and target property is bound to this extension and the screen orientation did change.
                DeviceDisplay.MainDisplayInfoChanged += (s, e) => {
                    var value = GetValue();

                    // Write the value associated with the new orientation to the bounded markup extension
                    targetObject.SetValue(targetProperty, value);
                };
            }
            var value = GetValue();
            return value;
        }

        protected T GetValue() => DeviceDisplay.MainDisplayInfo.Orientation == DisplayOrientation.Landscape ?
            Landscape :
            Portrait;
    }

    public class StackOrientationExtension : OrientationExtension<StackOrientation> { }
    public class ThicknessOrientationExtension : OrientationExtension<Thickness> { }
    public class ChunkSizeOrientationExtension : OrientationExtension<int> { }
    public class ChunkOrientationOrientationExtension : OrientationExtension<ChunkOrientationEnum> { }
    public class DoubleOrientationExtension : OrientationExtension<double?> { }
    public class IntOrientationExtension : OrientationExtension<int> { }
    public class GridColumnOrientationExtension : OrientationExtension<int?> { }
    public class GridRowOrientationExtension : OrientationExtension<int?> { }
    public class ColorOrientationExtension : OrientationExtension<Color> { }
    public class BooleanOrientationExtension : OrientationExtension<bool> { }
    public class LayoutOptionsOrientationExtension : OrientationExtension<LayoutOptions> { }
}
```
