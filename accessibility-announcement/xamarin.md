# Accessibility announcement - Xamarin

Xamarin Forms does not have built-in support for changing accessibility focus.

The [`SemanticExtensions`](https://github.com/xamarin/XamarinCommunityToolkit/blob/main/src/CommunityToolkit/Xamarin.CommunityToolkit/Extensions/Semantic/SemanticExtensions.shared.cs) file inside the [`Xamarin.CommunityToolkit`](https://github.com/xamarin/XamarinCommunityToolkit) contains the `Announce` method. It posts an accessibility announcement on the native platform.

```csharp
SemanticExtensions.Announce("Appt announcement");
```
