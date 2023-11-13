# Element identification - Android

In Android, you should create custom `Views` to re-use functionality on multiple screens.

When using icons, use the search function of your `IDE` to check all instances. The icon should have the same `accessibility label` on each screen, and the functionality should also be the same.

For example, when using a cross icon for closing a screen, make sure the label is 'Close' on all screens, and check that it always closes a screen.

In Android Studio, you can use the `Find Usages` option to check if resources are used on multiple screens. Go to your `drawable` folder, right click and select the `Find Usages` option. You can also use the shortcut `Option + F7` on Mac, or `Alt + F7` on Windows.

```kotlin
Not available, contribute!
```
