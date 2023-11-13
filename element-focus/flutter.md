# Element focus change - Flutter

In Flutter, you can use [`FocusNode`](https://api.flutter.dev/flutter/widgets/FocusNode-class.html) to listen to focus changes. The [`flutter_hooks`](https://pub.dev/packages/flutter_hooks) package includes a method named [`useFocusNode`](https://pub.dev/documentation/flutter_hooks/latest/flutter_hooks/useFocusNode.html) which makes it easier to listen to to focus changes.

Be careful when using the `FocusNode` listener: do not trigger any context change because they might confuse users.

```dart
import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';

class FocusWidget extends HookWidget {
    @override
    Widget build(BuildContext context) {
        final focusNode = useFocusNode();
        useEffect(() {
            focusNode.addListener(() {
                // Do not change context
            });
            return;
        }, [focusNode]);

        return TextField(focusNode: focusNode);
    }
}
```
