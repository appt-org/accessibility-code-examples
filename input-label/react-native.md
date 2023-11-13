# Input label - React Native

In React Native, there is no attribute to link a label to an input field. We recommend combining [`Text`](https://reactnative.dev/docs/text) with a [`TextInput`](https://reactnative.dev/docs/textinput) component.

You can also use a package for displaying instructions, such as [React Native Paper](https://callstack.github.io/react-native-paper/index.html). This package includes a [`TextInput`](https://callstack.github.io/react-native-paper/docs/components/TextInput/) component with a `label` property.

```jsx
import { TextInput } from 'react-native-paper';

const InputWithLabelComponent = () => {
  return (
    <TextInput
      label="Name"
      value={name}
    />
  );
};
```
