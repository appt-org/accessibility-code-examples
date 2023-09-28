# Element focus change

Whenever an element receives focus, it should not automatically trigger an event which changes `context`. Example of changing context include, but are not limited to: automatically submitting data, opening a new screen or moving to another element. Focus should only be moved deliberately by the user.
