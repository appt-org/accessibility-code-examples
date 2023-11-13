# Accessibility order - Flutter

For sorting the focus order in Flutter apps, the `sortKey` parameter of [`Semantics`](https://api.flutter.dev/flutter/semantics/SemanticsProperties-class.html) is used.

This parameter uses a [`SemanticsSortKey`](https://api.flutter.dev/flutter/semantics/SemanticsSortKey-class.html) to sort the elements. The most common way to sort elements is the [`OrdinalSortKey`](https://api.flutter.dev/flutter/semantics/OrdinalSortKey-class.html), but you can also write your own implementation based on the `SemanticsSortKey` class.

The `OrdinalSortKey` needs an `order` as double and optionally a `name` as String. The elements are then sorted by name, with empty names handled first, and subsequently by `order`.

It is also possible to leave out the `sortKey`. In this case, Flutter will generate `OrdinalSortKey`'s based on a platform specific algorithm. This order is often the order you want, but make sure to verify the sequence by using an assistive technology such as the screen reader.

```dart
Widget focusOrderWidget(context) {
    return Scaffold(
        body: Center(
            child: Column(
                mainAxisSize: MainAxisSize.min,
                children: <Widget>[
                    Semantics(
                        sortKey: OrdinalSortKey(2.0),
                        child: Text("Second focus")
                    ),
                    Semantics(
                        sortKey: OrdinalSortKey(1.0),
                        child: Text("First focus")
                    )
                ],
            )
        )
    );
}
```
