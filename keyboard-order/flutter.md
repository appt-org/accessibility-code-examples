# Keyboard order - Flutter

In Flutter, you can use [`FocusTraversalGroup`](https://api.flutter.dev/flutter/widgets/FocusTraversalGroup-class.html)  to group widgets together. All subwidgets must be fully traversed before the keyboard focus is moved to the next widget. When grouping widgets into related groups is not enough, a [`FocusTraversalPolicy`](https://api.flutter.dev/flutter/widgets/FocusTraversalPolicy-class.html) can be set to determine the ordering within the group.

The default [`ReadingOrderTraversalPolicy`](https://api.flutter.dev/flutter/widgets/ReadingOrderTraversalPolicy-class.html) is usually sufficient, but in cases where more control over ordering is needed, an [`OrderedTraversalPolicy`](https://api.flutter.dev/flutter/widgets/OrderedTraversalPolicy-class.html) can be used. The `order` argument of the [`FocusTraversalOrder`](https://api.flutter.dev/flutter/widgets/FocusTraversalOrder-class.html) widget wrapped around the focusable components determines the order. The order can be any subclass of [`FocusOrder`](https://api.flutter.dev/flutter/widgets/FocusOrder-class.html), but [`NumericFocusOrder`](https://api.flutter.dev/flutter/widgets/NumericFocusOrder-class.html) and [`LexicalFocusOrder`](https://api.flutter.dev/flutter/widgets/LexicalFocusOrder-class.html) are provided.

Read more about [Flutter's keyboard focus system](https://docs.flutter.dev/development/ui/advanced/focus).

The example below shows how to use the `FocusTraversalOrder` widget to traverse a row of buttons in the order TWO, ONE, THREE using `NumericFocusOrder`.

```dart
Row(
    children: <Widget>[
        FocusTraversalOrder(
            order: NumericFocusOrder(2.0),
            child: TextButton(
                child: const Text('ONE'),
            ),
        ),
        const Spacer(),
        FocusTraversalOrder(
            order: NumericFocusOrder(1.0),
            child: TextButton(
                child: const Text('TWO'),
            ),
        ),
        const Spacer(),
        FocusTraversalOrder(
            order: NumericFocusOrder(3.0),
            child: TextButton(
                child: const Text('THREE'),
            ),
        ),
    ],
);
```
